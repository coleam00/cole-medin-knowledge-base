---
type: concept
title: "Temporal-Aware Knowledge Graphs"
description: "A knowledge graph that never overwrites a changed fact but stores the new one alongside the old with valid_at/invalidated_at timestamps, so an agent knows both what is true now and how the knowledge evolved."
tags: [rag, retrieval, graph, memory, temporal, knowledge-graphs]
videos: [make-rag-100x-better-with-real-time-knowledge-graphs]
created: 2026-07-21
updated: 2026-07-21
---

# Temporal-Aware Knowledge Graphs

A temporal-aware knowledge graph is a graph that treats a changed fact as a new fact rather than an edit. Cole frames it as a retrofit for the weakest part of retrieval: "it's a layer on top of rag that is meant for constantly ingesting everchanging data, also keeping a historical record of how your data has changed" [0:00:51]. Every relationship carries `valid_at` and `invalidated_at` timestamps, so the old edge stays in the graph marked as superseded instead of being deleted. An agent querying it gets both halves of the answer: what is true now, and what used to be true.

The payoff is visible in the LLM-evolution demo. Ingest facts in phases (Gemini 2.5 Pro is best, then Claude 4 supersedes it) and the agent answers "Claude 4 is best now" while still volunteering that Gemini 2.5 Pro previously held the spot. That kind of answer is structurally impossible for a store that overwrites. Under the hood the graph is ordinary graph infrastructure: "all of this temporal aware knowledge is stored in a knowledge graph that looks like this. And so this is Neo4j. That is the engine behind the scenes powering our knowledge graph" [0:02:33]. Data goes in as loosely-typed "episodes" (text or JSON, no fixed schema) and an LLM builds the nodes and relationships dynamically, which is what makes continuous incremental ingestion practical.

The relational structure is the other half of the argument: "This is why knowledge graphs in general are just a lot more powerful than traditional rag" [0:03:05]. Chunk-and-embed loses the connections between facts; a graph keeps them, and the temporal layer keeps them across time.

Cole is explicit that this is not a replacement for vector search. The ideal setup hands the agent both a graph tool and a vector tool and lets it choose - [agentic RAG](./agentic-rag.md) with two representations rather than a winner.

## Builds on

- [Knowledge Graphs](./knowledge-graphs.md) - the entity-and-relationship substrate the temporal layer sits on.
- [Retrieval-Augmented Generation (RAG)](./rag.md) - explicitly framed as a layer on top of RAG, not an alternative to it.

## Contrasts with

- [Traditional RAG](./traditional-rag.md) - static, chunk-based, and constantly out of sync with changing source data.
- [Delete-Before-Insert Re-Ingestion](./delete-before-insert-reingestion.md) - the overwrite strategy this pattern deliberately refuses, because it destroys history.

## Implemented by

- [Graphiti](../entities/tools/graphiti.md) - the open-source platform Cole uses; episodes in, temporal edges out, subsecond search.
- [Neo4j](../entities/tools/neo4j.md) - the graph engine underneath.
- [Pydantic AI](../entities/tools/pydantic-ai.md) - the agent whose single tool queries the graph.
- [GraphRAG](../entities/tools/graphrag.md), [LightRAG](../entities/tools/lightrag.md) - static graph builders suited to rarely-changing document corpora, positioned against Graphiti's dynamic data.

## Related

- [Agentic RAG](./agentic-rag.md) - give the agent both graph search and vector search and let it reason about which to use.
- [Memory Systems](./memory-systems.md), [Self-Evolving Memory](./self-evolving-memory.md) - user preferences that change over time are the canonical use case.
- [Knowledge Bases](./knowledge-bases.md), [Semantic Search](./semantic-search.md), [Hybrid Search](./hybrid-search.md), [Vector Embeddings](./vector-embeddings.md) - the complementary retrieval side.
- [Second Brain](./second-brain.md), [Web Crawling & Ingestion](./web-crawling.md), [Production-Ready RAG](./production-ready-rag.md).

## Sources

- [Make RAG 100x Better with Real-Time Knowledge Graphs](../sources/make-rag-100x-better-with-real-time-knowledge-graphs.md) - "[0:00:51] it's a layer on top of rag that is meant for constantly ingesting everchanging data, also keeping a historical record of how your data has changed"
- [Make RAG 100x Better with Real-Time Knowledge Graphs](../sources/make-rag-100x-better-with-real-time-knowledge-graphs.md) - "[0:02:33] all of this temporal aware knowledge is stored in a knowledge graph that looks like this. And so this is Neo4j. That is the engine behind the scenes powering our knowledge graph"
- [Make RAG 100x Better with Real-Time Knowledge Graphs](../sources/make-rag-100x-better-with-real-time-knowledge-graphs.md) - "[0:03:05] This is why knowledge graphs in general are just a lot more powerful than traditional rag."
