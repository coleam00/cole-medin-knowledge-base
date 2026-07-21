---
type: entity
subtype: tool
title: "Ask Gordon"
description: "The AI agent built directly into Docker Desktop and wired to the MCP Toolkit by default, useful as a quick smoke test for MCP servers before connecting an external client (though its small model gets overwhelmed by large tool lists)."
tags: [ai-coding, coding-agent]
videos: [docker-just-made-using-mcp-servers-100x-easier-one-click-installs]
created: 2026-07-21
updated: 2026-07-21
---

# Ask Gordon

Ask Gordon is Docker's own chat agent, shipped inside Docker Desktop rather than installed as a separate client: "Gordon is the AI agent that is built directly into Docker Desktop... we can actually test our MCP servers directly within Docker Desktop thanks to Gordon" [0:04:38]. Its distinguishing property is that it is pre-wired to the [Docker MCP Toolkit](./docker-mcp-toolkit.md). Anything you install from the MCP Catalog is immediately callable by Gordon with no JSON config, no client restart, and no extra connection step - which makes it the shortest possible path from "I clicked install" to "did that server actually work?"

That is the role Cole gives it: a **smoke test**, not a daily driver. Before wiring a freshly installed server into [Claude Desktop](./claude-desktop.md) or [Claude Code](./claude-code.md), you can ask Gordon to call one of its tools and confirm the container spins up, the credentials resolve, and the response looks sane. Debugging a broken MCP connection inside a real coding agent is far more expensive, because the failure surfaces as an agent that quietly declines to use the tool.

Gordon's limit is the model behind it. Cole is blunt about the ceiling once you connect a large catalog: "it's not powered by the most powerful LLM. It seems like it's something like Gemini 2.5 Flash or GPT5 Nano. it gets quite overwhelmed with all of these tools" [0:10:59]. This is the tool-list problem in miniature - every connected server pushes more tool definitions into the same context window, and a small model degrades at selection long before a frontier model does. Gordon is therefore best used with a narrow set of servers enabled, testing one at a time, then handed off to a stronger client for real work.

## Realizes

- [Model Context Protocol (MCP)](../../concepts/mcp.md) - Gordon is an MCP client, consuming servers rather than exposing them.
- [What Is an AI Agent](../../concepts/what-is-an-ai-agent.md) - an LLM in a loop with tools, just embedded in a desktop app you already run.

## Works with

- [Docker](./docker.md) - Gordon ships as part of Docker Desktop and runs each MCP tool as an ephemeral container.
- [Docker MCP Toolkit](./docker-mcp-toolkit.md) - the one-click catalog Gordon is connected to by default.
- [MCP (Model Context Protocol)](./mcp.md) - the protocol every server it calls speaks.

## Contrasts with

- [Claude Desktop](./claude-desktop.md) - the stronger MCP client Cole moves to for the actual multi-server workflow.
- [Claude Code](./claude-code.md) - the terminal agent that consumes the same catalog when the work is code.
- [Gemini CLI](./gemini-cli.md) - another client Docker will auto-configure from the same Toolkit.

## Related

- [Context Window Limits](../../concepts/context-window-limits.md) - why a long tool list is what breaks Gordon first.
- [The Problems With MCP Servers](../../concepts/mcp-problems.md) - tool-list bloat and selection failure are the core complaints.
- [Model Selection](../../concepts/model-selection.md) - the small-model tradeoff that makes Gordon fast and free but shallow.
- [Progressive Disclosure](../../concepts/progressive-disclosure.md) - the mitigation: expose few tools at a time instead of everything at once.
- [Tool Design](../../concepts/tool-design.md) - clearer, fewer tools survive a weak model better than many overlapping ones.
- [Containerization & Docker Networking](../../concepts/containerization.md) - the ephemeral-container model underneath every Gordon tool call.

## Sources

- [Docker Just Made Using MCP Servers 100x Easier (One Click Installs!)](../../sources/docker-just-made-using-mcp-servers-100x-easier-one-click-installs.md) - "[0:04:38] Gordon is the AI agent that is built directly into Docker Desktop... we can actually test our MCP servers directly within Docker Desktop thanks to Gordon."
- [Docker Just Made Using MCP Servers 100x Easier (One Click Installs!)](../../sources/docker-just-made-using-mcp-servers-100x-easier-one-click-installs.md) - "[0:10:59] it's not powered by the most powerful LLM. It seems like it's something like Gemini 2.5 Flash or GPT5 Nano. it gets quite overwhelmed with all of these tools"
