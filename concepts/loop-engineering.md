---
type: concept
title: "Loop Engineering"
description: "Designing self-prompting loops (/loop, /goal, /routines) so coding agents pick up and run work autonomously instead of you prompting them each time - a buzzword Cole argues should fold into harness engineering."
tags: [loops, autonomy, orchestration]
videos: [the-creators-of-claude-code-and-openclaw-dont-prompt-their-agents-anymore]
created: 2026-07-21
updated: 2026-07-21
---

# Loop Engineering

Loop engineering is the practice of writing the loop that prompts your agent rather than prompting the agent yourself. The claim that named it came from the creators of Claude Code and OpenClaw: "He said, \"I don't prompt Claude anymore. I write loops and the loops do the work. My job is to write loops.\"" [0:01:40] Framed as a skill, "the real skill is designing loops that prompt your agents so they work for you 24/7." [0:00:00]

Mechanically it is thinner than the buzzword suggests. Claude Code already ships the primitives: `/loop` runs a prompt on an interval (check GitHub issues every five minutes), `/goal` keeps working until stated done-criteria are met (a Ralph-style exit gate), and `/routines` schedules jobs. A lightweight orchestrator agent wires them together, and the agent can even set up its own loop through the loop skill, so the human input collapses to a few sentences.

Cole's honest accounting names three costs. Loops do not produce the best results, because a self-driving session optimizes for continuing rather than for quality. They are extremely token-hungry: a simple app ran past a million tokens because the orchestrator repeatedly reasons and dispatches waves of workers. And a single-session loop bloats its own context window until quality decays.

His fix is to make the loop an explicit, partly deterministic workflow instead of one agent talking to itself. Plan, implement, and review each become a node running in its own coding-agent session, so no context accumulates. Each node picks its own model (small, cheap models for classification and exploration, a strong model for implementation, a different one for review) to control cost. State lives in a durable Postgres database, so a crashed run resumes rather than restarts, and worktree isolation lets several loops run in parallel with human approval gates between waves. That is why the verdict is deflationary: "Really, I would just fold loop engineering into harness engineering. It doesn't quite deserve its own buzzword." [0:24:23]

## Part of

- [AI Coding Harness](./ai-coding-harness.md) - the parent craft loop engineering collapses into.
- [Agentic Workflow Engineering](./agentic-workflow-engineering.md) - designing the nodes, gates, and exit conditions of the loop.

## Builds on

- [The Ralph Loop](./the-ralph-loop.md) - the original run-it-again pattern loop engineering generalizes.
- [Slash Commands](./slash-commands.md) - `/loop`, `/goal`, and `/routines` as the packaged primitives.

## Contrasts with

- [Deterministic Workflows](./deterministic-workflows.md) - a hardcoded pipeline is cheaper and more predictable than an agent deciding what to do next each pass.

## Tools

- [Claude Code](../entities/tools/claude-code.md) - ships the loop primitives and usually acts as the orchestrator.
- [Archon](../entities/tools/archon.md) - turns the loop into a durable multi-node workflow with per-node models.
- [Pi](../entities/tools/pi-coding-agent.md) and [Codex](../entities/tools/codex.md) - alternative executors inside individual nodes.
- [Neon](../entities/tools/neon.md) - the Postgres state store that makes runs resumable.
- [Retool](../entities/tools/retool.md) - Internal-app platform that imports React code and connects to a database to deploy dashboards with a governed, permissioned, audit-trailed path to production.
- [OpenClaw](../entities/tools/openclaw.md) - the other agent whose creator popularized the idea.
- [Boris Cherny](../entities/people/boris-cherny.md) and [Peter Steinberger](../entities/people/peter-steinberger.md) - the source of the "I write loops" claim.
- [Geoffrey Huntley](../entities/people/geoffrey-huntley.md) - Creator of the Ralph Wiggum long-running agent loop, who frames it as a planning-heavy philosophy rather than a shiny framework or the Anthropic plugin.

## Related

- [Long-Running Agents](./long-running-agents.md) - what a well-built loop produces overnight.
- [Heartbeat](./heartbeat.md) - the scheduled trigger that starts a loop without a human present.
- [Context Rot](./context-rot.md) and [Context Isolation](./context-isolation.md) - why each pass gets its own session.
- [Model Selection](./model-selection.md) and [LLM Cost Optimization](./llm-cost-optimization.md) - per-node model choice is the main lever on loop cost.
- [Parallel Agentic Coding](./parallel-agentic-coding.md) - many worktree-isolated loops at once.
- [Human in the Loop](./human-in-the-loop.md) - approval gates between waves keep an autonomous loop honest.
- [System Evolution](./system-evolution.md) - loops that improve the system they run inside.

## Sources

- [The Creators of Claude Code and OpenClaw don't Prompt Their Agents Anymore?!](../sources/the-creators-of-claude-code-and-openclaw-dont-prompt-their-agents-anymore.md) - "[0:00:00] The real skill is designing loops that prompt your agents so they work for you 24/7."
- [The Creators of Claude Code and OpenClaw don't Prompt Their Agents Anymore?!](../sources/the-creators-of-claude-code-and-openclaw-dont-prompt-their-agents-anymore.md) - "[0:01:40] He said, \"I don't prompt Claude anymore. I write loops and the loops do the work. My job is to write loops.\""
- [The Creators of Claude Code and OpenClaw don't Prompt Their Agents Anymore?!](../sources/the-creators-of-claude-code-and-openclaw-dont-prompt-their-agents-anymore.md) - "[0:24:23] Really, I would just fold loop engineering into harness engineering. It doesn't quite deserve its own buzzword."
