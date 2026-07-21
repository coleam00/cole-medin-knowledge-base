---
type: source
title: "Build an ARMY of AI Agents on Autopilot with Archon, Here's How"
description: "Archon, an open-source AI agent that builds other agents in pure code, can generate an 'AI agent army' of specialized MCP-backed sub-agents coordinated by one routing primary agent, so you can connect to many services without overwhelming any single LLM."
youtube_id: -Fpp4CBo14g
url: https://www.youtube.com/watch?v=-Fpp4CBo14g
slug: build-an-army-of-ai-agents-on-autopilot-with-archon-heres-how
published: 2025-04-02
duration: "0:19:46"
recency_rank: 104
raw: "../raw/build-an-army-of-ai-agents-on-autopilot-with-archon-heres-how.md"
tags: [archon, agent-teams, mcp, subagents, pydantic-ai]
created: 2026-07-21
updated: 2026-07-21
---

Cole introduces Archon, an experimental open-source "agenteer" (an AI agent that builds other AI agents) that produces agents as pure Python code using frameworks like Pydantic AI and LangGraph, rather than locking you into a no-code platform. He built it in public as both a practical agent builder and an educational framework for teaching advanced agentic concepts. The showcase is an "AI agent army": a primary agent that routes requests to a set of specialized sub-agents, each wired to a single MCP server (GitHub, Brave, Airtable, Slack, Firecrawl, filesystem).

The core lesson is why you split tools across specialized sub-agents instead of handing one agent thirty tools: every tool inflates the prompt, and LLMs get overwhelmed quickly. By giving each sub-agent one MCP server, prompts stay small and the primary agent only has to decide which agent to call, not which of many tools to use. Cole demos multi-step tasks (list GitHub repos, web-search frameworks then write them to Airtable, then post the base link to Slack) chaining several sub-agents in one request, running on a model as small as GPT-4o mini.

He then shows the Pydantic AI code behind it (each sub-agent gets a model, system prompt, and a list of MCP servers; the primary agent defines one tool per sub-agent with docstrings that teach it when to route where) and how Archon's own agentic flow built it. Archon v6 added a tool/MCP library plus a new "advisor" agent that intelligently picks example code and MCP configs to feed the primary coder, and Cole previews future versions including LangGraph support and a v9 that spins up an isolated environment to run, test, and autonomously refine the agents it writes.

## Concepts covered

- [Agent Teams](../concepts/agent-teams.md)
- [Subagents Pattern](../concepts/subagents-pattern.md)
- [The Problems With MCP Servers](../concepts/mcp-problems.md)
- [Context Engineering](../concepts/context-engineering.md)
- [Agentic Coding](../concepts/agentic-coding.md)
- [System Evolution](../concepts/system-evolution.md)
- [Retrieval-Augmented Generation (RAG)](../concepts/rag.md)

## Entities

- [Archon](../entities/tools/archon.md)
- [MCP (Model Context Protocol)](../entities/tools/mcp.md)
- [Pydantic AI](../entities/tools/pydantic-ai.md)
- [GitHub](../entities/tools/github.md)
- [OpenAI](../entities/organizations/openai.md)
- [LangGraph](../entities/tools/langgraph.md)
- [Agent Zero](../entities/tools/agent-zero.md)
- [Dynamous](../entities/organizations/dynamous.md)
- [Cole Medin](../entities/people/cole-medin.md)

## Key moments

- **[0:00:00]** Archon introduced as the first-of-its-kind open-source agent that builds other agents in pure code
- **[0:00:47]** Reveals the "AI agent army" of specialized MCP sub-agents built with Archon
- **[0:03:49]** Why specialized agents: too many tools overwhelm an LLM by bloating the prompt
- **[0:05:07]** Live demo: primary agent routes "what GitHub repos do I have" to the GitHub sub-agent
- **[0:06:05]** Complex multi-agent request chaining Brave web search then Airtable writes
- **[0:07:28]** Continues the conversation, adding a Slack sub-agent to post the Airtable link
- **[0:10:30]** The Pydantic AI MCP integration code: one MCP server per sub-agent
- **[0:11:49]** Primary agent defines a tool per sub-agent so it picks agents, not tools
- **[0:15:47]** Archon v6 adds a tool/MCP library and an "advisor" agent that selects examples
- **[0:18:14]** Preview of v9: Archon spins up an isolated env to run, test, and self-refine agents

## Transcript

[Raw transcript](../raw/build-an-army-of-ai-agents-on-autopilot-with-archon-heres-how.md)
