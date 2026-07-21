---
type: entity
subtype: tool
title: "nomic-embed-text"
description: "Embedding model added to the Ollama container pull so RAG embeddings are available in the workflows."
resource: "https://ollama.com/library/nomic-embed-text"
tags: [embeddings, local-ai, ollama, rag]
videos: [the-ultimate-n8n-rag-ai-agent-template-local-ai-edition, deploy-any-ai-app-to-the-cloud-fast]
created: 2026-07-21
updated: 2026-07-21
---

# nomic-embed-text

nomic-embed-text is the local embedding model Cole pulls into [Ollama](./ollama.md) so his RAG pipelines have something to turn text into [Vector Embeddings](../../concepts/vector-embeddings.md) without calling a cloud API. It is the default that ships with his local AI stack: "I'm just using nomic-embed-text that's the model that comes with the local AI package by default" - ["The ULTIMATE n8n RAG AI Agent Template - Local AI Edition"](../../sources/the-ultimate-n8n-rag-ai-agent-template-local-ai-edition.md) [0:21:08]. Where a chat model answers questions, this model does the quieter, foundational job of encoding documents and queries into the vectors that [Retrieval-Augmented Generation (RAG)](../../concepts/rag.md) searches over.

## How Cole uses it

In Cole's local and self-hosted builds, embeddings are a prerequisite that is easy to forget, and nomic-embed-text is the piece that fills the gap. Setting up a deployment, he pulls it explicitly alongside the chat model: "I want to add in another model so I'm going to pull the embedding model as well nomic-embed-text because without this available we don't actually have a model available to us for our embeddings for Rag" - ["Deploy ANY AI App to the Cloud FAST"](../../sources/deploy-any-ai-app-to-the-cloud-fast.md) [0:07:39]. That line captures its role precisely: it is not the star of the workflow, it is the dependency that makes RAG possible at all when you run everything locally.

Because it is served through Ollama as a container pull, nomic-embed-text keeps the whole retrieval stack free of external embedding costs and off third-party APIs, which is the point of Cole's [Local & Self-Hosted AI](../../concepts/local-ai.md) templates. It handles the unstructured side of ingestion: documents get chunked, each chunk is embedded with this model, and the resulting vectors land in a store (typically pgvector via [Supabase](./supabase.md)) for similarity search at query time.

## Realizes

- [Vector Embeddings](../../concepts/vector-embeddings.md) - Numeric representations of text that enable semantic similarity search, stored and managed in a vector database for retrieval.

## Works with

- [Ollama](./ollama.md) - Local LLM runtime; works with a locally-run bolt.diy but can't be reached by a self-hosted (remote) instance.
- [Local AI Package](./local-ai-package.md) - Cole's bundled collection of self-hosted AI services (database, n8n, Ollama, Open Web UI) that installs the whole stack together for free.
- [Supabase](./supabase.md) - A single platform providing Postgres for scalable chat memory plus the pgvector store for RAG embeddings, recommended over in-memory alternatives.

## Related

- [Retrieval-Augmented Generation (RAG)](../../concepts/rag.md) - Grounding an LLM's answers by retrieving relevant documents from an external knowledge base and injecting them into the prompt at query time.
- [Traditional RAG](../../concepts/traditional-rag.md) - The classic one-shot, static RAG pipeline that embeds a query, runs a single vector similarity search, and stuffs the top chunks into the prompt.
- [Agentic RAG](../../concepts/agentic-rag.md) - Giving an agent retrieval as a tool so it decides when and how to search a knowledge base, picking strategies and issuing follow-up queries instead of a single static lookup.
- [Chunking](../../concepts/chunking.md) - Splitting source documents into appropriately sized, embeddable segments, the foundational preprocessing step that determines RAG retrieval quality.
- [Structured vs Unstructured Data](../../concepts/structured-vs-unstructured-data.md) - Choosing the right representation for RAG, keeping tabular data queryable as SQL while formatting prose as markdown, rather than forcing everything through vector search.
- [Local & Self-Hosted AI](../../concepts/local-ai.md) - Running open-weight models on your own hardware or cloud for privacy, cost control, and independence from API providers.

## Sources

- [The ULTIMATE n8n RAG AI Agent Template - Local AI Edition](../../sources/the-ultimate-n8n-rag-ai-agent-template-local-ai-edition.md) - "[0:21:08] I'm just using nomic-embed-text that's the model that comes with the local AI package by default"
- [Deploy ANY AI App to the Cloud FAST](../../sources/deploy-any-ai-app-to-the-cloud-fast.md) - "[0:07:39] I want to add in another model so I'm going to pull the embedding model as well nomic-embed-text because without this available we don't actually have a model available to us for our embeddings for Rag"
