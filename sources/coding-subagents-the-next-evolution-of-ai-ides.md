---
type: source
title: "Coding Subagents - The Next Evolution of AI IDEs"
description: "The next evolution of AI IDEs is specialized sub-agents exposed as MCP tools, so a general coder like Windsurf or Cursor can call a framework-expert agent (Archon) instead of hallucinating unfamiliar code."
youtube_id: Ri3iyi3qFlI
url: https://www.youtube.com/watch?v=Ri3iyi3qFlI
slug: coding-subagents-the-next-evolution-of-ai-ides
published: 2025-02-19
duration: "0:26:59"
recency_rank: 116
raw: "../raw/coding-subagents-the-next-evolution-of-ai-ides.md"
tags: [subagents, mcp, archon, ai-ide]
created: 2026-07-21
updated: 2026-07-21
---

# Coding Subagents - The Next Evolution of AI IDEs

Cole argues that general-purpose AI coding assistants like Windsurf and Cursor are a jack-of-all-trades and master of none: even when handed a framework's documentation, they hallucinate bad code because they are too general. His proposed paradigm shift is to build specialized sub-agents that are experts at coding with one specific tool or framework, and expose them as MCP tools that any popular AI coder can invoke on demand. That gives the best of both worlds, a general coder for most work and a specialist called in only when it is needed.

He demonstrates by wrapping Archon, his meta-agent that builds Pydantic AI and LangGraph agents, as an MCP server and baking it into Windsurf. Claude 3.5 Sonnet in Windsurf sees Archon's two tools (create a thread ID, invoke Archon) via their docstring descriptions and delegates agent-building to it. Archon runs its own stateful LangGraph workflow, an o3-mini Reasoner defines the scope, a GPT-4o coder performs RAG over the Pydantic AI docs and writes the files, and a human-in-the-loop step lets you iterate, then hands the generated files back for Windsurf to write to disk. Because the workflow and system prompts are fixed, Archon produces far more consistent, structured output than a general coder that spews different code every time.

Cole then covers the implementation details. The MCP server is a simple FastAPI wrapper (built with the MCP Python SDK) around Archon's unchanged graph. Tool docstrings are injected into the LLM's prompt to tell it when and how to use each tool. A thread ID is threaded through calls so the otherwise-stateless MCP tool can maintain Archon's stateful conversation across iterations. He notes it is experimental and alpha, with plans for self-feedback loops, breaking builds into smaller steps, and a reusable tool library. The only real failure in the demo was a Brave API hallucination, since no docs were provided for it.

## Concepts covered

- [Subagents Pattern](../concepts/subagents-pattern.md)
- [Limitations of AI Coding Models](../concepts/ai-coding-limitations.md)
- [Model Context Protocol (MCP)](../concepts/mcp.md)
- [Agentic Workflow Engineering](../concepts/agentic-workflow-engineering.md)
- [Human in the Loop](../concepts/human-in-the-loop.md)
- [System Evolution](../concepts/system-evolution.md)
- [Retrieval-Augmented Generation (RAG)](../concepts/rag.md)
- [Tool Design](../concepts/tool-design.md)

## Entities

- [Archon](../entities/tools/archon.md)
- [MCP (Model Context Protocol)](../entities/tools/mcp.md)
- [Windsurf](../entities/tools/windsurf.md)
- [Cursor](../entities/tools/cursor.md)
- [Pydantic AI](../entities/tools/pydantic-ai.md)
- [LangGraph](../entities/tools/langgraph.md)
- [Anthropic](../entities/organizations/anthropic.md)
- [OpenAI](../entities/organizations/openai.md)
- [FastAPI](../entities/tools/fastapi.md)
- [Brave Search](../entities/tools/brave-search.md)
- [Cole Medin](../entities/people/cole-medin.md)

## Key moments

- **[0:00:36]** Cole frames the thesis: a paradigm shift for AI coding built on specialized sub-agents and Claude's MCP
- **[0:01:11]** The problem: AI coding assistants are too general, jack-of-all-trades master-of-none, even with docs
- **[0:01:41]** The "golden ticket": specialized agents for a specific tool/framework, callable by general coders as MCP tools
- **[0:03:18]** Live demo: prompting Windsurf to use Archon to build a Brave web-search agent
- **[0:04:16]** Archon's workflow runs: Reasoner scopes the agent, coder does RAG on Pydantic AI docs, control returns to Windsurf
- **[0:06:46]** Q&A: why not just use the built-in docs feature? Archon gives consistent, better-structured output via its whole flow
- **[0:08:24]** Why generate a thread ID: MCP tools are stateless but Archon is stateful, so an identifier maps the conversation
- **[0:12:20]** Explains MCP: a protocol from Anthropic standardizing how tools are given to LLMs
- **[0:15:11]** Walks through the Archon MCP server: FastAPI + MCP Python SDK wrapping the unchanged LangGraph graph
- **[0:17:16]** Tool docstrings are injected into the LLM prompt and dictate when/how the tool is used
- **[0:21:07]** Final demo: builds and iterates the Brave agent, uses human-in-the-loop to fix the model, runs it in Streamlit
- **[0:24:33]** Only real failure was a Brave API hallucination (no docs given), motivating a reusable tool library

## Transcript

[Raw transcript](../raw/coding-subagents-the-next-evolution-of-ai-ides.md)
