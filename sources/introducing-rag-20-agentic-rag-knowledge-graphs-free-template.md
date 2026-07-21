---
type: source
title: "Introducing RAG 2.0: Agentic RAG + Knowledge Graphs (FREE Template)"
description: "Combining agentic RAG with knowledge graphs gives an AI agent the flexibility to reason about how it retrieves knowledge, choosing a vector database for single-entity lookups and a knowledge graph for relational questions."
youtube_id: p0FERNkpyHE
url: https://www.youtube.com/watch?v=p0FERNkpyHE
slug: introducing-rag-20-agentic-rag-knowledge-graphs-free-template
published: 2025-06-25
duration: "0:38:49"
recency_rank: 83
raw: "../raw/introducing-rag-20-agentic-rag-knowledge-graphs-free-template.md"
tags: [rag, agentic-rag, knowledge-graphs, pydantic-ai]
created: 2026-07-21
updated: 2026-07-21
---

# Introducing RAG 2.0: Agentic RAG + Knowledge Graphs (FREE Template)

Cole introduces a free, neatly-packaged agent template that unites two retrieval strategies he keeps returning to: agentic RAG and knowledge graphs. He demos a CLI talking to a Pydantic AI agent that has both a Postgres/pgvector vector database (on Neon) and a Neo4j knowledge graph (built with Graphiti) as tools. Because the same corpus of documents is stored both as embedded chunks and as a graph of entities and relationships, the agent can reason about which source to hit: a vector search for information about a single company like Google, a graph search for how two companies like OpenAI and Microsoft relate, or both.

The middle of the video walks through the evolution of RAG. Naive/vanilla RAG chunks documents, embeds them, and force-feeds the top matches into the prompt as a rigid pre-processing step, which is inflexible because the agent must use whatever context it gets with no ability to refine or explore multiple sources. Agentic RAG fixes this by turning retrieval into agent tools, letting the LLM formulate queries, pick sources, and even supplement with web search. Cole then gives a full setup guide: prerequisites (Python, a Postgres DB, Neo4j, an OpenAI-compatible LLM key), running the SQL schema, ingesting markdown documents into both stores (noting knowledge-graph ingestion is slow because an LLM must extract every entity and relationship), and tuning the system prompt in prompts.py to control when the agent uses each tool.

The final segment shows how he used Claude Code to build the template. He relies on two MCP servers (his Crawl4AI RAG server for pulling in Pydantic AI docs, and Neon's MCP for autonomous database management), Claude Code's plan mode (shift+tab twice) to produce a planning.md and task.md alongside a claude.md of global rules, and an examples folder of prior code for the agent to reference. He is explicit that he does not condone vibe coding: he stresses validating the AI's output and adding the last 10% yourself.

## Concepts covered

- [Agentic RAG](../concepts/agentic-rag.md)
- [Knowledge Graphs](../concepts/knowledge-graphs.md)
- [Traditional RAG](../concepts/traditional-rag.md)
- [Retrieval-Augmented Generation (RAG)](../concepts/rag.md)
- [Vector Embeddings](../concepts/vector-embeddings.md)
- [Chunking](../concepts/chunking.md)
- [Structured vs Unstructured Data](../concepts/structured-vs-unstructured-data.md)
- [Planning with AI](../concepts/planning-with-ai.md)
- [Global Rules](../concepts/global-rules.md)
- [Vibe Coding](../concepts/vibe-coding.md)
- [Agentic Coding](../concepts/agentic-coding.md)
- [Model Context Protocol (MCP)](../concepts/mcp.md)

## Entities

- [Pydantic AI](../entities/tools/pydantic-ai.md)
- [Graphiti](../entities/tools/graphiti.md)
- [Neo4j](../entities/tools/neo4j.md)
- [Postgres](../entities/tools/postgres-pgvector.md)
- [Neon](../entities/tools/neon.md)
- [FastAPI](../entities/tools/fastapi.md)
- [Claude Code](../entities/tools/claude-code.md)
- [MCP (Model Context Protocol)](../entities/tools/mcp.md)
- [OpenAI](../entities/organizations/openai.md)
- [Cole Medin](../entities/people/cole-medin.md)
- [Dynamous](../entities/organizations/dynamous.md)

## Key moments

- **[0:01:05]** CLI demo of the agentic RAG agent with both a vector DB and knowledge graph as tools
- **[0:03:13]** Asking about Google triggers only vector search; asking how OpenAI/Microsoft relate triggers graph search
- **[0:05:25]** Tech stack rundown: Pydantic AI, Graphiti, Neo4j, Postgres/pgvector, FastAPI, Claude Code
- **[0:06:57]** Weaviate article: vanilla/naive RAG explained and why it is inflexible
- **[0:08:49]** Agentic RAG diagram: giving the agent the ability to reason about how it explores the knowledge base
- **[0:10:35]** Template setup begins: prerequisites, SQL schema, .env configuration
- **[0:20:05]** Running ingestion; vector insert is seconds, knowledge-graph build takes minutes
- **[0:22:37]** Configuring agent behavior via prompts.py system prompt to route between tools
- **[0:28:11]** How Claude Code built the template: MCP servers, plan mode, planning/task docs, examples
- **[0:36:40]** Explicitly does NOT condone vibe coding; validate output and add the last 10%

## Transcript

[Raw transcript](../raw/introducing-rag-20-agentic-rag-knowledge-graphs-free-template.md)
