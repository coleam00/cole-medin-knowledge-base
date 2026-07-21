---
type: source
title: "THE BEST Tool for AI Agent Workflows - LangGraph FULL Guide"
description: "LangGraph gives production-grade AI agent applications a clear, stateful graph structure (state, nodes, edges) that turns spaghetti multi-agent code into clean, scalable, extensible agentic workflows."
youtube_id: w_HeP0A2MF8
url: https://www.youtube.com/watch?v=w_HeP0A2MF8
slug: the-best-tool-for-ai-agent-workflows-langgraph-full-guide
published: 2024-08-11
duration: "0:24:08"
recency_rank: 175
raw: "../raw/the-best-tool-for-ai-agent-workflows-langgraph-full-guide.md"
tags: [langgraph, agentic-workflow-engineering, agent-graphs, streaming, human-in-the-loop]
created: 2026-07-21
updated: 2026-07-21
---

Cole introduces LangGraph, LangChain's library for building stateful multi-actor agentic applications, as the antidote to the spaghetti code developers write when they try to wire multiple agents and tool loops together by hand. He frames LangGraph around three core concepts: the graph state (all variables tracked across execution, like chat history), the nodes (the agents themselves), and the edges (how nodes connect, including conditional edges and routers). Key features like cycles and branching, persistence, human-in-the-loop approval, and streaming support are what make complex workflows manageable.

He walks through three example workflows to build intuition: a chart-generation flow with a researcher and a router deciding whether to research more or generate the chart; a code-execution flow that generates imports and code, retries on failure, and returns the final answer; and the simplest agent-tool loop where an agent repeatedly decides whether to call tools or respond to the user. He then refactors the recursive prompt_ai function from his Asana task-management agent into a LangGraph runnable, showing how the annotated add_messages state, a call-model node (async for streaming), a tool node, and a conditional "should continue" router come together into a compiled app.

Finally he wires the runnable into a Streamlit UI, using async stream_events to yield typewriter-style chunks, a thread ID plus a SQLite checkpointer for state persistence across executions, and a system message for agent context. He tests it live against Asana (listing projects, creating a task), confirms parity with the old implementation, and teases future content on human-in-the-loop and deploying LangGraph runnables to the cloud via LangServe.

## Concepts covered

- [Agentic Workflow Engineering](../concepts/agentic-workflow-engineering.md)
- [Graph-Based Agent Workflows](../concepts/langgraph-nodes-edges-state.md)
- [Agent Graphs](../concepts/agent-graphs.md)
- [The Agent Loop (Reason-Act-Observe)](../concepts/agent-loop.md)
- [Human in the Loop](../concepts/human-in-the-loop.md)
- [Streaming Responses](../concepts/streaming-responses.md)
- [Code Execution](../concepts/code-execution.md)
- [Model Selection](../concepts/model-selection.md)

## Entities

- [LangGraph](../entities/tools/langgraph.md)
- [LangChain](../entities/tools/langchain.md)
- [LangServe](../entities/tools/langserve.md)
- [Streamlit](../entities/tools/streamlit.md)
- [Asana](../entities/tools/asana.md)
- [OpenAI](../entities/organizations/openai.md)
- [Anthropic](../entities/organizations/anthropic.md)
- [Cole Medin](../entities/people/cole-medin.md)

## Key moments

- **[0:00:00]** Opens on the spaghetti-code problem of tying agents together and pitches LangGraph as the fix
- **[0:01:14]** Tours the LangGraph docs; defines it as a library for stateful multi-actor LLM apps
- **[0:01:47]** Lists key features: cycles/branching, persistence, human-in-the-loop, streaming, LangChain integration
- **[0:02:28]** Explains the three core concepts: graph, state, nodes, edges, checkpoints, threads
- **[0:03:11]** Example 1: chart-generation workflow with researcher + router
- **[0:04:18]** Example 2: code-execution workflow with retry-on-failure loop
- **[0:05:30]** Example 3: the agent-tool loop that the task manager will implement
- **[0:06:36]** Shows the original recursive prompt_ai function and why it does not extend
- **[0:10:11]** Model selection: build ChatOpenAI or ChatAnthropic based on config, bind tools
- **[0:10:26]** Defines the graph state with the add_messages annotated list
- **[0:11:25]** Builds the call-model node (async for streaming) and the tool node
- **[0:14:46]** Defines the router / conditional edge (should_continue) returning END or "tools"
- **[0:15:42]** Compiles nodes, entry point, and conditional edge into the app workflow
- **[0:16:48]** Adds SQLite-based persistence via a checkpointer at compile time
- **[0:17:27]** Wires the runnable into the Streamlit UI with stream_events and thread ID
- **[0:21:48]** Live test against Asana: list projects, create a task, confirm streaming + memory

## Transcript

[Raw transcript](../raw/the-best-tool-for-ai-agent-workflows-langgraph-full-guide.md)
