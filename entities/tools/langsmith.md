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

LangSmith is LangChain's tracing and monitoring platform, the closed-source counterpart that Cole most often measures [Langfuse](./langfuse.md) against. He describes it plainly as "Lang Chain's tracing and monitoring platform, it just gives you a very good inside scoop" [0:19:04], another realization of [Agent Observability](../../concepts/agent-observability.md) built to make multi-agent execution legible.

## What it is

LangSmith earns its keep the moment an agent system stops being a single prompt. As Cole puts it, it "helps you get visibility into what's going on because once you get past just a single prompt to an AI and you have many agents working together" [0:10:59] you need somewhere to watch the whole flow. Its natural home is the LangChain ecosystem: it is "super good if you're using [LangGraph](./langgraph.md) or anything from [LangChain](./langchain.md)" [0:11:51]. Cole used it himself when building [Archon](./archon.md), citing the "inside scoop" it gave into agent runs during development.

## How Cole treats it

Cole treats LangSmith as a legitimate, capable observability option, and it appears in his early developer roadmaps as a first recommendation for gaining agent visibility. Over time, though, his own default shifted to Langfuse for one reason: openness. He explicitly contrasts the two, noting Langfuse "is completely open source unlike a lot of its competitors like Langsmith" [0:27:33]. So LangSmith remains his recommendation for teams already committed to the LangChain and LangGraph stack, while he steers his own [local & self-hosted AI](../../concepts/local-ai.md) work toward the open-source alternative.

## Contrasts with

[Langfuse](./langfuse.md) - same job, opposite licensing posture. Cole prefers Langfuse precisely because LangSmith is not fully open-source.

## Related

- [Agent Observability](../../concepts/agent-observability.md) - the capability LangSmith provides.
- [Agent Deployment](../../concepts/agent-deployment.md) and [RAG](../../concepts/rag.md) - where tracing pays off for multi-agent and retrieval systems.
- [Model Selection](../../concepts/model-selection.md) and [Rapid Prototyping](../../concepts/rapid-prototyping.md) - decisions its trace data informs.
- [Local & Self-Hosted AI](../../concepts/local-ai.md) - the axis on which Cole prefers Langfuse instead.
- Sibling tools: [Langfuse](./langfuse.md), [LangChain](./langchain.md), [LangGraph](./langgraph.md), [Logfire](./logfire.md).

## Sources

- [Introducing Archon - an AI Agent that BUILDS AI Agents](../../sources/introducing-archon-an-ai-agent-that-builds-ai-agents.md) - "[0:19:04] starting with Langsmith here this is Lang Chain's tracing and monitoring platform it just gives you a very good inside scoop"
- [If You're Serious About Building AI Agents, This is Your Secret Weapon](../../sources/if-youre-serious-about-building-ai-agents-this-is-your-secret-weapon.md) - "[0:27:33] it is completely open source unlike a lot of its competitors like Langsmith."
- [Revealing my COMPLETE AI Agent Blueprint](../../sources/revealing-my-complete-ai-agent-blueprint.md) - "[0:11:51] we got Lang Smith which is super good if you're using Lang graph or anything from Lang chain"
- [The ONLY AI Developer Roadmap You Need in 2024](../../sources/the-only-ai-developer-roadmap-you-need-in-2024.md) - "[0:10:59] Langsmith which helps you get visibility into what's going on because once you get past just a single prompt to an AI and you have many agents working together"
