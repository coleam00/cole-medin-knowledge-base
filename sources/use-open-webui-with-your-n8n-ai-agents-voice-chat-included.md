---
type: source
title: "Use Open WebUI with Your N8N AI Agents - Voice Chat Included!"
description: "You can extend the self-hosted local-AI starter kit by adding Open WebUI and a custom function so its ChatGPT-like interface (including voice) talks directly to your n8n agent workflows via a webhook."
youtube_id: E2GIZrsDvuM
url: https://www.youtube.com/watch?v=E2GIZrsDvuM
slug: use-open-webui-with-your-n8n-ai-agents-voice-chat-included
published: 2024-10-23
duration: "0:26:08"
recency_rank: 150
raw: "../raw/use-open-webui-with-your-n8n-ai-agents-voice-chat-included.md"
tags: [local-ai, n8n, open-webui, rag, voice, self-hosted]
created: 2026-07-21
updated: 2026-07-21
---

[Cole Medin](../entities/people/cole-medin.md) extends the [n8n](../entities/tools/n8n.md) team's self-hosted AI starter kit, a [Docker](../entities/tools/docker.md) Compose bundle of n8n (workflow and agent builder), [Ollama](../entities/tools/ollama.md) (local LLMs), [Qdrant](../entities/tools/qdrant.md) (vector DB for RAG), and [Postgres](../entities/tools/postgres-pgvector.md) (SQL plus chat memory), by adding a fifth container: [Open Web UI](../entities/tools/open-web-ui.md). Open WebUI is an open-source ChatGPT-like interface normally used to chat with Ollama models, but its functions and pipelines extension points let you route chats to arbitrary agents and API endpoints.

Cole wrote (and published to the Open WebUI function list) an "n8n pipe" function that makes an n8n workflow appear as a selectable model alongside your Ollama models. The function is configured through valves, the webhook URL, a bearer token, and the input and output field names, plus a session ID so conversation state is preserved. Once wired up, chatting with the n8n agent as if it were just another model triggers the underlying workflow (webhook to AI agent to respond-to-webhook) and returns the answer inline.

The demo exercises a local "local rag AI agent" n8n workflow that retrieves action items from documents stored in Qdrant, all running on the local machine with Postgres holding chat memory. He also fixes the Ollama connection URL so Open WebUI points at the container rather than localhost, and closes by showing voice chat with the n8n agent through Open WebUI's call feature, turning the self-hosted stack into a full voice-capable assistant. The framing is learn-by-building: assemble the pieces yourself to understand how a private, local agent stack fits together.

## Concepts covered

- [Local & Self-Hosted AI](../concepts/local-ai.md)
- [Retrieval-Augmented Generation (RAG)](../concepts/rag.md)
- [Semantic Search](../concepts/semantic-search.md)
- [Chat Interfaces](../concepts/chat-interfaces.md)
- [Agent Deployment](../concepts/agent-deployment.md)
- [Memory Systems](../concepts/memory-systems.md)
- [Voice Agents](../concepts/voice-agents.md)
- [Learn by Building](../concepts/learn-by-building.md)

## Entities

- [Open Web UI](../entities/tools/open-web-ui.md)
- [n8n](../entities/tools/n8n.md)
- [Ollama](../entities/tools/ollama.md)
- [Qdrant](../entities/tools/qdrant.md)
- [Postgres](../entities/tools/postgres-pgvector.md)
- [Docker](../entities/tools/docker.md)
- [Google Drive](../entities/tools/google-drive.md)
- [Cole Medin](../entities/people/cole-medin.md)

## Key moments

- **[0:00:00]** Recap: prior video ran all AI locally via the self-hosted AI starter kit; the missing piece was Open WebUI
- **[0:02:09]** Walkthrough of the forked starter kit repo and its Docker Compose services (n8n, Ollama, Qdrant, Postgres)
- **[0:05:30]** Installation: GPU/Mac/CPU profiles, edit the .env example file, run docker compose
- **[0:09:48]** Demo n8n "local rag AI agent" workflow: webhook to AI agent to respond to webhook; Ollama + Postgres + Qdrant credentials
- **[0:15:15]** Open WebUI integration begins; fixing the Ollama connection URL to point at the container
- **[0:17:05]** Open WebUI functions: the n8n pipe, valves (webhook URL, bearer token, input/output field), session ID
- **[0:22:12]** Live test: chatting with the n8n agent as a model and retrieving action items from Qdrant
- **[0:24:07]** Voice chat with the n8n agent through Open WebUI's call feature

## Transcript

[Raw transcript](../raw/use-open-webui-with-your-n8n-ai-agents-voice-chat-included.md)
