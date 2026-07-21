---
type: entity
subtype: tool
title: "SearXNG"
description: "Local, private metasearch engine added for web search (with Redis for caching); kept private since it isn't password protected."
resource: "https://github.com/searxng/searxng"
tags: [web-search, local-ai, self-hosted]
videos: [the-ultimate-guide-to-local-ai-and-ai-agents-the-future-is-here, create-your-own-private-local-ai-cloud-stack-in-under-20-minutes]
created: 2026-07-21
updated: 2026-07-21
---

# SearXNG

SearXNG is the open-source metasearch engine Cole runs inside his self-hosted stack to give local agents web search without ever leaving the private network. He describes adding "SearXNG for open-source completely free and private web search" ([0:57:00]), and it is what lets a fully offline agent still reach the internet: one of his n8n agents "has a tool to use SearXNG for local and private web search" ([1:14:00]). It is the local-first counterpart to a hosted search API like [Brave Search](./brave-search.md), trading Brave's AI-summarized cloud results for search that stays entirely under Cole's control.

## How Cole uses it / why it matters

SearXNG is a piece of Cole's [local and self-hosted AI](../../concepts/local-ai.md) cloud stack, the same private environment where he runs local models, and it exists to close the one capability gap that self-hosting usually forces you to give up: live web access. Rather than call out to a third-party search provider, the agent queries a metasearch engine Cole controls, which aggregates results from many upstream search engines and returns them privately. He recently folded it into the stack alongside a cache layer: "recently I added SearXNG for local and private web search which includes Redis for caching" ([0:02:12]), where Redis speeds up repeated queries.

Because the point is [provider independence](../../concepts/provider-independence.md), the same value proposition that drives Cole toward local LLMs, [model quantization](../../concepts/model-quantization.md), and careful [model selection](../../concepts/model-selection.md) applies to search: nothing about the query or its results is exposed to an outside vendor. That privacy posture comes with an operational caveat Cole flags directly, since the SearXNG instance is not password protected by default it should be kept private, not exposed publicly, so it isn't left open to the internet. In practice it slots into his no-code agents as just another tool node, giving a [local LLM acting as an agent](../../concepts/local-llms-as-agents.md) the ability to ground its answers in current web results the same way a cloud agent would with Brave.

## Realizes

- [Local & Self-Hosted AI](../../concepts/local-ai.md) - Running open-weight models on your own hardware or cloud for privacy, cost control, and independence from API providers.
- [Provider Independence](../../concepts/provider-independence.md) - Architecting agents so the underlying model, framework, or client can be swapped without a rewrite, avoiding lock-in through low-level abstractions.

## Contrasts with

- [Brave Search API](./brave-search.md) - Web search API wired up as the single example tool giving the template agent the ability to search the web.

## Related

- [Local LLMs as Agents](../../concepts/local-llms-as-agents.md) - Using openly downloadable, self-hosted models for agentic work, which hinges on the model's ability to do reliable function calling.
- [Model Quantization](../../concepts/model-quantization.md) - Compressing model weights to lower precision so large models fit and run on limited local hardware.
- [Model Selection](../../concepts/model-selection.md) - Choosing the right LLM per task by trading off quality, speed, and cost, often routing easy requests to cheap models and hard ones to expensive models.
- [Fine-Tuning](../../concepts/fine-tuning.md) - Adapting a base model to a task or domain via additional training, weighed against just prompting a stronger general model.
- [Context Window Limits](../../concepts/context-window-limits.md) - Managing finite context by summarizing, compacting, and sizing what you load so the model stays sharp on long tasks.
- [grep (command-line search)](./ripgrep.md) - The default CLI search Claude Code uses for agentic navigation; the video argues it becomes slow and token-inefficient past six-figure line counts, motivating LSP.

## Sources

- [The Ultimate Guide to Local AI and AI Agents (The Future is Here)](../../sources/the-ultimate-guide-to-local-ai-and-ai-agents-the-future-is-here.md) - "[0:57:00] SearXNG for open-source completely free and private web search."
- [The Ultimate Guide to Local AI and AI Agents (The Future is Here)](../../sources/the-ultimate-guide-to-local-ai-and-ai-agents-the-future-is-here.md) - "[1:14:00] This one has a tool to use SearXNG for local and private web search."
- [Create Your Own Private Local AI Cloud Stack in Under 20 Minutes](../../sources/create-your-own-private-local-ai-cloud-stack-in-under-20-minutes.md) - "[0:02:12] recently I added SearXNG for local and private web search which includes Redis for caching."
