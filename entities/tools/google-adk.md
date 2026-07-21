---
type: entity
subtype: tool
title: "Google ADK (Agent Development Kit)"
description: "Google's minimalistic agent framework giving full control over prompting and tooling, with sandboxed code execution and one-command deployment to Google Cloud."
resource: "https://google.github.io/adk-docs/"
tags: [agent-framework, sdk]
videos: [googles-agents-cli-the-cli-skills-combination-to-ship-ai-agents-easily, harness-engineering-what-separates-top-agentic-engineers-right-now]
created: 2026-07-21
updated: 2026-07-21
---

# Google ADK (Agent Development Kit)

The Google ADK is Google's agent framework: a deliberately minimal library for defining agents, their tools, and their orchestration, without the heavy abstractions that hide the prompt from you. Cole positions it as a mainstream default rather than a niche pick - "It helps us build agents with Google's ADK which is an agent framework that a lot of people are using" ([0:00:15]) - and reaches for it when the job is a production agent that must be deployed, evaluated, and monitored rather than a quick script.

## How Cole uses it / why it matters

Two capabilities make ADK stand out in Cole's coverage. The first is sandboxed [Code Execution](../../concepts/code-execution.md), which he calls out as the framework's best feature: "This is one of the best parts of the ADK is code execution. A lot of agents rely on that now" ([0:07:15]). Giving an agent a sandbox to write and run code is the general-purpose alternative to bolting on a dozen narrow tools, and ADK ships it rather than making you build it - a direct answer to the [capabilities-over-tools](../../concepts/capabilities-over-tools.md) argument.

The second is that ADK treats [Agent Deployment](../../concepts/agent-deployment.md) as part of the framework, not an afterthought: "When you're ready to take your agent to production, it is a single command to deploy your Google agent SDK agent to the Google Cloud... your agent gets its own identity in the cloud" ([0:08:51]). That cloud identity matters as much as the convenience, because it gives the agent scoped credentials of its own instead of borrowing a developer's. Combined with ADK's built-in eval and tracing surfaces, this is what makes it a credible answer to the [SDK vs. Framework Decision](../../concepts/sdk-vs-framework-decision.md): you keep full control of prompting and tooling like a from-scratch framework, but inherit the production path of an SDK.

## Realizes

- [Code Execution](../../concepts/code-execution.md) - Ships a sandbox where the agent writes and runs code as a general-purpose tool.
- [Agent Deployment](../../concepts/agent-deployment.md) - One command to production, with the agent getting its own cloud identity.
- [The Core Components of an Agent](../../concepts/agent-core-components.md) - Exposes the LLM, tools, system prompt, and memory directly rather than abstracting them away.
- [Agent Evaluation](../../concepts/agent-evaluation.md) - Built-in evalsets and scoring as a gate before shipping.
- [Agent Observability](../../concepts/agent-observability.md) - Tracing and production monitoring wired into the same toolchain.

## Contrasts with

- [Pydantic AI](./pydantic-ai.md) - Cole's default Python agent framework, the closest peer on minimalism and type safety.
- [OpenAI Agents SDK](./openai-agents-sdk.md) - OpenAI's competing agent framework with its own hosted deployment story.
- [LangGraph](./langgraph.md) - Graph-first orchestration with explicit nodes, edges, and state, a heavier abstraction than ADK's.
- [Claude Agent SDK](./claude-agent-sdk.md) - A coding-agent harness exposed as a library, the other side of the SDK-versus-framework choice.
- [CrewAI](./crewai.md) - A higher-abstraction multi-agent framework that hides more of the prompt.

## Works with

- [Google Agents CLI](./google-agents-cli.md) - The CLI and skill collection that instructs a coding agent to build, deploy, and monitor ADK agents.
- [Vertex AI](./vertex-ai.md) - Google's model and agent platform ADK agents deploy onto.
- [Python](./python.md) - The primary language ADK agents are written in.

## Related

- [Agent Development Lifecycle](../../concepts/agent-development-lifecycle.md) - Plan, build, evaluate, deploy, observe, the loop ADK covers end to end.
- [SDK vs. Framework Decision](../../concepts/sdk-vs-framework-decision.md) - Choosing between a batteries-included SDK and a from-scratch framework.
- [Capabilities Over Tools](../../concepts/capabilities-over-tools.md) - Why a code sandbox beats a long list of rigid tool definitions.
- [Production-Grade Agents](../../concepts/production-grade-agents.md) - The bar ADK's deployment, eval, and tracing surfaces are aimed at.

## Sources

- [Google's Agents CLI: The CLI + Skills Combination to Ship AI Agents EASILY](../../sources/googles-agents-cli-the-cli-skills-combination-to-ship-ai-agents-easily.md) - "[0:00:15] I want you to install the Google Agent CLI... It helps us build agents with Google's ADK which is an agent framework that a lot of people are using."
- [Google's Agents CLI: The CLI + Skills Combination to Ship AI Agents EASILY](../../sources/googles-agents-cli-the-cli-skills-combination-to-ship-ai-agents-easily.md) - "[0:07:15] This is one of the best parts of the ADK is code execution. A lot of agents rely on that now."
- [Harness Engineering: What Separates Top Agentic Engineers Right Now](../../sources/harness-engineering-what-separates-top-agentic-engineers-right-now.md) - "[0:08:51] When you're ready to take your agent to production, it is a single command to deploy your Google agent SDK agent to the Google Cloud... your agent gets its own identity in the cloud."
