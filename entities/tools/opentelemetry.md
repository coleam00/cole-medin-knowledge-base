---
type: entity
subtype: tool
title: "OpenTelemetry"
description: "The open telemetry standard that agent frameworks (Pydantic AI via Logfire) emit traces through, letting any compatible backend such as Langfuse ingest them without vendor lock-in."
resource: "https://opentelemetry.io"
tags: [observability, validation, standard, telemetry, integration]
videos: [if-youre-serious-about-building-ai-agents-this-is-your-secret-weapon]
created: 2026-07-21
updated: 2026-07-21
---

# OpenTelemetry

OpenTelemetry is the open standard for shipping trace and log data out of an application, and in Cole's agent stack it is the wire format that makes [agent observability](../../concepts/agent-observability.md) portable. He introduces it while explaining how two separate tools end up talking to each other: Langfuse "supports this open telemetry backend which is basically a standard for communicating this kind of log data that we want to use in Langfuse. So Langfuse can directly integrate with log fire under the hood using open telemetry" [0:11:52]. The instrumenting library and the dashboard never need to know about each other, because both speak the same protocol.

## What it is

Practically, OpenTelemetry defines how spans (a tool call, an LLM generation, a whole agent run) are structured and transmitted, along with their attributes: token counts, cost, latency, inputs and outputs. [Pydantic AI](./pydantic-ai.md) emits those spans through [Logfire](./logfire.md), and the switch is a single argument: "you just have to make sure that you include this instrument parameter so that we have logfire enabled and the agent is going to be sending communication through open telemetry" [0:12:36] as it invokes tools and generates responses. From there, [Langfuse](./langfuse.md) ingests the stream and becomes the viewing layer, with Logfire acting purely as the instrumentation bridge. Because the span schema is open, Cole can also set custom attributes such as user ID and session ID so traces group into real conversations.

## Why it matters

The standard is what turns observability into a swappable component rather than a commitment. Any framework that emits OpenTelemetry can be pointed at any compatible backend, which is the [provider-independence](../../concepts/provider-independence.md) argument applied to monitoring, and it is part of why Cole prefers open-source [Langfuse](./langfuse.md) over closed alternatives like [LangSmith](./langsmith.md): the data leaves your agent in a format you own. It is the same instinct behind [tool standardization](../../concepts/tool-standardization.md) with MCP, one interface many implementations. For [production-grade agents](../../concepts/production-grade-agents.md), that neutrality is what makes it safe to instrument everything up front and decide where the traces land later, including a fully self-hosted stack.

## Realizes

- [Agent Observability](../../concepts/agent-observability.md) - Instrumenting agents with tracing, logging, and cost/token metrics so you can see and debug what they actually did.
- [Provider Independence](../../concepts/provider-independence.md) - Architecting so the underlying component can be swapped without a rewrite, here applied to the observability backend.

## Works with

- [Logfire](./logfire.md) - Pydantic's observability tool; the instrumentation layer that emits OpenTelemetry spans from an agent.
- [Pydantic AI](./pydantic-ai.md) - Cole's agent framework, which starts emitting telemetry as soon as you pass the instrument parameter.
- [Langfuse](./langfuse.md) - The open-source platform that ingests the OpenTelemetry stream and renders it as inspectable traces.
- [Sentry](./sentry.md) - Application monitoring for the surrounding backend and RAG infrastructure, alongside agent-level traces.

## Contrasts with

- [LangSmith](./langsmith.md) - A closed competing observability platform, the lock-in an open telemetry standard is meant to avoid.

## Related

- [Production-Grade Agents](../../concepts/production-grade-agents.md) - Real agents need logging, observability, and monitoring, not just an LLM plus tools.
- [Agent Deployment](../../concepts/agent-deployment.md) - Getting agents to production, a step Cole refuses to take without tracing in place.
- [Agent Evaluation](../../concepts/agent-evaluation.md) - Scoring agent behavior, made measurable by per-run span data.
- [Tool Standardization (USB-C for AI)](../../concepts/tool-standardization.md) - The same one-interface-many-implementations logic that MCP applies to tools.
- [Local & Self-Hosted AI](../../concepts/local-ai.md) - Running the whole stack yourself, which an open wire format keeps possible.
- [LLM Cost Optimization](../../concepts/llm-cost-optimization.md) - Cutting spend using the per-request cost and token data traces expose.

## Sources

- [If You're Serious About Building AI Agents, This is Your Secret Weapon](../../sources/if-youre-serious-about-building-ai-agents-this-is-your-secret-weapon.md) - "[0:11:52] It supports this open telemetry backend which is basically a standard for communicating this kind of log data that we want to use in Langfuse."
- [If You're Serious About Building AI Agents, This is Your Secret Weapon](../../sources/if-youre-serious-about-building-ai-agents-this-is-your-secret-weapon.md) - "[0:12:36] you just have to make sure that you include this instrument parameter so that we have logfire enabled and the agent is going to be sending communication through open telemetry."
