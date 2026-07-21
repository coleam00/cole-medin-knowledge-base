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

SearXNG is the open-source metasearch engine Cole runs inside his self-hosted stack to give local agents web search without ever leaving the private network. He describes adding "seir xng for open-source completely free and private web search" ([0:57:00]), and it is what lets a fully offline agent still reach the internet: one of his n8n agents "has a tool to use CRXNG for local and private web search" ([1:14:00]). It is the local-first counterpart to a hosted search API like [Brave Search](./brave-search.md), trading Brave's AI-summarized cloud results for search that stays entirely under Cole's control.

## How Cole uses it / why it matters

SearXNG is a piece of Cole's [local and self-hosted AI](../../concepts/local-ai.md) cloud stack, the same private environment where he runs local models, and it exists to close the one capability gap that self-hosting usually forces you to give up: live web access. Rather than call out to a third-party search provider, the agent queries a metasearch engine Cole controls, which aggregates results from many upstream search engines and returns them privately. He recently folded it into the stack alongside a cache layer: "recently I added CRX NG for local and private web search which includes reddis for caching" ([0:02:12]), where Redis speeds up repeated queries.

Because the point is [provider independence](../../concepts/provider-independence.md), the same value proposition that drives Cole toward local LLMs, [model quantization](../../concepts/model-quantization.md), and careful [model selection](../../concepts/model-selection.md) applies to search: nothing about the query or its results is exposed to an outside vendor. That privacy posture comes with an operational caveat Cole flags directly, since the SearXNG instance is not password protected by default it should be kept private, not exposed publicly, so it isn't left open to the internet. In practice it slots into his no-code agents as just another tool node, giving a [local LLM acting as an agent](../../concepts/local-llms-as-agents.md) the ability to ground its answers in current web results the same way a cloud agent would with Brave.

## Related

- [Local & Self-Hosted AI](../../concepts/local-ai.md) - SearXNG supplies the web-search capability inside Cole's fully private stack.
- [Provider Independence](../../concepts/provider-independence.md) - it removes the last external dependency (search) from a self-hosted agent.
- [Local LLMs as Agents](../../concepts/local-llms-as-agents.md) - the local models it grounds with live web results.
- [Model Quantization](../../concepts/model-quantization.md), [Model Selection](../../concepts/model-selection.md), [Fine-Tuning](../../concepts/fine-tuning.md), [Context Window Limits](../../concepts/context-window-limits.md) - the surrounding local-AI concerns it sits beside in the stack.
- Sibling tools: [Brave Search API](./brave-search.md) (the hosted, AI-summarizing web-search alternative) and [grep](./ripgrep.md) (local search over a codebase rather than the web).

## Sources

- [The Ultimate Guide to Local AI and AI Agents (The Future is Here)](../../sources/the-ultimate-guide-to-local-ai-and-ai-agents-the-future-is-here.md) - "[0:57:00] seir xng for open-source completely free and private web search."
- [The Ultimate Guide to Local AI and AI Agents (The Future is Here)](../../sources/the-ultimate-guide-to-local-ai-and-ai-agents-the-future-is-here.md) - "[1:14:00] This one has a tool to use CRXNG for local and private web search."
- [Create Your Own Private Local AI Cloud Stack in Under 20 Minutes](../../sources/create-your-own-private-local-ai-cloud-stack-in-under-20-minutes.md) - "[0:02:12] recently I added CRX NG for local and private web search which includes reddis for caching."
