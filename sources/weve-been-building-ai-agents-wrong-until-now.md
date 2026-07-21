---
type: source
title: "We've Been Building AI Agents WRONG Until Now"
description: "PydanticAI matters less as a specific framework than as a demonstration of the production-grade features (validation, dependency injection, retries, testing, logging) every agent framework must implement."
youtube_id: pC17ge_2n0Q
url: https://www.youtube.com/watch?v=pC17ge_2n0Q
slug: weve-been-building-ai-agents-wrong-until-now
published: 2024-12-08
duration: "0:19:53"
recency_rank: 135
raw: "../raw/weve-been-building-ai-agents-wrong-until-now.md"
tags: [pydantic-ai, production, validation, agents]
created: 2026-07-21
updated: 2026-07-21
---

# We've Been Building AI Agents WRONG Until Now

Cole argues that the first wave of agent frameworks ([LangChain](../entities/tools/langchain.md), CrewAI, Swarm, no-code builders) are not good enough for mature, [production-ready agents](../concepts/production-grade-agents.md) without significant extra work, and that [Pydantic AI](../entities/tools/pydantic-ai.md) is starting to change that. Built by the team behind Pydantic (Python's validation library that [OpenAI](../entities/organizations/openai.md), [Anthropic](../entities/organizations/anthropic.md), LangChain, and LlamaIndex already rely on), Pydantic AI puts validation at the core: LLM output validation, [structured and streamed responses](../concepts/structured-outputs.md), model-agnostic providers, type-safe dependency injection for context (DB connections, API keys), retry logic, testing with mock/test models, and [Logfire](../entities/tools/logfire.md) logging and [monitoring](../concepts/agent-observability.md).

The deeper point of the video is the "how," not the framework itself: any framework going forward must implement these often-overlooked features, and developers need to know how to leverage them to reach enterprise level. Cole walks the Pydantic AI docs (weather agent example, provider swapping, dependency injection) then builds a roughly 100-line web search agent from scratch using the [Brave Search API](../entities/tools/brave-search.md), an example of [agentic search](../concepts/agentic-search.md). He defines dependencies (HTTP client plus Brave key) so credentials never get passed through the LLM, a [guardrail](../concepts/guardrails.md) against leaking secrets, binds a search [tool](../concepts/tool-use.md) via a decorator whose docstring tells the model when and how to use it, and sets model retries.

He runs it locally with [Qwen 2.5 Coder 32B](../entities/tools/qwen.md) via [Ollama](../entities/tools/ollama.md) (overriding the OpenAI base URL to localhost:11434, a [local AI](../concepts/local-ai.md) setup), then shows a [Streamlit](../entities/tools/streamlit.md) version adding chat history and text streaming (noting Ollama did not stream well, so GPT-4o was used). The closing message: staying current is not about chasing the hottest monthly framework but understanding the direction of the industry and what genuinely makes agents production grade, which also depends on deliberate [model selection](../concepts/model-selection.md) and [evaluation](../concepts/agent-evaluation.md).

## Concepts covered

- [Production-Grade Agents](../concepts/production-grade-agents.md)
- [Structured Outputs](../concepts/structured-outputs.md)
- [Tool Calling](../concepts/tool-use.md)
- [Guardrails](../concepts/guardrails.md)
- [Agent Evaluation](../concepts/agent-evaluation.md)
- [Agent Observability](../concepts/agent-observability.md)
- [Model Selection](../concepts/model-selection.md)
- [Local & Self-Hosted AI](../concepts/local-ai.md)
- [Agentic Search](../concepts/agentic-search.md)
- [Streaming Responses](../concepts/streaming-responses.md)

## Entities

- [Pydantic AI](../entities/tools/pydantic-ai.md)
- [Ollama](../entities/tools/ollama.md)
- [Logfire](../entities/tools/logfire.md)
- [Streamlit](../entities/tools/streamlit.md)
- [OpenAI](../entities/organizations/openai.md)
- [Anthropic](../entities/organizations/anthropic.md)
- [Qwen 2.5 Coder 32B](../entities/tools/qwen.md)
- [Cole Medin](../entities/people/cole-medin.md)

## Key moments

- **[0:00:00]** Thesis: early frameworks (LangChain, CrewAI, Swarm, no-code) are not production-ready without heavy extra work
- **[0:01:38]** Pydantic explained as Python's validation library, already used by OpenAI/Anthropic/LangChain/LlamaIndex
- **[0:03:11]** Feature tour: model-agnostic, type-safe structured/streamed responses, dependency injection, Logfire
- **[0:05:55]** Weather agent doc example; docstring tells the LLM when/how to use a tool
- **[0:06:48]** Starts building a web search agent from scratch with the Brave Search API
- **[0:08:38]** Custom OpenAI-compatible client pointing at Ollama (localhost:11434) for local Qwen
- **[0:10:22]** Defining the agent, binding the search tool, setting model retry
- **[0:14:27]** Runs the ~100-line agent locally on Qwen; returns React 19 articles
- **[0:15:35]** Streamlit version adds chat history and text streaming (uses GPT-4o)
- **[0:19:09]** Closing: stay current to understand where the industry is heading and what makes agents production grade

## Transcript

[Raw transcript](../raw/weve-been-building-ai-agents-wrong-until-now.md)
