---
type: source
title: "Developers, THIS is How you Stay Relevant with AI - AI Agents Masterclass #1"
description: "AI agents, LLMs given the ability to interact with the outside world through tool calls, are the real way to unleash AI's power, and you can build a functional one from scratch in a few minutes."
youtube_id: zaNIvRllycM
url: https://www.youtube.com/watch?v=zaNIvRllycM
slug: developers-this-is-how-you-stay-relevant-with-ai-ai-agents-masterclass-1
published: 2024-06-23
duration: "0:16:55"
recency_rank: 189
raw: "../raw/developers-this-is-how-you-stay-relevant-with-ai-ai-agents-masterclass-1.md"
tags: [what-is-an-ai-agent, tool-use, tool-design, agent-loop]
created: 2026-07-21
updated: 2026-07-21
---

# Developers, THIS is How you Stay Relevant with AI - AI Agents Masterclass #1

This is the first episode of Cole's AI Agents Masterclass, arguing that developers who want to stay relevant must focus on AI agents, not just chatbots. He defines an agent simply as a large language model given the ability to interact with the outside world (draft emails, create tasks, update a CRM), and frames tool calling as the thing that turns a plain GPT chatbot into an agent.

The bulk of the video is a from-scratch Python build: a command-line GPT chatbot wired to the Asana API so it can create real tasks. Cole walks through the OpenAI client setup, environment variables for secrets, the message list with its three roles (system, user, assistant), a forever-loop that accumulates chat history, a create_asana_task function, and, critically, the tool schema (a JSON definition with a description telling the model when to call the function and a parameters block telling it what to pass). He shows how the model parses natural language into structured arguments (task name, a correctly-formatted due date), returns tool_calls in its response, and how the code executes the function and feeds the result back so the model can write a final human-facing reply with the task link.

The demo confirms the loop: a normal question gets a normal answer, but "create a task to make a thumbnail, due Wednesday" triggers the tool call and the task appears in Asana. Cole closes by noting the next episode will show an easier, more powerful way to build the same thing.

## Concepts covered

- [What Is an AI Agent](../concepts/what-is-an-ai-agent.md)
- [Tool Calling](../concepts/tool-use.md)
- [Tool Design](../concepts/tool-design.md)
- [Chat Interfaces](../concepts/chat-interfaces.md)
- [Memory Systems](../concepts/memory-systems.md)
- [The Agent Loop (Reason-Act-Observe)](../concepts/agent-loop.md)
- [System Prompt Engineering](../concepts/system-prompt-engineering.md)
- [Agent Security](../concepts/agent-security.md)

## Entities

- [OpenAI](../entities/organizations/openai.md)
- [Asana](../entities/tools/asana.md)
- [Python](../entities/tools/python.md)
- [Cole Medin](../entities/people/cole-medin.md)

## Key moments

- **[0:00:00]** Thesis: developers must focus on AI agents, defined as an LLM able to interact with the outside world
- **[0:01:34]** Project setup: skeleton main function for a GPT chatbot that creates Asana tasks
- **[0:02:17]** Imports, environment variables (.env) for API keys, loading them with dotenv
- **[0:03:19]** Creating the OpenAI client and the Asana tasks API client
- **[0:03:52]** Message list and the three roles: system, user, assistant
- **[0:05:08]** Forever loop reading user input and building up chat history
- **[0:06:18]** The create_asana_task function with name and optional due date params
- **[0:07:43]** prompt_ai function: client.chat.completions.create with model, messages, tools
- **[0:08:39]** The tool schema: description (when to call) plus parameters (what to pass), including date format
- **[0:10:57]** Parsing the GPT response: choices[0].message and the tool_calls attribute
- **[0:11:41]** Mapping tool-call names to Python functions, invoking with **args, appending result to messages
- **[0:13:19]** Re-prompting the AI with the function result so it writes the final user reply
- **[0:14:53]** Live demo: normal question vs. a task request that triggers the tool call and returns a task link
- **[0:16:03]** The created task confirmed in Asana; teaser that the next episode makes it simpler and more powerful

## Transcript

[Raw transcript](../raw/developers-this-is-how-you-stay-relevant-with-ai-ai-agents-masterclass-1.md)
