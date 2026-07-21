---
type: entity
subtype: tool
title: "CodeRabbit"
description: "AI code review tool that automatically and thoroughly reviews every pull request, free for open-source repos, with security vulnerability detection."
resource: "https://coderabbit.ai"
tags: [code-review, ai-review, pull-requests]
videos: [the-only-ai-tech-stack-you-need-in-2026, the-true-power-of-ai-coding-build-your-own-workflows-full-guide]
created: 2026-07-21
updated: 2026-07-21
---

# CodeRabbit

CodeRabbit is the AI-powered code review platform Cole runs over every pull request. He describes it as "an AI powered code review platform... I do use them every single day for my work and it's free for open source projects" [0:19:49]. It slots into the validation stage of his [PIV Loop](../../concepts/the-piv-loop.md): after AI writes and the developer plans, CodeRabbit acts as an automated reviewer catching what a human pass might miss.

## What it is

CodeRabbit reviews code changes automatically and, in Cole's experience, exhaustively. He wires it into [Archon](./archon.md)'s workflow so that "every single pull request that we have coming into Archon gets automatically reviewed by CodeRabbit. And man, is it thorough" [0:31:28]. Its thoroughness extends to flagging security vulnerabilities, making it a checkpoint rather than a rubber stamp. For open-source repositories it is free, which is why he can run it across public projects without friction.

## How Cole uses it

Cole uses CodeRabbit in two modes. The original is the GitHub PR reviewer: it comments on every incoming pull request before a human merges. The newer mode is local. As he notes, "they have a CLI tool now, so you can use CodeRabbit not just to review your PRs in GitHub, but now you can also use it as one of your agents reviewing things locally" [0:20:41]. That turns it into a reviewing agent inside his [agentic workflow engineering](../../concepts/agentic-workflow-engineering.md) setup, giving fast feedback before code ever reaches a PR. CodeRabbit sponsored the workflows video where he demonstrates it, a relationship he discloses, while stressing he uses it daily regardless.

## Related

- [The PIV Loop](../../concepts/the-piv-loop.md) - CodeRabbit is a validation-stage reviewer in Cole's core loop.
- [Agentic Workflow Engineering](../../concepts/agentic-workflow-engineering.md) - where its CLI acts as a local reviewing agent.
- [Context Engineering](../../concepts/context-engineering.md), [PRD-First Development](../../concepts/prd-first-development.md), [Two-Layer Planning](../../concepts/two-layer-planning.md), [Slash Commands](../../concepts/slash-commands.md) - practices its review complements.
- Sibling tools: [Archon](./archon.md) (which routes every PR through it), [Claude Code](./claude-code.md).

## Sources

- [The ONLY AI Tech Stack You Need in 2026](../../sources/the-only-ai-tech-stack-you-need-in-2026.md) - "[0:31:28] for AI code review... I love using CodeRabbit... every single pull request that we have coming into Archon gets automatically reviewed by CodeRabbit. And man, is it thorough."
- [The True Power of AI Coding - Build Your OWN Workflows (Full Guide)](../../sources/the-true-power-of-ai-coding-build-your-own-workflows-full-guide.md) - "[0:20:41] they have a CLI tool now, so you can use CodeRabbit not just to review your PRs in GitHub, but now you can also use it as one of your agents reviewing things locally"
