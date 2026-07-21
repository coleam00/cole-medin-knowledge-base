---
type: source
title: "Docker Just Made Using MCP Servers 100x Easier (One Click Installs!)"
description: "Docker's MCP Catalog, Toolkit, and open-source Gateway turn the painful JSON-config chore of wiring MCP servers into agents into a one-click experience, letting you connect curated tools to any client (or your own custom agents) and chain them into full agentic workflows."
youtube_id: TxlVdB2gmGE
url: https://www.youtube.com/watch?v=TxlVdB2gmGE
slug: docker-just-made-using-mcp-servers-100x-easier-one-click-installs
published: 2025-10-08
duration: "0:23:07"
recency_rank: 64
raw: "../raw/docker-just-made-using-mcp-servers-100x-easier-one-click-installs.md"
tags: [mcp, docker, tooling, workflow]
created: 2026-07-21
updated: 2026-07-21
---

Cole demonstrates the Docker MCP Catalog, a curated, popularity-sorted list of MCP servers built into Docker Desktop that replaces the old friction of hunting through registries and hand-editing JSON configs. With a single click you install a server (YouTube transcripts, Slack, GitHub, Obsidian, Context7, Playwright, Stripe, and hundreds more) and connect it to clients like Claude Desktop, Claude Code, or Gemini CLI, with Docker updating each client's configuration for you. Each MCP tool runs as an ephemeral Docker container that spins up only when a tool is called and spins down immediately after, so no matter how many servers you connect they consume no standing memory. All connected servers are aggregated behind a single "MCP_DOCKER" server in the client, and Docker's built-in Gordon agent lets you smoke-test servers directly inside Docker Desktop.

The payoff is workflow composition. Cole wires Claude Desktop to four MCP servers and issues one request that pulls a YouTube transcript, writes a summary into his Obsidian vault, reads research context from a Slack channel, creates a GitHub issue on the Archon repo, and comments "@claudefix work on this issue" to autonomously kick off a Claude Code agent that opens a pull request. The whole research-to-implementation chain is set up in about ten minutes.

Finally he shows you are not locked into the preconfigured client list: the same connection is powered by the open-source Docker MCP Gateway, which you can build from source and run yourself (for example on port 8089 with HTTP streamable transport). Pointed at your Docker catalog registry, the gateway exposes all your curated servers to any custom agent, which Cole demonstrates from an n8n agent and a Python LiveKit voice agent, both talking to the same set of MCP servers.

## Concepts covered

- [The Problems With MCP Servers](../concepts/mcp-problems.md)
- [Build Your Own MCP Server](../concepts/build-your-own-mcp-server.md)
- [MCP Server & Client Architecture](../concepts/mcp-architecture.md)
- [Agentic Workflow Engineering](../concepts/agentic-workflow-engineering.md)

## Entities

- [Docker](../entities/tools/docker.md)
- [MCP (Model Context Protocol)](../entities/tools/mcp.md)
- [Claude Desktop](../entities/tools/claude-desktop.md)
- [Claude Code](../entities/tools/claude-code.md)
- [Obsidian](../entities/tools/obsidian.md)
- [GitHub](../entities/tools/github.md)
- [Slack](../entities/tools/slack.md)
- [n8n](../entities/tools/n8n.md)
- [Docling](../entities/tools/docling.md)
- [Cole Medin](../entities/people/cole-medin.md)

## Key moments

- **[0:00:00]** Teaser: a 10-minute setup connecting Claude Desktop to YouTube, Obsidian, Slack, and GitHub MCP servers to run research-to-implementation end to end
- **[0:01:14]** Introduces the Docker MCP Catalog as the tool that makes finding/connecting MCP servers 100x easier
- **[0:03:39]** One-click install of the YouTube transcript MCP server from the catalog
- **[0:04:38]** Ask Gordon, Docker Desktop's built-in agent, as a quick way to test MCP servers before connecting external clients
- **[0:06:28]** Connecting servers to Claude Desktop with one click; Docker auto-updates the client config
- **[0:07:29]** Explains MCP tools run as ephemeral Docker containers that spin up per tool call and spin down after
- **[0:12:38]** Composing all four MCP servers into a single agentic workflow request in Claude Desktop
- **[0:15:44]** Workflow result: GitHub issue created on Archon and Claude Code triggered to open a PR
- **[0:17:47]** Reveals the open-source Docker MCP Gateway underneath, usable to connect custom agents
- **[0:19:17]** Running the gateway locally on port 8089 with HTTP streamable transport
- **[0:20:05]** Connecting an n8n agent to the gateway via host.docker.internal:8089
- **[0:21:52]** A Python LiveKit voice agent querying the same curated MCP servers by voice

## Transcript

[Raw transcript](../raw/docker-just-made-using-mcp-servers-100x-easier-one-click-installs.md)
