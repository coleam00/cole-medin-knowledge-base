---
type: source
title: "My COMPLETE Agentic Coding Workflow to Build Anything (No Fluff or Overengineering)"
description: "A dead-simple, evolvable greenfield workflow beats overengineered multi-agent frameworks: build an AI layer (PRD + rules + commands), split the PRD into phases, and knock each out with a plan-implement-validate loop while obeying four golden rules (protect context, commandify everything, git as memory, system evolution)."
youtube_id: goOZSXmrYQ4
url: https://www.youtube.com/watch?v=goOZSXmrYQ4
slug: my-complete-agentic-coding-workflow-to-build-anything-no-fluff-or-overengineering
published: 2026-02-23
duration: "0:42:27"
recency_rank: 32
raw: "../raw/my-complete-agentic-coding-workflow-to-build-anything-no-fluff-or-overengineering.md"
tags: [agentic-coding, workflow, piv-loop, planning]
created: 2026-07-21
updated: 2026-07-21
---
# My COMPLETE Agentic Coding Workflow to Build Anything (No Fluff or Overengineering)

Cole walks through the exact framework he uses to start every new (greenfield) project with a coding agent, arguing against complex frameworks like BMAD or GitHub spec kit in favor of something simple enough to make your own and evolve over time. He does a live build of a self-hosted Linktree-style app to make it concrete. The workflow starts with the 'AI layer' - all the assets you create as context for the agent: a PRD (the full scope of the MVP), global rules (how to build), reusable commands, and subagents for research. He begins with an unstructured voice brain dump, tells the agent to spin up research subagents and then ask a flurry of clarifying questions, because the number one planning goal is to reduce the agent's assumptions (one bad line in a PRD becomes a thousand bad lines of code).

Once aligned, he runs a /create-PRD command to produce a structured spec containing MVP scope, out-of-scope, directory structure, and phases of work. Rules go in a global AGENTS.md file (concise, always loaded) with heavier reference docs pulled in on demand via progressive disclosure. At the start of every session he runs a /prime command so the agent explores the codebase, reads the git log (long-term memory), and outputs its understanding for validation. Then each phase runs through a PIV (plan, implement, validate) loop: two-layer planning (project-level PRD/rules, then focused task-level plan via /plan-feature), a hard context reset so a fresh window gets only the plan, delegated implementation, and a validation pyramid (typecheck, lint, unit, integration, and detailed end-to-end browser testing via the Vercel agent-browser CLI) plus his own human code review and manual test.

He closes on regression testing (roll your own test harness or use QA Tech's self-evolving AI testing agents) and the system-evolution mindset: when you hit a bug or misalignment, don't just fix the code - fix the AI layer (rules, on-demand context, commands, tests) so it never happens again. That way you evolve your codebase, test base, and AI layer in parallel, and the reliability compounds over time.

## Concepts covered

- [The AI Layer](../concepts/the-ai-layer.md)
- [PRD-First Development](../concepts/prd-first-development.md)
- [Reduce Assumptions](../concepts/reduce-assumptions.md)
- [Clarifying Questions](../concepts/clarifying-questions.md)
- [Context Isolation](../concepts/context-isolation.md)
- [Subagents Pattern](../concepts/subagents-pattern.md)
- [Commandify Everything](../concepts/commandify-everything.md)
- [Global Rules](../concepts/global-rules.md)
- [Progressive Disclosure](../concepts/progressive-disclosure.md)
- [Prime Command](../concepts/prime-command.md)
- [Git as Long-Term Memory](../concepts/git-as-long-term-memory.md)
- [The PIV Loop](../concepts/the-piv-loop.md)
- [Phases of Work](../concepts/phases-of-work.md)
- [Two-Layer Planning](../concepts/two-layer-planning.md)
- [Context Reset](../concepts/context-reset.md)
- [End-to-End Validation](../concepts/end-to-end-validation.md)
- [Human in the Loop](../concepts/human-in-the-loop.md)
- [System Evolution](../concepts/system-evolution.md)
- [Context Engineering](../concepts/context-engineering.md)
- [Agentic Coding](../concepts/agentic-coding.md)

## Entities

- [Cole Medin](../entities/people/cole-medin.md)
- [Claude Code](../entities/tools/claude-code.md)
- [Neon](../entities/tools/neon.md)
- [Vercel Agent Browser CLI](../entities/tools/agent-browser.md)
- [QA Tech](../entities/tools/qa-tech.md)
- [GitHub](../entities/tools/github.md)
- [Vercel](../entities/organizations/vercel.md)
- [Dynamous](../entities/organizations/dynamous.md)

## Key moments

- **[0:02:29]** Defines the AI layer: PRD, global rules, commands, subagents as context for the coding agent
- **[0:06:04]** Live voice brain dump of the Linktree-style app idea, asking Claude to spin up research subagents
- **[0:07:29]** The number-one planning goal: reduce the agent's assumptions; one bad PRD line = thousands of bad code lines
- **[0:08:47]** Subagents for research give context isolation - they burn huge tokens exploring, return only findings
- **[0:12:44]** Golden rule: commandify everything; runs /create-PRD to output a structured spec
- **[0:15:41]** Sets up global rules in AGENTS.md plus a reference folder for on-demand progressive-disclosure context
- **[0:20:37]** The /prime command catches a fresh session up on the codebase, using git log as long-term memory
- **[0:23:12]** Introduces the PIV loop (plan, implement, validate) run over each phase
- **[0:23:49]** Two-layer planning: project-level (PRD/rules) then task-level structured plan
- **[0:26:29]** Context reset between planning and implementation so the plan is the only context sent in
- **[0:29:01]** Validation pyramid + Vercel agent-browser CLI for detailed end-to-end testing
- **[0:34:59]** Regression testing / test harness; QA Tech's self-evolving AI testing agents
- **[0:38:37]** System evolution mindset: fix the AI layer on every bug so it never recurs; codebase, test base, AI layer evolve in parallel

## Transcript

[Raw transcript](../raw/my-complete-agentic-coding-workflow-to-build-anything-no-fluff-or-overengineering.md)

