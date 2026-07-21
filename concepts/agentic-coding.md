---
type: concept
title: "Agentic Coding"
description: "Letting an AI agent drive software development end-to-end, from planning through implementation and validation, with human steering."
tags: [coding, agents, development, agentic-coding, workflow]
videos: [this-completely-changes-the-way-we-build-production-ai-agents-vercel-eve, google-just-dropped-a-masterclass-on-agentic-engineering-its-so-good, googles-agents-cli-the-cli-skills-combination-to-ship-ai-agents-easily, full-guide-to-becoming-a-principled-agentic-engineer-build-anything-with-ai, my-complete-agentic-coding-workflow-to-build-anything-no-fluff-or-overengineering, the-kiro-ai-coding-hackathon-has-officially-started-build-anything-win-big-prizes, ai-exploded-in-2025-heres-everything-that-happened, i-forced-claude-to-code-for-24-hours-nonstop-heres-what-happened, github-is-the-future-of-ai-coding-heres-why, claude-code-web-just-dropped-but-i-already-built-something-better-with-codex, claude-codes-real-purpose-its-bigger-than-you-think, the-official-archon-guide-10x-your-ai-coding-workflow, claude-sonnet-45-the-new-coding-king-sonnet-45-vs-gpt-5-codex, archon-beta-launch-livestream-what-you-missed, build-any-ai-agent-with-this-context-engineering-blueprint, introducing-rag-20-agentic-rag-knowledge-graphs-free-template, how-id-learn-ai-agents-fast-if-i-had-to-start-over-full-roadmap, this-mcp-server-for-ai-coding-assistants-will-10x-your-productivity, are-you-building-real-ai-agents-or-just-using-llms, pydantic-ai-deepseek-v3-the-best-ai-agent-combo, code-100x-faster-with-ai-heres-how-no-hype-full-process]
created: 2026-07-21
updated: 2026-07-21
---

# Agentic Coding

Agentic coding is the practice of delegating the actual writing of software to an AI coding agent while the human moves up the stack to steering, planning, and validating. As Cole puts it, "Our job as an engineer is to no longer write the code, but to do the higher leverage tasks like the planning and validating." The mandate is to hand off as much as possible: "it is important for us to delegate as much coding to the coding agent as we possibly can. That's the backstage work for developers now." Taken to its limit, an entire build can happen without a human touching the keyboard: "we took our agent from idea all the way to production in this video without me running a single command myself. Claude code drove the entire thing."

Crucially, agentic coding is not a dial between "how much I write by hand" and "how much I trust the agent." Cole reframes it as a maturity axis: "this is not a spectrum of how much do we write by hand versus trust the agent. It is just a spectrum of how evolved of a system do we actually have here." The point of the delegation is not laziness but leverage. Anthropic itself writes roughly 70% of its code with AI, and the skill that separates practitioners is process, not typing.

What makes an agent "agentic" is that it decides its own steps. Watching a tool work, "you have no idea what it's going to decide to analyze what files it's going to decide to edit." That autonomy is why a well-defined process matters: "you have to have a well-defined process when using AI to code if you want high-quality outputs and you want them consistently." The trend Cole tracks points toward remote, containerized agents that never touch your local machine, "completely remote agentic coding" triggered from a GitHub issue.

## Builds on

- [Context Engineering](./context-engineering.md) - curating the ecosystem of context that makes agentic coding reliable.
- [Planning with AI](./planning-with-ai.md) and [PRD-First Development](./prd-first-development.md) - the higher-leverage work the engineer keeps.

## Contrasts with

- [Vibe Coding](./vibe-coding.md) - unstructured prompting; agentic coding replaces it with an engineered process.
- [Agents vs. Workflows](./agents-vs-workflows.md) - how much decision-making to hand the agent versus fix in code.

## Related

- [AI Coding Harness](./ai-coding-harness.md) - the engineered system that makes delegation dependable.
- [Global Rules](./global-rules.md) and [Skills](./skills.md) - persistent context and capabilities the agent loads.
- [System Evolution](./system-evolution.md) - agentic coding matures as the surrounding system gets more evolved.
- [MCP](./mcp.md) - how agents reach documentation and external tools.
- [Human in the Loop](./human-in-the-loop.md) - the steering the engineer still provides.
- [Model Selection](./model-selection.md) - which model drives the implementation.

## Tools

- [Claude Code](../entities/tools/claude-code.md) - Cole's primary driver for end-to-end agentic builds.
- [Archon](../entities/tools/archon.md) - the operating system layer that adds RAG and task management.
- [Codex](../entities/tools/codex.md), [Cursor](../entities/tools/cursor.md), [Windsurf](../entities/tools/windsurf.md), [Kiro](../entities/tools/kiro.md) - other coding assistants that drive the same loop.
- [GitHub](../entities/tools/github.md) - the orchestration layer where remote agents are triggered from issues.
- [Pi](../entities/tools/pi-coding-agent.md) - a lightweight, provider-independent coding agent.

## Sources

