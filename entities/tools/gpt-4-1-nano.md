---
type: entity
subtype: tool
title: "GPT-4.1 Nano"
description: "OpenAI's smallest, cheapest model in the GPT-4.1 line, used for the per-chunk context-generation call in contextual retrieval because the task needs almost no reasoning power."
tags: [llm, model, cost, model-selection]
videos: [the-easiest-possible-strategy-for-accurate-rag-step-by-step-guide]
created: 2026-07-21
updated: 2026-07-21
---

# GPT-4.1 Nano

GPT-4.1 Nano is the smallest and cheapest model in OpenAI's GPT-4.1 line, and Cole picks it for exactly the reason it exists: the job is high-volume and nearly reasoning-free. In the contextual retrieval pipeline he states the choice plainly: "[0:13:40] I am using GPT 4.1 Nano. So, I'm using the smallest model offered from OpenAI. It is dirt cheap and we don't need that much reasoning power here." It is the clearest worked example in the catalog of matching model size to task difficulty rather than defaulting to the best model available.

The task is one LLM call per chunk. Each chunk plus its full source document goes to the model with Anthropic's situating prompt, and one or two sentences of context come back to be prepended before embedding. That is trivially easy language work, but it runs across every chunk of an entire knowledge base, so the cost profile is the inverse of a coding agent: negligible per call, enormous in aggregate. Two levers keep the bill down, a tiny model and [prompt caching](../../concepts/prompt-caching.md) on the repeated document tokens, which discounts the bulk of every request.

The surrounding pipeline is built in [n8n](./n8n.md): a Drive trigger, a custom 400-character chunker, the Nano call per chunk, then insertion into a [Neon](./neon.md) Postgres vector store with the generated context prepended and metadata attached for citation. The technique is model-agnostic (Cole ships the same logic in Python inside his RAG MCP server), so Nano here is a cost decision, not an architectural one. Anyone reproducing it should substitute whatever the current cheapest small model is.

## Realizes

- [Model Selection](../../concepts/model-selection.md) - Choosing the right LLM per task by trading off quality, speed, and cost, often routing easy requests to cheap models and hard ones to expensive models.
- [LLM Cost Optimization](../../concepts/llm-cost-optimization.md) - Sending the bulk of cheap-to-serve traffic to far cheaper models and paying premium rates only where reasoning is actually required.
- [Contextual Retrieval](../../concepts/contextual-retrieval.md) - Prepending LLM-generated context to each chunk before embedding so retrieval understands where the chunk sits in the larger document.
- [Chunking](../../concepts/chunking.md) - Splitting source documents into embeddable segments, the step whose output this model annotates.
- [Prompt Caching](../../concepts/prompt-caching.md) - Caching the repeated document tokens across per-chunk calls, which is what makes running a model over an entire corpus affordable.

## Contrasts with

- [GPT-4o mini](./gpt-4o-mini.md) - The previous generation's cheap tier, the model this one displaces for bulk, low-reasoning work.
- [GPT-5.4 Mini & Nano](./gpt-5-4-mini-nano.md) - The later small models that inherit the same role, underlining that the size tier matters more than the specific name.

## Works with

- [n8n](./n8n.md) - The no-code platform where the per-chunk call is wired as a node inside the ingestion loop.
- [Neon](./neon.md) - The serverless Postgres vector store that receives the context-prefixed chunks.
- [Google Drive](./google-drive.md) - The trigger and document source feeding the pipeline that this model annotates.
- [Crawl4AI RAG MCP Server](./crawl4ai-rag-mcp.md) - Cole's Python implementation of the same contextual-embedding step, showing the technique outside n8n.

## Related

- [Retrieval-Augmented Generation (RAG)](../../concepts/rag.md) - Grounding answers by retrieving relevant documents, the system this preprocessing step exists to improve.
- [Production-Ready RAG](../../concepts/production-ready-rag.md) - Building retrieval that survives a growing, changing knowledge base rather than a toy demo.
- [Stacking Context-Engineering Strategies](../../concepts/strategy-stacking.md) - Composing contextual retrieval with hybrid search, reranking, and query expansion for compounding accuracy gains.
- [Vector Embeddings](../../concepts/vector-embeddings.md) - The representations the generated context is prepended to before storage.
- [Context-Aware Chunking](../../concepts/context-aware-chunking.md) - Enriching chunks with surrounding context, the family of techniques this call belongs to.

## Sources

- [The EASIEST Possible Strategy for Accurate RAG (Step by Step Guide)](../../sources/the-easiest-possible-strategy-for-accurate-rag-step-by-step-guide.md) - "[0:13:40] I am using GPT 4.1 Nano. So, I'm using the smallest model offered from OpenAI. It is dirt cheap and we don't need that much reasoning power here"
