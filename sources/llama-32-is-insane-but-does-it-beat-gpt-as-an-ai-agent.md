---
type: source
title: "Llama 3.2 is INSANE - But Does it Beat GPT as an AI Agent?"
description: "Llama 3.2 90B is a real step forward for local LLMs as AI agents and can do function calling, but it still falls short of GPT-4o mini's reliability, especially on complex tool calls."
youtube_id: E3jO8YLc_CI
url: https://www.youtube.com/watch?v=E3jO8YLc_CI
slug: llama-32-is-insane-but-does-it-beat-gpt-as-an-ai-agent
published: 2024-09-29
duration: "0:16:31"
recency_rank: 159
raw: "../raw/llama-32-is-insane-but-does-it-beat-gpt-as-an-ai-agent.md"
tags: [local-llms, function-calling, benchmarks, llama]
created: 2026-07-21
updated: 2026-07-21
---

# Llama 3.2 is INSANE - But Does it Beat GPT as an AI Agent?

Cole tests Meta's newly released Llama 3.2 (specifically the 90B version, the one considered comparable to GPT-4o mini) to answer a single question: can a local, downloadable LLM finally act as a reliable AI agent? The bottleneck he cares about is function calling (tool calling), the ability for an LLM to actually do things like manage Asana tasks, search Google Drive, and query a RAG knowledge base, because local models have historically been bad at it. He walks through a custom LangChain + LangGraph agent whose graph has just two nodes (call the LLM, invoke tools) plus a router that loops until every requested tool call is done, and a model-mapping layer that lets you swap between OpenAI, Anthropic, and Groq models by changing a single environment variable.

He runs an escalating battery of prompts against GPT-4o mini first: list Asana projects (a no-argument tool call), create a task (requires parameters), search and download a Google Drive file (requires a precisely formatted API query), add the file to the knowledge base, and finally chain download-plus-index-plus-RAG-answer in one request. GPT-4o mini handles nearly all of it, chaining tools and reusing context from prior calls, only stumbling by redundantly downloading a file four times. Llama 3.2 90B then runs the identical prompts: it nails the Asana project listing, task creation, and RAG retrieval, but fails the Google Drive search, producing a malformed query with no search term and even asking the user for more information it shouldn't need.

The verdict: Llama 3.2 is genuinely usable for function calling and RAG (a big leap over Llama 3.1, where even the 70B was unusable and only the 405B worked), and the sub-90B versions (1B/3B/11B) simply won't invoke tools at all. But it does not yet match GPT-4o mini on harder tool calls. Cole notes you can close some of the gap with better tool docstrings and fine-tuning, and frames this as one entry in an ongoing series until an open-source model truly crushes agentic use.

## Concepts covered

- [Tool Calling](../concepts/tool-use.md)
- [Local LLMs as Agents](../concepts/local-llms-as-agents.md)
- [Model Selection](../concepts/model-selection.md)
- [Provider Independence](../concepts/provider-independence.md)
- [The Agent Loop (Reason-Act-Observe)](../concepts/agent-loop.md)
- [Retrieval-Augmented Generation (RAG)](../concepts/rag.md)
- [Tool Design](../concepts/tool-design.md)

## Entities

- [GPT-4o mini](../entities/tools/gpt-4o-mini.md)
- [LangChain](../entities/tools/langchain.md)
- [LangGraph](../entities/tools/langgraph.md)
- [Meta AI](../entities/organizations/meta.md)
- [OpenAI](../entities/organizations/openai.md)
- [Groq](../entities/organizations/groq.md)
- [Streamlit](../entities/tools/streamlit.md)
- [Chroma](../entities/tools/chroma.md)
- [Asana](../entities/tools/asana.md)
- [Google Drive](../entities/tools/google-drive.md)
- [Cole Medin](../entities/people/cole-medin.md)

## Key moments

- **[0:00:00]** Meta releases Llama 3.2 in 1B/3B/11B/90B sizes; 90B approaches GPT-4o mini
- **[0:00:37]** Framing: local LLMs have historically been bad AI agents because they can't do function calling well
- **[0:01:49]** Walkthrough of the custom LangChain + LangGraph agent code
- **[0:02:58]** Model-mapping layer swaps OpenAI/Anthropic/Groq via one env variable
- **[0:03:59]** The LangGraph structure: two nodes (LLM plus tools) and a router that loops
- **[0:05:08]** Tools overview: Asana, Google Drive, and local Chroma vector DB for RAG
- **[0:07:09]** GPT-4o mini test begins with escalating prompts
- **[0:10:48]** GPT-4o mini's one mistake: downloads the same file four times
- **[0:11:30]** Switch to Llama 3.2 90B; smaller Llama 3.2 models won't invoke tools at all
- **[0:13:03]** Llama 3.2 fails the Google Drive search with a malformed query
- **[0:14:40]** Llama 3.2 succeeds at RAG retrieval when given the file path directly
- **[0:15:11]** Verdict: Llama 3.2 is a step forward but doesn't reach GPT-4o mini

## Transcript

[Raw transcript](../raw/llama-32-is-insane-but-does-it-beat-gpt-as-an-ai-agent.md)
