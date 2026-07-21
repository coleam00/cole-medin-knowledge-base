---
type: concept
title: "Ollama's Default Context Window"
description: "Every Ollama model ships with a 2048-token context window that silently truncates history and tool output; the fix is a two-line Modelfile that raises num_ctx."
tags: [ollama, context-window, local-ai, gotcha, local-llms]
videos: [flowise-n8n-the-best-no-code-local-ai-agent-combo, how-to-use-boltnew-for-free-with-local-llms-and-no-rate-limits]
created: 2026-07-21
updated: 2026-07-21
---

# Ollama's Default Context Window

Ollama serves every model with a 2048-token context window unless you override it, and anything beyond that window is dropped without an error: "every single olama model defaults to 248 tokens for the window size so anything that is past that is going to be cut off from the current context" [0:12:42] (the transcript's "248" is 2048). This is the single most common reason a local model that benchmarks fine looks incompetent inside an agent. Nothing crashes. The system prompt, the conversation history, and the tool definitions simply fall off the end, and the model answers from whatever fragment survived.

The symptoms are diagnostic, and they look like model quality problems rather than configuration problems: "you want to Jack this number up something like 32,000 is what I typically do... otherwise your AMA models will not perform very well they'll miss out on tool calls and hallucinate stuff" [0:13:12]. Missed tool calls plus confident invention is the signature. Before blaming the model, or reaching for a bigger one, check the window.

## The fix

The override is a Modelfile, which creates a small variant of an existing model rather than a new download: "it's from and then the model ID of your olama model that you want to use within autod Dev and then the parameter for the number of context that is where you define the new context limit" [0:04:54]. Two lines, a `FROM` pointing at the base model and a `PARAMETER num_ctx` setting the new limit, then `ollama create` to register the variant and point your tool at that name instead. The effect on tools that push large prompts is dramatic: the documented recipe makes any Ollama model "that has that increased context link so that it magically Works a 100 times better within bolt. new" [0:04:26].

The tradeoff is memory. A larger `num_ctx` raises VRAM use, so the ceiling is set by your hardware, not by preference, which puts this squarely inside the [local LLM hardware requirements](./local-llm-hardware-requirements.md) conversation and often alongside [quantization](./model-quantization.md).

## Prerequisites

- [Local AI](./local-ai.md) - running models on your own machine is the setting where this bites.
- [Context Window Limits](./context-window-limits.md) - the general constraint this is a specific, silent instance of.

## Related

- [Local LLMs as Agents](./local-llms-as-agents.md) - agents are the worst case, since tool definitions and history blow past 2048 tokens immediately.
- [Tool Use](./tool-use.md) - dropped tool definitions are the classic symptom.
- [Model Quantization](./model-quantization.md), [Local LLM Hardware Requirements](./local-llm-hardware-requirements.md) - what caps how far you can raise the window.
- [Local vs Cloud Decision Framework](./local-vs-cloud-decision-framework.md) - part of the real cost of running locally.
- [Context Engineering](./context-engineering.md), [Context Rot](./context-rot.md) - a bigger window is necessary, not sufficient.
- [Browser-Based AI Coding](./browser-based-ai-coding.md), [Open Source AI Coding](./open-source-ai-coding.md) - the tools where the small default was most visible.

## Tools

- [Ollama](../entities/tools/ollama.md) - the runtime with the 2048-token default and the Modelfile override.
- [bolt.diy](../entities/tools/bolt-diy.md) and [oTToDev (autod Dev)](../entities/tools/ottodev.md) - the coding tools whose large prompts exposed the truncation.
- [Flowise](../entities/tools/flowise.md), [n8n](../entities/tools/n8n.md) - no-code agent builders where the same fix applies.
- [Local AI Package](../entities/tools/local-ai-package.md), [n8n Self-Hosted AI Starter Kit](../entities/tools/n8n-self-hosted-ai-starter-kit.md) - bundles that ship Ollama and inherit the default.

## Sources

- [Flowise + n8n - The BEST No Code + Local AI Agent Combo](../sources/flowise-n8n-the-best-no-code-local-ai-agent-combo.md) - "[0:12:42] every single olama model defaults to 248 tokens for the window size so anything that is past that is going to be cut off from the current context"
- [Flowise + n8n - The BEST No Code + Local AI Agent Combo](../sources/flowise-n8n-the-best-no-code-local-ai-agent-combo.md) - "[0:13:12] you want to Jack this number up something like 32,000 is what I typically do... otherwise your AMA models will not perform very well they'll miss out on tool calls and hallucinate stuff"
- [How to Use Bolt.new for FREE with Local LLMs (And NO Rate Limits)](../sources/how-to-use-boltnew-for-free-with-local-llms-and-no-rate-limits.md) - "[0:04:26] this has the instructions on how to create a slight variation of any olama model that has that increased context link so that it magically Works a 100 times better within bolt. new"
- [How to Use Bolt.new for FREE with Local LLMs (And NO Rate Limits)](../sources/how-to-use-boltnew-for-free-with-local-llms-and-no-rate-limits.md) - "[0:04:54] it's from and then the model ID of your olama model that you want to use within autod Dev and then the parameter for the number of context that is where you define the new context limit"
