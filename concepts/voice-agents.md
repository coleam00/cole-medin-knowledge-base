---
type: concept
title: "Voice Agents"
description: "Real-time voice-to-voice agents built from speech-to-text and text-to-speech pipelines, where latency is the key constraint."
tags: [voice, speech, latency, agents, real-time, swappable-backend]
videos: [build-render-entire-videos-with-claude-code-full-workflow, build-your-first-voice-ai-agent-in-20-minutes-with-livekit-open-source, turn-any-ai-agent-into-a-live-person-voice-chat-setup-in-minutes, use-open-webui-with-your-n8n-ai-agents-voice-chat-included]
created: 2026-07-21
updated: 2026-07-21
---

# Voice Agents

A voice agent lets a person speak to an agent and hear it speak back, turning a text agent into something that feels like a live person. Cole's framing is that this is a long-requested feature precisely because it changes the feel of the interaction: "a lot of you have asked me to implement voice with a lot of different projects on my channel and I get it it's super nice to be able to just chat with your agents like it's a person." The reason it stayed on the back burner is friction, not desire: "one of the biggest reasons I haven't focused on voice agents at this point is most platforms don't make it very easy to implement them."

There are two ways to build one. The composable route bolts speech onto an existing text agent: you add a step to "turn this audio into text so we can feed it into the large language model," send that transcript to the model, then read the reply back with text-to-speech. The direct route uses a single voice-to-voice model, "there are also voicetovoice options with the OpenAI real-time API for example." The composable route is the more common one on Cole's channel because it reuses an agent he already built and keeps each stage swappable. For pure narration a voice agent can even be one-shot rather than conversational: "we're going to make a single call to ElevenLabs, send in the full script, get the audio out, and then we're going to sync the animation timing to the video."

The recurring practical constraints are latency and audio hygiene. Because every turn passes through transcription, reasoning, and synthesis, delay compounds, which is why real-time voice work obsesses over shaving each stage. Environment is the other trap: playing responses aloud over speakers can feed the agent its own voice, "the only thing that's kind of awkward is I was playing the audio right out of my speaker so it actually picked it up and thought I was talking." When the plumbing is in place, though, the result is a genuinely different product, "as promised you can use voice to chat with your n8n AI agents it is just an incredible feature of open web UI."

## Builds on

- [Voice Agent Pipeline](./voice-pipeline.md) - the speech-to-text, LLM, text-to-speech architecture a voice agent runs on.

## Related

- [No-Code Automation](./no-code-automation.md) - adding a speech-to-text node to an existing no-code agent.
- [Visual Workflow Builder](./visual-workflow-builder.md) - the multimodal nodes that wire voice into a flow.
- [Prompt Engineering](./prompt-engineering.md) - the underlying text agent still needs a well-crafted prompt.

## Tools

- [ElevenLabs](../entities/tools/elevenlabs.md) - text-to-speech for narration and agent replies.
- [n8n](../entities/tools/n8n.md) - hosts the text agent that voice is layered onto.
- [Open Web UI](../entities/tools/open-web-ui.md) - front end that adds built-in voice chat over an n8n agent.
- [OpenAI](../entities/organizations/openai.md) - real-time voice-to-voice API as the single-model route.

## Sources

- [Turn ANY AI Agent into a Live Person - Voice Chat Setup in Minutes](../sources/turn-any-ai-agent-into-a-live-person-voice-chat-setup-in-minutes.md) - "[0:00:14] one of the biggest reasons I haven't focused on voice agents at this point is most platforms don't make it very easy to implement them."
- [Turn ANY AI Agent into a Live Person - Voice Chat Setup in Minutes](../sources/turn-any-ai-agent-into-a-live-person-voice-chat-setup-in-minutes.md) - "[0:03:28] the next thing we have to do is turn this audio into text so we can feed it into the large language model... we have this multimodal tab and we have our speech to text node."
- [Build Your First Voice AI Agent in 20 Minutes with LiveKit (Open Source)](../sources/build-your-first-voice-ai-agent-in-20-minutes-with-livekit-open-source.md) - "[0:04:15] And there are also voicetovoice options with the OpenAI real-time API for example."
- [Build + Render ENTIRE Videos with Claude Code (Full Workflow)](../sources/build-render-entire-videos-with-claude-code-full-workflow.md) - "[0:08:39] we're going to make a single call to ElevenLabs, send in the full script, get the audio out, and then we're going to sync the animation timing to the video."
- [Use Open WebUI with Your N8N AI Agents - Voice Chat Included!](../sources/use-open-webui-with-your-n8n-ai-agents-voice-chat-included.md) - "[0:25:03] the only thing that's kind of awkward is I was playing the audio right out of my speaker so it actually picked it up and thought I was talking."
