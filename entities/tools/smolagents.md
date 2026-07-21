---
type: entity
subtype: tool
title: "smolagents"
description: "Hugging Face's minimal agent framework whose base agent executes actions through generated code, used here to build an entire agentic RAG workflow in very little code."
resource: "https://github.com/huggingface/smolagents"
tags: [agent-framework, sdk]
videos: [you-have-to-try-agentic-rag-with-deepseek-r1-insane-results]
created: 2026-07-21
updated: 2026-07-21
---

# smolagents

smolagents is Hugging Face's deliberately tiny agent framework, and Cole picks it when the architecture is the lesson and the framework should stay out of the way: "we're going to be using small agents by hugging face a super simple agent framework to keep it very easy to understand and follow along" [0:00:18]. Its defining design choice is unusual. Rather than emitting JSON tool calls, "in small agents the base agent actually executes its actions through code it's a very unique paradigm I kind of have mixed feelings about this" [0:08:43]. The base `CodeAgent` writes Python to act, which makes it a working example of [code execution](../../concepts/code-execution.md) as the agent's action space, and also the thing Cole is least comfortable with, since he does not always want an agent running code to get its job done.

## How Cole uses it

It is the scaffold for his local [agentic RAG](../../concepts/agentic-rag.md) build with [DeepSeek R1](./deepseek-r1.md). A fast, non-reasoning primary model drives the conversation and calls a single `rag_with_reasoner` tool that retrieves the top chunks from a [Chroma](./chroma.md) vector store and hands them to R1 for the hard reasoning step. Tools are declared with a `@tool` decorator whose docstring becomes the model's usage instructions, which he notes "is going to look very similar to setting up your tools in another framework like Lang chain or pantic AI" [0:10:37]. He caps the reasoner at `max_steps=2` to stop hallucination loops, keeps history alive with `reset=False`, and gets a full chat interface for free because smolagents integrates with [Gradio](./gradio.md) in a single line. Because the reasoner is allowed to reply with a better query, the loop becomes genuinely self-reflective rather than one-shot retrieval.

His verdict is honest about the tradeoff. smolagents is the fastest way to bootstrap and teach an agentic flow, but it has quirks (it fails to parse reasoning-model thinking tokens, surfacing an error you must ignore) that make him reach for [Pydantic AI](./pydantic-ai.md) and [LangGraph](./langgraph.md) for anything he intends to keep.

## Realizes

- [Agentic RAG](../../concepts/agentic-rag.md) - Giving an agent retrieval as a tool so it decides when and how to search a knowledge base, picking strategies and issuing follow-up queries instead of a single static lookup.
- [Code Execution](../../concepts/code-execution.md) - Giving agents a sandbox to write and run code as a general-purpose tool rather than exposing many narrow tools.
- [The Agent Loop (Reason-Act-Observe)](../../concepts/agent-loop.md) - The core agentic cycle where the LLM reasons, calls a tool, observes the result, and loops an unknown number of times until it decides to respond.
- [Tool Design](../../concepts/tool-design.md) - Designing agent tools to be few, single-purpose, and well-described (often via docstrings) so the model uses them reliably.

## Contrasts with

- [Pydantic AI](./pydantic-ai.md) - Cole's framework for the individual agents, structured around three parts: dependencies, the agent definition, and tools.
- [LangGraph](./langgraph.md) - The orchestration framework wiring agents into a stateful graph of nodes and edges, used here to run agents in parallel and add human-in-the-loop.
- [CrewAI](./crewai.md) - Multi-agent framework named as one of the interchangeable backends AG-UI supports.
- [OpenAI Swarm](./openai-swarm.md) - OpenAI's experimental multi-agent framework for building teams of agents that hand off to each other; defaults to OpenAI models but accepts a custom client.

## Works with

- [DeepSeek R1](./deepseek-r1.md) - Open-source MIT-licensed reasoning LLM that rivals OpenAI o1, ships in distilled sizes, and is far cheaper to run.
- [Gradio](./gradio.md) - Python UI framework for ML/LLM apps, integrated directly into smolagents so an agent gets a full chat interface in a single line of code.
- [Ollama](./ollama.md) - Local LLM runtime; works with a locally-run bolt.diy but can't be reached by a self-hosted (remote) instance.
- [Chroma](./chroma.md) - Publisher of the technical report on context rot that Cole cites as the most practical treatment of how input tokens degrade LLM performance.
- [LangChain](./langchain.md) - The framework used in prior masterclass videos to build the Asana agent; its message objects and invoke/stream methods underpin the chatbot logic.

## Related

- [Reasoning Model as a Tool](../../concepts/reasoning-model-as-a-tool.md) - Architecture where a fast, lightweight model drives the conversation and calls a slow, powerful reasoning model as just another tool, keeping the flow nimble while still getting reasoning-grade answers on the hard step.
- [Self-Reflective RAG](../../concepts/self-reflective-rag.md) - A RAG pattern where the agent evaluates its own retrieved context and re-queries or researches further until it has what it needs to answer well.
- [SDK vs. Framework Decision](../../concepts/sdk-vs-framework-decision.md) - Choosing between a batteries-included coding-agent SDK and a from-scratch agent framework based on who uses the agent and tolerance for speed, cost, and determinism.
- [Local & Self-Hosted AI](../../concepts/local-ai.md) - Running open-weight models on your own hardware or cloud for privacy, cost control, and independence from API providers.
- [Learn by Building](../../concepts/learn-by-building.md) - Learning AI engineering by building real projects, forking open source, and rebuilding from docs rather than passive study.

## Sources

- [You HAVE to Try Agentic RAG with DeepSeek R1 (Insane Results)](../../sources/you-have-to-try-agentic-rag-with-deepseek-r1-insane-results.md) - "[0:00:18] we're going to be using small agents by hugging face a super simple agent framework to keep it very easy to understand and follow along"
- [You HAVE to Try Agentic RAG with DeepSeek R1 (Insane Results)](../../sources/you-have-to-try-agentic-rag-with-deepseek-r1-insane-results.md) - "[0:08:43] in small agents the base agent actually executes its actions through code it's a very unique paradigm I kind of have mixed feelings about this"
