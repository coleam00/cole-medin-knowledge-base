---
type: source
title: "Flowise + n8n - The BEST No Code + Local AI Agent Combo"
description: "Pairing Flowise (fast no-code agent prototyping) with n8n (workflows exposed as agent tools), all inside a fully local AI stack, is the fastest way to build powerful AI agents that can actually do anything."
youtube_id: 23s2N3ug8B8
url: https://www.youtube.com/watch?v=23s2N3ug8B8
slug: flowise-n8n-the-best-no-code-local-ai-agent-combo
published: 2024-12-04
duration: "0:29:13"
recency_rank: 136
raw: "../raw/flowise-n8n-the-best-no-code-local-ai-agent-combo.md"
tags: [flowise, n8n, local-ai, no-code, tools]
created: 2026-07-21
updated: 2026-07-21
---

# Flowise + n8n - The BEST No Code + Local AI Agent Combo

Cole argues the future of AI is running everything locally, LLMs, RAG pipelines, and workflow automation, and demonstrates it by extending the n8n team's Local AI Starter Kit with [Flowise](../entities/tools/flowise.md), a free, open-source, [LangChain](../entities/tools/langchain.md)-based low/no-code agent builder backed by Y Combinator. Flowise is his go-to for very fast [agent prototyping](../concepts/rapid-prototyping.md) because of its drag-and-drop node canvas, while [n8n](../entities/tools/n8n.md) remains his favorite automation platform because of its integrations. The two pair perfectly as [no-code agents](../concepts/no-code-agents.md): Flowise hosts the agent brain, and n8n workflows become the agent's tools, a full [local AI](../concepts/local-ai.md) stack.

He builds a [tool-calling](../concepts/tool-use.md) agent from scratch in Flowise, wiring buffer memory, a ChatOllama model ([Qwen 2.5 Coder 32B](../entities/tools/qwen.md), which he finds performs best as an agent) via [Ollama](../entities/tools/ollama.md), an in-memory cache, and a [Brave Search](../entities/tools/brave-search.md) web-search tool. A recurring theme is [Docker](../entities/tools/docker.md) container networking: to reach Ollama on the host you use host.docker.internal, and to reach another container (Ollama, n8n) you use its compose service name, never localhost. He also flags that every Ollama model defaults to a 2048-token context window, which silently truncates long histories and tool outputs, so you must raise it (e.g. 32,000) or the agent misses tool calls and hallucinates.

The core pattern is turning n8n workflows into Flowise tools via the [webhook tool pattern](../concepts/webhook-tool-pattern.md): each n8n tool starts with a webhook trigger and ends with a respond-to-webhook node, and Flowise calls them via a Custom Tool node containing basic JavaScript fetch requests. Each custom tool needs a good name, an LLM-facing description (tells the model when to use it), and an input schema (tells the model how to call it). Secrets like bearer tokens go in Flowise Variables ($vars.name), never hardcoded, a basic [agent security](../concepts/agent-security.md) discipline. He builds tools for [Postgres](../entities/tools/postgres-pgvector.md) table queries, [Slack](../entities/tools/slack.md) summarization, Google Doc creation, and Slack messaging, then chains them in one multi-tool request. Google Drive/Slack credentials require an HTTPS domain, so those tools point at his [DigitalOcean](../entities/organizations/digital-ocean.md)-hosted n8n rather than the localhost starter kit, a note on real-world [deployment](../concepts/agent-deployment.md).

## Concepts covered

- [Local & Self-Hosted AI](../concepts/local-ai.md)
- [No-Code AI Agents](../concepts/no-code-agents.md)
- [Rapid Prototyping](../concepts/rapid-prototyping.md)
- [Tool Calling](../concepts/tool-use.md)
- [Agent Deployment](../concepts/agent-deployment.md)
- [Agent Security](../concepts/agent-security.md)
- [Webhook Tool Pattern](../concepts/webhook-tool-pattern.md)

## Entities

- [Flowise](../entities/tools/flowise.md)
- [n8n](../entities/tools/n8n.md)
- [Ollama](../entities/tools/ollama.md)
- [LangChain](../entities/tools/langchain.md)
- [Brave Search API](../entities/tools/brave-search.md)
- [Docker](../entities/tools/docker.md)
- [Postgres](../entities/tools/postgres-pgvector.md)
- [Slack](../entities/tools/slack.md)
- [DigitalOcean](../entities/organizations/digital-ocean.md)
- [Cole Medin](../entities/people/cole-medin.md)

## Key moments

- **[0:00:31]** Thesis: the future of AI is running everything locally
- **[0:01:20]** Adds Flowise (LangChain-based, YC-backed) to the Local AI Starter Kit alongside n8n
- **[0:03:50]** Install: git clone the Local AI package, rename .env.example, run docker compose
- **[0:08:55]** Starts building a tool-calling agent from scratch on the Flowise canvas
- **[0:10:29]** ChatOllama config; host.docker.internal vs container name for base URL
- **[0:12:28]** Raise Ollama context window from the 2048 default (e.g. 32000)
- **[0:13:51]** Adds Brave Search web-search tool plus credential; first agent test
- **[0:15:41]** Integrating n8n: workflows-as-tools via Flowise Custom Tool nodes
- **[0:18:33]** Custom Tool anatomy: name, LLM-facing description, input schema, fetch code
- **[0:20:56]** Bearer token stored as a Flowise Variable ($vars), not hardcoded
- **[0:25:43]** Multi-tool chained request: summarize Slack, web research, Google Doc, Slack message

## Transcript

[Raw transcript](../raw/flowise-n8n-the-best-no-code-local-ai-agent-combo.md)
