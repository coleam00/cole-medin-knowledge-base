---
type: entity
subtype: tool
title: "n8n Self-Hosted AI Starter Kit"
description: "n8n's official Docker Compose package bundling Ollama, Qdrant, Postgres, and n8n so a fully local AI stack (LLMs, vector DB, SQL DB, orchestration) starts with one command."
resource: "https://github.com/n8n-io/self-hosted-ai-starter-kit"
tags: [deployment, infrastructure, local-ai, self-hosting, privacy]
videos: [run-all-your-ai-locally-in-minutes-llms-rag-and-more]
created: 2026-07-21
updated: 2026-07-21
---

# n8n Self-Hosted AI Starter Kit

The n8n Self-Hosted AI Starter Kit is one Docker Compose file that stands up four services at once: [Ollama](./ollama.md) for local LLMs, [Qdrant](./qdrant.md) for vectors, [Postgres](./postgres-pgvector.md) for SQL and chat memory, and [n8n](./n8n.md) for orchestration. You clone the repo, fill in the `.env` with Postgres credentials and n8n encryption secrets, and run the compose profile that matches your hardware (GPU, Mac, or CPU). That is the whole install. Cole reaches for it because the economics have flipped: "running your own AI infrastructure is the way of the future especially because of how accessible is becoming and because open-source models like llama are getting to the point where they're so powerful" ([0:00:47](../../sources/run-all-your-ai-locally-in-minutes-llms-rag-and-more.md)).

Two gaps in the official readme are worth patching before you build anything on it. The Postgres port (5432) is not exposed by default, so it cannot back agent chat memory until you publish it, and no embedding model is pulled, so [RAG](../../concepts/rag.md) silently has nothing to embed with until you add a line to pull one (Cole uses [nomic-embed-text](./nomic-embed-text.md)). Once both are fixed, a complete local RAG agent is buildable inside n8n: Llama 3.1 as the chat model, Postgres as memory, Qdrant as the vector-store tool, with the Qdrant dashboard on localhost:6333 showing collections, chunks, and metadata.

The kit is also where the [delete-before-insert re-ingestion](../../concepts/delete-before-insert-reingestion.md) lesson surfaces: n8n's vector inserter inserts rather than upserts, so re-ingesting an edited document quietly doubles its chunks until you delete the old ones by file-ID metadata first. Everything runs on your own box, which is the entire point: "it's fully fully local it is just a beautiful thing so I hope that this whole local AI setup is just as cool for you as it is for me" ([0:19:12](../../sources/run-all-your-ai-locally-in-minutes-llms-rag-and-more.md)). The same kit later doubles as the worked example for taking a localhost stack to a real domain with a reverse proxy and TLS.

## Realizes

- [Local & Self-Hosted AI](../../concepts/local-ai.md) - Running open-weight models on your own hardware or cloud for privacy, cost control, and independence from API providers.
- [LLM Data Privacy Tiers](../../concepts/llm-data-privacy-tiers.md) - The top tier of the privacy ladder, where nothing leaves your infrastructure at all.

## Contrasts with

- [Local AI Package](./local-ai-package.md) - Cole's extension of this kit, adding Supabase, Open Web UI, Flowise, and SearXNG to the same one-command idea.

## Works with

- [Docker](./docker.md) - The compose file is the whole install; every service is a container on one private network.
- [n8n](./n8n.md) - The orchestration layer where the local RAG agent is actually assembled.
- [Ollama](./ollama.md) - Serves the local chat and embedding models in the stack.
- [Qdrant](./qdrant.md) - The bundled vector database backing retrieval.
- [Postgres](./postgres-pgvector.md) - The bundled SQL database, used for agent chat memory once port 5432 is exposed.
- [nomic-embed-text](./nomic-embed-text.md) - The embedding model you must pull yourself before RAG works.
- [Nginx](./nginx.md) - The reverse proxy that puts this localhost stack behind a real domain.

## Related

- [Containerization & Docker Networking](../../concepts/containerization.md) - Containers in one compose file reference each other by service name, not localhost.
- [Delete-Before-Insert Re-Ingestion](../../concepts/delete-before-insert-reingestion.md) - The duplicate-vector trap the kit's ingestion pipeline walks straight into.
- [Agent Deployment](../../concepts/agent-deployment.md) - Getting agents to production: containerize, network, reverse-proxy, secure, and pick a cost-predictable host.
- [Local vs. Cloud Decision Framework](../../concepts/local-vs-cloud-decision-framework.md) - When a self-hosted stack like this is the right call rather than managed services.
- [Ollama's Default Context Window](../../concepts/ollama-context-window.md) - The 2048-token default that silently truncates history in exactly this kind of local setup.

## Sources

- [Run ALL Your AI Locally in Minutes (LLMs, RAG, and more)](../../sources/run-all-your-ai-locally-in-minutes-llms-rag-and-more.md) - "[0:00:47] running your own AI infrastructure is the way of the future especially because of how accessible is becoming and because open-source models like llama are getting to the point where they're so powerful"
- [Run ALL Your AI Locally in Minutes (LLMs, RAG, and more)](../../sources/run-all-your-ai-locally-in-minutes-llms-rag-and-more.md) - "[0:19:12] it's fully fully local it is just a beautiful thing so I hope that this whole local AI setup is just as cool for you as it is for me"
