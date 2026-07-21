---
type: concept
title: "Mixture of Experts"
description: "A model architecture that routes each token through a subset of specialized expert networks, contrasted with a dense Transformer, explaining why two similar-looking reasoning LLMs behave very differently."
tags: [reasoning-models, architecture, mixture-of-experts]
videos: [lets-settle-the-o3-mini-vs-r1-debate-for-coding-once-and-for-all]
created: 2026-07-21
updated: 2026-07-21
---

# Mixture of Experts

A mixture of experts (MoE) model splits its parameters into many specialized sub-networks and routes each token through only a few of them, instead of pushing every token through the whole network the way a dense Transformer does. The architecture is the reason two models that both advertise "reasoning" can behave nothing alike: "open aai 03 mini it's a dense Transformer architecture like most of the open AI models and then R1 is a mixture of experts combined with reinforcement learning from Human feedback" [0:02:23].

That single sentence carries the practical lesson. o3-mini and R1 are marketed as peers, benchmarked as peers, and priced as competitors, but under the hood they are different machines. Cole's framing is that the architecture split shows up as a task split: the dense model tends to be steadier on directed, instruction-following work, while the MoE reasoning model tends to shine on open-ended, logical, exploratory problems. Reading a leaderboard without reading the architecture is how you end up with the wrong model on the wrong task.

The MoE design also explains a practical asymmetry for anyone running open weights locally. Total parameter count and active parameter count diverge: an MoE model must hold every expert in memory but only computes with a slice of them per token, so it can be cheap to run and expensive to host. That tension is the heart of [local LLM hardware requirements](./local-llm-hardware-requirements.md) and a common reason a model that looks affordable on paper will not fit on a workstation.

## Builds on

- [Reasoning Models](./reasoning-models.md) - the class of model where the architecture distinction actually bites, since both o3-mini and R1 are reasoning models.

## Contrasts with

- [OpenAI o3-mini](../entities/tools/o3-mini.md) - the dense-Transformer counterpart in the comparison, "like most of the open AI models."

## Implemented by

- [DeepSeek R1](../entities/tools/deepseek-r1.md) - the open-weight mixture-of-experts reasoning model, MoE combined with reinforcement learning from human feedback.
- [DeepSeek](../entities/organizations/deepseek.md) - the lab that shipped it.

## Related

- [Model Selection](./model-selection.md) - architecture is a selection criterion, not trivia; route directed tasks and free-thinking tasks differently.
- [Coding Benchmarks](./coding-benchmarks.md) - why head-to-head scores alone mislead when the two models are built differently.
- [Model Quantization](./model-quantization.md), [Local LLM Hardware Requirements](./local-llm-hardware-requirements.md) - what it takes to actually run an open-weight MoE model yourself.
- [Local LLMs as Agents](./local-llms-as-agents.md), [Local AI](./local-ai.md) - the setting where these tradeoffs are felt most directly.

## Sources

- [Let's Settle the o3-mini Vs. R1 Debate for Coding ONCE and for ALL](../sources/lets-settle-the-o3-mini-vs-r1-debate-for-coding-once-and-for-all.md) - "[0:02:23] open aai 03 mini it's a dense Transformer architecture like most of the open AI models and then R1 is a mixture of experts combined with reinforcement learning from Human feedback"
