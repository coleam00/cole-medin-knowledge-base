---
type: concept
title: "Reasoning Model as a Tool"
description: "Architecture where a fast, lightweight model drives the conversation and calls a slow, powerful reasoning model as just another tool, keeping the flow nimble while still getting reasoning-grade answers on the hard step."
tags: [model-selection, reasoning-models, architecture, agent-design]
videos: [you-have-to-try-agentic-rag-with-deepseek-r1-insane-results]
created: 2026-07-21
updated: 2026-07-21
---

# Reasoning Model as a Tool

Reasoning model as a tool is an agent architecture in which the model holding the conversation is deliberately *not* the model doing the hard thinking. A fast, cheap model orchestrates, and when a step genuinely needs depth it calls the reasoning model the same way it would call any other function. Cole states the pattern directly: "combining the raw power of models like R1 with faster more lightweight models that actually direct the conversation or a gentic flow you can basically think about it as these models having R1 as one of their tools" [0:00:51].

The motivation is that [reasoning models](./reasoning-models.md) are expensive in both senses. They burn tokens on hidden chain-of-thought and they are slow, which makes them miserable as a chat driver - every "hi" costs seconds and cents. They are also frequently weaker at the mechanical parts of agent work like reliable [tool calling](./tool-use.md) and format adherence. Making the lightweight model the driver keeps latency low on the ninety percent of turns that are routing, clarification, and formatting, and spends reasoning-grade compute only on the step that earns it.

The concrete instance Cole builds is retrieval: "we're going to have an R1 driven rag tool that can be used to extract in-depth insights from a knowledge base while still keeping the rest of the conversation very very Nimble" [0:01:08]. The tool signature is ordinary - a question goes in, a synthesized answer comes out - so the calling agent never sees R1's reasoning trace. That encapsulation is the second benefit: the expensive model's verbose thinking stays inside the tool boundary rather than polluting the driver's window, which is [context isolation](./context-isolation.md) achieved through architecture rather than through subagent plumbing.

Structurally this is the same move as the [subagents pattern](./subagents-pattern.md) and [workflow as a tool](./workflow-as-a-tool.md): wrap something heavyweight behind a narrow interface and let a cheap orchestrator decide when to pay for it. It is also [model selection](./model-selection.md) applied per-step instead of per-application, and one of the cleaner forms of [LLM cost optimization](./llm-cost-optimization.md) available - a [multi-model agent](./multi-model-agent.md) where each model does only what it is best at.

## Prerequisites

- [Reasoning Models](./reasoning-models.md) - what gets wrapped, and why it is too slow to drive a conversation.
- [Tool Calling](./tool-use.md) - the mechanism the whole pattern rides on.

## Part of

- [Agent Architecture Patterns](./agent-architecture-patterns.md) - one of the recurring shapes for composing models into an agent.
- [Multi-Model Agents](./multi-model-agent.md) - the general case of routing different steps to different models.

## Contrasts with

- [Model Selection](./model-selection.md) - instead of choosing one model for the whole app, this pattern lets both win at different steps.

## Implemented by

- [Agentic RAG](./agentic-rag.md) - Cole's concrete build wraps R1 behind a knowledge-base search tool.
- [Subagents Pattern](./subagents-pattern.md), [Workflow as a Tool](./workflow-as-a-tool.md) - the same encapsulation applied to agents and workflows rather than raw models.

## Related

- [Context Isolation](./context-isolation.md) - the reasoning trace stays inside the tool instead of flooding the driver's context.
- [Chain-of-Thought Prompting](./chain-of-thought.md) - the behavior reasoning models internalize and this pattern buys on demand.
- [LLM Cost Optimization](./llm-cost-optimization.md) - paying for deep reasoning only on the steps that need it.

## Tools

- [DeepSeek R1](../entities/tools/deepseek-r1.md) - the reasoning model exposed as a tool in the build.
- [Qwen 2.5 Coder 32B](../entities/tools/qwen.md) - the fast driver model handling the conversation and tool calls.
- [Ollama](../entities/tools/ollama.md) - runs both models locally for this setup.
- [Pydantic AI](../entities/tools/pydantic-ai.md), [smolagents](../entities/tools/smolagents.md) - frameworks where wrapping a second model as a tool is a few lines.
- [OpenAI o3-mini](../entities/tools/o3-mini.md) - an alternative reasoning model for the same slot.
- [OpenAI o1](../entities/tools/o1.md) - OpenAI's reasoning model line that thinks before answering via inference-time compute, cited as the leading example of reasoning LLMs that reduce hallucinations and bad agent decisions.

## Sources

- [You HAVE to Try Agentic RAG with DeepSeek R1 (Insane Results)](../sources/you-have-to-try-agentic-rag-with-deepseek-r1-insane-results.md) - "[0:00:51] combining the raw power of models like R1 with faster more lightweight models that actually direct the conversation or a gentic flow you can basically think about it as these models having R1 as one of their tools"
- [You HAVE to Try Agentic RAG with DeepSeek R1 (Insane Results)](../sources/you-have-to-try-agentic-rag-with-deepseek-r1-insane-results.md) - "[0:01:08] we're going to have an R1 driven rag tool that can be used to extract in-depth insights from a knowledge base while still keeping the rest of the conversation very very Nimble"
