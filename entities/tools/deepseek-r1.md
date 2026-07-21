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

DeepSeek R1 is an open-source, MIT-licensed [reasoning model](../../concepts/reasoning-models.md) that landed as a genuine shock to the field. Cole introduces it as exactly that: "DeepSeek is getting in on this game they have just released an incredible new open-source reasoning llm called R1" [0:00:16], and stresses the punchline that a freely downloadable model matched the frontier, "you can actually go and run a variation yourself or get something that is literally more powerful than OpenAI o1 Claude 3.5 Sonnet basically every llm out there" [0:00:34]. It shipped in a full 671-billion-parameter version plus distilled sizes, making it his most-recommended local reasoning model.

## How Cole uses it

R1's headline appeal is closed-model reasoning quality at open-source cost and control. He calls it "the most popular local LLM ever ... the best part about DeepSeek R1 is they have an option that fits into each of the size ranges" [0:20:00], which is why it slots cleanly into his [local-AI](../../concepts/local-ai.md) stack: pick the distilled size your hardware allows, or run the "671 billion parameter model ... the massive version the real version of DeepSeek R1" [0:04:38] via a provider.

He puts it to work as the reasoning brain inside [agentic RAG](../../concepts/agentic-rag.md), pairing R1's step-by-step thinking with a smaller Qwen conversation driver so the system reasons over retrieved context. He also benchmarks it head-to-head against OpenAI for coding, and R1 wins on output quality: "this looks so much better than the chess board built from o3-mini so the UI yet again goes to R1" [0:16:44]. The through-line is that R1 collapsed the price and access gap between reasoning models and everyone else: "DeepSeek R1 was kicking their Bud being open source and more powerful than all of their other models" [0:00:19].

## Realizes

- [Reasoning Models](../../concepts/reasoning-models.md) - Models that produce explicit reasoning before answering, and when that extra thinking helps versus hurts.
- [Mixture of Experts](../../concepts/mixture-of-experts.md) - A model architecture that routes each token through a subset of specialized expert networks, contrasted with a dense Transformer, explaining why two similar-looking reasoning LLMs behave very differently.

## Works with

- [Qwen](./qwen.md) - Alibaba's open-source LLM family Cole cites as among his favorites that stood the test of time.
- [Ollama](./ollama.md) - Local LLM runtime; works with a locally-run bolt.diy but can't be reached by a self-hosted (remote) instance.
- [LM Studio](./lm-studio.md) - Desktop app for downloading and running open-weight LLMs locally, the main alternative to Ollama and a requested provider integration for the bolt.new fork.
- [DeepSeek V3](./deepseek-v3.md) - New open model Cole cites as evidence the local-vs-closed gap is closing fast; he's using it heavily in his own stack and it's performing great.
- [smolagents](./smolagents.md) - Hugging Face's minimal agent framework whose base agent executes actions through generated code, used here to build an entire agentic RAG workflow in very little code.

## Related

- [QwQ](./qwq.md) - Alibaba's open reasoning model, cited as the kind of model that could draft a plan or README before any code is generated.
- [Model Selection](../../concepts/model-selection.md) - Choosing the right LLM per task by trading off quality, speed, and cost, often routing easy requests to cheap models and hard ones to expensive models.
- [Local & Self-Hosted AI](../../concepts/local-ai.md) - Running open-weight models on your own hardware or cloud for privacy, cost control, and independence from API providers.
- [Model Quantization](../../concepts/model-quantization.md) - Compressing model weights to lower precision so large models fit and run on limited local hardware.
- [Fine-Tuning](../../concepts/fine-tuning.md) - Adapting a base model to a task or domain via additional training, weighed against just prompting a stronger general model.
- [Vibe Coding](../../concepts/vibe-coding.md) - Building software by conversationally prompting an AI without closely reading the code, useful for prototypes but risky for production.

## Sources

- [DeepSeek R1 Just Revolutionized AI Forever](../../sources/deepseek-r1-just-revolutionized-ai-forever.md) - "[0:00:34] you can actually go and run a variation yourself or get something that is literally more powerful than OpenAI o1 Claude 3.5 Sonnet basically every llm out there"
- [The Ultimate Guide to Local AI and AI Agents (The Future is Here)](../../sources/the-ultimate-guide-to-local-ai-and-ai-agents-the-future-is-here.md) - "[0:20:00] This is the most popular local LLM ever ... the best part about DeepSeek R1 is they have an option that fits into each of the size ranges"
- [You HAVE to Try Agentic RAG with DeepSeek R1 (Insane Results)](../../sources/you-have-to-try-agentic-rag-with-deepseek-r1-insane-results.md) - "[0:00:00] DeepSeek R1 the latest and greatest open-source reasoning llm has taken the World by storm"
- [Let's Settle the o3-mini Vs. R1 Debate for Coding ONCE and for ALL](../../sources/lets-settle-the-o3-mini-vs-r1-debate-for-coding-once-and-for-all.md) - "[0:16:44] this looks so much better than the chess board built from o3-mini so the UI yet again goes to R1"
