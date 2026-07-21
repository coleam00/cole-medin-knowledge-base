---
type: concept
title: "Granular Task Management"
description: "Breaking a large request into small focused tasks on a shared, persistent task board the agent works through one at a time, so its plan stays visible and steerable."
tags: [implementation, tasks, workflow, task-management]
videos: [the-true-power-of-ai-coding-build-your-own-workflows-full-guide, introducing-archon-the-revolutionary-operating-system-for-ai-coding]
created: 2026-07-21
updated: 2026-07-21
---

# Granular Task Management

Granular task management is the practice of decomposing a large request into small, single-purpose tasks that the agent works through one at a time, tracked on a board you can see and edit. Cole calls it the load-bearing piece of the implementation phase: "the task management here is the most important thing, especially if you're trying to do quite a bit in one request. If the coding assistant tries to do too much at once, that's when you have a lot of hallucinations." [0:16:28] The mechanism is focus, not bookkeeping - "tasks are your way to have a larger request, but still have it be very focused and granular on one little thing each time." [0:16:44]

Execution is deliberately serial and stateful. The agent "is going to knock them out one by one slowly moving them into in process and then in review, moving on to the next one" [0:12:24], so at any moment exactly one small thing is in flight and everything else is parked outside the working context. That is what keeps a long build from degrading: each task is a small enough unit that the model's attention covers it fully, the same "never too much at once" rule that [Phases of Work](./phases-of-work.md) and [One Feature Per Prompt](./one-feature-per-prompt.md) apply at other scales.

The second payoff is steerability. Because the board is shared rather than internal to the agent, the plan becomes an artifact you can inspect and correct: "we can update these descriptions and things in real time, add our own tasks" [0:12:24], and the board doubles as a review surface for the plan itself - "it's like, 'Oh, let me create the project at Archon and set all the tasks.' And it puts it in there and I go look and I'm like, 'Yeah, this plan looks good.' It's so much easier for me to work with than seeing their to-do list." [0:21:40] That last clause is the sharp contrast: a coding agent's built-in to-do list is an ephemeral scroll-by, while a persistent board is legible, durable, and editable.

It also fixes a specific failure mode. Editing a task the agent has not reached yet lets you redirect work without interrupting it mid-thought, and interrupting a coding assistant mid-thought is itself a reliable cause of hallucination. The correction lands when the agent picks the task up, so [human steering](./human-in-the-loop.md) becomes asynchronous instead of disruptive.

## Part of

- [The PIV Loop](./the-piv-loop.md) - tasks are how the implement phase is executed.
- [Agentic Workflow Engineering](./agentic-workflow-engineering.md) - a structural component of a reusable workflow.

## Builds on

- [Planning with AI](./planning-with-ai.md) and [PRD-First Development](./prd-first-development.md) - the plan is what gets sharded into tasks.
- [Phases of Work](./phases-of-work.md) - phases are the coarser decomposition tasks sit inside.

## Tools

- [Archon](../entities/tools/archon.md) - the shared task board Cole uses, human UI plus MCP server on the same projects.
- [Claude Code](../entities/tools/claude-code.md) - the agent working the board via MCP.

## Related

- [One Feature Per Prompt](./one-feature-per-prompt.md) - the same focus rule at prompt scale.
- [Human in the Loop](./human-in-the-loop.md) - editing tasks beats interrupting a running agent.
- [Hallucination Detection](./hallucination-detection.md), [Compounding Error Rates](./compounding-error-rates.md), [Context Rot](./context-rot.md) - what doing too much at once causes.
- [Slash Commands](./slash-commands.md) and [Commandify Everything](./commandify-everything.md) - an execute-plan command drives the task loop.
- [Handoff Documents](./handoff-documents.md) - persisted state across sessions, the same durability argument.
- [Spec-Driven Development](./spec-driven-development.md) - tasks are the executable end of the spec.

## Sources

- [The True Power of AI Coding - Build Your OWN Workflows (Full Guide)](../sources/the-true-power-of-ai-coding-build-your-own-workflows-full-guide.md) - "[0:16:28] the task management here is the most important thing, especially if you're trying to do quite a bit in one request. If the coding assistant tries to do too much at once, that's when you have a lot of hallucinations."
- [The True Power of AI Coding - Build Your OWN Workflows (Full Guide)](../sources/the-true-power-of-ai-coding-build-your-own-workflows-full-guide.md) - "[0:16:44] tasks are your way to have a larger request, but still have it be very focused and granular on one little thing each time."
- [Introducing Archon - The Revolutionary Operating System for AI Coding](../sources/introducing-archon-the-revolutionary-operating-system-for-ai-coding.md) - "[0:12:24] it's going to knock them out one by one slowly moving them into in process and then in review, moving on to the next one. And like I said, we can update these descriptions and things in real time, add our own tasks"
- [Introducing Archon - The Revolutionary Operating System for AI Coding](../sources/introducing-archon-the-revolutionary-operating-system-for-ai-coding.md) - "[0:21:40] it's like, 'Oh, let me create the project at Archon and set all the tasks.' And it puts it in there and I go look and I'm like, 'Yeah, this plan looks good.' It's so much easier for me to work with than seeing their to-do list."
