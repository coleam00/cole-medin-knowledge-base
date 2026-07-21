---
type: concept
title: "Model Context Protocol (MCP)"
description: "An open protocol for packaging tools, data, and RAG capabilities as servers that any AI coding assistant or agent can connect to and call with a standard interface."
tags: [mcp, tools, integration, ai-coding, protocol, agents, fastmcp, monitoring]
videos: [build-and-ship-any-mcp-server-in-minutes-full-guide, the-ultimate-guide-to-building-your-own-mcp-servers-free-template, google-is-quietly-revolutionizing-ai-agents-this-is-huge, claude-mcp-has-changed-ai-forever-heres-what-you-need-to-know, coding-subagents-the-next-evolution-of-ai-ides, the-big-problem-with-mcp-servers-and-the-solution, stripes-coding-agents-ship-1300-prs-every-week-heres-how-they-do-it, everything-you-thought-about-building-ai-agents-is-wrong, claude-codes-real-purpose-its-bigger-than-you-think, the-official-archon-guide-10x-your-ai-coding-workflow, archon-beta-launch-livestream-what-you-missed, knowledge-graphs-in-n8n-are-finally-here, introducing-rag-20-agentic-rag-knowledge-graphs-free-template, all-the-best-rag-strategies-in-one-mcp-for-ai-coding-assistants, the-3-must-have-mcp-servers-for-any-ai-coding-and-how-to-use-them, i-built-the-ultimate-rag-mcp-server-for-ai-coding-better-than-context7, this-mcp-server-for-ai-coding-assistants-will-10x-your-productivity, code-100x-faster-with-ai-heres-how-no-hype-full-process, the-future-of-ai-and-saas-is-agentic-experiences-heres-how-to-build-them, i-love-the-karpathy-llm-wiki-but-it-doesnt-scale-heres-what-does, brand-new-stealth-llm-released-on-openrouter-its-a-beast]
created: 2026-07-21
updated: 2026-07-21
---

# Model Context Protocol (MCP)

The Model Context Protocol is the first open standard for connecting LLMs to external services. "It's the first ever standard for connecting LLMs to your services like Gmail, Slack, GitHub, web search, the list goes on." [0:00:00] Anthropic shipped it in November: "When Anthropic launched the model context protocol last November, it was genuinely impressive. Finally, a way for us to connect our AI agents to our external tools." [0:00:16] The most durable framing is the ports analogy: "it's the USBC port for AI applications that people really started to latch on to the concept of the MCP protocol overall." [0:03:22]

Under the hood MCP is deliberately unglamorous. "It's all just APIs, but repackaged in a standard for AI agents specifically. That's all MCP is. But even though that's all it is, it still is very powerful." [0:06:26] Cole is careful to puncture the hype: "under the hood with MCP AI agents are still using Tools in exactly the same way because in the end the tools that these servers expose are just given as a part of the prompt to the llm" [0:07:16], and warns that the claim MCP "is somehow revolutionary in the way that it provides these capabilities for llms that we never had before... is simply not true." [0:07:31] The value is standardization, not new capability. The protocol also carries lesser-known primitives: "there are some other parts to MCP like resources prompts sampling and Roots... resources you can expose data to your llms that's updated in real time things like files and database records." [0:08:55]

The killer property is one server, many clients. "For the AI coding assistant, it is an MCP server... So super easy to connect this to literally any AI coding assistant" [0:00:34], and "any MCP compatible AI coding assistant can connect to Archon." [0:10:13] That reach powers a whole class of RAG-over-docs servers: "this is an MCP server that's kind of like archon for knowledge retrieval. It gives our AI coding assistant the ability to search through the CopilotKit and AGUI documentation and best practices." [0:09:34] It scales dramatically too, as with "a single stripe MCP server that they call tool shed... it has over 400, actually around 500 MCP tools" [0:08:00], where Stripe uses "MCP tools deterministically here. So, not giving it to an agent, but right within code." [0:07:43]

MCP servers also let you standardize your own tools for reuse. "So instead of defining the tools directly into our agent, we can create them as MCP servers, so they're a lot more reusable" [0:04:48], and even sub-agents can be exposed this way: "you can Define these specialized agents as subagents that work as MCP tools that you can bake into all the popular AI coding assistants." [0:02:15] The same standard reaches [RAG](./rag.md) knowledge graphs, Neon databases, and web search, which is why MCP became the connective tissue of the modern [agentic coding](./agentic-coding.md) stack.

## Part of

- [Agent Protocols](./agent-protocols.md) - MCP is the agent-to-tool member of the broader protocol family.

## Related

