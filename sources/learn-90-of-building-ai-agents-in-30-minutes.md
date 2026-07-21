---
type: source
title: "Learn 90% of Building AI Agents in 30 Minutes"
description: "You can build 90% of any AI agent by mastering four simple core components (LLM, tools, system prompt, memory) and deliberately deferring the production-grade complexity until you actually hit its limits."
youtube_id: i5kwX7jeWL8
url: https://www.youtube.com/watch?v=i5kwX7jeWL8
slug: learn-90-of-building-ai-agents-in-30-minutes
published: 2025-10-29
duration: "0:29:21"
recency_rank: 58
raw: "../raw/learn-90-of-building-ai-agents-in-30-minutes.md"
tags: [ai-agents, pydantic-ai, fundamentals]
created: 2026-07-21
updated: 2026-07-21
---

# Learn 90% of Building AI Agents in 30 Minutes

Cole argues that the biggest mistake new and even experienced agent builders make is over-complicating the first version: agonizing over the perfect prompt, tools, model, security, and infrastructure before anything works. He reframes an AI agent as just an LLM given tools to act on your behalf, and reduces it to four core components, a large language model (the brain), tools (functions it can call), a system prompt (top-level instructions), and memory (short- and long-term context). He live-codes a sub-50-line Pydantic AI agent with a single add-numbers tool and a CLI loop to prove how little is actually required to cross from chatbot to agent.

For each component he pairs a "focus on this now" tip with a "do not over-engineer this yet" warning. Pick a cheap model (Claude Haiku 4.5) via OpenRouter so swapping models is a one-line change, and do not obsess over the perfect model. Work off a reusable system-prompt template (persona and goals, tool instructions with examples, output format, miscellaneous) instead of building prompt eval harnesses. Keep tools under 10 with distinct purposes, lean on MCP servers for prepackaged tools, and learn RAG first since 80% or more of real agents use it, but skip multi-agent orchestration until you exceed roughly 10 tools. Handle security with existing tools (Guardrails AI for input/output guardrails, Snyk for dependency and code vulnerability scanning via its MCP server) rather than becoming a security expert overnight.

On context and memory, keep prompts concise, use a sliding window of the last 10-20 messages, and reach for a library like Mem0 for long-term memory (which itself uses RAG) rather than building compression from scratch. He adds observability up front with Langfuse (a few lines to instrument the agent) and recommends designing Docker-native from the start so deployment is easy, either as a serverless container for background agents or a container plus a Streamlit or React front end for conversational ones. Throughout, the message is: start with the foundations, give yourself permission to be imperfect, and iterate toward production instead of front-loading the last 10%.

## Concepts covered

- [The Core Components of an Agent](../concepts/agent-core-components.md)
- [What Is an AI Agent](../concepts/what-is-an-ai-agent.md)
- [Agent Development Lifecycle](../concepts/agent-development-lifecycle.md)
- [Model Selection](../concepts/model-selection.md)
- [Provider Independence](../concepts/provider-independence.md)
- [System Prompt Engineering](../concepts/system-prompt-engineering.md)
- [Tool Design](../concepts/tool-design.md)
- [Retrieval-Augmented Generation (RAG)](../concepts/rag.md)
- [Subagents Pattern](../concepts/subagents-pattern.md)
- [Guardrails](../concepts/guardrails.md)
- [Memory Systems](../concepts/memory-systems.md)
- [Context Engineering](../concepts/context-engineering.md)
- [Agent Observability](../concepts/agent-observability.md)
- [Agent Deployment](../concepts/agent-deployment.md)

## Entities

- [Cole Medin](../entities/people/cole-medin.md)
- [Pydantic AI](../entities/tools/pydantic-ai.md)
- [OpenRouter](../entities/tools/openrouter.md)
- [Snyk](../entities/organizations/snyk.md)
- [Mem0](../entities/tools/mem0.md)
- [Langfuse](../entities/tools/langfuse.md)
- [MCP (Model Context Protocol)](../entities/tools/mcp.md)
- [Claude Code](../entities/tools/claude-code.md)
- [n8n](../entities/tools/n8n.md)
- [Docker](../entities/tools/docker.md)
- [Anthropic](../entities/organizations/anthropic.md)
- [Dynamous](../entities/organizations/dynamous.md)

## Key moments

- **[0:01:44]** Defines an AI agent and the four core components: tools, LLM, system prompt, memory
- **[0:03:05]** The three steps to start any agent: pick an LLM, write a basic system prompt, add your first tool
- **[0:04:19]** Begins live-coding a sub-50-line Pydantic AI agent from scratch
- **[0:06:04]** Explains tool decorators and docstrings as the mechanism that turns an LLM into an agent
- **[0:09:00]** Model selection guidance: Haiku 4.5 for prototyping, Sonnet 4.5 all-around, local models for privacy
- **[0:10:38]** System prompt template with four sections; don't build prompt evals yet
- **[0:12:21]** Tool rules: keep under 10, distinct purposes, use MCP servers, learn RAG first
- **[0:14:32]** Security essentials: no hardcoded keys, Guardrails AI, Snyk MCP vulnerability scanning
- **[0:19:44]** Context/memory management: concise prompts, sliding window, Mem0 for long-term memory
- **[0:24:02]** Observability with Langfuse and Docker-native deployment as the last-10% components

## Transcript

[Raw transcript](../raw/learn-90-of-building-ai-agents-in-30-minutes.md)
