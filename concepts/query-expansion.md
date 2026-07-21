---
type: concept
title: "Query Expansion"
description: "Rewriting or enriching a user's query with an LLM before retrieval to improve recall and match how source documents are phrased."
tags: [query-expansion, query-rewriting, retrieval, rag]
videos: [every-rag-strategy-explained-in-13-minutes-no-fluff, all-the-best-rag-strategies-in-one-mcp-for-ai-coding-assistants, the-proven-solution-for-unbelievable-rag-performance-lightrag-guide, build-ai-agents-that-evolve-over-time]
created: 2026-07-21
updated: 2026-07-21
---

# Query Expansion

Query expansion is a pre-retrieval step that hands the raw user question to a language model and lets it rewrite or enrich the query before anything is searched. As Cole frames it, "we are using a large language model to expand the query to make it more specific in ways that we know are going to lead to pulling more relevant chunks from the knowledge base" (every-rag-strategy, 0:06:28). The problem it solves is a mismatch of phrasing: a user's terse, casual question rarely reads like the source documents it needs to match, so a literal embedding of that question can miss the best chunks.

## How it works

An LLM rewrites the query intelligently before it ever touches the vector database. In an agent-memory setting the same move applies: "we have an LLM that intelligently rewrites the query to extract the most relevant information from our vector database" (build-ai-agents-that-evolve, 0:23:29). The rewrite can add synonyms, disambiguate intent, or restate the question in the vocabulary the corpus uses. Because retrieval quality is bounded by how well the query matches the stored text, improving the query improves recall without touching the index itself.

## Contrasts with

- [Multi-Query RAG](./multi-query-rag.md) is the sibling technique: instead of enriching one query, it fans out into several. Cole groups them together, "Things like multi-query rag and query expansion" (all-the-best-rag-strategies, 0:18:51). Query expansion sharpens a single query; multi-query RAG multiplies it.

## Builds on

- [Retrieval-Augmented Generation (RAG)](./rag.md) is the pipeline query expansion sits in front of.
- [Semantic Search](./semantic-search.md) is what the expanded query feeds; better phrasing yields better embedding matches.

## Related

- [Reranking](./reranking.md) is a complementary post-retrieval step. Query expansion improves what comes back; reranking reorders it.
- [Agentic RAG](./agentic-rag.md) can drive query expansion dynamically, deciding when and how to rewrite before searching. Cole lists it among the advanced strategies worth stacking: "You also have agentic rag, query expansion, reranking. There's so many strategies that I want to keep diving into on my channel" (lightrag guide, 0:22:42).

## Sources

- [Every RAG Strategy Explained in 13 Minutes (No Fluff)](../sources/every-rag-strategy-explained-in-13-minutes-no-fluff.md) - "[0:06:28] we are using a large language model to expand the query to make it more specific in ways that we know are going to lead to pulling more relevant chunks from the knowledge base"
- [Build AI Agents that EVOLVE Over Time](../sources/build-ai-agents-that-evolve-over-time.md) - "[0:23:29] we have an LLM that intelligently rewrites the query to extract the most relevant information from our vector database"
- [All the BEST RAG Strategies in ONE MCP for AI Coding Assistants](../sources/all-the-best-rag-strategies-in-one-mcp-for-ai-coding-assistants.md) - "[0:18:51] Things like multi-query rag and query expansion"
- [The PROVEN Solution for Unbelievable RAG Performance (LightRAG Guide)](../sources/the-proven-solution-for-unbelievable-rag-performance-lightrag-guide.md) - "[0:22:42] You also have agentic rag, query expansion, reranking. There's so many strategies that I want to keep diving into on my channel."
