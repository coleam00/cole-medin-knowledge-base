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

nomic-embed-text is the local embedding model Cole pulls into [Ollama](./ollama.md) so his RAG pipelines have something to turn text into [Vector Embeddings](../../concepts/vector-embeddings.md) without calling a cloud API. It is the default that ships with his local AI stack: "I'm just using namic embed text that's the model that comes with the local AI package by default" - ["The ULTIMATE n8n RAG AI Agent Template - Local AI Edition"](../../sources/the-ultimate-n8n-rag-ai-agent-template-local-ai-edition.md) [0:21:08]. Where a chat model answers questions, this model does the quieter, foundational job of encoding documents and queries into the vectors that [Retrieval-Augmented Generation (RAG)](../../concepts/rag.md) searches over.

## How Cole uses it

In Cole's local and self-hosted builds, embeddings are a prerequisite that is easy to forget, and nomic-embed-text is the piece that fills the gap. Setting up a deployment, he pulls it explicitly alongside the chat model: "I want to add in another model so I'm going to pull the embedding model as well namic embed text because without this available we don't actually have a model available to us for our embeddings for Rag" - ["Deploy ANY AI App to the Cloud FAST"](../../sources/deploy-any-ai-app-to-the-cloud-fast.md) [0:07:39]. That line captures its role precisely: it is not the star of the workflow, it is the dependency that makes RAG possible at all when you run everything locally.

Because it is served through Ollama as a container pull, nomic-embed-text keeps the whole retrieval stack free of external embedding costs and off third-party APIs, which is the point of Cole's [Local & Self-Hosted AI](../../concepts/local-ai.md) templates. It handles the unstructured side of ingestion: documents get chunked, each chunk is embedded with this model, and the resulting vectors land in a store (typically pgvector via [Supabase](./supabase.md)) for similarity search at query time.

## Related

- [Vector Embeddings](../../concepts/vector-embeddings.md) - nomic-embed-text is the model that produces them locally.
- [Retrieval-Augmented Generation (RAG)](../../concepts/rag.md) - embeddings are the retrieval substrate it feeds.
- [Traditional RAG](../../concepts/traditional-rag.md) - the vector-similarity approach it enables.
- [Agentic RAG](../../concepts/agentic-rag.md) - the same embeddings power agent-driven retrieval.
- [Chunking](../../concepts/chunking.md) - text is chunked before it is embedded.
- [Structured vs Unstructured Data](../../concepts/structured-vs-unstructured-data.md) - embeddings handle the unstructured half.
- [Ollama](./ollama.md) - serves the model as a local container pull.
- [Local AI Package](./local-ai-package.md) - the stack that ships nomic-embed-text as its default.
- [Supabase](./supabase.md) - pgvector store the embeddings are written to.

## Sources

- [The ULTIMATE n8n RAG AI Agent Template - Local AI Edition](../../sources/the-ultimate-n8n-rag-ai-agent-template-local-ai-edition.md) - "[0:21:08] I'm just using namic embed text that's the model that comes with the local AI package by default"
- [Deploy ANY AI App to the Cloud FAST](../../sources/deploy-any-ai-app-to-the-cloud-fast.md) - "[0:07:39] I want to add in another model so I'm going to pull the embedding model as well namic embed text because without this available we don't actually have a model available to us for our embeddings for Rag"
