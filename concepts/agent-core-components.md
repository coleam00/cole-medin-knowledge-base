---
type: concept
title: "The Core Components of an Agent"
description: "Every AI agent reduces to four parts: the LLM (brain), tools (actions), the system prompt (instructions), and memory (context)."
tags: [llm, tools, system-prompt, memory]
videos: [learn-90-of-building-ai-agents-in-30-minutes, google-anthropic-and-openais-guides-to-ai-agents-all-in-18-minutes]
created: 2026-07-21
updated: 2026-07-21
---

# The Core Components of an Agent

Every AI agent, no matter how sophisticated, decomposes into the same four parts. As Cole puts it, "we have the four components that go into any AI agent. And that is our large language model... We have the tools... We have the instructions, usually known as the system prompt... And then last we have our memory." [0:05:04] Master these four and you can build roughly 90% of any agent; the remaining complexity (deployment, evaluation, scale) is deferred until you actually hit its limits.

The **LLM** is the brain (see [Model Selection](./model-selection.md)): the reasoning engine, GPT, Gemini, or Claude, that decides what to do next. **Tools** are the agent's hands (see [Tool Design](./tool-design.md)): the functions it can call to act on the world, from querying a database to sending an email. The **system prompt** is the instructions (see [System Prompt Engineering](./system-prompt-engineering.md)): the standing guidance that shapes the agent's behavior, persona, and constraints. **Memory** is the context (see [Memory Systems](./memory-systems.md)): the conversation history and retrieved knowledge that lets the agent stay coherent across turns.

The framing is not just tidy taxonomy, it is a debugging discipline. "Whenever you have an issue with your agent in general, it's always going to be one of these four things." [0:06:06] A hallucinating agent points at the model or system prompt; a stuck agent points at a broken tool; a forgetful agent points at memory. Reducing every failure to one of four buckets keeps beginners from over-engineering: "what I'm focusing on here is just defining our four core components. LLM, tools, memory, and a system prompt." [0:05:09]

## Part of

- [The Agent Loop (Reason-Act-Observe)](./agent-loop.md) - the loop is what animates these four components at runtime.
- [What Is an AI Agent?](./what-is-an-ai-agent.md) - the definition these components fill in.

## Related

- [Memory Systems](./memory-systems.md) - the fourth component, expanded.
- [Tool Design](./tool-design.md) - how to build the actions the agent calls.
- [Model Selection](./model-selection.md) - choosing the brain.
- [System Prompt Engineering](./system-prompt-engineering.md) - writing the instructions.

## Tools

- [Pydantic AI](../entities/tools/pydantic-ai.md) - a framework that exposes exactly these four components as first-class primitives.
- [n8n](../entities/tools/n8n.md) - a no-code agent node built around the same LLM/tools/memory/prompt structure.

## Sources

- [Learn 90% of Building AI Agents in 30 Minutes](../sources/learn-90-of-building-ai-agents-in-30-minutes.md) - "[0:01:44] the first thing I want to cover with you is the four core components of any AI agent"
- [Google, Anthropic, and OpenAI's Guides to AI Agents ALL in 18 Minutes](../sources/google-anthropic-and-openais-guides-to-ai-agents-all-in-18-minutes.md) - "[0:06:06] whenever you have an issue with your agent in general, it's always going to be one of these four things."
