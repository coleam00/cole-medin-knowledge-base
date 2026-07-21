---
type: concept
title: "Model Quantization"
description: "Compressing model weights to lower precision so large models fit and run on limited local hardware."
tags: [quantization, local-llms, compression]
videos: [the-ultimate-guide-to-local-ai-and-ai-agents-the-future-is-here, deepseek-r1-just-revolutionized-ai-forever, qwen-just-casually-started-the-local-ai-revolution]
created: 2026-07-21
updated: 2026-07-21
---

# Model Quantization

Quantization shrinks a model by storing its weights at lower numerical precision. "There's a concept called quantizing with local large language models where essentially you can reduce the size of the model significantly while only reducing the performance a tiny bit" [0:03:36]. The mechanism is precision reduction, not pruning: the goal is "how we can make large language models a lot smaller so they can fit on our GPUs without hurting performance too much. We are lowering the model precision here" [0:25:00]. Because "we can make these numbers less precise or smaller without losing much performance... we can fit larger LLMs within a GPU that normally wouldn't even be close to running the full-size model" [0:30:00]. This is what makes serious models runnable on consumer hardware, so it sits at the center of every [local AI](./local-ai.md) setup.

## How it works

Quantization levels are labeled by bit-width, from aggressive (Q2) to light (Q8), and the choice trades size against quality. At Q2 "the model is 12 GB instead of the 20 GB from the default one that Ollama has for you" [0:03:55]. Cole's default recommendation is the middle of that range: "a Q4 quantization is generally the best balance... pick the largest large language model that can work with your hardware with a Q4 quantization" [0:31:00]. The rule of thumb is to maximize parameter count first, then quantize as needed to fit VRAM, rather than run a small model at full precision.

Quantization is why even frontier open models are downloadable at all. DeepSeek R1's full weights are enormous: "the biggest one here the 671 billion parameter version... it is a whopping 400 GB super super big and this is a Q4 quantization so it's not even the biggest version of this model that you could download" [0:06:34]. When picking a file, provenance matters: on Hugging Face "click on quantizations there's 43 models available here and then the one that I'd recommend selecting here is the one from UNS sloth" [0:09:41].

## Related

- [Local & Self-Hosted AI](./local-ai.md) - quantization is the enabling technique; it decides which models fit your GPU and pairs with layer offloading to CPU/RAM.
- [Model Selection](./model-selection.md) - quantization level is part of choosing a local model: bigger-but-quantized usually beats smaller-at-full-precision.
- [Fine-Tuning](./fine-tuning.md) - a distilled or fine-tuned open model is then quantized for the last mile onto local hardware.

## Tools

- [DeepSeek R1](../entities/tools/deepseek-r1.md) - its 671B weights ship as a 400 GB Q4 file, the canonical example of why quantization is unavoidable.
- [Qwen](../entities/tools/qwen.md) - the model whose Q2 vs default sizes Cole uses to illustrate the size/quality dial.
- [Ollama](../entities/tools/ollama.md) - serves quantized models locally, with a default quantization per model.
- [Hugging Face](../entities/organizations/hugging-face.md) - hosts the many per-model quantizations to choose among.

## Sources

- [Qwen Just Casually Started the Local AI Revolution](../sources/qwen-just-casually-started-the-local-ai-revolution.md) - "[0:03:36] there's a concept called quantizing with local large language models where essentially you can reduce the size of the model significantly while only reducing the performance a tiny bit"
- [The Ultimate Guide to Local AI and AI Agents (The Future is Here)](../sources/the-ultimate-guide-to-local-ai-and-ai-agents-the-future-is-here.md) - "[0:31:00] a Q4 quantization is generally the best balance... pick the largest large language model that can work with your hardware with a Q4 quantization"
- [DeepSeek R1 Just Revolutionized AI Forever](../sources/deepseek-r1-just-revolutionized-ai-forever.md) - "[0:06:34] the biggest one here the 671 billion parameter version ... it is a whopping 400 GB super super big and this is a Q4 quantization so it's not even the biggest version of this model that you could download"
