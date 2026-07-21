---
type: overview
title: "Cole Medin AI Knowledge Base"
description: "An Open Knowledge Format (OKF) wiki mined from Cole Medin's entire long-form YouTube catalog, built to be dropped next to any project as agent-ready reference."
tags: [readme, overview]
updated: 2026-07-21
---

# Cole Medin - AI Knowledge Base

A synthesized, densely cross-linked knowledge base mined from [Cole Medin's](https://www.youtube.com/@ColeMedin) **entire long-form YouTube catalog** - agentic coding, AI engineering, RAG, harnesses, memory systems, and more. It is an [Open Knowledge Format](https://github.com/GoogleCloudPlatform/knowledge-catalog) (OKF v0.1) bundle and a Karpathy-style [LLM wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f): plain markdown + YAML frontmatter, navigated by index and relative links, no database and no embeddings required.

**The point:** drop this folder next to your project and any coding agent can answer questions from Cole's videos with citations back to the exact video and timestamp - zero integration, no RAG stack, no API keys.

## What's inside

- **`concepts/`** - the ideas, techniques, patterns, and mental models (the PIV loop, context engineering, agentic search, and so on), each synthesizing every video that discusses it.
- **`entities/`** - the tools, people, and organizations (Claude Code, Archon, MCP, Anthropic, …).
- **`sources/`** - one summary page per video, with provenance to the raw transcript.
- **`raw/`** - the immutable, timestamped transcripts (the source of truth).
- **`index.md`** - start here (after `SCHEMA.md`). The compiled wiki *is* the search index.

## Use it with an agent (copy-paste)

Point your coding agent at this bundle with a prompt like:

```
Use the Cole Medin AI Knowledge Base as a reference:

1. Clone it next to my project (skip if I already have it):
   git clone https://github.com/coleam00/cole-medin-knowledge-base.git

2. Read `cole-medin-knowledge-base/index.md`, then `cole-medin-knowledge-base/SCHEMA.md`.
   This is an Open Knowledge Format (OKF) bundle - a linked wiki of concepts and entities
   mined from Cole Medin's videos. Navigate it the OKF way: read the index, follow the
   relative links into `concepts/`, `entities/`, and `sources/`, and open only the pages a
   question needs. Do not load the whole folder.

3. When I ask a question, answer from the knowledge base and cite the concept/entity pages
   you used and the source video(s) they came from (each page ends with a `## Sources`
   section listing the videos and timestamps). If something is not covered, tell me instead
   of guessing.
```

## How it was built (reproducible)

1. **Source.** Full transcripts for every long-form video are pulled from the source database and written as immutable `raw/<slug>.md` files (timestamped), plus `raw/manifest.json`.
2. **Extract.** Each transcript is mined for the concepts and entities it teaches, with timestamped quotes.
3. **Canonicalize.** All candidates are deduplicated into one taxonomy so each durable idea is a single page synthesizing every video that covers it (synthesis, not one-page-per-video).
4. **Write & link.** Concept/entity/source pages are written and cross-linked with typed relationship headings.
5. **Validate.** `python scripts/build_indexes.py` regenerates the indexes; `python lint.py` gates conformance, link integrity, index coverage, and orphans.

See [`SCHEMA.md`](SCHEMA.md) for the full contract and [`docs/ingestion-workflow.md`](docs/ingestion-workflow.md) for the step-by-step. Coverage and growth model are in [`roadmap.md`](roadmap.md).

## License / provenance

Knowledge is synthesized from publicly available YouTube videos by Cole Medin; each page cites its sources. Raw transcripts are included under `raw/` for provenance and auditability.
