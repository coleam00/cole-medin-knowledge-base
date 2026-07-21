---
type: entity
subtype: tool
title: "Kimi K2"
description: "Moonshot's Kimi model (K2.7), used as a cheap driver and exploration model in Cole's harness via a Kimi subscription to control per-token cost."
tags: [llm, model, cost-optimization, harness]
videos: [the-creators-of-claude-code-and-openclaw-dont-prompt-their-agents-anymore]
created: 2026-07-21
updated: 2026-07-21
---

# Kimi K2

Kimi K2 is Moonshot's coding-capable LLM family, and in Cole's harness work it plays a specific economic role rather than a headline one: it is the cheap model you assign to the many steps that do not need a frontier model. "For all of our context loading and exploration up front we can use a smaller model like Kimi K 2.7" [0:11:57]. Reading files, classifying issues, and gathering context are high-volume, low-judgment operations, and paying premium per-token rates for them is the single easiest way to make an autonomous loop uneconomical.

That matters because the honest downside of loop engineering is cost. Cole is blunt that loops are extremely token hungry - one simple app ran past a million tokens because the orchestrator repeatedly reasons and dispatches waves of workers. His fix is not fewer loops but per-node [model selection](../../concepts/model-selection.md) inside an [Archon](./archon.md) workflow: a small model like Kimi for classification and exploration, a strong coding model for implementation, a different model again for review. Each node runs in its own coding-agent session, so swapping the model per step costs nothing architecturally.

He also runs the orchestration layer on it outright. "I'm actually using my Kimi subscription with Kimi K 2.7 to drive all of these workflows" [0:19:04]. A flat subscription rather than metered API billing changes the calculus for a loop that never stops running - the orchestrator can poll, re-plan, and dispatch as often as the design wants without the bill scaling linearly with ambition. In his loop-engineering dashboard, [Pi](./pi-coding-agent.md) is the agent and Kimi is the model behind it, which is also a working demonstration of [provider independence](../../concepts/provider-independence.md): the harness, not the vendor, owns the workflow.

## Realizes

- [LLM Cost Optimization](../../concepts/llm-cost-optimization.md) - Sending the bulk of cheap-to-serve traffic to far cheaper models and paying premium rates only for the rare hard requests.
- [Model Selection](../../concepts/model-selection.md) - Choosing the right LLM per task by trading off quality, speed, and cost, applied per workflow node rather than per project.
- [The Scout Pattern](../../concepts/the-scout-pattern.md) - Sending a cheap agent ahead to explore and decide what context is worth loading before the expensive model commits.
- [Multi-Model Agents](../../concepts/multi-model-agent.md) - Running a system across more than one LLM so each model's strengths are used where they pay off.

## Contrasts with

- [Claude Opus 4.8](./claude-opus-4-8.md) - The reasoning-heavy premium model reserved for planning and hard implementation, the expensive end of the same per-node tradeoff.
- [Claude Code](./claude-code.md) - The implementation-grade agent Kimi feeds context to rather than replaces in these workflows.
- [MiniMax M2.7](./minimax-m2.md) - A cheap, fast, capable LLM that Cole routes Claude Code to (via environment variables) to drive the entire dark factory economically at high throughput instead of Anthropic models.

## Works with

- [Pi](./pi-coding-agent.md) - The minimalistic, open-source coding agent Cole drives on his Kimi subscription in the loop-engineering dashboard.
- [Archon](./archon.md) - The harness builder where each workflow node picks its own model, which is what makes a cheap exploration model usable.
- [OpenRouter](./openrouter.md) - Unified API gateway to many LLMs, the other common route to reaching models like this without vendor lock-in.

## Related

- [Loop Engineering](../../concepts/loop-engineering.md) - Designing self-prompting loops so agents pick up work autonomously; token hunger is the downside Kimi is deployed against.
- [Meta-Harness](../../concepts/meta-harness.md) - A layer above individual coding assistants that orchestrates many of them, where per-node model choice lives.
- [Provider Independence](../../concepts/provider-independence.md) - Architecting so the underlying model or client can be swapped without a rewrite.
- [Context Isolation](../../concepts/context-isolation.md) - Each workflow node running in its own session, which is what allows a different model per step.
- [Open-Source & Local AI Coding](../../concepts/open-source-ai-coding.md) - Community-maintained and open-weight alternatives that dodge frontier API costs.

## Sources

- [The Creators of Claude Code and OpenClaw don't Prompt Their Agents Anymore?!](../../sources/the-creators-of-claude-code-and-openclaw-dont-prompt-their-agents-anymore.md) - "[0:11:57] For all of our context loading and exploration up front we can use a smaller model like Kimi K 2.7."
- [The Creators of Claude Code and OpenClaw don't Prompt Their Agents Anymore?!](../../sources/the-creators-of-claude-code-and-openclaw-dont-prompt-their-agents-anymore.md) - "[0:19:04] I'm actually using my Kimi subscription with Kimi K 2.7 to drive all of these workflows."
