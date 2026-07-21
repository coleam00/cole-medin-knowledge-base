---
type: concept
title: "Agent Architecture Patterns"
description: "Reusable agent design patterns like prompt chaining, routing, parallelization, orchestrator-workers, and evaluator loops for structuring agentic systems."
tags: [patterns, orchestration, routing, chaining]
videos: [how-to-dominate-with-ai-in-2025]
created: 2026-07-21
updated: 2026-07-21
---

# Agent Architecture Patterns

Agent architecture patterns are the reusable building blocks for structuring an agentic system, a small vocabulary of shapes that recur across almost every serious agent. Cole runs through the canonical set: "they have a ton of really cool things like promp chaining and routing... parallelization to conquer tasks with multiple llms at the same time they've got orchestration workers" [0:09:39]. Each pattern answers a different structural question. Prompt chaining sequences steps so one model's output feeds the next. Routing classifies a request and sends it to the specialized handler for that case. Parallelization fans a task out across multiple LLM calls at once. Orchestrator-workers has a lead agent decompose a task and delegate slices to worker agents.

The pattern Cole singles out as most underrated is the evaluator, "an evaluator which is super important for reducing hallucinations" [0:09:56]. An evaluator (or evaluator-optimizer loop) adds a second model whose only job is to judge the first one's output and send it back for another pass if it falls short, which is why it maps so directly onto reducing hallucinations and raising reliability.

Knowing the patterns also drives the build-versus-buy decision. Cole frames the whole discussion around "agent architecture best practices when to build yourself versus use a platform that does a lot for you" [0:07:10]: once you can name the pattern a problem needs, you can tell whether a no-code platform already implements it or whether you should assemble it yourself. These patterns are largely the ones popularized in Anthropic's "Building Effective Agents" writing, and they are the concrete moves inside the broader discipline of designing agentic workflows.

## Part of

- [Agentic Workflow Engineering](./agentic-workflow-engineering.md) - patterns are the concrete moves you compose when engineering an agentic workflow.

## Contrasts with

- [Agents vs. Workflows](./agents-vs-workflows.md) - these patterns span the spectrum from fixed workflows (chaining, routing) to open-ended agents (orchestrator-workers).
- [Single vs. Multi-Agent Architecture](./single-vs-multi-agent.md) - orchestrator-workers and routing are the patterns you reach for once one agent is not enough.

## Related

- [Agent Teams](./agent-teams.md) - orchestrator-workers and routing realized as coordinating, specialized agents.
- [Subagents Pattern](./subagents-pattern.md) - the delegation half of orchestrator-workers.
- [Parallel Agent Execution](./parallel-agent-execution.md) - the parallelization pattern in practice.
- [Graph-Based Agent Workflows](./langgraph-nodes-edges-state.md) - a concrete framework for wiring these patterns as nodes and edges.
- [Self-Correcting Agents](./self-correction.md) - the evaluator pattern applied to an agent judging its own work.
- [Buy vs. Build](./buy-vs-build.md) - the decision the patterns inform: build the shape yourself or adopt a platform that already has it.
- [What Is an AI Agent](./what-is-an-ai-agent.md) - the primitive these patterns arrange.

## Tools

- [Anthropic](../entities/organizations/anthropic.md) - publisher of the "Building Effective Agents" guide that names most of these patterns.

## Sources

- [How to DOMINATE with AI in 2025](../sources/how-to-dominate-with-ai-in-2025.md) - "[0:09:39] they have a ton of really cool things like promp chaining and routing... parallelization to conquer tasks with multiple llms at the same time they've got orchestration workers"
- [How to DOMINATE with AI in 2025](../sources/how-to-dominate-with-ai-in-2025.md) - "[0:09:56] an evaluator which is super important for reducing hallucinations"
- [How to DOMINATE with AI in 2025](../sources/how-to-dominate-with-ai-in-2025.md) - "[0:07:10] for you and I to dive into agent architecture best practices when to build yourself versus use a platform that does a lot for you"
