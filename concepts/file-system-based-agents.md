---
type: concept
title: "File-System-Based Agents"
description: "An architecture where an entire AI agent is defined as a single folder of organized markdown and TypeScript primitives rather than hand-wired framework code."
tags: [agent-architecture, composability]
videos: [this-completely-changes-the-way-we-build-production-ai-agents-vercel-eve]
created: 2026-07-21
updated: 2026-07-21
---

# File-System-Based Agents

A file-system-based agent is an agent whose definition *is* a directory tree. There is no graph to wire and no registry to populate: "your entire AI agent is just a collection of files in a single folder... your AI agent is just a folder. That's what makes it so easy to build, making everything composable." [0:00:47] The whole artifact reduces to two file types - "we have a single folder that's just a collection of organized markdown and TypeScript." [0:15:39]

The folder is organized by primitive, one subfolder per concern: instructions (the system prompt, effectively [global rules](./global-rules.md)), the agent definition with model and config, [skills](./skills.md), tools, a sandbox for [code execution](./code-execution.md), channels such as Slack, connections to [MCP](../entities/tools/mcp.md) servers, [sub-agents](./subagents-pattern.md), evals, and schedules. Each is a file you drop in place, so adding a tool means writing one typed [TypeScript](../entities/tools/typescript.md) file and adding a sub-agent means creating one folder.

What makes it work rather than merely tidy is a compilation step. You never import or register anything, because running or deploying traverses the tree, discovers every skill and MCP server, and builds a single manifest that hooks it all together - the same auto-discovery move [Claude Code](../entities/tools/claude-code.md) makes when it finds a `SKILL.md` on disk. Convention replaces wiring, which is what turns the folder into a genuinely composable unit.

The consequences compound. The agent becomes diffable and reviewable in git, which makes it legible to humans and editable by coding agents alike - a coding agent scaffolding an agent is just writing files. It also collapses the distance between an agent and the [AI layer](./the-ai-layer.md) of a coding harness, since both are markdown-plus-config folders read by a runtime. And because the folder is the source of truth, the platform underneath can supply the production plumbing separately: durable checkpointed sessions, sandboxed execution, [human-in-the-loop](./human-in-the-loop.md) approvals, and [evals](./agent-evaluation.md) as a deploy gate.

Cole treats [Eve](../entities/tools/eve.md) as a standard-in-the-making for this shape, and pairs it deliberately with a separate knowledge layer in [OKF](./open-knowledge-format.md), since a markdown wiki does not scale to tens of thousands of documents. The agent is a folder; the knowledge base is its own bundle.

## Contrasts with

- [Agent Graphs](./agent-graphs.md) - explicit nodes, edges, and state wired in code instead of discovered on disk.
- [SDK vs. Framework Decision](./sdk-vs-framework-decision.md) - the tradeoff this architecture reframes as a filesystem convention.

## Builds on

- [The Core Components of an Agent](./agent-core-components.md) - the primitives that become subfolders.
- [Skills](./skills.md) and [Global Rules](./global-rules.md) - markdown-on-disk conventions this generalizes.

## Tools

- [Eve (Vercel)](../entities/tools/eve.md) - the open-source file-system-first agent framework.
- [Vercel](../entities/organizations/vercel.md) - supplies the durability, sandboxing, and hosting layer.
- [Claude Code](../entities/tools/claude-code.md) - the auto-discovery precedent, and a client that scaffolds these folders.

## Related

- [Capabilities Over Tools](./capabilities-over-tools.md), [Reusable Components and Variables](./reusable-components.md) - composability as the design goal.
- [Production-Grade Agents](./production-grade-agents.md), [Agent Deployment](./agent-deployment.md) - what the platform adds beneath the folder.
- [Subagents Pattern](./subagents-pattern.md), [Agent Evaluation](./agent-evaluation.md), [Human in the Loop](./human-in-the-loop.md) - primitives that ship as files.
- [Open Knowledge Format](./open-knowledge-format.md), [Knowledge Bases](./knowledge-bases.md) - the separate knowledge layer it pairs with.
- [The AI Layer](./the-ai-layer.md), [Docs and Templates as Coding-Assistant Context](./docs-as-agent-context.md) - the same folder-as-configuration idea in coding harnesses.
- [Handoff Documents](./handoff-documents.md) - Because isolated agents share no conversation history, they communicate by writing and reading markdown handoff files (initial.md, prompts.md) in a shared planning folder, passing only the distilled context each next step needs.

## Sources

- [This Completely Changes the Way We Build Production AI Agents (Vercel Eve)](../sources/this-completely-changes-the-way-we-build-production-ai-agents-vercel-eve.md) - "[0:00:47] your entire AI agent is just a collection of files in a single folder... your AI agent is just a folder. That's what makes it so easy to build, making everything composable."
- [This Completely Changes the Way We Build Production AI Agents (Vercel Eve)](../sources/this-completely-changes-the-way-we-build-production-ai-agents-vercel-eve.md) - "[0:15:39] we have a single folder that's just a collection of organized markdown and TypeScript."
