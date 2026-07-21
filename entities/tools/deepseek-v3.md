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

DeepSeek V3 is DeepSeek's open, general-purpose (non-reasoning) LLM, and Cole treats it as fresh evidence that open models have closed most of the gap on closed frontier models. In his 2025 stack rundown he names it his current pick and vouches for it from real use: "for large language models this is probably the most volatile but right now I'm using a lot of the new DeepSeek V3 I've tested it's performing fantastic" [0:20:43]. Where its sibling [DeepSeek R1](./deepseek-r1.md) is the reasoning model, V3 is the fast general workhorse.

## How Cole uses it

V3 is the default LLM in his current agent builds, typically accessed through [OpenRouter](./openrouter.md) rather than run locally. Upgrading an agent, he notes the model powering it: "we've got DeepSeek V3 for our large language model that we were using through OpenRouter last time" [0:08:21]. That placement, behind an OpenRouter endpoint and swappable, reflects his [provider-independence](../../concepts/provider-independence.md) posture: the agent is [frontend-agnostic](../../concepts/frontend-agnostic-agent.md) and the model is a routable dependency, so V3 can be the driver today and something else tomorrow.

He flags the whole model layer as "the most volatile" part of the stack, which is why V3 matters as a snapshot: at the time of recording it is the open model good enough to build production-shaped agents on, feeding an [agent exposed as an API endpoint](../../concepts/agent-as-api-endpoint.md) with a clean [request/response schema](../../concepts/request-response-schema.md).

## Contrasts with

- [DeepSeek R1](./deepseek-r1.md) - Open-source MIT-licensed reasoning LLM that rivals OpenAI o1, ships in distilled sizes, and is far cheaper to run.
- [Qwen](./qwen.md) - Alibaba's open-source LLM family Cole cites as among his favorites that stood the test of time.
- [Llama](./llama.md) - The open LLM model powering the agent, served via Groq in the current build.
- [DeepSeek Coder V2](./deepseek-coder-v2.md) - Open-source 236B-parameter coding model available via OpenRouter or the DeepSeek API, recommended as roughly 20x cheaper than Claude while remaining highly capable for AI coding.

## Works with

- [OpenRouter](./openrouter.md) - Unified API gateway to many LLMs; here it hosts Quasar Alpha, its first stealth/cloaked pre-release Foundation model, free to use.

## Related

- [Context Engineering](../../concepts/context-engineering.md) - The deliberate practice of curating exactly what goes into an LLM's limited context window - system messages, schemas, chat history, and dynamic variables - to avoid overload and keep outputs sharp.
- [Agent as an API Endpoint](../../concepts/agent-as-api-endpoint.md) - Wrapping an AI agent in a web API (typically FastAPI) turns it from a terminal-bound script into a deployable, scalable service any frontend, SaaS, or client can call remotely.
- [Frontend-Agnostic Agents](../../concepts/frontend-agnostic-agent.md) - Decouple the agent backend from any specific UI by emitting standardized events and subscribing to real-time messages (AG-UI, agentic experiences), so the same agent can power any frontend.
- [Agent Request/Response Schema](../../concepts/request-response-schema.md) - Standardizing how any agent plugs in by fixing a strict input payload (query, user_id, request_id, session_id) and a minimal output (a success boolean), so agents become interchangeable behind a common contract.
- [Memory Systems](../../concepts/memory-systems.md) - Giving agents durable short- and long-term memory so conversations, user context, and facts persist across sessions and users.
- [Chat Interfaces](../../concepts/chat-interfaces.md) - Wrapping agents in chat surfaces (websites, DMs, platforms) with adapters, a shared message format, and durable history.

## Sources

- [How to DOMINATE with AI in 2025](../../sources/how-to-dominate-with-ai-in-2025.md) - "[0:20:43] for large language models this is probably the most volatile but right now I'm using a lot of the new DeepSeek V3 I've tested it's performing fantastic"
- [The GLOW-UP Every AI Agent Needs](../../sources/the-glow-up-every-ai-agent-needs.md) - "[0:08:21] we've got DeepSeek V3 for our large language model that we were using through OpenRouter last time"
