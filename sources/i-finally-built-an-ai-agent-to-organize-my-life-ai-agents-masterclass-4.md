---
type: source
title: "I FINALLY Built an AI Agent to Organize my Life - AI Agents Masterclass #4"
description: "By giving an LLM a set of well-documented Python functions as tools, you can build a conversational agent that fully manages your Asana workspace (projects and tasks) from natural language."
youtube_id: s3SY_2a3Woo
url: https://www.youtube.com/watch?v=s3SY_2a3Woo
slug: i-finally-built-an-ai-agent-to-organize-my-life-ai-agents-masterclass-4
published: 2024-07-14
duration: "0:13:20"
recency_rank: 183
raw: "../raw/i-finally-built-an-ai-agent-to-organize-my-life-ai-agents-masterclass-4.md"
tags: [tool-use, docstrings-as-tool-descriptions, agent-prompting, agentic-workflow-engineering]
created: 2026-07-21
updated: 2026-07-21
---

# I FINALLY Built an AI Agent to Organize my Life - AI Agents Masterclass #4

This masterclass installment turns the simple task-creating chatbot from the prior video into a full task-management AI agent wired into Asana. Cole demos the finished product first: the agent researches a topic, then from a single natural-language prompt creates a new Asana project, generates a task per item, and assigns due dates by reasoning about the current date. It can also mark tasks complete, delete tasks, and update due dates from conversational, non-explicit requests, returning links to everything it touches.

The build walks through adding new tools alongside the existing create-task function: get projects, create project, get tasks, update task, and delete task. Each is a plain Python function that calls the Asana SDK and returns either the response or an error message as a string. The critical piece is each function's docstring, which tells the agent when to use the tool, what parameters to pass (including how to shape a generic "data" dictionary), and exactly what the response will contain. Cole stresses that these docstrings are the most important part of the prompt, because a poorly described tool gets used at the wrong times or ignored when needed.

Adding tools is nearly free: functions are registered in an available-functions mapping that is dynamically fetched and bound into the chatbot, so no other code changes. A final tweak to the system prompt instructs the agent never to surface internal IDs to the user. The video closes teasing the next installment on RAG, where a recorded meeting will be transcribed via Google Drive and its action items turned into Asana tasks.

## Concepts covered

- [Tool Calling](../concepts/tool-use.md)
- [Docstrings as Tool Descriptions](../concepts/docstrings-as-tool-descriptions.md)
- [Agentic Workflow Engineering](../concepts/agentic-workflow-engineering.md)
- [Agent Prompting Techniques](../concepts/agent-prompting.md)
- [System Prompt Engineering](../concepts/system-prompt-engineering.md)
- [MCP Server & Client Architecture](../concepts/mcp-architecture.md)
- [Retrieval-Augmented Generation (RAG)](../concepts/rag.md)

## Entities

- [Asana](../entities/tools/asana.md)
- [Streamlit](../entities/tools/streamlit.md)
- [OpenAI](../entities/organizations/openai.md)
- [Anthropic](../entities/organizations/anthropic.md)
- [GitHub](../entities/tools/github.md)
- [Cole Medin](../entities/people/cole-medin.md)

## Key moments

- **[0:00:42]** Overview of everything the Asana chatbot can do: create/search projects, create/delete/update/complete tasks
- **[0:01:22]** Demo: research a list, then one prompt creates a project and a task per item with computed due dates
- **[0:02:50]** Marking a task complete from implicit natural language ("I have learned python now")
- **[0:05:08]** Code walkthrough begins; workspace ID replaces single project ID
- **[0:06:32]** Building the new tools: get projects, create project, get tasks, update task, delete task
- **[0:10:42]** Registering all tools in the available-functions mapping; dynamically bound to the chatbot
- **[0:11:12]** Docstrings are the most important part of the prompt for correct tool use
- **[0:11:25]** System prompt tweak: never expose internal IDs to the user
- **[0:12:31]** Teaser for the next video on RAG: meeting recording to Google Drive transcript to Asana action items

## Transcript

[Raw transcript](../raw/i-finally-built-an-ai-agent-to-organize-my-life-ai-agents-masterclass-4.md)
