---
type: concept
title: "Docstrings as Tool Descriptions"
description: "Writing clear function docstrings that double as the tool descriptions an agent reads, so the LLM knows exactly when and how to call each tool."
tags: [prompting, tools, docstrings, ai-agents, tool-calling]
videos: [i-finally-built-an-ai-agent-to-organize-my-life-ai-agents-masterclass-4]
created: 2026-07-21
updated: 2026-07-21
---

# Docstrings as Tool Descriptions

When you give an agent a tool, the function's docstring is not documentation for humans, it is the prompt the model reads to decide whether and how to call that function. "we have a doc string just like we have with our create a task function which tells the AI agent how to use this function when to use it and what kind of parameters to give" ([0:07:06]). In agent frameworks the docstring is extracted verbatim into the tool schema, so it sits directly in the model's context alongside the parameter signatures.

## Why it matters

Cole is emphatic that this is the highest-leverage part of an agent's prompt: "this honestly is the most important part of the prompt to the AI is these dock strings because if it doesn't know how to use these tools well it's going to use them when it shouldn't and it won't use them when it should" ([0:11:12]). Two failure modes fall out of a weak docstring: the agent over-calls a tool in situations it does not fit, or it fails to call a tool that would have solved the task. Both are prompting problems disguised as capability problems.

A good docstring earns its keep by making vague parameters legible. Even a generically named argument works when the docstring explains its shape: "data is a very generic variable um but we can tell it in the doc string exactly how to format this data dictionary and even with something kind of vague like this... the agent still does really well" ([0:09:00]). The practical guidance is to state, for each tool, what it does, precisely when to use it (and when not to), and the exact format each parameter expects. This makes docstrings a form of [tool design](./tool-design.md) and a concrete slice of [context engineering](./context-engineering.md): the words in the docstring are the context the agent uses to act.

## Part of

- [Context Engineering](./context-engineering.md)

## Related

- [Tool Use](./tool-use.md)
- [Tool Design](./tool-design.md)
- [Agent Prompting Techniques](./agent-prompting.md)
- [Structured Outputs](./structured-outputs.md)

## Tools

- [Pydantic AI](../entities/tools/pydantic-ai.md)
- [Python](../entities/tools/python.md)
- [FastMCP](../entities/tools/fastmcp.md) - Anthropic's high-level Python interface in the MCP SDK for spinning up an MCP server in one line (name, description, lifespan, host, port) and registering tools with the @mcp.tool decorator.

## Sources

- [I FINALLY Built an AI Agent to Organize my Life - AI Agents Masterclass #4](../sources/i-finally-built-an-ai-agent-to-organize-my-life-ai-agents-masterclass-4.md) - "[0:11:12] this honestly is the most important part of the prompt to the AI is these dock strings because if it doesn't know how to use these tools well it's going to use them when it shouldn't and it won't use them when it should"
