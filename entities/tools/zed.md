---
type: entity
subtype: tool
title: "Zed"
description: "A free, open-source code editor from the team that created the Agent Client Protocol, shipping the first beta ACP implementation with native Gemini CLI and adapter-based Claude Code support."
resource: "https://zed.dev"
tags: [ai-coding, coding-agent]
videos: [this-new-protocol-will-change-ai-coding-forever-acp]
created: 2026-07-21
updated: 2026-07-21
---

# Zed

Zed is a code editor, and Cole places it precisely: "Zed is a code editor just like VS Code and its forks like Windsurf and Cursor" [0:01:22]. What separates it is authorship. Zed's team did not build a one-off [Claude Code](./claude-code.md) integration when they wanted an agent in the editor. They wrote a standard, the [Agent Client Protocol](../../concepts/agent-client-protocol.md), and Zed is its first shipping implementation: "all you have to do to get started with ACP is install Zed. That's what we're looking at right here. It's a completely free and open source code editor" [0:02:26].

In practice that means the agent panel toggles open on the right, and a plus button starts a [Gemini CLI](./gemini-cli.md) thread (a direct ACP integration), a Claude Code thread (through an adapter), or a thread against any custom agent you build. Authentication happens inside the editor, so there is no external setup to bring a coding assistant in. Native assistant features survive the trip: subagents, custom slash commands, and file @-mentions all still work, and edits arrive as in-editor diffs you accept or reject with feedback. Cole calls that last part "the kind of stuff that I've always wanted to have with Claude code," and it is the clearest example in the bundle of an [AI coding UX](../../concepts/ai-coding-ux.md) improving without the agent changing at all.

The payoff is switching cost. Because both threads look and behave identically, moving between assistants stops being a migration, which matters as "Cloud code is becoming less and less of an obvious winner." That is [provider independence](../../concepts/provider-independence.md) delivered at the editor layer instead of the SDK layer, and it also makes running many agents [in parallel](../../concepts/parallel-agentic-coding.md) easier. Cole is candid that the implementation is beta: threads occasionally hang while connecting, and thread history does not persist. He argues the design outlives the bugs, since Zed borrowed openly from [MCP](../../concepts/mcp.md) and the decade-old [Language Server Protocol](../../concepts/language-server-protocol.md), so whatever standard wins "is going to look a lot like ACP." He expects [VS Code](./vs-code.md) to follow, and has sketched connecting [Archon](./archon.md) as a custom ACP agent.

## Realizes

- [Agent Client Protocol (ACP)](../../concepts/agent-client-protocol.md) - An open standard for connecting any coding agent to any code editor, the agent-to-editor analog of MCP.
- [AI Coding Assistant UX Patterns](../../concepts/ai-coding-ux.md) - Interaction patterns of coding assistants: streamed code output, inline vs manual suggestions, and schema inference from a name.

## Works with

- [Gemini CLI](./gemini-cli.md) - Google's coding CLI, where subagent support is experimental and which has a direct integration with the Agent Client Protocol.
- [Claude Code](./claude-code.md) - Anthropic's terminal-based agentic coding assistant that is the subject of this complete-guide walkthrough.
- [Archon](./archon.md) - Cole's free, open-source AI command center and harness builder for AI coding; started as an AI agent that builds other AI agents.

## Contrasts with

- [Visual Studio Code](./vs-code.md) - Microsoft's editor where Cole drops LLM-generated Python, fills in placeholders, and runs the app from the integrated terminal.
- [Cursor](./cursor.md) - AI coding assistant that can consume AG-UI's llms.txt docs to help build with the protocol.
- [Windsurf](./windsurf.md) - AI coding IDE Cole used to build the Python AG-UI backend and consume the protocol docs.

## Related

- [Provider Independence](../../concepts/provider-independence.md) - Architecting agents so the underlying model, framework, or client can be swapped without a rewrite, avoiding lock-in through low-level abstractions.
- [Language Server Protocol](../../concepts/language-server-protocol.md) - Using LSP to give agents precise code navigation (definitions, references, symbols) instead of guessing from text.
- [Model Context Protocol (MCP)](../../concepts/mcp.md) - An open protocol for packaging tools, data, and RAG capabilities as servers that any AI coding assistant or agent can connect to and call with a standard interface.
- [Parallel Agentic Coding](../../concepts/parallel-agentic-coding.md) - Dispatching agents to background tasks in isolated git worktrees, each fed repo context and returning a reviewable PR.
- [Open-Source & Local AI Coding](../../concepts/open-source-ai-coding.md) - Community-maintained, self-hostable AI coding tools and local models that dodge API costs and rate limits.
- [The Evolution of AI Coding](../../concepts/the-evolution-of-ai-coding.md) - How AI coding assistants moved from novelty to daily driver, and where the landscape, adoption, and commentary are heading.

## Sources

- [This New Protocol Will Change AI Coding Forever (ACP)](../../sources/this-new-protocol-will-change-ai-coding-forever-acp.md) - "[0:01:22] Zed is a code editor just like VS Code and its forks like Windsurf and Cursor."
- [This New Protocol Will Change AI Coding Forever (ACP)](../../sources/this-new-protocol-will-change-ai-coding-forever-acp.md) - "[0:02:26] all you have to do to get started with ACP is install Zed. That's what we're looking at right here. It's a completely free and open source code editor."
