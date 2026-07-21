---
type: source
title: "Make RAG 100x Better with Real-Time Knowledge Graphs"
description: "Temporal-aware knowledge graphs (via Graphiti + Neo4j) layer on top of RAG to continuously ingest changing data and preserve historical context, giving AI agents far richer, time-aware retrieval than static traditional RAG."
youtube_id: PxcOIINgiaA
url: https://www.youtube.com/watch?v=PxcOIINgiaA
slug: make-rag-100x-better-with-real-time-knowledge-graphs
published: 2025-05-28
duration: "0:26:41"
recency_rank: 88
raw: "../raw/make-rag-100x-better-with-real-time-knowledge-graphs.md"
tags: [knowledge-graphs, rag, agentic-rag, graphiti, temporal]
created: 2026-07-21
updated: 2026-07-21
---

# Make RAG 100x Better with Real-Time Knowledge Graphs

Cole argues that plain RAG has a fundamental weakness: it is static, forcing you to constantly and unreliably re-sync a knowledge base against changing data. For dynamic domains (user preferences, internal metrics, market conditions) this breaks down. His answer is Graphiti, an open-source platform for building temporal-aware knowledge graphs on top of Neo4j: instead of overwriting a fact when it changes, Graphiti keeps both the old and new versions with timestamps (valid_at / invalidated_at), so an agent knows not just what is currently true but how the knowledge evolved.

The video walks through a quick start where information is ingested as "episodes" (plain text or JSON, no fixed schema) and an LLM dynamically builds nodes and relationships in the graph. Search is a single function call, with a center-node search that re-ranks results around a specific node for more precise retrieval. Cole then builds a full agent with Pydantic AI whose single tool queries the Graphiti graph, and runs an "LLM evolution" script in phases: first establishing Gemini 2.5 Pro as best, then Claude 4 superseding it, then a joke "MLM" model. Each phase shows the agent's answer changing while still surfacing historical caveats (e.g. "Claude 4 is best now, but Gemini 2.5 Pro used to be").

Cole positions Graphiti against static knowledge-graph tools like GraphRAG and LightRAG, which he says suit rarely-changing document summarization, whereas Graphiti is built for dynamic, incrementally-updated data and is faster and more scalable (subsecond latency). He stresses this is not knowledge-graphs-vs-vector-RAG: the ideal setup gives the agent both a graph search tool and a vector-DB search tool (agentic RAG), letting it reason over whichever representation surfaces the right context.

## Concepts covered

- [Knowledge Graphs](../concepts/knowledge-graphs.md)
- [Retrieval-Augmented Generation (RAG)](../concepts/rag.md)
- [Traditional RAG](../concepts/traditional-rag.md)
- [Agentic RAG](../concepts/agentic-rag.md)
- [Web Crawling & Ingestion](../concepts/web-crawling.md)

## Entities

- [Graphiti](../entities/tools/graphiti.md)
- [Neo4j](../entities/tools/neo4j.md)
- [Pydantic AI](../entities/tools/pydantic-ai.md)
- [LightRAG](../entities/tools/lightrag.md)
- [Ollama](../entities/tools/ollama.md)
- [OpenAI](../entities/organizations/openai.md)
- [Cole Medin](../entities/people/cole-medin.md)

## Key moments

- **[0:00:00]** RAG is static and hard to keep in sync, the core limitation this video addresses
- **[0:00:33]** Introduces Graphiti as a temporal-aware knowledge graph layer on top of RAG for ever-changing data
- **[0:01:35]** Kendra shoes example: keep both old and new preference facts with historical context instead of overwriting
- **[0:02:33]** Neo4j shown as the knowledge-graph engine; nodes linked by relationships (GPT-4 is previous version of 3.5)
- **[0:03:33]** Graph search and vector lookup as two complementary agent tools; still keep hybrid/contextual RAG
- **[0:04:05]** Comparison to GraphRAG / LightRAG (static doc summarization) vs Graphiti (dynamic data); partnership disclosure
- **[0:09:18]** Quick start: connect to Neo4j, build indices, add episodes (text or JSON), reference_time
- **[0:11:34]** Single-call graphiti.search; results carry fact, valid_at, and invalidation timestamps
- **[0:12:34]** Center-node search to refine/re-rank retrieval around a specific node
- **[0:16:42]** Builds a Pydantic AI agent with one Graphiti search tool over the graph
- **[0:17:23]** LLM evolution script adds facts in phases (Gemini best -> Claude 4 best -> MLM joke)
- **[0:22:26]** Agent answers "Claude 4 is best now" while noting Gemini 2.5 Pro used to be, temporal reasoning payoff
- **[0:24:50]** Combine knowledge graph with vector DB (agentic RAG); don't pick one over the other

## Transcript

[Raw transcript](../raw/make-rag-100x-better-with-real-time-knowledge-graphs.md)
