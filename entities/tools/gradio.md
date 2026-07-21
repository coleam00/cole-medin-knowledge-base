---
type: entity
subtype: tool
title: "Gradio"
description: "Python UI framework for ML/LLM apps, integrated directly into smolagents so an agent gets a full chat interface in a single line of code."
resource: "https://www.gradio.app"
tags: [no-code, app-builder]
videos: [you-have-to-try-agentic-rag-with-deepseek-r1-insane-results]
created: 2026-07-21
updated: 2026-07-21
---

# Gradio

Gradio is a Python framework for putting a web UI in front of machine-learning and LLM code without writing frontend. In Cole's work it earns its place through one property: it is wired straight into the agent framework, so the interface stops being a project of its own. Building the frontend for a local agentic RAG assistant, he sums up the entire step as - "now to create the user interface with small agents it is a single line of code because they are integrated directly with gradio UI" [0:13:25]. One import, one call, and the agent has a browser chat window with history and streaming.

That single line is doing more work than it looks. In the [agentic RAG](../../concepts/agentic-rag.md) build it wraps a [smolagents](./smolagents.md) tool-calling agent that reaches for a [DeepSeek R1](./deepseek-r1.md)-backed retrieval tool over a [Chroma](./chroma.md) vector store, with everything running locally through [Ollama](./ollama.md). The whole stack is offline and open, and Gradio is the piece that makes it feel like a product instead of a terminal script.

The value is squarely in [rapid prototyping](../../concepts/rapid-prototyping.md). Cole's repeated pattern is to prove the agent logic first and defer interface work until the logic is worth wrapping, and a one-line UI is the cheapest possible way to honor that ordering: you get something demoable the moment the agent works, and you have spent effectively zero engineering on a surface you may throw away. When a build graduates past the demo stage, the [chat interface](../../concepts/chat-interfaces.md) usually moves to something with real session handling and adapters, but Gradio is what gets a local agent in front of a human on day one.

## Realizes

- [Chat Interfaces](../../concepts/chat-interfaces.md) - Wrapping agents in chat surfaces so a human can actually use them, here in a single line of code.
- [Rapid Prototyping](../../concepts/rapid-prototyping.md) - Proving the agent out fast and deferring real frontend work until the logic earns it.
- [Local & Self-Hosted AI](../../concepts/local-ai.md) - Serving the UI from the same machine as the models, keeping the entire stack offline.

## Works with

- [smolagents](./smolagents.md) - Hugging Face's minimal agent framework, integrated with Gradio directly so the UI comes free with the agent.
- [DeepSeek R1](./deepseek-r1.md) - The reasoning model wrapped as a retrieval tool behind the Gradio chat window.
- [Ollama](./ollama.md) - The local runtime serving both models behind the interface.
- [Chroma](./chroma.md) - The vector store the agent's RAG tool searches before answering.

## Contrasts with

- [Streamlit](./streamlit.md) - The other Python-native way Cole builds a quick chat UI, used when the agent is not a smolagents build.
- [Open Web UI](./open-web-ui.md) - The heavier, self-hostable ChatGPT-style frontend with history, functions, and voice for agents that have outgrown a demo surface.

## Related

- [Agentic RAG](../../concepts/agentic-rag.md) - The workflow this UI fronts, where the agent decides when to search the knowledge base.
- [Reasoning Models](../../concepts/reasoning-models.md) - The slow-but-powerful model class the fast primary agent calls as a tool.
- [Tool Calling](../../concepts/tool-use.md) - The mechanism by which the chat agent reaches the retrieval tool.

## Sources

- [You HAVE to Try Agentic RAG with DeepSeek R1 (Insane Results)](../../sources/you-have-to-try-agentic-rag-with-deepseek-r1-insane-results.md) - "[0:13:25] now to create the user interface with small agents it is a single line of code because they are integrated directly with gradio UI"
