---
type: concept
title: "MCP Transports"
description: "The ways an MCP client and server talk: stdio, where the client launches the server as a fast local subprocess, versus SSE and its successor streamable HTTP for remote servers."
tags: [mcp, transport, http, stdio, sse]
videos: [build-and-ship-any-mcp-server-in-minutes-full-guide, the-ultimate-guide-to-building-your-own-mcp-servers-free-template]
created: 2026-07-21
updated: 2026-07-21
---

# MCP Transports

A transport is the wire an MCP client and server talk over, and there are two families. With the local one, "with standard IO... your client is actually going to start an instance of the server kind of as a subprocess... It's very fast." [0:22:10] There is no network hop, no port, and no hosting: the client owns the server process for the life of the session. The remote family runs the server somewhere else and speaks HTTP to it, first through SSE and now through streamable HTTP, which Anthropic added because it is "a new transport for the protocol that actually scales." [0:01:08]

Choosing one is not a detail, and it is the thing most implementations get wrong: "Most MCP servers don't understand this very well from what I've seen. They usually only make the server work with one of these different transport types, but both are important for different purposes." [0:21:05] The right default is to support both and toggle with an environment variable, because clients differ in what they accept - some tools only ever spoke SSE - and because the server's local and hosted lives have opposite needs. A production build exposes both endpoints side by side: "also /mcp just the regular.serve. This is for streamable HTTP the new transport that we have." [0:07:42] SSE stays mounted for legacy clients, which is exactly how Cole frames it: "we'll be supporting the new streamable HTTP transport layer and then for legacy purposes supporting SSE." [0:02:50]

Stdio wins on latency and simplicity for anything colocated with the client, such as a developer's coding assistant reading local files. HTTP is what makes the server a product: "this is very important if you want to not just have your MCP server running on the exact same machine as your client... the direction we're heading with MCP servers is everyone wants to run them remotely to monetize them." [0:22:42] The moment the transport becomes remote, everything else in the production checklist follows - identity, rate limits, monitoring - because the server is now a public API rather than a subprocess.

## Prerequisites

- [Model Context Protocol (MCP)](./mcp.md) - the protocol these transports carry.

## Part of

- [MCP Server & Client Architecture](./mcp-architecture.md) - transport is the third structural component after lifespan and tool registration.

## Implemented by

- [Build Your Own MCP Server](./build-your-own-mcp-server.md) - supporting both transports behind an environment-variable toggle.
- [Remote MCP Server](./remote-mcp-server.md) - the hosted deployment that HTTP transports exist to enable.

## Contrasts with

- [MCP Authentication with OAuth](./mcp-oauth.md) - the security layer a remote transport forces and a local subprocess never needs.

## Tools

- [FastMCP](../entities/tools/fastmcp.md) - the Python server framework where host, port, and transport are configured.
- [MCP (Model Context Protocol)](../entities/tools/mcp.md) - the protocol and its SDKs.
- [Docker](../entities/tools/docker.md) - packaging a server so it can run locally or hosted without code changes.
- [n8n](../entities/tools/n8n.md) - a client that historically only supported SSE, the reason to keep it mounted.
- [Claude Desktop](../entities/tools/claude-desktop.md) - a client that launches stdio servers as subprocesses.
- [Sequential Thinking MCP Server](../entities/tools/sequential-thinking-mcp.md) - A stdio MCP server that instructs a model to reason step by step, used to buy extra thinking tokens and attached to custom Claude Agent SDK agents via JSON config.
- [ngrok](../entities/tools/ngrok.md) - Tunneling tool that exposes a local dev server on a public HTTPS URL so third-party webhooks (here ChargeBee's) can reach a local endpoint during development.

## Related

- [Streaming Responses](./streaming-responses.md) - why the HTTP transports stream rather than return one blob.
- [Agent Deployment](./agent-deployment.md) - hosting decisions that follow from choosing HTTP.
- [The Problems With MCP Servers](./mcp-problems.md) - the early absence of a scalable remote transport.
- [MCP with Custom Agents](./mcp-with-custom-agents.md) - your own agent acting as the client on either transport.
- [Containerization & Docker Networking](./containerization.md) - the localhost-versus-container gotchas a transport choice exposes.

## Sources

- [The ULTIMATE Guide to Building Your Own MCP Servers (Free Template)](../sources/the-ultimate-guide-to-building-your-own-mcp-servers-free-template.md) - "[0:21:05] Most MCP servers don't understand this very well from what I've seen. They usually only make the server work with one of these different transport types, but both are important for different purposes."
- [The ULTIMATE Guide to Building Your Own MCP Servers (Free Template)](../sources/the-ultimate-guide-to-building-your-own-mcp-servers-free-template.md) - "[0:22:10] With standard IO... your client is actually going to start an instance of the server kind of as a subprocess... It's very fast."
- [The ULTIMATE Guide to Building Your Own MCP Servers (Free Template)](../sources/the-ultimate-guide-to-building-your-own-mcp-servers-free-template.md) - "[0:22:42] This is very important if you want to not just have your MCP server running on the exact same machine as your client... the direction we're heading with MCP servers is everyone wants to run them remotely to monetize them."
- [Build and Ship Any MCP Server in MINUTES (Full Guide)](../sources/build-and-ship-any-mcp-server-in-minutes-full-guide.md) - "[0:01:08] They have streamable HTTP as a new transport for the protocol that actually scales."
- [Build and Ship Any MCP Server in MINUTES (Full Guide)](../sources/build-and-ship-any-mcp-server-in-minutes-full-guide.md) - "[0:02:50] Also, we'll be supporting the new streamable HTTP transport layer and then for legacy purposes supporting SSE."
- [Build and Ship Any MCP Server in MINUTES (Full Guide)](../sources/build-and-ship-any-mcp-server-in-minutes-full-guide.md) - "[0:07:42] And then also /mcp just the regular.serve. This is for streamable HTTP the new transport that we have."
