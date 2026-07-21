---
type: overview
title: "Ingestion Workflow"
description: "The reproducible process for turning a video transcript into synthesized, cross-linked wiki pages."
tags: [meta, workflow, ingestion]
updated: 2026-07-21
---

# Ingestion Workflow

How one transcript becomes pages. This is the process for both the initial bulk build and incremental refreshes (see [roadmap.md](../roadmap.md)). It obeys [SCHEMA.md](../SCHEMA.md).

## The principle: synthesis, not accretion

Never create one page per video. Each transcript feeds *many* pages, and each durable concept or entity is *one* page that synthesizes **every** video discussing it. The unit of knowledge is the idea, not the video. A video's own page (`sources/<slug>.md`) is a summary + provenance record, not where the knowledge lives.

## The two-pass build (bulk)

Because the bundle is mined from the whole catalog at once, the build runs in two passes so that shared ideas collapse into single canonical pages instead of duplicating per video:

1. **Extract (per video, parallel).** For each `raw/<slug>.md`, mine the concepts and entities it teaches. Emit, per candidate: a proposed slug, a one-line description, 2-3 timestamped supporting quotes, and the typed edges it implies. No prose pages yet.
2. **Canonicalize (once).** Merge all candidates across all videos: deduplicate slugs (the-piv-loop == piv-loop == plan-implement-validate collapse to one), apply the page-creation threshold (>=2 videos or >=2 inbound links), cluster into themes, and freeze the manifest + `scripts/taxonomy.json`. Every page's source videos and quotes are assigned here.
3. **Write (per page, parallel).** With slugs and sources frozen, write each `concepts/`, `entities/`, and `sources/` page against the manifest - no dedup decisions remain, so there is no divergence risk.

## The per-transcript workflow (incremental refresh)

For a single new video once the taxonomy exists:

1. **Raw.** Produce the immutable `raw/<slug>.md` (timestamped, `immutable: true`). Never hand-edit it.
2. **Read before writing.** Read `SCHEMA.md`, the root `index.md`, and the concept/entity pages this video likely touches. Synthesis requires knowing what already exists.
3. **Source page.** Write `sources/<slug>.md`: a 2-3 paragraph synthesized summary (not a dump), then `## Concepts covered`, `## Entities`, `## Key moments` (timestamped), and a `## Transcript` link to the raw file.
4. **Concept/entity pages.** For each idea the video teaches: if a page exists, **extend it** (add the new video under `## Sources` with a timestamped quote, refine the prose); if it clears the threshold and is new, create it.
5. **Link, both directions.** Wire typed edges (`## Prerequisites`, `## Builds on`, `## Contrasts with`, `## Implemented by`, `## Related`, `## Sources`). If A links to B, B links back to A.
6. **Regenerate + validate.** `python scripts/build_indexes.py`, then `python lint.py`. Fix every error; update the root coverage banner; append to `log.md`.

## Quality bar

- Every concept/entity page ends with `## Sources` citing the video(s) and timestamps.
- Prefer a verbatim timestamped quote for the load-bearing claim on a page.
- Link density is a quality signal: a page with fewer than ~2 outbound links is under-developed.
- Contradictions across videos are flagged with a `> **Contradiction:**` note, never silently resolved. Views that evolve over time are narrated instead.
