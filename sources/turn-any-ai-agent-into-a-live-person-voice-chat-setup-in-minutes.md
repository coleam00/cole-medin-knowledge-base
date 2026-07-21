---
type: source
title: "Turn ANY AI Agent into a Live Person - Voice Chat Setup in Minutes"
description: "You can build and deploy a full voice AI agent with a Google Drive knowledge base in minutes, no coding, by chaining audio input, speech-to-text, an LLM with RAG, and text-to-speech in a no-code platform like Vector Shift."
youtube_id: L9JqdwdCiyE
url: https://www.youtube.com/watch?v=L9JqdwdCiyE
slug: turn-any-ai-agent-into-a-live-person-voice-chat-setup-in-minutes
published: 2024-11-15
duration: "0:16:24"
recency_rank: 142
raw: "../raw/turn-any-ai-agent-into-a-live-person-voice-chat-setup-in-minutes.md"
tags: [voice-agents, no-code, rag, knowledge-base, deployment]
created: 2026-07-21
updated: 2026-07-21
---

[Cole Medin](../entities/people/cole-medin.md) walks through building a complete voice AI agent from scratch inside [Vector Shift](../entities/tools/vector-shift.md), a no-code AI automation platform he favors specifically for its strong voice-agent support. The pipeline is assembled as connected nodes: an audio input, an [OpenAI](../entities/organizations/openai.md) Whisper speech-to-text node, a GPT-4o-mini LLM node, a knowledge-base (RAG) node querying documents ingested from [Google Drive](../entities/tools/google-drive.md), and a text-to-speech node whose audio feeds back to an audio output. The trick that unlocks voice is simply switching the input and output node types from text to audio.

Along the way he demonstrates prompt templating (defining named `{{prompt}}` and `{{context}}` variables inside a node to accept multiple inputs) and how the LLM node can be swapped for essentially any agent, via Integrations, an API or webhook node calling a custom Python agent or an [n8n](../entities/tools/n8n.md) workflow, or bridging to [Zapier](../entities/tools/zapier.md) or Make for missing integrations. Text-to-speech can run through OpenAI or [ElevenLabs](../entities/tools/elevenlabs.md). The finished pipeline is deployed and attached to a Voice Bot, which produces an embeddable chat widget (script tag or iframe) plus a standalone hosted page. Cole positions Vector Shift alongside alternatives like [Flowise](../entities/tools/flowise.md) for this kind of visual build.

He live-tests the agent against his Google Drive knowledge base, and it correctly retrieves silly action items from an 8/23 meeting-notes doc, though it botches the cited source URL, and he notes the response latency is slower than dedicated phone-calling platforms like [Vapi](../entities/tools/vapi.md). Finally he uses [bolt.new](../entities/tools/bolt-new.md) driving a locally-hosted [Qwen 2.5 Coder 32B](../entities/tools/qwen.md) via [Ollama](../entities/tools/ollama.md) to generate a vanilla HTML landing page wrapping the agent's iframe, working around bolt's web-container iframe blocking by pasting the generated code into JSFiddle.

## Concepts covered

- [Voice Agents](../concepts/voice-agents.md)
- [No-Code Automation](../concepts/no-code-automation.md)
- [Visual Workflow Builder](../concepts/visual-workflow-builder.md)
- [Knowledge Bases](../concepts/knowledge-bases.md)
- [Retrieval-Augmented Generation (RAG)](../concepts/rag.md)
- [Prompt Variable Templating](../concepts/prompt-templating.md)
- [Effective Prompting](../concepts/effective-prompting.md)
- [Embeddable Agent Widget](../concepts/embeddable-agent-widget.md)

## Entities

- [Vector Shift](../entities/tools/vector-shift.md)
- [OpenAI](../entities/organizations/openai.md)
- [ElevenLabs](../entities/tools/elevenlabs.md)
- [Google Drive](../entities/tools/google-drive.md)
- [n8n](../entities/tools/n8n.md)
- [Flowise](../entities/tools/flowise.md)
- [Zapier](../entities/tools/zapier.md)
- [bolt.new](../entities/tools/bolt-new.md)
- [Ollama](../entities/tools/ollama.md)
- [Qwen 2.5 Coder 32B](../entities/tools/qwen.md)
- [Vapi](../entities/tools/vapi.md)
- [Cole Medin](../entities/people/cole-medin.md)

## Key moments

- **[0:00:14]** Why voice is hard: most platforms do not make voice agents easy; Vector Shift does
- **[0:02:50]** Starts a new pipeline from scratch with an input node
- **[0:03:15]** Switching the input node type from text to audio is what enables voice
- **[0:03:28]** Adds OpenAI Whisper speech-to-text node
- **[0:03:58]** Adds GPT-4o-mini LLM node with system message and user prompt
- **[0:04:54]** Prompt templating: defining {{prompt}} and {{context}} variables for multiple node inputs
- **[0:05:57]** Swap the LLM for any agent via Integrations, API node, or n8n/Zapier webhooks
- **[0:07:20]** Wires the knowledge base node (RAG) using speech-to-text output as the query
- **[0:08:03]** Adds text-to-speech node (OpenAI or ElevenLabs) and audio output
- **[0:09:08]** Attaches pipeline to a Voice Bot for embeddable widget/iframe deployment
- **[0:12:04]** Live voice test; retrieves action items from the 8/23 knowledge-base doc
- **[0:13:41]** Uses bolt.new + Ollama/Qwen 2.5 Coder to build an HTML front end for the iframe

## Transcript

[Raw transcript](../raw/turn-any-ai-agent-into-a-live-person-voice-chat-setup-in-minutes.md)
