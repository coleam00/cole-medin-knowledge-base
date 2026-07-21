---
type: source
title: "The Simplest RAG Stack That Actually Works (Complete Guide)"
description: "A simple, robust RAG stack combines keyword and semantic search on every query (hybrid search) merged via reciprocal rank fusion, built on MongoDB, Pydantic AI, and Docling."
youtube_id: Tz2YXg61aPo
url: https://www.youtube.com/watch?v=Tz2YXg61aPo
slug: the-simplest-rag-stack-that-actually-works-complete-guide
published: 2025-12-10
duration: "0:24:26"
recency_rank: 49
raw: "../raw/the-simplest-rag-stack-that-actually-works-complete-guide.md"
tags: [rag, hybrid-search, reciprocal-rank-fusion, mongodb, pydantic-ai]
created: 2026-07-21
updated: 2026-07-21
---

Cole walks through building a hybrid search RAG agent that gives the agent the ability to search a knowledge base both semantically (understanding concepts and relationships) and by exact keywords, combining both strategies on a single tool call to get the best of both worlds while staying fast. He frames hybrid search as his favorite RAG strategy precisely because, as he has evolved his approach, he has simplified it, leaning on strategies that just work regardless of the use case. Keyword search guarantees you find exact terms (a legal statute, a character name, a specific year like 2025, a 409 error code) and supports fuzzy matching to tolerate typos, while semantic search connects concepts (king finds queens, Berlin finds Germany, slow PC finds articles on making a PC fast) and catches synonyms; each covers the other's blind spots.

The tech stack is deliberately minimal. MongoDB serves as both the NoSQL document store and the vector database (storing document records plus chunk embeddings), Pydantic AI is the agent framework, and Docling handles file processing (PDFs, Word, markdown, audio) and hybrid chunking for clean chunk boundaries. Because search type is a tool parameter, the agent can choose semantic-only, keyword-only, or hybrid, which Cole considers a form of agentic RAG since the agent decides how to explore the knowledge base. He demonstrates live queries showing when each strategy wins.

Under the hood, each search runs as a MongoDB aggregation pipeline (roughly four stages: initial vector or fuzzy lookup, a join with the documents collection to attach metadata for source citation, an unwind data transformation, and score extraction). The two pipelines produce scores on completely different scales (vector similarity around 0.85 vs text scores like 15, 13, 11), so results are merged with reciprocal rank fusion, which ranks by position rather than raw score to normalize across pipelines and pick the final top chunks. MongoDB is building native Rank Fusion (in preview, not on the free tier), but Cole codes it himself to keep the template accessible. The whole retrieval, including the merge, takes under a second.

## Concepts covered

- [Hybrid Search](../concepts/hybrid-search.md)
- [Keyword Search](../concepts/keyword-search.md)
- [Semantic Search](../concepts/semantic-search.md)
- [Reciprocal Rank Fusion](../concepts/reciprocal-rank-fusion.md)
- [Agentic RAG](../concepts/agentic-rag.md)
- [Retrieval-Augmented Generation (RAG)](../concepts/rag.md)
- [Chunking](../concepts/chunking.md)
- [Traditional RAG](../concepts/traditional-rag.md)
- [Vector Embeddings](../concepts/vector-embeddings.md)

## Entities

- [MongoDB](../entities/tools/mongodb.md)
- [Pydantic AI](../entities/tools/pydantic-ai.md)
- [Docling](../entities/tools/docling.md)
- [Cole Medin](../entities/people/cole-medin.md)

## Key moments

- **[0:00:00]** Intro: hybrid search RAG agent gives both semantic and keyword search on every query
- **[0:01:43]** Tech stack decision: MongoDB as the (NoSQL + vector) database
- **[0:02:42]** Pydantic AI introduced as the agent framework (v1.27)
- **[0:03:34]** Docling for file processing and hybrid chunking
- **[0:05:26]** Pros/cons of keyword vs semantic search; why combine them
- **[0:07:10]** Live demo: revenue-by-service-line query using hybrid search
- **[0:08:33]** Keyword search wins on year-specific values (2025 vs 2023)
- **[0:09:29]** Semantic search wins: timeline for Converse Pro launch (no keyword match)
- **[0:11:14]** Hybrid search framed as a form of agentic RAG (agent picks search type)
- **[0:12:07]** Concrete examples of when vector vs keyword search each does well
- **[0:13:54]** Fuzzy matching in keyword search tolerates typos
- **[0:14:46]** MongoDB aggregation pipeline: lookup, join, unwind, score extraction
- **[0:18:49]** Join with documents collection to attach metadata for source citation
- **[0:20:35]** Reciprocal rank fusion to merge results from both pipelines
- **[0:21:04]** Why RRF is needed: score scales differ (0.85 vector vs 15 text)
- **[0:23:00]** Complete hybrid flow + demo showing sub-second retrieval latency

## Transcript

[Raw transcript](../raw/the-simplest-rag-stack-that-actually-works-complete-guide.md)
