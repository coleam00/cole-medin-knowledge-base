---
type: source
title: "This Completely Changes the Way We Build Production AI Agents (Vercel Eve)"
description: "Vercel's open-source Eve framework makes file-system-first AI agents (an agent that is just a folder of markdown and TypeScript) production-grade by handling compilation, durable sessions, sandboxing, human-in-the-loop, and evals under the hood."
youtube_id: m8VC2SV2igM
url: https://www.youtube.com/watch?v=m8VC2SV2igM
slug: this-completely-changes-the-way-we-build-production-ai-agents-vercel-eve
published: 2026-07-15
duration: "0:16:25"
recency_rank: 1
raw: "../raw/this-completely-changes-the-way-we-build-production-ai-agents-vercel-eve.md"
tags: [agent-frameworks, file-system-agents, production-agents]
created: 2026-07-21
updated: 2026-07-21
---

Cole reviews Eve, a new open-source "file system first" agent framework from Vercel. The core idea is that an AI agent is just a single parent folder containing subfolders for each primitive: instructions (system prompt / global rules), the agent definition (model + config), skills, tools, a sandbox for code execution, channels (Slack/Discord), connections (MCP servers), sub-agents, evals, and schedules. Eve's most impressive feature is a compilation step: you never import or wire anything by hand, because running or deploying the agent traverses the folder, discovers every skill and MCP server, and builds a single manifest that hooks everything together, similar to how Claude Code auto-discovers a skill.md file.

Beyond composability, Eve inherits Vercel's infrastructure for production reliability: durable checkpointed sessions that survive crashes, isolated sandboxed code execution, human-in-the-loop approvals at risky steps, and evals as a deploy gate, plus autoscaling hosting. A Vercel plugin lets coding agents like Claude Code or Cursor scaffold, build, test, and one-command deploy Eve agents.

Cole frames Eve as a standard-in-the-making for file-system agents that pairs naturally with OKF for the separate knowledge-base layer, since markdown wikis don't scale to tens of thousands of documents. The framework is a clean expression of the harness idea applied to production: the folder is the source of truth, and the platform supplies the durability, security, and evaluation plumbing you would otherwise have to build yourself.

## Concepts covered

- [Agentic Coding](../concepts/agentic-coding.md)
- [System Evolution](../concepts/system-evolution.md)
- [Memory Systems](../concepts/memory-systems.md)
- [Agent Evaluation](../concepts/agent-evaluation.md)
- [Human in the Loop](../concepts/human-in-the-loop.md)
- [Code Execution](../concepts/code-execution.md)
- [Skills](../concepts/skills.md)
- [Subagents Pattern](../concepts/subagents-pattern.md)
- [Global Rules](../concepts/global-rules.md)
- [Agent Protocols](../concepts/agent-protocols.md)
- [Knowledge Bases](../concepts/knowledge-bases.md)

## Entities

- [Vercel](../entities/organizations/vercel.md)
- [Claude Code](../entities/tools/claude-code.md)
- [Cline](../entities/tools/cline.md)
- [MCP (Model Context Protocol)](../entities/tools/mcp.md)
- [Anthropic](../entities/organizations/anthropic.md)
- [Slack](../entities/tools/slack.md)
- [Cole Medin](../entities/people/cole-medin.md)

## Key moments

- **[0:00:00]** Intro: Vercel releases Eve, a "file system first" open-source agent framework
- **[0:01:02]** The agent-as-a-folder structure: instructions, agent definition, skills, tools, sandbox, channels, connections, sub-agents, schedules
- **[0:02:35]** The compilation step: Eve traverses the folder and builds a single manifest, no manual imports
- **[0:03:54]** Production reliability: durable sessions, isolated sandboxing, human-in-the-loop, evals as deploy gate, Vercel hosting
- **[0:05:25]** On standards (MCP, A2A, OKF): Eve sets a precedent for file-system agents; pairs with OKF for knowledge bases
- **[0:06:57]** Vercel plugin for coding agents (Claude Code/Cursor) makes building/deploying Eve agents trivial
- **[0:08:09]** Demo: the Eve analyst agent, agent.ts, running locally with Claude Sonnet 5
- **[0:11:04]** Adding tools (single TypeScript files with Zod typing), skills, sub-agents with zero wiring
- **[0:12:22]** One-command deploy via the Vercel MCP, smoke test, running eval suite
- **[0:13:40]** Talking to the deployed agent in Slack, thread short-term memory, parallel conversations
- **[0:14:34]** Human-in-the-loop approval buttons in Slack for a risky SQL operation

## Transcript

[Raw transcript](../raw/this-completely-changes-the-way-we-build-production-ai-agents-vercel-eve.md)
