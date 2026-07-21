---
type: entity
subtype: tool
title: "DeepSeek R1"
description: "Open-source MIT-licensed reasoning LLM that rivals OpenAI o1, ships in distilled sizes, and is far cheaper to run."
resource: "https://api-docs.deepseek.com/news/news250120"
tags: [llm, reasoning-model, open-source, local-ai]
videos: [the-ultimate-guide-to-local-ai-and-ai-agents-the-future-is-here, lets-settle-the-o3-mini-vs-r1-debate-for-coding-once-and-for-all, you-have-to-try-agentic-rag-with-deepseek-r1-insane-results, deepseek-r1-just-revolutionized-ai-forever]
created: 2026-07-21
updated: 2026-07-21
---

# DeepSeek R1

DeepSeek R1 is an open-source, MIT-licensed [reasoning model](../../concepts/reasoning-models.md) that landed as a genuine shock to the field. Cole introduces it as exactly that: "deep seek is getting in on this game they have just released an incredible new open-source reasoning llm called R1" [0:00:16], and stresses the punchline that a freely downloadable model matched the frontier, "you can actually go and run a variation yourself or get something that is literally more powerful than open AI 01 Claude 3.5 son it basically every llm out there" [0:00:34]. It shipped in a full 671-billion-parameter version plus distilled sizes, making it his most-recommended local reasoning model.

## How Cole uses it

R1's headline appeal is closed-model reasoning quality at open-source cost and control. He calls it "the most popular local LLM ever ... the best part about DeepSeek R1 is they have an option that fits into each of the size ranges" [0:20:00], which is why it slots cleanly into his [local-AI](../../concepts/local-ai.md) stack: pick the distilled size your hardware allows, or run the "671 billion parameter model ... the massive version the real version of Deep seek R1" [0:04:38] via a provider.

He puts it to work as the reasoning brain inside [agentic RAG](../../concepts/agentic-rag.md), pairing R1's step-by-step thinking with a smaller Qwen conversation driver so the system reasons over retrieved context. He also benchmarks it head-to-head against OpenAI for coding, and R1 wins on output quality: "this looks so much better than the chess board built from 03 mini so the UI yet again goes to R1" [0:16:44]. The through-line is that R1 collapsed the price and access gap between reasoning models and everyone else: "deep seek R1 was kicking their Bud being open source and more powerful than all of their other models" [0:00:19].

## Related

- [Reasoning Models](../../concepts/reasoning-models.md) - R1 is his canonical open reasoning model
- [Model Selection](../../concepts/model-selection.md) - R1 for the reasoning role, cheaper than o1
- [Local & Self-Hosted AI](../../concepts/local-ai.md) - distilled sizes fit each hardware tier
- [Model Quantization](../../concepts/model-quantization.md) - shrinking R1 to run locally
- [Fine-Tuning](../../concepts/fine-tuning.md)
- [Vibe Coding](../../concepts/vibe-coding.md) - R1 vs. o3-mini for building UIs
- [DeepSeek V3](./deepseek-v3.md) - sibling DeepSeek model; [Qwen 2.5 Coder 32B](./qwen.md) - paired as conversation driver; [Ollama](./ollama.md) - local serving

## Sources

- [DeepSeek R1 Just Revolutionized AI Forever](../../sources/deepseek-r1-just-revolutionized-ai-forever.md) - "[0:00:34] you can actually go and run a variation yourself or get something that is literally more powerful than open AI 01 Claude 3.5 son it basically every llm out there"
- [The Ultimate Guide to Local AI and AI Agents (The Future is Here)](../../sources/the-ultimate-guide-to-local-ai-and-ai-agents-the-future-is-here.md) - "[0:20:00] This is the most popular local LLM ever ... the best part about DeepSeek R1 is they have an option that fits into each of the size ranges"
- [You HAVE to Try Agentic RAG with DeepSeek R1 (Insane Results)](../../sources/you-have-to-try-agentic-rag-with-deepseek-r1-insane-results.md) - "[0:00:00] deep seek R1 the latest and greatest open-source reasoning llm has taken the World by storm"
- [Let's Settle the o3-mini Vs. R1 Debate for Coding ONCE and for ALL](../../sources/lets-settle-the-o3-mini-vs-r1-debate-for-coding-once-and-for-all.md) - "[0:16:44] this looks so much better than the chess board built from 03 mini so the UI yet again goes to R1"
