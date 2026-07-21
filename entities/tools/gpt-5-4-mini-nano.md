---
type: entity
subtype: tool
title: "GPT-5.4 Mini & Nano"
description: "OpenAI's small/fast model releases marketed explicitly for subagents and AI coding; nano reportedly beats Claude Haiku 4.5 at a fifth the price and ~188 tok/s, anchoring the 'subagent era' thesis."
tags: [llm, model, model-selection, subagents]
videos: [the-subagent-era-is-officially-here-learn-this-now]
created: 2026-07-21
updated: 2026-07-21
---

# GPT-5.4 Mini & Nano

GPT-5.4 Mini and Nano are OpenAI's small, fast tier of the GPT-5.4 line, and what makes them worth a page is less the weights than the marketing copy attached to them: they were released as models *for subagents and AI coding*. Cole reads the launch as a signal about where the industry is heading rather than as a product announcement: "what's more important here is the message from OpenAI. They are putting a lot of effort into designing LLM that are specifically meant to be used for sub agents" [0:00:15]. Nano is reported to beat Claude Haiku 4.5 at roughly a fifth of the price and around 188 tokens per second, and that price-per-token collapse is the fact the rest of the argument stands on.

The reason a subagent-shaped model makes sense is that delegated work has an unusual profile: enormous token volume, modest reasoning demand. Cole states the tradeoff directly - "the work that we're delegating to the sub agents are the kind of things that are super token heavy, but also don't require as much reasoning power. So, it's overkill to use something like GPT 5.4 high or claude opus 4.6" [0:04:39]. Codebase analysis, web research, and code review all fit that shape, so paying flagship rates for them burns a weekly rate limit on work a cheap model does just as well.

The pattern is already baked into the tools. Describing [Claude Code](./claude-code.md)'s built-in delegation, Cole notes: "these built-in sub agents are smart enough to use faster and cheaper models under the hood... They are using either haiku or sonnet under the hood instead of opus which is the model that my main context window is working in" [0:11:40]. GPT-5.4 Mini and Nano are [OpenAI](../organizations/openai.md)'s version of that same bet, and as the effective budget for delegation trends toward unlimited, the binding constraint stops being cost and becomes [Context Rot](../../concepts/context-rot.md) - which is exactly what subagents exist to solve.

## Realizes

- [Subagents Pattern](../../concepts/subagents-pattern.md) - Delegating scoped tasks to isolated subagents to parallelize work and protect the main agent's context window.
- [Model Selection](../../concepts/model-selection.md) - Choosing the right LLM per task, which here means routing token-heavy but reasoning-light delegation to the cheapest capable model.
- [LLM Cost Optimization](../../concepts/llm-cost-optimization.md) - Paying premium rates only for the rare hard request and sending the bulk of traffic to far cheaper models.
- [Context Isolation](../../concepts/context-isolation.md) - Giving each subagent its own clean window so only a small synthesized summary returns to the main agent.

## Contrasts with

- [Claude Opus 4.8](./claude-opus-4-8.md) - The reasoning-heavy Claude tier that stays in the main context window and is overkill for delegated work.
- [Claude Sonnet 4.5](./claude-sonnet-4-5.md) - The mid-tier coding driver that built-in subagents fall back to when a task needs more than the cheapest model.
- [GPT-4.1 Nano](./gpt-4-1-nano.md) - The earlier smallest-and-cheapest OpenAI model, used for reasoning-light per-chunk work in contextual retrieval.

## Works with

- [Claude Code](./claude-code.md) - Anthropic's terminal-based agentic coding tool, whose built-in subagents already run cheaper models under the hood.
- [Codex](./codex.md) - OpenAI's coding agent, the harness these models are aimed at.
- [OpenRouter](./openrouter.md) - Unified API gateway that makes swapping a subagent's model a one-line change.

## Related

- [Context Rot](../../concepts/context-rot.md) - The degradation subagent delegation exists to prevent.
- [Context Window Limits](../../concepts/context-window-limits.md) - The finite budget that makes offloading token-heavy work valuable.
- [Parallel Agent Execution](../../concepts/parallel-agent-execution.md) - Running delegated work concurrently, now economically viable at these prices.
- [Agent Teams](../../concepts/agent-teams.md) - The larger coordination pattern, which Cole warns should still never own implementation.
- [GPT-4o mini](./gpt-4o-mini.md) - The prior generation's cheap-and-fast OpenAI model and long-time latency yardstick.

## Sources

- [The Subagent Era Is Officially Here - Learn this Now](../../sources/the-subagent-era-is-officially-here-learn-this-now.md) - "[0:00:15] what's more important here is the message from OpenAI. They are putting a lot of effort into designing LLM that are specifically meant to be used for sub agents"
- [The Subagent Era Is Officially Here - Learn this Now](../../sources/the-subagent-era-is-officially-here-learn-this-now.md) - "[0:04:39] the work that we're delegating to the sub agents are the kind of things that are super token heavy, but also don't require as much reasoning power. So, it's overkill to use something like GPT 5.4 high or claude opus 4.6."
- [The Subagent Era Is Officially Here - Learn this Now](../../sources/the-subagent-era-is-officially-here-learn-this-now.md) - "[0:11:40] these built-in sub agents are smart enough to use faster and cheaper models under the hood... They are using either haiku or sonnet under the hood instead of opus which is the model that my main context window is working in."
