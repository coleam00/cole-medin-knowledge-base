---
type: entity
subtype: tool
title: "Arcade"
description: "Platform for agent authorization and tool security, enabling secure OAuth flows and MCP servers so agents can act on a user's accounts."
resource: "https://www.arcade.dev"
tags: [agent-authorization, tool-security, mcp]
videos: [turn-claude-code-into-your-full-engineering-team-with-subagents, the-only-ai-tech-stack-you-need-in-2026, why-is-everyone-missing-this-with-ai-agents-memory-tools-that-scale]
created: 2026-07-21
updated: 2026-07-21
---

# Arcade

Arcade is a platform that solves agent authorization: how an AI agent securely acts on a user's third-party accounts (Gmail, GitHub, Slack, Linear) without you hand-rolling OAuth for every service. Cole introduces it as exactly that in the subagents build at [0:02:12]: "I'm also using Arcade. This is the platform to make it super easy for us to connect to Linear, GitHub, and Slack through MCP." The load-bearing feature is the auth handshake itself, which he underlines at [0:06:21]: "They also implement what's called agent authorization. So they walk us through the OAuth flows really easily with these different services."

Across Cole's videos, Arcade earns its place by removing a problem most builders underestimate. In the memory-and-tools deep dive he is blunt about the value at [0:02:19]: "Arcade is the key here for solving the authentication and scaling nightmare for tools that I can almost guarantee you wouldn't want to build yourself." Beyond auth, it ships preconfigured tool kits so an agent gets working integrations out of the box. Demonstrating this he notes at [0:10:41]: "we passed in a couple of tool kits here for Gmail and Asana... these are the preconfigured tools. They come out of the box with Arcade." That combination, ready-made tools plus the OAuth plumbing behind them, is what makes it a shortcut rather than another dependency.

Arcade has grown into part of Cole's recommended 2026 stack, and the reason is a newer capability: building secure tool servers directly. At [0:09:12] he explains "they've recently released an MCP server SDK, so we can build secure MCP servers directly with Arcade, leveraging their tool authorization." So Arcade sits at the intersection of two things Cole cares about, the [MCP](./mcp.md) standard for exposing tools and the security layer that lets agents use those tools on real accounts safely, which is what makes it relevant for agents that serve many users at once.

## Realizes

- [Multi-Tenant Agents](../../concepts/multi-tenant-agents.md) - Building a single agent that serves many users, each with personalized tools, memory, and securely authorized access to their own accounts.
- [Memory Systems](../../concepts/memory-systems.md) - Giving agents durable short- and long-term memory so conversations, user context, and facts persist across sessions and users.

## Works with

- [MCP (Model Context Protocol)](./mcp.md) - The protocol used to connect Claude Code to external tools and servers.
- [Linear](./linear.md) - Project/issue tracker Cole used in place of the local file system to track a harness's feature list and progress, adding human-in-the-loop where teams already work.
- [GitHub](./github.md) - The gh command-line tool that lets Claude Code manage issues and pull requests directly on a remote GitHub repository.
- [Slack](./slack.md) - Messaging platform used as an alerting destination for error workflows and scheduled report notifications, and as the chat surface for talking to agents.
- [Claude Code](./claude-code.md) - Anthropic's terminal-based agentic coding assistant that is the subject of this complete-guide walkthrough.

## Related

- [Agentic Workflow Engineering](../../concepts/agentic-workflow-engineering.md) - Designing repeatable AI workflows as engineered systems with defined steps, orchestration, and background execution rather than ad-hoc prompting.
- [AI Coding Harness](../../concepts/ai-coding-harness.md) - The surrounding scaffolding (prompts, tools, rules, validation) that turns a raw model into a reliable coding system.
- [Context Engineering](../../concepts/context-engineering.md) - The deliberate practice of curating exactly what goes into an LLM's limited context window - system messages, schemas, chat history, and dynamic variables - to avoid overload and keep outputs sharp.
- [Subagents Pattern](../../concepts/subagents-pattern.md) - Delegating scoped tasks to isolated subagents to parallelize work and protect the main agent's context window.

## Sources

- [Turn Claude Code into Your Full Engineering Team with Subagents](../../sources/turn-claude-code-into-your-full-engineering-team-with-subagents.md) - "[0:06:21] They also implement what's called agent authorization. So they walk us through the OAuth flows really easily with these different services."
- [Why is Everyone Missing This with AI Agents?! (Memory + Tools that Scale)](../../sources/why-is-everyone-missing-this-with-ai-agents-memory-tools-that-scale.md) - "[0:02:19] Arcade is the key here for solving the authentication and scaling nightmare for tools that I can almost guarantee you wouldn't want to build yourself"
- [The ONLY AI Tech Stack You Need in 2026](../../sources/the-only-ai-tech-stack-you-need-in-2026.md) - "[0:09:12] they've recently released an MCP server SDK, so we can build secure MCP servers directly with Arcade, leveraging their tool authorization"
