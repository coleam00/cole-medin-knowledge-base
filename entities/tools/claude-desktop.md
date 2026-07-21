---
type: entity
subtype: tool
title: "Claude Desktop"
description: "The MCP client used to demo connecting to the server, configured via developer settings and mcp-remote pointed at the streamable HTTP endpoint."
resource: "https://claude.ai/download"
tags: [mcp-client, anthropic]
videos: [claude-skills-arent-just-for-claude-heres-how-to-build-them-for-any-agent, docker-just-made-using-mcp-servers-100x-easier-one-click-installs, build-and-ship-any-mcp-server-in-minutes-full-guide, how-id-learn-ai-agents-fast-if-i-had-to-start-over-full-roadmap, the-ultimate-guide-to-building-your-own-mcp-servers-free-template, the-mcp-integration-everyone-is-sleeping-on-mcp-custom-ai-agents, claude-mcp-has-changed-ai-forever-heres-what-you-need-to-know]
created: 2026-07-21
updated: 2026-07-21
---

# Claude Desktop

Claude Desktop is Anthropic's desktop chat application, and in Cole's videos it is both his everyday LLM scratchpad and the canonical [MCP](../../concepts/mcp.md) client he demos servers against. As a general tool he keeps it open for thinking out loud: "Starting with Claude Desktop. This is my go-to application just to quickly have conversations with an LLM," and elsewhere "I love using Claude Desktop just to generally brainstorm ideas with an LLM." That low-friction chat surface is the baseline before any tooling gets attached.

Its more technical role is as the reference host for [Model Context Protocol](../../concepts/mcp.md) servers. When Cole walks through [building your own MCP server](../../concepts/build-your-own-mcp-server.md), Claude Desktop is where he proves it works: "I'll even show you an example right now with Claude Desktop ... you can see that I have the math MCP server with my calculate tool." The wiring is a settings edit plus a bridge command: "with Claude Desktop ... if you go to the top left click on file and then settings you can go to the developer tab and then edit your configuration," and to reach a remote streamable-HTTP server "we just do npxmcp remote and then it is going to be our localhost 8789." That configuration shape is portable, the same pattern he then applies to custom agents: "the way that you configure your MCP servers is exactly the same way that you would do it for another application like Claude Desktop."

That portability is exactly why Claude Desktop also illustrates the limits of native MCP clients. Cole notes "it's pretty limiting when you have to use applications that natively support MCP like Claude Desktop Windsurf or cursor," which is his motivation for [MCP with custom agents](../../concepts/mcp-with-custom-agents.md) that aren't boxed into a vendor app. In the Docker one-click-install video it doubles as the client that triggers containerized tools on demand: "whenever our client like Claude Desktop requests to use a tool ... that actually quickly spins up a container." It even hosts Anthropic's own skill-creator, letting you "go to file settings and then capabilities ... scroll all the way down to skills" to build skills you later port to any agent.

## Realizes

- [Model Context Protocol (MCP)](../../concepts/mcp.md) - An open protocol for packaging tools, data, and RAG capabilities as servers that any AI coding assistant or agent can connect to and call with a standard interface.
- [Build Your Own MCP Server](../../concepts/build-your-own-mcp-server.md) - Standing up custom MCP servers (often with LLM help) to expose tools to any client over a standard transport.
- [MCP Server & Client Architecture](../../concepts/mcp-architecture.md) - The structural foundations of the Model Context Protocol: how servers expose tools to clients, server lifespan and state management, containerized one-click installs, aggregating many servers, and registering tools dynamically.
- [The Problems With MCP Servers](../../concepts/mcp-problems.md) - MCP's practical failure modes, tool overload and context/token bloat that overwhelm LLMs, JSON setup friction, and early production gaps like missing built-in auth and security.
- [MCP with Custom Agents](../../concepts/mcp-with-custom-agents.md) - Integrating MCP servers directly into agents you build yourself, so you control the front end, tool selection, and how the tools are used.
- [Context Engineering](../../concepts/context-engineering.md) - The deliberate practice of curating exactly what goes into an LLM's limited context window - system messages, schemas, chat history, and dynamic variables - to avoid overload and keep outputs sharp.
- [Provider Independence](../../concepts/provider-independence.md) - Architecting agents so the underlying model, framework, or client can be swapped without a rewrite, avoiding lock-in through low-level abstractions.

## Contrasts with

- [Cursor](./cursor.md) - AI coding assistant that can consume AG-UI's llms.txt docs to help build with the protocol.
- [Windsurf](./windsurf.md) - AI coding IDE Cole used to build the Python AG-UI backend and consume the protocol docs.

## Sources

- [How I'd Learn AI Agents FAST if I Had to Start Over (Full Roadmap)](../../sources/how-id-learn-ai-agents-fast-if-i-had-to-start-over-full-roadmap.md) - "[0:03:32] Starting with Claude Desktop. This is my go-to application just to quickly have conversations with an LLM."
- [Build and Ship Any MCP Server in MINUTES (Full Guide)](../../sources/build-and-ship-any-mcp-server-in-minutes-full-guide.md) - "[0:08:18] I'll even show you an example right now with Claude Desktop. So, I've got my Claude Desktop up. You can see that I have the math MCP server with my calculate tool."
- [Claude MCP has Changed AI Forever - Here's What You NEED to Know](../../sources/claude-mcp-has-changed-ai-forever-heres-what-you-need-to-know.md) - "[0:12:12] with Claude Desktop for example the way that you can set up these servers if you go to the top left click on file and then settings you can go to the developer tab and then edit your configuration"
- [The MCP Integration EVERYONE is Sleeping On (MCP + Custom AI Agents)](../../sources/the-mcp-integration-everyone-is-sleeping-on-mcp-custom-ai-agents.md) - "[0:00:21] it's pretty limiting when you have to use applications that natively support MCP like Claude Desktop Windsurf or cursor"
- [Docker Just Made Using MCP Servers 100x Easier (One Click Installs!)](../../sources/docker-just-made-using-mcp-servers-100x-easier-one-click-installs.md) - "[0:07:43] whenever our client like Claude Desktop requests to use a tool like to get a transcript, that actually quickly spins up a container"
- [The ULTIMATE Guide to Building Your Own MCP Servers (Free Template)](../../sources/the-ultimate-guide-to-building-your-own-mcp-servers-free-template.md) - "[0:03:03] We can go to our Claude Desktop and then follow those instructions to set up our configuration."
- [Claude Skills Aren't Just for Claude - Here's How to Build Them for ANY Agent](../../sources/claude-skills-arent-just-for-claude-heres-how-to-build-them-for-any-agent.md) - "[0:17:54] you just go to file settings and then capabilities. You scroll all the way down to skills, go to example skills, and you can toggle on the skill creator."
