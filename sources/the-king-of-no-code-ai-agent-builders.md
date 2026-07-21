---
type: source
title: "The KING of No Code AI Agent Builders?!"
description: "Voiceflow is a no-code AI agent platform that lets you build production-ready agents with fine-grained control by acting as the brain between a front end and back-end services, driving tools through intents and entities."
youtube_id: 0c05ijEmk2g
url: https://www.youtube.com/watch?v=0c05ijEmk2g
slug: the-king-of-no-code-ai-agent-builders
published: 2024-11-08
duration: "0:19:16"
recency_rank: 144
raw: "../raw/the-king-of-no-code-ai-agent-builders.md"
tags: [no-code, agents, voiceflow, intents-entities, production]
created: 2026-07-21
updated: 2026-07-21
---

[Cole Medin](../entities/people/cole-medin.md) walks through building a production-ready AI agent with [Voiceflow](../entities/tools/voiceflow.md), a no-code platform he pitches as the sweet spot between full custom coding and simpler no-code builders: it gives you control over the RAG pipeline, conversation flow, tool integrations, and even custom JavaScript while remaining code-free. He frames Voiceflow's mission as being "the brain between your front end and your back end." In his demo the front end is a React and HTML app and the back end is a single [n8n](../entities/tools/n8n.md) workflow that posts a message to [Slack](../entities/tools/slack.md), with Voiceflow orchestrating the conversation and deciding when to call the tool.

The core mechanics are intents and entities. An intent is the natural-language instruction (name, description, and example utterances) that tells the agent when to invoke a tool; an entity is a required input variable (like the Slack message text) that the agent must collect from the user before it ever calls the tool. Voiceflow's knowledge base is front-and-center for RAG, ingesting a URL, sitemap, file, or plain text, and workflows are built in a drag-and-drop canvas with logic nodes, API nodes, reusable components, variables, and custom functions. Cole builds an intent "send a Slack message," defines the entity, wires a workflow that POSTs to his n8n webhook with a bearer token, handles success and failure branches, and tests it in a debug run view that surfaces every intent, decision, and variable.

Finally he deploys the agent as an embeddable chat widget or API endpoint via the publish and integration tabs, and generates a simple front-end wrapper using [autodev](../entities/tools/autodev.md) (his bolt.new fork) driven by DeepSeek Coder v2 236B through [OpenRouter](../entities/tools/openrouter.md) for under a penny. The takeaway: you can build any agent integrating with any service without writing the agent itself, while keeping the control needed for production.

## Concepts covered

- [No-Code AI Agents](../concepts/no-code-agents.md)
- [Full-Stack AI Application](../concepts/full-stack-ai-application.md)
- [Intents and Entities](../concepts/intents-and-entities.md)
- [Tool Calling](../concepts/tool-use.md)
- [Clarifying Questions](../concepts/clarifying-questions.md)
- [Retrieval-Augmented Generation (RAG)](../concepts/rag.md)
- [Visual Workflow Builder](../concepts/visual-workflow-builder.md)
- [Reusable Components and Variables](../concepts/reusable-components.md)
- [Production-Grade Agents](../concepts/production-grade-agents.md)
- [Agent Deployment](../concepts/agent-deployment.md)
- [Chat Interfaces](../concepts/chat-interfaces.md)

## Entities

- [Voiceflow](../entities/tools/voiceflow.md)
- [n8n](../entities/tools/n8n.md)
- [Slack](../entities/tools/slack.md)
- [autodev (bolt.new fork)](../entities/tools/autodev.md)
- [OpenRouter](../entities/tools/openrouter.md)
- [Cole Medin](../entities/people/cole-medin.md)

## Key moments

- **[0:00:16]** The problem: no-code platforms rarely give the control needed for production agents
- **[0:01:45]** Voiceflow's mission, the brain between your front end and back end
- **[0:03:49]** Create the first agent and import a web page to seed the knowledge base
- **[0:04:55]** Knowledge base ingestion options: URLs, sitemap, file upload, plain text, Zendesk
- **[0:07:51]** Intents and entities, where tools for the agent are defined
- **[0:08:39]** Creating the "send a slack message" intent with description and utterances
- **[0:09:40]** Adding a required entity (input variable) the agent must collect before calling the tool
- **[0:11:55]** Building the workflow that defines the tool: POST to the n8n webhook API
- **[0:15:30]** Testing in the debug run view showing intents, decisions, and variables
- **[0:16:38]** Deploying as an embeddable chat widget or API endpoint via publish/integration tabs
- **[0:17:15]** Generating a front-end wrapper with autodev + DeepSeek Coder v2 via OpenRouter

## Transcript

[Raw transcript](../raw/the-king-of-no-code-ai-agent-builders.md)
