---
type: entity
subtype: tool
title: "OpenAI Whisper"
description: "OpenAI's open-source speech-to-text model; Whisper Turbo runs fully locally as Docling's ASR pipeline to transcribe audio and video into timestamped text."
resource: "https://github.com/openai/whisper"
tags: [voice, media]
videos: [turn-any-file-into-llm-knowledge-in-seconds, turn-any-ai-agent-into-a-live-person-voice-chat-setup-in-minutes]
created: 2026-07-21
updated: 2026-07-21
---

# OpenAI Whisper

Whisper is [OpenAI's](../organizations/openai.md) open-weight speech-to-text model, and Cole's one-line definition is also his recommendation: "I did add OpenAI Whisper, which is an open source tool. We're going to be using Whisper Turbo as our speech to text model completely locally" [0:08:34]. Open source and completely local are the two properties that matter. Whisper is the rare default that costs nothing per minute and never sends audio to a vendor.

Its main job in this catalog is turning audio into knowledge base material. [Docling](./docling.md) handles every other file type, and audio is the one case that needs extra dependencies: FFmpeg plus Whisper, wired up as an ASR pipeline that Docling's converter drives like any other format. The output is markdown, same as a PDF or a Word doc, so a podcast or a recorded meeting drops straight into the same [chunking](../../concepts/chunking.md) and ingestion path as text. Cole notes the whole thing runs on models pulled from [Hugging Face](../organizations/hugging-face.md) with nothing hosted, and that a 30-second clip transcribed in about 10 seconds into 576 characters, with per-sentence timestamps included. That makes [document extraction](../../concepts/document-extraction.md) from media a solved step rather than a separate vendor bill, and it keeps ingestion at the strictest tier of [LLM data privacy](../../concepts/llm-data-privacy-tiers.md).

Its second role is the front of a [voice pipeline](../../concepts/voice-pipeline.md). Building a voice agent on [Vector Shift](./vector-shift.md), Cole drops in a speech-to-text node between the audio input and the LLM, and picks Whisper without deliberating: "there's a couple of options here for the model I just recommend using open AI whisper" [0:03:44]. The transcript then flows into [GPT-4o mini](./gpt-4o-mini.md) with a knowledge base attached. Same model, same slot, one layer up: whether the audio is a stored file or a live speaker, transcription is a swappable stage, and Whisper is the default that works.

## Realizes

- [Document Extraction](../../concepts/document-extraction.md) - Pulling clean raw text out of source files (PDFs, Excel, HTML, JSON) is the real bottleneck in RAG ingestion, solved by branching on each file's MIME type to a format-specific extractor rather than one universal node.
- [Voice Agent Pipeline](../../concepts/voice-pipeline.md) - The speech-to-text, LLM reasoning, and text-to-speech pipeline architecture that turns an agent into a real-time voice assistant (e.g. with LiveKit).

## Works with

- [Docling](./docling.md) - The open-source Python data-extraction/chunking tool that is the subject of the video summarized and integrated into Archon during the workflow demo.
- [Vector Shift](./vector-shift.md) - A visual AI-workflow builder cited as a comparable node-based platform.
- [GPT-4o mini](./gpt-4o-mini.md) - A fast, cheap OpenAI model cited as a speed benchmark; Quasar Alpha runs the MCP agent army even faster than it.
- [Hugging Face](../organizations/hugging-face.md) - AI platform whose blog post and AI Agents course provide the starting definition: programs where LLM outputs control the workflow to achieve a goal.

## Contrasts with

- [Deepgram](./deepgram.md) - Speech-to-text provider (with a free tier) used as the transcription stage of the deployed LiveKit voice pipeline.
- [Aqua Voice](./aqua-voice.md) - Speech-to-text platform Cole uses to dictate into any text box, especially for communicating with LLMs.
- [Kokoro](./kokoro.md) - A free, open-source text-to-speech model that lets you run the entire AI video-generation workflow at no cost.

## Related

- [Local & Self-Hosted AI](../../concepts/local-ai.md) - Running open-weight models on your own hardware or cloud for privacy, cost control, and independence from API providers.
- [Knowledge Bases](../../concepts/knowledge-bases.md) - Curated bodies of knowledge an agent can retrieve from, distinct from raw model weights, that ground responses in trusted source material.
- [Chunking](../../concepts/chunking.md) - Splitting source documents into appropriately sized, embeddable segments, the foundational preprocessing step that determines RAG retrieval quality.
- [Voice Agents](../../concepts/voice-agents.md) - Real-time voice-to-voice agents built from speech-to-text and text-to-speech pipelines, where latency is the key constraint.
- [LLM Data Privacy Tiers](../../concepts/llm-data-privacy-tiers.md) - The privacy ladder from closed models that may train on your data, to hosted open-model providers, to true self-hosting - and using mock data until you reach the tier your workload requires.

## Sources

- [Turn ANY File into LLM Knowledge in SECONDS](../../sources/turn-any-file-into-llm-knowledge-in-seconds.md) - "[0:08:34] I did add OpenAI Whisper, which is an open source tool. We're going to be using Whisper Turbo as our speech to text model completely locally."
- [Turn ANY AI Agent into a Live Person - Voice Chat Setup in Minutes](../../sources/turn-any-ai-agent-into-a-live-person-voice-chat-setup-in-minutes.md) - "[0:03:44] there's a couple of options here for the model I just recommend using open AI whisper"
