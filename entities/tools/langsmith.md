---
type: entity
subtype: tool
title: "LangSmith"
description: "A competing observability platform Cole contrasts against Langfuse, faulting it for not being fully open-source."
resource: "https://smith.langchain.com"
tags: [observability, tracing, langchain]
videos: [if-youre-serious-about-building-ai-agents-this-is-your-secret-weapon, introducing-archon-an-ai-agent-that-builds-ai-agents, revealing-my-complete-ai-agent-blueprint, the-only-ai-developer-roadmap-you-need-in-2024]
created: 2026-07-21
updated: 2026-07-21
---

# LangSmith

LangSmith is LangChain's tracing and monitoring platform, the closed-source counterpart that Cole most often measures [Langfuse](./langfuse.md) against. He describes it plainly as "LangChain's tracing and monitoring platform, it just gives you a very good inside scoop" [0:19:04], another realization of [Agent Observability](../../concepts/agent-observability.md) built to make multi-agent execution legible.

## What it is

LangSmith earns its keep the moment an agent system stops being a single prompt. As Cole puts it, it "helps you get visibility into what's going on because once you get past just a single prompt to an AI and you have many agents working together" [0:10:59] you need somewhere to watch the whole flow. Its natural home is the LangChain ecosystem: it is "super good if you're using [LangGraph](./langgraph.md) or anything from [LangChain](./langchain.md)" [0:11:51]. Cole used it himself when building [Archon](./archon.md), citing the "inside scoop" it gave into agent runs during development.

## How Cole treats it

Cole treats LangSmith as a legitimate, capable observability option, and it appears in his early developer roadmaps as a first recommendation for gaining agent visibility. Over time, though, his own default shifted to Langfuse for one reason: openness. He explicitly contrasts the two, noting Langfuse "is completely open source unlike a lot of its competitors like LangSmith" [0:27:33]. So LangSmith remains his recommendation for teams already committed to the LangChain and LangGraph stack, while he steers his own [local & self-hosted AI](../../concepts/local-ai.md) work toward the open-source alternative.

## Contrasts with

[Langfuse](./langfuse.md) - same job, opposite licensing posture. Cole prefers Langfuse precisely because LangSmith is not fully open-source.

## Realizes

- [Agent Observability](../../concepts/agent-observability.md) - Instrumenting agents with tracing, logging, and cost/token metrics so you can see and debug what they actually did.

## Works with

- [LangChain](./langchain.md) - The framework used in prior masterclass videos to build the Asana agent; its message objects and invoke/stream methods underpin the chatbot logic.
- [LangGraph](./langgraph.md) - The orchestration framework wiring agents into a stateful graph of nodes and edges, used here to run agents in parallel and add human-in-the-loop.
- [Logfire](./logfire.md) - Observability tool by the Pydantic team that instruments Pydantic AI agents to send traces, token usage, and cost as telemetry for local and production debugging.

## Related

- [Agent Deployment](../../concepts/agent-deployment.md) - Getting agents to production, containerizing, networking, reverse-proxying, and choosing a provider-agnostic, cost-predictable host.
- [Retrieval-Augmented Generation (RAG)](../../concepts/rag.md) - Grounding an LLM's answers by retrieving relevant documents from an external knowledge base and injecting them into the prompt at query time.
- [Local & Self-Hosted AI](../../concepts/local-ai.md) - Running open-weight models on your own hardware or cloud for privacy, cost control, and independence from API providers.
- [Rapid Prototyping](../../concepts/rapid-prototyping.md) - Building a fast proof of concept with managed services first, then hardening only what proves out, instead of over-engineering up front.
- [Model Selection](../../concepts/model-selection.md) - Choosing the right LLM per task by trading off quality, speed, and cost, often routing easy requests to cheap models and hard ones to expensive models.

## Sources

- [Introducing Archon - an AI Agent that BUILDS AI Agents](../../sources/introducing-archon-an-ai-agent-that-builds-ai-agents.md) - "[0:19:04] starting with LangSmith here this is LangChain's tracing and monitoring platform it just gives you a very good inside scoop"
- [If You're Serious About Building AI Agents, This is Your Secret Weapon](../../sources/if-youre-serious-about-building-ai-agents-this-is-your-secret-weapon.md) - "[0:27:33] it is completely open source unlike a lot of its competitors like LangSmith."
- [Revealing my COMPLETE AI Agent Blueprint](../../sources/revealing-my-complete-ai-agent-blueprint.md) - "[0:11:51] we got LangSmith which is super good if you're using LangGraph or anything from LangChain"
- [The ONLY AI Developer Roadmap You Need in 2024](../../sources/the-only-ai-developer-roadmap-you-need-in-2024.md) - "[0:10:59] LangSmith which helps you get visibility into what's going on because once you get past just a single prompt to an AI and you have many agents working together"
