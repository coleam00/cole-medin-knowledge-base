---
type: entity
subtype: organization
title: "Cartesia"
description: "Named as one of the swappable speech providers available for the LiveKit voice pipeline."
resource: "https://cartesia.ai"
tags: [voice, speech, tts, provider]
videos: [build-your-first-voice-ai-agent-in-20-minutes-with-livekit-open-source, the-ultimate-n8n-rag-ai-agent-template-local-ai-edition]
created: 2026-07-21
updated: 2026-07-21
---

# Cartesia

Cartesia is a speech-model company that Cole names as one of the interchangeable providers you can slot into a voice-agent stack. In his LiveKit build he treats it as a drop-in option for the speech-to-text stage: "if you wanted to use Anthropic for the LLM instead or Cartesia for speech to text. There's a lot of different providers that are available." That framing is the point of the mention, Cartesia is one node in a [voice pipeline](../../concepts/voice-pipeline.md) whose every stage (STT, LLM, TTS) is swappable, an embodiment of [provider independence](../../concepts/provider-independence.md).

The company's technical differentiator, in Cole's telling, is its architecture. Discussing its roadmap he notes it is "about to release Sonic 2.0 their next model that is a complete GameChanger it's based on a revolutionary State space model architecture." State-space models promise very low latency, which matters enormously for [voice agents](../../concepts/voice-agents.md) where any lag between a person speaking and the agent responding breaks the illusion of a real conversation. Cartesia therefore competes on the speed and naturalness of turning text into speech (and speech into text), the exact qualities that make a spoken agent feel human.

Cole does not build a dedicated Cartesia tutorial; instead the org recurs as a named alternative alongside other speech vendors when he wants to show that a voice stack is not locked to one provider. In that role it pairs naturally with [tool use](../../concepts/tool-use.md) and [clarifying questions](../../concepts/clarifying-questions.md), the behaviors a deployed voice agent needs once the audio layer is handled, and it slots into whatever [deployment](../../concepts/agent-deployment.md) target the rest of the agent runs on.

## Works with

- [Voice Agent Pipeline](../../concepts/voice-pipeline.md) - The speech-to-text, LLM reasoning, and text-to-speech pipeline architecture that turns an agent into a real-time voice assistant (e.g. with LiveKit).
- [Voice Agents](../../concepts/voice-agents.md) - Real-time voice-to-voice agents built from speech-to-text and text-to-speech pipelines, where latency is the key constraint.

## Contrasts with

- [ElevenLabs](../tools/elevenlabs.md) - The paid text-to-speech provider used for high-quality narration and voice cloning (though cloning takes work to make reliable).

## Related

- [Provider Independence](../../concepts/provider-independence.md) - Architecting agents so the underlying model, framework, or client can be swapped without a rewrite, avoiding lock-in through low-level abstractions.
- [Tool Calling](../../concepts/tool-use.md) - Letting an LLM invoke external functions and APIs so it can take actions and fetch data beyond its parametric knowledge.
- [Clarifying Questions](../../concepts/clarifying-questions.md) - Having the agent ask targeted questions up front to infer intent and reduce assumptions before it plans or builds.
- [Agent Deployment](../../concepts/agent-deployment.md) - Getting agents to production, containerizing, networking, reverse-proxying, and choosing a provider-agnostic, cost-predictable host.
- [Anthropic](./anthropic.md) - Maker of Claude and Claude Code, creator of MCP, and Cole's pick for the best coding LLM and the lab whose research most shapes his practice.

## Sources

- [Build Your First Voice AI Agent in 20 Minutes with LiveKit (Open Source)](../../sources/build-your-first-voice-ai-agent-in-20-minutes-with-livekit-open-source.md) - "[0:04:15] if you wanted to use Anthropic for the LLM instead or Cartesia for speech to text. There's a lot of different providers that are available"
- [The ULTIMATE n8n RAG AI Agent Template - Local AI Edition](../../sources/the-ultimate-n8n-rag-ai-agent-template-local-ai-edition.md) - "[0:11:23] they are also about to release Sonic 2.0 their next model that is a complete GameChanger it's based on a revolutionary State space model architecture"
