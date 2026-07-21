---
type: source
title: "Run Supabase 100% LOCALLY for Your AI Agents"
description: "Supabase can be self-hosted alongside the rest of a local AI stack via Docker so you can run a fully local RAG AI agent (database, vector store, and chat memory) with no cloud dependency."
youtube_id: pOsO40HSbOo
url: https://www.youtube.com/watch?v=pOsO40HSbOo
slug: run-supabase-100-locally-for-your-ai-agents
published: 2025-02-16
duration: "0:29:37"
recency_rank: 117
raw: "../raw/run-supabase-100-locally-for-your-ai-agents.md"
tags: [local-ai, supabase, docker, self-hosting]
created: 2026-07-21
updated: 2026-07-21
---

# Run Supabase 100% LOCALLY for Your AI Agents

Cole walks through a revamped "local AI package," a Docker-based bundle (originally from the n8n team) that ships n8n, Ollama, Qdrant, Open WebUI, Flowise, and now Supabase as self-hosted containers. The headline addition is Supabase, which replaces the standalone Postgres container. Because Supabase is Postgres under the hood with the pgvector extension, it doubles as both the SQL/state database and a vector store for RAG, while also bringing auth and object storage along for free.

The practical core is a step-by-step self-hosting guide. Install the prerequisites (Python, Git, Docker), clone the repo, populate the `.env` (Postgres password, dashboard login, Pooler tenant ID, and the JWT secret, anon key, and service-role key generated from Supabase's self-hosting docs), then launch everything with a Python helper script (`start_services.py`) chosen by hardware profile (Nvidia GPU, AMD, Mac/CPU, or none). Because Supabase is itself a multi-container stack (Studio, Kong, auth, REST, realtime, storage, and the DB container), the script clones Supabase's own repo and merges its docker-compose with the package's compose on a shared Docker network, so containers can address each other by name and updates or restarts are one command.

Finally Cole builds a fully local RAG agent in n8n: an Ollama chat model (Qwen 2.5 7B) with Supabase serving both Postgres chat memory and vector retrieval, plus a local file-trigger ingestion pipeline (replacing Google Drive) that watches a shared folder, cleans old vectors on change, extracts text, and inserts embeddings (nomic-embed-text, 768-dim) into a documents table set up via Supabase's vector quick-start SQL. A key gotcha: the Postgres node connects to host `db`, but the Supabase vector-store node must use `host.docker.internal:8000` instead.

## Concepts covered

- [Local & Self-Hosted AI](../concepts/local-ai.md)
- [Vector Embeddings](../concepts/vector-embeddings.md)
- [Retrieval-Augmented Generation (RAG)](../concepts/rag.md)
- [Agent Deployment](../concepts/agent-deployment.md)

## Entities

- [Supabase](../entities/tools/supabase.md)
- [n8n](../entities/tools/n8n.md)
- [Ollama](../entities/tools/ollama.md)
- [Docker](../entities/tools/docker.md)
- [Qdrant](../entities/tools/qdrant.md)
- [Postgres / pgvector](../entities/tools/postgres-pgvector.md)
- [Open WebUI](../entities/tools/open-web-ui.md)
- [Flowise](../entities/tools/flowise.md)
- [Archon](../entities/tools/archon.md)
- [Cole Medin](../entities/people/cole-medin.md)

## Key moments

- **[0:00:00]** Why Supabase is ideal for AI agents: Postgres + pgvector = database, state, and vector store in one, plus auth and storage
- **[0:02:00]** Tour of the revamped local AI package: n8n, Ollama, Qdrant, Postgres, now Supabase (replacing Postgres), Flowise, Open WebUI, in a dedicated GitHub repo
- **[0:06:35]** Setting the .env: JWT secret, anon key, service-role key generated from Supabase's self-hosting docs; Pooler tenant ID; dashboard login
- **[0:11:56]** start_services.py launch commands by hardware profile (Nvidia GPU / AMD / Mac / CPU / none)
- **[0:13:14]** Why Supabase needs a separate compose file, it's many containers; the script clones Supabase's repo and merges its compose onto one shared Docker network
- **[0:19:55]** Building the local RAG agent in n8n: Ollama chat model + Supabase Postgres memory + Supabase vector retrieval
- **[0:21:34]** Credential gotcha: Postgres node uses host 'db'; the Supabase vector-store node must use host.docker.internal:8000
- **[0:23:12]** Local file-trigger ingestion pipeline: watch shared folder, clean old vectors on change, extract text, insert embeddings
- **[0:27:46]** End-to-end demo: query the local Qwen agent, it invokes the Supabase vector store tool and returns the to-do list from the ingested file

## Transcript

[Raw transcript](../raw/run-supabase-100-locally-for-your-ai-agents.md)
