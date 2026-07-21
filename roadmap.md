---
type: overview
title: "Roadmap & Coverage"
description: "What this knowledge base covers, what is intentionally out of scope, and how it grows over time."
tags: [meta, roadmap, coverage]
updated: 2026-07-21
---

# Roadmap & Coverage

## Coverage

This bundle covers Cole Medin's **entire long-form YouTube catalog** as of the last build. Exact counts are in [`raw/manifest.json`](raw/index.md) and the root [`index.md`](index.md) coverage banner.

- **In scope:** every long-form video on the channel (agentic coding, AI engineering, RAG and retrieval, harnesses and workflow engineering, memory / knowledge systems, tooling walkthroughs).
- **Out of scope (by design):** YouTube **Shorts** and **livestreams**. Shorts are too brief to synthesize durable concepts from, and livestreams are long, loosely structured, and largely re-cover material from the edited long-form videos. They can be folded in later if there is demand.

## Source of truth

Transcripts are sourced from the AI Tutor (DynaChat) production database, which enumerates and syncs the full channel daily via Supadata, then written as immutable, timestamped `raw/<slug>.md` files. Publish dates are enriched from the YouTube Data API. Because the source keeps the channel current, refreshing this bundle is an incremental operation (below).

## Growth model

The canonical taxonomy (the set of concept/entity pages and their theme groupings in `scripts/taxonomy.json`) already exists, so adding newly published videos is incremental, not a rebuild:

1. New `raw/<slug>.md` files are produced for videos not yet present.
2. Each new transcript is ingested per [`docs/ingestion-workflow.md`](docs/ingestion-workflow.md): write its `sources/` page, then **extend existing** concept/entity pages (adding the new video under `## Sources`) and create new pages only for genuinely new, link-worthy ideas.
3. `python scripts/build_indexes.py` then `python lint.py`; append to [`log.md`](log.md).

A monthly refresh keeps the bundle current with the channel.

## Non-goals

- Not a transcript search box or a vector database - the compiled wiki is the index.
- Not a per-video blog - knowledge is synthesized across videos, one page per durable idea.
- Not a course or a tutorial - it is a reference graph for agents and humans.
