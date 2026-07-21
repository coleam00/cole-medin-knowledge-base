---
type: source
title: "The True Power of AI Coding - Build Your OWN Workflows (Full Guide)"
description: "Rather than adopting an off-the-shelf framework like PRP or BMAD, you should understand the plan-implement-validate philosophy behind them all and build your own reusable AI coding workflow out of global rules, slash commands, and sub-agents."
youtube_id: mHBk8Z7Exag
url: https://www.youtube.com/watch?v=mHBk8Z7Exag
slug: the-true-power-of-ai-coding-build-your-own-workflows-full-guide
published: 2025-09-24
duration: "0:26:04"
recency_rank: 68
raw: "../raw/the-true-power-of-ai-coding-build-your-own-workflows-full-guide.md"
tags: [workflow, piv-loop, planning, slash-commands, subagents]
created: 2026-07-21
updated: 2026-07-21
---

Cole argues that effective AI coding is not about prompts but about building evolvable systems and workflows. Instead of getting lost in the proliferation of context-engineering frameworks (PRP, BMAD, GitHub Spec Kit), he scraps them and rebuilds from first principles around one core mental model: plan, then implement, then validate (the PIV loop). Understanding that philosophy lets you use existing frameworks better, tweak them, and author your own.

Planning is the most important phase. It starts with unstructured "vibe planning," free-form exploration of ideas, architecture, and tech stack with the assistant as a research companion, then hardens into an "initial MD" (a high-level PRD you could hand to a human), which a second, fresh conversation turns into a full context-engineered plan via a create-plan slash command that leans on RAG, a codebase-analyst sub-agent, and Archon. Implementation is driven by an execute-plan slash command centered on granular task management (Cole uses Archon), knocking out one focused task at a time to avoid hallucinations. Crucially, sub-agents are used for planning and validation but NOT for implementation, because implementation must stay in one shared context window or parallel agents produce conflicting, overlapping changes.

Validation combines a specialized validator sub-agent (isolated context, writes tests), an AI code-review platform (CodeRabbit), and human-in-the-loop review plus manual tests, because skipping human review is just reverting to vibe coding. Global rules (CLAUDE.md) hold the golden instructions that apply no matter the task. The payoff: the primer, planning commands, sub-agents, and task-management workflow are not specific to the demo (an Obsidian OpenAI-compatible agent endpoint), they compose into a reusable system for building anything.

## Concepts covered

- [The PIV Loop](../concepts/the-piv-loop.md)
- [Agentic Workflow Engineering](../concepts/agentic-workflow-engineering.md)
- [Context Engineering](../concepts/context-engineering.md)
- [PRD-First Development](../concepts/prd-first-development.md)
- [Two-Layer Planning](../concepts/two-layer-planning.md)
- [Slash Commands](../concepts/slash-commands.md)
- [Commandify Everything](../concepts/commandify-everything.md)
- [Prime Command](../concepts/prime-command.md)
- [Subagents Pattern](../concepts/subagents-pattern.md)
- [Context Isolation](../concepts/context-isolation.md)
- [Planning with AI](../concepts/planning-with-ai.md)
- [Context Reset](../concepts/context-reset.md)
- [Validation](../concepts/validation.md)
- [Code Review](../concepts/code-review.md)
- [Separate Reviewer](../concepts/separate-reviewer.md)
- [Human in the Loop](../concepts/human-in-the-loop.md)
- [Global Rules](../concepts/global-rules.md)
- [Vibe Coding](../concepts/vibe-coding.md)
- [Retrieval-Augmented Generation (RAG)](../concepts/rag.md)

## Entities

- [Claude Code](../entities/tools/claude-code.md)
- [Archon](../entities/tools/archon.md)
- [Obsidian](../entities/tools/obsidian.md)
- [CodeRabbit](../entities/tools/code-rabbit.md)
- [GitHub](../entities/tools/github.md)
- [Docker](../entities/tools/docker.md)
- [Cole Medin](../entities/people/cole-medin.md)

## Key moments

- **[0:00:00]** Thesis: AI coding is about systems and evolvable workflows, not just prompts
- **[0:00:33]** Scrap existing frameworks (PRP, BMAD, Spec Kit) and build your own by understanding their philosophy
- **[0:01:18]** Core mental model introduced: plan, implement, validate
- **[0:01:33]** Planning is multi-step: vibe planning to initial requirements to context prep
- **[0:03:09]** Live demo context: Obsidian second brain + custom Dockerized agent (the thing being built)
- **[0:05:04]** Vibe planning explained: unstructured, free-form exploration with the assistant as research companion
- **[0:06:26]** Create the initial MD (a high-level PRD) from the vibe-planning conversation
- **[0:07:34]** Turn the initial MD into a full context-engineered plan (this is what PRP does)
- **[0:10:14]** Live: start a fresh Claude Code conversation and run a primer slash command
- **[0:13:17]** Fresh conversation + create-plan slash command with codebase-analyst sub-agent
- **[0:16:12]** Implementation: task management is the most important thing; one granular task at a time
- **[0:19:32]** CodeRabbit sponsor segment: AI code review integrated with Archon PRs, now with a CLI
- **[0:22:46]** Key distinction: use sub-agents for planning and validation, never for implementation
- **[0:24:36]** Manual test: the built Obsidian agent summarizes the workflow diagram via the OpenAI-compatible endpoint
- **[0:25:06]** Payoff: the whole workflow is reusable for anything, not specific to this build

## Transcript

[Raw transcript](../raw/the-true-power-of-ai-coding-build-your-own-workflows-full-guide.md)
