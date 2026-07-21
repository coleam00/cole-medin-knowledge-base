---
type: concept
title: "Agent Graphs"
description: "Modeling agents as stateful graphs of nodes and conditional edges with persisted checkpoints, as in LangGraph."
tags: [graph, state, langgraph]
videos: [i-was-wrong-about-ralph-wiggum, are-agent-harnesses-bringing-back-vibe-coding, give-me-28-minutes-and-ill-completely-change-the-way-you-build-ai-agents, this-is-hands-down-the-best-way-to-build-ai-agents, n8n-crawl4ai-scrape-any-website-in-minutes-with-no-code, the-best-tool-for-ai-agent-workflows-langgraph-full-guide]
created: 2026-07-21
updated: 2026-07-21
---

# Agent Graphs

An agent graph is the underlying structure every agent actually is: a set of nodes connected by edges, with shared state flowing through them. Cole makes the claim bluntly: "This is just so important to understand that agents under the hood are really just graphs" [0:01:48]. The reason is that agents have a fundamental cycle, "the LLM deciding to use a tool getting feedback and reasoning about what happened when it used that tool and then it can invoke more tools" [0:02:31], and that cycle is precisely a loop in a graph. Seeing it as a graph is what lets you decompose the agent: "When we have these different cycles and these different nodes in a graph, that allows us to reason about how we break the agent into smaller components" [0:03:18].

The load-bearing part of a graph is its state, the information carried across the whole run. "we have to manage the state for our graph... these are all pieces of information that we want to keep track of throughout the entire execution of the graph" [0:28:20]. Nodes update that state by convention: "when you want to update the state the global state that we're tracking for this execution of the graph at the end of Any Given node you just have to return an object where you have the key that maps to the specific value" [0:31:25]. The framework then persists state per conversation, "you pass that into LangGraph and it's going to manage the state independently for each one of those conversation IDs" [0:29:11], which is what gives an agent memory and resumability across turns.

Graphs also model the loops that drive long-running agent harnesses. The Ralph loop is a graph with an explicit exit edge: "The only time that we're allowed to output this to exit the Ralph loop is when passes is true for every single feature that we have in our PRD" [0:08:28], and "otherwise, this Ralph loop is going to run forever or until we reach the max iterations" [0:08:56]. A common harness shape is a two-node graph, "some kind of initializer that sets the stage for the longrunning task. And then you have the task agent that is responsible for making incremental progress" [0:07:10]. The same poll-and-branch structure shows up even in no-code: a node kicks off a task, then "we have this if statement where we basically just check to see if the status is completed and if it is not completed... loop back around wait another 5 seconds and then check again" [0:25:09].

## Builds on

- [The Agent Loop (Reason-Act-Observe)](./agent-loop.md) - the reason-act-observe cycle is the loop a graph makes explicit.

## Part of

- [Agentic Workflow Engineering](./agentic-workflow-engineering.md) - thinking in graphs is how you engineer a durable agentic workflow.

## Related

- [Graph-Based Agent Workflows](./langgraph-nodes-edges-state.md) - the LangGraph vocabulary of nodes, edges, and state that realizes this idea.
- [The Ralph Loop](./the-ralph-loop.md) - a graph whose single exit edge is "all features pass."
- [Deterministic Workflows](./deterministic-workflows.md) - hard-coding edges makes parts of the graph deterministic.
- [Human in the Loop](./human-in-the-loop.md) - a checkpoint edge where the graph pauses for approval.
- [Guardrails](./guardrails.md) - conditions on edges that keep the graph from running off the rails.
- [PRD-First Development](./prd-first-development.md) - the feature list a harness graph checks against to decide when to exit.
- [Tool Calling](./tool-use.md) - the action a node takes before the graph loops back to reason.
- [AI Coding Harness](./ai-coding-harness.md) - long-running harnesses are graphs of initializer and task nodes.
- [Context Reset](./context-reset.md) - a fresh node run can reset context between iterations of the loop.
- [End-to-End Validation](./end-to-end-validation.md) - the check on the exit edge of a build loop.
- [Containerization](./containerization.md) - where a long-running graph is often executed.
- [Agent Teams](./agent-teams.md) - multiple agents wired together are just a larger graph.
- [The Seven Node Blueprint](./seven-node-blueprint.md) - Cole's mental model that decomposes any AI agent into seven reusable node types (LLM, tool, control, memory, guardrail, fallback, user input) you build individually and combine like Lego bricks.
- [File-System-Based Agents](./file-system-based-agents.md) - An architecture where an entire AI agent is defined as a single folder of organized markdown and TypeScript primitives rather than hand-wired framework code.

## Tools

- [LangGraph](../entities/tools/langgraph.md) - the framework built specifically to define agents as stateful graphs.

## Sources

- [Give Me 28 Minutes and I'll Completely Change the Way You Build AI Agents](../sources/give-me-28-minutes-and-ill-completely-change-the-way-you-build-ai-agents.md) - "[0:01:48] This is just so important to understand that agents under the hood are really just graphs."
- [Give Me 28 Minutes and I'll Completely Change the Way You Build AI Agents](../sources/give-me-28-minutes-and-ill-completely-change-the-way-you-build-ai-agents.md) - "[0:03:18] When we have these different cycles and these different nodes in a graph, that allows us to reason about how we break the agent into smaller components."
- [This is Hands Down the BEST Way to Build AI Agents](../sources/this-is-hands-down-the-best-way-to-build-ai-agents.md) - "[0:28:20] we have to manage the state for our graph... these are all pieces of information that we want to keep track of throughout the entire execution of the graph"
- [This is Hands Down the BEST Way to Build AI Agents](../sources/this-is-hands-down-the-best-way-to-build-ai-agents.md) - "[0:29:11] you pass that into LangGraph and it's going to manage the state independently for each one of those conversation IDs"
- [I Was Wrong About Ralph Wiggum](../sources/i-was-wrong-about-ralph-wiggum.md) - "[0:08:28] The only time that we're allowed to output this to exit the Ralph loop is when passes is true for every single feature that we have in our PRD"
- [Are Agent Harnesses Bringing Back Vibe Coding?](../sources/are-agent-harnesses-bringing-back-vibe-coding.md) - "[0:07:10] the most common architecture is to have some kind of initializer that sets the stage for the longrunning task. And then you have the task agent that is responsible for making incremental progress."
- [THE BEST Tool for AI Agent Workflows - LangGraph FULL Guide](../sources/the-best-tool-for-ai-agent-workflows-langgraph-full-guide.md) - "[0:13:06] the way that you take a node and you have it update the state of the graph is you just return an object of the node where the keys are going to be the pieces of state that you want to update"
- [n8n + Crawl4AI - Scrape ANY Website in Minutes with NO Code](../sources/n8n-crawl4ai-scrape-any-website-in-minutes-with-no-code.md) - "[0:25:09] we have this if statement where we basically just check to see if the status is completed and if it is not completed... loop back around wait another 5 seconds and then check again"
