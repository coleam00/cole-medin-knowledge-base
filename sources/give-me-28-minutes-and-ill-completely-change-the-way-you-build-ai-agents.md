---
type: source
title: "Give Me 28 Minutes and I'll Completely Change the Way You Build AI Agents"
description: "Any AI agent, no matter how complex, can be understood as a graph and decomposed into seven reusable node types (LLM, tool, control, memory, guardrail, fallback, user input) that you build one at a time and combine like Lego bricks."
youtube_id: TV8SyEuSMIA
url: https://www.youtube.com/watch?v=TV8SyEuSMIA
slug: give-me-28-minutes-and-ill-completely-change-the-way-you-build-ai-agents
published: 2025-05-11
duration: "0:28:21"
recency_rank: 93
raw: "../raw/give-me-28-minutes-and-ill-completely-change-the-way-you-build-ai-agents.md"
tags: [agents, agent-architecture, n8n, mental-models]
created: 2026-07-21
updated: 2026-07-21
---

# Give Me 28 Minutes and I'll Completely Change the Way You Build AI Agents

Cole presents his mental model for building robust AI agents: the 'seven node blueprint.' The foundational principle is that agents are really just graphs. Unlike traditional linear, deterministic automations, agents form a cycle where an LLM reasons, decides to call a tool, gets feedback, and reasons again any number of times. This non-deterministic, cyclic structure is what makes them agents, and thinking of them as graphs lets you break a daunting agent into focused subsections you can build independently.

He then walks through each of the seven node types with concrete n8n examples built around a running 'generate a dish' demo. The LLM node is the reasoning brain; the tool node performs actions (web search, code execution, DB queries); the control node injects deterministic routing/filtering logic instead of agent reasoning; the memory node handles short-term (conversation history) and long-term (vector DB, or a Google Doc in the demo) memory with retrieval at the start and extraction/storage at the end; guardrail nodes validate inputs and outputs (e.g. a critic node that checks a dish has a name, description, and origin, then retries with feedback); fallback nodes handle errors gracefully via an error trigger rather than crashing; and the user input node implements human-in-the-loop interrupts (e.g. Slack approval before sending a message), which often pair with control nodes for deterministic approve/deny routing.

Finally he assembles all seven nodes into one complex workflow, showing that the payoff of the blueprint is a reasoning process: for any problem you simply ask whether the agent needs long-term memory, what guardrails to add, what to do on error, and so on. He notes that stringing multiple LLM nodes together (or using agents as tools / sub-agents) is how you build multi-agent workflows, and points to graph-native frameworks like Pydantic AI and LangGraph as the natural abstraction.

## Concepts covered

- [Agent Graphs](../concepts/agent-graphs.md)
- [Tool Calling](../concepts/tool-use.md)
- [Memory Systems](../concepts/memory-systems.md)
- [Guardrails](../concepts/guardrails.md)
- [Human in the Loop](../concepts/human-in-the-loop.md)
- [Deterministic Workflows](../concepts/deterministic-workflows.md)
- [Subagents Pattern](../concepts/subagents-pattern.md)

## Entities

- [Cole Medin](../entities/people/cole-medin.md)
- [n8n](../entities/tools/n8n.md)
- [Pydantic AI](../entities/tools/pydantic-ai.md)
- [MCP (Model Context Protocol)](../entities/tools/mcp.md)
- [Mem0](../entities/tools/mem0.md)
- [Bright Data](../entities/organizations/bright-data.md)
- [LangGraph](../entities/tools/langgraph.md)

## Key moments

- **[0:01:08]** Introduces the 'seven node blueprint', every agent decomposes into one of seven node categories
- **[0:01:48]** Core principle: agents under the hood are just graphs
- **[0:02:31]** Contrasts agent cycles/non-determinism with linear deterministic automations
- **[0:04:53]** Node 1: the LLM node (reasoning brain)
- **[0:05:17]** Node 2: the tool node (actions, web search, code execution, DB queries)
- **[0:05:32]** Node 3: the control node (deterministic routing/filters/conditions)
- **[0:06:14]** Node 4: the memory node (long-term vector DB + short-term conversation history)
- **[0:06:35]** Node 5: guardrail nodes (input and output validation)
- **[0:07:14]** Node 6: fallback nodes (graceful error handling)
- **[0:07:40]** Node 7: user input node / human-in-the-loop interrupts
- **[0:09:53]** Long-term memory example using Mem0 and a Google Doc for storage
- **[0:14:44]** Human-in-the-loop + control node: Slack approval before sending a message
- **[0:16:52]** Guardrail example: a critic node checks the dish output and retries with feedback
- **[0:20:31]** Fallback example: error trigger sends an internal Slack alert instead of crashing
- **[0:22:52]** The full payoff: all seven nodes combined into one robust agentic workflow
- **[0:24:02]** Multi-agent note: stringing LLM nodes together / agents-as-tools builds multi-agent workflows

## Transcript

[Raw transcript](../raw/give-me-28-minutes-and-ill-completely-change-the-way-you-build-ai-agents.md)
