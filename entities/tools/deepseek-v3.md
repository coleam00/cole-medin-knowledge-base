---
type: entity
subtype: tool
title: "DeepSeek V3"
description: "New open model Cole cites as evidence the local-vs-closed gap is closing fast; he's using it heavily in his own stack and it's performing great."
resource: "https://www.deepseek.com"
tags: [llm, open-source, model-access]
videos: [the-glow-up-every-ai-agent-needs, how-to-dominate-with-ai-in-2025]
created: 2026-07-21
updated: 2026-07-21
---

# DeepSeek V3

DeepSeek V3 is DeepSeek's open, general-purpose (non-reasoning) LLM, and Cole treats it as fresh evidence that open models have closed most of the gap on closed frontier models. In his 2025 stack rundown he names it his current pick and vouches for it from real use: "for large language models this is probably the most volatile but right now I'm using a lot of the new deep seek V3 I've tested it's performing fantastic" [0:20:43]. Where its sibling [DeepSeek R1](./deepseek-r1.md) is the reasoning model, V3 is the fast general workhorse.

## How Cole uses it

V3 is the default LLM in his current agent builds, typically accessed through [OpenRouter](./openrouter.md) rather than run locally. Upgrading an agent, he notes the model powering it: "we've got deep seek V3 for our large language model that we were using through open router last time" [0:08:21]. That placement, behind an OpenRouter endpoint and swappable, reflects his [provider-independence](../../concepts/provider-independence.md) posture: the agent is [frontend-agnostic](../../concepts/frontend-agnostic-agent.md) and the model is a routable dependency, so V3 can be the driver today and something else tomorrow.

He flags the whole model layer as "the most volatile" part of the stack, which is why V3 matters as a snapshot: at the time of recording it is the open model good enough to build production-shaped agents on, feeding an [agent exposed as an API endpoint](../../concepts/agent-as-api-endpoint.md) with a clean [request/response schema](../../concepts/request-response-schema.md).

## Related

- [Context Engineering](../../concepts/context-engineering.md) - feeding V3 the right context
- [Agent as an API Endpoint](../../concepts/agent-as-api-endpoint.md) - V3 behind a service boundary
- [Frontend-Agnostic Agents](../../concepts/frontend-agnostic-agent.md) - model as a swappable dependency
- [Request/Response Schema](../../concepts/request-response-schema.md)
- [Memory Systems](../../concepts/memory-systems.md), [Chat Interfaces](../../concepts/chat-interfaces.md)
- [DeepSeek R1](./deepseek-r1.md) - sibling reasoning model; [OpenRouter](./openrouter.md) - how Cole accesses V3; [Qwen 2.5 Coder 32B](./qwen.md), [Llama](./llama.md) - sibling open models

## Sources

- [How to DOMINATE with AI in 2025](../../sources/how-to-dominate-with-ai-in-2025.md) - "[0:20:43] for large language models this is probably the most volatile but right now I'm using a lot of the new deep seek V3 I've tested it's performing fantastic"
- [The GLOW-UP Every AI Agent Needs](../../sources/the-glow-up-every-ai-agent-needs.md) - "[0:08:21] we've got deep seek V3 for our large language model that we were using through open router last time"
