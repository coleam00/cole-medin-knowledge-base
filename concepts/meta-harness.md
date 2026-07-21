---
type: concept
title: "Meta-Harness"
description: "A layer above individual AI coding assistants that orchestrates many of them together on larger tasks, distinct from a single-agent harness."
tags: [harness-engineering, orchestration]
videos: [omnigent-the-new-meta-harness-for-every-coding-agent-claude-code-codex-pi-more]
created: 2026-07-21
updated: 2026-07-21
---

# Meta-Harness

A meta-harness is the coordination layer that sits above coding assistants rather than inside one: "Instead of making one coding agent better, what if we have the layer above that orchestrates many AI coding assistants working together on larger tasks? That's exactly what a metah harness is." [0:02:10] Where a harness wraps a single agent in prompts, validation, and a loop, a meta-harness treats whole agents as interchangeable executors and routes work between them - "it is a very powerful and free-to-use meta harness. A meta harness is a tool that allows you to run longer AI coding workflows, mixing AI coding assistance." [0:00:03]

The argument for the layer is that reliability no longer comes from the model. Models get deprecated, banned, or regress, so the durable investment is the surrounding system, and the next increment up from a per-agent harness is one that mixes agents deliberately: lean on each tool's strengths and isolate context across separate sessions to control tokens.

Structurally, a meta-harness hoists the customizable AI layer out of any one assistant and into a server: system prompts, skills, MCP servers, policies, guardrails, and sandboxing are configured once and apply to every connected agent, reachable through a native app, a REST API, a terminal, or a web UI. Orchestrators are then assembled from three primitives - configuration (executor, system prompt, sandboxing, guardrails, tools), skills (repeatable workflows), and the set of agents it may delegate to. The shipped examples make the shape concrete: one delegates implementation to Claude Code and review to Codex, keeping review in a separate unbiased session; another pits two agents against each other to debate a question and synthesizes the conclusion. Because policy lives at the meta layer, a Python rule requiring human approval before a force push applies no matter which agent is executing, and a session can be shared across devices or hosted for a team.

The practical takeaway is provider strategy: you do not want a whole workflow locked to one model or vendor, and the meta-harness is where that mixing becomes a configuration choice instead of a rewrite.

## Builds on

- [AI Coding Harness](./ai-coding-harness.md) - the single-agent layer a meta-harness sits above.
- [The AI Layer](./the-ai-layer.md) - the prompts, skills, and policies hoisted to the server so every agent inherits them.

## Contrasts with

- [Subagents Pattern](./subagents-pattern.md) and [Agent Teams](./agent-teams.md) - delegation inside one assistant, versus orchestration across separate assistants.

## Tools

- [Omnigent](../entities/tools/omnigent.md) - the open-source meta-harness this page is drawn from.
- [Databricks](../entities/organizations/databricks.md) - released and dogfoods Omnigent.
- [Claude Code](../entities/tools/claude-code.md), [Codex](../entities/tools/codex.md), and [Pi](../entities/tools/pi-coding-agent.md) - the interchangeable executors it orchestrates.
- [Archon](../entities/tools/archon.md) - the workflow-engine take on the same layer, with per-node models and durable state.

## Related

- [Provider Independence](./provider-independence.md) - the core motivation for not binding a workflow to one vendor.
- [Model Selection](./model-selection.md) - picking the right agent per step is the meta-harness's main lever.
- [Separate Reviewer](./separate-reviewer.md) - implement with one agent, review with another to avoid self-bias.
- [Adversarial Agents](./adversarial-agents.md) - the debate-and-synthesize orchestrator pattern.
- [Context Isolation](./context-isolation.md) - each delegated agent runs in its own session.
- [Guardrails](./guardrails.md) and [Human in the Loop](./human-in-the-loop.md) - policies enforced at the layer above every executor.
- [Skills](./skills.md) - repeatable workflows an orchestrator can call.
- [Agentic Workflow Engineering](./agentic-workflow-engineering.md) and [Loop Engineering](./loop-engineering.md) - designing what the layer actually runs.
- [Parallel Agentic Coding](./parallel-agentic-coding.md) - many orchestrated agents working at once.
- [Agents That Build Agents](./agents-that-build-agents.md) - A meta-agent whose specialty is generating, iterating on, and eventually running other AI agents on demand, so the agents it produces become reusable sub-agents themselves.

## Sources

- [Omnigent: The New Meta-Harness for EVERY Coding Agent - Claude Code, Codex, Pi, More](../sources/omnigent-the-new-meta-harness-for-every-coding-agent-claude-code-codex-pi-more.md) - "[0:00:03] It's called Omni Agent... it is a very powerful and free-to-use meta harness. A meta harness is a tool that allows you to run longer AI coding workflows, mixing AI coding assistance."
- [Omnigent: The New Meta-Harness for EVERY Coding Agent - Claude Code, Codex, Pi, More](../sources/omnigent-the-new-meta-harness-for-every-coding-agent-claude-code-codex-pi-more.md) - "[0:02:10] Instead of making one coding agent better, what if we have the layer above that orchestrates many AI coding assistants working together on larger tasks? That's exactly what a metah harness is."
