---
type: source
title: "I Forked Bolt.new and Made it WAY Better"
description: "Because Bolt.new is open source, you can fork it and run it locally to break its two biggest limits, usage caps and being locked to a single model, by adding a model dropdown that supports any provider or local LLM."
youtube_id: 3PFcAu_oU80
url: https://www.youtube.com/watch?v=3PFcAu_oU80
slug: i-forked-boltnew-and-made-it-way-better
published: 2024-10-13
duration: "0:19:30"
recency_rank: 153
raw: "../raw/i-forked-boltnew-and-made-it-way-better.md"
tags: [open-source, ai-coding, bolt-new, provider-independence]
created: 2026-07-21
updated: 2026-07-21
---

# I Forked Bolt.new and Made it WAY Better

Cole walks through forking Bolt.new, the open-source browser-based full-stack AI development platform, to fix its two main frustrations: limited usage credits and being hardcoded to Claude 3.5 Sonnet. By running the fork locally you pay nothing (especially with local models) and gain a model-selection dropdown that exposes providers like Anthropic, OpenAI, Groq, and any Ollama-hosted local coding model (Qwen 2.5 Coder, DeepSeek Coder, CodeLlama). You can even switch models mid-conversation.

He then explains the technical changes behind the fork. A constants file defines the default model, default provider, and a list of model objects (model ID, display label, provider). The front end gains model state passed to the backend by embedding the model into the user message content (a workaround for the Vercel AI SDK's useChat hook not accepting extra parameters), then stripped out via regex before display and before sending to the LLM. The backend extracts the latest selected model, resolves the API key via a provider switch statement, and instantiates the model through the corresponding Vercel AI SDK provider package.

The broader lesson is the leverage of open source: forking an application gives you full source access to extend it. Adding new models for an existing provider is trivial (copy a record, change the ID and label), and adding a whole new provider (Fireworks, Together AI) just means a new SDK provider function plus API-key wiring. Cole notes smaller local models (7B) sometimes fail inside Bolt's WebContainer because Bolt's system prompts are massive, but they remain surprisingly capable.

## Concepts covered

- [Provider Independence](../concepts/provider-independence.md)
- [Model Selection](../concepts/model-selection.md)
- [Learn by Building](../concepts/learn-by-building.md)
- [Local & Self-Hosted AI](../concepts/local-ai.md)
- [Vibe Coding](../concepts/vibe-coding.md)

## Entities

- [bolt.new](../entities/tools/bolt-new.md)
- [Ollama](../entities/tools/ollama.md)
- [Vercel AI SDK](../entities/tools/vercel-ai-sdk.md)
- [Anthropic](../entities/organizations/anthropic.md)
- [OpenAI](../entities/organizations/openai.md)
- [Groq](../entities/organizations/groq.md)
- [Cole Medin](../entities/people/cole-medin.md)

## Key moments

- **[0:00:45]** The two problems with Bolt.new: limited usage and locked to Claude 3.5 Sonnet
- **[0:03:47]** Reveals the fork's key difference: a model-selection dropdown
- **[0:05:16]** Demonstrates switching models mid-conversation to a local Qwen 2.5 Coder 7B
- **[0:06:42]** Small local model output is janky in the WebContainer because Bolt's prompts are massive
- **[0:11:02]** Walks the constants file: default model/provider plus the model list objects
- **[0:14:13]** Passing the model to the backend by embedding it in the user message content
- **[0:16:32]** Backend resolves API key and model instance via provider switch statements
- **[0:17:35]** Extending to a new provider (Fireworks/Together) via the Vercel AI SDK

## Transcript

[Raw transcript](../raw/i-forked-boltnew-and-made-it-way-better.md)
