---
type: entity
subtype: tool
title: "GPT-5 Codex"
description: "OpenAI's coding-specialized GPT-5 model, the head-to-head opponent Cole benchmarks against Sonnet 4.5 on an identical real-world Stripe integration task."
tags: [llm, model]
videos: [claude-sonnet-45-the-new-coding-king-sonnet-45-vs-gpt-5-codex]
created: 2026-07-21
updated: 2026-07-21
---

# GPT-5 Codex

GPT-5 Codex is [OpenAI](../organizations/openai.md)'s coding-specialized variant of GPT-5, the model that drives the [Codex](./codex.md) agent. In Cole's catalog it appears almost entirely in one role: the opponent. When [Claude Sonnet 4.5](./claude-sonnet-4-5.md) landed at the top of the coding leaderboards, he refused to take the charts at face value and ran both models against the same real task, splitting his screen between the two harnesses: "On the left side, I've got Codeex running with GBT5 codecs for the LLM" [0:01:47].

The setup is what makes the comparison a genuine [real-world coding benchmark](../../concepts/coding-benchmarks.md) rather than a vibe check. Both agents receive an identical PRP-style requirements document (a [PRD-first](../../concepts/prd-first-development.md) contract), both work off the same pre-Stripe codebase on isolated Git branches, and both track their task lists in [Archon](./archon.md). The task, adding a [Stripe](../organizations/stripe.md) token-purchase integration to an existing complex application, sits in the sweet spot where models make visible mistakes without the app collapsing.

The headline result is wall-clock time. Cole's summary is blunt: "It took 1 hour and 20 minutes in total for the implementation while Sonnet 4.5 took 15 minutes" [0:08:06]. Codex also shipped three or four rough edges against Sonnet's two minor ones. His verdict avoids the usual dunk, though - Codex still produced a working integration off the same spec, and he calls it "really solid," just slower and rougher on this particular build. That is the useful shape of the finding for [model selection](../../concepts/model-selection.md): on a mid-sized brownfield feature the gap is speed and polish, not capability, and both models cleared the bar the spec set.

## Realizes

- [Real-World Coding Benchmarks](../../concepts/coding-benchmarks.md) - Evaluating coding models on real engineering tasks instead of leaderboard scores.
- [Agentic Coding](../../concepts/agentic-coding.md) - Letting an AI agent drive a feature end-to-end from planning through implementation and validation.
- [Model Selection](../../concepts/model-selection.md) - Choosing the right LLM per task by trading off quality, speed, and cost.

## Contrasts with

- [Claude Sonnet 4.5](./claude-sonnet-4-5.md) - The head-to-head opponent on the identical Stripe integration, roughly five times faster on the same spec.
- [Claude Opus 4.8](./claude-opus-4-8.md) - Anthropic's reasoning-heavy tier, the model Cole reaches for on planning-shaped work.
- [GPT-5.4 Mini & Nano](./gpt-5-4-mini-nano.md) - The small, delegation-focused end of the same OpenAI lineup, aimed at subagents rather than main-thread implementation.

## Works with

- [Codex](./codex.md) - OpenAI's cloud and CLI software-engineering agent, the harness this model runs inside.
- [Archon](./archon.md) - Cole's open-source AI command center, used here to track both agents' task lists during the benchmark.
- [Git Worktrees](./git-worktree.md) - The isolation mechanism that lets competing agents build the same feature without collisions.

## Related

- [PRP Framework](../../concepts/prp-framework.md) - The structured requirements-prompt format both agents were handed as their identical contract.
- [AI Coding Harness](../../concepts/ai-coding-harness.md) - The scaffolding around the raw model that decides how much of its capability actually lands.
- [Validation](../../concepts/validation.md) - The explicit checks that caught the rough edges each agent left behind.

## Sources

- [Claude Sonnet 4.5 - The New Coding King? (Sonnet 4.5 vs. GPT 5 Codex)](../../sources/claude-sonnet-45-the-new-coding-king-sonnet-45-vs-gpt-5-codex.md) - "[0:01:47] On the left side, I've got Codeex running with GBT5 codecs for the LLM"
- [Claude Sonnet 4.5 - The New Coding King? (Sonnet 4.5 vs. GPT 5 Codex)](../../sources/claude-sonnet-45-the-new-coding-king-sonnet-45-vs-gpt-5-codex.md) - "[0:08:06] It took 1 hour and 20 minutes in total for the implementation while Sonnet 4.5 took 15 minutes"
