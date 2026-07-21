---
type: overview
title: "Making Of - How This Knowledge Base Was Built"
description: "The full pipeline, tooling, and validation results behind this bundle: how 198 video transcripts became a synthesized, cited, cross-linked OKF wiki."
tags: [meta, methodology, reproducible]
updated: 2026-07-21
---

# Making Of

How 198 long-form YouTube videos became this knowledge base: the pipeline, the architecture decisions, the tooling, and the validation results. Everything here is reproducible from the scripts in [`../tools/`](../tools).

The whole thing was built by AI agents orchestrated in **Claude Code Workflows** (JavaScript scripts that fan out subagents with real control flow), with human review at each checkpoint. Roughly 700 agent runs across 8 workflows.

## The core problem: synthesis, not accretion

The naive way to build a knowledge base from 198 transcripts is one page per video. That produces a transcript archive, not a wiki. The interesting knowledge is *cross-cutting*: the PIV loop appears in 20+ videos, RAG in 40+. A useful page for "the PIV loop" synthesizes every video that discusses it.

That creates a hard engineering constraint. If you process videos in parallel with independent agents, each one invents its own page for the same idea (`piv-loop`, `the-piv-loop`, `plan-implement-validate`) and you get duplicates with divergent content. If you process them sequentially so each agent can see the growing wiki, the build takes forever and later agents drown in context.

**The fix is a two-pass architecture with a canonicalization barrier in the middle.**

## The pipeline

![The build pipeline](pipeline.png)


```
[1] SOURCE          198 transcripts + publish dates -> raw/*.md (immutable, timestamped)
         |
[2] EXTRACT         198 agents in parallel, one per transcript
         |          -> candidate concepts/entities + timestamped quotes (JSON, no prose)
         |
[3] CANONICALIZE    aggregate -> cluster -> per-cluster dedup -> cross-cluster merge
         |          -> FROZEN manifest.json + taxonomy.json  (the contract)
         |
[4] WRITE           ~70 agents in parallel against the frozen manifest
         |          -> concepts/, entities/, sources/ pages, cross-linked
         |
[5] POLISH          ASR proper-noun normalization + typed Related sections
         |
[6] VALIDATE        lint + audit + citation integrity + dedup + QA + recall
         |
[7] GAP SWEEP       detect uncovered durable ideas -> notability triage -> fill
```

### [1] Source: transcripts without touching YouTube

Transcripts came from the production database of Cole's AI Tutor app, which already syncs the full channel daily. Full text lives in a `videos.transcript` column; per-chunk `start_seconds` let us reconstruct **timestamped** transcripts (196 of 198; two videos had no chunk rows and got a paragraph-only fallback).

The database has no publish dates, so those were enriched separately from each watch page's `datePublished` microformat (keyless). Output: `raw/<slug>.md`, marked `immutable: true`, plus `raw/manifest.json`.

Tooling: [`../tools/export_transcripts.py`](../tools/export_transcripts.py)

> If you are rebuilding this from scratch without such a database, the equivalent step is `yt-dlp --flat-playlist -J` to enumerate the channel plus a captions pull, or a managed transcript API.

### [2] Extract: mine, do not write

One agent per transcript, all in parallel. Each reads its video and emits **structured JSON only**: candidate concepts and entities, each with a proposed slug, a one-line definition, and 2-3 verbatim timestamped quotes. No prose pages yet.

Agents were seeded with the canonical slugs from an earlier 20-video build so independent agents converge on the same names (`the-piv-loop`, not `plan-implement-validate-loop`).

Result: **785 concept candidates, 340 entity candidates** across 198 videos.

Tooling: [`../tools/workflows/01-extract-canonicalize.mjs`](../tools/workflows/01-extract-canonicalize.mjs)

### [3] Canonicalize: the barrier that makes synthesis work

This is the step that turns a pile of candidates into a wiki:

1. **Aggregate** all extractions, group by normalized slug, count how many distinct videos mention each, and cluster by dominant tag (14 clusters).
2. **Per-cluster dedup** (parallel, one agent per cluster): merge candidates meaning the same thing into one canonical page; apply the page-creation threshold (>=2 videos, or one clearly substantial deep-dive); assign a theme.
3. **Cross-cluster merge** (single agent): resolve duplicates that landed in different clusters, canonicalize entities, gather each page's supporting quotes by walking member candidates back through the extractions, and freeze:
   - `scripts/manifest.json` - every page with its description, related slugs, and per-video quotes.
   - `scripts/taxonomy.json` - theme groupings that drive every `index.md`.

785 candidates collapsed to **186 canonical concepts**. That ~4x compression *is* the synthesis.

