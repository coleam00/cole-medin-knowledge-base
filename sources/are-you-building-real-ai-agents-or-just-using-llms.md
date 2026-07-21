---
type: source
title: "Are You Building REAL AI Agents or Just Using LLMs?"
description: "A real AI agent is a non-deterministic program where the LLM decides what tools to invoke and how many times to interact with its environment to reach a goal, which is fundamentally different from a workflow that merely chains LLM calls in a fixed sequence."
youtube_id: GYFTQU2iV4A
url: https://www.youtube.com/watch?v=GYFTQU2iV4A
slug: are-you-building-real-ai-agents-or-just-using-llms
published: 2025-02-23
duration: "0:18:29"
recency_rank: 115
raw: "../raw/are-you-building-real-ai-agents-or-just-using-llms.md"
tags: [agents-vs-workflows, agent-definition, tool-use, n8n]
created: 2026-07-21
updated: 2026-07-21
---

# Are You Building REAL AI Agents or Just Using LLMs?

Cole tackles the widespread habit of calling any LLM-containing program an "AI agent," arguing the distinction matters because agents and workflows solve different problems and are built differently. Drawing on definitions from Hugging Face ("programs where LLM outputs control the workflow") and Anthropic (agents let the LLM decide how many times to run and loop until resolution), he distills two criteria that together define an agent. It must be non-deterministic, meaning the LLM decides what runs, when, and how many times, and it must interact with an environment through tools to achieve a goal. An agent is given tools, goals and preferences via its system prompt, and prior knowledge via short-term (conversation history) or long-term (RAG) memory, then runs an observe-act loop.

He grounds this with contrasting n8n examples. A workflow that crafts a post for X, LinkedIn, and a blog and then summarizes is a valuable "not agent" because it is purely sequential, step A then B then C, with no LLM-controlled branching. A tech-stack-expert chatbot is non-deterministic (an unknown number of conversational turns) but still not an agent because its dangling tools node means it never actually interacts with the environment. Both criteria are required: sequential-but-tool-using fails, and non-deterministic-but-toolless fails.

The true-agent examples satisfy both criteria at once: an n8n note-taking agent that decides when to save or fetch long-term memories in Google Docs, and Cole's GitHub agent that autonomously chooses which repo files and READMEs to analyze. He closes by contrasting ChatGPT, essentially a chatbot even with web search because it cannot decide to re-search, against Windsurf, a highly agentic coding tool that independently decides which files to analyze and edit. Both agents and workflows are valuable, but Cole sees the larger future in agents.

## Concepts covered

- [Agents vs. Workflows](../concepts/agents-vs-workflows.md)
- [Deterministic Workflows](../concepts/deterministic-workflows.md)
- [Tool Calling](../concepts/tool-use.md)
- [The Agent Loop (Reason-Act-Observe)](../concepts/agent-loop.md)
- [Memory Systems](../concepts/memory-systems.md)
- [Retrieval-Augmented Generation (RAG)](../concepts/rag.md)
- [Agentic Coding](../concepts/agentic-coding.md)

## Entities

- [n8n](../entities/tools/n8n.md)
- [Anthropic](../entities/organizations/anthropic.md)
- [Hugging Face](../entities/organizations/hugging-face.md)
- [Archon](../entities/tools/archon.md)
- [Windsurf](../entities/tools/windsurf.md)
- [ChatGPT](../entities/tools/chatgpt.md)
- [Pydantic AI](../entities/tools/pydantic-ai.md)
- [GitHub](../entities/tools/github.md)
- [Cole Medin](../entities/people/cole-medin.md)

## Key moments

- **[0:00:00]** Opening: everyone calls any LLM program an agent, but there's a big difference between agents and workflows
- **[0:01:27]** Hugging Face definition: AI agents are programs where LLM outputs control the workflow (key word: non-deterministic)
- **[0:02:34]** Anthropic clip: agents let the LLM decide how many times to loop until it finds a resolution
- **[0:04:20]** Diagram of an agent: tools, goals via system prompt, short/long-term memory, and the observe-act loop
- **[0:06:30]** Not-agent example #1: sequential X/LinkedIn/blog posting workflow (no non-determinism)
- **[0:10:58]** Not-agent example #2: tech-stack chatbot is non-deterministic but has a dangling tools node (no environment)
- **[0:12:45]** True agent #1: n8n note-taking agent saves/fetches long-term memory in Google Docs
- **[0:14:54]** True agent #2: Cole's GitHub agent autonomously analyzes repo structure and individual READMEs
- **[0:16:24]** ChatGPT (not agent) vs Windsurf (highly agentic coding tool making many autonomous decisions)

## Transcript

[Raw transcript](../raw/are-you-building-real-ai-agents-or-just-using-llms.md)
