---
type: concept
title: "The Seven Node Blueprint"
description: "Cole's mental model that decomposes any AI agent into seven reusable node types (LLM, tool, control, memory, guardrail, fallback, user input) you build individually and combine like Lego bricks."
tags: [mental-model, agent-architecture, framework]
videos: [give-me-28-minutes-and-ill-completely-change-the-way-you-build-ai-agents]
created: 2026-07-21
updated: 2026-07-21
---

# The Seven Node Blueprint

The seven node blueprint is Cole's claim that agent architecture is a closed set: "The mental model that I'm going to be sharing with you now, I'm calling the seven node blueprint for AI agents. Because any AI agent that you could possibly dream of making can be broken down into components that are going to fall into one of seven categories" [0:01:08]. It rests on the prior observation that agents are graphs, so once you accept the graph, the node types are enumerable and reusable: "You can kind of think of these graphs as just being a bunch of Lego bricks that are put together" [0:03:45].

The seven types:

1. **LLM node** - the reasoning brain that decides what happens next.
2. **Tool node** - the action: web search, code execution, a database query.
3. **Control node** - deterministic routing, filters, and conditions where you do not want the agent reasoning at all.
4. **Memory node** - short-term conversation history plus long-term storage, retrieved at the start of a run and written back at the end.
5. **Guardrail node** - input and output validation, such as a critic that checks the output has the required fields and retries with feedback.
6. **Fallback node** - graceful error handling via an error trigger instead of a crash.
7. **User input node** - the human-in-the-loop interrupt, often paired with a control node for deterministic approve/deny routing.

The value is not the taxonomy, it is the checklist it produces: "The reason that this is powerful for us to understand these different components is we can reason about what we want to add into this by just thinking like does this agent need long-term memory?" [0:25:57]. Face any agent problem and you walk the seven questions - what tools, what routing must be deterministic, what memory, what guardrails, what happens on error, where does a human approve - and the daunting build becomes seven small independent builds. Chaining multiple LLM nodes, or exposing an agent as a tool, is how the same blueprint scales into multi-agent systems.

## Builds on

- [Agent Graphs](./agent-graphs.md) - the blueprint only makes sense once you see the agent as a cyclic graph.
- [The Core Components of an Agent](./agent-core-components.md) - LLM, tools, and instructions, which the blueprint extends outward.

## Contrasts with

- [Agents vs. Workflows](./agents-vs-workflows.md) - the control node is where a linear deterministic automation is deliberately reintroduced inside an agent.

## Implemented by

- [n8n](../entities/tools/n8n.md) - the no-code canvas Cole uses to build all seven node types in the walkthrough.
- [LangGraph](../entities/tools/langgraph.md), [Pydantic AI](../entities/tools/pydantic-ai.md) - graph-native frameworks that map onto the blueprint in code.
- [Mem0](../entities/tools/mem0.md) - the long-term memory node in the demo.

## Related

- [Tool Calling](./tool-use.md) - node 2.
- [Memory Systems](./memory-systems.md) - node 4, short-term and long-term.
- [Guardrails](./guardrails.md) - node 5, including the critic-and-retry pattern.
- [Human in the Loop](./human-in-the-loop.md) - node 7.
- [Deterministic Workflows](./deterministic-workflows.md) - node 3.
- [Subagents Pattern](./subagents-pattern.md), [Agent Teams](./agent-teams.md) - what stringing LLM nodes together becomes.
- [What Is an AI Agent](./what-is-an-ai-agent.md), [The Agent Loop (Reason-Act-Observe)](./agent-loop.md), [Graph-Based Agent Workflows](./langgraph-nodes-edges-state.md), [Agent Architecture Patterns](./agent-architecture-patterns.md).

## Sources

- [Give Me 28 Minutes and I'll Completely Change the Way You Build AI Agents](../sources/give-me-28-minutes-and-ill-completely-change-the-way-you-build-ai-agents.md) - "[0:01:08] The mental model that I'm going to be sharing with you now, I'm calling the seven node blueprint for AI agents. Because any AI agent that you could possibly dream of making can be broken down into components that are going to fall into one of seven categories."
- [Give Me 28 Minutes and I'll Completely Change the Way You Build AI Agents](../sources/give-me-28-minutes-and-ill-completely-change-the-way-you-build-ai-agents.md) - "[0:03:45] You can kind of think of these graphs as just being a bunch of Lego bricks that are put together."
- [Give Me 28 Minutes and I'll Completely Change the Way You Build AI Agents](../sources/give-me-28-minutes-and-ill-completely-change-the-way-you-build-ai-agents.md) - "[0:25:57] The reason that this is powerful for us to understand these different components is we can reason about what we want to add into this by just thinking like does this agent need long-term memory?"
