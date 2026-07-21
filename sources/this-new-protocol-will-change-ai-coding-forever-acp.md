---
type: source
title: "This New Protocol Will Change AI Coding Forever (ACP)"
description: "Zed's new Agent Client Protocol (ACP) is an MCP-like open standard that lets any coding agent connect to any code editor, making it trivial to switch between agents, build custom ones, and orchestrate them in parallel."
youtube_id: 5gUR55_gbzc
url: https://www.youtube.com/watch?v=5gUR55_gbzc
slug: this-new-protocol-will-change-ai-coding-forever-acp
published: 2025-09-10
duration: "0:22:35"
recency_rank: 71
raw: "../raw/this-new-protocol-will-change-ai-coding-forever-acp.md"
tags: [protocols, agentic-coding, provider-independence]
created: 2026-07-21
updated: 2026-07-21
---

# This New Protocol Will Change AI Coding Forever (ACP)

This video introduces the Agent Client Protocol (ACP), a new open standard from the Zed editor team that does for coding-agent-to-editor connections what MCP did for tools and what the Language Server Protocol did for programming languages. Cole demonstrates running both Gemini CLI and Claude Code threads inside Zed, switching between them with a single click, and getting live in-editor updates where he can accept or reject the agent's changes. Because ACP is a standard rather than a bespoke integration, none of an agent's native features (subagents, custom slash commands) are lost, and authentication happens entirely inside the editor.

Cole then explains how ACP works under the hood. It is a JSON-RPC protocol, like MCP, with a small set of operations: the editor spins up a local agent instance over standard IO, opens a session as a handshake, then exchanges JSON events for user messages, agent message chunks, task lists, tool calls, and permission requests. He walks through building a custom agent from Zed's TypeScript example, where hardcoded ACP messages stand in for a real LLM loop, and shows how Claude Code, which lacks native ACP support, is bridged with a roughly 600-line adapter that reformats Claude Code SDK messages into ACP's JSON shape.

The final third is a proof of concept from teammate Rasmus that wires ACP into Archon, Cole's command center for AI coding. The vision: connect a git repository, attach a knowledge base and MCP servers as context, then dispatch any ACP-compatible agent (Claude Code, Gemini CLI, Cursor, Codex, Devin) to a background task in its own git worktree that returns a reviewable PR, all managed in parallel from one interface and running locally rather than in a vendor cloud.

## Concepts covered

- [Agent Client Protocol (ACP)](../concepts/agent-client-protocol.md)
- [Provider Independence](../concepts/provider-independence.md)
- [Agent Protocols](../concepts/agent-protocols.md)
- [Language Server Protocol](../concepts/language-server-protocol.md)
- [Human in the Loop](../concepts/human-in-the-loop.md)
- [Parallel Agentic Coding](../concepts/parallel-agentic-coding.md)

## Entities

- [Gemini CLI](../entities/tools/gemini-cli.md)
- [Claude Code](../entities/tools/claude-code.md)
- [Archon](../entities/tools/archon.md)
- [MCP (Model Context Protocol)](../entities/tools/mcp.md)
- [Git Worktrees](../entities/tools/git-worktree.md)
- [Rasmus](../entities/people/rasmus.md)
- [Cole Medin](../entities/people/cole-medin.md)

## Key moments

- **[0:00:00]** Intro: Zed introduces the Agent Client Protocol (ACP), a standard like MCP but for connecting any coding assistant to any code editor
- **[0:02:40]** Getting started: install Zed (free/open source); Gemini CLI has native ACP support, Claude Code goes through an adapter
- **[0:03:41]** Live demo: sending requests, @-mentioning files, and accepting/rejecting changes in-editor for Gemini CLI
- **[0:04:15]** Switching to a Claude Code thread with one click; same experience, different agent
- **[0:05:56]** ACP builds on MCP and the Language Server Protocol (LSP); even if ACP isn't the winner, the standard will look like it
- **[0:07:28]** Under the hood: JSON-RPC protocol, session handshake, and a small set of operations (user messages, tool calls, permission requests)
- **[0:11:22]** Building a custom agent from Zed's TypeScript example (hardcoded ACP messages simulating a turn)
- **[0:14:19]** The Claude Code ACP adapter: ~600 lines that reformat Claude Code SDK messages into ACP JSON
- **[0:16:17]** Rasmus's Archon + ACP proof of concept: dispatch any agent to a background task in its own git worktree, returning a PR

## Transcript

[Raw transcript](../raw/this-new-protocol-will-change-ai-coding-forever-acp.md)

## Sources

- [This New Protocol Will Change AI Coding Forever (ACP)](./this-new-protocol-will-change-ai-coding-forever-acp.md) - "[0:05:56] ACP builds on MCP and the Language Server Protocol (LSP); even if ACP isn't the winner, the standard will look like it"