- [Build Your Own MCP Server](./build-your-own-mcp-server.md) - creating custom servers with FastMCP.
- [MCP Server & Client Architecture](./mcp-architecture.md) - how servers, clients, and tool registration fit together.
- [The Problems With MCP Servers](./mcp-problems.md) - token bloat, tool overload, and early production gaps.
- [Context Engineering](./context-engineering.md) - MCP tools are context you inject deliberately.
- [Retrieval-Augmented Generation (RAG)](./rag.md) - a common capability packaged behind MCP.
- [Agentic RAG](./agentic-rag.md) - agent-driven retrieval exposed as MCP tools.
- [Agentic Coding](./agentic-coding.md) - the workflow MCP servers plug into.
- [AI Coding Harness](./ai-coding-harness.md)
- [Skills](./skills.md) - the more context-optimized alternative Cole often reaches for.
- [Tool Design](./tool-design.md)
- [Agent Security](./agent-security.md)
- [Agentic Experiences](./agentic-experiences.md)

## Tools

- [MCP](../entities/tools/mcp.md) - the protocol itself and its FastMCP tooling.
- [Anthropic](../entities/organizations/anthropic.md) - released MCP in November 2024.
- [Archon](../entities/tools/archon.md) - exposes its knowledge and task management as an MCP server.
- [Context7](../entities/tools/context7.md) - documentation retrieval delivered over MCP.
- [Neon](../entities/tools/neon.md) - ships an MCP server for database provisioning and queries.
- [n8n](../entities/tools/n8n.md) - consumes MCP servers as agent tools natively.
- [Docker](../entities/tools/docker.md) - catalog and one-click install of MCP servers.
- [Pydantic AI](../entities/tools/pydantic-ai.md) - builds MCP clients into custom agents.

## Sources

- [The ULTIMATE Guide to Building Your Own MCP Servers (Free Template)](../sources/the-ultimate-guide-to-building-your-own-mcp-servers-free-template.md) - "[0:00:00] It's the first ever standard for connecting LLMs to your services like Gmail, Slack, GitHub, web search, the list goes on."
- [Build and Ship Any MCP Server in MINUTES (Full Guide)](../sources/build-and-ship-any-mcp-server-in-minutes-full-guide.md) - "[0:06:26] It's all just APIs, but repackaged in a standard for AI agents specifically. That's all MCP is. But even though that's all it is, it still is very powerful."
- [Google is Quietly Revolutionizing AI Agents (This is HUGE)](../sources/google-is-quietly-revolutionizing-ai-agents-this-is-huge.md) - "[0:03:22] it's the USBC port for AI applications that people really started to latch on to the concept of the MCP protocol overall."
- [Claude MCP has Changed AI Forever - Here's What You NEED to Know](../sources/claude-mcp-has-changed-ai-forever-heres-what-you-need-to-know.md) - "[0:07:16] under the hood with MCP AI agents are still using Tools in exactly the same way because in the end the tools that these servers expose are just given as a part of the prompt to the llm"
- [Stripe's Coding Agents Ship 1,300 PRs EVERY Week - Here's How They Do It](../sources/stripes-coding-agents-ship-1300-prs-every-week-heres-how-they-do-it.md) - "[0:08:00] this massive set of MCP tools, this is a single stripe MCP server that they call tool shed. And so it has over 400, actually around 500 MCP tools"
- [Everything You Thought About Building AI Agents is Wrong](../sources/everything-you-thought-about-building-ai-agents-is-wrong.md) - "[0:04:48] So instead of defining the tools directly into our agent, we can create them as MCP servers, so they're a lot more reusable"
- [The OFFICIAL Archon Guide - 10x Your AI Coding Workflow](../sources/the-official-archon-guide-10x-your-ai-coding-workflow.md) - "[0:10:13] any MCP compatible AI coding assistant can connect to Archon."
- [Coding Subagents - The Next Evolution of AI IDEs](../sources/coding-subagents-the-next-evolution-of-ai-ides.md) - "[0:12:20] MCP it is a protocol developed by Claude pretty recently here just a few months ago to standardize the use of tools with large language models"
- [The Future of AI and SaaS is Agentic Experiences (Here's How to Build Them)](../sources/the-future-of-ai-and-saas-is-agentic-experiences-heres-how-to-build-them.md) - "[0:09:34] this is an MCP server that's kind of like archon for knowledge retrieval. It gives our AI coding assistant the ability to search through the CopilotKit and AGUI documentation and best practices."
- [Introducing RAG 2.0: Agentic RAG + Knowledge Graphs (FREE Template)](../sources/introducing-rag-20-agentic-rag-knowledge-graphs-free-template.md) - "[0:29:04] there are two MCP servers that I set up to help me build this all. The first one... my crawl for rag MCP server... this is how I add external documentation through rag to my AI coding assistant."
