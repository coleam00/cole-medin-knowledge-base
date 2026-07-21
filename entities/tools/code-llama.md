---
type: entity
subtype: tool
title: "Code Llama"
description: "Meta's open-source code-specialized LLM family whose larger 34B variant fails builds that the smaller Qwen 2.5 Coder 32B handles, showing capability beats parameter count."
tags: [llm, model, open-source, local-ai]
videos: [qwen-just-casually-started-the-local-ai-revolution]
created: 2026-07-21
updated: 2026-07-21
---

# Code Llama

Code Llama is Meta's code-specialized branch of the [Llama](./llama.md) family, an open-weight model line trained for code completion and generation and available in several parameter sizes for [local, self-hosted](../../concepts/local-ai.md) use. In Cole's catalog it plays one specific and useful role: the control group. When he wants to prove that Qwen 2.5 Coder 32B is genuinely different rather than just the latest release, he runs the identical build against Code Llama 34B and lets it fail on camera.

The demo is a React and Tailwind chat interface generated inside oTToDev, his [bolt.new](./bolt-new.md) fork, with both models served locally through [Ollama](./ollama.md). Cole sets the trap explicitly: "I've got code llama 34b loaded in here and I'll show you that this this model it's actually a little bit bigger than the one I just used and it still is going to mess up" [0:06:22]. It does. The model never runs `npm install` or starts Vite, so the app it writes cannot actually run. He recalls the same pattern with Llama 3.1 70B failing his agent tests, a model twice the size again.

The lesson is the throughline of that whole video, and it is a [model selection](../../concepts/model-selection.md) lesson rather than a hardware one: parameter count is not capability. A 32B model trained more recently and more deliberately for coding beats a 34B and a 70B at the task they were nominally built for, which is why VRAM budgeting and [quantization](../../concepts/model-quantization.md) only tell you which models you *can* run, never which ones you *should*. Code Llama also marks the "before" state of local AI. It is the generation that made local coding models feel like toys, and the reason Cole frames Qwen 2.5 Coder 32B as the moment [open-source and local AI coding](../../concepts/open-source-ai-coding.md) became practical for real work.

## Realizes

- [Local & Self-Hosted AI](../../concepts/local-ai.md) - Running open-weight models on your own hardware or cloud for privacy, cost control, and independence from API providers.
- [Open-Source & Local AI Coding](../../concepts/open-source-ai-coding.md) - Community-maintained, self-hostable AI coding tools and local models that dodge API costs and rate limits.

## Contrasts with

- [Qwen 2.5 Coder 32B](./qwen.md) - Alibaba's open-source coding model that succeeds at the exact build Code Llama 34B fails, despite being smaller.
- [Llama](./llama.md) - Meta's general open LLM family Code Llama specializes from; its 3.1 70B variant failed Cole's agent tests the same way.

## Works with

- [Ollama](./ollama.md) - Local LLM runtime used to pull and serve both models for the head-to-head.
- [bolt.new](./bolt-new.md) - StackBlitz's AI coding platform whose oTToDev fork hosts the failing React and Tailwind build.

## Related

- [Model Selection](../../concepts/model-selection.md) - Choosing the right LLM per task by trading off quality, speed, and cost.
- [Model Quantization](../../concepts/model-quantization.md) - Compressing model weights to lower precision so large models fit and run on limited local hardware.
- [Local LLM Hardware Requirements](../../concepts/local-llm-hardware-requirements.md) - The VRAM-per-parameter-tier ladder that decides which model your hardware can actually run.
- [Local LLMs as Agents](../../concepts/local-llms-as-agents.md) - Using openly downloadable, self-hosted models for agentic work, which hinges on reliable function calling.
- [Limitations of AI Coding Models](../../concepts/ai-coding-limitations.md) - General coding models stay too general and hallucinate, and silently generate stale library code because of the training cutoff.

## Sources

- [Qwen Just Casually Started the Local AI Revolution](../../sources/qwen-just-casually-started-the-local-ai-revolution.md) - "[0:06:22] I've got code llama 34b loaded in here and I'll show you that this this model it's actually a little bit bigger than the one I just used and it still is going to mess up"
