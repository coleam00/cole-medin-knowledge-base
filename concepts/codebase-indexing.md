---
type: concept
title: "Codebase Indexing"
description: "Building a searchable index or map of a codebase so the agent can retrieve the right files instead of scanning everything."
tags: [indexing, codebase, retrieval]
videos: [anthropic-just-dropped-a-masterclass-on-building-agent-harnesses-for-large-codebases, why-the-best-ai-coding-tools-abandoned-rag-and-what-they-use-instead, the-official-archon-guide-10x-your-ai-coding-workflow, ai-code-that-fixes-itself-an-mcp-you-can-try-now]
created: 2026-07-21
updated: 2026-07-21
---

# Codebase Indexing

Codebase indexing is the practice of pre-processing a repository into a searchable structure (a vector index, a knowledge graph, or a hand-written map) so an agent can jump to the relevant files instead of scanning the whole tree on every task. Its defining weakness is keeping that structure current: "This retrieval pipeline is just another thing we have to maintain with the coding agent and it is a very difficult problem to keep the indexed codebase in sync with the actual changes you are making to the code because code changes a lot more frequently than most unstructured data" [0:05:34]. That sync cost is why the leading terminal agents dropped it. As Cole puts it, "There's no codebase indexing with Claude Code. Instead, it's going to navigate a codebase more as an engineer would with command line tools."

## How it works

Two families of indexing show up across the videos. The first is a **built index**: parse the repo into embeddings or a graph so lookups are cheap at query time. A knowledge-graph variant is fast precisely because no model is involved, "this entire process of indexing and storing a repository takes less than 30 seconds usually depending on the size of the repo because there's no large language model being used here." You "tell the AI coding assistant like I want to parse this GitHub repo into the knowledge graph," and later queries hit the graph rather than the raw files.

The second is a **lightweight map** you maintain by hand. When the directory structure alone does not orient the agent, Cole writes a map into his rules: "Building up some kind of codebased map when the directory structure doesn't do the work and this usually I put in my global rule." The map "outlines the directory structure... That way, Claude can help me do the discovery, help me figure out what slice of the larger codebase to focus on." For external docs, the same instinct uses `llms.txt` and `sitemap.xml` as ready-made indexes of ingestible content.

## Contrasts with

- [Agentic Search](./agentic-search.md) - navigate-and-read on demand, deliberately avoiding an index that must be kept in sync.
- [When RAG Is Dead](./when-rag-is-dead.md) - the argument that index-based retrieval is being replaced for coding.
- [Traditional RAG](./traditional-rag.md) - one-shot semantic retrieval over a pre-built vector index.

## Builds on

- [Retrieval-Augmented Generation (RAG)](./rag.md) - indexing is the ingestion half of a RAG pipeline.
- [Structured vs. Unstructured Data](./structured-vs-unstructured-data.md) - code churns far faster than typical unstructured corpora, which is what makes the index hard to maintain.

## Related

- [Knowledge Bases](./knowledge-bases.md), [Knowledge Graphs](./knowledge-graphs.md) - the target structures an index is written into.
- [Global Rules](./global-rules.md) - where Cole parks a hand-written codebase map.
- [Context Engineering](./context-engineering.md) - giving the agent enough starting context to know where to look.

## Tools

- [Claude Code](../entities/tools/claude-code.md) - ships no codebase index; navigates with command-line tools like an engineer.
- [Archon](../entities/tools/archon.md) - ingests docs via `llms.txt` and sitemaps into a knowledge base.

## Sources

- [Why the Best AI Coding Tools Abandoned RAG (And What They Use Instead)](../sources/why-the-best-ai-coding-tools-abandoned-rag-and-what-they-use-instead.md) - "[0:05:34] it is a very difficult problem to keep the indexed codebase in sync with the actual changes you are making to the code because code changes a lot more frequently than most unstructured data."
- [Anthropic Just Dropped a Masterclass on Building Agent Harnesses (for Large Codebases)](../sources/anthropic-just-dropped-a-masterclass-on-building-agent-harnesses-for-large-codebases.md) - "[0:01:52] There's no codebase indexing with Claude Code. Instead, it's going to navigate a codebase more as an engineer would with command line tools."
- [AI Code That Fixes Itself (An MCP You Can Try Now)](../sources/ai-code-that-fixes-itself-an-mcp-you-can-try-now.md) - "[0:15:05] this entire process of indexing and storing a repository takes less than 30 seconds usually depending on the size of the repo because there's no large language model being used here."
- [The OFFICIAL Archon Guide - 10x Your AI Coding Workflow](../sources/the-official-archon-guide-10x-your-ai-coding-workflow.md) - "[0:15:39] Most documentation websites, if you just append llm.ext to it... has this curated list of files that are ready to be ingested as markdown for your AI coding assistant."
