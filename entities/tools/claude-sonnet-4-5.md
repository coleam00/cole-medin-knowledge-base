---
type: entity
subtype: tool
title: "Claude Sonnet 4.5"
description: "Anthropic's coding-focused model release that topped the coding and agentic-tool-use benchmarks over Opus 4.1 and shipped as the default model in Claude Code 2.0."
tags: [llm, model, anthropic]
videos: [claude-sonnet-45-the-new-coding-king-sonnet-45-vs-gpt-5-codex]
created: 2026-07-21
updated: 2026-07-21
---

# Claude Sonnet 4.5

Claude Sonnet 4.5 is Anthropic's coding-focused model release that arrived at the top of the coding and agentic-tool-use leaderboards and shipped as the default model inside Claude Code 2.0. Cole's opening line is the whole framing: "I know that benchmarks don't tell us the entire story, but right now Sonnet 4.5 is at the top of the charts, even beating out previous anthropic models like Opus 4.1" [0:00:00]. The notable part is not just the raw coding score but the roughly 20 percent jump in agentic tool use and computer use over Opus 4.1, which is what actually decides whether a model can drive a long [agentic coding](../../concepts/agentic-coding.md) run without derailing.

Because he distrusts leaderboards, Cole runs the model through a [real-world coding benchmark](../../concepts/coding-benchmarks.md) instead: "I want to see how Sonnet 4.5 compares to GPT5 codecs when working on a new feature in an existing complex codebase" [0:01:31]. Both agents get the identical PRP-style requirements document (a [PRD-first](../../concepts/prd-first-development.md) contract), work on isolated Git branches off the same pre-Stripe codebase, and track their task lists in [Archon](./archon.md). Sonnet 4.5 finishes the Stripe token-purchase integration in 15 minutes versus 35 minutes for the same build on Opus 4.1, leaving only minor URL fixes and a stale token-count bug. Codex takes 1 hour 20 minutes and ships three or four rough edges.

His verdict is measured rather than triumphal: "overall, I would say that Claude Sonnet 4.5 was faster by a lot and better by a decent amount. Codeex is still really solid" [0:10:26]. He picked a task in the sweet spot, non-trivial but not a two-hour build, where models make visible mistakes without the app collapsing, which is what makes the comparison a discriminator instead of a coin flip.

## Realizes

- [Model Selection](../../concepts/model-selection.md) - Choosing the right LLM per task by trading off quality, speed, and cost, often routing easy requests to cheap models and hard ones to expensive models.
- [Real-World Coding Benchmarks](../../concepts/coding-benchmarks.md) - Evaluating coding models on real engineering tasks, and the gap between exploding benchmark scores and flat developer productivity.
- [Agentic Coding](../../concepts/agentic-coding.md) - Letting an AI agent drive software development end-to-end, from planning through implementation and validation, with human steering.

## Contrasts with

- [GPT-5 Codex](./gpt-5-codex.md) - OpenAI's coding-specialized GPT-5 model, the head-to-head opponent on the identical Stripe integration task.
- [Codex](./codex.md) - OpenAI's cloud-based software-engineering agent integrated with GitHub, plus a Codex CLI; slower and flakier in this run but still solid.
- [Claude Opus 4.8](./claude-opus-4-8.md) - The later reasoning-heavy Claude model used for planning and integrations, where Sonnet is the speed-first coding driver.

## Works with

- [Claude Code](./claude-code.md) - Anthropic's terminal-based agentic coding assistant; version 2.0 shipped with Sonnet 4.5 as its default model.
- [Claude Agent SDK](./claude-agent-sdk.md) - The engine that powers Claude Code, exposed as a library so you can build custom agents on the same harness.
- [Archon](./archon.md) - Cole's free, open-source AI command center and harness builder, used here to track both agents' task lists.

## Related

- [Claude](./claude.md) - The model family Sonnet 4.5 belongs to.
- [Claude 3.5 Sonnet](./claude-3-5-sonnet.md) - The earlier Sonnet generation and the first Claude model Cole could not break on multi-step tool use.
- [AI Coding Harness](../../concepts/ai-coding-harness.md) - The surrounding scaffolding (prompts, tools, rules, validation) that turns a raw model into a reliable coding system.
- [End-to-End Validation](../../concepts/end-to-end-validation.md) - Validating the whole system through its real interface so the agent proves the feature actually works.

## Sources

- [Claude Sonnet 4.5 - The New Coding King? (Sonnet 4.5 vs. GPT 5 Codex)](../../sources/claude-sonnet-45-the-new-coding-king-sonnet-45-vs-gpt-5-codex.md) - "[0:00:00] I know that benchmarks don't tell us the entire story, but right now Sonnet 4.5 is at the top of the charts, even beating out previous anthropic models like Opus 4.1"
