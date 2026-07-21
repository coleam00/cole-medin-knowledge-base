---
type: concept
title: "LLM Cost Optimization"
description: "Systematically cutting the bill for running LLM applications at scale by sending the bulk of cheap-to-serve traffic to far cheaper models and paying premium rates only for the rare hard requests."
tags: [cost, production]
videos: [ai-is-too-expensive-if-you-dont-do-this]
created: 2026-07-21
updated: 2026-07-21
---

# LLM Cost Optimization

LLM cost optimization is the discipline of driving down the per-request cost of an AI application without giving up the quality users notice. It only becomes a real problem at scale: "using large language models to create AI applications is insanely expensive... when you have a full production application with a lot of users you are quickly going to get a bill for thousands of dollars" [0:00:00]. A prototype hides this because a handful of test requests cost nothing. Production surfaces it because the bill is linear in traffic, so every unit of waste multiplies by user count.

The core move is refusing to pay frontier prices for easy work. Most production traffic is simple (classification, extraction, short answers, routine tool calls) and a small model handles it indistinguishably. So you put a cheap router in front and let it decide which requests genuinely need the expensive model: "it is Pennies on the dollar if most of the requests can go to the cheaper model even if you have to pay for this first step of using the AI router" [0:02:19]. That last clause is the important accounting insight - the router itself costs tokens, and it still wins, because the routing call is priced like the cheap tier while the savings come off the expensive tier.

## Builds on

- [Model Selection](./model-selection.md) - routing presumes you have already ranked models by capability *and* price per token, so you know what the cheap tier can safely absorb.
- [Multi-Model Agents](./multi-model-agent.md) - the architecture that makes cost tiering possible: one system, several models, each chosen per step.

## Contrasts with

- [Self-Hosting Cost Crossover](./self-hosting-cost-crossover.md) - the other lever on the same bill. Routing optimizes *within* per-token pricing; self-hosting swaps per-token pricing for fixed hardware cost once volume is high enough.
- [Usage-Based Pricing Trap](./usage-based-pricing-trap.md) - the revenue-side mirror image: if your customers pay per seat while your models charge per token, cost optimization is the only thing protecting the margin.

## Related

- [Prompt Caching](./prompt-caching.md) - the complementary lever, cutting cost on the repeated prefix of every request rather than on model choice.
- [Context Engineering](./context-engineering.md) - fewer wasted tokens in context is a direct, permanent discount on every call.
- [Reasoning Model as a Tool](./reasoning-model-as-a-tool.md) - the same tiering idea taken further: call the slow expensive reasoner only as an escalation path.
- [Production-Grade Agents](./production-grade-agents.md), [Production vs. Personal Agents](./production-vs-personal-agents.md) - cost only becomes a first-class constraint once an agent has real users.
- [Local & Self-Hosted AI](./local-ai.md) - running open weights yourself removes per-token cost entirely for workloads that fit your hardware.
- [Mixture of Experts](./mixture-of-experts.md) - the in-model analogue of routing: activate only the parameters a token needs.

## Tools

- [OpenRouter](../entities/tools/openrouter.md) - one API across providers, which makes swapping in a cheaper model per request a config change instead of a rewrite.
- [GPT-4o mini](../entities/tools/gpt-4o-mini.md), [GPT-4.1 nano](../entities/tools/gpt-4-1-nano.md), [Gemini 3.5 Flash](../entities/tools/gemini-3-5-flash.md) - the cheap tier that absorbs the routed majority.
- [Langfuse](../entities/tools/langfuse.md) - per-request cost tracking, without which optimization is guesswork.
- [GPT-5.4 Mini & Nano](../entities/tools/gpt-5-4-mini-nano.md) - OpenAI's small/fast model releases marketed explicitly for subagents and AI coding; nano reportedly beats Claude Haiku 4.5 at a fifth the price and ~188 tok/s, anchoring the "subagent era" thesis.
- [OpenTelemetry](../entities/tools/opentelemetry.md) - The open telemetry standard that agent frameworks (Pydantic AI via Logfire) emit traces through, letting any compatible backend such as Langfuse ingest them without vendor lock-in.
- [Abacus.AI](../entities/organizations/abacus-ai.md) - The AI company behind ChatLLM, offering a consolidated multi-model chat product with connectors to Teams, Jira, Confluence, Google Drive, and Slack.
- [Kimi K2](../entities/tools/kimi-k2.md) - Moonshot's Kimi model (K2.7), used as a cheap driver and exploration model in Cole's harness via a Kimi subscription to control per-token cost.
- [MiniMax M2.7](../entities/tools/minimax-m2.md) - A cheap, fast, capable LLM that Cole routes Claude Code to (via environment variables) to drive the entire dark factory economically at high throughput instead of Anthropic models.

## Sources

- [AI is TOO EXPENSIVE if You Don't Do This](../sources/ai-is-too-expensive-if-you-dont-do-this.md) - "[0:00:00] using large language models to create AI applications is insanely expensive... when you have a full production application with a lot of users you are quickly going to get a bill for thousands of dollars"
- [AI is TOO EXPENSIVE if You Don't Do This](../sources/ai-is-too-expensive-if-you-dont-do-this.md) - "[0:02:19] it is Pennies on the dollar if most of the requests can go to the cheaper model even if you have to pay for this first step of using the AI router"
