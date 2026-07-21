---
type: entity
subtype: organization
title: "Together AI"
description: "Pay-per-token inference provider serving open models like Llama 3.1; cheaper on its lite 70B variant but pricier than Groq once you want turbo-speed inference."
resource: "https://www.together.ai"
tags: [company, inference, provider, llama, cost]
videos: [the-hard-truth-about-hosting-your-own-llms]
created: 2026-07-21
updated: 2026-07-21
---

# Together AI

Together AI is a pay-per-token inference provider that serves open-weight models, most notably [Meta AI](./meta.md)'s [Llama](../tools/llama.md) 3.1, as a hosted API you call instead of standing up your own GPU. In Cole's catalog it plays one precise role: the price comparison that proves how cheap [Groq](./groq.md) is. Walking Groq's Llama 3.1 70B pricing, he notes "comparing to other services that offer llama 3.1 like together for example they have their light version of llama 3.1 70b that actually is technically a little bit cheaper but if you want to go turbo... you're going to be paying more" ([0:06:31]). The verdict is friendly rather than dismissive - "together AI it's a fine service I've used it before I like it" - but the cost of its fast tier is what keeps Groq as the default recommendation.

The tiering is the actual lesson. Together AI ships multiple builds of the same open weights (a cheaper lite variant, a faster turbo variant), so a headline per-million-token figure means nothing until you pin down the throughput you need. Comparing "Llama 3.1 70B here versus Llama 3.1 70B there" is a category error: the unit of comparison is model plus serving tier, which is why [Model Selection](../../concepts/model-selection.md) and [LLM Cost Optimization](../../concepts/llm-cost-optimization.md) have to be done on real quoted speed, not model names.

Structurally, Together AI occupies the same middle rung of the hosting ladder as Groq. You pay per token for the exact model you would eventually run yourself, so a later migration to your own hardware does not change model behavior - the practical payoff of [Provider Independence](../../concepts/provider-independence.md). But it is not [local AI](../../concepts/local-ai.md): a third party still holds the weights and sees your prompts, placing it above closed frontier models yet below true self-hosting on the [LLM Data Privacy Tiers](../../concepts/llm-data-privacy-tiers.md) ladder. Once monthly volume passes the [Self-Hosting Cost Crossover](../../concepts/self-hosting-cost-crossover.md), the same reasoning that recommends a hosted provider recommends leaving it for [Cloud GPU Hosting](../../concepts/cloud-gpu-hosting.md).

## Contrasts with

- [Groq](./groq.md) - A fast inference provider Cole recommends (with a Llama model) when you need speed over raw power.
- [OpenRouter](../tools/openrouter.md) - Unified API gateway to many LLMs, the aggregator alternative to picking one open-model host.
- [RunPod](../tools/runpod.md) - GPU cloud recommended when you need a powerful high-VRAM machine to run large language models yourself.

## Works with

- [Llama](../tools/llama.md) - The open LLM Together AI serves in lite and turbo variants.
- [Meta AI](./meta.md) - Trainer of the open weights Together AI hosts.

## Related

- [Self-Hosting Cost Crossover](../../concepts/self-hosting-cost-crossover.md) - Where monthly per-token spend exceeds a fixed cloud-GPU bill.
- [Cloud GPU Hosting](../../concepts/cloud-gpu-hosting.md) - Renting VRAM-sized GPU machines instead of owning hardware.
- [LLM Data Privacy Tiers](../../concepts/llm-data-privacy-tiers.md) - Closed models, to hosted open-model providers, to true self-hosting.
- [LLM Cost Optimization](../../concepts/llm-cost-optimization.md) - Matching traffic to the cheapest model and tier that can serve it.
- [Model Selection](../../concepts/model-selection.md) - Trading off quality, speed, and cost per task.
- [Provider Independence](../../concepts/provider-independence.md) - Swapping model or provider without a rewrite.
- [Local vs. Cloud Decision Framework](../../concepts/local-vs-cloud-decision-framework.md) - Whether a stack should be self-hosted or run on managed services.
- [DigitalOcean](./digital-ocean.md) - The general-compute host Cole weighs against dedicated GPU clouds.

## Sources

- [The HARD Truth About Hosting Your Own LLMs](../../sources/the-hard-truth-about-hosting-your-own-llms.md) - "[0:06:31] comparing to other services that offer llama 3.1 like together for example they have their light version of llama 3.1 70b that actually is technically a little bit cheaper but if you want to go turbo... you're going to be paying more"
