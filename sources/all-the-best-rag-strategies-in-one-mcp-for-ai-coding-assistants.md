---
type: source
title: "All the BEST RAG Strategies in ONE MCP for AI Coding Assistants"
description: "Combining four advanced RAG strategies (contextual embeddings, hybrid search, agentic RAG, and reranking) into a single open-source Crawl4AI RAG MCP server gives AI coding assistants an accurate, up-to-date documentation knowledge base and forms the knowledge backbone of the next evolution of Archon."
youtube_id: BdZ_GOaaz7M
url: https://www.youtube.com/watch?v=BdZ_GOaaz7M
slug: all-the-best-rag-strategies-in-one-mcp-for-ai-coding-assistants
published: 2025-06-04
duration: "0:21:10"
recency_rank: 87
raw: "../raw/all-the-best-rag-strategies-in-one-mcp-for-ai-coding-assistants.md"
tags: [rag, hybrid-search, reranking, contextual-retrieval, mcp, archon]
created: 2026-07-21
updated: 2026-07-21
---

# All the BEST RAG Strategies in ONE MCP for AI Coding Assistants

Cole demonstrates his open-source Crawl4AI RAG MCP server, built to solve the core problem that AI coding assistants hallucinate when working with libraries and documentation. The server crawls documentation (via llms.txt pages, sitemaps, or recursive navigation), embeds it into a Supabase knowledge base, and exposes RAG tools that AI coders (in Windsurf, N8N, or any MCP client) can query for accurate, current docs and code examples. He shows a live demo crawling the Vercel AI SDK docs and using the retrieved knowledge to build a clean Claude 4 chat interface with a weather tool.

The heart of the video walks through four RAG strategies that make the server more powerful, each toggleable via environment variables. Contextual embeddings (from Anthropic's contextual retrieval article) prepend each chunk with LLM-generated context situating it in the full document, using prompt caching to stay cheap. Hybrid search adds case-insensitive keyword matching on top of semantic search so exact terms like "OpenAI" are reliably retrieved. Agentic RAG maintains a separate code-examples vector table alongside the documentation table, giving the agent distinct tools to reason about which knowledge base to search. Reranking uses a locally-run HuggingFace cross-encoder to reorder retrieved chunks by true relevance, letting the server pull many chunks and return only the most relevant few without overwhelming the LLM's context.

Cole frames this as the foundation of a larger vision: turning the RAG server into the next evolution of Archon, a master platform that combines a strong RAG knowledge backbone with task management and agents that manage different parts of a project. He teases future strategies (multi-query RAG, query expansion, agentic RAG with knowledge graphs via Graphiti or LightRAG) and an in-progress Archon front-end overhaul for auto-crawling and managing sources from a UI, all kept fully open source.

## Concepts covered

- [Retrieval-Augmented Generation (RAG)](../concepts/rag.md)
- [Knowledge Bases](../concepts/knowledge-bases.md)
- [Contextual Retrieval](../concepts/contextual-retrieval.md)
- [Chunking](../concepts/chunking.md)
- [Hybrid Search](../concepts/hybrid-search.md)
- [Keyword Search](../concepts/keyword-search.md)
- [Semantic Search](../concepts/semantic-search.md)
- [Agentic RAG](../concepts/agentic-rag.md)
- [Reranking](../concepts/reranking.md)
- [Vector Embeddings](../concepts/vector-embeddings.md)
- [Multi-Query RAG](../concepts/multi-query-rag.md)
- [Query Expansion](../concepts/query-expansion.md)
- [Knowledge Graphs](../concepts/knowledge-graphs.md)
- [Model Context Protocol (MCP)](../concepts/mcp.md)

## Entities

- [Archon](../entities/tools/archon.md)
- [Crawl4AI RAG MCP Server](../entities/tools/crawl4ai-rag-mcp.md)
- [Supabase](../entities/tools/supabase.md)
- [MCP (Model Context Protocol)](../entities/tools/mcp.md)
- [OpenAI](../entities/organizations/openai.md)
- [Anthropic](../entities/organizations/anthropic.md)
- [Vercel AI SDK](../entities/tools/vercel-ai-sdk.md)
- [Windsurf](../entities/tools/windsurf.md)
- [n8n](../entities/tools/n8n.md)
- [Hugging Face](../entities/organizations/hugging-face.md)
- [Graphiti](../entities/tools/graphiti.md)
- [Dynamous](../entities/organizations/dynamous.md)
- [Cole Medin](../entities/people/cole-medin.md)

## Key moments

- **[0:00:00]** Frames the problem: AI coding assistants hallucinate on libraries and docs
- **[0:00:34]** Introduces the Crawl4AI RAG MCP server as the future core of Archon
- **[0:02:34]** Live demo: crawling the Vercel AI SDK llms.txt into a Supabase knowledge base from Windsurf
- **[0:06:14]** Uses the knowledge base to build a clean Claude 4 chat UI with a weather tool
- **[0:08:23]** Contextual embeddings explained (Anthropic contextual retrieval + prompt caching)
- **[0:09:58]** Hybrid search: keyword search combined with semantic RAG
- **[0:13:30]** Agentic RAG: separate code-examples vector table with its own tool
- **[0:16:19]** Reranking with a local HuggingFace cross-encoder model
- **[0:18:51]** Future plans: multi-query RAG, query expansion, knowledge graphs, Archon vision

## Transcript

[Raw transcript](../raw/all-the-best-rag-strategies-in-one-mcp-for-ai-coding-assistants.md)
