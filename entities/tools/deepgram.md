---
type: entity
subtype: tool
title: "Deepgram"
description: "Speech-to-text provider (with a free tier) used as the transcription stage of the deployed LiveKit voice pipeline."
resource: "https://deepgram.com"
tags: [voice, speech-to-text, media]
videos: [build-your-first-voice-ai-agent-in-20-minutes-with-livekit-open-source]
created: 2026-07-21
updated: 2026-07-21
---

# Deepgram

Deepgram is a hosted speech-to-text (STT) API, and in Cole's catalog it plays exactly one role: the transcription stage at the front of a [voice agent pipeline](../../concepts/voice-pipeline.md). When he deploys a [LiveKit](./livekit.md) agent to the cloud, the provider shows up as nothing more than a key in the environment: "We specify our deepgram API key and then the large language model that we want to use for that part of our voice pipeline" [0:15:25]. That framing is the point. STT is a swappable slot, not an architectural commitment.

The pipeline it feeds is STT to LLM to TTS. Deepgram converts the caller's audio into text, the model reasons over that text and calls tools, and a text-to-speech provider like [ElevenLabs](./elevenlabs.md) or the free [Kokoro](./kokoro.md) speaks the answer back. Because each stage is named independently in the agent's session config, swapping Deepgram for another transcriber is a one-line change, which is the concrete payoff of [provider independence](../../concepts/provider-independence.md) at the component level rather than only at the model level.

The other reason Deepgram appears is cost. Cole builds and ships the entire LiveKit agent without paying for the voice infrastructure: "I'm not paying for anything for LiveKit or for Deepgram in this video" [0:14:25]. Only the LLM key is billed. That free tier is what makes a working, deployed [voice agent](../../concepts/voice-agents.md) something you can stand up in twenty minutes instead of committing to per-minute pricing on a no-code platform.

## Realizes

- [Voice Agent Pipeline](../../concepts/voice-pipeline.md) - The speech-to-text, LLM reasoning, and text-to-speech pipeline architecture that turns an agent into a real-time voice assistant (e.g. with LiveKit).
- [Voice Agents](../../concepts/voice-agents.md) - Real-time voice-to-voice agents built from speech-to-text and text-to-speech pipelines, where latency is the key constraint.

## Works with

- [LiveKit](./livekit.md) - Open-source Python framework for building customizable, self-hostable voice AI agents with a swappable STT/LLM/TTS pipeline, tool calling, MCP server support, and a CLI deploy path to LiveKit Cloud.
- [ElevenLabs](./elevenlabs.md) - The paid text-to-speech provider used for high-quality narration and voice cloning (though cloning takes work to make reliable).
- [Kokoro](./kokoro.md) - A free, open-source text-to-speech model that lets you run the entire AI video-generation workflow at no cost.

## Contrasts with

- [OpenAI Whisper](./whisper.md) - OpenAI's open-source speech-to-text model; Whisper Turbo runs fully locally as Docling's ASR pipeline to transcribe audio and video into timestamped text.
- [Aqua Voice](./aqua-voice.md) - Speech-to-text platform Cole uses to dictate into any text box, especially for communicating with LLMs.
- [Vapi](./vapi.md) - No-code voice AI platform cited as easy but a black box, which Cole and clients have moved off of for custom solutions.

## Related

- [Provider Independence](../../concepts/provider-independence.md) - Architecting agents so the underlying model, framework, or client can be swapped without a rewrite, avoiding lock-in through low-level abstractions.
- [Agent Deployment](../../concepts/agent-deployment.md) - Getting agents to production, containerizing, networking, reverse-proxying, and choosing a provider-agnostic, cost-predictable host.
- [Local & Self-Hosted AI](../../concepts/local-ai.md) - Running open-weight models on your own hardware or cloud for privacy, cost control, and independence from API providers.
- [Model Selection](../../concepts/model-selection.md) - Choosing the right LLM per task by trading off quality, speed, and cost, often routing easy requests to cheap models and hard ones to expensive models.

## Sources

- [Build Your First Voice AI Agent in 20 Minutes with LiveKit (Open Source)](../../sources/build-your-first-voice-ai-agent-in-20-minutes-with-livekit-open-source.md) - "[0:15:25] We specify our deepgram API key and then the large language model that we want to use for that part of our voice pipeline."
- [Build Your First Voice AI Agent in 20 Minutes with LiveKit (Open Source)](../../sources/build-your-first-voice-ai-agent-in-20-minutes-with-livekit-open-source.md) - "[0:14:25] I'm not paying for anything for LiveKit or for Deepgram in this video."
