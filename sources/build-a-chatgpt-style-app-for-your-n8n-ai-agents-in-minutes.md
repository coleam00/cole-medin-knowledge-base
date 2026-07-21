---
type: source
title: "Build a ChatGPT Style App for Your n8n AI Agents in MINUTES"
description: "You can wrap your n8n AI agents in a polished, ChatGPT-style interface in minutes by connecting the open-source Open Web UI to an n8n webhook via a custom function, giving your agents conversation history, formatted output, and metadata without writing a custom app."
youtube_id: 6zn8vVTeFE0
url: https://www.youtube.com/watch?v=6zn8vVTeFE0
slug: build-a-chatgpt-style-app-for-your-n8n-ai-agents-in-minutes
published: 2025-04-09
duration: "0:22:03"
recency_rank: 101
raw: "../raw/build-a-chatgpt-style-app-for-your-n8n-ai-agents-in-minutes.md"
tags: [n8n, open-web-ui, chat-interfaces, no-code-agents, local-ai]
created: 2026-07-21
updated: 2026-07-21
---

n8n's built-in chat trigger and public chat page work, but they are ugly and limited: no conversation history and almost no customization. Cole's fix is Open Web UI, a free, self-hostable, open-source ChatGPT-style frontend, wired to an n8n agent through a custom Open Web UI "function." He walks through installing Open Web UI (pip, Docker, or his Local AI package), then importing the function, which is configured through "valves" where you set the agent URL, a bearer token, and the input/output field names.

On the n8n side the key change is swapping the chat trigger for a webhook trigger, which exposes a public production URL the frontend can call. Because a public endpoint could be abused to drain LLM credits, Cole recommends protecting it with header (bearer token) authentication unless n8n runs purely locally. The input and output field names in the workflow must exactly match what the Open Web UI function expects (for example "chat input" in, "output" out) or the response never renders.

The subtle addition this time is a second, cheap LLM call gated by an if-statement on the session ID. Open Web UI fires extra LLM calls on the first message of a conversation to auto-generate a title and tags, and those arrive with a null session ID. The workflow routes null-session (metadata) calls to a fast, cheap model and real conversation turns (defined session ID) to the primary agent, which also keys Postgres chat memory. Both the workflow and the function ship as downloadable templates.

## Concepts covered

- [Agentic Experiences](../concepts/agentic-experiences.md)
- [The AI Layer](../concepts/the-ai-layer.md)
- [Local & Self-Hosted AI](../concepts/local-ai.md)
- [Webhook Tool Pattern](../concepts/webhook-tool-pattern.md)
- [Securing Agent APIs](../concepts/api-security.md)
- [Structured Outputs](../concepts/structured-outputs.md)
- [Agent Teams](../concepts/agent-teams.md)
- [Model Selection](../concepts/model-selection.md)
- [Memory Systems](../concepts/memory-systems.md)

## Entities

- [Open Web UI](../entities/tools/open-web-ui.md)
- [n8n](../entities/tools/n8n.md)
- [Ollama](../entities/tools/ollama.md)
- [Local AI Package](../entities/tools/local-ai-package.md)
- [Postgres](../entities/tools/postgres-pgvector.md)
- [Brave Search API](../entities/tools/brave-search.md)
- [DigitalOcean](../entities/organizations/digital-ocean.md)
- [Cole Medin](../entities/people/cole-medin.md)

## Key moments

- **[0:00:14]** Problem: n8n chat trigger and public chat page are ugly, limited, no conversation history
- **[0:01:06]** Solution reveal: a full ChatGPT-like interface for your n8n agents
- **[0:01:52]** Powered by open-source Open Web UI, no coding required
- **[0:02:06]** Demo: snake-game prompt in Open Web UI actually hits an n8n-hosted agent
- **[0:04:00]** Installing Open Web UI: pip, Docker, or the Local AI package
- **[0:06:41]** Importing the custom Open Web UI function for the n8n integration (two ways)
- **[0:08:20]** Configuring the function via "valves": URL, bearer token, input/output fields
- **[0:09:26]** Sponsor: Zams enterprise agent platform
- **[0:11:35]** Swap chat trigger for a webhook trigger to get a public production URL
- **[0:12:21]** Protect the webhook with header/bearer-token authentication to prevent abuse
- **[0:15:04]** Input field (chat input) and output field (output) must match between n8n and the function
- **[0:17:08]** Why there's a second LLM call: Open Web UI auto-generates title and tags on first message
- **[0:19:43]** Route by session ID: null = metadata (cheap LLM), defined = primary agent + Postgres memory

## Transcript

[Raw transcript](../raw/build-a-chatgpt-style-app-for-your-n8n-ai-agents-in-minutes.md)
