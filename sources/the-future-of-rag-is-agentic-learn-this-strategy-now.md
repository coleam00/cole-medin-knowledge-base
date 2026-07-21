---
type: source
title: "The Future of RAG is Agentic - Learn this Strategy NOW"
description: "Turning standard one-shot RAG into agentic RAG, where retrieval becomes a set of tools an agent can reason about and choose between, solves RAG's most common failures and delivers far more accurate, consistent results."
youtube_id: _R-ff4ZMLC8
url: https://www.youtube.com/watch?v=_R-ff4ZMLC8
slug: the-future-of-rag-is-agentic-learn-this-strategy-now
published: 2025-01-15
duration: "0:45:50"
recency_rank: 125
raw: "../raw/the-future-of-rag-is-agentic-learn-this-strategy-now.md"
tags: [rag, agentic-rag, retrieval]
created: 2026-07-21
updated: 2026-07-21
---

# The Future of RAG is Agentic - Learn this Strategy NOW

Cole Medin walks through why traditional RAG so often disappoints in practice: the wrong text gets retrieved, the LLM ignores context, and there's no chance for the agent to recover because a single vector search is a one-shot: the agent works only with whatever it was handed and can't decide it needs to search again or search differently. His fix is agentic RAG: instead of injecting retrieved context once, you expose retrieval AS tools the agent can call, letting it intelligently choose where and how to fetch knowledge.

The video is a full build. Using Crawl4AI he scrapes the entire Pydantic AI documentation (42 pages) from the sitemap, chunks each page while respecting code blocks and paragraphs, uses GPT-4o-mini to generate a title and summary for every chunk, embeds chunks with OpenAI's text-embedding-3-small, and stores everything (URL, chunk number, title, summary, content, metadata, embedding) in a Supabase table (245 chunks). Metadata like a 'source' field lets one table serve many agents via filtering. He then builds a Pydantic AI agent in three parts: dependencies, agent, tools, starting with a basic-RAG retrieval tool.

He demonstrates the limits of basic RAG: a simple 'what models are supported' question works, but 'give me the weather agent example' fails because a small chunk can't capture a whole example. Agentic RAG fixes it by adding two more tools, list all documentation URLs and fetch the full contents of a specific page, so the agent can start with basic RAG, notice it was insufficient, list pages, reason about which one to visit (using titles/summaries), and pull the complete page. He also compares Supabase (RAG + structured data in one place) versus Qdrant (faster, vector-only), covers a Streamlit chat UI, and stresses that agentic RAG is extensible with more specialized knowledge stores and tools.

## Concepts covered

- [Agentic RAG](../concepts/agentic-rag.md)
- [Retrieval-Augmented Generation (RAG)](../concepts/rag.md)
- [Traditional RAG](../concepts/traditional-rag.md)
- [Chunking](../concepts/chunking.md)
- [Context-Aware Chunking](../concepts/context-aware-chunking.md)
- [Vector Embeddings](../concepts/vector-embeddings.md)
- [Semantic Search](../concepts/semantic-search.md)
- [Knowledge Bases](../concepts/knowledge-bases.md)
- [Structured vs Unstructured Data](../concepts/structured-vs-unstructured-data.md)

## Entities

- [Cole Medin](../entities/people/cole-medin.md)
- [Pydantic AI](../entities/tools/pydantic-ai.md)
- [Supabase](../entities/tools/supabase.md)
- [Qdrant](../entities/tools/qdrant.md)
- [Crawl4AI](../entities/tools/crawl4ai.md)
- [OpenAI](../entities/organizations/openai.md)
- [Streamlit](../entities/tools/streamlit.md)
- [Weaviate](../entities/organizations/weaviate.md)
- [Live Agent Studio](../entities/tools/live-agent-studio.md)
- [GitHub](../entities/tools/github.md)

## Key moments

- **[0:00:00]** Framing: RAG is the go-to for feeding external knowledge to LLMs, but it falls apart in practice (wrong text retrieved, LLM ignores context)
- **[0:00:50]** Thesis: of all the strategies (reranking, query expansion, rank normalization), agentic RAG works best
- **[0:02:30]** Weaviate article diagrams: basic RAG (chunk -> embed -> store -> match) explained
- **[0:04:12]** The core problem: basic RAG is a one-shot; the agent can't reason about or improve on what it got
- **[0:04:44]** Definition of agentic RAG: make RAG into tools the agent interacts with and reasons over
- **[0:11:03]** Chunking strategy: split pages while respecting code blocks, paragraphs, and sentences
- **[0:15:39]** Per-chunk title + summary generation with an LLM to help the agent reason about relevance
- **[0:17:08]** Metadata (source field) lets one knowledge table serve many agents via filtering
- **[0:33:57]** Live test - basic RAG works for 'what models are supported'
- **[0:34:45]** Live test - basic RAG fails on 'give me the weather agent example'
- **[0:37:17]** Adding agentic tools: list documentation pages + fetch full page content
- **[0:38:00]** Qdrant vs Supabase for RAG - vector-only speed vs unified RAG + structured data
- **[0:40:36]** Re-test with agentic RAG: agent tries basic RAG, lists pages, fetches the right one, returns the full example

## Transcript

[Raw transcript](../raw/the-future-of-rag-is-agentic-learn-this-strategy-now.md)