### [4] Write: parallel with zero dedup risk

Because slugs, sources, and quotes are frozen, page-writing agents make **no structural decisions**. They fan out (batched at 5-8 pages each) and write prose against the manifest, resolving every link through a precomputed `slug_index.json` of relative paths so no agent can miscompute or invent a link.

Tooling: [`../tools/workflows/02-write-pages.mjs`](../tools/workflows/02-write-pages.mjs)

### [5] Polish

Two passes ([`03-polish.mjs`](../tools/workflows/03-polish.mjs)):

- **ASR normalization.** YouTube auto-captions garble proper nouns ("Enthropic", "pantic Ai", "Lang graph", "canban"). Every authored page was swept against a canonical glossary, correcting names while preserving quote meaning and timestamps exactly. **`raw/` was deliberately left untouched** so verbatim provenance stays auditable.
- **Typed relationships.** Entity `## Related` sections were rewritten into typed subheadings (`## Realizes`, `## Contrasts with`, `## Works with`, `## Related`) with one-line descriptions, matching the concept pages.

### [7] Gap sweep: fixing what validation found

The recall test (below) showed 88% coverage, so a dedicated sweep ran over all 198 videos to find durable ideas with no page: **342 gap mentions** canonicalized into an add-list.

Critically, this add-list was then **notability-triaged** ([`07-notability-triage.mjs`](../tools/workflows/07-notability-triage.mjs)) rather than filled blindly. Of the single-video entity candidates, **30 were rejected** as sponsor reads or obscure micro-tools, because thin pages about things nobody will ask about actively degrade a knowledge base. The surviving **155 pages** were written with cited quotes and reciprocal backlinks.

## Validation: how we know it works

Six independent checks. Anyone can re-run them from a clone.

| Check | What it proves | Result |
|---|---|---|
| [`lint.py`](../lint.py) | OKF conformance, link integrity, index coverage, source/raw parity, orphans | **0 errors, 0 warnings** (1,050+ files) |
| [`audit.py`](../tools/validation/audit.py) | Per-type frontmatter completeness, `videos:` cross-refs, thin pages, duplicate titles, taxonomy consistency | **0 problems** |
| [`citation_integrity.py`](../tools/validation/citation_integrity.py) | Every quote actually appears in the transcript it cites, near the timestamp it claims | **99%** verified (2,562 / 2,567) |
| [`semantic_dedup.py`](../tools/validation/semantic_dedup.py) | No two pages are near-copies (local embeddings, cosine >= 0.86) | **0 duplicate pairs** |
| [`04-qa-answerability.mjs`](../tools/workflows/04-qa-answerability.mjs) | 40 questions answered by navigation, then independently judged | **30/30** answerable, **10/10** traps declined, **0 hallucinations** |
| [`05-recall-coverage.mjs`](../tools/workflows/05-recall-coverage.mjs) | Do videos' core ideas actually have pages? | **88%** pre-sweep, gaps then closed |

The two most valuable checks are the last-listed ones, because they test things lint cannot:

- **Citation integrity** is the antidote to the biggest risk in an LLM-built knowledge base: confident, fabricated quotes. Extracting all 2,567 quotes and diffing them against the raw transcripts at their claimed timestamps proves the provenance is real.
- **Adversarial QA** included 10 deliberately out-of-scope questions ("What did Cole say about Claude 5 Opus?", "Which crypto token did he launch?"). A knowledge base that answers those is worse than useless. This one declined all 10.

## Lessons worth stealing

1. **Put a barrier where the duplication risk is.** Everything else fans out; only canonicalization is serial. Parallelism is safe once the contract is frozen.
2. **Separate structure from prose.** Agents that decide *what pages exist* should not also write them. Freezing the manifest first removes a whole class of divergence bugs.
3. **Precompute link targets.** Handing writers a resolved path index eliminates broken links by construction rather than catching them in review.
4. **Test recall, not just precision.** "Can it answer X?" and "is anything missing?" are different questions, and the second one is the one that found 155 pages of real gaps.
5. **Curate the gap list.** The sweep proposed 185 pages; 30 were noise. More pages is not better; more *answerable questions* is better.
6. **Keep the raw layer immutable.** Polishing the synthesized layer while preserving verbatim transcripts means you get readable pages and auditable provenance.

## Refreshing this bundle

New videos land in the source database automatically. Adding them is incremental, not a rebuild, because the canonical taxonomy already exists: produce the new `raw/` files, ingest per [`ingestion-workflow.md`](ingestion-workflow.md) (extend existing pages, create pages only for genuinely new link-worthy ideas), then `python scripts/build_indexes.py` and `python lint.py`.
