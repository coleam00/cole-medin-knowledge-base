---
type: source
title: "OpenAI's BRAND NEW Agents SDK (Crash Course)"
description: "OpenAI's new Agents SDK makes it remarkably simple to build multi-agent systems with tools, handoffs, guardrails, and tracing, but its higher-level abstraction sacrifices the control, human-in-the-loop, and testing maturity that Pydantic AI and LangGraph still offer."
youtube_id: e7qvd2bOITc
url: https://www.youtube.com/watch?v=e7qvd2bOITc
slug: openais-brand-new-agents-sdk-crash-course
published: 2025-03-16
duration: "0:31:19"
recency_rank: 109
raw: "../raw/openais-brand-new-agents-sdk-crash-course.md"
tags: [openai-agents-sdk, agent-teams, guardrails, tracing, abstraction-distraction]
created: 2026-07-21
updated: 2026-07-21
---

Cole walks through OpenAI's newly released Agents SDK (the production-grade successor to its experimental Swarm framework) by building a travel-planner assistant in six incremental versions. He introduces the SDK's four core concepts: agents (instructions plus tools plus model), handoffs (specialized agents delegating to each other), guardrails (safety checks that can halt execution), and tracing (observability into agent runs), and shows how few lines of code each requires. Along the way he demonstrates structured outputs for consistent JSON responses, function tools defined via a decorator and docstring, agent handoffs to dedicated flight and hotel specialists (a mixture-of-experts pattern), an input guardrail that runs a budget-analysis agent in parallel to reject unrealistic trips, and user-context injection that lets tools access metadata (preferred airlines, amenities) without polluting the prompt.

The build closes with tracing via Pydantic Logfire (favored over OpenAI's own dashboard, especially when using non-OpenAI models) and a Streamlit UI that renders the structured output into a polished component. Cole also notes the SDK is provider-flexible: any OpenAI-compatible endpoint like OpenRouter or Ollama works via custom clients.

In his honest verdict, Cole praises how easy and fun the SDK is but places it near the CrewAI/LangChain end of the abstraction spectrum, what he calls "abstraction distraction," where the framework does so much for you that you lose control and understanding. He prefers the low-level abstraction of Pydantic AI and LangGraph, citing the SDK's gaps: no obvious way to run custom logic around handoffs, missing human-in-the-loop approval, and no testing or mocking story. He concludes the SDK is brand new and worth watching closely, but he will keep using Pydantic AI and LangGraph for full production apps.

## Concepts covered

- [Agent Teams](../concepts/agent-teams.md)
- [Structured Outputs](../concepts/structured-outputs.md)
- [Tool Calling](../concepts/tool-use.md)
- [Guardrails](../concepts/guardrails.md)
- [Agent Observability](../concepts/agent-observability.md)
- [Memory Systems](../concepts/memory-systems.md)
- [Human in the Loop](../concepts/human-in-the-loop.md)
- [Abstraction Distraction](../concepts/abstraction-distraction.md)
- [Provider Independence](../concepts/provider-independence.md)
- [Validation](../concepts/validation.md)

## Entities

- [OpenAI Agents SDK](../entities/tools/openai-agents-sdk.md)
- [OpenAI](../entities/organizations/openai.md)
- [OpenAI Swarm](../entities/tools/openai-swarm.md)
- [Pydantic AI](../entities/tools/pydantic-ai.md)
- [LangGraph](../entities/tools/langgraph.md)
- [LangChain](../entities/tools/langchain.md)
- [CrewAI](../entities/tools/crewai.md)
- [MCP (Model Context Protocol)](../entities/tools/mcp.md)
- [OpenRouter](../entities/tools/openrouter.md)
- [Ollama](../entities/tools/ollama.md)
- [Streamlit](../entities/tools/streamlit.md)
- [Anthropic](../entities/organizations/anthropic.md)
- [Cole Medin](../entities/people/cole-medin.md)

## Key moments

- **[0:00:15]** Agents SDK is the production-ready successor to OpenAI's experimental Swarm
- **[0:01:33]** Four core concepts: agents, handoffs, guardrails, tracing
- **[0:03:07]** Building a travel-planner assistant in six versions, starting bare-bones
- **[0:07:15]** Version 2, structured outputs force consistent JSON responses
- **[0:11:39]** Version 3, adding a weather tool via @function_tool decorator + docstring
- **[0:14:32]** Version 4, agent handoffs to specialized flight and hotel agents
- **[0:19:27]** Version 5, guardrails, user context, and tracing
- **[0:24:56]** Tracing via Pydantic Logfire, recommended over OpenAI's dashboard
- **[0:27:21]** Verdict: easy and fun but too high-abstraction; prefers Pydantic AI and LangGraph

## Transcript

[Raw transcript](../raw/openais-brand-new-agents-sdk-crash-course.md)
