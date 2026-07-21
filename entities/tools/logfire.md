---
type: entity
subtype: tool
title: "Logfire"
description: "Observability tool by the Pydantic team that instruments Pydantic AI agents to send traces, token usage, and cost as telemetry for local and production debugging."
resource: "https://pydantic.dev/logfire"
tags: [observability, pydantic, opentelemetry]
videos: [claude-skills-arent-just-for-claude-heres-how-to-build-them-for-any-agent, if-youre-serious-about-building-ai-agents-this-is-your-secret-weapon, revealing-my-complete-ai-agent-blueprint, weve-been-building-ai-agents-wrong-until-now]
created: 2026-07-21
updated: 2026-07-21
---

# Logfire

Logfire is the observability tool built by the Pydantic team, and it is Cole's natural first choice whenever he is working in [Pydantic AI](./pydantic-ai.md). He explains the fit directly: "that's why we need a tool like Logfire. So it's created by the Pydantic team. They also made Pydantic AI. So it's just a fantastic integration to have here" [0:22:52]. Because the same team makes both, it drops in with almost no friction and delivers [Agent Observability](../../concepts/agent-observability.md) out of the box.

## What it is

Logfire works by instrumentation: it hooks into an agent's execution and emits telemetry for everything the agent does. As Cole describes it, "it's going to instrument all the Pydantic agents as in every time we invoke a tool interact with the LLM. It's going to send all of that as telemetry data" [0:23:00]. That means traces, token usage, and cost for each run, captured whether you are debugging locally or watching a deployed agent. In his Pydantic AI series he reaches for it by default: "I'm going to configure Logfire for that amazing logging and monitoring that's included with Pydantic AI" [0:09:25], calling it "again open source, absolutely fantastic for monitoring" [0:12:06].

## How Cole uses it

Cole's key architectural insight is that Logfire is not necessarily the final destination for the data. It speaks OpenTelemetry, which lets it act as the bridge between the agent and a higher-level dashboard. He wires it into [Langfuse](./langfuse.md) exactly this way: "Langfuse can directly integrate with Logfire under the hood using open telemetry" [0:12:08], so that "Logfire is our connection between Pydantic AI, our agent, and Langfuse" [0:13:18]. Logfire becomes the instrumentation layer, Langfuse the viewing layer. This makes Logfire a foundational piece for anyone building [production-grade agents](../../concepts/production-grade-agents.md) on Pydantic AI, and it supports [agent evaluation](../../concepts/agent-evaluation.md) by making each run measurable.

## Related

- [Agent Observability](../../concepts/agent-observability.md) - the capability Logfire realizes at the instrumentation layer.
- [Agent Evaluation](../../concepts/agent-evaluation.md) and [Production-Grade Agents](../../concepts/production-grade-agents.md) - supported by its per-run telemetry.
- [Agent Deployment](../../concepts/agent-deployment.md), [Local & Self-Hosted AI](../../concepts/local-ai.md), [Model Selection](../../concepts/model-selection.md) - decisions its traces inform.
- Sibling tools: [Pydantic AI](./pydantic-ai.md) (the agent it instruments), [Langfuse](./langfuse.md) (the dashboard it feeds), [LangSmith](./langsmith.md).

## Sources

- [Claude Skills Aren't Just for Claude - Here's How to Build Them for ANY Agent](../../sources/claude-skills-arent-just-for-claude-heres-how-to-build-them-for-any-agent.md) - "[0:22:52] that's why we need a tool like Logfire. So it's created by the Pydantic team. They also made Pydantic AI. So it's just a fantastic integration to have here."
- [If You're Serious About Building AI Agents, This is Your Secret Weapon](../../sources/if-youre-serious-about-building-ai-agents-this-is-your-secret-weapon.md) - "[0:13:18] Logfire is our connection between Pydantic AI, our agent and Langfuse."
- [We've Been Building AI Agents WRONG Until Now](../../sources/weve-been-building-ai-agents-wrong-until-now.md) - "[0:09:25] I'm going to configure Logfire for that amazing logging and monitoring that's included with Pydantic AI"
- [Revealing my COMPLETE AI Agent Blueprint](../../sources/revealing-my-complete-ai-agent-blueprint.md) - "[0:12:06] if you're using Pydantic AI like I'm going to be using in the series you have Logfire which is again open source absolutely fantastic for monitoring"
