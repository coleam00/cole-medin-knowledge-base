---
type: entity
subtype: tool
title: "oTToDev (autod Dev)"
description: "Community fork of bolt.new that adds support for any LLM, including local models via Ollama; the tool this video is built around."
resource: "https://github.com/coleam00/bolt.new-any-llm"
tags: [ai-coding, open-source, app-builder]
videos: [ottodev-is-becoming-the-best-open-source-ai-coding-assistant, how-to-use-boltnew-for-free-with-local-llms-and-no-rate-limits]
created: 2026-07-21
updated: 2026-07-21
---

# oTToDev (autod Dev)

oTToDev (transcribed in Cole's videos as "autod Dev") is the community fork of [bolt.new](./bolt-new.md) that started life as "bolt.new-any-llm." Cole defines its founding purpose directly: "we as a community started autod Dev, a fork of bolt.new, that aims to implement a bunch of much needed features including being able to use any large language model like local ones with Ollama." The shared goal, repeated across the videos, is to build "the best open-source AI coding assistant."

Its headline capability is [provider independence](../../concepts/provider-independence.md): unlike the single-LLM commercial product, oTToDev lets you plug in any [model](../../concepts/model-selection.md), cloud or [local](../../concepts/local-ai.md) via Ollama, and Cole regularly stress-tests brand-new models (DeepSeek R1, Qwen, o3-mini) through it. That flexibility surfaces real [context-window](../../concepts/context-window-limits.md) and [iterative-prompting](../../concepts/iterative-prompting.md) tradeoffs between models. Setup is documented in the repo README, and Cole covers running it "both with Docker and without Docker."

oTToDev is a stage in a single evolving [open-source](../../concepts/open-source-ai-coding.md) project, not a separate tool: bolt.new -> bolt.new-any-llm -> oTToDev / [autodev](./autodev.md) -> [bolt.diy](./bolt-diy.md). After the StackBlitz partnership made it the official open-source bolt.new, it was renamed to bolt.diy, so this page and its siblings describe the same lineage under the names Cole used at each point in time.

## Realizes

- [Open-Source & Local AI Coding](../../concepts/open-source-ai-coding.md) - Community-maintained, self-hostable AI coding tools and local models that dodge API costs and rate limits.
- [Provider Independence](../../concepts/provider-independence.md) - Architecting agents so the underlying model, framework, or client can be swapped without a rewrite, avoiding lock-in through low-level abstractions.
- [Local & Self-Hosted AI](../../concepts/local-ai.md) - Running open-weight models on your own hardware or cloud for privacy, cost control, and independence from API providers.
- [Model Selection](../../concepts/model-selection.md) - Choosing the right LLM per task by trading off quality, speed, and cost, often routing easy requests to cheap models and hard ones to expensive models.
- [Context Window Limits](../../concepts/context-window-limits.md) - Managing finite context by summarizing, compacting, and sizing what you load so the model stays sharp on long tasks.
- [Iterative Prompting](../../concepts/iterative-prompting.md) - Build complex software by prompting for a minimal baseline first and adding one change at a time to minimize hallucination.
- [Model-Specific Prompts](../../concepts/model-specific-prompts.md) - Different LLMs need different prompts, so a serious system keeps a library of model-tuned system prompts instead of reusing one prompt written for a single frontier model.
- [Ollama's Default Context Window](../../concepts/ollama-context-window.md) - Every Ollama model ships with a 2048-token context window that silently truncates history and tool output; the fix is a two-line Modelfile that raises num_ctx.

## Related

- [bolt.new](./bolt-new.md) - StackBlitz's commercial AI coding platform that generates entire full-stack applications; the stable product bolt.DIY forks from.
- [autodev (bolt.new fork)](./autodev.md) - Cole's community-built fork of bolt.new, used to generate the front-end wrapper (vanilla JS/HTML) that embeds the Voiceflow chat widget.
- [bolt.diy](./bolt-diy.md) - Front-end build tools cited as examples of domains that already have strong built-in self-correction, so the knowledge-graph MCP isn't needed there.
- [DeepSeek Coder V2](./deepseek-coder-v2.md) - Open-source 236B-parameter coding model available via OpenRouter or the DeepSeek API, recommended as roughly 20x cheaper than Claude while remaining highly capable for AI coding.
- [Mistral](../organizations/mistral.md) - French AI lab and LLM provider whose models were added to the bolt.new fork as a first-class API integration by popular community request.

## Sources

- [oTToDev is Becoming the BEST Open Source AI Coding Assistant](../../sources/ottodev-is-becoming-the-best-open-source-ai-coding-assistant.md) - "[0:00:00] we are building to be the best open- source AI coding assistant"
- [How to Use Bolt.new for FREE with Local LLMs (And NO Rate Limits)](../../sources/how-to-use-boltnew-for-free-with-local-llms-and-no-rate-limits.md) - "[0:00:00] we as a community started autod Dev a for bolt.new that aims to implement a bunch of much needed features including being able to use any large language model like local ones with Ollama"
