---
type: entity
subtype: tool
title: "Codex"
description: "OpenAI's cloud-based software-engineering agent integrated with GitHub, plus a Codex CLI."
resource: "https://openai.com/index/introducing-codex/"
tags: [coding-agent, openai, cloud-agent, code-review]
videos: [i-turned-claude-code-into-a-complete-video-generation-system-with-archon, pydantic-ai-20-the-new-best-way-to-build-ai-agents-is-composing-capabilities, i-love-the-karpathy-llm-wiki-but-it-doesnt-scale-heres-what-does, the-creators-of-claude-code-and-openclaw-dont-prompt-their-agents-anymore, omnigent-the-new-meta-harness-for-every-coding-agent-claude-code-codex-pi-more, harness-engineering-what-separates-top-agentic-engineers-right-now, full-guide-to-becoming-a-principled-agentic-engineer-build-anything-with-ai, parallel-claude-code-git-worktrees-this-setup-will-change-how-you-ship, pi-coding-agent-archon-build-any-ai-coding-workflow-no-claude-code-bloat, the-next-evolution-of-ai-coding-is-harnesses-heres-how-to-build-them, coding-agent-reliability-explodes-when-they-argue-new-adversarial-dev-technique, everything-you-thought-about-building-ai-agents-is-wrong, the-subagent-era-is-officially-here-learn-this-now, ai-exploded-in-2025-heres-everything-that-happened, i-forced-claude-to-code-for-24-hours-nonstop-heres-what-happened, the-way-we-use-ai-will-completely-change-in-2026-hot-takes, ai-fixes-my-code-better-than-me-now-heres-how, github-is-the-future-of-ai-coding-heres-why, claude-code-web-just-dropped-but-i-already-built-something-better-with-codex, should-i-build-my-ai-agents-with-n8n-or-python, claude-codes-real-purpose-its-bigger-than-you-think, the-official-archon-guide-10x-your-ai-coding-workflow, claude-sonnet-45-the-new-coding-king-sonnet-45-vs-gpt-5-codex]
created: 2026-07-21
updated: 2026-07-21
---

# Codex

[Codex](./codex.md) is OpenAI's cloud-based software-engineering agent, later joined by a Codex CLI and SDK. "OpenAI introduced Codex, their cloud-based software engineering agent that integrates directly with GitHub," Cole recaps, adding "they also released the Codex CLI later. This still is one of my favorite platforms for AI assisted coding." Like [Claude Code](./claude-code.md), it is really an [AI coding harness](../../concepts/ai-coding-harness.md) engineered around a model: "Claude Code, Codex, Pi... all of them are actually harnesses that a company has engineered around their model."

Cole's signature use is adversarial pairing. Because "a lot of people feel like Codex is best at reviewing and Claude is best at implementing," he routes work accordingly: "delegate the implementation to Claude Code and the review to Codex." There is even a Codex plugin for Claude Code exposing a `/codex adversarial review` command. This split makes Codex a workhorse for [context isolation](../../concepts/context-isolation.md) and [agentic workflow engineering](../../concepts/agentic-workflow-engineering.md), letting two providers check each other.

Programmatically he drives it through the Codex SDK: "I'm using the Codex SDK to programmatically invoke Codex in my own environment... we just call thread.runstreamed with our current user prompt. It is that easy." That [provider independence](../../concepts/provider-independence.md) is a theme, harnesses like Archon and his 24-hour experiment can "swap out Claude Code for Codex" without rewriting anything. On [model selection](../../concepts/model-selection.md), Codex runs GPT-5-class models (GPT-5 Codex, GPT-5.4 mini for cheap fast sub-agents), and in one head-to-head it was thorough but slow: the Codex implementation "took 1 hour and 20 minutes in total... while Sonnet 4.5 took 15 minutes." A GitHub action and Codex Web round out the surfaces.

## Realizes

- [AI Coding Harness](../../concepts/ai-coding-harness.md) - The surrounding scaffolding (prompts, tools, rules, validation) that turns a raw model into a reliable coding system.
- [Context Isolation](../../concepts/context-isolation.md) - Giving each agent or subagent its own clean context window so unrelated tokens never dilute the task at hand.
- [Agentic Workflow Engineering](../../concepts/agentic-workflow-engineering.md) - Designing repeatable AI workflows as engineered systems with defined steps, orchestration, and background execution rather than ad-hoc prompting.
- [Provider Independence](../../concepts/provider-independence.md) - Architecting agents so the underlying model, framework, or client can be swapped without a rewrite, avoiding lock-in through low-level abstractions.
- [Model Selection](../../concepts/model-selection.md) - Choosing the right LLM per task by trading off quality, speed, and cost, often routing easy requests to cheap models and hard ones to expensive models.
- [Human in the Loop](../../concepts/human-in-the-loop.md) - Keeping a human as the approver and steerer of agentic work rather than fully automating, so AI augments engineers instead of replacing them.

## Contrasts with

- [Claude Code](./claude-code.md) - Anthropic's terminal-based agentic coding assistant; the harness Codex is paired against, with Claude implementing and Codex reviewing.
- [Pi](./pi-coding-agent.md) - A minimalistic, open-source coding agent cited as another example of a company-built harness around a model.
- [Gemini CLI](./gemini-cli.md) - Google's coding CLI, where subagent support is experimental and which has a direct integration with the Agent Client Protocol.

## Works with

