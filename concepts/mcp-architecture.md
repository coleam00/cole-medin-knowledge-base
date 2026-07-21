---
type: concept
title: "MCP Server & Client Architecture"
description: "The structural foundations of the Model Context Protocol: how servers expose tools to clients, server lifespan and state management, containerized one-click installs, aggregating many servers, and registering tools dynamically."
tags: [mcp, servers, clients, tools, docker, tool-registration]
videos: [claude-mcp-has-changed-ai-forever-heres-what-you-need-to-know, the-ultimate-guide-to-building-your-own-mcp-servers-free-template, docker-just-made-using-mcp-servers-100x-easier-one-click-installs, i-finally-built-an-ai-agent-to-organize-my-life-ai-agents-masterclass-4]
created: 2026-07-21
updated: 2026-07-21
---

# MCP Server & Client Architecture

MCP architecture is a two-sided design: servers expose tools, clients consume them. "Instead of having to Define all of those individual tools and functions we have these services that our MCP servers expose that communicate all these tools to our AI agent." [0:05:36] You can build either half or both: "we can create our own servers to package our own tools and we can also create our own clients so we can build AI agents with Frameworks like Pydantic AI that can leverage MCP servers." [0:14:31] This clean split is what lets one [MCP](./mcp.md) server serve many different clients.

**Server lifespan is the load-bearing detail most implementations get wrong.** "We want to define the lifespan for our MCP server. I see a lot of MCP servers missing this. It is a very core concept." [0:15:53] The point is to create expensive resources once and reuse them: "For the whole life cycle, we want to define the client once and then never have to redefine it again" [0:16:27], which Cole compares to "the singleton pattern as well." [0:16:59] A database connection or API client is opened at startup, shared across every tool call, and torn down at shutdown.

**Tools are registered dynamically, and their docstrings do the heavy lifting.** A client "dynamically fetch[es] all the tools that are available through this mapping and then we bind that into our chatbot so it's so nice how easy is to add these tools." [0:10:55] The work is in describing them: "All of the work really goes into creating these functions and then defining the dock string in a way that allows the AI to understand properly when and how to use these functions." [0:11:12] See [docstrings as tool descriptions](./docstrings-as-tool-descriptions.md) for why that prose is effectively the tool's interface.

**Containerization gives isolation and on-demand execution.** With Docker's catalog, "all of these tools that we add, they run as Docker containers. So whenever our client... requests to use a tool... that actually quickly spins up a container to perform that tool action and then once the tool is done running, it immediately spins the container down." [0:07:29] The container runs only during the call, so it is "extremely efficient and secure." [0:08:01] An aggregation layer hides the sprawl: "this single server is basically aggregating all the tools from all the MCPs that we have selected in the catalog... we're going to just see it still as a single server in our client just with all the tools from all of our different servers." [0:07:14] Building a server yourself means designing against these same primitives, covered in [build your own MCP server](./build-your-own-mcp-server.md).

## Part of

- [Model Context Protocol (MCP)](./mcp.md) - the protocol whose internal structure this page details.

## Related

- [Build Your Own MCP Server](./build-your-own-mcp-server.md) - applying lifespan, registration, and transport choices in practice.
- [Docstrings as Tool Descriptions](./docstrings-as-tool-descriptions.md) - the docstrings that tell the client when to call each tool.
- [Tool Design](./tool-design.md) - shaping tools clients can use reliably.
- [Tool Use](./tool-use.md) - how the LLM actually invokes the registered tools.

## Tools

- [MCP](../entities/tools/mcp.md) - the server and client protocol described here.
- [Docker](../entities/tools/docker.md) - containerized, on-demand tool execution and server aggregation.

## Sources

- [Claude MCP has Changed AI Forever - Here's What You NEED to Know](../sources/claude-mcp-has-changed-ai-forever-heres-what-you-need-to-know.md) - "[0:14:31] we can create our own servers to package our own tools and we can also create our own clients so we can build AI agents with Frameworks like Pydantic AI that can leverage MCP servers"
- [The ULTIMATE Guide to Building Your Own MCP Servers (Free Template)](../sources/the-ultimate-guide-to-building-your-own-mcp-servers-free-template.md) - "[0:15:53] We want to define the lifespan for our MCP server. I see a lot of MCP servers missing this. It is a very core concept."
- [Docker Just Made Using MCP Servers 100x Easier (One Click Installs!)](../sources/docker-just-made-using-mcp-servers-100x-easier-one-click-installs.md) - "[0:07:29] All of these tools that we add, they run as Docker containers. So whenever our client... requests to use a tool... that actually quickly spins up a container to perform that tool action and then once the tool is done running, it immediately spins the container down."
- [I FINALLY Built an AI Agent to Organize my Life - AI Agents Masterclass #4](../sources/i-finally-built-an-ai-agent-to-organize-my-life-ai-agents-masterclass-4.md) - "[0:11:12] All of the work really goes into creating these functions and then defining the dock string in a way that allows the AI to understand properly when and how to use these functions"
