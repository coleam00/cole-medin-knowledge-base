---
type: concept
title: "Agent Client Protocol (ACP)"
description: "An open standard for connecting any coding agent to any code editor, the agent-to-editor analog of MCP."
tags: [ai-coding, protocols, interoperability]
videos: [this-new-protocol-will-change-ai-coding-forever-acp]
created: 2026-07-21
updated: 2026-07-21
---

# Agent Client Protocol (ACP)

The Agent Client Protocol is an open standard for wiring any coding agent into any code editor. "Zed has just introduced the agent client protocol or ACP for short. It's a standard just like MCP, but for connecting any coding assistant to any code editor." [0:00:00] Where [MCP](./mcp.md) standardizes how an agent reaches tools, ACP standardizes how an editor reaches an agent, closing the other side of the loop.

The payoff is portability. "The standard like I said for connecting any coding agent to any code editor and this is just such a gamecher. It makes it so easy to switch between coding assistants." [0:01:37] Instead of every editor building a bespoke integration for every agent, both sides implement one protocol and interoperate. That decoupling is exactly the [provider independence](./provider-independence.md) that keeps you from being locked to a single vendor's IDE or agent.

Because ACP is a standard, it also opens the door to custom agents. "Since ACP is a standard, we're able to create our own custom agents that we can attach as coding agents into any editor, just like with MCP, we're able to build tools that we can connect into any agent." [0:00:49] The plumbing is a message-format translation, not a rewrite. To connect Claude Code to Zed, "all we have to do to connect Claude Code to any editor through ACP is we need to convert any of our Claude Code SDK messages into the format, the JSON format needed for the ACP standard." [0:14:50] The resulting adapter "for Claude Code to zed thanks to ACP is only around 600 lines of code. It's so simple." [0:15:27]

## Part of

- [Agent Protocols](./agent-protocols.md) - ACP is one of the emerging interoperability standards in the agent-protocol family.

## Related

- [Model Context Protocol (MCP)](./mcp.md) - the direct analog; ACP connects editors to agents, MCP connects agents to tools.
- [Language Server Protocol](./language-server-protocol.md) - the older editor-standardization pattern ACP echoes for agents.
- [Provider Independence](./provider-independence.md) - the freedom to swap agents and editors that ACP enables.

## Tools

- [Claude Code](../entities/tools/claude-code.md) - bridged into Zed through a ~600-line ACP adapter over the Claude Agent SDK.

## Sources

- [This New Protocol Will Change AI Coding Forever (ACP)](../sources/this-new-protocol-will-change-ai-coding-forever-acp.md) - "[0:00:00] Zed has just introduced the agent client protocol or ACP for short. It's a standard just like MCP, but for connecting any coding assistant to any code editor."
- [This New Protocol Will Change AI Coding Forever (ACP)](../sources/this-new-protocol-will-change-ai-coding-forever-acp.md) - "[0:15:27] this full adapter for Claude Code to zed thanks to ACP is only around 600 lines of code. It's so simple"
