---
type: source
title: "I Made a Custom AI Chatbot Site in 47 Lines of Code"
description: "You can build a fully-functional GPT-powered custom chatbot with a real web UI in just 47 lines of Python using Streamlit and LangChain, which is the foundation for building AI agents that go beyond what ChatGPT can do."
youtube_id: blQAUBtCgdc
url: https://www.youtube.com/watch?v=blQAUBtCgdc
slug: i-made-a-custom-ai-chatbot-site-in-47-lines-of-code
published: 2024-07-03
duration: "0:08:46"
recency_rank: 186
raw: "../raw/i-made-a-custom-ai-chatbot-site-in-47-lines-of-code.md"
tags: [chat-interfaces, generative-ui, streaming-responses, system-prompt-engineering]
created: 2026-07-21
updated: 2026-07-21
---

# I Made a Custom AI Chatbot Site in 47 Lines of Code

Cole walks through building a custom GPT-powered chatbot with a complete user interface in only 47 lines of Python. He opens by answering the obvious objection: why build a custom chatbot instead of just using the ChatGPT website? The answer is power and extensibility. A custom chatbot can interact with external services, third-party libraries, and API endpoints to do things ChatGPT cannot, like scheduling appointments, managing tasks, or checking calendar availability. This is the entry point into building AI agents.

The build uses Streamlit for the UI and LangChain for talking to the LLM (GPT-4o by default, set via an environment variable). He covers the core mechanics: adding UI components by calling `st.<component>` (title, chat_message, chat_input), seeding the conversation with a system message that sets context (including the current date, which many models lack), and the critical Streamlit behavior that the entire Python script reruns on every UI state change. Because of this rerun model, message history must be persisted in Streamlit's session state and guarded with an `if messages not in session_state` check so it is not reset on every rerun.

When the user submits a prompt, the app appends it to both the UI and the session state, invokes the LLM with the full message history, and streams the response back in typewriter style via Streamlit's stream writer. The AI's response is then also saved to session state. Cole notes the demo chatbot is basic and not yet worth using over ChatGPT, but stresses the real value: now that it is custom-coded, it can be extended into an AI agent that interacts with a calendar, tasks, Discord, or Slack.

## Concepts covered

- [Chat Interfaces](../concepts/chat-interfaces.md)
- [Agentic Workflow Engineering](../concepts/agentic-workflow-engineering.md)
- [System Prompt Engineering](../concepts/system-prompt-engineering.md)
- [Generative UI](../concepts/generative-ui.md)
- [Memory Systems](../concepts/memory-systems.md)
- [Streaming Responses](../concepts/streaming-responses.md)
- [Model Selection](../concepts/model-selection.md)

## Entities

- [Streamlit](../entities/tools/streamlit.md)
- [LangChain](../entities/tools/langchain.md)
- [OpenAI](../entities/organizations/openai.md)
- [GPT-4o](../entities/tools/gpt-4o.md)
- [GitHub](../entities/tools/github.md)
- [Cole Medin](../entities/people/cole-medin.md)

## Key moments

- **[0:00:00]** Intro: build a GPT-powered custom chatbot UI in 47 lines of Python
- **[0:00:17]** Why build a custom chatbot instead of using the ChatGPT website: power and external integrations
- **[0:01:33]** Imports, requirements.txt, and .env.example for OpenAI auth plus model selection
- **[0:02:19]** Model defaults to GPT-4o via LLM_MODEL env var
- **[0:02:33]** Initializing the system message in Streamlit session state
- **[0:03:17]** Streamlit reruns the entire script on every UI state change, why the session-state guard matters
- **[0:04:31]** chat_input component captures the user prompt
- **[0:05:17]** Create OpenAI chatbot instance and stream the response into the UI
- **[0:06:47]** Running the app and demoing it live in the browser with typewriter streaming
- **[0:08:05]** Next step: extend the custom chatbot into an AI agent that touches calendar, tasks, Discord, Slack

## Transcript

[Raw transcript](../raw/i-made-a-custom-ai-chatbot-site-in-47-lines-of-code.md)
