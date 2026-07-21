---
type: overview
title: "Build & Validation Tooling"
description: "The workflow scripts and validators that built and verified this knowledge base, kept in-repo so the process is reproducible and auditable."
tags: [meta, tooling, reproducible]
updated: 2026-07-21
---

# Build & Validation Tooling

The actual scripts behind this bundle. See [`../docs/MAKING-OF.md`](../docs/MAKING-OF.md) for the narrative and the validation results.

These are kept in-repo for transparency and reuse, not as a turnkey CLI: the workflows were run with [Claude Code](https://claude.com/claude-code)'s Workflow tool (JavaScript scripts that orchestrate subagents), and they assume this bundle's layout. Treat them as a reference implementation of the two-pass build.

## `workflows/` - the build (run in order)

| Script | Phase | What it does |
|---|---|---|
| `01-extract-canonicalize.mjs` | Extract + Canonicalize | One agent per transcript mines candidate concepts/entities with timestamped quotes; then aggregate, cluster, dedup per cluster, and cross-merge into the frozen `manifest.json` + `taxonomy.json`. |
| `02-write-pages.mjs` | Write | Splits the manifest into per-page specs plus a precomputed relative-link index, then writes all source/concept/entity pages in parallel. |
| `03-polish.mjs` | Polish | Normalizes ASR proper-noun errors across authored pages; rewrites entity `## Related` into typed subheadings with descriptions. |
| `04-qa-answerability.mjs` | Validate | Answers 30 real + 10 out-of-scope questions by navigating the bundle, then independently judges each answer against the cited pages. |
| `05-recall-coverage.mjs` | Validate | Samples videos, extracts their core ideas, and checks whether each durable idea has a page. |
| `06-gap-detect.mjs` | Gap sweep | Scans every video for durable ideas lacking a page; canonicalizes mentions into an add-list. |
| `07-notability-triage.mjs` | Gap sweep | Rubric-scores single-video candidates KEEP/DROP so sponsor reads and micro-tools never become pages. |
| `08-gap-fill.mjs` | Gap sweep | Writes the approved new pages with cited quotes and wires reciprocal backlinks. |

## `validation/` - the checks (plain Python, run anytime)

```bash
python ../lint.py                          # OKF conformance, links, index coverage, orphans
python validation/audit.py                 # frontmatter completeness, thin pages, dup titles, taxonomy consistency
python validation/citation_integrity.py    # every quote vs the transcript + timestamp it cites
python validation/sweep.py                 # agent-artifact leakage, encoding gremlins, link-graph health
python validation/semantic_dedup.py        # near-duplicate pages via local embeddings (needs fastembed + numpy)
```

`lint.py` and the first three validators are stdlib-only. `semantic_dedup.py` needs a local embedding model and expects to import an `embeddings` module providing `embed_batch`; swap in any embedder.

## `export_transcripts.py`

Pulls full transcripts from the source database, reconstructs timestamps from per-chunk offsets, enriches publish dates, and writes the immutable `raw/<slug>.md` files plus `raw/manifest.json`. Specific to the AI Tutor database schema; adapt the query for your own source, or replace this step with `yt-dlp` captions.
