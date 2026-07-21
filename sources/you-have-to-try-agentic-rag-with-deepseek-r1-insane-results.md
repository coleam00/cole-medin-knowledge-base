---
type: source
title: "You HAVE to Try Agentic RAG with DeepSeek R1 (Insane Results)"
description: "Reasoning models like DeepSeek R1 are powerful but slow, so wrapping R1 as a RAG tool called by a faster, lightweight primary LLM unlocks a simple yet powerful local agentic RAG workflow."
youtube_id: uWDocIoiaXE
url: https://www.youtube.com/watch?v=uWDocIoiaXE
slug: you-have-to-try-agentic-rag-with-deepseek-r1-insane-results
published: 2025-02-02
duration: "0:22:20"
recency_rank: 120
raw: "../raw/you-have-to-try-agentic-rag-with-deepseek-r1-insane-results.md"
tags: [agentic-rag, deepseek-r1, local-ai, reasoning-models]
created: 2026-07-21
updated: 2026-07-21
---

# You HAVE to Try Agentic RAG with DeepSeek R1 (Insane Results)

Cole demonstrates an agentic RAG setup that pairs a slow-but-powerful reasoning model (DeepSeek R1) with a faster, lightweight non-reasoning model (Qwen 2.5) that drives the conversation. The key mental model is treating R1 as a tool the primary agent can reach for when it needs deep reasoning: the fast agent handles the nimble conversation flow, and only invokes an R1-backed RAG tool when it needs in-depth insight from a knowledge base. This keeps the overall interaction responsive while still delivering reasoning-model quality on the hard retrieval-and-synthesis step.

The implementation uses Hugging Face's smolagents (small agents) framework to keep everything minimal, and runs entirely locally via Ollama with the distilled 7B R1 and Qwen models. Cole builds it step by step: a CodeAgent reasoner (capped at `max_steps=2` to prevent hallucination loops), a ChromaDB vector database populated from PDFs via LangChain chunking and a local Hugging Face embedding model, and a single `rag_with_reasoner` tool decorated with a docstring so the primary tool-calling agent knows when to call it. The tool does a similarity search for the top-3 chunks, formats them into a prompt, and feeds them to R1 to extract insights, returning the answer to the primary LLM. A Gradio UI is wired up in a single line.

A notable agentic detail: the reasoner's prompt allows it to tell the primary LLM to retry with a better query if the retrieved context is insufficient, creating a feedback loop that makes this true agentic RAG rather than one-shot RAG. Cole also shares the practical Ollama gotcha that default models cap context at 2048 tokens, which causes hallucinations, and shows how to build a model file to raise it (for example to 8192 tokens). He notes smolagents has quirks (a code-execution paradigm, and failing to parse thinking tokens) and teases a more robust future build with Pydantic AI and LangGraph.

## Concepts covered

- [Agentic RAG](../concepts/agentic-rag.md)
- [Model Selection](../concepts/model-selection.md)
- [Retrieval-Augmented Generation (RAG)](../concepts/rag.md)
- [Self-Reflective RAG](../concepts/self-reflective-rag.md)
- [Semantic Search](../concepts/semantic-search.md)
- [Chunking](../concepts/chunking.md)
- [Local & Self-Hosted AI](../concepts/local-ai.md)
- [Tool Design](../concepts/tool-design.md)

## Entities

- [DeepSeek R1](../entities/tools/deepseek-r1.md)
- [Ollama](../entities/tools/ollama.md)
- [Hugging Face](../entities/organizations/hugging-face.md)
- [Chroma](../entities/tools/chroma.md)
- [LangChain](../entities/tools/langchain.md)
- [Qwen](../entities/tools/qwen.md)
- [Pydantic AI](../entities/tools/pydantic-ai.md)
- [OpenAI](../entities/organizations/openai.md)
- [Cole Medin](../entities/people/cole-medin.md)

## Key moments

- **[0:00:34]** Core idea: combine slow powerful reasoning models (R1) with faster lightweight models that direct the flow, treating R1 as a tool
- **[0:01:53]** High-level architecture diagram: fast primary agent + a single RAG tool box wrapping vector DB retrieval into R1 reasoning
- **[0:05:10]** Explains R1 distill models: DeepSeek fine-tuned Qwen and Llama on R1-generated data to make small local reasoning models
- **[0:08:29]** Creates the CodeAgent reasoning model with max_steps=2 to prevent hallucination loops
- **[0:10:37]** Defines the rag_with_reasoner tool: similarity search top-3 chunks, format, feed to R1
- **[0:11:54]** Prompt lets R1 return a better query to the primary LLM for retry, making it true agentic RAG
- **[0:15:46]** Ollama context-limit gotcha: default 2048 tokens causes hallucinations; build a model file to raise it to 8192+
- **[0:19:57]** Live demo: Qwen calls the RAG tool, R1 reasons over context, final answer returned

## Transcript

[Raw transcript](../raw/you-have-to-try-agentic-rag-with-deepseek-r1-insane-results.md)
