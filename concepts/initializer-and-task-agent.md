---
type: concept
title: "Initializer + Task Agent Architecture"
description: "The most common harness pattern: an initializer agent scaffolds the project and produces a validated feature list, then a task agent runs in a loop making incremental progress across context-reset sessions."
tags: [architecture, initializer, agent-harness]
videos: [are-agent-harnesses-bringing-back-vibe-coding]
created: 2026-07-21
updated: 2026-07-21
---

# Initializer + Task Agent Architecture

Nearly every serious agent harness splits into two agents with different jobs and different lifetimes. Cole names it as the default shape: "the most common architecture is to have some kind of initializer that sets the stage for the longrunning task. And then you have the task agent that is responsible for making incremental progress."

The **initializer runs once**. It reads the spec, scaffolds the project, and, crucially, converts the spec into a machine-readable work queue: "what the initializer agent does is it takes our appspec and then it creates this feature list JSON file... It basically outlines 200 plus features that need to be developed and all the validation." Two things make that artifact load-bearing. It is structured rather than prose, so a loop can read, filter, and mark it off without an LLM re-interpreting the plan each pass. And each entry carries its own validation criteria, so "done" is checkable rather than asserted.

The **task agent runs many times**. Each session picks up the next unfinished feature, implements it, validates it, marks it complete, and exits. Its context is disposable by design: state lives in the feature list and the repository, not in a conversation, so a fresh window loses nothing and long-horizon work stops decaying as the transcript grows. This is also why the pattern survives error compounding better than one long agent run, since each iteration re-grounds against durable state instead of inheriting the last hour of drift.

The split is what makes the harness principled rather than a fancier way to vibe code: all the judgment concentrates in the initializer's plan, and the loop after it is mostly mechanical.

## Part of

- [AI Coding Harness](./ai-coding-harness.md) - this is the canonical internal structure of a harness.
- [Agent Architecture Patterns](./agent-architecture-patterns.md) - a two-role specialization of the general pattern set.

## Builds on

- [The Ralph Loop](./the-ralph-loop.md) - the task agent is a Ralph loop; the initializer is what gives it a queue to grind.
- [Context Reset](./context-reset.md) - disposable task-agent sessions are the whole point of externalizing state.
- [Spec-Driven Development](./spec-driven-development.md) - the appspec is the initializer's input.
- [Granular Task Management](./granular-task-management.md) - the feature list is that discipline in JSON form.

## Contrasts with

- [Vibe Coding](./vibe-coding.md) - a harness looks like autonomous vibe coding, but the validated feature list is what keeps it accountable.

## Implemented by

- [Omnigent](../entities/tools/omnigent.md) - initializer agent plus feature-list JSON plus a looping task agent, the reference implementation.
- [Archon](../entities/tools/archon.md) - workflows encode the same setup-then-iterate split as DAG nodes.
- [Claude Code](../entities/tools/claude-code.md) - the agent typically running in both roles.

## Related

- [Long-Running Agents](./long-running-agents.md) - the problem this architecture exists to solve.
- [Loop Engineering](./loop-engineering.md) - designing the task agent's iteration and exit conditions.
- [Compounding Error Rates](./compounding-error-rates.md) - per-feature validation is what stops errors multiplying across 200 steps.
- [Validation](./validation.md) and [End-to-End Validation](./end-to-end-validation.md) - the criteria attached to each feature entry.
- [One Feature Per Prompt](./one-feature-per-prompt.md) - the granularity a task-agent iteration should target.
- [Meta-Harness](./meta-harness.md) - a harness that builds harnesses reuses this same two-stage shape.
- [Structured Outputs](./structured-outputs.md) - why the feature list is JSON and not a markdown to-do.
- [Two-Layer Planning](./two-layer-planning.md) and [Phases of Work](./phases-of-work.md) - the planning discipline the initializer performs.
- [File-System-Based Agents](./file-system-based-agents.md) - state on disk is what lets the task agent forget everything else.

## Sources

- [Are Agent Harnesses Bringing Back Vibe Coding?](../sources/are-agent-harnesses-bringing-back-vibe-coding.md) - "[0:07:10] the most common architecture is to have some kind of initializer that sets the stage for the longrunning task. And then you have the task agent that is responsible for making incremental progress."
- [Are Agent Harnesses Bringing Back Vibe Coding?](../sources/are-agent-harnesses-bringing-back-vibe-coding.md) - "[0:16:28] what the initializer agent does is it takes our appspec and then it creates this feature list JSON file... It basically outlines 200 plus features that need to be developed and all the validation."
