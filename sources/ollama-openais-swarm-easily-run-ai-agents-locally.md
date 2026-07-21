---
type: source
title: "Ollama + OpenAI's Swarm - EASILY Run AI Agents Locally"
description: "By overriding the OpenAI base URL to point at a local Ollama instance, you can run OpenAI's Swarm multi-agent framework entirely locally and for free using small tool-calling models like Qwen 2.5."
youtube_id: 8jpVeUTNExI
url: https://www.youtube.com/watch?v=8jpVeUTNExI
slug: ollama-openais-swarm-easily-run-ai-agents-locally
published: 2024-10-30
duration: "0:20:05"
recency_rank: 147
raw: "../raw/ollama-openais-swarm-easily-run-ai-agents-locally.md"
tags: [local-ai, ollama, multi-agent, swarm, tool-calling]
created: 2026-07-21
updated: 2026-07-21
---

[Cole Medin](../entities/people/cole-medin.md) demonstrates how to take [OpenAI](../entities/organizations/openai.md)'s experimental [Swarm](../entities/tools/openai-swarm.md) multi-agent framework, which defaults to paid OpenAI models like GPT-4o, and make every agent run locally on your own machine with [Ollama](../entities/tools/ollama.md). The key insight is that Ollama supports function and tool calling in the exact same format as OpenAI, and exposes an OpenAI-compatible endpoint. So the only change needed is to instantiate an OpenAI client pointed at Ollama's local base URL (localhost:11434) with a dummy API key, then pass that client into the Swarm instance. No fork of Swarm is required.

He illustrates this with a SQL agent swarm from a prior video: a lightweight 3B router agent ([Qwen](../entities/tools/qwen.md) 2.5 3B) that makes no tool calls except transferring, dispatching requests to specialized agents (an RSS-feed agent and an analytics agent) that generate SQL queries against a database using Qwen 2.5 Coder 7B. Splitting one overwhelmed agent into specialized agents makes each perform better, and each can carry its own instructions and behavior. A big advantage of Ollama over OpenAI is model choice: you can mix dozens or hundreds of models across agents rather than being limited to 4o-mini vs 4o.

The video closes with a from-scratch setup walkthrough: install Ollama from ollama.com (Mac, Linux, Windows), clone the [GitHub](../entities/tools/github.md) repo, create and activate a Python virtual environment, pip install requirements, rename the .env example and set the model, then pull a tool-supporting model via `ollama pull`. Cole stresses only using models with the "tools" label, since non-tool models cannot act as agents, and notes that small 3B and 7B models run well even on a laptop 3060 GPU while larger 32B+ models need a 3080 or 3090. Local performance still trails GPT, but the gap is closing fast.

## Concepts covered

- [Local & Self-Hosted AI](../concepts/local-ai.md)
- [Provider Independence](../concepts/provider-independence.md)
- [Tool Calling](../concepts/tool-use.md)
- [Agent Teams](../concepts/agent-teams.md)
- [Model Selection](../concepts/model-selection.md)

## Entities

- [Ollama](../entities/tools/ollama.md)
- [OpenAI Swarm](../entities/tools/openai-swarm.md)
- [Qwen 2.5 Coder 32B](../entities/tools/qwen.md)
- [OpenAI](../entities/organizations/openai.md)
- [GitHub](../entities/tools/github.md)
- [Cole Medin](../entities/people/cole-medin.md)

## Key moments

- **[0:00:00]** Intro: OpenAI's Swarm makes multi-agent systems easy but defaults to paid OpenAI models; goal is to run swarms locally with Ollama for free
- **[0:01:52]** Ollama added tool support (July 25) with OpenAI compatibility, override the base URL to route requests to Ollama instead of OpenAI
- **[0:03:17]** Swarm's default client has no base URL override; the only change is to pass in a custom OpenAI client pointed at Ollama
- **[0:04:42]** Model config: default agent model set via env var (Qwen 2.5 Coder 7B); router uses a lightweight 3B model
- **[0:07:13]** Explains the SQL agent swarm: router agent dispatches to specialized RSS-feed and analytics agents
- **[0:09:51]** Live test: how many users on the platform routes to user agent, runs a count, answers "five users"
- **[0:11:10]** Harder analytics test: most popular RSS feed, analytics agent generates a JOIN query, returns correct answer
- **[0:12:56]** From-scratch setup: install Ollama, clone repo, venv, pip install requirements, set .env
- **[0:16:40]** Pulling models: only use models with the "tools" label from ollama.com/search; ollama pull <model>

## Transcript

[Raw transcript](../raw/ollama-openais-swarm-easily-run-ai-agents-locally.md)
