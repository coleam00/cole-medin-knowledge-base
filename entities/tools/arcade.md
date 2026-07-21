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

Arcade is a platform that solves agent authorization: how an AI agent securely acts on a user's third-party accounts (Gmail, GitHub, Slack, Linear) without you hand-rolling OAuth for every service. Cole introduces it as exactly that in the subagents build at [0:02:12]: "I'm also using Arcade. This is the platform to make it super easy for us to connect to Linear, GitHub, and Slack through MCP." The load-bearing feature is the auth handshake itself, which he underlines at [0:06:21]: "They also implement what's called agent authorization. So they walk us through the OOTH flows really easily with these different services."

Across Cole's videos, Arcade earns its place by removing a problem most builders underestimate. In the memory-and-tools deep dive he is blunt about the value at [0:02:19]: "Arcade is the key here for solving the authentication and scaling nightmare for tools that I can almost guarantee you wouldn't want to build yourself." Beyond auth, it ships preconfigured tool kits so an agent gets working integrations out of the box. Demonstrating this he notes at [0:10:41]: "we passed in a couple of tool kits here for Gmail and ASA... these are the preconfigured tools. They come out of the box with Arcade." That combination, ready-made tools plus the OAuth plumbing behind them, is what makes it a shortcut rather than another dependency.

Arcade has grown into part of Cole's recommended 2026 stack, and the reason is a newer capability: building secure tool servers directly. At [0:09:12] he explains "they've recently released an MCP server SDK, so we can build secure MCP servers directly with Arcade, leveraging their tool authorization." So Arcade sits at the intersection of two things Cole cares about, the [MCP](./mcp.md) standard for exposing tools and the security layer that lets agents use those tools on real accounts safely, which is what makes it relevant for agents that serve many users at once.

## Related

- Arcade's OAuth handshakes and preconfigured tool kits are how it realizes [Multi-Tenant Agents](../../concepts/multi-tenant-agents.md) and safe [Memory Systems](../../concepts/memory-systems.md) that touch a user's real accounts.
- Its MCP server SDK connects it to the [MCP](./mcp.md) tooling layer and to [Context Engineering](../../concepts/context-engineering.md), giving an agent scoped access to external context.
- It appears inside Cole's [Subagents Pattern](../../concepts/subagents-pattern.md) builds and broader [Agentic Workflow Engineering](../../concepts/agentic-workflow-engineering.md), often driven from within an [AI Coding Harness](../../concepts/ai-coding-harness.md).
- Sibling tools it wires together: [Linear](./linear.md), [GitHub](./github.md), [Slack](./slack.md), [Claude Code](./claude-code.md).

## Sources

- [Turn Claude Code into Your Full Engineering Team with Subagents](../../sources/turn-claude-code-into-your-full-engineering-team-with-subagents.md) - "[0:06:21] They also implement what's called agent authorization. So they walk us through the OOTH flows really easily with these different services."
- [Why is Everyone Missing This with AI Agents?! (Memory + Tools that Scale)](../../sources/why-is-everyone-missing-this-with-ai-agents-memory-tools-that-scale.md) - "[0:02:19] Arcade is the key here for solving the authentication and scaling nightmare for tools that I can almost guarantee you wouldn't want to build yourself"
- [The ONLY AI Tech Stack You Need in 2026](../../sources/the-only-ai-tech-stack-you-need-in-2026.md) - "[0:09:12] they've recently released an MCP server SDK, so we can build secure MCP servers directly with Arcade, leveraging their tool authorization"
