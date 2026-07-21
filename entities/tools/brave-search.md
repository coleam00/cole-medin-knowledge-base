---
type: entity
subtype: tool
title: "Brave Search API"
description: "Web search API wired up as the single example tool giving the template agent the ability to search the web."
resource: "https://brave.com/search/api/"
tags: [web-search, mcp, tool]
videos: [the-3-must-have-mcp-servers-for-any-ai-coding-and-how-to-use-them, if-youre-serious-about-building-ai-agents-this-is-your-secret-weapon, this-mcp-server-for-ai-coding-assistants-will-10x-your-productivity, the-ultimate-guide-to-building-your-own-mcp-servers-free-template, build-a-chatgpt-style-app-for-your-n8n-ai-agents-in-minutes, code-100x-faster-with-ai-heres-how-no-hype-full-process, claude-mcp-has-changed-ai-forever-heres-what-you-need-to-know, coding-subagents-the-next-evolution-of-ai-ides, flowise-n8n-the-best-no-code-local-ai-agent-combo]
created: 2026-07-21
updated: 2026-07-21
---

# Brave Search API

Brave Search is the web search API Cole reaches for by default whenever an agent or coding assistant needs to look something up on the internet. As he puts it, "the last server that I use no matter what is one to search the web. And typically I use the Brave MCP server" ([0:03:41]). What sets it apart in his stack is that it is built for LLM consumption rather than human browsing: "It has a very AI ccentric web search summarizing things for AI. The way that it pulls information is just perfect for LLMs" ([0:03:56]). In most of his demos it shows up as the one canonical example tool, the minimal capability he bolts onto an agent so it has "at least one tool here" ([0:11:21]) to prove out the loop.

## How Cole uses it / why it matters

Brave plays two recurring roles across the videos. First, it is Cole's go-to web-search [MCP](../../concepts/mcp.md) server, one of the three servers he installs on essentially every coding assistant, and even when he leads with something else he keeps it as the safety net: "as a fallback, use the Brave MCP server" ([0:07:40]). The appeal is that "the Brave API is very powerful in the way that it actually uses AI under the hood to summarize a bunch of the different web search results" ([0:14:28]), so the model gets pre-digested, high-signal text instead of raw HTML.

Second, it is his default single tool when scaffolding a new agent, the smallest possible capability that makes an agent more than a chatbot. He wires it in explicitly through the tool array: "I have the Brave MCP server defined like this and I add it into my agent through the MCP servers array" ([0:13:33]), and in no-code builds he does the same with a native node, "I'm going to use the brave search API which I absolutely love and so we're going to connect the tool here to the brave search API" ([0:15:16]). Because it is a clean, well-behaved tool, it is ideal for demonstrating [tool calling](../../concepts/mcp-with-custom-agents.md) and the [agent loop](../../concepts/human-in-the-loop.md): in one walkthrough Claude "first it's calling the tool to see what Brave tools are available because it knows that that's for web search" ([0:20:37]), then returns the answer. It is also what powers heavier retrieval workloads, where an agent is "making a ton of web searches based on all the different LLMs" ([0:21:06]).

Brave is a cloud, hosted service. When Cole wants the same web-search capability fully local and private, he swaps it for [SearXNG](./searxng.md) instead.

## Realizes

- [Model Context Protocol (MCP)](../../concepts/mcp.md) - An open protocol for packaging tools, data, and RAG capabilities as servers that any AI coding assistant or agent can connect to and call with a standard interface.
- [MCP with Custom Agents](../../concepts/mcp-with-custom-agents.md) - Integrating MCP servers directly into agents you build yourself, so you control the front end, tool selection, and how the tools are used.

## Contrasts with

- [SearXNG](./searxng.md) - Local, private metasearch engine added for web search (with Redis for caching); kept private since it isn't password protected.
- [grep (command-line search)](./ripgrep.md) - The default CLI search Claude Code uses for agentic navigation; the local counterpart for searching a codebase rather than the web.

## Related

- [Context Engineering](../../concepts/context-engineering.md) - The deliberate practice of curating exactly what goes into an LLM's limited context window to avoid overload and keep outputs sharp.
- [Memory Systems](../../concepts/memory-systems.md) - Giving agents durable short- and long-term memory so conversations, user context, and facts persist across sessions and users.
- [Human in the Loop](../../concepts/human-in-the-loop.md) - Keeping a human as the approver and steerer of agentic work rather than fully automating, so AI augments engineers instead of replacing them.
- [Global Rules](../../concepts/global-rules.md) - Persistent project- or user-level rule files that inject standing context and conventions into every agent run.
- [Local & Self-Hosted AI](../../concepts/local-ai.md) - Running open-weight models on your own hardware or cloud for privacy, cost control, and independence from API providers.

## Sources

- [The 3 MUST Have MCP Servers for Any AI Coding (and How to Use Them)](../../sources/the-3-must-have-mcp-servers-for-any-ai-coding-and-how-to-use-them.md) - "[0:03:41] the last server that I use no matter what is one to search the web. And typically I use the Brave MCP server."
- [The 3 MUST Have MCP Servers for Any AI Coding (and How to Use Them)](../../sources/the-3-must-have-mcp-servers-for-any-ai-coding-and-how-to-use-them.md) - "[0:03:56] It has a very AI ccentric web search summarizing things for AI. The way that it pulls information is just perfect for LLMs."
- [If You're Serious About Building AI Agents, This is Your Secret Weapon](../../sources/if-youre-serious-about-building-ai-agents-this-is-your-secret-weapon.md) - "[0:13:33] I have the Brave MCP server defined like this and I add it into my agent through the MCP servers array."
- [This MCP Server for AI Coding Assistants Will 10x Your Productivity](../../sources/this-mcp-server-for-ai-coding-assistants-will-10x-your-productivity.md) - "[0:07:40] as a fallback, use the Brave MCP server."
- [Code 100x Faster with AI, Here's How (No Hype, FULL Process)](../../sources/code-100x-faster-with-ai-heres-how-no-hype-full-process.md) - "[0:14:28] the Brave API is very powerful in the way that it actually uses AI under the hood to summarize a bunch of the different web search results."
- [Claude MCP has Changed AI Forever - Here's What You NEED to Know](../../sources/claude-mcp-has-changed-ai-forever-heres-what-you-need-to-know.md) - "[0:20:37] first it's calling the tool to see what Brave tools are available because it knows that that's for web search."
- [Flowise + n8n - The BEST No Code + Local AI Agent Combo](../../sources/flowise-n8n-the-best-no-code-local-ai-agent-combo.md) - "[0:13:51] I'm going to use the brave search API which I absolutely love and so we're going to connect the tool here to the brave search API."
- [Build a ChatGPT Style App for Your n8n AI Agents in MINUTES](../../sources/build-a-chatgpt-style-app-for-your-n8n-ai-agents-in-minutes.md) - "[0:11:21] very basic agent. It just has a single tool to search the web with the Brave API just so I can have at least one tool here."
- [The ULTIMATE Guide to Building Your Own MCP Servers (Free Template)](../../sources/the-ultimate-guide-to-building-your-own-mcp-servers-free-template.md) - "[0:02:29] You can click into any of these MCP servers like Brave Search to give our LLM very powerful web search capabilities."
- [Coding Subagents - The Next Evolution of AI IDEs](../../sources/coding-subagents-the-next-evolution-of-ai-ides.md) - "[0:03:18] build me an AI agent using archon that is able to search the web using Brave."
