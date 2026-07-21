---
type: overview
title: "SCHEMA - How This Knowledge Base Is Built"
description: "The maintainer contract: OKF conformance rules, directory layout, page schemas, linking conventions, and the ingestion workflow for this bundle."
tags: [meta, schema, contract]
updated: 2026-07-21
---

# SCHEMA - How This Knowledge Base Is Built

This file is the **contract** every page in this bundle obeys. It is written for the LLM that maintains the wiki (and any human reviewing it). If you are an agent ingesting a transcript or answering a question, **read this first, then `index.md`.**

This bundle is an [Open Knowledge Format](https://github.com/GoogleCloudPlatform/knowledge-catalog) (OKF v0.1) bundle **and** a Karpathy-style [LLM wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f): a synthesized, densely cross-linked graph of concepts and entities mined from [Cole Medin's](entities/people/cole-medin.md) YouTube videos, not raw transcripts. Raw transcripts are kept immutable under `raw/` for provenance; the knowledge lives in `concepts/`, `entities/`, and `sources/`.

## 1. What this bundle is (and is not)

- **Is:** a synthesized knowledge base covering Cole Medin's **entire long-form YouTube catalog** (agentic coding, AI engineering, RAG, harnesses, memory systems, and more). It is optimized **first for an agent** navigating by index + links, and **second for a human** reading top to bottom.
- **Is not:** a transcript dump, a per-video blog, or a vector database. There is no embedding index; **the compiled wiki IS the search index**. An agent reads `index.md`, follows links, and opens only the atomic pages a question needs.
- **Scope:** long-form videos only. Shorts and livestreams are intentionally out of scope. See [roadmap.md](roadmap.md).

## 2. OKF conformance (the hard rules)

Verified against the OKF SPEC (§3.1, §4.1, §5, §9, §11):

1. **Every OKF concept document carries YAML frontmatter with a non-empty `type`.** That is the only strictly required field.
2. **Reserved filenames:** `index.md` (directory listing) and `log.md` (update history). These are the only files that are *not* concept documents and carry no frontmatter, **except** a bundle-root `index.md`, which MAY declare `okf_version`.
3. **A concept's ID is its path within the bundle minus `.md`** (`concepts/the-piv-loop.md` -> `concepts/the-piv-loop`). The path is the identity, so **filenames are stable and never renamed casually.**
4. **Cross-links are ordinary relative markdown links**, never `[[wikilinks]]`. A link asserts an (untyped) directed edge; the *kind* of relationship is carried by the section heading it sits under (see §5).
5. Consumers must tolerate broken links, unknown `type` values, and missing indexes, but **we do not rely on that tolerance**: this bundle aims for zero broken links and full index coverage, enforced by `lint.py`.

**Repository meta vs. OKF concept docs.** `README.md`, `SCHEMA.md`, `roadmap.md`, and `docs/*.md` are documentation; they still carry `type: overview` frontmatter so the whole tree is uniformly conformant. `scripts/*.py`, `lint.py`, and `raw/manifest.json` are tooling, not markdown concept docs.

## 3. Directory layout

```
cole-medin-knowledge-base/
├── index.md            # OKF root catalog (declares okf_version); read first after SCHEMA
├── roadmap.md          # scope + coverage + growth model
├── SCHEMA.md           # this file - the maintainer contract
├── README.md           # human entry point + copy-paste consume prompt
├── log.md              # append-only ingestion history (reserved)
├── lint.py             # conformance + graph-health checker (run before every commit)
├── docs/
│   ├── ingestion-workflow.md   # how one transcript becomes pages (reproducible)
│   └── query-guide.md          # how to ask this bundle questions
├── scripts/
│   ├── build_indexes.py        # regenerate every index.md from the taxonomy + frontmatter
│   └── taxonomy.json           # theme -> slug groupings that drive the indexes
├── concepts/           # ideas, techniques, patterns, mental models
│   ├── index.md
│   └── <concept-id>.md
├── entities/           # nameable things that exist
│   ├── index.md
│   ├── tools/          # tools & products (Claude Code, Archon, MCP, …)
│   ├── people/         # people (Cole Medin, Andrej Karpathy, …)
│   └── organizations/  # orgs (Anthropic, OpenAI, …)
├── sources/            # one synthesized summary page per video (provenance)
│   ├── index.md
│   └── <slug>.md
└── raw/                # immutable timestamped transcripts + manifest.json
    ├── index.md
    └── <slug>.md
```

**Why `entities/` is subdivided but `concepts/` is flat:** entities cleave cleanly into tools/people/orgs (aids the index and disambiguation); concepts do not partition cleanly, so they stay flat and are grouped *thematically in the index* instead of by folder.

## 4. Page types & frontmatter schemas

All dates are ISO `YYYY-MM-DD`. `videos` lists the source slugs that taught the item (provenance).

**Concept** (`concepts/<id>.md`)
```yaml
---
type: concept
title: "The PIV Loop"
description: "One-sentence definition used verbatim in index listings and search snippets."
tags: [workflow, planning, core]
videos: [complete-agentic-coding-workflow, principled-agentic-engineer]
created: 2026-07-21
updated: 2026-07-21
---
```

**Entity** (`entities/{tools,people,organizations}/<id>.md`) - add `resource` for a canonical URL/repo/homepage:
```yaml
---
type: entity
subtype: tool        # tool | person | organization
title: "Claude Code"
description: "Anthropic's terminal-based agentic coding tool; Cole's primary driver."
resource: "https://www.anthropic.com/claude-code"
tags: [coding-agent, anthropic]
videos: [claude-code-hidden-features, claude-code-2000-hours]
created: 2026-07-21
updated: 2026-07-21
---
```

**Source** (`sources/<slug>.md`) - one per video:
```yaml
---
type: source
title: "Why the Best AI Coding Tools Abandoned RAG (And What They Use Instead)"
description: "One-sentence framing of the video's thesis."
youtube_id: 60G93MXT4DI
url: https://www.youtube.com/watch?v=60G93MXT4DI
slug: why-ai-coding-abandoned-rag
published: 2026-05-14
duration: "14:52"
recency_rank: 19
raw: "../raw/why-ai-coding-abandoned-rag.md"
tags: [rag, retrieval]
created: 2026-07-21
updated: 2026-07-21
---
```

**Overview** (`roadmap.md`, `SCHEMA.md`, `README.md`, `docs/*.md`): `type: overview`.

**Raw transcript** (`raw/<slug>.md`): `type: raw-transcript`, `immutable: true` - machine-written from the source database; never hand-edited.

## 5. Linking & typed edges (the load-bearing discipline)

Relationships are what make this a wiki instead of a folder of notes. Rules:

- **Link with relative markdown paths:** from `concepts/x.md` to a tool -> `[Claude Code](../entities/tools/claude-code.md)`; to a sibling concept -> `[Agentic Coding](./agentic-coding.md)`.
- **Type every edge with the heading it lives under.** Because OKF links are untyped, we recover semantics from section headings. Canonical relationship headings:
  - `## Prerequisites` - what you must understand first
  - `## Builds on` / `## Part of` - the parent concept/loop
  - `## Contrasts with` - the thing it is defined against
  - `## Implemented by` / `## Tools` - entities that realize it
  - `## Related` - everything else worth a hop
  - `## Sources` - the `sources/` video pages that taught it (provenance; every page ends with this)
- **Bidirectional:** if page A links to B under a typed heading, B links back to A. `lint.py` reports orphan pages (no inbound links) so this stays honest.
- **Link density is a quality signal.** A concept/entity page with fewer than ~2 outbound links is under-developed. Link liberally.
- **Unresolved links are allowed as intent** but flagged by lint - prefer to create the target stub if a term recurs.

## 6. Atomicity, synthesis, and the page-creation threshold

- **One topic per page, captured in full.** Split a page past ~800-1000 words of distinct subtopics; merge two pages that cover the same thing.
- **Mine, don't mirror.** Never one page per video. Each transcript feeds many pages; each durable concept/entity is **one** page synthesizing *all* the videos that discuss it (each cited under `## Sources`).
- **Page-creation threshold = link-worthiness / reuse.** Give something its own page when it is linked-to from >=2 places or recurs across >=2 videos. Below that bar: a mention or an attribute inside a parent page, not a file.
- **Contradictions are flagged, never silently resolved.** If two videos conflict, add a `> **Contradiction:**` note on both pages citing the two sources and the date; let the reader judge. (Views that *evolve* over time are narrated, not flagged as contradictions.)

## 7. Index conventions

Every directory has an `index.md` - a grouped listing for progressive disclosure. Format per entry:
```markdown
- [Display Name](relative-path.md) - one-line description (copied from the target's frontmatter `description`)
```
Group under `##` headings (concepts by theme; entities by tool/person/org; sources by cluster). The groupings live in `scripts/taxonomy.json` and are applied by `scripts/build_indexes.py` (deterministic, idempotent; anything unlisted lands under "Other" so nothing is silently dropped). The **root `index.md` is the product** - invest in it: it is what an agent reads to decide where to go.

## 8. Ingestion workflow (reproducible)

The full step-by-step lives in [docs/ingestion-workflow.md](docs/ingestion-workflow.md). In brief, for each transcript:
1. The immutable `raw/<slug>.md` is produced from the source database (see roadmap for the source).
2. Read this SCHEMA + `index.md` + the pages the video likely touches (synthesis, not dumping).
3. Write/refresh the `sources/<slug>.md` summary.
4. Create or update the concept/entity pages the video touches; wire typed links both directions.
5. Regenerate indexes (`python scripts/build_indexes.py`), update the root coverage banner, and append to `log.md`.
6. Run `python lint.py` and fix everything it reports.

## 9. Validation

`lint.py` enforces, deterministically:
- every non-reserved `.md` has frontmatter with a non-empty `type`;
- every relative markdown link resolves to a file in the bundle;
- every concept/entity/source page appears in its directory `index.md`;
- every `sources/<slug>.md` has a matching `raw/<slug>.md` and vice-versa;
- no orphan concept/entity pages (each has >=1 inbound link).

Semantic checks (contradictions, staleness, missing concepts) are an LLM pass, not the script.
