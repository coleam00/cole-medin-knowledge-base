---
type: entity
subtype: tool
title: "Vertex AI"
description: "Google's cloud AI platform offering powerful agent capabilities out of the box, recommended in Google's agent white paper."
resource: "https://cloud.google.com/vertex-ai"
tags: [deployment, infrastructure]
videos: [google-anthropic-and-openais-guides-to-ai-agents-all-in-18-minutes]
created: 2026-07-21
updated: 2026-07-21
---

# Vertex AI

Vertex AI is Google's managed cloud platform for building and running AI agents, and Cole introduces it exactly as Google's own agent white paper does: "They also cover Vertex AI. That's their cloud offering that gives you a lot of powerful agent capabilities right out of the box" [0:15:44]. The phrase "out of the box" is the whole definition. Where a from-scratch stack makes you assemble the model, the tool layer, memory, tracing, and a deployment target yourself, Vertex AI is the version where those [core agent components](../../concepts/agent-core-components.md) arrive pre-wired and hosted.

It surfaces in Cole's catalog inside his condensed read of the Google, Anthropic, and OpenAI agent guides, and its placement there matters more than its feature list. He deliberately keeps that guide "very framework agnostic... not focusing on specific tools or frameworks" [0:15:44], then names the vendor-specific things each guide leans on: Google pushes prompt templates, [LangChain](./langchain.md), and Vertex AI; OpenAI pushes its own [Agents SDK](./openai-agents-sdk.md). Vertex AI is therefore best read as Google's answer to [agent deployment](../../concepts/agent-deployment.md), one option among frameworks he rates highly like [Pydantic AI](./pydantic-ai.md), [CrewAI](./crewai.md), and [smolagents](./smolagents.md), not as a required layer.

That framing lines up with the closing argument of the same video, which is to focus on outcomes rather than architectural complexity. A managed platform is attractive precisely when the goal is a working agent rather than a bespoke harness: it is the buy side of [buy vs. build](../../concepts/buy-vs-build.md), and the counterweight to [running models yourself](../../concepts/local-ai.md) for privacy or cost reasons. Within [Google's](../organizations/google.md) own tooling it sits under the [ADK](./google-adk.md) and the [Agents CLI](./google-agents-cli.md), which deploy to it, and it runs the [Gemini](./gemini.md) models those tools default to.

## Realizes

- [Agent Deployment](../../concepts/agent-deployment.md) - Getting agents to production, containerizing, networking, reverse-proxying, and choosing a provider-agnostic, cost-predictable host.
- [Production-Grade Agents](../../concepts/production-grade-agents.md) - Real agents need validation, error handling, testing, logging, observability, and monitoring rather than just an LLM plus tools stitched together.

## Works with

- [Google ADK (Agent Development Kit)](./google-adk.md) - Google's minimalistic agent framework giving full control over prompting and tooling, with sandboxed code execution and one-command deployment to Google Cloud.
- [Google Agents CLI](./google-agents-cli.md) - Google's free open-source CLI and skill collection that instructs a coding agent to build, evaluate, deploy, and monitor agents on the ADK.
- [Google Gemini 2.0 Flash](./gemini.md) - Google's LLM line; Gemini 2.5 led general-purpose models for months and Gemini 3 is considered the most powerful general LLM at year-end.
- [Google](../organizations/google.md) - Author of the A2UI generative-UI specification used in the demo.

## Contrasts with

- [Local & Self-Hosted AI](../../concepts/local-ai.md) - Running open-weight models on your own hardware or cloud for privacy, cost control, and independence from API providers.
- [LangChain](./langchain.md) - The framework used in prior masterclass videos to build the Asana agent; its message objects and invoke/stream methods underpin the chatbot logic.
- [OpenAI Agents SDK](./openai-agents-sdk.md) - OpenAI's agent framework, which their guide leans on heavily with code examples.

## Related

- [Buy vs. Build](../../concepts/buy-vs-build.md) - For a classic, well-solved use case, leaning on a robust existing platform beats building it yourself, since wiring up all the tools and integrations is real work even for a technical builder.
- [The Core Components of an Agent](../../concepts/agent-core-components.md) - Every AI agent reduces to four parts: the LLM (brain), tools (actions), the system prompt (instructions), and memory (context).
- [Cloud GPU Hosting](../../concepts/cloud-gpu-hosting.md) - Renting GPU machines in the cloud (VRAM-sized to the model, e.g. a 48GB A40 for Llama 3.1 70B) to self-host models without owning, powering, maintaining, or upgrading hardware.
- [Agent Observability](../../concepts/agent-observability.md) - Instrumenting agents with tracing, logging, and cost/token metrics so you can see and debug what they actually did.
- [Prompt Templating](../../concepts/prompt-templating.md) - Defining named variables (e.g. {{prompt}}, {{context}}) inside a node's prompt to create typed inputs the workflow can wire data into.

## Sources

- [Google, Anthropic, and OpenAI's Guides to AI Agents ALL in 18 Minutes](../../sources/google-anthropic-and-openais-guides-to-ai-agents-all-in-18-minutes.md) - "[0:15:44] They also cover Vertex AI. That's their cloud offering that gives you a lot of powerful agent capabilities right out of the box."
