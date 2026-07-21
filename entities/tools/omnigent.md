---
type: entity
subtype: tool
title: "Omnigent"
description: "Open-source meta-harness from Databricks that orchestrates multiple AI coding agents (Claude Code, Codex, Pi) from one customizable AI layer with sandboxing, guardrails, and cross-device collaboration."
resource: "https://github.com/databricks/omnigent"
tags: [ai-coding, coding-agent, meta-harness, open-source]
videos: [omnigent-the-new-meta-harness-for-every-coding-agent-claude-code-codex-pi-more]
created: 2026-07-21
updated: 2026-07-21
---

# Omnigent

Omnigent is an open-source [meta-harness](../../concepts/meta-harness.md) from Databricks that sits above your individual coding assistants and drives them as a fleet. Cole's definition is exact: "An Omni agent is the layer above the AI coding assistance that makes this orchestration really straightforward" [0:00:51]. Without it you juggle terminals and per-tool configs; with it, one session commands [Claude Code](./claude-code.md), [Codex](./codex.md), [Pi](./pi-coding-agent.md), and the rest. It is the first tool he points at as a working, out-of-the-box realization of the category: "Omni Agent has made it so easy for us to run this meta harness pretty much right out of the box" [0:02:40].

## What it is

The architectural move is that [the AI layer](../../concepts/the-ai-layer.md) lives once, at the server, instead of once per assistant. System prompts, [skills](../../concepts/skills.md), MCP servers, policies, [guardrails](../../concepts/guardrails.md), and sandboxing are configured centrally and then apply to whichever agent runs, reachable from a native app, REST API, terminal, or web UI. Every orchestrator is assembled from three primitives: configuration (executor, system prompt, sandboxing, guardrails, tools), skills as repeatable workflows, and the set of agents it may delegate to. Runs go into a sandbox by default, unsandboxed or via [Docker](./docker.md) or a hosted sandbox platform, and you can point a run at a [git worktree](./git-worktree.md) for [parallel work](../../concepts/parallel-agentic-coding.md).

## Why it matters

Cole's argument is that the harness now matters as much as the model, so provider lock-in for an entire workflow is a liability. Omnigent's shipped orchestrators show the payoff: Poly delegates implementation to Claude Code and review to Codex, which is [separate reviewer](../../concepts/separate-reviewer.md) discipline enforced by the tool rather than by habit, and Debbie pits two models against each other to debate a question before synthesizing a conclusion ([adversarial agents](../../concepts/adversarial-agents.md)). Mixing assistants also buys [context isolation](../../concepts/context-isolation.md) across separate sessions. He demos a Python-defined policy requiring human approval before any force git push, showing that [human-in-the-loop](../../concepts/human-in-the-loop.md) controls hold no matter which agent is executing, and highlights shared sessions across phone and desktop. He is explicit that Omnigent is feeding his own thinking on [Archon](./archon.md), which he is building around meta-harness engineering.

## Realizes

- [Meta-Harness](../../concepts/meta-harness.md) - A layer above individual AI coding assistants that orchestrates many of them together on larger tasks.
- [The AI Layer](../../concepts/the-ai-layer.md) - The rules, commands, skills, and context you own on top of a codebase, here hoisted to the server so it applies to every agent.
- [Provider Independence](../../concepts/provider-independence.md) - Architecting so the underlying model or client can be swapped without a rewrite.
- [Initializer + Task Agent Architecture](../../concepts/initializer-and-task-agent.md) - The most common harness pattern: an initializer agent scaffolds the project and produces a validated feature list, then a task agent runs in a loop making incremental progress across context-reset sessions.

## Works with

- [Claude Code](./claude-code.md) - Anthropic's terminal coding agent, the default executor and the implementer in the Poly orchestrator.
- [Codex](./codex.md) - OpenAI's software-engineering agent, assigned the review pass so the reviewer is not the author.
- [Pi](./pi-coding-agent.md) - Minimalistic open-source coding agent, another harness Omnigent can drive.
- [Docker](./docker.md) - One of the sandboxing backends an agent run can be confined to.
- [Git Worktrees](./git-worktree.md) - Isolated branch checkouts Omnigent can target so parallel runs never collide.
- [Archon](./archon.md) - Cole's own AI command center, which he is evolving toward meta-harness engineering with ideas taken from Omnigent.
- [Databricks](../organizations/databricks.md) - Data and AI company that open-sourced Omnigent (driven by its CTO and dogfooded internally); also the acquirer of Neon.

## Related

- [AI Coding Harness](../../concepts/ai-coding-harness.md) - The scaffolding around a raw model that Omnigent orchestrates one level up from.
- [Separate Reviewer](../../concepts/separate-reviewer.md) - Splitting authoring and grading across agents so review is not biased.
- [Adversarial Agents](../../concepts/adversarial-agents.md) - Pitting a generator against a critic, which the Debbie orchestrator implements as a debate.
- [Guardrails](../../concepts/guardrails.md) - Policy checks that stop dangerous actions, defined in Python and enforced per agent.
- [Human in the Loop](../../concepts/human-in-the-loop.md) - Requiring approval on risky operations such as a force push.
- [Context Isolation](../../concepts/context-isolation.md) - Splitting work across sessions so unrelated tokens never dilute the task.
- [Disposable Agent Sandboxes](../../concepts/disposable-agent-sandboxes.md) - Ephemeral scoped environments, the execution model Omnigent defaults to.
- [Parallel Agentic Coding](../../concepts/parallel-agentic-coding.md) - Running many agents at once in isolated worktrees.
- [Model Selection](../../concepts/model-selection.md) - Choosing the right model per step, which mixing harnesses makes routine.
- [Skills](../../concepts/skills.md) - Reusable capability packages, one of the three orchestrator primitives.

## Sources

- [Omnigent: The New Meta-Harness for EVERY Coding Agent - Claude Code, Codex, Pi, More](../../sources/omnigent-the-new-meta-harness-for-every-coding-agent-claude-code-codex-pi-more.md) - "[0:00:51] An Omni agent is the layer above the AI coding assistance that makes this orchestration really straightforward."
- [Omnigent: The New Meta-Harness for EVERY Coding Agent - Claude Code, Codex, Pi, More](../../sources/omnigent-the-new-meta-harness-for-every-coding-agent-claude-code-codex-pi-more.md) - "[0:02:40] Omni Agent has made it so easy for us to run this meta harness pretty much right out of the box."
