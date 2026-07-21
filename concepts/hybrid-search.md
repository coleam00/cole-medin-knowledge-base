---
type: concept
title: "Hybrid Search"
description: "Combining keyword (BM25) and semantic vector search so retrieval catches both exact-term and meaning-based matches."
tags: [hybrid-search, bm25, semantic-search, keyword-search]
videos: [build-a-rag-ai-agent-with-real-time-source-validation-copilotkit-pydantic-ai, the-simplest-rag-stack-that-actually-works-complete-guide, the-official-archon-guide-10x-your-ai-coding-workflow, all-the-best-rag-strategies-in-one-mcp-for-ai-coding-assistants, the-easiest-possible-strategy-for-accurate-rag-step-by-step-guide, the-proven-solution-for-unbelievable-rag-performance-lightrag-guide, introducing-archon-an-ai-agent-that-builds-ai-agents]
created: 2026-07-21
updated: 2026-07-21
---

# Hybrid Search

Hybrid search runs keyword and semantic retrieval side by side and merges their results, so you catch both exact terms and conceptual matches. As Cole puts it, "we give our agent the ability to search our documents and data both semantically understanding the relationship between concepts but also with keywords so we can very accurately pick out super specific information" [0:00:00]. Semantic search alone misses exact tokens; keyword search alone misses meaning. Hybrid search is the union: "we're going to be able to find concepts and exact terms. And so our search is going to pull in chunks from both of those strategies."

## How it works

The keyword leg is typically BM25 over a text index, "BM25 for hybrid rag where we have keyword search along with semantic search," while the semantic leg is nearest-neighbor over [vector embeddings](./vector-embeddings.md). Both legs return candidate chunks, and the pipeline combines the two sets before handing them to the LLM: "we'll just combine that with regular rag so that we have both sets of chunks that we're returning." Some stacks expose the search mode as an agent-tunable parameter, "we can change different attributes for how the agent performs rag under the hood like semantic versus hybrid search," which makes hybrid search a natural fit inside agentic RAG.

When two ranked result lists are merged, a fusion step decides the final ordering, which is where [reciprocal rank fusion](./reciprocal-rank-fusion.md) comes in. A knowledge-graph "mix" mode generalizes the same both-worlds idea: LightRAG "will use both vector retrieval basic rag and it'll search the knowledge graph. So we literally lose out on nothing from basic rag."

## Builds on

- [Keyword Search](./keyword-search.md) - the lexical/BM25 leg that guarantees exact-term matches.
- [Semantic Search](./semantic-search.md) - the vector leg that captures conceptual meaning.

## Related

- [Reciprocal Rank Fusion](./reciprocal-rank-fusion.md) - the standard way to merge the two ranked result lists.
- [Reranking](./reranking.md) - often applied after fusion to reorder combined results.
- [Agentic RAG](./agentic-rag.md) - hybrid vs. semantic is frequently a per-query choice the agent makes.
- [Retrieval-Augmented Generation (RAG)](./rag.md), [Traditional RAG](./traditional-rag.md), [Chunking](./chunking.md), [Hierarchical RAG](./hierarchical-rag.md), [Knowledge Graphs](./knowledge-graphs.md) - the surrounding retrieval stack.
- [Metadata Filtering](./metadata-filtering.md) - Tagging every embedded chunk with source metadata so retrieval can be scoped to one document set and answers can cite which document they came from.

## Tools

- [Archon](../entities/tools/archon.md) - "performing rag under the hood for both keyword and semantic searching."
- [LightRAG](../entities/tools/lightrag.md) - its "mix" mode searches vectors and a knowledge graph together.
- [Pydantic AI](../entities/tools/pydantic-ai.md) - exposes semantic-vs-hybrid as an agent-configurable retrieval attribute.

## Sources

- [The Simplest RAG Stack That Actually Works (Complete Guide)](../sources/the-simplest-rag-stack-that-actually-works-complete-guide.md) - "[0:06:21] that's why the hybrid search is the solution here because we're going to be able to find concepts and exact terms. And so our search is going to pull in chunks from both of those strategies"
- [All the BEST RAG Strategies in ONE MCP for AI Coding Assistants](../sources/all-the-best-rag-strategies-in-one-mcp-for-ai-coding-assistants.md) - "[0:09:58] hybrid search is all about being able to give your AI agent the ability to do a keyword search on top of regular rag"
- [The EASIEST Possible Strategy for Accurate RAG (Step by Step Guide)](../sources/the-easiest-possible-strategy-for-accurate-rag-step-by-step-guide.md) - "[0:22:27] Things like BM25 for hybrid rag where we have keyword search along with semantic search"
- [The OFFICIAL Archon Guide - 10x Your AI Coding Workflow](../sources/the-official-archon-guide-10x-your-ai-coding-workflow.md) - "[0:03:06] It's performing rag under the hood for both keyword and semantic searching. Very, very powerful rag strategies that we have for this."
- [Build a RAG AI Agent with REAL-TIME Source Validation (CopilotKit + Pydantic AI)](../sources/build-a-rag-ai-agent-with-real-time-source-validation-copilotkit-pydantic-ai.md) - "[0:14:42] we can change different attributes for how the agent performs rag under the hood like semantic versus hybrid search."
- [The PROVEN Solution for Unbelievable RAG Performance (LightRAG Guide)](../sources/the-proven-solution-for-unbelievable-rag-performance-lightrag-guide.md) - "[0:03:33] this will use both vector retrieval basic rag and it'll search the knowledge graph. So we literally lose out on nothing from basic rag because we have that and more with LightRAG."
- [Introducing Archon - an AI Agent that BUILDS AI Agents](../sources/introducing-archon-an-ai-agent-that-builds-ai-agents.md) - "[0:17:57] things like hybrid search reranking uh query decomposition or better chunking through things like hierarchical chunking there's a lot of opportunities that we have here"
