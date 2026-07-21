---
type: entity
subtype: tool
title: "Redis"
description: "In-memory cache bundled alongside SearXNG for caching web-search results."
resource: "https://redis.io"
tags: [cache, in-memory, local-ai, backend]
videos: [create-your-own-private-local-ai-cloud-stack-in-under-20-minutes, local-vs-cloud-llmsrag-lets-finally-end-this-debate]
created: 2026-07-21
updated: 2026-07-21
---

# Redis

Redis is an in-memory data store that shows up in Cole's local-AI stacks as the caching layer bundled alongside SearXNG for private web search. In his private local AI cloud stack it is one of the supporting services, "SearXNG for local and private web search which includes Redis for caching" (create-your-own-private-local-ai-cloud-stack, 0:02:12). It plays the same role in his self-hosted local-versus-cloud walkthrough, where he lists it plainly as "finally redis for caching" (local-vs-cloud-llms-rag, 0:02:19) and again as "redis doio for your posted redis caching" (local-vs-cloud-llms-rag, 0:02:53).

Unlike Postgres, Supabase, or Neon, Redis is not the system of record in Cole's builds; it is a fast ephemeral cache that keeps the search stack responsive without hitting slower services on every request. Its appearance is tied to the SearXNG search component of the local stack rather than to RAG storage or agent memory, which Cole keeps in a durable Postgres-backed store instead.

## Works with

- [Redis Iris](./redis-iris.md) - A preview Redis product that wraps the database with a Context Retriever (auto-generated MCP tools over defined entities/schema) and Agent Memory (short/long-term with background promotion to vector-indexed memory), demoed as the production-agent substitute for markdown second brains.
- [Ollama](./ollama.md) - the local LLM runtime that rounds out the same self-hosted stack Redis caches for.
- [Local & Self-Hosted AI](../../concepts/local-ai.md) - running open-weight models on your own hardware or cloud; the setting where Cole runs Redis as part of a private, fully self-hosted stack.

## Related

- [Agent Deployment](../../concepts/agent-deployment.md) - getting agents to production; shaped by keeping the whole stack, cache included, running locally.
- [Agent Security](../../concepts/agent-security.md) - sandboxing agents and keeping secrets out of the model; served by keeping the stack self-hosted.
- [Rapid Prototyping](../../concepts/rapid-prototyping.md) - building a fast proof of concept first; benefits from the pre-bundled cache in the ready-to-run local stack.
- [Retrieval-Augmented Generation (RAG)](../../concepts/rag.md) - grounding an LLM's answers with retrieved documents; a surrounding workload the cached search results feed into.
- [Model Selection](../../concepts/model-selection.md) - choosing the right LLM per task; another surrounding workload in the same stack.

## Sources

- [Create Your Own Private Local AI Cloud Stack in Under 20 Minutes](../../sources/create-your-own-private-local-ai-cloud-stack-in-under-20-minutes.md) - "[0:02:12] SearXNG for local and private web search which includes Redis for caching"
- [Local vs. Cloud LLMs/RAG - Let's FINALLY End this Debate](../../sources/local-vs-cloud-llmsrag-lets-finally-end-this-debate.md) - "[0:02:19] finally redis for caching"
