---
type: entity
subtype: tool
title: "Graphiti"
description: "A knowledge-graph tool Cole names as a candidate for a future agentic-RAG-with-knowledge-graphs strategy."
resource: "https://github.com/getzep/graphiti"
tags: [knowledge-graphs, rag, memory-systems, open-source]
videos: [the-only-ai-tech-stack-you-need-in-2026, every-rag-strategy-explained-in-13-minutes-no-fluff, should-i-build-my-ai-agents-with-n8n-or-python, knowledge-graphs-in-n8n-are-finally-here, introducing-rag-20-agentic-rag-knowledge-graphs-free-template, all-the-best-rag-strategies-in-one-mcp-for-ai-coding-assistants, make-rag-100x-better-with-real-time-knowledge-graphs, the-proven-solution-for-unbelievable-rag-performance-lightrag-guide]
created: 2026-07-21
updated: 2026-07-21
---

# Graphiti

Graphiti is Cole's favorite open-source library for building [knowledge graphs](../../concepts/knowledge-graphs.md), and specifically temporal-aware ones. As he introduces it, "an open- source platform with you right now called Graffiti. Graffiti is all about building temporal aware knowledge graphs" ([0:00:33]). It is the extraction-and-query layer that sits on top of a graph database: "graffiti is the library. It's the tooling that gives us the ability to extract from raw text the entities and relationships to then store in Neo4j" ([0:06:25]). Where a plain [vector embedding](../../concepts/vector-embeddings.md) pipeline captures similarity, Graphiti captures structure, making it the backbone of Cole's [agentic RAG](../../concepts/agentic-rag.md) with knowledge graphs.

## How Cole uses it

Cole pairs Graphiti with [Neo4j](./neo4j.md) as a two-part system: Graphiti is the intelligent library, Neo4j is the underlying engine. He uses it "for the library to help us insert data into Neoforj and search our knowledge graphs here. I love using graffiti... very intelligent entity and relationship extraction" ([0:16:16]), and calls it "my favorite library for working with knowledge graphs" ([0:05:14]). The entity and relationship extraction is LLM-driven: ingested as timestamped episodes, "the different entities and their relationships, all of this has to be defined by large language models" ([0:21:09]).

Its temporal model is the differentiator Cole keeps returning to. Because it tracks how facts change over time with "subsecond latency," "Graffiti is a lot more lightweight and scalable... you can seriously take graffiti all the way to production environments" ([0:05:09]), and "If you're looking to build AI agents that work with constantly changing information, then graffiti is the solution for you" ([0:10:32]). That temporal awareness is also why it underpins a real [memory system](../../concepts/memory-systems.md): "it powers the core of Zep's memory layer" ([0:09:57]).

Graphiti recurs across his stack in both code and no-code contexts. It "gives us the MCP server that makes it possible to use graffiti with nan" ([0:06:45]), it anchors his RAG 2.0 template "working alongside Neo4j which is the underlying knowledge graph engine" ([0:05:41]), and he names it as the path to "building out a gentic rag with knowledge graphs with something like graffiti or light rag" ([0:18:51]).

> **Contradiction:** Cole calls Graphiti "a lot more lightweight and scalable" with subsecond latency and production-readiness ([0:05:09], make-rag-100x-better-with-real-time-knowledge-graphs), while elsewhere he presents [LightRAG](./lightrag.md) as the "proven solution for unbelievable RAG performance." These are framed as alternative knowledge-graph engines for the same job; he recommends evaluating both against your latency and freshness needs rather than treating either as strictly superior.

## Related

- [Knowledge Graphs](../../concepts/knowledge-graphs.md) - Graphiti extracts entities and relationships into a graph.
- [Agentic RAG](../../concepts/agentic-rag.md), [RAG](../../concepts/rag.md), [Traditional RAG](../../concepts/traditional-rag.md) - it is the graph half of RAG-plus-knowledge-graph strategies.
- [Memory Systems](../../concepts/memory-systems.md) - its temporal graph powers agent long-term memory (Zep).
- [Vector Embeddings](../../concepts/vector-embeddings.md) and [Chunking](../../concepts/chunking.md) - the structural complement to similarity-based retrieval.
- Sibling tools: [Neo4j](./neo4j.md) (its underlying engine), [LightRAG](./lightrag.md) (an alternative), [n8n](./n8n.md), [Docling](./docling.md), [Crawl4AI](./crawl4ai.md).

## Sources

- [Make RAG 100x Better with Real-Time Knowledge Graphs](../../sources/make-rag-100x-better-with-real-time-knowledge-graphs.md) - "[0:00:33] an open- source platform with you right now called Graffiti. Graffiti is all about building temporal aware knowledge graphs."
- [Knowledge Graphs in n8n are FINALLY Here!](../../sources/knowledge-graphs-in-n8n-are-finally-here.md) - "[0:06:25] graffiti is the library. It's the tooling that gives us the ability to extract from raw text the entities and relationships to then store in Neo4j and it gives us the MCP server that makes it possible to use graffiti with nan."
- [The ONLY AI Tech Stack You Need in 2026](../../sources/the-only-ai-tech-stack-you-need-in-2026.md) - "[0:16:16] for the library to help us insert data into Neoforj and search our knowledge graphs here. I love using graffiti... very intelligent entity and relationship extraction."
- [The PROVEN Solution for Unbelievable RAG Performance (LightRAG Guide)](../../sources/the-proven-solution-for-unbelievable-rag-performance-lightrag-guide.md) - "[0:09:57] The solution to this is a powerful open-source platform for building real time knowledge graphs called Graffiti... it powers the core of Zep's memory layer."
- [Introducing RAG 2.0: Agentic RAG + Knowledge Graphs (FREE Template)](../../sources/introducing-rag-20-agentic-rag-knowledge-graphs-free-template.md) - "[0:21:09] all of these different um episodes as they're called with graffiti... the different entities and their relationships, all of this has to be defined by large language models."
- [Every RAG Strategy Explained in 13 Minutes (No Fluff)](../../sources/every-rag-strategy-explained-in-13-minutes-no-fluff.md) - "[0:05:14] This is the pseudo code if you want to see an example using graffiti which is my favorite library for working with knowledge graphs."
- [All the BEST RAG Strategies in ONE MCP for AI Coding Assistants](../../sources/all-the-best-rag-strategies-in-one-mcp-for-ai-coding-assistants.md) - "[0:18:51] building out a gentic rag with knowledge graphs with something like graffiti or light rag."
- [Should I Build My AI Agents with n8n or Python?](../../sources/should-i-build-my-ai-agents-with-n8n-or-python.md) - "[0:13:13] All these things that I've covered on my channel like graffiti for knowledge graphs, dockling for rag."