- [GitHub](./github.md) - The gh command-line tool that lets Claude Code manage issues and pull requests directly on a remote GitHub repository.
- [Archon](./archon.md) - Cole's free, open-source AI command center and harness builder for AI coding; started as an AI agent that builds other AI agents.
- [CodeRabbit](./code-rabbit.md) - AI code review tool that automatically and thoroughly reviews every pull request, free for open-source repos, with security vulnerability detection.

## Sources

- [I Turned Claude Code Into a Complete Video Generation System (with Archon)](../../sources/i-turned-claude-code-into-a-complete-video-generation-system-with-archon.md)
- [Pydantic AI 2.0: The New Best Way to Build AI Agents is Composing Capabilities](../../sources/pydantic-ai-20-the-new-best-way-to-build-ai-agents-is-composing-capabilities.md)
- [I Love the Karpathy LLM Wiki but it Doesn't Scale. Here's What Does.](../../sources/i-love-the-karpathy-llm-wiki-but-it-doesnt-scale-heres-what-does.md)
- [The Creators of Claude Code and OpenClaw don't Prompt Their Agents Anymore?!](../../sources/the-creators-of-claude-code-and-openclaw-dont-prompt-their-agents-anymore.md)
- [Omnigent: The New Meta-Harness for EVERY Coding Agent - Claude Code, Codex, Pi, More](../../sources/omnigent-the-new-meta-harness-for-every-coding-agent-claude-code-codex-pi-more.md) - "[0:07:13] a lot of people feel like Codex is best at reviewing and Claude is best at implementing."
- [Harness Engineering: What Separates Top Agentic Engineers Right Now](../../sources/harness-engineering-what-separates-top-agentic-engineers-right-now.md) - "[0:01:56] Claude Code, Codex, Pi, you name the millions of coding agents out there. All of them are actually harnesses that a company has engineered around their model."
- [FULL Guide to Becoming a Principled Agentic Engineer (Build Anything with AI)](../../sources/full-guide-to-becoming-a-principled-agentic-engineer-build-anything-with-ai.md)
- [Parallel Claude Code + Git Worktrees: This Setup Will Change How You Ship](../../sources/parallel-claude-code-git-worktrees-this-setup-will-change-how-you-ship.md)
- [Pi Coding Agent + Archon: Build ANY AI Coding Workflow (No Claude Code Bloat)](../../sources/pi-coding-agent-archon-build-any-ai-coding-workflow-no-claude-code-bloat.md) - "[0:06:28] They got anthropic, github copilot, anti-gravity, Codex. That's the one that I'm using. So my model is GPT 5.3 spark."
- [The Next Evolution of AI Coding Is Harnesses - Here's How to Build Them](../../sources/the-next-evolution-of-ai-coding-is-harnesses-heres-how-to-build-them.md)
- [Coding Agent Reliability EXPLODES When They Argue (New Adversarial Dev Technique)](../../sources/coding-agent-reliability-explodes-when-they-argue-new-adversarial-dev-technique.md) - "[0:02:10] you could even mix these to have Claude be the implementator and Codex be the evaluator."
- [Everything You Thought About Building AI Agents is Wrong](../../sources/everything-you-thought-about-building-ai-agents-is-wrong.md)
- [The Subagent Era Is Officially Here - Learn this Now](../../sources/the-subagent-era-is-officially-here-learn-this-now.md) - "[0:01:54] I'm literally thinking I might want to switch to Codex from Claude Code because of how much I love using subagents."
- [AI Exploded in 2025 - Here's Everything That Happened](../../sources/ai-exploded-in-2025-heres-everything-that-happened.md) - "[0:05:16] OpenAI introduced Codex, their cloud-based software engineering agent that integrates directly with GitHub"
- [I Forced Claude to Code for 24 Hours NONSTOP, Here's What Happened](../../sources/i-forced-claude-to-code-for-24-hours-nonstop-heres-what-happened.md)
- [The Way We Use AI Will Completely Change in 2026 (Hot Takes)](../../sources/the-way-we-use-ai-will-completely-change-in-2026-hot-takes.md)
- [AI Fixes My Code Better than Me Now?! (Here's How)](../../sources/ai-fixes-my-code-better-than-me-now-heres-how.md)
- [GitHub is the Future of AI Coding (Here's Why)](../../sources/github-is-the-future-of-ai-coding-heres-why.md)
- [Claude Code Web JUST Dropped but I Already Built Something BETTER (with Codex!)](../../sources/claude-code-web-just-dropped-but-i-already-built-something-better-with-codex.md) - "[0:10:14] I'm using the Codex SDK to programmatically invoke Codex in my own environment"
- [Should I Build My AI Agents with n8n or Python?](../../sources/should-i-build-my-ai-agents-with-n8n-or-python.md)
- [Claude Code's Real Purpose (It's Bigger Than You Think)](../../sources/claude-codes-real-purpose-its-bigger-than-you-think.md)
- [The OFFICIAL Archon Guide - 10x Your AI Coding Workflow](../../sources/the-official-archon-guide-10x-your-ai-coding-workflow.md)
- [Claude Sonnet 4.5 - The New Coding King? (Sonnet 4.5 vs. GPT 5 Codex)](../../sources/claude-sonnet-45-the-new-coding-king-sonnet-45-vs-gpt-5-codex.md) - "[0:01:47] On the left side, I've got Codex running with GPT-5 Codex for the LLM"
