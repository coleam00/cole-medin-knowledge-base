---
type: source
title: "Knowledge Graphs in n8n are FINALLY Here!"
description: "You can layer a knowledge graph onto an existing n8n vector-database RAG template using the Graphiti MCP server and Neo4j, giving your agent a second, relationship-aware way to search its knowledge base."
youtube_id: NQ3vJ8iZPaQ
url: https://www.youtube.com/watch?v=NQ3vJ8iZPaQ
slug: knowledge-graphs-in-n8n-are-finally-here
published: 2025-09-23
duration: "0:18:55"
recency_rank: 69
raw: "../raw/knowledge-graphs-in-n8n-are-finally-here.md"
tags: [knowledge-graphs, n8n, rag, neo4j]
created: 2026-07-21
updated: 2026-07-21
---

Cole extends his ongoing n8n RAG template by adding knowledge graphs alongside the existing vector database. He starts from RAG fundamentals: traditional RAG chunks source data (for example from Google Drive) and stores it in a vector database like Postgres/pgvector, Qdrant, or Pinecone, but vector stores are poor at capturing relationships between entities (people, companies, products). A knowledge graph fills that gap by storing entities as nodes and their relationships as edges, letting the agent navigate between related items. Both stores are built up simultaneously from the same data, just represented differently. This is agentic RAG: the agent chooses which store to query, using the vector DB for single-entity overviews and the knowledge graph for relational questions spanning multiple entities.

The build hinges on the Graphiti MCP server backed by Neo4j. Cole clarifies the division of labor: Neo4j is the graph database (analogous to Postgres) and Graphiti is the library and tooling that uses an LLM (OpenAI by default) to extract entities and relationships from raw text and exposes an MCP server for n8n to call. Setup requires self-hosted n8n (the cloud version will not work) on something like a DigitalOcean droplet, running Graphiti plus Neo4j via a single docker compose. Gotchas covered: point the URL at the Neo4j service name rather than localhost inside containers, add host.docker.internal as an extra host in n8n's compose, and open only the n8n gateway IP to the Graphiti port via UFW rather than exposing it publicly.

Inside n8n, because the native MCP integration only supports MCP servers as agent tools, Cole installs the n8n-nodes-mcp community node to also call Graphiti during ingestion. Only two nodes are added to the template: an add-memory call in the RAG pipeline (passing document name plus episode body for the LLM to extract entities and relationships) and a search-memory-nodes tool for the agent (where the LLM decides the query). He closes with a caveat: knowledge graphs are slower and more expensive because an LLM extracts every node, so for large data or non-relational use cases a plain vector database may be the better choice.

## Concepts covered

- [Knowledge Graphs](../concepts/knowledge-graphs.md)
- [Traditional RAG](../concepts/traditional-rag.md)
- [Agentic RAG](../concepts/agentic-rag.md)
- [Chunking](../concepts/chunking.md)
- [Vector Embeddings](../concepts/vector-embeddings.md)
- [Model Context Protocol (MCP)](../concepts/mcp.md)

## Entities

- [n8n](../entities/tools/n8n.md)
- [Graphiti](../entities/tools/graphiti.md)
- [Neo4j](../entities/tools/neo4j.md)
- [MCP (Model Context Protocol)](../entities/tools/mcp.md)
- [Postgres](../entities/tools/postgres-pgvector.md)
- [OpenAI](../entities/organizations/openai.md)
- [DigitalOcean](../entities/organizations/digital-ocean.md)
- [Docker](../entities/tools/docker.md)
- [Cole Medin](../entities/people/cole-medin.md)

## Key moments

- **[0:00:30]** Returns to RAG fundamentals to motivate layering knowledge graphs on top
- **[0:01:33]** Core problem: vector databases don't store relationships between entities
- **[0:02:04]** Knowledge graph built simultaneously with the vector database via a single node
- **[0:03:26]** Live demo: vector DB for a single-company overview, knowledge graph for relational questions
- **[0:06:25]** Clarifies Neo4j = graph database, Graphiti = LLM extraction library + MCP server
- **[0:07:00]** Docker compose setup of Graphiti + Neo4j on a DigitalOcean droplet
- **[0:10:26]** Hacky networking: host.docker.internal + UFW rule scoped to the n8n gateway IP
- **[0:13:13]** Install the n8n-nodes-mcp community node (native MCP only supports tools)
- **[0:15:51]** The two added nodes: add-memory in the pipeline, search-memory-nodes as an agent tool
- **[0:17:40]** Caveat: knowledge graphs are slower/more expensive; not always worth it

## Transcript

[Raw transcript](../raw/knowledge-graphs-in-n8n-are-finally-here.md)
