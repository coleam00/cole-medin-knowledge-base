---
type: source
title: "AG-UI Just Released: The NEW WAVE of AI Agent Apps"
description: "AG-UI is the missing protocol that standardizes the connection between AI agents and any front end, completing the trio alongside MCP (tools) and A2A (agents) to turn agents into full user-facing applications."
youtube_id: BFWviieMyGw
url: https://www.youtube.com/watch?v=BFWviieMyGw
slug: ag-ui-just-released-the-new-wave-of-ai-agent-apps
published: 2025-05-21
duration: "0:21:40"
recency_rank: 90
raw: "../raw/ag-ui-just-released-the-new-wave-of-ai-agent-apps.md"
tags: [agent-protocols, ag-ui, generative-ui, frontend]
created: 2026-07-21
updated: 2026-07-21
---

# AG-UI Just Released: The NEW WAVE of AI Agent Apps

2025 has been the year of agent protocols: Anthropic's MCP standardized connecting tools to agents, and Google's A2A standardized connecting agents to other agents. The missing piece was a standard way to connect agents to a front end and to users. AG-UI, built by the CopilotKit team, fills that gap with an open, framework-agnostic protocol that sits as a middleman between an application (e.g. React) and agents built in any framework (LangGraph, CrewAI, Pydantic AI), emitting a standard set of events for everything the agent does.

The protocol solves recurring front-end pain points: real-time token streaming (so the agent appears to type its answer), tool orchestration (showing tool progress and results), and "framework sprawl" (each agent framework wiring to a UI differently, forcing reinvented adapters). AG-UI defines roughly 16 standard event types (run started, message start/content/end, tool call chunks, error, run finished) that a backend emits and any front end consumes, so the UI has one consistent way to display agent activity regardless of the underlying LLM or framework. Cole walks through the CopilotKit quickstart demo (streaming responses, changing the background color via front-end tools, tool-based generative UI like a haiku), then shows the raw event stream, and finally swaps the JavaScript agent for a Python FastAPI backend without changing the front end at all.

Cole frames AG-UI as brand-new and not yet fully mature, worth learning now but not yet for everything, drawing the parallel to MCP taking four to five months to reach wide adoption after its November release. He notes AG-UI's documentation and design are already stronger than early MCP, and points to the provided llms.txt docs file and MCP-based crawling as ways to give AI coding assistants like Cursor and Windsurf the context to build with the protocol.

## Concepts covered

- [Agent Protocols](../concepts/agent-protocols.md)
- [Generative UI](../concepts/generative-ui.md)
- [Frontend-Agnostic Agents](../concepts/frontend-agnostic-agent.md)
- [Streaming Responses](../concepts/streaming-responses.md)
- [Provider Independence](../concepts/provider-independence.md)
- [Human in the Loop](../concepts/human-in-the-loop.md)
- [Docs and Templates as Coding-Assistant Context](../concepts/docs-as-agent-context.md)

## Entities

- [AG-UI](../entities/tools/ag-ui.md)
- [CopilotKit](../entities/tools/copilotkit.md)
- [MCP (Model Context Protocol)](../entities/tools/mcp.md)
- [LangGraph](../entities/tools/langgraph.md)
- [CrewAI](../entities/tools/crewai.md)
- [Pydantic AI](../entities/tools/pydantic-ai.md)
- [React](../entities/tools/react.md)
- [Next.js](../entities/tools/nextjs.md)
- [FastAPI](../entities/tools/fastapi.md)
- [OpenAI](../entities/organizations/openai.md)
- [Anthropic](../entities/organizations/anthropic.md)
- [Lutra](../entities/tools/lutra.md)
- [Cursor](../entities/tools/cursor.md)
- [Windsurf](../entities/tools/windsurf.md)
- [Cole Medin](../entities/people/cole-medin.md)
- [Dynamous](../entities/organizations/dynamous.md)

## Key moments

- **[0:00:00]** 2025 as the year of agent protocols: MCP (tools) and A2A (agents), with front-end connection still missing
- **[0:00:33]** Introduces AG-UI as the protocol connecting agents to front ends and users
- **[0:01:04]** AG-UI built by the CopilotKit team; sits as a middleman between React app and any agent framework
- **[0:01:54]** Autonomous vs conversational agents; most agents need a front end for human-in-the-loop
- **[0:02:26]** Challenges without a standard: real-time streaming, tool orchestration, framework sprawl
- **[0:04:13]** How AG-UI works: standard events emitted from agent to front end
- **[0:06:20]** Live CopilotKit demo: streamed LLM response, change background color via front-end tools
- **[0:07:04]** Tool-based generative UI demo: generate a haiku, interact with the tool call in the front end
- **[0:09:53]** Core AG-UI events walkthrough: run started, message start/content/end, run finished
- **[0:10:50]** LLM-driven example with GPT-4.1 Mini streaming chunks and tool-call chunk events
- **[0:12:44]** 16 total event types including error events; framework/LLM agnostic
- **[0:15:41]** Swaps the JS agent for a Python FastAPI backend with no front-end changes
- **[0:18:44]** Using AI coding assistants (Cursor/Windsurf) with the llms.txt docs to build with AG-UI
- **[0:19:48]** Current state: brand new, not fully mature; MCP adoption parallel

## Transcript

[Raw transcript](../raw/ag-ui-just-released-the-new-wave-of-ai-agent-apps.md)
