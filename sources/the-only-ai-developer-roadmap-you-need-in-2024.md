---
type: source
title: "The ONLY AI Developer Roadmap You Need in 2024"
description: "A 10-step roadmap to go from zero to hero as an AI developer: master fundamentals fast, do not over-invest in prompt engineering or custom model training, and spend most of your time on LLM app-building, RAG, and AI agents."
youtube_id: 2NjuPJjx3zI
url: https://www.youtube.com/watch?v=2NjuPJjx3zI
slug: the-only-ai-developer-roadmap-you-need-in-2024
published: 2024-06-26
duration: "0:15:53"
recency_rank: 188
raw: "../raw/the-only-ai-developer-roadmap-you-need-in-2024.md"
tags: [learn-by-building, rag, what-is-an-ai-agent, model-selection]
created: 2026-07-21
updated: 2026-07-21
---

# The ONLY AI Developer Roadmap You Need in 2024

Cole lays out a sequential 10-step learning path for becoming an AI developer in 2024. The early steps are foundational and meant to be moved through quickly: master Python (functions, OOP, basics, do not spend six months), learn how AI models and LLMs are trained and where they fail, and pick up prompt engineering (a few hours is enough, he explicitly pushes back on gurus who frame prompt engineering as a $300k career). Deep learning, ML, and NLP are marked optional, because GPT and Claude are powerful enough for most use cases; you only need to train custom models for specialized tasks (his example: a builder.io-style figma-to-code model where general GPT failed).

The middle steps are where real value accrues. Step five is building basic projects directly against the OpenAI and Anthropic SDKs in Python (chatbots, summarizers, idea generators) and, critically, learning to read SDK documentation instead of leaning on tutorials. Step six is LangChain, his favorite tool, a suite of Python libraries that handle chat memory, chains, output parsing, and prompt templating so you build faster and with fewer errors. Step seven is RAG (retrieval augmented generation): augmenting an LLM with external knowledge via vector databases and embeddings so the model has the context it needs.

Step eight, AI agents, is where he spends most of his own time and says takes the most effort: the LangChain suite (LangGraph for multi-agent infrastructure, LangServe for deployment, LangSmith for observability) plus LLM function calling to let agents interact with databases, APIs, and services, plus cloud deployment. Step nine is building front ends (HTML/CSS/JS, React/Next.js, the Vercel AI SDK) so real users can access the app. Step ten is a grab-bag of advanced, use-case-dependent topics: fine-tuning, multimodal models, explainable AI, mixture of agents, and app development for mobile.

## Concepts covered

- [Learn by Building](../concepts/learn-by-building.md)
- [Rapid Prototyping](../concepts/rapid-prototyping.md)
- [Prompt Engineering](../concepts/prompt-engineering.md)
- [Model Selection](../concepts/model-selection.md)
- [Retrieval-Augmented Generation (RAG)](../concepts/rag.md)
- [Vector Embeddings](../concepts/vector-embeddings.md)
- [What Is an AI Agent](../concepts/what-is-an-ai-agent.md)
- [Tool Calling](../concepts/tool-use.md)
- [Agent Deployment](../concepts/agent-deployment.md)
- [Generative UI](../concepts/generative-ui.md)
- [Fine-Tuning](../concepts/fine-tuning.md)
- [Multi-Model Agents](../concepts/multi-model-agent.md)

## Entities

- [Cole Medin](../entities/people/cole-medin.md)
- [Python](../entities/tools/python.md)
- [OpenAI](../entities/organizations/openai.md)
- [Anthropic](../entities/organizations/anthropic.md)
- [LangChain](../entities/tools/langchain.md)
- [LangGraph](../entities/tools/langgraph.md)
- [LangServe](../entities/tools/langserve.md)
- [LangSmith](../entities/tools/langsmith.md)
- [Pinecone](../entities/tools/pinecone.md)
- [React](../entities/tools/react.md)
- [Vercel AI SDK](../entities/tools/vercel-ai-sdk.md)

## Key moments

- **[0:00:00]** Intro: condensing years of AI learning into a zero-to-hero roadmap
- **[0:01:20]** Step 1: Master Python (basics, do not over-invest)
- **[0:02:20]** Step 2: Basics of AI and LLMs (how they are trained, pitfalls)
- **[0:03:37]** Step 3: Prompt engineering (a few hours is enough; pushback on gurus)
- **[0:04:38]** Step 4: Deep learning / ML / NLP marked as OPTIONAL
- **[0:05:44]** builder.io figma-to-code example: when a custom model is worth it
- **[0:07:00]** Step 5: Build basic projects on OpenAI/Anthropic SDKs; learn to read docs
- **[0:08:21]** Step 6: LangChain, his favorite AI tool
- **[0:09:33]** Step 7: RAG, vector databases and embeddings
- **[0:10:26]** Step 8: AI agents: LangGraph/LangServe/LangSmith plus function calling plus deploy
- **[0:12:22]** Step 9: Front ends (React/Next.js, Vercel AI SDK)
- **[0:13:47]** Step 10: Advanced use-case topics: fine-tuning, multimodal, mixture of agents

## Transcript

[Raw transcript](../raw/the-only-ai-developer-roadmap-you-need-in-2024.md)
