---
type: source
title: "DeepSeek R1 Just Revolutionized AI Forever"
description: "DeepSeek R1 is an open-source reasoning LLM that rivals OpenAI's o1 at a fraction of the cost, ships in distilled sizes you can run locally, and outperforms Claude 3.5 Sonnet as a coding assistant in a one-shot app build."
youtube_id: -GmEIqi0yNE
url: https://www.youtube.com/watch?v=-GmEIqi0yNE
slug: deepseek-r1-just-revolutionized-ai-forever
published: 2025-01-22
duration: "0:21:08"
recency_rank: 123
raw: "../raw/deepseek-r1-just-revolutionized-ai-forever.md"
tags: [reasoning-models, open-source, local-ai, deepseek]
created: 2026-07-21
updated: 2026-07-21
---

# DeepSeek R1 Just Revolutionized AI Forever

Cole introduces DeepSeek R1, a newly released MIT-licensed open-source reasoning model that 'thinks' to itself before giving a final answer. He walks through DeepSeek's blog benchmarks showing R1 performing on par with OpenAI's o1 across most tasks while being dramatically cheaper (~$0.55/M input, ~$2.19/M output), and highlights that DeepSeek distilled R1's reasoning into smaller Qwen- and Llama-based versions so almost anyone can run a capable model locally. He shows that even the 14B distilled Qwen version is on par with o1-mini.

He demonstrates running the distilled models locally two ways: via Ollama (copy a run command into a terminal) and via Hugging Face (choosing quantizations for LM Studio and llama.cpp). He explains the anatomy of reasoning-model output: everything inside the thinking tags is the model reasoning to itself and should be stripped when you only want to surface the final response in an AI agent.

The centerpiece is a head-to-head coding test inside bolt.diy, his open-source bolt.new fork. Using the full 671B R1 through the DeepSeek API, he one-shots a chat interface for an n8n agent (with Supabase auth and history) for under a penny (~9,000 tokens), and it looks and works better than a comparable Lovable build and better than the same prompt run through Claude 3.5 Sonnet, which produced a nicer-than-expected but non-functional result. The takeaway: powerful open reasoning models free builders from depending solely on Anthropic/OpenAI APIs.

## Concepts covered

- [Reasoning Models](../concepts/reasoning-models.md)
- [Model Selection](../concepts/model-selection.md)
- [Fine-Tuning](../concepts/fine-tuning.md)
- [Local & Self-Hosted AI](../concepts/local-ai.md)
- [Model Quantization](../concepts/model-quantization.md)
- [Vibe Coding](../concepts/vibe-coding.md)

## Entities

- [DeepSeek R1](../entities/tools/deepseek-r1.md)
- [DeepSeek](../entities/organizations/deepseek.md)
- [Ollama](../entities/tools/ollama.md)
- [Hugging Face](../entities/organizations/hugging-face.md)
- [bolt.diy](../entities/tools/bolt-diy.md)
- [Lovable](../entities/tools/lovable.md)
- [n8n](../entities/tools/n8n.md)
- [Supabase](../entities/tools/supabase.md)
- [OpenAI](../entities/organizations/openai.md)
- [Anthropic](../entities/organizations/anthropic.md)
- [OpenRouter](../entities/tools/openrouter.md)
- [Cole Medin](../entities/people/cole-medin.md)

## Key moments

- **[0:00:00]** Intro to reasoning LLMs that think before answering; DeepSeek releases R1
- **[0:01:21]** DeepSeek R1 blog: MIT-licensed, fully open source, thinking model
- **[0:02:55]** Benchmarks vs o1/o1-mini/DeepSeek V3 (with grain-of-salt caveat)
- **[0:03:42]** Distilled Qwen/Llama versions; 14B on par with o1-mini
- **[0:04:48]** Pricing: ~55c/M input, ~$2.19/M output; dozens of times cheaper than o1
- **[0:06:06]** Running R1 via Ollama; 671B Q4 is ~400GB and too big for consumer hardware
- **[0:07:50]** Anatomy of reasoning output: strip everything inside thinking tags
- **[0:09:00]** Installing distilled R1 via Hugging Face quantizations for LM Studio / llama.cpp
- **[0:10:28]** bolt.diy test setup: build an n8n chat interface with the 671B R1 via DeepSeek API
- **[0:15:14]** R1 one-shots the full app for ~9,000 tokens (fractions of a penny)
- **[0:18:29]** Head-to-head: same prompt on Claude 3.5 Sonnet looks decent but does not function

## Transcript

[Raw transcript](../raw/deepseek-r1-just-revolutionized-ai-forever.md)
