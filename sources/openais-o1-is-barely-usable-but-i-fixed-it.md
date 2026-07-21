---
type: source
title: "OpenAI's o1 is Barely Usable, but I Fixed it..."
description: "OpenAI's o1 launched without native function calling, so Cole hand-codes a custom tool-calling layer in LangChain that turns o1 (or any LLM) into a capable, self-correcting AI agent."
youtube_id: IsxXO3EbIqc
url: https://www.youtube.com/watch?v=IsxXO3EbIqc
slug: openais-o1-is-barely-usable-but-i-fixed-it
published: 2024-09-18
duration: "0:24:47"
recency_rank: 164
raw: "../raw/openais-o1-is-barely-usable-but-i-fixed-it.md"
tags: [tool-calling, ai-agents, langchain, reasoning-models]
created: 2026-07-21
updated: 2026-07-21
---

# OpenAI's o1 is Barely Usable, but I Fixed it...

The video addresses a gap in OpenAI's o1 beta preview: it ships without tool messages, function calling, or system messages, which makes it unusable for AI agents that need to interact with APIs and the outside world. Rather than wait for OpenAI to add native tool calling, Cole builds a custom function-calling layer from scratch in Python using LangChain, Streamlit for the UI, and Asana as the example toolset, and stresses that the same setup works with any LLM that lacks function calling.

The implementation packages each tool's docstring (description, example call, arguments, return) into a tool-description list injected into the prompt, then constrains the model to emit a strict JSON object (a list of tool calls plus a content string) enforced by a LangChain JSON output parser. A recursive prompt loop invokes requested tools, and after each invocation feeds the result back to the model as a "thought," internal dialogue that can be optionally surfaced in the UI. Failures are also returned as thoughts with the exception message so the model can self-correct, and a duplicate-call guard detects when the model re-requests an already-executed tool to prevent infinite loops.

Cole then demos the agent managing Asana tasks: creating a task in a coding project (where o1 first hallucinates a project name, catches the error, calls get-projects to fetch the real ID, and fixes the due date), deleting it, and batch-creating three tasks. The agent is not flawless (it misses a due date on the batch job) but the reasoning-plus-self-correction loop works impressively well, showing o1's reasoning strength paired with a homemade tool-calling harness.

## Concepts covered

- [Tool Calling](../concepts/tool-use.md)
- [Provider Independence](../concepts/provider-independence.md)
- [Structured Outputs](../concepts/structured-outputs.md)
- [Tool Design](../concepts/tool-design.md)
- [Self-Correcting Agents](../concepts/self-correction.md)
- [Agent Prompting Techniques](../concepts/agent-prompting.md)
- [The Agent Loop (Reason-Act-Observe)](../concepts/agent-loop.md)
- [Effective Prompting](../concepts/effective-prompting.md)

## Entities

- [LangChain](../entities/tools/langchain.md)
- [Streamlit](../entities/tools/streamlit.md)
- [Asana](../entities/tools/asana.md)
- [OpenAI](../entities/organizations/openai.md)
- [Cole Medin](../entities/people/cole-medin.md)

## Key moments

- **[0:00:33]** o1 beta preview is missing tool messages and function calling, blocking most agent use cases
- **[0:01:07]** Cole announces he custom-coded function calling for o1, usable with any LLM
- **[0:03:27]** Stack reveal: Asana tools, Streamlit UI, LangChain
- **[0:06:05]** Tool descriptions built from each function's docstring (description, example, args, return)
- **[0:07:07]** Defining the strict response format: a list of tool calls plus a content string, enforced by a JSON output parser
- **[0:09:26]** The "thought" pattern: internal AI dialogue that gives the model context and can be optionally shown
- **[0:13:13]** On tool failure, the exception is added as a thought and Prompt AI recurses so the model self-corrects
- **[0:14:24]** Duplicate tool-call detection prevents infinite loops when the model re-requests an executed tool
- **[0:16:57]** o1 has no system message, so the opening human message stands in as the system prompt
- **[0:19:07]** Live demo: o1 hallucinates a project name, catches the error, fetches the real project ID, and corrects the due date

## Transcript

[Raw transcript](../raw/openais-o1-is-barely-usable-but-i-fixed-it.md)
