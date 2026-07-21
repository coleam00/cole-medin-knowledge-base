---
type: entity
subtype: tool
title: "FastMCP"
description: "Anthropic's high-level Python interface in the MCP SDK for spinning up an MCP server in one line (name, description, lifespan, host, port) and registering tools with the @mcp.tool decorator."
tags: [mcp, protocol, python, sdk, server]
videos: [the-ultimate-guide-to-building-your-own-mcp-servers-free-template]
created: 2026-07-21
updated: 2026-07-21
---

# FastMCP

FastMCP is the high-level Python class inside Anthropic's MCP SDK that turns "build an MCP server" into a handful of lines. Cole's framing is exactly that: "You just pip install MCP and then you can import fast MCP which is Anthropic's very easy for way for you to spin up a server" ([0:11:38](../../sources/the-ultimate-guide-to-building-your-own-mcp-servers-free-template.md)). You install one package, import one class, decorate your functions, and you have a server any [MCP](./mcp.md) client can connect to.

In the best-practices Python template he ships (a [Mem0](./mem0.md) long-term-memory server), FastMCP is component two of three. Component one is a lifespan that instantiates a single shared client for the whole process, singleton style, and cleans it up gracefully. FastMCP takes that lifespan as a constructor argument alongside the server's identity and network binding: "After the lifespan, now we can instantiate our fast MCP server... we're giving it a name and description. We're defining the lifespan here" ([0:17:26](../../sources/the-ultimate-guide-to-building-your-own-mcp-servers-free-template.md)). Name and description are what a client shows the model; the lifespan context is what every tool receives so nothing re-opens a connection per call.

Component three is `@mcp.tool`, and this is where FastMCP quietly enforces good [tool design](../../concepts/tool-design.md): the decorated function's docstring becomes the tool description the LLM reads to decide when and how to call it, so the docstring is prompt engineering, not documentation. The template's three tools (save-memory, get-all-memories, search-memories) are deliberately few and single-purpose for that reason.

Because the same FastMCP instance runs over either transport, one server covers local and remote use: stdio when the client launches it as a same-machine subprocess, SSE or streamable HTTP when it must be hosted for clients like [n8n](./n8n.md), toggled by an environment variable. Cole proves the payoff by pointing [Claude Desktop](./claude-desktop.md), a custom Pydantic AI agent, and n8n at the identical server, shipped as a [Docker](./docker.md) image.

## Realizes

- [Build Your Own MCP Server](../../concepts/build-your-own-mcp-server.md) - Standing up custom MCP servers to expose your own tools to any client over a standard transport.
- [MCP Server & Client Architecture](../../concepts/mcp-architecture.md) - Server lifespan and shared state, tool registration, and how servers expose capabilities to clients.
- [Docstrings as Tool Descriptions](../../concepts/docstrings-as-tool-descriptions.md) - The `@mcp.tool` docstring is literally the description the model reads before calling.

## Contrasts with

- [FastAPI](./fastapi.md) - The general-purpose Python web framework you drop to when you want to hand-serve the endpoint instead of letting FastMCP own the server.

## Works with

- [MCP (Model Context Protocol)](./mcp.md) - The protocol FastMCP implements; `pip install mcp` is the same package.
- [Python](./python.md) - The language the SDK and the template are written in.
- [Mem0](./mem0.md) - The memory library wrapped by the template's three tools.
- [Docker](./docker.md) - How the finished server is packaged and run.
- [Claude Desktop](./claude-desktop.md) - Client used to verify a custom server behaves like an official one.
- [n8n](./n8n.md) - Client that only speaks SSE, which is why the server supports both transports.

## Related

- [MCP Transports](../../concepts/mcp-transports.md) - stdio versus SSE and streamable HTTP, and why a single server should support both.
- [Model Context Protocol (MCP)](../../concepts/mcp.md) - The standard interface that makes any of these tools reusable across clients.
- [Tool Design](../../concepts/tool-design.md) - Few, single-purpose, well-described tools so the model calls them reliably.
- [Remote MCP Server](../../concepts/remote-mcp-server.md) - Hosting the same server in the cloud behind a production URL.
- [Docs and Templates as Coding-Assistant Context](../../concepts/docs-as-agent-context.md) - Feeding the MCP llms.txt plus this template to an assistant so it builds servers from real context.

## Sources

- [The ULTIMATE Guide to Building Your Own MCP Servers (Free Template)](../../sources/the-ultimate-guide-to-building-your-own-mcp-servers-free-template.md) - "[0:11:38] You just pip install MCP and then you can import fast MCP which is Anthropic's very easy for way for you to spin up a server."
- [The ULTIMATE Guide to Building Your Own MCP Servers (Free Template)](../../sources/the-ultimate-guide-to-building-your-own-mcp-servers-free-template.md) - "[0:17:26] After the lifespan, now we can instantiate our fast MCP server... we're giving it a name and description. We're defining the lifespan here."
