---
type: concept
title: "Voice Agent Pipeline"
description: "The speech-to-text, LLM reasoning, and text-to-speech pipeline architecture that turns an agent into a real-time voice assistant (e.g. with LiveKit)."
tags: [voice, livekit, stt, tts, real-time, pipeline]
videos: [build-your-first-voice-ai-agent-in-20-minutes-with-livekit-open-source]
created: 2026-07-21
updated: 2026-07-21
---

# Voice Agent Pipeline

The voice agent pipeline is the three-stage architecture that converts spoken input into a spoken reply. Cole lays out the whole chain in one line: "you have your speechtoext model that sits at the front and then it goes to the large language model. So whatever speech it transcribes into text it goes to the LLM to get the response and then the response goes through a texttospech model so that we have the voice come out." Speech-to-text (STT) transcribes the user, the LLM reasons over that text, and text-to-speech (TTS) synthesizes the answer back into audio. In a LiveKit build these three stages are assembled into one object, "this is our session where we define our voice pipeline," so the framework handles the streaming and turn-taking between them.

The pipeline shape is what makes each stage independently swappable: you can change the STT model, the LLM, or the TTS voice without rewriting the others, because the interface between them is just text. That modularity is also the pipeline's defining tradeoff against a single voice-to-voice model. A three-hop pipeline gives you fine-grained control and provider choice at every stage, but every hop adds latency, so the transcription, reasoning, and synthesis steps each become a place to optimize for responsiveness. Because the middle stage is an ordinary LLM call, the same model-selection reasoning that governs any agent applies here, with the added pressure that a slow model is far more noticeable in a live spoken conversation than in text.

## Part of

- [Voice Agents](./voice-agents.md) - the pipeline is the architecture a real-time voice agent runs on.

## Related

- [Model Selection](./model-selection.md) - choosing the LLM for the reasoning stage, where speed is weighed heavily.

## Tools

- [LiveKit](../entities/tools/livekit.md) - Open-source Python framework for building customizable, self-hostable voice AI agents with a swappable STT/LLM/TTS pipeline, tool calling, MCP server support, and a CLI deploy path to LiveKit Cloud.
- [OpenAI](../entities/organizations/openai.md) - supplies STT, LLM, and TTS stages, or a single real-time voice-to-voice alternative to the pipeline.
- [Deepgram](../entities/tools/deepgram.md) - Speech-to-text provider (with a free tier) used as the transcription stage of the deployed LiveKit voice pipeline.
- [Kokoro](../entities/tools/kokoro.md) - A free, open-source text-to-speech model that lets you run the entire AI video-generation workflow at no cost.

## Sources

- [Build Your First Voice AI Agent in 20 Minutes with LiveKit (Open Source)](../sources/build-your-first-voice-ai-agent-in-20-minutes-with-livekit-open-source.md) - "[0:03:45] you have your speechtoext model that sits at the front and then it goes to the large language model. So whatever speech it transcribes into text it goes to the LLM to get the response and then the response goes through a texttospech model so that we have the voice come out."
- [Build Your First Voice AI Agent in 20 Minutes with LiveKit (Open Source)](../sources/build-your-first-voice-ai-agent-in-20-minutes-with-livekit-open-source.md) - "[0:04:31] this is our session where we define our voice pipeline."
