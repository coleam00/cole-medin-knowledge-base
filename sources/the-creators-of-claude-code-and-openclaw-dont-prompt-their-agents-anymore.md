---
type: source
title: "The Creators of Claude Code and OpenClaw don't Prompt Their Agents Anymore?!"
description: "\"Loop engineering\" is a useful but over-hyped idea best folded into harness engineering: don't let a single looping agent session drive everything, wrap loops in durable, deterministic, cost-controlled harnesses that orchestrate many isolated coding-agent sessions."
youtube_id: UztrFXaSWv0
url: https://www.youtube.com/watch?v=UztrFXaSWv0
slug: the-creators-of-claude-code-and-openclaw-dont-prompt-their-agents-anymore
published: 2026-06-17
duration: "0:24:37"
recency_rank: 8
raw: "../raw/the-creators-of-claude-code-and-openclaw-dont-prompt-their-agents-anymore.md"
tags: [loop-engineering, harness-engineering, archon]
created: 2026-07-21
updated: 2026-07-21
---

Cole responds to Boris Cherny (Claude Code) and Peter Steinberger (OpenClaw) claiming they no longer prompt their agents but instead "write loops" that make agents work autonomously. He demystifies loop engineering as a simple pattern built on Claude Code features: /loop (run a prompt on an interval, e.g. check GitHub issues every 5 min), /goal (work until done-criteria are met, Ralph-style), and /routines (scheduled jobs), all coordinated by a lightweight orchestrator agent you barely prompt. He demonstrates the built-in loop skill letting Claude Code set up and drive its own /loop through a task list.

He then lays out three honest downsides: loops don't produce the best results, they are extremely token-hungry (a simple app cost over a million tokens because the orchestrator must repeatedly reason and dispatch waves of workers), and single-session loops bloat the context window. His fix is harness engineering with Archon: build the plan-implement-review process as an explicit, partly-deterministic workflow where each step runs in its own coding-agent session (no context bloat), you pick a different model per node (small models like Kimi/Haiku for classification/exploration, Claude Code for implementation, Codex for review) to control cost, and state lives durably in a Neon Postgres database so any run can resume after a crash.

He shows Archon dispatching four GitHub-issue-fix workflows in parallel (worktree-isolated so agents don't collide), then four code-review workflows, orchestrated by a primary Claude Code session with human-in-the-loop gates. Finally he shows an open-source loop-engineering dashboard he built for his second brain: an orchestrator reads external DB state, dispatches workers who update state, and the loop repeats, driven entirely by Pi on a Kimi subscription with full cost tracking and observability, deployed via Retool for a governed, shareable, audit-trailed path to production.

## Concepts covered

- [The Ralph Loop](../concepts/the-ralph-loop.md)
- [Heartbeat](../concepts/heartbeat.md)
- [AI Coding Harness](../concepts/ai-coding-harness.md)
- [Agentic Workflow Engineering](../concepts/agentic-workflow-engineering.md)
- [Deterministic Workflows](../concepts/deterministic-workflows.md)
- [Model Selection](../concepts/model-selection.md)
- [Context Rot](../concepts/context-rot.md)
- [Context Isolation](../concepts/context-isolation.md)
- [Parallel Agentic Coding](../concepts/parallel-agentic-coding.md)
- [Human in the Loop](../concepts/human-in-the-loop.md)
- [Git as Long-Term Memory](../concepts/git-as-long-term-memory.md)
- [Second Brain](../concepts/second-brain.md)
- [Provider Independence](../concepts/provider-independence.md)

## Entities

- [Claude Code](../entities/tools/claude-code.md)
- [Archon](../entities/tools/archon.md)
- [Pi](../entities/tools/pi-coding-agent.md)
- [Codex](../entities/tools/codex.md)
- [Neon](../entities/tools/neon.md)
- [Git Worktrees](../entities/tools/git-worktree.md)
- [OpenClaw](../entities/tools/openclaw.md)
- [Boris Cherny](../entities/people/boris-cherny.md)
- [Cole Medin](../entities/people/cole-medin.md)

## Key moments

- **[0:00:00]** Framing: Steinberger and Cherny say they write loops instead of prompting; Cole is skeptical of "loop engineering" as a buzzword
- **[0:02:09]** Loop primitives in Claude Code explained: /loop (interval), /goal (done-criteria), /routines (scheduled)
- **[0:03:42]** Orchestrator-agent idea: minimal prompting, the agent sets up the whole loop via the loop skill
- **[0:05:56]** Three downsides begin: not best results, huge cost (>1M tokens for a simple app), context bloat in single-session loops
- **[0:08:42]** Archon as harness builder: deterministic workflows, plan/implement/review, each step its own session
- **[0:11:43]** Per-node model selection and mixing providers to control cost; Neon Postgres for durable, resumable runs
- **[0:13:29]** Live: Claude Code orchestrator dispatches 4 parallel GitHub-issue-fix workflows, then 4 reviews, worktree-isolated with human-in-the-loop
- **[0:17:38]** Open-source loop-engineering dashboard: external-DB state loop driven by Pi+Kimi, cost tracking, observability, human-in-the-loop
- **[0:21:23]** Retool deploy: import the React dashboard, connect Neon, governed production path with permissions and audit trails
- **[0:24:10]** Conclusion: fold loop engineering into harness engineering; it doesn't deserve its own buzzword

## Transcript

[Raw transcript](../raw/the-creators-of-claude-code-and-openclaw-dont-prompt-their-agents-anymore.md)
