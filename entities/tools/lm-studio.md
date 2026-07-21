---
type: entity
subtype: tool
title: "LM Studio"
description: "Desktop app for downloading and running open-weight LLMs locally, the main alternative to Ollama and a requested provider integration for the bolt.new fork."
resource: "https://lmstudio.ai"
tags: [llm, model]
videos: [deepseek-r1-just-revolutionized-ai-forever, im-building-the-best-open-source-ai-coding-assistant-with-your-help]
created: 2026-07-21
updated: 2026-07-21
---

# LM Studio

LM Studio is a desktop application for downloading and running open-weight models on your own machine. In Cole's catalog it is defined almost entirely by position: it is the alternative people reach for when they do not want [Ollama](./ollama.md). Walking through how to run the distilled [DeepSeek R1](./deepseek-r1.md) models, he lays out both doors: "you can also install through hugging face as well I know a lot of people love olama but then a lot of other people like using other platforms like LM studio and llama CPP" [0:09:00]. The Hugging Face path is the important half, because that is where you pick a [quantization](../../concepts/model-quantization.md) and therefore decide whether a 14B or 32B model actually fits the VRAM you have.

The second appearance is a demand signal rather than a demo. Reviewing the roadmap for his community fork of bolt.new, he puts LM Studio on the build list because of who is asking: "we have the LM Studio integration because a lot of you use that instead of something like AMA for your local models" [0:11:21]. That is the whole argument for [provider independence](../../concepts/provider-independence.md) in miniature. A tool that hardcodes one local runtime loses the half of its users who standardized on the other, so the fork adds providers rather than picking winners, the same reason it grew OpenRouter, Gemini, and DeepSeek API support alongside Ollama.

Functionally the two runtimes overlap heavily: both pull open weights, both serve an OpenAI-compatible local endpoint that agent frameworks and [open-source AI coding](../../concepts/open-source-ai-coding.md) tools can point at. The practical difference is packaging. LM Studio is a graphical desktop app with model browsing and quantization selection built in, where Ollama is a command-line runtime that a stack like the [Local AI Package](./local-ai-package.md) can compose into containers. Either way the ceiling is your hardware, not the software, which is why [local LLM hardware requirements](../../concepts/local-llm-hardware-requirements.md) decide what you can honestly run and why the strongest reason to bother is data staying on your machine.

## Realizes

- [Local & Self-Hosted AI](../../concepts/local-ai.md) - Running open-weight models on your own hardware for privacy, cost control, and independence from API providers.
- [Model Quantization](../../concepts/model-quantization.md) - Compressing weights to lower precision so large models fit and run on limited local hardware.
- [Local LLMs as Agents](../../concepts/local-llms-as-agents.md) - Using self-hosted models for agentic work, which hinges on reliable function calling.
- [Open-Source & Local AI Coding](../../concepts/open-source-ai-coding.md) - Community-maintained, self-hostable coding tools and local models that dodge API costs and rate limits.
- [Provider Independence](../../concepts/provider-independence.md) - Architecting so the underlying model or runtime can be swapped without a rewrite.

## Works with

- [DeepSeek R1](./deepseek-r1.md) - Open MIT-licensed reasoning model whose distilled versions are exactly what LM Studio is used to run.
- [Qwen 2.5 Coder 32B](./qwen.md) - Alibaba's open model family, the base for several R1 distillations and a common local pick.
- [Llama](./llama.md) - Meta's open model family, the other base used for the distilled reasoning models.
- [oTToDev (autod Dev)](./ottodev.md) - Cole's community fork of bolt.new, where LM Studio support was added as a requested provider.
- [bolt.diy](./bolt-diy.md) - The renamed community fork that carries the any-provider, any-local-model design forward.

## Contrasts with

- [Ollama](./ollama.md) - The command-line local LLM runtime LM Studio is the desktop alternative to.
- [Open Web UI](./open-web-ui.md) - Self-hostable ChatGPT-style frontend that wraps a separate runtime, where LM Studio bundles runner and UI together.
- [Local AI Package](./local-ai-package.md) - Cole's containerized bundle of self-hosted AI services, the compose-file route to the same local stack.
- [OpenRouter](./openrouter.md) - Unified cloud gateway to many hosted LLMs, the opposite trade of running weights yourself.

## Related

- [Local LLM Hardware Requirements](../../concepts/local-llm-hardware-requirements.md) - The VRAM ladder that decides which parameter tier your machine can actually run.
- [LLM Data Privacy Tiers](../../concepts/llm-data-privacy-tiers.md) - The privacy ladder from closed APIs to hosted open models to true self-hosting.
- [Local vs. Cloud Decision Framework](../../concepts/local-vs-cloud-decision-framework.md) - The four questions that decide whether a stack should be self-hosted or managed.
- [Self-Hosting Cost Crossover](../../concepts/self-hosting-cost-crossover.md) - The point where per-token spend exceeds a fixed hardware or GPU bill.
- [Model Selection](../../concepts/model-selection.md) - Trading quality, speed, and cost per task rather than defaulting to one model.
- [Reasoning Models](../../concepts/reasoning-models.md) - Models that think before answering, the class of distilled weights most often run locally.
- [Community-Driven Development](../../concepts/community-driven-development.md) - Building open source in public with a roadmap shaped by what users actually run.

## Sources

- [DeepSeek R1 Just Revolutionized AI Forever](../../sources/deepseek-r1-just-revolutionized-ai-forever.md) - "[0:09:00] you can also install through hugging face as well I know a lot of people love olama but then a lot of other people like using other platforms like LM studio and llama CPP"
- [I'm Building the BEST Open Source AI Coding Assistant with YOUR Help](../../sources/im-building-the-best-open-source-ai-coding-assistant-with-your-help.md) - "[0:11:21] we have the LM Studio integration because a lot of you use that instead of something like AMA for your local models"
