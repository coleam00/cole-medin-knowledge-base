---
type: source
title: "Claude Sonnet 4.5 - The New Coding King? (Sonnet 4.5 vs. GPT 5 Codex)"
description: "Claude Sonnet 4.5 (in Claude Code 2.0) beats GPT-5 Codex on a live, identical real-world coding task, finishing a Stripe integration in 15 minutes versus Codex's 1h20m with better code quality."
youtube_id: P-0fm8ljl0I
url: https://www.youtube.com/watch?v=P-0fm8ljl0I
slug: claude-sonnet-45-the-new-coding-king-sonnet-45-vs-gpt-5-codex
published: 2025-09-29
duration: "0:11:15"
recency_rank: 67
raw: "../raw/claude-sonnet-45-the-new-coding-king-sonnet-45-vs-gpt-5-codex.md"
tags: [model-selection, claude-code, codex, benchmarks]
created: 2026-07-21
updated: 2026-07-21
---

Cole reacts to Anthropic's release of Claude Sonnet 4.5, which tops the coding and agentic-tool-use benchmarks (beating Opus 4.1 and reportedly GPT-5 Codex) and ships alongside Claude Code 2.0, a new VS Code extension, and the renamed Claude Agents SDK. He stresses that benchmarks do not tell the whole story, so he runs a live, un-rehearsed head-to-head: Codex on GPT-5 Codex versus Claude Code on Sonnet 4.5, both executing the identical PRP-style requirements document to add a Stripe token-purchase integration to an existing agentic RAG chat app.

Both agents work on isolated Git branches so they do not collide, starting from a pre-Stripe version of the codebase, with task lists tracked in Archon. Sonnet 4.5 blazes through, finishing the whole implementation in 15 minutes (versus 35 minutes for the same build on Opus 4.1 previously) with only minor front-end and back-end URL fixes and a token-count refresh bug. Codex is far slower and flakier, failing commands and re-reading files after edits, taking 1 hour 20 minutes, and its result had three or four issues (UI polish, transaction history, stale balance) though it was still a solid implementation.

Cole's verdict: Sonnet 4.5 was faster by a lot and better by a decent amount, but Codex is close and will likely catch up quickly. He picked this task deliberately because it is non-trivial but not a two-hour build, the sweet spot where models make visible mistakes without the app crashing outright, making it a good real-world discriminator beyond leaderboard numbers.

## Concepts covered

- [Model Selection](../concepts/model-selection.md)
- [Agentic Coding](../concepts/agentic-coding.md)
- [PRD-First Development](../concepts/prd-first-development.md)
- [End-to-End Validation](../concepts/end-to-end-validation.md)
- [AI Coding Harness](../concepts/ai-coding-harness.md)

## Entities

- [Claude Code](../entities/tools/claude-code.md)
- [Codex](../entities/tools/codex.md)
- [Anthropic](../entities/organizations/anthropic.md)
- [OpenAI](../entities/organizations/openai.md)
- [Claude Agent SDK](../entities/tools/claude-agent-sdk.md)
- [Archon](../entities/tools/archon.md)
- [Stripe](../entities/organizations/stripe.md)
- [Dynamous](../entities/organizations/dynamous.md)
- [Cole Medin](../entities/people/cole-medin.md)

## Key moments

- **[0:00:00]** Sonnet 4.5 released, tops coding benchmarks, beating Opus 4.1 and reportedly GPT-5 Codex
- **[0:00:38]** Sonnet 4.5 leads agentic tool use; ~20% jump in computer use vs Opus 4.1
- **[0:00:56]** Claude Code 2.0 ships with VS Code extension and the renamed Claude Agents SDK
- **[0:01:47]** Live head-to-head begins: Codex/GPT-5 Codex vs Claude Code/Sonnet 4.5 on identical Stripe integration
- **[0:04:05]** PRP requirements-doc workflow: load feature requirement, plan, break into tasks, execute task by task
- **[0:04:38]** Mid-build: Codex slow and failing commands; Sonnet 4.5 blazing through
- **[0:05:41]** Sonnet 4.5 finishes in 15 min (vs 35 min on Opus 4.1); minor URL fixes needed
- **[0:08:06]** Codex finally finishes at 1h20m, several issues but still solid
- **[0:10:26]** Verdict: Sonnet 4.5 faster by a lot and better by a decent amount; Codex will catch up

## Transcript

[Raw transcript](../raw/claude-sonnet-45-the-new-coding-king-sonnet-45-vs-gpt-5-codex.md)