- [FULL Guide to Becoming a Principled Agentic Engineer](../sources/full-guide-to-becoming-a-principled-agentic-engineer-build-anything-with-ai.md) - "[0:01:06] Our job as an engineer is to no longer write the code, but to do the higher leverage tasks like the planning and validating."
- [Google Just Dropped a Masterclass on Agentic Engineering (It's SO Good)](../sources/google-just-dropped-a-masterclass-on-agentic-engineering-its-so-good.md) - "[0:11:43] Even with agentic engineering, you are delegating all of the coding... It is just a spectrum of how evolved of a system do we actually have here."
- [Google's Agents CLI: The CLI + Skills Combination to Ship AI Agents EASILY](../sources/googles-agents-cli-the-cli-skills-combination-to-ship-ai-agents-easily.md) - "[0:14:30] we took our agent from idea all the way to production in this video without me running a single command myself. Claude code drove the entire thing."
- [My COMPLETE Agentic Coding Workflow to Build Anything](../sources/my-complete-agentic-coding-workflow-to-build-anything-no-fluff-or-overengineering.md) - "[0:03:28] That's why I recommend something like this over a more complex framework like BMAD or the GitHub spec kit... it's hard to really make it your own."
- [Code 100x Faster with AI, Here's How](../sources/code-100x-faster-with-ai-heres-how-no-hype-full-process.md) - "[0:00:34] you have to have a well-defined process when using AI to code if you want high-quality outputs and you want them consistently."
- [Are You Building REAL AI Agents or Just Using LLMs?](../sources/are-you-building-real-ai-agents-or-just-using-llms.md) - "[0:17:39] it's very agentic here because you have no idea what it's going to decide to analyze what files it's going to decide to edit."
- [How I'd Learn AI Agents FAST if I Had to Start Over](../sources/how-id-learn-ai-agents-fast-if-i-had-to-start-over-full-roadmap.md) - "[0:07:35] Even anthropic the company that built claude 70% of the code that's written for their company is written by AI now."
- [Claude Code Web JUST Dropped but I Already Built Something BETTER (with Codex!)](../sources/claude-code-web-just-dropped-but-i-already-built-something-better-with-codex.md) - "[0:00:00] I can send off any request to my AI coding assistant on any GitHub repository and it just goes to town completely remote agentic coding."
- [GitHub is the Future of AI Coding (Here's Why)](../sources/github-is-the-future-of-ai-coding-heres-why.md) - "[0:03:08] I can do @claude-fix... it's going to analyze the issue and then start digging into the codebase, doing a root cause analysis, and then implementing a fix."
- [Claude Code's Real Purpose (It's Bigger Than You Think)](../sources/claude-codes-real-purpose-its-bigger-than-you-think.md) - "[0:21:04] we use it to programmatically define our own custom agents to build them into our code bases, our workflows to really suit our needs the best."
- [I Forced Claude to Code for 24 Hours NONSTOP](../sources/i-forced-claude-to-code-for-24-hours-nonstop-heres-what-happened.md) - "[0:23:58] It still is really cool how much I was able to build here without laying a finger on anything."
- [Introducing RAG 2.0: Agentic RAG + Knowledge Graphs](../sources/introducing-rag-20-agentic-rag-knowledge-graphs-free-template.md) - "[0:30:11] It's this whole agentic process where it can literally run for 30 minutes to an hour just building everything for you."
- [This Completely Changes the Way We Build Production AI Agents (Vercel Eve)](../sources/this-completely-changes-the-way-we-build-production-ai-agents-vercel-eve.md) - "[0:00:47] your entire AI agent is just a collection of files in a single folder... That's what makes it so easy to build, making everything composable."
- [Claude Sonnet 4.5 - The New Coding King?](../sources/claude-sonnet-45-the-new-coding-king-sonnet-45-vs-gpt-5-codex.md) - "[0:04:53] Claude sonnet 4.5 on the other hand has been blazing through this implementation... what matters the most is code quality, but speed is nice as well."
- [Archon Beta Launch Livestream - What You Missed!](../sources/archon-beta-launch-livestream-what-you-missed.md) - "[0:11:30] brownfield projects, it's more let's reference the existing codebase to figure out the patterns... With a new project, it's let's look at the documentation."
- [Pydantic AI + DeepSeek V3 - The BEST AI Agent Combo](../sources/pydantic-ai-deepseek-v3-the-best-ai-agent-combo.md) - "[0:16:08] all the code that I'm about to show you here I did not make myself I used wind surf to do it."
- [The Kiro AI Coding Hackathon has Officially Started!](../sources/the-kiro-ai-coding-hackathon-has-officially-started-build-anything-win-big-prizes.md) - "[0:04:33] We want to see not just your finished project, but your actual AI coding process as you are working with Kira."
- [AI Exploded in 2025 - Here's Everything That Happened](../sources/ai-exploded-in-2025-heres-everything-that-happened.md) - "[0:11:39] Being able to work on your repositories with agents running remotely... I definitely think this is the future of Agentic Coding."
- [Build ANY AI Agent with this Context Engineering Blueprint](../sources/build-any-ai-agent-with-this-context-engineering-blueprint.md) - "[0:11:01] Agents generally consist of three parts... dependencies... our agent definition itself... And then last but not least, our agents always have tools."
- [This MCP Server for AI Coding Assistants Will 10x Your Productivity](../sources/this-mcp-server-for-ai-coding-assistants-will-10x-your-productivity.md) - "[0:06:36] our agent can actually reason about how many tokens it thinks it has to fetch from the documentation."
- [The OFFICIAL Archon Guide - 10x Your AI Coding Workflow](../sources/the-official-archon-guide-10x-your-ai-coding-workflow.md) - "[0:01:53] In our tools that we have like Kirao or Cloud Code or Codeex, all these coding assistants, they have the ability to search the web."
