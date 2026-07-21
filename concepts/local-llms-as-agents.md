---
type: concept
title: "Local LLMs as Agents"
description: "Using openly downloadable, self-hosted models for agentic work, which hinges on the model's ability to do reliable function calling."
tags: [local-llm, self-hosted, function-calling, open-source]
videos: [llama-32-is-insane-but-does-it-beat-gpt-as-an-ai-agent]
created: 2026-07-21
updated: 2026-07-21
---

# Local LLMs as Agents

Running a local LLM as an agent means using an openly downloadable, self-hosted model to do the reasoning-and-tool-calling work an agent needs, without sending anything to a hosted API. Whether a local model can serve as an agent at all comes down to one capability: reliable function calling. Cole draws the line sharply: "whatever local llm is able to First do function calling reliably is going to be an absolute GameChanger and so you and I get to figure out right now if llama 3.2 is that model" [0:01:14]. Function calling is the gate because an agent is defined by its ability to choose and invoke tools; a model that cannot emit well-formed tool calls consistently cannot drive the agent loop no matter how good its prose is.

This reframes the whole "can I run agents locally" question. It is not primarily about raw benchmark intelligence or context length, it is about the narrower, more mechanical skill of producing correct structured tool invocations turn after turn. When a model clears that bar, the payoff is large: privacy, no per-token cost, and full control over the stack. Testing Llama 3.2, Cole's verdict is measured optimism, "this is looking really nice and is definitely a step forward for local llms as AI agents" [0:15:11], a step forward rather than full parity with the frontier hosted models.

Local agents are typically stood up with a runtime like Ollama that serves an open model behind a local API, which lets the same agent code target a local model instead of a hosted one. The choice of which local model, and the tradeoff against hosted options, is a model-selection decision.

## Prerequisites

- [Tool Calling](./tool-use.md) - reliable function calling is the single capability that determines whether a local model can be an agent.

## Builds on

- [Model Selection](./model-selection.md) - picking a local model, and weighing it against hosted options, is a model-selection call.

## Related

- [Local & Self-Hosted AI](./local-ai.md) - the broader practice of running AI infrastructure on your own hardware.
- [Open-Source & Local AI Coding](./open-source-ai-coding.md) - the same open-weights models applied to coding assistants.
- [Multi-Model Agents](./multi-model-agent.md) - mixing a local model in alongside hosted ones.
- [What Is an AI Agent](./what-is-an-ai-agent.md) - the definition a local model has to satisfy to qualify.

## Tools

- [Llama](../entities/tools/llama.md) - the open model Cole tests as a candidate local agent.
- [Ollama](../entities/tools/ollama.md) - the runtime that serves open models locally behind an API.
- [Local AI Package](../entities/tools/local-ai-package.md) - a bundled stack for running the surrounding local-AI infrastructure.
- [Qwen 2.5 Coder 32B](../entities/tools/qwen.md) - another open model in the local-agent conversation.

## Sources

- [Llama 3.2 is INSANE - But Does it Beat GPT as an AI Agent?](../sources/llama-32-is-insane-but-does-it-beat-gpt-as-an-ai-agent.md) - "[0:01:14] whatever local llm is able to First do function calling reliably is going to be an absolute GameChanger and so you and I get to figure out right now if llama 3.2 is that model"
- [Llama 3.2 is INSANE - But Does it Beat GPT as an AI Agent?](../sources/llama-32-is-insane-but-does-it-beat-gpt-as-an-ai-agent.md) - "[0:15:11] this is looking really nice and is definitely a step forward for local llms as AI agents"
