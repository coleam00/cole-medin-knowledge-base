---
type: concept
title: "Synthesizer Agent"
description: "The final agent in a parallel architecture that takes every sub-agent's output and summarizes, formats, and optionally validates it into one coherent answer, replacing a dumb non-LLM aggregator."
tags: [agent-teams, parallel-execution, agent-architecture]
videos: [10x-your-ai-agents-with-this-one-agent-architecture]
created: 2026-07-21
updated: 2026-07-21
---

# Synthesizer Agent

A synthesizer agent is the terminal node of a fan-out architecture: it receives the outputs of every specialized sub-agent that ran in parallel and turns them into one coherent answer. It is Cole's upgrade to the standard shape, where "each of these represent an AI agent with its own instructions and tools to tackle a certain part of the problem and then you have an aggregator at the end" [0:02:36]. A plain aggregator is deterministic glue that concatenates results; a synthesizer is an LLM call that reads them, resolves overlap and contradiction between them, and writes the response the user actually wanted.

The defining trait is that it carries **no tools**. All the doing already happened upstream in the flight, hotel, and activity agents of the travel-planner demo; the synthesizer's only job is language. That narrowness is what keeps it reliable - it never has to decide whether to search, so it cannot fan out further or hallucinate an action. Its system prompt is about format and voice: merge the three recommendations into an itinerary, keep the tone consistent, surface tradeoffs, and drop the scaffolding of who produced what.

It also becomes the natural place for a last validation pass. Because it is the only component that sees all the sub-agent output at once, it is where you check that nothing required is missing before the answer leaves the system, and where token-by-token [streaming](./streaming-responses.md) is turned on so the user sees the final text form rather than the silence of parallel work.

## Part of

- [Parallel Agent Execution](./parallel-agent-execution.md) - the fan-out whose fan-in this node is.
- [Agent Teams](./agent-teams.md) - the specialist roster whose work it combines.

## Builds on

- [Subagents Pattern](./subagents-pattern.md) - narrow sub-agents are what produce the pieces worth synthesizing.

## Contrasts with

- [Deterministic Workflows](./deterministic-workflows.md) - a hard-coded aggregator node that concatenates results without reasoning over them.
- [Separate Reviewer](./separate-reviewer.md) - a second agent that judges and rejects work, where the synthesizer merges and formats it.

## Implemented by

- [Pydantic AI](../entities/tools/pydantic-ai.md) - the tool-less agent definition (model plus system prompt) used for the synthesizer.
- [LangGraph](../entities/tools/langgraph.md) - the graph whose parallel branches converge on this node.

## Related

- [Single vs. Multi-Agent Architecture](./single-vs-multi-agent.md) - why the work was split up in the first place.
- [Context Rot](./context-rot.md) - the overload the split avoids, and the risk of dumping every sub-agent result into one final prompt.
- [Structured Outputs](./structured-outputs.md) - typed sub-agent results make synthesis far easier.
- [Streaming Responses](./streaming-responses.md) - the synthesizer is what the user watches stream in.
- [Agent Architecture Patterns](./agent-architecture-patterns.md), [Agent Graphs](./agent-graphs.md), [Human in the Loop](./human-in-the-loop.md), [Agent Prompting](./agent-prompting.md).

## Sources

- [10x Your AI Agents with this ONE Agent Architecture](../sources/10x-your-ai-agents-with-this-one-agent-architecture.md) - "[0:02:36] each of these represent an AI agent with its own instructions and tools to tackle a certain part of the problem and then you have an aggregator at the end"
