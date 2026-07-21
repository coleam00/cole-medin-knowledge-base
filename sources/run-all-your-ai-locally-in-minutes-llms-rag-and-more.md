---
type: source
title: "Run ALL Your AI Locally in Minutes (LLMs, RAG, and more)"
description: "The n8n self-hosted AI starter kit bundles Ollama, Qdrant, Postgres, and n8n into one Docker package that lets you stand up a fully local RAG AI agent in minutes, with a few key customizations to fill gaps in the official setup."
youtube_id: V_0dNE-H2gw
url: https://www.youtube.com/watch?v=V_0dNE-H2gw
slug: run-all-your-ai-locally-in-minutes-llms-rag-and-more
published: 2024-09-15
duration: "0:20:21"
recency_rank: 165
raw: "../raw/run-all-your-ai-locally-in-minutes-llms-rag-and-more.md"
tags: [local-ai, rag, n8n, self-hosting]
created: 2026-07-21
updated: 2026-07-21
---

# Run ALL Your AI Locally in Minutes (LLMs, RAG, and more)

Cole walks through n8n's self-hosted AI starter kit, a single Docker Compose package that bundles Ollama (local LLMs), Qdrant (vector database), Postgres (SQL database), and n8n (workflow automation) so you can run all your AI infrastructure locally. He argues local AI is the way of the future now that open-source models like Llama 3.1 are competitive with closed models like GPT and Claude. Setup is just cloning the repo, editing the .env file for Postgres and n8n credentials, and running a Docker Compose command tailored to your architecture (GPU, Mac, or CPU).

He fills two gaps the official readme misses: exposing the Postgres port (5432) so it can back agent chat memory, and adding a line to pull an Ollama embedding model needed for RAG. He then demonstrates a complete local RAG agent built in n8n: Ollama 3.1 as the chat model (referenced via host.docker.internal:11434), Postgres for chat memory, and Qdrant as the vector store tool. The Qdrant dashboard at localhost:6333 gives visibility into collections, vectors, chunks, and metadata.

The most important lesson is in the ingestion pipeline: n8n's vector inserter is an insert, not an upsert, so re-ingesting an updated document creates duplicate vectors that confuse the LLM. Cole's fix is a custom code node using LangChain to delete all existing vectors matching the file's ID (stored as metadata) before re-inserting, guaranteeing zero duplicates. He uses a small 100-character chunk size to keep context low for his modest local hardware, and closes by teasing future extensions like Redis caching and Supabase instead of vanilla Postgres.

## Concepts covered

- [Local & Self-Hosted AI](../concepts/local-ai.md)
- [Retrieval-Augmented Generation (RAG)](../concepts/rag.md)
- [Agentic RAG](../concepts/agentic-rag.md)
- [Vector Embeddings](../concepts/vector-embeddings.md)
- [Chunking](../concepts/chunking.md)
- [Memory Systems](../concepts/memory-systems.md)
- [Knowledge Bases](../concepts/knowledge-bases.md)

## Entities

- [n8n](../entities/tools/n8n.md)
- [Ollama](../entities/tools/ollama.md)
- [Qdrant](../entities/tools/qdrant.md)
- [Postgres](../entities/tools/postgres-pgvector.md)
- [Docker](../entities/tools/docker.md)
- [Llama](../entities/tools/llama.md)
- [LangChain](../entities/tools/langchain.md)
- [Google Drive](../entities/tools/google-drive.md)
- [Cole Medin](../entities/people/cole-medin.md)

## Key moments

- **[0:00:14]** Introduces the n8n self-hosted AI starter kit: Ollama plus Qdrant plus Postgres plus n8n in one package
- **[0:01:18]** Walks through the GitHub repo: just .env and docker-compose.yml matter
- **[0:03:42]** Fix #1: expose Postgres port 5432 so it can back agent chat memory
- **[0:04:30]** Fix #2: add a line to pull an Ollama embedding model for RAG
- **[0:05:15]** Start the stack with docker compose --profile cpu up
- **[0:07:48]** Build a fully local RAG AI agent in n8n
- **[0:09:13]** Wire up Ollama chat model via host.docker.internal:11434
- **[0:10:01]** Wire Postgres chat memory and Qdrant vector store tool
- **[0:11:30]** Qdrant self-hosted dashboard at localhost:6333 for collection and vector visibility
- **[0:12:47]** Google Drive ingestion pipeline: trigger on file create or update
- **[0:14:04]** Critical: insert is not upsert; delete old vectors by file-ID metadata before re-inserting
- **[0:16:36]** Chunk size of 100 chars keeps context small for modest local hardware
- **[0:18:04]** Test the agent; Llama 3.1 correctly answers from the ingested meeting-notes document
- **[0:19:25]** Future extensions: Redis caching, Supabase, front end, RAG best-practice templates

## Transcript

[Raw transcript](../raw/run-all-your-ai-locally-in-minutes-llms-rag-and-more.md)
