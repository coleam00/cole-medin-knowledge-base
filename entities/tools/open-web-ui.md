---
type: entity
subtype: tool
title: "Open Web UI"
description: "Free, open-source, self-hostable ChatGPT-style chat interface; the frontend used to give n8n agents a polished UI with history, functions, and voice."
resource: "https://github.com/open-webui/open-webui"
tags: [chat-interface, local-ai, self-hosted]
videos: [the-ultimate-guide-to-local-ai-and-ai-agents-the-future-is-here, build-a-chatgpt-style-app-for-your-n8n-ai-agents-in-minutes, create-your-own-private-local-ai-cloud-stack-in-under-20-minutes, run-supabase-100-locally-for-your-ai-agents, use-open-webui-with-your-n8n-ai-agents-voice-chat-included]
created: 2026-07-21
updated: 2026-07-21
---

# Open Web UI

Open Web UI is a free, open-source, self-hostable ChatGPT-style chat interface, and in Cole's local-AI stack it is the polished frontend that sits in front of everything else. He describes it exactly that way: "open web UI is an open-Source ChatGPT like interface that you typically use to chat with llms that are running with Ollama." It gives a private stack the thing raw model servers lack, a real UI with "conversation history" and the familiar chat experience, without sending a single message to a hosted provider.

Its standout role across Cole's videos is as a frontend for [n8n](./n8n.md) agents. Rather than build a custom app, he wires an existing n8n workflow into Open Web UI through a custom function: "there are two ways to do this in Open Web UI both through setting up this custom function that I have created for the n8n integration." The result is a ChatGPT-grade interface, complete with voice chat, for agents you assembled in a no-code builder. That is the pattern he keeps returning to: Open Web UI supplies the [chat interface](../../concepts/chat-interfaces.md) and [agent deployment](../../concepts/agent-deployment.md) surface, n8n supplies the logic, and [Ollama](./ollama.md) supplies the models, all self-hosted.

Because it is self-hostable, Open Web UI is a core component of the [Local AI Package](./local-ai-package.md) and of Cole's private-cloud builds. He runs it on `localhost:3000`, pairs it with a local [Supabase](./supabase.md) database, and treats it as the default face of a fully private stack where nothing leaves your infrastructure, the same [local-AI](../../concepts/local-ai.md) and [agent-security](../../concepts/agent-security.md) argument that runs through the rest of his self-hosting work. It also supports functions, model management, and [RAG](../../concepts/rag.md)-style knowledge, making it more than a thin chat window: it is the extensible frontend layer of the whole local ecosystem.

## Realizes

- [Chat Interfaces](../../concepts/chat-interfaces.md) - Wrapping agents in chat surfaces (websites, DMs, platforms) with adapters, a shared message format, and durable history.
- [Agent Deployment](../../concepts/agent-deployment.md) - Getting agents to production, containerizing, networking, reverse-proxying, and choosing a provider-agnostic, cost-predictable host.

## Works with

- [Ollama](./ollama.md) - Local LLM runtime; works with a locally-run bolt.diy but can't be reached by a self-hosted (remote) instance.
- [n8n](./n8n.md) - A no-code AI automation platform for building agents and workflows that integrate with 500+ applications.
- [Local AI Package](./local-ai-package.md) - Cole's bundled collection of self-hosted AI services (database, n8n, Ollama, Open Web UI) that installs the whole stack together for free.
- [Supabase](./supabase.md) - A single platform providing Postgres for scalable chat memory plus the pgvector store for RAG embeddings, recommended over in-memory alternatives.

## Related

- [Local & Self-Hosted AI](../../concepts/local-ai.md) - Running open-weight models on your own hardware or cloud for privacy, cost control, and independence from API providers.
- [Memory Systems](../../concepts/memory-systems.md) - Giving agents durable short- and long-term memory so conversations, user context, and facts persist across sessions and users.
- [Model Selection](../../concepts/model-selection.md) - Choosing the right LLM per task by trading off quality, speed, and cost, often routing easy requests to cheap models and hard ones to expensive models.
- [Retrieval-Augmented Generation (RAG)](../../concepts/rag.md) - Grounding an LLM's answers by retrieving relevant documents from an external knowledge base and injecting them into the prompt at query time.
- [Agent Security](../../concepts/agent-security.md) - Sandboxing agents, scoping permissions, and keeping secrets out of the model to limit blast radius and prevent abuse.

## Sources

- [Use Open WebUI with Your N8N AI Agents - Voice Chat Included!](../../sources/use-open-webui-with-your-n8n-ai-agents-voice-chat-included.md) - "[0:00:53] open web UI is an open- Source ChatGPT like interface that you typically use to chat with llms that are running with Ollama"
- [Build a ChatGPT Style App for Your n8n AI Agents in MINUTES](../../sources/build-a-chatgpt-style-app-for-your-n8n-ai-agents-in-minutes.md) - "[0:01:37] this is all using the power of an incredible open- source platform called open web UI. That's what gives us the UI right here. Very beautiful."
- [The Ultimate Guide to Local AI and AI Agents (The Future is Here)](../../sources/the-ultimate-guide-to-local-ai-and-ai-agents-the-future-is-here.md) - "[0:56:30] Open Web UI, which gives us a ChatGPT like interface for us to talk to our LLMs and have things like conversation history"
- [Run Supabase 100% LOCALLY for Your AI Agents](../../sources/run-supabase-100-locally-for-your-ai-agents.md) - "[0:02:45] open web UI so we can have a ChatGPT like interface and now I'm adding in Supabase"
- [Create Your Own Private Local AI Cloud Stack in Under 20 Minutes](../../sources/create-your-own-private-local-ai-cloud-stack-in-under-20-minutes.md) - "[0:15:40] We can do YT open web UI all right there we go we got open web UI so everything is working perfectly"
