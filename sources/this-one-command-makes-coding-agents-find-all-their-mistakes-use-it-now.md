---
type: source
title: "This One Command Makes Coding Agents Find All Their Mistakes (Use it Now)"
description: "Packaging a comprehensive, browser-driven end-to-end validation process into a single reusable slash command lets a coding agent test its own work as a real user would, fixing the big blockers and surfacing everything else so far less review burden falls back on you."
youtube_id: YeCHI1dmpZY
url: https://www.youtube.com/watch?v=YeCHI1dmpZY
slug: this-one-command-makes-coding-agents-find-all-their-mistakes-use-it-now
published: 2026-02-25
duration: "0:20:02"
recency_rank: 31
raw: "../raw/this-one-command-makes-coding-agents-find-all-their-mistakes-use-it-now.md"
tags: [validation, end-to-end-testing, agentic-coding, claude-code]
created: 2026-07-21
updated: 2026-07-21
---
# This One Command Makes Coding Agents Find All Their Mistakes (Use it Now)

Cole argues that AI coding assistants generate code faster than humans can review it, yet they are terrible at validating their own work unless given an explicit framework. His answer is a 'self-healing AI coding workflow' packaged as a single Claude Code skill/command (/e2e test) that runs a six-step process on any codebase with a frontend. It auto-installs the Vercel agent browser CLI and drives the app the way a real user would rather than trusting sim-layer tests.

The command runs a prereq check (frontend required, Windows falls back to WSL), then a research phase where three sub-agents run in parallel: one maps the app structure and user journeys, one reads the database schema, and one does a static bug-hunt code review. Their findings are compiled into the primary agent's context. The agent then starts the dev server, builds a task list of user journeys, and loops through each one comprehensively, using the agent browser to navigate the UI, taking screenshots to visually verify, and querying the database (Postgres/Neon) to confirm records were created, updated, or deleted correctly. Critically it only fixes the big blockers that prevent completing a journey; moderate and minor issues are deliberately left for the human to triage, plus a structured final report and an optional markdown export to hand into a fresh context window.

The workflow can be invoked ad hoc or wired directly into feature development as a sub-step of the PIV (plan-implement-validate) loop, so that after an agent writes a feature it immediately runs regression-style end-to-end testing. Cole notes it is token-heavy and slow by design, meant to be comprehensive rather than fast, and that Neon database branching is a handy way to keep end-to-end test data isolated from your real dev database.

## Concepts covered

- [End-to-End Validation](../concepts/end-to-end-validation.md)
- [Validation](../concepts/validation.md)
- [The PIV Loop](../concepts/the-piv-loop.md)
- [Subagents Pattern](../concepts/subagents-pattern.md)
- [Code Review](../concepts/code-review.md)
- [Phases of Work](../concepts/phases-of-work.md)
- [Commandify Everything](../concepts/commandify-everything.md)
- [Skills](../concepts/skills.md)
- [Human in the Loop](../concepts/human-in-the-loop.md)
- [Context Reset](../concepts/context-reset.md)
- [Structured Outputs](../concepts/structured-outputs.md)
- [Vibe Coding](../concepts/vibe-coding.md)

## Entities

- [Vercel Agent Browser CLI](../entities/tools/agent-browser.md)
- [Claude Code](../entities/tools/claude-code.md)
- [Neon](../entities/tools/neon.md)
- [Bright Data](../entities/organizations/bright-data.md)
- [Cole Medin](../entities/people/cole-medin.md)

## Key moments

- **[0:00:00]** Thesis: coding agents are bad at validating their own work without a framework
- **[0:01:47]** Names it the 'self-healing AI coding workflow'
- **[0:03:47]** Two ways to use it: ad hoc full end-to-end testing, or wired into feature dev
- **[0:03:56]** Invoked as /e2e test, kicking off the six-step workflow
- **[0:04:50]** Research phase runs three sub-agents in parallel (structure, DB schema, code review)
- **[0:05:37]** Agent starts dev server and defines a task list of user journeys
- **[0:06:08]** A for-loop knocks out each user journey one at a time
- **[0:07:32]** Fixes only big blockers, retests and loops; leaves moderate/minor issues for the human
- **[0:08:42]** Structured final report: what was fixed, what remains, what it went through
- **[0:09:12]** Hand the report into a NEW context window to avoid bloat
- **[0:15:04]** Neon database branching to keep end-to-end test data isolated
- **[0:16:59]** Wiring the skill into the PIV loop's validation strategy
- **[0:17:32]** Disabling model-invocation on the skill so it's only invoked deliberately
- **[0:18:31]** Warning: token-heavy and slow by design; be comprehensive not fast

## Transcript

[Raw transcript](../raw/this-one-command-makes-coding-agents-find-all-their-mistakes-use-it-now.md)

