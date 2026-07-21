---
type: entity
subtype: tool
title: "Docker MCP Toolkit"
description: "Docker Desktop's MCP feature set: a curated catalog of hundreds of servers, a toolkit that runs each tool as an ephemeral container, and an open-source gateway for orchestrating them."
resource: "https://hub.docker.com/mcp"
tags: [mcp, docker, tooling]
videos: [docker-just-made-using-mcp-servers-100x-easier-one-click-installs]
created: 2026-07-21
updated: 2026-07-21
---

# Docker MCP Toolkit

The Docker MCP Toolkit is [Docker](./docker.md) Desktop's built-in system for finding, installing, and running [MCP](./mcp.md) servers, and it exists to delete the single worst part of MCP adoption: hunting through registries and hand-editing JSON config files. It has three pieces. The catalog is the storefront: "the Docker MCP catalog. This is what I want to show you today... It is a beautifully curated list of all of these MCP servers and with a single click of a button I can connect them" [0:01:30]. The toolkit is the runtime that actually executes the tools. The gateway is the open-source layer underneath: "The MCP gateway is Docker's open-source enterprise ready solution for orchestrating and managing MCP servers" [0:18:03]. At the time of recording the toolkit is behind a flag: "when you are working with the MCP toolkit, which is in beta, you might need to go to your Docker settings... and go to beta features and enable it" [0:04:11].

The runtime detail is what makes it more than a package manager. Each MCP tool runs as an ephemeral container that spins up on a tool call and disappears immediately after, so connecting a hundred servers costs no standing memory. That is [containerization](../../concepts/containerization.md) applied to the tool layer, and it is a direct answer to one of the [problems with MCP servers](../../concepts/mcp-problems.md): the client side stays lean because everything is aggregated behind a single `MCP_DOCKER` server entry rather than a sprawling list of processes.

Installation writes the client config for you. One click wires a server into [Claude Desktop](./claude-desktop.md), [Claude Code](./claude-code.md), or [Gemini CLI](./gemini-cli.md), and [Ask Gordon](./ask-gordon.md) inside Docker Desktop serves as an immediate smoke test before any external client is involved. Cole's payoff demo chains four servers (YouTube transcripts, [Obsidian](./obsidian.md), [Slack](./slack.md), [GitHub](./github.md)) into one request that researches a topic, files an issue on [Archon](./archon.md), and triggers a coding agent to open a pull request, which is [agentic workflow engineering](../../concepts/agentic-workflow-engineering.md) assembled in about ten minutes.

You are not confined to the preconfigured client list either. The gateway can be built from source and run on a port with streamable HTTP, exposing the same curated registry to any custom agent. Cole demonstrates that from an [n8n](./n8n.md) agent and from a Python [LiveKit](./livekit.md) voice agent, both talking to one shared set of servers.

## Realizes

- [MCP Server & Client Architecture](../../concepts/mcp-architecture.md) - The structural foundations of the Model Context Protocol: how servers expose tools to clients, server lifespan and state management, containerized one-click installs, aggregating many servers, and registering tools dynamically.
- [Containerization & Docker Networking](../../concepts/containerization.md) - Running each service and your own agent as Docker containers in one stack so they communicate over a private network by service name.

## Works with

- [Docker](./docker.md) - The containerization platform the catalog, toolkit, and gateway all ship inside.
- [MCP (Model Context Protocol)](./mcp.md) - The protocol the whole toolkit packages and distributes.
- [Ask Gordon](./ask-gordon.md) - The AI agent built into Docker Desktop and wired to the MCP Toolkit by default, useful as a quick smoke test for MCP servers.
- [Claude Desktop](./claude-desktop.md) - A one-click connection target whose config Docker updates automatically.
- [Claude Code](./claude-code.md) - Anthropic's terminal-based agentic coding assistant, another supported client.
- [Gemini CLI](./gemini-cli.md) - Google's coding CLI, also connectable in one click.
- [n8n](./n8n.md) - A no-code AI automation platform whose agents reach the gateway over host.docker.internal.
- [LiveKit](./livekit.md) - Open-source Python voice-agent framework; Cole's voice agent queries the same curated servers through the gateway.

## Related

- [Sequential Thinking MCP Server](./sequential-thinking-mcp.md) - A stdio MCP server that instructs a model to reason step by step, used to buy extra thinking tokens and attached to custom Claude Agent SDK agents via JSON config.
- [Model Context Protocol (MCP)](../../concepts/mcp.md) - An open protocol for packaging tools, data, and RAG capabilities as servers that any AI coding assistant or agent can connect to and call with a standard interface.
- [The Problems With MCP Servers](../../concepts/mcp-problems.md) - MCP's practical failure modes, tool overload and context/token bloat that overwhelm LLMs, JSON setup friction, and early production gaps.
- [MCP Transports](../../concepts/mcp-transports.md) - The ways an MCP client and server talk: stdio, where the client launches the server as a fast local subprocess, versus SSE and its successor streamable HTTP for remote servers.
- [Remote MCP Server](../../concepts/remote-mcp-server.md) - An MCP server hosted in the cloud rather than run locally, making tool access scalable, shareable, and deployable behind a production URL.
- [Tool Standardization (USB-C for AI)](../../concepts/tool-standardization.md) - MCP standardizes how tools are exposed to LLMs, so the same tools can be reused identically across any agent framework or host.
- [Agentic Workflow Engineering](../../concepts/agentic-workflow-engineering.md) - Designing repeatable AI workflows as engineered systems with defined steps, orchestration, and background execution rather than ad-hoc prompting.

## Sources

- [Docker Just Made Using MCP Servers 100x Easier (One Click Installs!)](../../sources/docker-just-made-using-mcp-servers-100x-easier-one-click-installs.md) - "[0:01:30] the Docker MCP catalog. This is what I want to show you today... It is a beautifully curated list of all of these MCP servers and with a single click of a button I can connect them"
- [Docker Just Made Using MCP Servers 100x Easier (One Click Installs!)](../../sources/docker-just-made-using-mcp-servers-100x-easier-one-click-installs.md) - "[0:04:11] when you are working with the MCP toolkit, which is in beta, you might need to go to your Docker settings... and go to beta features and enable it."
- [Docker Just Made Using MCP Servers 100x Easier (One Click Installs!)](../../sources/docker-just-made-using-mcp-servers-100x-easier-one-click-installs.md) - "[0:18:03] The MCP gateway is Docker's open-source enterprise ready solution for orchestrating and managing MCP servers."
