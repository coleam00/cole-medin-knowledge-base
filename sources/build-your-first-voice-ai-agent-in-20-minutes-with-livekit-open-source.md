---
type: source
title: "Build Your First Voice AI Agent in 20 Minutes with LiveKit (Open Source)"
description: "LiveKit is an open-source Python framework that makes building fully customizable, self-hostable voice AI agents nearly as easy as no-code platforms like Vapi, but without the black-box trade-offs."
youtube_id: TXVyxJdlzQs
url: https://www.youtube.com/watch?v=TXVyxJdlzQs
slug: build-your-first-voice-ai-agent-in-20-minutes-with-livekit-open-source
published: 2025-10-04
duration: "0:19:01"
recency_rank: 65
raw: "../raw/build-your-first-voice-ai-agent-in-20-minutes-with-livekit-open-source.md"
tags: [voice-agents, livekit, python, deployment]
created: 2026-07-21
updated: 2026-07-21
---

Cole builds a voice AI agent from scratch with LiveKit, an open-source Python framework, positioning it against no-code voice platforms (Vapi, Synthflow, Bland.ai) that lock you into premium per-minute pricing, slow tool calls, and a customization-limiting black box. He walks through a roughly 52-line basic agent: import LiveKit dependencies, define an Assistant agent class with a system prompt, and set up an AgentSession that wires a voice pipeline, a speech-to-text model at the front, an LLM in the middle, and a text-to-speech model at the end (with OpenAI's realtime API as a voice-to-voice alternative). A room maintains conversation history and the agent can generate an initial greeting so the user does not have to speak first.

He then layers on capability: tools are just Python functions with an @function_tool decorator whose docstring tells the agent when and how to use them, the same pattern as Pydantic AI or CrewAI. He demos a date/time tool, then a mock Airbnb search-and-book assistant that clarifies missing arguments, then swaps in the real Airbnb API via an MCP server (served over streamable HTTP through Docker's MCP gateway), which connects to LiveKit by simply passing the server URL in an mcp_servers list.

Finally he deploys the local agent to the cloud using the LiveKit CLI (lk): authenticate, set environment variables (OpenAI plus Deepgram keys, LLM choice), run start, then lk agent create to build a Dockerfile and ship it. The deployed agent is testable in the browser playground, and can be extended with telephony (a real phone number via a Twilio-style integration). LiveKit is free and open source, so everything can be self-hosted for full control; the only paid piece in the demo is the OpenAI API key.

## Concepts covered

- [Voice Agent Pipeline](../concepts/voice-pipeline.md)
- [Voice Agents](../concepts/voice-agents.md)
- [Tool Calling](../concepts/tool-use.md)
- [Clarifying Questions](../concepts/clarifying-questions.md)
- [Provider Independence](../concepts/provider-independence.md)
- [Agent Deployment](../concepts/agent-deployment.md)

## Entities

- [OpenAI](../entities/organizations/openai.md)
- [Cartesia](../entities/organizations/cartesia.md)
- [Anthropic](../entities/organizations/anthropic.md)
- [MCP (Model Context Protocol)](../entities/tools/mcp.md)
- [Docker](../entities/tools/docker.md)
- [Vapi](../entities/tools/vapi.md)
- [Archon](../entities/tools/archon.md)
- [Dynamous](../entities/organizations/dynamous.md)
- [Cole Medin](../entities/people/cole-medin.md)

## Key moments

- **[0:00:00]** Framing: no-code voice platforms (Vapi/Synthflow/Bland) are easy but a black box, with slow tool calls, premium per-minute pricing, hard to customize
- **[0:00:40]** LiveKit intro: open-source Python framework, full control, MCP integrations, self-host or LiveKit cloud
- **[0:03:45]** The voice pipeline explained: STT to LLM to TTS, plus voice-to-voice via OpenAI realtime API
- **[0:04:46]** AgentSession + room maintains conversation history; agent generates an initial greeting so the user doesn't speak first
- **[0:05:44]** First working agent in ~52 lines, tested in the console
- **[0:06:54]** Adding a tool = a plain Python function + @function_tool decorator; docstring tells the agent when/how to use it
- **[0:08:08]** Mock Airbnb search/book assistant; agent clarifies arguments it doesn't yet know
- **[0:10:05]** Swapping mock data for the real Airbnb API via an MCP server over Docker's MCP gateway
- **[0:11:23]** Connecting MCP to LiveKit = pass the server URL in an mcp_servers list (local, no auth)
- **[0:13:53]** Deploying to the cloud with the LiveKit CLI (lk): auth, env vars, start, lk agent create to Dockerfile
- **[0:17:29]** Deployed agent tested in the browser playground; telephony (phone number) teased as next step

## Transcript

[Raw transcript](../raw/build-your-first-voice-ai-agent-in-20-minutes-with-livekit-open-source.md)
