---
type: entity
subtype: organization
title: "DeepSeek"
description: "Chinese startup whose R1 open-source model was tied to Nvidia's $600B one-day drop; later shipped DeepSeek 3.2."
resource: "https://www.deepseek.com"
tags: [llm-provider, open-source, reasoning-models]
videos: [ai-exploded-in-2025-heres-everything-that-happened, deepseek-r1-just-revolutionized-ai-forever, pydantic-ai-deepseek-v3-the-best-ai-agent-combo, this-boltnew-fork-is-exploding-dont-miss-out-on-whats-happening, im-building-the-best-open-source-ai-coding-assistant-with-your-help]
created: 2026-07-21
updated: 2026-07-21
---

# DeepSeek

DeepSeek is a Chinese AI startup whose open-source models became a landmark moment in the open-weight movement. Cole treats its January 2025 R1 release as one of the defining events of the year, "the release of DeepSeek R1. At the time, a very revolutionary open-source large language model." Its impact was as much financial as technical: he ties it directly to the market shock, noting "this is the reason the Nvidia market cap went down $600 billion, the largest one-day loss for a single company." A cheaply-trained, freely-available reasoning model that rivaled closed frontier systems forced a repricing of the assumption that only massive proprietary spend could produce top-tier AI, which is why DeepSeek recurs as a case study in open-source disruption.

Technically, DeepSeek matters to Cole as a practical, cheap, powerful option for agents. R1 is a [reasoning model](../../concepts/reasoning-models.md) he runs at full size ("the 671 billion parameter through the DeepSeek API") and also accesses through [OpenRouter](../tools/openrouter.md) to sidestep first-party outages. DeepSeek V3 is the workhorse he pairs with [Pydantic AI](../tools/pydantic-ai.md): "we're going to use the new DeepSeek V3 large language model through OpenRouter so we can make our agent super powerful and still dirt cheap." That combination of capability and low cost makes DeepSeek a natural fit for [agentic coding](../../concepts/agentic-coding.md) and a poster child for [provider independence](../../concepts/provider-independence.md) and [model selection](../../concepts/model-selection.md), where a swappable, inexpensive model beats a locked-in expensive one.

Its coder models earn repeated praise. In the [oTToDev](../tools/ottodev.md) fork the DeepSeek API integration lands because "DeepSeek coder is just a fantastic model for coding projects," and building the open-source assistant he singles out "the DeepSeek coder models especially the 236 billion parameter one absolutely kick butt." Because the weights are open, DeepSeek also feeds Cole's [local AI](../../concepts/local-ai.md) interest and the broader [community-driven development](../../concepts/community-driven-development.md) around models anyone can self-host, and it repeatedly appears in the [vibe coding](../../concepts/vibe-coding.md) tools he reviews.

## Realizes

- [Reasoning Models](../../concepts/reasoning-models.md) - Models that produce explicit reasoning before answering, and when that extra thinking helps versus hurts.

## Works with

- [OpenRouter](../tools/openrouter.md) - Unified API gateway to many LLMs; here it hosts Quasar Alpha, its first stealth/cloaked pre-release Foundation model, free to use.
- [Pydantic AI](../tools/pydantic-ai.md) - Cole's framework for the individual agents, structured around three parts: dependencies, the agent definition, and tools.
- [oTToDev (autod Dev)](../tools/ottodev.md) - Community fork of bolt.new that adds support for any LLM, including local models via Ollama; the tool this video is built around.

## Related

- [DeepSeek R1](../tools/deepseek-r1.md) - Open-source MIT-licensed reasoning LLM that rivals OpenAI o1, ships in distilled sizes, and is far cheaper to run.
- [DeepSeek V3](../tools/deepseek-v3.md) - New open model Cole cites as evidence the local-vs-closed gap is closing fast; he's using it heavily in his own stack and it's performing great.
- [Provider Independence](../../concepts/provider-independence.md) - Architecting agents so the underlying model, framework, or client can be swapped without a rewrite, avoiding lock-in through low-level abstractions.
- [Model Selection](../../concepts/model-selection.md) - Choosing the right LLM per task by trading off quality, speed, and cost, often routing easy requests to cheap models and hard ones to expensive models.
- [Local & Self-Hosted AI](../../concepts/local-ai.md) - Running open-weight models on your own hardware or cloud for privacy, cost control, and independence from API providers.
- [Agentic Coding](../../concepts/agentic-coding.md) - Letting an AI agent drive software development end-to-end, from planning through implementation and validation, with human steering.
- [Community-Driven Development](../../concepts/community-driven-development.md) - Building products and open source in public with a community, using a public roadmap and shared learning.
- [Vibe Coding](../../concepts/vibe-coding.md) - Building software by conversationally prompting an AI without closely reading the code, useful for prototypes but risky for production.
- [Nvidia](./nvidia.md) - Co-sponsor of the AI agents developer contest whose technologies Cole must integrate to qualify.

## Sources

- [AI Exploded in 2025 - Here's Everything That Happened](../../sources/ai-exploded-in-2025-heres-everything-that-happened.md) - "[0:01:57] this is the reason the Nvidia market cap went down $600 billion, the largest one-day loss for a single company"
- [DeepSeek R1 Just Revolutionized AI Forever](../../sources/deepseek-r1-just-revolutionized-ai-forever.md) - "[0:10:28] I'm going to take the most powerful version of the model the 671 billion parameter through the DeepSeek API"
- [Pydantic AI + DeepSeek V3 - The BEST AI Agent Combo](../../sources/pydantic-ai-deepseek-v3-the-best-ai-agent-combo.md) - "[0:00:34] we're going to use the new DeepSeek V3 large language model through OpenRouter so we can make our agent super powerful and still dirt cheap"
- [This Bolt.new Fork is EXPLODING - Don't Miss out on What's Happening!](../../sources/this-boltnew-fork-is-exploding-dont-miss-out-on-whats-happening.md) - "[0:05:19] the DeepSeek API integration this is a great addition ... Because DeepSeek coder is just a fantastic model for coding projects"
- [I'm Building the BEST Open Source AI Coding Assistant with YOUR Help](../../sources/im-building-the-best-open-source-ai-coding-assistant-with-your-help.md) - "[0:11:36] integration with the DeepSeek API because the DeepSeek coder models especially the 236 billion parameter one absolutely kick butt"
