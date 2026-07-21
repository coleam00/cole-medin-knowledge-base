---
type: source
title: "I Built the Ultimate RAG MCP Server for AI Coding (Better than Context7)"
description: "Cole builds an open-source Crawl4AI RAG MCP server that gives AI coding assistants a private, self-hostable documentation knowledge base, solving the privacy and scoping limitations of Context7."
youtube_id: ZoyPqXvnnZ8
url: https://www.youtube.com/watch?v=ZoyPqXvnnZ8
slug: i-built-the-ultimate-rag-mcp-server-for-ai-coding-better-than-context7
published: 2025-05-04
duration: "0:28:24"
recency_rank: 95
raw: "../raw/i-built-the-ultimate-rag-mcp-server-for-ai-coding-better-than-context7.md"
tags: [rag, mcp, knowledge-base, crawl4ai]
created: 2026-07-21
updated: 2026-07-21
---

# I Built the Ultimate RAG MCP Server for AI Coding (Better than Context7)

Cole opens by praising Context7, a hosted MCP server that gives AI coding assistants RAG over the documentation of thousands of frameworks, dramatically reducing hallucinations. But he flags three problems: the collective 8,000-library knowledge base is too broad (agents grab the wrong docs), it can't include your private GitHub repos, and its core scraping/RAG logic lives behind a private API endpoint (the MCP wrapper is only ~68 lines) that will likely be monetized. This motivates his open-source alternative.

He introduces a Crawl4AI-based RAG MCP server that lets you scrape any website into your own private Supabase knowledge base and instantly query it from any AI coding assistant or agent. In a Windsurf demo he crawls the Pydantic AI llms-full.txt and the Mem0 sitemap, watches the container embed the content (288k characters, 67 chunks), then prompts the assistant to build a Pydantic AI + Mem0 agent that pulls the freshly-crawled docs via RAG. The server exposes four tools: crawl a single page, smart-crawl a URL (auto-detecting sitemaps, llms.txt, or recursive scraping), list available sources, and perform a RAG query with optional per-source metadata filtering. Source metadata preserves the ability to scope search to one framework, matching a Context7 feature he refused to lose.

Cole frames the server as a proof of concept for evolving Archon from an agent builder into a general knowledge engine for agents and coding assistants. His roadmap: pluggable embedding models (Gemini, Ollama for fully-local RAG), advanced retrieval strategies (contextual retrieval, late chunking, agentic RAG), better chunking, and faster crawling to make RAG feel instant. Setup requires Docker or Python, Supabase (local or cloud), and an OpenAI key, with SSE or stdio transport, and he shows wiring it into Windsurf and n8n.

## Concepts covered

- [Retrieval-Augmented Generation (RAG)](../concepts/rag.md)
- [Model Context Protocol (MCP)](../concepts/mcp.md)
- [Knowledge Bases](../concepts/knowledge-bases.md)
- [Web Crawling & Ingestion](../concepts/web-crawling.md)
- [Chunking](../concepts/chunking.md)
- [Vector Embeddings](../concepts/vector-embeddings.md)
- [Traditional RAG](../concepts/traditional-rag.md)
- [Contextual Retrieval](../concepts/contextual-retrieval.md)
- [Late Chunking](../concepts/late-chunking.md)
- [Agentic RAG](../concepts/agentic-rag.md)
- [Local & Self-Hosted AI](../concepts/local-ai.md)
- [Planning with AI](../concepts/planning-with-ai.md)
- [Global Rules](../concepts/global-rules.md)

## Entities

- [Cole Medin](../entities/people/cole-medin.md)
- [Context7](../entities/tools/context7.md)
- [Crawl4AI](../entities/tools/crawl4ai.md)
- [Archon](../entities/tools/archon.md)
- [Pydantic AI](../entities/tools/pydantic-ai.md)
- [Mem0](../entities/tools/mem0.md)
- [Supabase](../entities/tools/supabase.md)
- [Windsurf](../entities/tools/windsurf.md)
- [Cursor](../entities/tools/cursor.md)
- [Ollama](../entities/tools/ollama.md)
- [OpenAI](../entities/organizations/openai.md)
- [Anthropic](../entities/organizations/anthropic.md)
- [n8n](../entities/tools/n8n.md)
- [Docker](../entities/tools/docker.md)
- [Dynamous](../entities/organizations/dynamous.md)

## Key moments

- **[0:00:15]** Introduces Context7 as a hosted MCP RAG server for framework documentation
- **[0:01:38]** Three limitations of Context7: too broad, no private repos, core logic closed-source
- **[0:03:21]** Introduces his open-source Crawl4AI RAG MCP server
- **[0:03:48]** Windsurf demo: crawl Pydantic AI + Mem0 docs into private Supabase knowledge base
- **[0:06:47]** Source metadata lets you scope RAG search to a single tool/framework
- **[0:08:23]** Agent builds a full Pydantic AI + Mem0 agent using the crawled knowledge
- **[0:14:17]** Vision: turn Archon into a general knowledge engine, this server is the proof of concept
- **[0:15:36]** Roadmap: local embeddings (Ollama), contextual retrieval, late chunking, agentic RAG, better chunking
- **[0:17:28]** The four MCP tools: crawl single page, smart crawl, get sources, perform RAG query
- **[0:19:59]** Setup walkthrough: Docker/Python, Supabase SQL, env vars, SSE transport, wiring into Windsurf and n8n

## Transcript

[Raw transcript](../raw/i-built-the-ultimate-rag-mcp-server-for-ai-coding-better-than-context7.md)
