---
type: source
title: "This is Hands Down the BEST Way to Build AI Agents"
description: "Combining Pydantic AI (to build individual agents) with LangGraph (to orchestrate them into a non-deterministic workflow) is the most powerful, controllable way to build robust multi-agent systems, demonstrated by building Archon, an agent that builds other agents."
youtube_id: U6LbW2IFUQw
url: https://www.youtube.com/watch?v=U6LbW2IFUQw
slug: this-is-hands-down-the-best-way-to-build-ai-agents
published: 2025-02-12
duration: "0:51:25"
recency_rank: 118
raw: "../raw/this-is-hands-down-the-best-way-to-build-ai-agents.md"
tags: [pydantic-ai, langgraph, agent-teams, archon]
created: 2026-07-21
updated: 2026-07-21
---

# This is Hands Down the BEST Way to Build AI Agents

Cole argues the best way to build serious AI agent systems is to pair two complementary tools that both expose low-level abstractions: Pydantic AI to build each individual agent, and LangGraph to orchestrate those agents into a workflow. Pydantic AI structures every agent into three parts (dependencies like API keys and DB connections, the agent definition with system prompt and model, and the tool functions), while LangGraph is not an agent framework but an orchestrator that connects agents as nodes and edges so they can reason together over a shared, non-deterministic flow. He stresses that both frameworks keep you in control, unlike high-level frameworks like CrewAI that eventually hit a wall, and warns against over-engineering: the graph approach is a nail gun you should not reach for unless the job needs it.

The demonstration is Archon, a free open-source agent that builds other Pydantic AI agents, taught iteratively across versions. Version 1 is a single Pydantic AI RAG agent that fetches the Pydantic AI docs (crawled with Crawl4AI, chunked into Supabase/pgvector) and generates agent code, but its output does not run out of the gate because of missing env vars and no model specified. Version 2 introduces a LangGraph workflow: a Reasoner model (o3-mini or DeepSeek R1) first writes a scope document and picks relevant doc pages, a coder agent (the V1 agent, now given the scope injected dynamically into its system prompt) writes the agent, a human-in-the-loop interrupt collects feedback, a router agent decides whether to loop back or finish, and a final agent summarizes the code plus run instructions. This produces markedly better results.

Along the way Cole teaches the mechanics of LangGraph: global state that persists across nodes and is updated by returning key/value objects from each node, per-thread state isolation, conditional edges driven by routing functions that return the next node name, dynamic system-prompt injection via Pydantic AI's context dependency, message-history format conversion (binary JSON), custom stream writers, and provider independence (swapping the base URL and API key to run local models via Ollama, with a noted streaming caveat), though OpenAI embeddings remain a dependency for now.

## Concepts covered

- [Agentic Workflow Engineering](../concepts/agentic-workflow-engineering.md)
- [Agent Teams](../concepts/agent-teams.md)
- [Human in the Loop](../concepts/human-in-the-loop.md)
- [Model Selection](../concepts/model-selection.md)
- [Agentic RAG](../concepts/agentic-rag.md)
- [Provider Independence](../concepts/provider-independence.md)
- [Context Engineering](../concepts/context-engineering.md)
- [Rapid Prototyping](../concepts/rapid-prototyping.md)
- [Deterministic Workflows](../concepts/deterministic-workflows.md)
- [Agent Graphs](../concepts/agent-graphs.md)
- [System Evolution](../concepts/system-evolution.md)

## Entities

- [Pydantic AI](../entities/tools/pydantic-ai.md)
- [LangGraph](../entities/tools/langgraph.md)
- [Archon](../entities/tools/archon.md)
- [Postgres / pgvector](../entities/tools/postgres-pgvector.md)
- [Crawl4AI](../entities/tools/crawl4ai.md)
- [Ollama](../entities/tools/ollama.md)
- [Streamlit](../entities/tools/streamlit.md)
- [OpenAI](../entities/organizations/openai.md)
- [Cole Medin](../entities/people/cole-medin.md)

## Key moments

- **[0:01:44]** Grounding: what Pydantic AI and LangGraph each do and why they pair well
- **[0:02:30]** The three parts of any Pydantic AI agent: dependencies, agent definition, tool functions
- **[0:03:19]** LangGraph is an orchestrator, not an agent framework; low-level abstractions preserve control
- **[0:04:33]** LangChain research-agent example: agents as nodes, LangGraph defines the non-deterministic flow
- **[0:06:41]** Fair warning: don't over-engineer, the nail-gun analogy
- **[0:08:04]** Introducing Archon: an AI agent that builds other AI agents, taught iteratively
- **[0:12:49]** Archon V1: a single Pydantic AI RAG agent over the Pydantic AI docs
- **[0:16:40]** V1 shortcomings: output doesn't run, missing model and env vars
- **[0:18:34]** Archon V2 graph: Reasoner to coder to human-in-the-loop to router to finish
- **[0:19:46]** Reasoner model (DeepSeek R1 / o3-mini) writes a scope doc and picks doc pages
- **[0:20:18]** Human-in-the-loop feedback loop explained
- **[0:25:31]** Provider independence: base URL / API key override to run local Ollama models
- **[0:28:20]** LangGraph global state: what to track across all nodes
- **[0:33:00]** Dynamically injecting the Reasoner scope into the coder's system prompt via a dependency
- **[0:41:29]** Router node returns the name of the next node for conditional edges
- **[0:44:02]** Assembling the graph: adding nodes and defining edges
- **[0:48:56]** Full-power test: o3-mini Reasoner + GPT-4o coder builds a web-search agent

## Transcript

[Raw transcript](../raw/this-is-hands-down-the-best-way-to-build-ai-agents.md)
