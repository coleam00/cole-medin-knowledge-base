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

Claude Desktop is Anthropic's desktop chat application, and in Cole's videos it is both his everyday LLM scratchpad and the canonical [MCP](../../concepts/mcp.md) client he demos servers against. As a general tool he keeps it open for thinking out loud: "Starting with Claude Desktop. This is my go-to application just to quickly have conversations with an LLM," and elsewhere "I love using Cloud Desktop just to generally brainstorm ideas with an LLM." That low-friction chat surface is the baseline before any tooling gets attached.

Its more technical role is as the reference host for [Model Context Protocol](../../concepts/mcp.md) servers. When Cole walks through [building your own MCP server](../../concepts/build-your-own-mcp-server.md), Claude Desktop is where he proves it works: "I'll even show you an example right now with cloud desktop ... you can see that I have the math MCP server with my calculate tool." The wiring is a settings edit plus a bridge command: "with claw desktop ... if you go to the top left click on file and then settings you can go to the developer tab and then edit your configuration," and to reach a remote streamable-HTTP server "we just do npxmcp remote and then it is going to be our localhost 8789." That configuration shape is portable, the same pattern he then applies to custom agents: "the way that you configure your mCP servers is exactly the same way that you would do it for another application like CLA desktop."

That portability is exactly why Claude Desktop also illustrates the limits of native MCP clients. Cole notes "it's pretty limiting when you have to use applications that natively support mCP like claw desktop wind surf or cursor," which is his motivation for [MCP with custom agents](../../concepts/mcp-with-custom-agents.md) that aren't boxed into a vendor app. In the Docker one-click-install video it doubles as the client that triggers containerized tools on demand: "whenever our client like Claw Desktop requests to use a tool ... that actually quickly spins up a container." It even hosts Anthropic's own skill-creator, letting you "go to file settings and then capabilities ... scroll all the way down to skills" to build skills you later port to any agent.

## Related

- [Model Context Protocol (MCP)](../../concepts/mcp.md) - the reference client for connecting to MCP servers.
- [Build Your Own MCP Server](../../concepts/build-your-own-mcp-server.md) - where Cole demos and verifies servers he builds.
- [MCP Server & Client Architecture](../../concepts/mcp-architecture.md) - configured as the client half via developer settings and mcp-remote.
- [The Problems With MCP Servers](../../concepts/mcp-problems.md) - its native-only support illustrates the vendor-lock-in limitation.
- [MCP with Custom Agents](../../concepts/mcp-with-custom-agents.md) - the pattern Cole reaches for beyond native clients.
- [Context Engineering](../../concepts/context-engineering.md) - a brainstorming surface for shaping prompts and context.
- [Provider Independence](../../concepts/provider-independence.md) - the config pattern ports to non-Anthropic clients.
- [Cursor](./cursor.md) and [Windsurf](./windsurf.md) - the other native MCP clients he names alongside it.

## Sources

- [How I'd Learn AI Agents FAST if I Had to Start Over (Full Roadmap)](../../sources/how-id-learn-ai-agents-fast-if-i-had-to-start-over-full-roadmap.md) - "[0:03:32] Starting with Claude Desktop. This is my go-to application just to quickly have conversations with an LLM."
- [Build and Ship Any MCP Server in MINUTES (Full Guide)](../../sources/build-and-ship-any-mcp-server-in-minutes-full-guide.md) - "[0:08:18] I'll even show you an example right now with cloud desktop. So, I've got my cloud desktop up. You can see that I have the math MCP server with my calculate tool."
- [Claude MCP has Changed AI Forever - Here's What You NEED to Know](../../sources/claude-mcp-has-changed-ai-forever-heres-what-you-need-to-know.md) - "[0:12:12] with claw desktop for example the way that you can set up these servers if you go to the top left click on file and then settings you can go to the developer tab and then edit your configuration"
- [The MCP Integration EVERYONE is Sleeping On (MCP + Custom AI Agents)](../../sources/the-mcp-integration-everyone-is-sleeping-on-mcp-custom-ai-agents.md) - "[0:00:21] it's pretty limiting when you have to use applications that natively support mCP like claw desktop wind surf or cursor"
- [Docker Just Made Using MCP Servers 100x Easier (One Click Installs!)](../../sources/docker-just-made-using-mcp-servers-100x-easier-one-click-installs.md) - "[0:07:43] whenever our client like Claw Desktop requests to use a tool like to get a transcript, that actually quickly spins up a container"
- [The ULTIMATE Guide to Building Your Own MCP Servers (Free Template)](../../sources/the-ultimate-guide-to-building-your-own-mcp-servers-free-template.md) - "[0:03:03] We can go to our cloud desktop and then follow those instructions to set up our configuration."
- [Claude Skills Aren't Just for Claude - Here's How to Build Them for ANY Agent](../../sources/claude-skills-arent-just-for-claude-heres-how-to-build-them-for-any-agent.md) - "[0:17:54] you just go to file settings and then capabilities. You scroll all the way down to skills, go to example skills, and you can toggle on the skill creator."
