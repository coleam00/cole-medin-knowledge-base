---
type: entity
subtype: tool
title: "Neo4j"
description: "The graph database used to store and visualize the repository knowledge graph."
resource: "https://neo4j.com"
tags: [knowledge-graphs, graph-database, open-source]
videos: [the-only-ai-tech-stack-you-need-in-2026, knowledge-graphs-in-n8n-are-finally-here, introducing-rag-20-agentic-rag-knowledge-graphs-free-template, ai-code-that-fixes-itself-an-mcp-you-can-try-now, make-rag-100x-better-with-real-time-knowledge-graphs, the-proven-solution-for-unbelievable-rag-performance-lightrag-guide]
created: 2026-07-21
updated: 2026-07-21
---

# Neo4j

Neo4j is the graph database Cole uses as the storage engine beneath his [knowledge graphs](../../concepts/knowledge-graphs.md). He draws a clean division of labor: the extraction library does the thinking, Neo4j does the storing. "Neo4j is the database like postgress where we store our knowledge graph" ([0:06:25]), or as he puts it in his stack overview, "for the graph database, what I like to call the engine, I love using Neo4j. They have a really beautiful UI" ([0:15:49]). That UI matters to how Cole works, because he leans on Neo4j's node-and-edge visualization to inspect and debug what his pipelines produce.

## How Cole uses it

In Cole's [agentic RAG](../../concepts/agentic-rag.md) template, Neo4j is "the underlying knowledge graph engine that's the user interface that we saw earlier with all of the nodes" ([0:05:41]), paired with [Graphiti](./graphiti.md) as the extraction layer that inserts and searches. When he demonstrates the knowledge-graph hallucination check in his [Crawl4AI RAG MCP Server](./crawl4ai-rag-mcp.md), he inspects the parsed repository visually: "let me go ahead and zoom in on the center node of our graph that I have here in my Neo-4j graph visualization" ([0:01:27]). The same visual engine powers his temporal-graph demos: "this is Neo4j. That is the engine behind the scenes powering our knowledge graph for the graffiti" ([0:02:33]).

Because Neo4j is open source, it fits Cole's [local AI](../../concepts/local-ai.md) posture. "we can host Neo4j completely locally since it is an open- source knowledge graph engine" ([0:06:40]), and he gives viewers "two different ways for you to get Neo4j up and running that I would recommend" ([0:14:01]) - through his [local AI package](./local-ai-package.md) or via Neo4j Desktop: "you can install Neo4j either through my local AI package... or you can install Neo4j desktop very easily as well" ([0:12:54]). In no-code builds it ships together with Graphiti: "with a single docker compose we're going to have the graffiti mcp server and neo-4j which is our underlying database hosted" ([0:06:06]).

Cole also uses Neo4j to draw the line between graph storage and vector storage. Comparing it to [Supabase](./supabase.md) Postgres, he explains, "You can use Neo4j for the knowledge graph and then also you can use Postgress" ([0:04:21]), and his own preferred split is "using Neo4j for just the knowledge graph and then Postgress for just the vector database" ([0:04:38]) - graph structure in one engine, [vector embeddings](../../concepts/vector-embeddings.md) in another.

## Related

- [Knowledge Graphs](../../concepts/knowledge-graphs.md) - Neo4j is the database that stores and visualizes them.
- [Agentic RAG](../../concepts/agentic-rag.md), [RAG](../../concepts/rag.md), [Traditional RAG](../../concepts/traditional-rag.md) - the graph half of these strategies lives in Neo4j.
- [Local & Self-Hosted AI](../../concepts/local-ai.md) - it self-hosts locally as open source.
- [Vector Embeddings](../../concepts/vector-embeddings.md) and [Chunking](../../concepts/chunking.md) - the complementary vector side he keeps in Postgres.
- Sibling tools: [Graphiti](./graphiti.md) (its extraction layer), [LightRAG](./lightrag.md), [Supabase](./supabase.md), [Local AI Package](./local-ai-package.md), [n8n](./n8n.md).

## Sources

- [The ONLY AI Tech Stack You Need in 2026](../../sources/the-only-ai-tech-stack-you-need-in-2026.md) - "[0:15:49] for the graph database, what I like to call the engine, I love using Neo4j. They have a really beautiful UI."
- [Knowledge Graphs in n8n are FINALLY Here!](../../sources/knowledge-graphs-in-n8n-are-finally-here.md) - "[0:06:25] Neo4j is the database like postgress where we store our knowledge graph."
- [Introducing RAG 2.0: Agentic RAG + Knowledge Graphs (FREE Template)](../../sources/introducing-rag-20-agentic-rag-knowledge-graphs-free-template.md) - "[0:05:41] Neo4j which is the underlying knowledge graph engine that's the user interface that we saw earlier with all of the nodes."
- [AI Code That Fixes Itself (An MCP You Can Try Now)](../../sources/ai-code-that-fixes-itself-an-mcp-you-can-try-now.md) - "[0:12:54] you can install Neo4j either through my local AI package... or you can install Neo4j desktop very easily as well."
- [Make RAG 100x Better with Real-Time Knowledge Graphs](../../sources/make-rag-100x-better-with-real-time-knowledge-graphs.md) - "[0:06:40] we can host Neo4j completely locally since it is an open- source knowledge graph engine."
- [The PROVEN Solution for Unbelievable RAG Performance (LightRAG Guide)](../../sources/the-proven-solution-for-unbelievable-rag-performance-lightrag-guide.md) - "[0:04:38] What I've been playing with is using Neo4j for just the knowledge graph and then Postgress for just the vector database."
