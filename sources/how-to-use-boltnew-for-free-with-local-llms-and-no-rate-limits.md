---
type: source
title: "How to Use Bolt.new for FREE with Local LLMs (And NO Rate Limits)"
description: "You can run bolt.new-style AI app-building entirely on free local LLMs via the oTToDev fork and Ollama, provided you fix Ollama's tiny default context window and prompt incrementally from simple to complex."
youtube_id: 8ommGcs_-VU
url: https://www.youtube.com/watch?v=8ommGcs_-VU
slug: how-to-use-boltnew-for-free-with-local-llms-and-no-rate-limits
published: 2024-11-06
duration: "0:16:10"
recency_rank: 145
raw: "../raw/how-to-use-boltnew-for-free-with-local-llms-and-no-rate-limits.md"
tags: [local-ai, ollama, context-window, prompting, open-source]
created: 2026-07-21
updated: 2026-07-21
---

[Cole Medin](../entities/people/cole-medin.md) introduces [oTToDev](../entities/tools/ottodev.md), a community fork of [bolt.new](../entities/tools/bolt-new.md) that unlocks using any large language model, including local ones through [Ollama](../entities/tools/ollama.md), instead of bolt.new's single hardcoded Claude 3.5 Sonnet. The appeal of local models is no cost and no rate limits, and Cole demonstrates that even a small model like [Qwen](../entities/tools/qwen.md) 2.5 Coder 7B can build a full application well enough to serve as a strong starting point.

The video's core technical tip is fixing Ollama's default context length, which is only about 2048 tokens and too small to fit bolt.new's large system prompt, causing the model to chat in plain text instead of opening the web container and writing files. The fix is a small Ollama Modelfile (FROM the base model plus a num_ctx PARAMETER above 8192, recommended 32768) run through `ollama create` to produce a new higher-context variant that works dramatically better inside the tool.

Cole then shares prompting strategy: start with a very simple prompt to get a working (if ugly) baseline, then iterate with increasingly detailed requirements, including explicit UI and UX design details like colors, padding, and measurements, which guides even larger models better and minimizes hallucinations. He builds a Next.js chat interface that calls an [n8n](../entities/tools/n8n.md) AI agent (webhook endpoint, RAG over a [Postgres](../entities/tools/postgres-pgvector.md) PGVector knowledge base) and notes model-selection tradeoffs: closed models like Claude and GPT-4o are strongest, but DeepSeek Coder V2 236B via [OpenRouter](../entities/tools/openrouter.md) or the DeepSeek API is 20x cheaper than Claude while still open source and capable.

## Concepts covered

- [Open-Source & Local AI Coding](../concepts/open-source-ai-coding.md)
- [Provider Independence](../concepts/provider-independence.md)
- [Context Window Limits](../concepts/context-window-limits.md)
- [Local & Self-Hosted AI](../concepts/local-ai.md)
- [Iterative Prompting](../concepts/iterative-prompting.md)
- [Prompting Techniques for AI Coding](../concepts/ai-coding-prompting.md)
- [Model Selection](../concepts/model-selection.md)
- [Retrieval-Augmented Generation (RAG)](../concepts/rag.md)

## Entities

- [oTToDev (autod Dev)](../entities/tools/ottodev.md)
- [bolt.new](../entities/tools/bolt-new.md)
- [Ollama](../entities/tools/ollama.md)
- [Qwen 2.5 Coder 32B](../entities/tools/qwen.md)
- [n8n](../entities/tools/n8n.md)
- [OpenRouter](../entities/tools/openrouter.md)
- [Postgres](../entities/tools/postgres-pgvector.md)
- [Cole Medin](../entities/people/cole-medin.md)

## Key moments

- **[0:00:00]** Intro: oTToDev fork of bolt.new adds ability to use any LLM including local ones via Ollama
- **[0:00:35]** Plan: build an app with the small Qwen 2.5 Coder 7B local model that chats with an n8n AI agent
- **[0:03:08]** Problem: local model just chats and never opens the web container or writes files
- **[0:03:54]** Root cause: Ollama's default context length (~2048) is too small for bolt.new's prompt
- **[0:04:41]** Fix: create an Ollama Modelfile with num_ctx above 8192 (recommend 32768) via ollama create
- **[0:06:36]** With the higher-context variant, the model opens the code window and builds correctly
- **[0:08:37]** Model selection: recommends DeepSeek Coder V2 236B as a cheap, open-source, capable alternative
- **[0:10:35]** Prompting strategy: start simple and iterate to more complex to reduce hallucinations
- **[0:11:48]** Second iteration: add detailed UI/UX requirements (colors, padding, measurements)
- **[0:12:58]** Third iteration: wire the app to an n8n agent webhook with RAG over PGVector
- **[0:14:28]** Working result: the local-LLM-built app talks to the n8n agent and answers from its knowledge base

## Transcript

[Raw transcript](../raw/how-to-use-boltnew-for-free-with-local-llms-and-no-rate-limits.md)
