---
type: source
title: "FULL Guide to Becoming a Principled Agentic Engineer (Build Anything with AI)"
description: "Reliable, repeatable AI coding comes not from fancy harnesses but from a simple, ownable three-phase foundation: ideate to a structured PRD, run the PIV loop per ticket, and continuously evolve your AI layer whenever the agent makes a mistake."
youtube_id: luBkbzjo-TA
url: https://www.youtube.com/watch?v=luBkbzjo-TA
slug: full-guide-to-becoming-a-principled-agentic-engineer-build-anything-with-ai
published: 2026-04-29
duration: "1:06:59"
recency_rank: 16
raw: "../raw/full-guide-to-becoming-a-principled-agentic-engineer-build-anything-with-ai.md"
tags: [piv-loop, workflow, foundations, system-evolution]
created: 2026-07-21
updated: 2026-07-21
---

# FULL Guide to Becoming a Principled Agentic Engineer (Build Anything with AI)

This is Cole's portion of the AI Transformation Workshop (co-hosted with Lior Weinstein), teaching a foundational system for getting reliable results from AI coding assistants without the bloat of off-the-shelf frameworks like BMAD, GSD, or GitHub Spec Kit. He argues those frameworks are overengineered and hard to mold to a team's existing software development life cycle, whereas a simple foundation lets you bake your own conventions into rules, commands, and skills. The whole process is tool-agnostic (he uses Claude Code + Jira, but Codex + GitHub or Copilot + Linear work identically); all you need is one place to manage work and one place to work with an LLM.

The system has three phases. First, ideation/planning: start unstructured with a brain dump, then have the agent ask clarifying questions one at a time to reduce assumptions, then run a create-PRD command to turn the conversation into a structured document, and a create-stories command to split the PRD into Jira tickets via MCP. This is two-layer planning, project-level (features/bugs, no code) then task-level (dig into the codebase). Second, the PIV loop, repeated per ticket: prime the agent on the codebase (using git history as long-term memory and the Jira issue as the spec), explore unstructured with research sub-agents, run a plan command to produce a plan.md with patterns, files to change, task order, and a self-validation strategy, then start a FRESH session and run an implement command so the agent codes with unbiased focus and validates its own work before human code review.

The third and most powerful phase is system evolution. Because agents are non-deterministic and mistakes are inevitable, you don't just patch the bug, you run a retroactive session asking the agent to identify what in its AI layer (global rules, commands, skills, plan/PRD templates, on-demand context) allowed the bug, and improve it. Checked into source control, these improvements compound across the whole team. There's an inner loop (chug through tickets when things go well) and an outer loop (pause to make the system better), and the commands he shares are deliberately general starting points meant to be customized to your own process.

## Concepts covered

- [The PIV Loop](../concepts/the-piv-loop.md)
- [System Evolution](../concepts/system-evolution.md)
- [Two-Layer Planning](../concepts/two-layer-planning.md)
- [Reduce Assumptions](../concepts/reduce-assumptions.md)
- [Clarifying Questions](../concepts/clarifying-questions.md)
- [PRD-First Development](../concepts/prd-first-development.md)
- [The AI Layer](../concepts/the-ai-layer.md)
- [Global Rules](../concepts/global-rules.md)
- [Commandify Everything](../concepts/commandify-everything.md)
- [Slash Commands](../concepts/slash-commands.md)
- [Skills](../concepts/skills.md)
- [Prime Command](../concepts/prime-command.md)
- [Git as Long-Term Memory](../concepts/git-as-long-term-memory.md)
- [Context Engineering](../concepts/context-engineering.md)
- [Subagents Pattern](../concepts/subagents-pattern.md)
- [Context Isolation](../concepts/context-isolation.md)
- [Context Reset](../concepts/context-reset.md)
- [The Issue Is the Spec](../concepts/issue-is-the-spec.md)
- [Human in the Loop](../concepts/human-in-the-loop.md)
- [Validation](../concepts/validation.md)
- [End-to-End Validation](../concepts/end-to-end-validation.md)
- [Code Review](../concepts/code-review.md)
- [Planning with AI](../concepts/planning-with-ai.md)
- [Vibe Coding](../concepts/vibe-coding.md)
- [Agentic Coding](../concepts/agentic-coding.md)

## Entities

- [Cole Medin](../entities/people/cole-medin.md)
- [Claude Code](../entities/tools/claude-code.md)
- [Jira](../entities/tools/jira.md)
- [MCP (Model Context Protocol)](../entities/tools/mcp.md)
- [GitHub](../entities/tools/github.md)
- [Linear](../entities/tools/linear.md)
- [Codex](../entities/tools/codex.md)
- [Vercel Agent Browser CLI](../entities/tools/agent-browser.md)
- [Lior Weinstein](../entities/people/lior-weinstein.md)
- [Dynamous](../entities/organizations/dynamous.md)

## Key moments

- **[0:00:35]** Boils AI coding into three phases: ideate with agents, build an iterative loop (PIV), evolve agents over time
- **[0:04:47]** Critiques off-the-shelf frameworks (Spec Kit, BMAD, GSD, Cloudflow) as overengineered and hard to mold to your SDLC
- **[0:09:29]** The most important planning move: reduce assumptions by having the agent ask clarifying questions one at a time
- **[0:11:41]** The AI layer: global rules + commands + skills; turn any prompt used 3+ times into a reusable command/skill
- **[0:12:48]** create-PRD command turns unstructured conversation into a structured PRD; create-stories splits it into Jira tickets
- **[0:38:50]** Two-layer planning explained: project-level (features/bugs) vs task-level (dig into the code)
- **[0:41:23]** The prime command loads codebase understanding + Jira issue context + recent git commits as long-term memory
- **[0:46:06]** Spins up research sub-agents to explore the codebase without overwhelming the main agent's context
- **[0:53:40]** Start a FRESH session for implementation so the agent is focused and free of planning bias
- **[0:57:04]** System evolution: fix the system that allowed the bug, not just the bug, improve the AI layer so it can't recur
- **[1:00:58]** Inner loop (chug through tickets) vs outer loop (pause to evolve the system)

## Transcript

[Raw transcript](../raw/full-guide-to-becoming-a-principled-agentic-engineer-build-anything-with-ai.md)
