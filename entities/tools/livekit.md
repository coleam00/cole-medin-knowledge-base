---
type: entity
subtype: tool
title: "LiveKit"
description: "Open-source Python framework for building customizable, self-hostable voice AI agents with a swappable STT/LLM/TTS pipeline, tool calling, MCP server support, and a CLI deploy path to LiveKit Cloud."
resource: "https://livekit.io"
tags: [voice, media]
videos: [build-your-first-voice-ai-agent-in-20-minutes-with-livekit-open-source]
created: 2026-07-21
updated: 2026-07-21
---

# LiveKit

LiveKit is the code-first answer to no-code voice platforms. Cole defines it in one line: "LiveKit is an open-source Python framework for building your agents with code. So, it gives you full customization, control over your conversation logic, direct integrations with your tools and MCP servers" [0:00:40]. He deflates the mystique just as directly later: "LiveKit really is just another AI agent framework, but for building voice agents in particular" [0:07:25]. Everything you already know about building agents in [Python](./python.md) carries over; what LiveKit adds is the real-time audio plumbing.

That plumbing is the [voice pipeline](../../concepts/voice-pipeline.md): a speech-to-text model at the front, an LLM in the middle, a text-to-speech model at the end, assembled inside an AgentSession, with a room that maintains conversation history and an agent that can speak first so the user is not left staring at silence. OpenAI's realtime API drops in as a single voice-to-voice alternative when you want to skip the three-stage chain. Each stage is a swappable plugin, which is [provider independence](../../concepts/provider-independence.md) at the pipeline level rather than a marketing claim. A working agent is roughly 52 lines.

Capability is layered the same way as any other framework. A tool is a plain Python function with an @function_tool decorator whose [docstring tells the agent when and how to call it](../../concepts/docstrings-as-tool-descriptions.md), identical to the [Pydantic AI](./pydantic-ai.md) and [CrewAI](./crewai.md) pattern, and the agent will ask [clarifying questions](../../concepts/clarifying-questions.md) for arguments it does not have. Real integrations arrive through [MCP](./mcp.md): Cole swaps mock Airbnb data for the live API by serving it over streamable HTTP through [Docker](./docker.md)'s MCP gateway and passing the URL in an mcp_servers list.

Deployment is a CLI story. The lk tool authenticates, takes environment variables, runs the agent, and lk agent create generates a Dockerfile and ships it to LiveKit Cloud, where a browser playground exercises the deployed agent and telephony can attach a real phone number. Because the framework is free and open source, the whole stack is self-hostable, which is the trade LiveKit is really offering against [Vapi](./vapi.md): more assembly up front in exchange for escaping per-minute premium pricing, slow tool calls, and a black box you cannot open.

## Realizes

- [Voice Agent Pipeline](../../concepts/voice-pipeline.md) - The speech-to-text, LLM reasoning, and text-to-speech architecture that turns an agent into a real-time voice assistant.
- [Voice Agents](../../concepts/voice-agents.md) - Real-time voice-to-voice agents where latency is the key constraint.
- [Tool Calling](../../concepts/tool-use.md) - Letting the LLM invoke external functions and APIs so it can act beyond its parametric knowledge.
- [Docstrings as Tool Descriptions](../../concepts/docstrings-as-tool-descriptions.md) - Writing function docstrings that double as the tool descriptions the agent reads.
- [Agent Deployment](../../concepts/agent-deployment.md) - Getting agents to production through containerization, environment config, and a provider-agnostic host.
- [Provider Independence](../../concepts/provider-independence.md) - Architecting so the model, speech provider, or client can be swapped without a rewrite.

## Works with

- [MCP (Model Context Protocol)](./mcp.md) - Real integrations attach by passing MCP server URLs in an mcp_servers list.
- [Docker](./docker.md) - Serves the MCP gateway locally and packages the agent for cloud deployment.
- [Deepgram](./deepgram.md) - Speech-to-text provider (with a free tier) used as the transcription stage of the deployed pipeline.
- [ElevenLabs](./elevenlabs.md) - High-quality text-to-speech provider, the kind of plugin that slots into the pipeline's final stage.
- [Python](./python.md) - The language the agent, its tools, and its session config are written in.

## Contrasts with

- [Vapi](./vapi.md) - No-code voice AI platform that is easy but a black box, with slow tool calls and premium per-minute pricing.
- [Pydantic AI](./pydantic-ai.md) - Cole's general-purpose agent framework; same tool-decorator ergonomics, no voice pipeline.
- [CrewAI](./crewai.md) - Multi-agent Python framework named alongside Pydantic AI for the identical tool pattern.
- [Vector Shift](./vector-shift.md) - A visual AI-workflow builder where the same voice pipeline is assembled as nodes on a canvas instead of code.
- [Voiceflow](./voiceflow.md) - Conversational-AI builder, the node-based route to the same conversation logic.

## Related

- [Clarifying Questions](../../concepts/clarifying-questions.md) - Having the agent ask targeted questions before acting to reduce assumptions.
- [Containerization & Docker Networking](../../concepts/containerization.md) - Running the agent and its services as containers that talk over a private network.
- [Model Context Protocol (MCP)](../../concepts/mcp.md) - The open protocol for packaging tools and data as servers any agent can call.
- [No-Code vs. Code](../../concepts/no-code-vs-code.md) - The use-case-by-use-case decision to build agents visually or in code.
- [Local & Self-Hosted AI](../../concepts/local-ai.md) - Running the stack on your own hardware for privacy, cost control, and independence.
- [Production-Grade Agents](../../concepts/production-grade-agents.md) - What real agents need beyond an LLM plus tools stitched together.

## Sources

- [Build Your First Voice AI Agent in 20 Minutes with LiveKit (Open Source)](../../sources/build-your-first-voice-ai-agent-in-20-minutes-with-livekit-open-source.md) - "[0:00:40] LiveKit is an open-source Python framework for building your agents with code. So, it gives you full customization, control over your conversation logic, direct integrations with your tools and MCP servers"
- [Build Your First Voice AI Agent in 20 Minutes with LiveKit (Open Source)](../../sources/build-your-first-voice-ai-agent-in-20-minutes-with-livekit-open-source.md) - "[0:07:25] LiveKit really is just another AI agent framework, but for building voice agents in particular."
