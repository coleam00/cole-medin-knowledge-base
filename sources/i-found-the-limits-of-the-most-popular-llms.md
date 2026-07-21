---
type: source
title: "I Found the Limits of the Most Popular LLMs"
description: "By escalating the complexity of requests to an AI agent wired to RAG, Google Drive, and Asana until each model breaks, you can empirically find which LLM is actually best for agentic workflows, and in 2024 that winner is Claude 3.5 Sonnet."
youtube_id: uIWNzcqHQ58
url: https://www.youtube.com/watch?v=uIWNzcqHQ58
slug: i-found-the-limits-of-the-most-popular-llms
published: 2024-08-28
duration: "0:32:41"
recency_rank: 170
raw: "../raw/i-found-the-limits-of-the-most-popular-llms.md"
tags: [model-selection, agent-evaluation, llms, tool-calling]
created: 2026-07-21
updated: 2026-07-21
---

# I Found the Limits of the Most Popular LLMs

Cole builds an AI agent (Streamlit UI plus LangGraph runnable) that has three tool groups bound to it, a vector-database knowledge base (RAG), Google Drive CRUD, and Asana task management, and swaps the underlying LLM via a single environment variable so the same agent can be driven by GPT-4o mini, Claude 3.5 Sonnet, a Groq fine-tuned Llama 3, or GPT-4o. The agent loops through a call-model, call-tools, route cycle until the model decides it is done, so any request can trigger an arbitrary chain of tool calls.

He then runs an informal evaluation-by-escalation: starting with trivial one-tool requests and building up to a hard multi-step request ("take my Aug 24 meeting notes from Drive, put them in your knowledge base, then mark every task in a project as complete that the notes say is done") that forces the agent to coordinate all three systems. GPT-4o mini handles a lot but breaks on the final multi-step request by passing bad arguments to the complete-task tool; the Groq Llama 3 fine-tune breaks almost immediately (wrong due date, wrong Drive search format, wrong file ID); GPT-4o gets about 90% of the hard request but silently misses one task; Claude 3.5 Sonnet is the only model he cannot break.

Along the way Cole teaches a validation design pattern (the agent has no tool to read Drive file contents directly, it can only download and then add to the knowledge base, so any answer is provably sourced from RAG) and floats the idea of turning the whole "break the LLM" process into an automated agentic test suite and scoring framework for new models.

## Concepts covered

- [Model Selection](../concepts/model-selection.md)
- [Agent Evaluation](../concepts/agent-evaluation.md)
- [Agentic Workflow Engineering](../concepts/agentic-workflow-engineering.md)
- [Tool Calling](../concepts/tool-use.md)
- [Retrieval-Augmented Generation (RAG)](../concepts/rag.md)
- [Validation](../concepts/validation.md)
- [The Agent Loop (Reason-Act-Observe)](../concepts/agent-loop.md)
- [Prompt Engineering](../concepts/prompt-engineering.md)

## Entities

- [Cole Medin](../entities/people/cole-medin.md)
- [Anthropic](../entities/organizations/anthropic.md)
- [OpenAI](../entities/organizations/openai.md)
- [Groq](../entities/organizations/groq.md)
- [Llama](../entities/tools/llama.md)
- [LangGraph](../entities/tools/langgraph.md)
- [LangChain](../entities/tools/langchain.md)
- [Streamlit](../entities/tools/streamlit.md)
- [Asana](../entities/tools/asana.md)
- [Google Drive](../entities/tools/google-drive.md)

## Key moments

- **[0:00:00]** Intro: an agent with RAG plus Google Drive plus Asana, goal is to push each LLM until it breaks
- **[0:00:30]** Models under test: GPT models, Claude 3.5 Sonnet, and a Groq fine-tuned Llama 3 for function calling
- **[0:01:29]** Code walkthrough of the agent begins (Streamlit plus LangGraph plus tool files)
- **[0:02:06]** Names the folder "llm agent evaluation framework"; idea to automate breaking LLMs into a scored test suite
- **[0:03:19]** Single LM_MODEL env var selects the chat client (OpenAI / Groq / Anthropic) intelligently
- **[0:06:32]** LangGraph cycle explained: call-model node, tool node, router / should-continue
- **[0:08:44]** Validation design: no tool to read Drive contents directly, must download then add to knowledge base so answers are provably from RAG
- **[0:16:12]** Building up GPT-4o mini through progressively harder combined RAG plus Asana plus Drive requests
- **[0:17:37]** GPT-4o mini breaks on the final multi-step request (bad arguments to mark-complete)
- **[0:21:16]** Claude 3.5 Sonnet passes the exact request that broke GPT-4o mini
- **[0:23:59]** Groq Llama 3 fine-tune breaks fast: wrong due date, wrong search format, recursion limit, wrong file ID
- **[0:30:29]** GPT-4o gets about 90% but silently misses marking one task complete
- **[0:31:32]** Verdict: Claude 3.5 Sonnet is the clear winner for agentic workflows

## Transcript

[Raw transcript](../raw/i-found-the-limits-of-the-most-popular-llms.md)
