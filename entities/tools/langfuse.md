---
type: entity
subtype: tool
title: "Langfuse"
description: "The platform Cole uses specifically to monitor AI agents in production, distinct from Sentry which he uses for backend/RAG infrastructure."
resource: "https://langfuse.com"
tags: [observability, open-source, agent-monitoring]
videos: [the-only-ai-tech-stack-you-need-in-2026, learn-90-of-building-ai-agents-in-30-minutes, should-i-build-my-ai-agents-with-n8n-or-python, my-top-20-lessons-from-building-100s-of-ai-agents-super-actionable, build-and-ship-any-mcp-server-in-minutes-full-guide, how-id-learn-ai-agents-fast-if-i-had-to-start-over-full-roadmap, if-youre-serious-about-building-ai-agents-this-is-your-secret-weapon, revealing-my-complete-ai-agent-blueprint]
created: 2026-07-21
updated: 2026-07-21
---

# Langfuse

Langfuse is the open-source LLM engineering platform Cole reaches for to watch what his agents are actually doing in production. As he frames it, "It's a completely free and open-source tool that I've also added to my local AI stack and it's called Langfuse. Langfuse is an LLM engineering platform for agent observability" [0:00:17]. It is his default realization of [Agent Observability](../../concepts/agent-observability.md): a dashboard where every agent run becomes an inspectable trace.

## What it is

Langfuse instruments an agent so that each run is captured with its full execution detail. Cole's pitch is concrete: "for every single run, you can see the token usage, the total cost, the latency, the tool calls that your agents are making" [0:11:24]. Instead of guessing why an agent misbehaved, he opens the dashboard and reads the trace. In his agent-building tutorials he introduces it early: "we can set up the ability to watch for the actions that our agent is taking, view them in a dashboard" [0:24:02].

## How Cole uses it

Langfuse is a fixed part of his stack across n8n-vs-Python discussions ("you have tools like Langfuse for tracing, so you can get a lot of visibility" [0:11:08]) and his lessons from building hundreds of agents ("Langfuse is a really good one for sure" [0:29:40]). He draws a deliberate division of labor: Langfuse monitors the *agents*, while [Sentry](./sentry.md) covers the surrounding backend and RAG infrastructure. Two things keep it his pick over rivals: it is fully open-source, so it drops cleanly into his [local & self-hosted AI](../../concepts/local-ai.md) stack, and it integrates with [Logfire](./logfire.md) under the hood via OpenTelemetry, which is how [Pydantic AI](./pydantic-ai.md) agents flow their telemetry into it. That open-source stance is the crux of how he contrasts it with the closed alternative.

## Contrasts with

Cole singles out [LangSmith](./langsmith.md) as the closed counterpoint: Langfuse "is completely open source unlike a lot of its competitors like LangSmith. And so I'm going to keep focusing on this as my observability platform" [0:27:33].

## Realizes

- [Agent Observability](../../concepts/agent-observability.md) - Instrumenting agents with tracing, logging, and cost/token metrics so you can see and debug what they actually did.

## Works with

- [Logfire](./logfire.md) - Observability tool by the Pydantic team that instruments Pydantic AI agents to send traces, token usage, and cost as telemetry for local and production debugging.
- [Sentry](./sentry.md) - Application monitoring platform (the video sponsor) that makes it easy to add tracing, logs, and error alerting to MCP servers in production.
- [Pydantic AI](./pydantic-ai.md) - Cole's framework for the individual agents, structured around three parts: dependencies, the agent definition, and tools.

## Contrasts with

- [LangSmith](./langsmith.md) - A competing observability platform Cole contrasts against Langfuse, faulting it for not being fully open-source.

## Related

- [Agent Deployment](../../concepts/agent-deployment.md) - Getting agents to production, containerizing, networking, reverse-proxying, and choosing a provider-agnostic, cost-predictable host.
- [Memory Systems](../../concepts/memory-systems.md) - Giving agents durable short- and long-term memory so conversations, user context, and facts persist across sessions and users.
- [Guardrails](../../concepts/guardrails.md) - Constraints and checks that keep agents from hallucinating, going off the rails, or emitting unsafe output.
- [Local & Self-Hosted AI](../../concepts/local-ai.md) - Running open-weight models on your own hardware or cloud for privacy, cost control, and independence from API providers.
- [Rapid Prototyping](../../concepts/rapid-prototyping.md) - Building a fast proof of concept with managed services first, then hardening only what proves out, instead of over-engineering up front.

## Sources

- [If You're Serious About Building AI Agents, This is Your Secret Weapon](../../sources/if-youre-serious-about-building-ai-agents-this-is-your-secret-weapon.md) - "[0:00:17] It's a completely free and open-source tool that I've also added to my local AI stack and it's called Langfuse. Langfuse is an LLM engineering platform for agent observability."
- [The ONLY AI Tech Stack You Need in 2026](../../sources/the-only-ai-tech-stack-you-need-in-2026.md) - "[0:11:24] for every single run, you can see the token usage, the total cost, the latency, the tool calls that your agents are making."
- [Learn 90% of Building AI Agents in 30 Minutes](../../sources/learn-90-of-building-ai-agents-in-30-minutes.md) - "[0:24:02] I want to introduce you to Langfuse right now... we can set up the ability to watch for the actions that our agent is taking, view them in a dashboard"
- [Build and Ship Any MCP Server in MINUTES (Full Guide)](../../sources/build-and-ship-any-mcp-server-in-minutes-full-guide.md) - "[0:23:12] I use Langfuse as my platform more specifically to monitor agents, but then my whole like backend infrastructure and rag pipelines, Sentry is a great option."
- [Should I Build My AI Agents with n8n or Python?](../../sources/should-i-build-my-ai-agents-with-n8n-or-python.md) - "[0:11:08] you have tools like Langfuse for tracing. So you can get a lot of visibility and sort of a visualization into what is going on"
- [My Top 20 Lessons from Building 100s of AI Agents (Super Actionable)](../../sources/my-top-20-lessons-from-building-100s-of-ai-agents-super-actionable.md) - "[0:29:40] Langfuse is a really good one for sure... tools like Langfuse are also fantastic."
- [How I'd Learn AI Agents FAST if I Had to Start Over (Full Roadmap)](../../sources/how-id-learn-ai-agents-fast-if-i-had-to-start-over-full-roadmap.md) - "[0:14:26] there are a lot of good options for agent observability like Langfuse Helicone LangSmith Logfire"
- [Revealing my COMPLETE AI Agent Blueprint](../../sources/revealing-my-complete-ai-agent-blueprint.md) - "[0:11:51] Langfuse which is an open source LLM observability platform that's super awesome"
