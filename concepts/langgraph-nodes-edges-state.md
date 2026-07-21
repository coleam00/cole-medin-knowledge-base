---
type: concept
title: "Graph-Based Agent Workflows"
description: "Model an agent as a directed graph of nodes, edges, and shared state (LangGraph) with routing between steps, giving explicit control over branching, loops, and serving of complex agent workflows."
tags: [langgraph, langserve, state-machine, routing, workflows, graphs]
videos: [complete-guide-to-langserve-make-your-ai-agent-actually-useful, the-best-tool-for-ai-agent-workflows-langgraph-full-guide]
created: 2026-07-21
updated: 2026-07-21
---

# Graph-Based Agent Workflows

A graph-based agent workflow expresses an agent as three explicit primitives, and LangGraph's vocabulary names them cleanly: "you've got the graph which is the highest level concept then you have the state which is all the variables that are maintained in the execution of the agentic workflow like the chat history" [0:02:28], and "then you have the nodes which are basically your agents the edges which is how all the agents are connected together even conditionally" [0:02:44]. The graph is the container, the state is the data that persists across the run, nodes are the units of work (often themselves agents or LLM calls), and edges are the wiring between them. The key move over a plain agent loop is that edges can be conditional, which turns implicit control flow into something you draw and control directly.

The conditional edge is what makes this powerful for real workflows. A router node inspects the model's output and branches: "I have this router this conditional router where basically if the AI agent says it wants to invoke a tool then I go to the tool node otherwise I just return the response the user" [0:03:51]. Assembling the workflow is then just declaring nodes and their edges, and the state can be persisted so the graph remembers across turns: "defining the workflow we just have our agent and Tool nodes with that conditional Edge I can pile it with memory and then return it" [0:04:04]. Because the whole thing is a compiled object, it can be served behind an API (LangServe) to make the agent actually usable by clients, which is where "make your AI agent actually useful" comes in.

This is the concrete, framework-level realization of the broader idea that agents are graphs. Where the general concept explains why the shape matters, this page is about the specific nodes-edges-state model you code against in LangGraph and serve with LangServe.

## Builds on

- [Agent Graphs](./agent-graphs.md) - the general principle that agents are graphs; this is the LangGraph model that operationalizes it.

## Related

- [Tool Calling](./tool-use.md) - the tool node a conditional edge routes to when the model decides to act.
- [Deterministic Workflows](./deterministic-workflows.md) - hard-wiring edges makes parts of the graph deterministic instead of model-decided.
- [Agentic Workflow Engineering](./agentic-workflow-engineering.md) - designing these node-and-edge workflows is the core of the discipline.
- [Memory Systems](./memory-systems.md) - the persisted state that lets a compiled graph remember across turns.
- [Human in the Loop](./human-in-the-loop.md) - a conditional edge that pauses the graph for approval.
- [Streaming Responses](./streaming-responses.md) - how a served graph returns output token by token.

## Tools

- [LangGraph](../entities/tools/langgraph.md) - the framework whose graph, node, edge, and state primitives this describes.
- [LangServe](../entities/tools/langserve.md) - serves a compiled graph behind an API so clients can use the agent.
- [LangChain](../entities/tools/langchain.md) - the surrounding ecosystem LangGraph and LangServe sit within.

## Sources

- [THE BEST Tool for AI Agent Workflows - LangGraph FULL Guide](../sources/the-best-tool-for-ai-agent-workflows-langgraph-full-guide.md) - "[0:02:28] you've got the graph which is the highest level concept then you have the state which is all the variables that are maintained in the execution of the agentic workflow like the chat history"
- [THE BEST Tool for AI Agent Workflows - LangGraph FULL Guide](../sources/the-best-tool-for-ai-agent-workflows-langgraph-full-guide.md) - "[0:02:44] then you have the nodes which are basically your agents the edges which is how all the agents are connected together even conditionally"
- [COMPLETE Guide to LangServe - Make Your AI Agent Actually Useful](../sources/complete-guide-to-langserve-make-your-ai-agent-actually-useful.md) - "[0:03:51] I have this router this conditional router where basically if the AI agent says it wants to invoke a tool then I go to the tool node otherwise I just return the response the user"
- [COMPLETE Guide to LangServe - Make Your AI Agent Actually Useful](../sources/complete-guide-to-langserve-make-your-ai-agent-actually-useful.md) - "[0:04:04] defining the workflow we just have our agent and Tool nodes with that conditional Edge I can pile it with memory and then return it"
