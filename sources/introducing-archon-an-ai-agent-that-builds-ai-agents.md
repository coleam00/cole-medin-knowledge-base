---
type: source
title: "Introducing Archon - an AI Agent that BUILDS AI Agents"
description: "Archon is an open-source AI agent that builds, iterates on, and (eventually) runs other AI agents, serving both as a specialized agent-generation engine and as a public teaching tool for building agents with Pydantic AI and LangGraph."
youtube_id: GjR5UsVGE60
url: https://www.youtube.com/watch?v=GjR5UsVGE60
slug: introducing-archon-an-ai-agent-that-builds-ai-agents
published: 2025-03-02
duration: "0:21:56"
recency_rank: 113
raw: "../raw/introducing-archon-an-ai-agent-that-builds-ai-agents.md"
tags: [archon, meta-agent, pydantic-ai, langgraph]
created: 2026-07-21
updated: 2026-07-21
---

# Introducing Archon - an AI Agent that BUILDS AI Agents

Cole introduces Archon, an open-source AI agent whose specialty is building other AI agents. Unlike generalist AI coders such as Windsurf, Cursor, and Cline, which never work quite as well as he wants for one specific framework, Archon is a specialized engine that knows how to produce correct Pydantic AI and LangGraph code through targeted instructions and better RAG retrieval over framework documentation. It can run standalone with a Streamlit interface or plug into an AI IDE via the Model Context Protocol, effectively acting as a sub-agent the IDE invokes when it needs specialized agent-building intelligence. A live demo builds a Brave-API web-search agent inside Windsurf, and Archon returns the file structure, working Pydantic AI code, an `.env.example`, and a README.

The bulk of the video lays out Cole's iteration roadmap and long-term vision. Archon is built in versioned increments both to build in public and to teach progressively harder concepts. Planned versions split the primary coder into specialized sub-agents (prompt, tools, dependencies, agent instance), add a pre-built tool library and example-agent grounding to stop it hallucinating tools that have already been written a thousand times, expand the knowledge base with more frameworks (LangGraph, CrewAI, LlamaIndex), and introduce self-feedback loops for autonomous iteration. Later comes self-agent execution, which spins up an isolated Docker environment (database, vector store, web search) so Archon can actually run and test the agents it writes.

Further out, Cole sketches an MCP agent marketplace so Archon-built agents become reusable sub-agents, autonomous framework learning that feeds good agents and tools back into its own examples and tool library (even adjusting its own system prompt), advanced RAG techniques (hybrid search, reranking, query decomposition, hierarchical chunking), and integrations like LangSmith tracing and alternative vector databases. The through-line: build agents complex enough to be powerful and hard to replace, while breaking the concepts down simply enough to teach.

## Concepts covered

- [System Evolution](../concepts/system-evolution.md)
- [Model Selection](../concepts/model-selection.md)
- [Subagents Pattern](../concepts/subagents-pattern.md)
- [Context Engineering](../concepts/context-engineering.md)
- [Retrieval-Augmented Generation (RAG)](../concepts/rag.md)
- [Tool Design](../concepts/tool-design.md)
- [Self-Evolving Memory](../concepts/self-evolving-memory.md)
- [The Ralph Loop](../concepts/the-ralph-loop.md)
- [Abstraction Distraction](../concepts/abstraction-distraction.md)
- [Hybrid Search](../concepts/hybrid-search.md)
- [Build Your Own MCP Server](../concepts/build-your-own-mcp-server.md)
- [Community-Driven Development](../concepts/community-driven-development.md)

## Entities

- [Archon](../entities/tools/archon.md)
- [Pydantic AI](../entities/tools/pydantic-ai.md)
- [LangGraph](../entities/tools/langgraph.md)
- [MCP (Model Context Protocol)](../entities/tools/mcp.md)
- [Cline](../entities/tools/cline.md)
- [Windsurf](../entities/tools/windsurf.md)
- [Cursor](../entities/tools/cursor.md)
- [Supabase](../entities/tools/supabase.md)
- [Docker](../entities/tools/docker.md)
- [LangChain](../entities/tools/langchain.md)
- [Local AI Package](../entities/tools/local-ai-package.md)
- [LangSmith](../entities/tools/langsmith.md)
- [Cole Medin](../entities/people/cole-medin.md)

## Key moments

- **[0:00:00]** Introduces Archon as an open-source AI agent that builds other AI agents
- **[0:01:06]** Gap in the market: generalist AI coders exist, but few specialized agents for specific frameworks
- **[0:01:57]** Two ways to run Archon: standalone app, or as an MCP engine inside AI IDEs like Windsurf
- **[0:03:10]** Live demo: building a simple Brave-API web-search agent in Windsurf via Archon
- **[0:04:13]** Archon returns file structure and perfect Pydantic AI code, .env.example, and README
- **[0:06:22]** Archon uses Pydantic AI + LangGraph; built in iterations for public building and teaching
- **[0:07:29]** Why Pydantic AI + LangGraph: other frameworks are an "abstraction distraction"
- **[0:07:58]** Getting started: Docker (three commands) or pure Python + Streamlit setup UI
- **[0:11:07]** v5 roadmap: multi-agent coding workflow splitting the coder into specialized sub-agents
- **[0:12:39]** v6: tool library + example agents to prevent hallucinating already-built tools
- **[0:15:13]** v8 self-feedback loops; v9 self-agent execution via the Local AI Package
- **[0:17:11]** v11 autonomous framework learning; v12 advanced RAG; v13 MCP agent marketplace

## Transcript

[Raw transcript](../raw/introducing-archon-an-ai-agent-that-builds-ai-agents.md)
