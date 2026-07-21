---
type: concept
title: "Metadata Filtering"
description: "Tagging every embedded chunk with source metadata so retrieval can be scoped to one document set and answers can cite which document they came from."
tags: [rag, retrieval, metadata, citations, filtering]
videos: [i-built-the-ultimate-rag-mcp-server-for-ai-coding-better-than-context7, the-ultimate-n8n-rag-ai-agent-template-local-ai-edition, the-future-of-rag-is-agentic-learn-this-strategy-now]
created: 2026-07-21
updated: 2026-07-21
---

# Metadata Filtering

Metadata filtering is the discipline of storing structured attributes alongside every embedded chunk, then using those attributes to narrow a search before or during retrieval. The attribute that matters most is provenance: "In the metadata, we have important things like the source that each chunk is coming from. So we can still separate the rag search by specific tools and frameworks" [0:06:32]. One vector store can hold many document sets and still behave like many separate knowledge bases, because the filter, not the index, defines the scope: the retriever "can also search within just a single documentation if we want to provide a metadata filter" [0:19:13].

## Why one knowledge base beats many

The naive fix for mixed-domain retrieval is a separate collection per source, which multiplies infrastructure and blocks cross-domain questions. Metadata filtering collapses it: "I can have them all use the same knowledge base but whenever I query the knowledge base for that specific agent I would just say give me the results from your search but only looking at the records where the source is pantic AI docs" [0:17:23]. The same field that scopes an agent to its own documentation can be left off for a broad search, so scope becomes a per-query decision instead of an architectural one. This is exactly the lever [agentic RAG](./agentic-rag.md) needs: an agent that picks its own filter is doing retrieval strategy, not just lookup.

Filters are not limited to source. Time is the other high-value axis: "I can also query based on time for example if I only want to search based on the records in the last day that were ingested" [0:17:39]. That makes freshness a first-class query dimension and pairs with [delete-before-insert reingestion](./delete-before-insert-reingestion.md), which keeps the versions honest in the first place.

## Metadata as the citation layer

The second payoff is attribution. When file identity travels with the chunk, the model can name its source without a second lookup: "I am adding metadata for this record including the file ID and file title ... when we do a rag lookup when this record is returned the metadata is included so the llm can actually use this information to cite its source" [0:21:23]. Citations turn a plausible answer into a checkable one, which is why this is table stakes for [production-ready RAG](./production-ready-rag.md).

## Builds on

- [Chunking](./chunking.md) - the chunk is the unit metadata is attached to.
- [Vector Embeddings](./vector-embeddings.md) - metadata rides alongside the vector in the same record.
- [Retrieval-Augmented Generation (RAG)](./rag.md) - the pipeline this narrows.

## Related

- [Agentic RAG](./agentic-rag.md) - an agent choosing its own filter per query.
- [Hybrid Search](./hybrid-search.md), [Semantic Search](./semantic-search.md) - filters apply on top of either retrieval leg.
- [Contextual Retrieval](./contextual-retrieval.md), [Hierarchical RAG](./hierarchical-rag.md) - other ways to give a chunk more context than its own text.
- [Production-Ready RAG](./production-ready-rag.md), [Knowledge Bases](./knowledge-bases.md) - where citations and scoping become requirements.
- [Web Crawling](./web-crawling.md) - where the source field usually gets populated.

## Tools

- [Supabase](../entities/tools/supabase.md) and [Postgres](../entities/tools/postgres-pgvector.md) - a JSONB metadata column filtered in the same query as the vector match.
- [Qdrant](../entities/tools/qdrant.md) - payload filtering built into the vector search call.
- [n8n](../entities/tools/n8n.md) - where file ID and title are attached during ingestion.
- [Crawl4AI RAG MCP Server](../entities/tools/crawl4ai-rag-mcp.md) - stores a source per chunk so coding assistants can search one framework's docs at a time.

## Sources

- [I Built the Ultimate RAG MCP Server for AI Coding (Better than Context7)](../sources/i-built-the-ultimate-rag-mcp-server-for-ai-coding-better-than-context7.md) - "[0:06:32] In the metadata, we have important things like the source that each chunk is coming from. So we can still separate the rag search by specific tools and frameworks."
- [I Built the Ultimate RAG MCP Server for AI Coding (Better than Context7)](../sources/i-built-the-ultimate-rag-mcp-server-for-ai-coding-better-than-context7.md) - "[0:19:13] It can also search within just a single documentation if we want to provide a metadata filter."
- [The Future of RAG is Agentic - Learn this Strategy NOW](../sources/the-future-of-rag-is-agentic-learn-this-strategy-now.md) - "[0:17:23] I can have them all use the same knowledge base but whenever I query the knowledge base for that specific agent I would just say give me the results from your search but only looking at the records where the source is pantic AI docs"
- [The Future of RAG is Agentic - Learn this Strategy NOW](../sources/the-future-of-rag-is-agentic-learn-this-strategy-now.md) - "[0:17:39] I can also query based on time for example if I only want to search based on the records in the last day that were ingested"
- [The ULTIMATE n8n RAG AI Agent Template - Local AI Edition](../sources/the-ultimate-n8n-rag-ai-agent-template-local-ai-edition.md) - "[0:21:23] I am adding metadata for this record including the file ID and file title ... when we do a rag lookup when this record is returned the metadata is included so the llm can actually use this information to cite its source"
