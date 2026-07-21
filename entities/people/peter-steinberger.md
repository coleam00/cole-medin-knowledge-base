---
type: entity
subtype: person
title: "Peter Steinberger"
description: "Creator of OpenClaw, cited alongside Boris Cherny as a proponent of loop engineering - writing loops instead of prompting agents, backed by a near-infinite token budget."
resource: "https://x.com/steipete"
tags: [openclaw, loop-engineering, coding-agent]
videos: [the-creators-of-claude-code-and-openclaw-dont-prompt-their-agents-anymore]
created: 2026-07-21
updated: 2026-07-21
---

# Peter Steinberger

Peter Steinberger is the creator of [OpenClaw](../tools/openclaw.md) and, with [Boris Cherny](./boris-cherny.md), one of the two names Cole uses to introduce [Loop Engineering](../../concepts/loop-engineering.md): "Peter Steinberger, the creator of OpenClaw... they're pushing this new fad" ([0:00:15]). The claim under the fad is that they no longer prompt their agents at all, they write loops and let the loops do the work. Cole takes it seriously enough to demystify it: the pattern is mostly built out of ordinary [Claude Code](../tools/claude-code.md) features, a /loop that re-runs a prompt on an interval, a /goal that works until done-criteria are met in the style of [The Ralph Loop](../../concepts/the-ralph-loop.md), and scheduled /routines, all coordinated by a lightweight orchestrator agent you barely talk to.

Steinberger is also the reason Cole attaches an economic caveat to the whole idea. The blunt version: "Unless you have an infinite budget like Peter pretty much, then you have to be really careful with these kinds of systems" ([0:00:32]). Loops are extremely token-hungry, because the orchestrator has to reason and dispatch waves of workers over and over, and Cole measures a simple app costing over a million tokens. They also do not produce the best results, and a single looping session steadily bloats its own context window. What reads as a workflow breakthrough for someone with unlimited tokens reads as a cost and quality problem for everyone else.

So Cole's position is to fold loop engineering into [AI Coding Harness](../../concepts/ai-coding-harness.md) rather than adopt it wholesale. Keep the autonomy, but make the process explicit and partly deterministic, run each step in its own isolated coding-agent session, pick a cheaper model per node, and keep state durable in a database so a crashed run resumes. That is the same autonomy Steinberger is chasing, with the token bill and the context window brought back under control.

## Works with

- [OpenClaw](../tools/openclaw.md) - The open-source coding agent (formerly Claudebot) Steinberger created.
- [Claude Code](../tools/claude-code.md) - Anthropic's terminal-based agentic coding assistant, whose /loop, /goal, and /routines features implement the pattern.
- [Boris Cherny](./boris-cherny.md) - Creator of Claude Code who says he writes loops rather than prompts, the other half of this claim.

## Implemented by

- [Loop Engineering](../../concepts/loop-engineering.md) - Designing self-prompting loops so coding agents pick up and run work autonomously instead of you prompting them each time.
- [The Ralph Loop](../../concepts/the-ralph-loop.md) - Re-running an agent against the same prompt/state in a tight loop, letting each pass fix errors and compound reliability.

## Contrasts with

- [AI Coding Harness](../../concepts/ai-coding-harness.md) - The scaffolding Cole argues should absorb loop engineering, replacing one long-running session with orchestrated, isolated ones.
- [Deterministic Workflows](../../concepts/deterministic-workflows.md) - Encoding known steps as fixed code paths and reserving the LLM for the genuinely fuzzy decisions, trading autonomy for reliability.

## Related

- [LLM Cost Optimization](../../concepts/llm-cost-optimization.md) - Systematically cutting the bill for running LLM applications at scale by routing cheap traffic to cheap models.
- [Model Selection](../../concepts/model-selection.md) - Choosing the right LLM per task by trading off quality, speed, and cost.
- [Context Rot](../../concepts/context-rot.md) - The degradation of an agent's output quality as its context window fills over a long session.
- [Context Isolation](../../concepts/context-isolation.md) - Giving each agent or subagent its own clean context window so unrelated tokens never dilute the task at hand.
- [Parallel Agentic Coding](../../concepts/parallel-agentic-coding.md) - Dispatching agents to background tasks in isolated git worktrees, each returning a reviewable PR.
- [Human in the Loop](../../concepts/human-in-the-loop.md) - Keeping a human as the approver and steerer of agentic work rather than fully automating.
- [Archon](../tools/archon.md) - Cole's free, open-source AI command center and harness builder for AI coding.
- [Geoffrey Huntley](./geoffrey-huntley.md) - Creator of the Ralph Wiggum loop, the planning-heavy ancestor of this pattern.
- [Cole Medin](./cole-medin.md) - AI engineer and educator whose YouTube channel and Dynamous community teach agentic coding.

## Sources

- [The Creators of Claude Code and OpenClaw don't Prompt Their Agents Anymore?!](../../sources/the-creators-of-claude-code-and-openclaw-dont-prompt-their-agents-anymore.md) - "[0:00:15] Peter Steinberger, the creator of OpenClaw... they're pushing this new fad."
- [The Creators of Claude Code and OpenClaw don't Prompt Their Agents Anymore?!](../../sources/the-creators-of-claude-code-and-openclaw-dont-prompt-their-agents-anymore.md) - "[0:00:32] Unless you have an infinite budget like Peter pretty much, then you have to be really careful with these kinds of systems."
