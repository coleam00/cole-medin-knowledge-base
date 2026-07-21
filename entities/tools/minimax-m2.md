---
type: entity
subtype: tool
title: "MiniMax M2.7"
description: "A cheap, fast, capable LLM that Cole routes Claude Code to (via environment variables) to drive the entire dark factory economically at high throughput instead of Anthropic models."
tags: [llm, model]
videos: [im-building-an-ai-dark-factory-that-ships-its-own-code-public-experiment]
created: 2026-07-21
updated: 2026-07-21
---

# MiniMax M2.7

MiniMax M2.7 is the model Cole puts behind the [dark factory](../../concepts/dark-factory.md), and he is unusually blunt that the choice has nothing to do with capability rankings: "I want to use M2.7. And it's a purely economical decision" [0:16:22]. The justification is throughput per dollar rather than peak quality - "Miniax M2.7, it's a pretty powerful model. It's very cheap and fast, though. So it's going to allow us to run the experiment continuously" [0:16:42].

The word doing the work there is *continuously*. A dark factory is not one impressive run; it is a cron loop that triages GitHub issues, dispatches parallel implementation workflows in [git worktrees](./git-worktree.md), and runs a separate validation pass, over and over, indefinitely. At Anthropic pricing that loop is a budget decision every hour. At MiniMax pricing it is background noise, so the experiment can stay running long enough to actually learn something. This is [LLM cost optimization](../../concepts/llm-cost-optimization.md) applied to agentic coding rather than to serving traffic: the cheap model is not handling the easy requests, it is handling everything, because the system's reliability is meant to come from governance and validation rather than from model brilliance.

Mechanically it is a swap, not a rewrite. [Claude Code](./claude-code.md) remains the coding agent and [Archon](./archon.md) remains the workflow engine; Claude Code is simply routed to M2.7 through environment variables. That is [provider independence](../../concepts/provider-independence.md) paying off exactly where it is supposed to - the harness, the governance files (mission, factory rules, global rules), and the workflows are all model-agnostic, so the most expensive component in the stack becomes a config line.

The bet is explicit and falsifiable. If shipping unreviewed code depends on a frontier model, routing to a budget model should break the factory, and the [separate reviewer](../../concepts/separate-reviewer.md) plus [end-to-end validation](../../concepts/end-to-end-validation.md) layers should show it. If the governance layer is what carries reliability, then model spend was never the constraint. Given how badly [error rates compound](../../concepts/compounding-error-rates.md) across a long autonomous chain, that is the question worth answering, and running cheap is what makes answering it affordable.

## Realizes

- [LLM Cost Optimization](../../concepts/llm-cost-optimization.md) - Systematically cutting the bill for running LLM systems at scale rather than paying premium rates by default.
- [Model Selection](../../concepts/model-selection.md) - Choosing the right LLM per task by trading off quality, speed, and cost.
- [Provider Independence](../../concepts/provider-independence.md) - Architecting so the underlying model can be swapped without a rewrite, here via environment variables.
- [Dark Factory](../../concepts/dark-factory.md) - A self-evolving codebase where autonomous workflows build and merge a product with no human review.

## Works with

- [Claude Code](./claude-code.md) - The coding agent that stays in place and is simply pointed at M2.7 through environment variables.
- [Archon](./archon.md) - The harness and workflow engine running triage, implementation, and validation on a cron loop.
- [Git Worktrees](./git-worktree.md) - The isolation that lets many cheap agent runs execute in parallel without collisions.

## Contrasts with

- [Claude Opus 4.8](./claude-opus-4-8.md) - Anthropic's reasoning-heavy model, the expensive default M2.7 displaces in the loop.
- [Claude Sonnet 4.5](./claude-sonnet-4-5.md) - Anthropic's coding-focused release and Claude Code's default model.
- [Kimi K2](./kimi-k2.md) - Another cheap, capable non-Anthropic model in the same budget tier.
- [DeepSeek V3](./deepseek-v3.md) - Open model Cole cites as evidence the cheap-versus-frontier gap keeps closing.
- [Qwen 2.5 Coder 32B](./qwen.md) - Alibaba's open model family, the self-hosted route to cheap tokens.
- [OpenRouter](./openrouter.md) - Unified gateway that makes this kind of model swap a routing choice rather than an integration.

## Related

- [The Five Levels of AI Coding Autonomy](../../concepts/five-levels-of-ai-coding-autonomy.md) - Dan Shapiro's ladder from spicy autocomplete to the level-5 dark factory this model powers.
- [Agentic Workflow Engineering](../../concepts/agentic-workflow-engineering.md) - Designing repeatable AI workflows as engineered systems with defined steps and background execution.
- [Deterministic Workflows](../../concepts/deterministic-workflows.md) - Encoding known steps as fixed code paths and reserving the LLM for genuinely fuzzy decisions.
- [Separate Reviewer](../../concepts/separate-reviewer.md) - Splitting authoring and grading across agents so the reviewer is not biased by its own code.
- [End-to-End Validation](../../concepts/end-to-end-validation.md) - Proving a feature works through the real interface instead of trusting stored unit tests.
- [Parallel Agentic Coding](../../concepts/parallel-agentic-coding.md) - Dispatching background agents in isolated worktrees, which cheap tokens make practical at volume.
- [Long-Running Agents](../../concepts/long-running-agents.md) - Agents that run for hours or days, where per-token cost compounds into a real bill.
- [The Ralph Loop](../../concepts/the-ralph-loop.md) - Re-running an agent against the same state so each pass compounds reliability.
- [Compounding Error Rates](../../concepts/compounding-error-rates.md) - Why a long autonomous chain needs governance rather than a better model alone.
- [System Evolution](../../concepts/system-evolution.md) - Building systems that improve themselves over time with minimal human touch.

## Sources

- [I'm Building an AI Dark Factory That Ships Its Own Code (Public Experiment)](../../sources/im-building-an-ai-dark-factory-that-ships-its-own-code-public-experiment.md) - "[0:16:22] I want to use M2.7. And it's a purely economical decision"
- [I'm Building an AI Dark Factory That Ships Its Own Code (Public Experiment)](../../sources/im-building-an-ai-dark-factory-that-ships-its-own-code-public-experiment.md) - "[0:16:42] Miniax M2.7, it's a pretty powerful model. It's very cheap and fast, though. So it's going to allow us to run the experiment continuously"
