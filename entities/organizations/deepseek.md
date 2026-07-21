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

DeepSeek is a Chinese AI startup whose open-source models became a landmark moment in the open-weight movement. Cole treats its January 2025 R1 release as one of the defining events of the year, "the release of Deepseek R1. At the time, a very revolutionary open-source large language model." Its impact was as much financial as technical: he ties it directly to the market shock, noting "this is the reason the Nvidia market cap went down $600 billion, the largest one-day loss for a single company." A cheaply-trained, freely-available reasoning model that rivaled closed frontier systems forced a repricing of the assumption that only massive proprietary spend could produce top-tier AI, which is why DeepSeek recurs as a case study in open-source disruption.

Technically, DeepSeek matters to Cole as a practical, cheap, powerful option for agents. R1 is a [reasoning model](../../concepts/reasoning-models.md) he runs at full size ("the 671 billion parameter through the Deep seek API") and also accesses through [OpenRouter](../tools/openrouter.md) to sidestep first-party outages. DeepSeek V3 is the workhorse he pairs with [Pydantic AI](../tools/pydantic-ai.md): "we're going to use the new deep seek V3 large language model through open router so we can make our agent super powerful and still dirt cheap." That combination of capability and low cost makes DeepSeek a natural fit for [agentic coding](../../concepts/agentic-coding.md) and a poster child for [provider independence](../../concepts/provider-independence.md) and [model selection](../../concepts/model-selection.md), where a swappable, inexpensive model beats a locked-in expensive one.

Its coder models earn repeated praise. In the [oTToDev](../tools/ottodev.md) fork the DeepSeek API integration lands because "deep seek coder is just a fantastic model for coding projects," and building the open-source assistant he singles out "the deep-seat coder models especially the 236 billion parameter one absolutely kick butt." Because the weights are open, DeepSeek also feeds Cole's [local AI](../../concepts/local-ai.md) interest and the broader [community-driven development](../../concepts/community-driven-development.md) around models anyone can self-host, and it repeatedly appears in the [vibe coding](../../concepts/vibe-coding.md) tools he reviews.

## Related

- [DeepSeek R1](../tools/deepseek-r1.md)
- [DeepSeek V3](../tools/deepseek-v3.md)
- [Reasoning Models](../../concepts/reasoning-models.md)
- [Provider Independence](../../concepts/provider-independence.md)
- [Model Selection](../../concepts/model-selection.md)
- [Local & Self-Hosted AI](../../concepts/local-ai.md)
- [Agentic Coding](../../concepts/agentic-coding.md)
- [Community-Driven Development](../../concepts/community-driven-development.md)
- [Vibe Coding](../../concepts/vibe-coding.md)
- [OpenRouter](../tools/openrouter.md)
- [Pydantic AI](../tools/pydantic-ai.md)
- [oTToDev](../tools/ottodev.md)
- [Nvidia](./nvidia.md)

## Sources

- [AI Exploded in 2025 - Here's Everything That Happened](../../sources/ai-exploded-in-2025-heres-everything-that-happened.md) - "[0:01:57] this is the reason the Nvidia market cap went down $600 billion, the largest one-day loss for a single company"
- [DeepSeek R1 Just Revolutionized AI Forever](../../sources/deepseek-r1-just-revolutionized-ai-forever.md) - "[0:10:28] I'm going to take the most powerful version of the model the 671 billion parameter through the Deep seek API"
- [Pydantic AI + DeepSeek V3 - The BEST AI Agent Combo](../../sources/pydantic-ai-deepseek-v3-the-best-ai-agent-combo.md) - "[0:00:34] we're going to use the new deep seek V3 large language model through open router so we can make our agent super powerful and still dirt cheap"
- [This Bolt.new Fork is EXPLODING - Don't Miss out on What's Happening!](../../sources/this-boltnew-fork-is-exploding-dont-miss-out-on-whats-happening.md) - "[0:05:19] the Deep seek API integration this is a great addition ... Because deep seek coder is just a fantastic model for coding projects"
- [I'm Building the BEST Open Source AI Coding Assistant with YOUR Help](../../sources/im-building-the-best-open-source-ai-coding-assistant-with-your-help.md) - "[0:11:36] integration with the Deep seek API because the deep-seat coder models especially the 236 billion parameter one absolutely kick butt"
