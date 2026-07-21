---
type: entity
subtype: tool
title: "Eve (Vercel)"
description: "Vercel's open-source 'file-system first' agent framework where an entire agent is a single folder of markdown/TypeScript, compiled and deployed to production with durable sessions, sandboxing, human-in-the-loop, and evals."
resource: "https://vercel.com"
tags: [agent-framework, sdk, production-agents]
videos: [this-completely-changes-the-way-we-build-production-ai-agents-vercel-eve]
created: 2026-07-21
updated: 2026-07-21
---

# Eve (Vercel)

Eve is Vercel's open-source agent framework, and its defining claim is architectural rather than model-related: "A new open-source AI agent framework was just released by Vercel called Eve... They're calling it a file system first framework" [0:00:00]. An agent is a single parent folder, and every primitive is a subfolder inside it: instructions ([global rules](../../concepts/global-rules.md) and the system prompt), the agent definition (model plus config), [skills](../../concepts/skills.md), tools, a sandbox for [code execution](../../concepts/code-execution.md), channels like [Slack](./slack.md), connections to [MCP](./mcp.md) servers, [sub-agents](../../concepts/subagents-pattern.md), evals, and schedules. Cole closes by naming the ambition directly: "that's everything that I have to cover for Eve, the new framework and standard for file-system-based agents" [0:15:25].

The feature that makes the folder more than a convention is compilation. You never import or wire anything by hand; running or deploying traverses the tree, discovers every skill, tool, and MCP server, and builds one manifest that hooks it all together, the same auto-discovery instinct that [Claude Code](./claude-code.md) applies to a SKILL.md. That is [progressive disclosure](../../concepts/progressive-disclosure.md) enforced by the build step rather than by the developer's discipline.

The rest is Vercel's infrastructure answering the hard parts of [production-grade agents](../../concepts/production-grade-agents.md): checkpointed durable sessions that survive crashes, isolated sandboxes, [human-in-the-loop](../../concepts/human-in-the-loop.md) approval buttons in Slack before a risky SQL operation runs, and [evals](../../concepts/agent-evaluation.md) as a deploy gate. Tools are single [TypeScript](./typescript.md) files typed with [Zod](./zod.md), and a Vercel plugin lets a coding agent like Claude Code or [Cursor](./cursor.md) scaffold, test, and one-command deploy the whole thing.

Cole frames Eve as a standard in the making that pairs naturally with the [Open Knowledge Format](../../concepts/open-knowledge-format.md) for the separate [knowledge-base](../../concepts/knowledge-bases.md) layer, since markdown wikis do not scale to tens of thousands of documents. Read that way, Eve is the harness idea pushed into production: the folder is the source of truth, and the platform supplies the durability, security, and evaluation plumbing you would otherwise hand-build.

## Realizes

- [File-System-Based Agents](../../concepts/file-system-based-agents.md) - An architecture where an entire AI agent is defined as a single folder of organized markdown and TypeScript primitives rather than hand-wired framework code.
- [Production-Grade Agents](../../concepts/production-grade-agents.md) - Real agents need validation, error handling, testing, logging, observability, and monitoring rather than just an LLM plus tools stitched together.
- [Agent Evaluation](../../concepts/agent-evaluation.md) - Systematically scoring agent behavior with evals and benchmarks, including as a gate before deployment.
- [Human in the Loop](../../concepts/human-in-the-loop.md) - Keeping a human as the approver and steerer of agentic work rather than fully automating.
- [Code Execution](../../concepts/code-execution.md) - Giving agents a sandbox to write and run code as a general-purpose tool rather than exposing many narrow tools.

## Works with

- [Claude Code](./claude-code.md) - Anthropic's terminal-based agentic coding assistant; scaffolds, builds, and deploys Eve agents through the Vercel plugin.
- [Cursor](./cursor.md) - AI coding assistant, the other named client for the Eve plugin.
- [MCP (Model Context Protocol)](./mcp.md) - Connections are just MCP servers dropped into a folder and discovered at compile time.
- [Slack](./slack.md) - The channel used to talk to the deployed agent and to surface approval buttons.
- [TypeScript](./typescript.md) - The language tools and agent definitions are written in.
- [Zod](./zod.md) - A TypeScript schema/validation library used to type agent tool inputs so the arguments the model passes to a function are reliable.
- [Vercel AI SDK](./vercel-ai-sdk.md) - Vercel's other AI library, the lower-level sibling to Eve's full framework.

## Contrasts with

- [Claude Agent SDK](./claude-agent-sdk.md) - The engine behind Claude Code exposed as a library; the coding-agent harness route rather than a file-system agent standard.
- [LangChain Deep Agents](./langchain-deep-agents.md) - LangChain's harness implementation for long-running agents that manages context by offloading to file-system tools.
- [Archon](./archon.md) - Cole's free, open-source AI command center and harness builder for AI coding.

## Related

- [SDK vs. Framework Decision](../../concepts/sdk-vs-framework-decision.md) - Choosing between a batteries-included coding-agent SDK and a from-scratch agent framework based on who uses the agent and tolerance for speed, cost, and determinism.
- [Skills](../../concepts/skills.md) - Reusable, model-invoked capability packages that load specialized instructions and tools on demand to extend an agent.
- [Subagents Pattern](../../concepts/subagents-pattern.md) - Delegating scoped tasks to isolated subagents to parallelize work and protect the main agent's context window.
- [Global Rules](../../concepts/global-rules.md) - Persistent project- or user-level rule files that inject standing context and conventions into every agent run.
- [Agent Protocols](../../concepts/agent-protocols.md) - Emerging standards (A2A, agent cards, discovery) that let agents interoperate and be called across clients.
- [Open Knowledge Format (OKF)](../../concepts/open-knowledge-format.md) - A minimal open standard layered on the Karpathy LLM wiki that fixes how a knowledge base is organized and what metadata its pages carry.
- [Knowledge Bases](../../concepts/knowledge-bases.md) - Curated bodies of knowledge an agent can retrieve from, distinct from raw model weights.
- [Agent Deployment](../../concepts/agent-deployment.md) - Getting agents to production, containerizing, networking, reverse-proxying, and choosing a provider-agnostic, cost-predictable host.
- [Memory Systems](../../concepts/memory-systems.md) - Giving agents durable short- and long-term memory so conversations, user context, and facts persist across sessions.
- [AI Coding Harness](../../concepts/ai-coding-harness.md) - The surrounding scaffolding (prompts, tools, rules, validation) that turns a raw model into a reliable coding system.

## Sources

- [This Completely Changes the Way We Build Production AI Agents (Vercel Eve)](../../sources/this-completely-changes-the-way-we-build-production-ai-agents-vercel-eve.md) - "[0:00:00] A new open-source AI agent framework was just released by Vercel called Eve... They're calling it a file system first framework."
- [This Completely Changes the Way We Build Production AI Agents (Vercel Eve)](../../sources/this-completely-changes-the-way-we-build-production-ai-agents-vercel-eve.md) - "[0:15:25] that's everything that I have to cover for Eve, the new framework and standard for file-system-based agents."
