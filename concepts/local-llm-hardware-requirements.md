---
type: concept
title: "Local LLM Hardware Requirements"
description: "The VRAM-per-parameter-tier ladder for local models (7B chat, 14B basic tool-calling, 32B genuinely impressive, 70B near-cloud) that decides which model your hardware can actually run."
tags: [model-selection, hardware, vram]
videos: [the-ultimate-guide-to-local-ai-and-ai-agents-the-future-is-here]
created: 2026-07-21
updated: 2026-07-21
---

# Local LLM Hardware Requirements

Running open weights yourself is gated by one number: the VRAM on your graphics card. Parameter count sets the floor, and the conversion is roughly two-thirds of a gigabyte per billion parameters at Q4 - "a 7 billion parameter model will need about four to 5 GB of VRAM on your graphics card" [0:14:00]. Everything else about a local setup follows from where your card lands on that ladder.

The ladder is best read as capability tiers, not sizes:

- **7B (about 4-5 GB VRAM).** Runs on almost any modern GPU. Good for chat, summarization, and simple classification. Unreliable the moment you ask for structured output or tool calls.
- **14B (roughly 8-10 GB).** The first tier that behaves like an agent: "once you get to something around 14 billion parameters that's when I see agents being able to really accept instructions well around tools and system prompts" [0:16:00]. This is the practical minimum for anything agentic.
- **32B (roughly 20-24 GB).** The tier where local stops feeling like a compromise: "32 billion when you start to get into this range is when I'm actually genuinely impressed. I'm like, Oh, this is actually pretty close to the performance of some of the best cloud AI" [0:18:00]. A single 24 GB consumer card lands exactly here, which is why 32B is the sweet spot for serious home setups.
- **70B and up (48 GB or multiple cards).** Closest to frontier cloud quality, and the point where hardware cost stops being a hobby purchase.

Two adjustments move you up a rung without new hardware. [Quantization](./model-quantization.md) shrinks the weights so a bigger model fits, and the standing advice is to take the largest model that fits at Q4 rather than a smaller one at full precision. Offloading splits layers between GPU and CPU/RAM, which lets an oversized model run at all, just slowly. Both are why the VRAM number is a budget to spend, not a hard wall.

## Prerequisites

- [Local & Self-Hosted AI](./local-ai.md) - the setup this hardware question exists inside.
- [Model Quantization](./model-quantization.md) - the compression that decides how many parameters actually fit in a given VRAM budget.

## Related

- [Local LLMs as Agents](./local-llms-as-agents.md) - why 14B is the floor: below it, tool calling and instruction-following break down.
- [Tool Calling](./tool-use.md) - the specific capability that separates the chat tier from the agent tier.
- [Cloud GPU Hosting](./cloud-gpu-hosting.md) - renting the VRAM you cannot buy, while still controlling the box.
- [Self-Hosting Cost Crossover](./self-hosting-cost-crossover.md) - the money version of this page: at what volume the card pays for itself.
- [Local vs. Cloud Decision Framework](./local-vs-cloud-decision-framework.md) - hardware capability is one of the four questions that decide the whole architecture.
- [Model Selection](./model-selection.md) - choosing among the models that clear your VRAM bar.
- [Ollama's Default Context Window](./ollama-context-window.md) - the other local gotcha; fitting the weights is only half the memory story, since context costs VRAM too.
- [Mixture of Experts](./mixture-of-experts.md) - architectures that activate a fraction of their parameters, changing the size-to-speed math.

## Tools

- [Ollama](../entities/tools/ollama.md) - serves the model and handles quantization defaults and CPU offloading.
- [LM Studio](../entities/tools/lm-studio.md) - a GUI alternative that reports whether a given model fits your card before you download it.
- [Qwen 2.5 Coder 32B](../entities/tools/qwen.md), [Llama](../entities/tools/llama.md), [DeepSeek R1](../entities/tools/deepseek-r1.md) - the open-weight families that ship across every tier of the ladder.
- [Nvidia](../entities/organizations/nvidia.md) - whose VRAM tiers effectively define the rungs.
- [RunPod](../entities/tools/runpod.md) - rented GPUs when the local card tops out.
- [Hugging Face](../entities/organizations/hugging-face.md) - where the per-tier quantized files are downloaded from.

## Sources

- [The Ultimate Guide to Local AI and AI Agents (The Future is Here)](../sources/the-ultimate-guide-to-local-ai-and-ai-agents-the-future-is-here.md) - "[0:14:00] a 7 billion parameter model will need about four to 5 GB of VRAM on your graphics card"
- [The Ultimate Guide to Local AI and AI Agents (The Future is Here)](../sources/the-ultimate-guide-to-local-ai-and-ai-agents-the-future-is-here.md) - "[0:16:00] once you get to something around 14 billion parameters that's when I see agents being able to really accept instructions well around tools and system prompts"
- [The Ultimate Guide to Local AI and AI Agents (The Future is Here)](../sources/the-ultimate-guide-to-local-ai-and-ai-agents-the-future-is-here.md) - "[0:18:00] 32 billion when you start to get into this range is when I'm actually genuinely impressed. I'm like, Oh, this is actually pretty close to the performance of some of the best cloud AI"
