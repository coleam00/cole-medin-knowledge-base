---
type: source
title: "The Future of AI and SaaS is Agentic Experiences (Here's How to Build Them)"
description: "The future of SaaS isn't standalone agents but 'agentic experiences,' AI agents deeply embedded into products via the AG-UI protocol, which standardizes front-end-to-agent communication so state syncs both ways in a hundred lines of code."
youtube_id: BcvjGTxzK40
url: https://www.youtube.com/watch?v=BcvjGTxzK40
slug: the-future-of-ai-and-saas-is-agentic-experiences-heres-how-to-build-them
published: 2025-09-17
duration: "0:20:46"
recency_rank: 70
raw: "../raw/the-future-of-ai-and-saas-is-agentic-experiences-heres-how-to-build-them.md"
tags: [agentic-experiences, ag-ui, generative-ui, copilotkit]
created: 2026-07-21
updated: 2026-07-21
---

Cole argues that as general-purpose agents (ChatGPT, Operator) grow more powerful, isolated niche chatbots and agent-as-product companies will be wiped out; what survives is SaaS that deeply integrates agents into a product with its own unique value, what he calls "agentic experiences." These are harder to build than isolated chatbots because they require two-way state synchronization between the front end and the agent, but the AG-UI protocol (from the CopilotKit team) makes them tractable. AG-UI is like MCP, but instead of connecting agents to tools it connects agents to applications in a standard way, so a React front end (CopilotKit) and any agent framework (Pydantic AI, LangGraph, Agno) can be swapped without changing the other side.

He demos the power of AG-UI: a recipe builder with two-way state sync (edit ingredients in the UI and the agent sees them; ask the agent for a recipe and it renders the UI), front-end tools the agent does not need to know about (set theme, clear proverbs), generative UI (rendering a weather card component from a tool call), and human-in-the-loop collaboration. Getting started is a single npx/npm quick-start that scaffolds a CopilotKit + AG-UI + agent-framework project running locally.

To build on top, Cole uses CopilotKit's "vibe coding" MCP server, a remote, free MCP that lets a coding assistant (Claude Code) search CopilotKit and AG-UI documentation as expert context (RAG over docs, like Archon). He adds a "clear all proverbs" front-end tool and then shows a bigger payoff: he takes an existing Pydantic AI RAG agent from a prior video and wraps a full app around it with almost no code changes. The backend is a single agent.py whose `.to_ag_ui()` call turns it into an AG-UI-compatible API endpoint on port 8000, handling state sync, streaming, and conversation history. The RAG app surfaces retrieved chunks, match percentages, and metadata in the UI. His closing point: AG-UI, CopilotKit, and Pydantic AI are just tools, the durable principles are state syncing, front-end tools, and human-in-the-loop.

## Concepts covered

- [Agentic Experiences](../concepts/agentic-experiences.md)
- [Generative UI](../concepts/generative-ui.md)
- [Human in the Loop](../concepts/human-in-the-loop.md)
- [Frontend-Agnostic Agents](../concepts/frontend-agnostic-agent.md)
- [Model Context Protocol (MCP)](../concepts/mcp.md)
- [Retrieval-Augmented Generation (RAG)](../concepts/rag.md)

## Entities

- [AG-UI](../entities/tools/ag-ui.md)
- [CopilotKit](../entities/tools/copilotkit.md)
- [Pydantic AI](../entities/tools/pydantic-ai.md)
- [MCP (Model Context Protocol)](../entities/tools/mcp.md)
- [Claude Code](../entities/tools/claude-code.md)
- [Cole Medin](../entities/people/cole-medin.md)

## Key moments

- **[0:00:17]** Thesis: the future isn't agents-as-products but embedding agents into products as "agentic experiences"
- **[0:01:24]** Introduces AG-UI, a protocol from the CopilotKit team that standardizes front-end-to-agent communication, "like MCP but for applications"
- **[0:02:36]** Tech stack: CopilotKit (React front end) + Pydantic AI (agent framework), newly integrated via AG-UI
- **[0:04:16]** Recipe-builder demo showing two-way state sync between front end and backend agent
- **[0:05:33]** Front-end tools and tool-based generative UI, tools built in the front end and passed into the agent
- **[0:05:48]** Quick-start command scaffolds a CopilotKit + AG-UI + agent-framework app running locally
- **[0:07:40]** Front-end tool demo: "set the theme to green," the backend agent doesn't even know the tool exists
- **[0:08:52]** Generative UI: "what is the weather in Orlando" renders a nice React card from a tool call
- **[0:09:26]** CopilotKit's "vibe coding" MCP server, RAG over CopilotKit/AG-UI docs for a coding assistant, like Archon
- **[0:10:50]** Adds a "clear all proverbs" front-end tool with Claude Code using the MCP docs server
- **[0:15:31]** Backend is a single agent.py; `.to_ag_ui()` turns a Pydantic AI agent into an AG-UI-compatible API endpoint
- **[0:16:50]** Wraps an existing Pydantic AI RAG agent in a full app, surfacing retrieved chunks, match %, and metadata in the UI
- **[0:20:04]** Closing: the tools are interchangeable; the durable principles are state syncing, front-end tools, and human-in-the-loop

## Transcript

[Raw transcript](../raw/the-future-of-ai-and-saas-is-agentic-experiences-heres-how-to-build-them.md)
