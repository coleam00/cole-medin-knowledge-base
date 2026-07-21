---
type: concept
title: "MCP with Custom Agents"
description: "Integrating MCP servers directly into agents you build yourself, so you control the front end, tool selection, and how the tools are used."
tags: [mcp, tools, integration, custom-agents]
videos: [the-mcp-integration-everyone-is-sleeping-on-mcp-custom-ai-agents]
created: 2026-07-21
updated: 2026-07-21
---

# MCP with Custom Agents

MCP with custom agents is the practice of wiring [MCP](./mcp.md) servers into agents you build yourself, rather than only consuming them through hosted clients like Claude Desktop or Cursor. "The true power comes in building our own AI agents you and I both know that but how do we integrate mCP servers with our own agents so we can use these tools for ourselves." [0:00:21] Answering that question is the integration many people overlook: the same standard that lets a vendor's client call tools also lets your own application act as the MCP client.

The reason to do it is control. Owning the client means owning everything around the tools: "because then we can build our own front ends and apps we can integrate mCP servers with other tools that we built for our agent we can even pick and choose the different tools that we pull from these servers." [0:00:39] You are not stuck with whatever tool surface a hosted app exposes. You can combine MCP tools with your own custom tools, select only the subset of a server's tools you actually want, and present them through any interface you build. Pulling a curated subset is also one concrete defense against the tool-overload described in [the problems with MCP servers](./mcp-problems.md).

Mechanically the integration follows the client side of [MCP architecture](./mcp-architecture.md): initialize a session with the server, list its tools, and adapt each tool's schema so your agent knows its parameters. Because MCP is a standard rather than a vendor lock-in, this is the same portability story as [provider independence](./provider-independence.md): connect the same server to any framework or model you choose, and keep the freedom to swap them later.

## Builds on

- [Model Context Protocol (MCP)](./mcp.md) - the protocol whose client side your custom agent implements.
- [MCP Server & Client Architecture](./mcp-architecture.md) - the session-init, list-tools, and schema-binding flow the integration follows.

## Related

- [Provider Independence](./provider-independence.md) - keeping tool integrations portable across frameworks and models.
- [Build Your Own MCP Server](./build-your-own-mcp-server.md) - the complementary skill of owning the server side too.
- [The Problems With MCP Servers](./mcp-problems.md) - why cherry-picking only the tools you need matters.

## Tools

- [MCP](../entities/tools/mcp.md) - the servers your custom agent connects to as a client.
- [Pydantic AI](../entities/tools/pydantic-ai.md) - a framework for building the custom agent that leverages MCP servers.

## Sources

- [The MCP Integration EVERYONE is Sleeping On (MCP + Custom AI Agents)](../sources/the-mcp-integration-everyone-is-sleeping-on-mcp-custom-ai-agents.md) - "[0:00:21] the true power comes in building our own AI agents you and I both know that but how do we integrate mCP servers with our own agents so we can use these tools for ourselves"
- [The MCP Integration EVERYONE is Sleeping On (MCP + Custom AI Agents)](../sources/the-mcp-integration-everyone-is-sleeping-on-mcp-custom-ai-agents.md) - "[0:00:39] because then we can build our own front ends and apps we can integrate mCP servers with other tools that we built for our agent we can even pick and choose the different tools that we pull from these servers"
