---
type: source
title: "Qwen Just Casually Started the Local AI Revolution"
description: "Qwen 2.5 Coder 32B closes the gap between free, locally-run open-source LLMs and expensive closed models like Sonnet and o1, making capable local coding and agent workloads practical for the first time."
youtube_id: y6Wh4SpRoao
url: https://www.youtube.com/watch?v=y6Wh4SpRoao
slug: qwen-just-casually-started-the-local-ai-revolution
published: 2024-11-13
duration: "0:16:06"
recency_rank: 143
raw: "../raw/qwen-just-casually-started-the-local-ai-revolution.md"
tags: [local-ai, qwen, quantization, model-selection, agents]
created: 2026-07-21
updated: 2026-07-21
---

[Cole Medin](../entities/people/cole-medin.md) reacts to the release of [Qwen 2.5 Coder 32B](../entities/tools/qwen.md), an open-source coding model he runs entirely locally and for free via [Ollama](../entities/tools/ollama.md). He argues that until now local LLMs simply were not powerful enough for real work, but this model changes that: he demonstrates it building a React + Tailwind chat interface inside [oTToDev](../entities/tools/ottodev.md) (his [bolt.new](../entities/tools/bolt-new.md) fork) and driving a non-trivial [LangChain](../entities/tools/langchain.md) / [LangGraph](../entities/tools/langgraph.md) agent, results so strong he had to check it was not secretly using o1.

The video doubles as a practical primer on running local models. Cole covers hardware requirements, recommending at least one NVIDIA 3090 for the 32B model, how to pull models through Ollama, and quantization as the lever to shrink a model's size (for example a Q2 build at 12GB instead of 20GB) at a small performance cost so weaker machines can still run it. He also points to the 14B variant as a lighter alternative.

To prove the model's edge, he contrasts it against Code Llama 34B, a slightly larger model that fails a basic build by never running npm install or Vite, and recalls [Llama](../entities/tools/llama.md) 3.1 70B failing the same agent tests. His custom agent exercises [Asana](../entities/tools/asana.md) task tools, Google Drive file search and download, and a local [Chroma](../entities/tools/chroma.md) vector database for RAG over meeting notes, all of which Qwen handles well. The throughline: local, open-source AI is now good enough for always-on agents where paying per-token API costs would be impractical.

## Concepts covered

- [Local & Self-Hosted AI](../concepts/local-ai.md)
- [Model Quantization](../concepts/model-quantization.md)
- [Model Selection](../concepts/model-selection.md)
- [Agentic Coding](../concepts/agentic-coding.md)
- [Agentic RAG](../concepts/agentic-rag.md)
- [Human in the Loop](../concepts/human-in-the-loop.md)

## Entities

- [Qwen 2.5 Coder 32B](../entities/tools/qwen.md)
- [Ollama](../entities/tools/ollama.md)
- [bolt.new](../entities/tools/bolt-new.md)
- [LangChain](../entities/tools/langchain.md)
- [LangGraph](../entities/tools/langgraph.md)
- [Chroma](../entities/tools/chroma.md)
- [Streamlit](../entities/tools/streamlit.md)
- [Asana](../entities/tools/asana.md)
- [Cole Medin](../entities/people/cole-medin.md)

## Key moments

- **[0:00:32]** Announces Qwen 2.5 Coder 32B was released Nov 11 2024, downloaded and tested it overnight
- **[0:01:53]** Primer on running local models: Ollama, the Qwen 2.5 Coder page, pulling the model
- **[0:02:37]** Hardware requirements: recommends at least one NVIDIA 3090 for the 32B model
- **[0:03:36]** Explains quantization: shrink model size significantly for a small performance hit (Q2 = 12GB vs 20GB)
- **[0:04:24]** Builds a React/Tailwind chat interface in oTToDev (bolt.new fork) with iterative prompting
- **[0:06:22]** Code Llama 34B fails the same build, never runs npm install / Vite
- **[0:07:47]** Sponsor segment: Novita AI cloud LLM platform
- **[0:09:45]** Tests Qwen with a custom LangChain/LangGraph agent that pushes LLM limits
- **[0:11:30]** Agent calls Asana tools to list projects and create a task due the 18th
- **[0:12:43]** Agent downloads meeting notes from Google Drive and adds them to a Chroma knowledge base, then answers via RAG

## Transcript

[Raw transcript](../raw/qwen-just-casually-started-the-local-ai-revolution.md)
