---
type: concept
title: "Embedding a Coding Agent in Your Application"
description: "Using a coding agent's SDK to programmatically define and embed the same agent harness inside your own apps and workflows, including non-coding work like note-taking, research, and knowledge management."
tags: [sdk, custom-agents, python]
videos: [claude-codes-real-purpose-its-bigger-than-you-think]
created: 2026-07-21
updated: 2026-07-21
---

# Embedding a Coding Agent in Your Application

Embedding a coding agent means treating a tool like Claude Code not as a terminal you sit in front of, but as a library you call from your own code. "In just a few lines of Python code, we can create our own custom instance of cloud code. We can set our own MCP servers and permission and system prompt and then we can query it." [0:04:08] The harness stops being an application you use and becomes a component you compose with, configured per invocation and dropped anywhere a function call fits.

## Why it matters

The reframing Cole pushes is that the terminal UI was never the product. "We take this lightweight wrapper like Claude code and we use it to programmatically define our own custom agents to build them into our code bases, our workflows to really suit our needs the best." [0:21:04] What you are buying is the harness: an [Agent Loop](./agent-loop.md) with file-system tools, search, subagents, and permissions already solved and hardened. Rebuilding that from raw model calls is months of work that the SDK hands over for free.

The corollary is that the agent's usefulness is not limited to writing code. The same file-editing, searching, planning loop is exactly what note-taking, research, and knowledge management need, which is why it generalizes into a [Second Brain](./second-brain.md) or a [Coding Agent as General Assistant](./coding-agent-as-general-assistant.md). Swap the system prompt and the tool surface and the identical harness becomes a domain agent.

## How it works

Instantiation is configuration, not construction. You pass a system prompt, an allowed-tool list and permission mode, the MCP servers the agent may reach, and a working directory, then query it and stream results back into your application. Because permissions are set per instance, an embedded agent can be locked down far tighter than an interactive session, which is what makes unattended runs inside a product plausible rather than reckless.

## Prerequisites

- [AI Coding Harness](./ai-coding-harness.md) - what you are actually embedding.
- [Agent Core Components](./agent-core-components.md) - system prompt, tools, and loop, now set through code.

## Part of

- [Agents That Build Agents](./agents-that-build-agents.md) - programmatic instantiation is the enabling step.
- [Meta-Harness](./meta-harness.md) - harnesses that spawn and orchestrate other harnesses.

## Contrasts with

- [SDK vs. Framework Decision](./sdk-vs-framework-decision.md) - the alternative is assembling the loop yourself from an agent framework instead of inheriting a finished one.
- [Production vs. Personal Agents](./production-vs-personal-agents.md) - a general-purpose coding harness embedded in a product carries different cost and risk than a purpose-built agent.

## Related

- [Coding Agent as General Assistant](./coding-agent-as-general-assistant.md) - the non-coding use cases this unlocks.
- [Agent as an API Endpoint](./agent-as-api-endpoint.md) - the natural next step once the agent is a library call.
- [Permission Management](./permission-management.md) - permission mode is an instantiation argument here.
- [MCP with Custom Agents](./mcp-with-custom-agents.md) - the tool surface you attach per instance.
- [Second Brain](./second-brain.md) and [Memory Systems](./memory-systems.md) - the knowledge-work application Cole builds on this foundation.

## Tools

- [Claude Agent SDK](../entities/tools/claude-agent-sdk.md) - the library that exposes the harness programmatically.
- [Claude Code](../entities/tools/claude-code.md) - the harness being embedded.
- [MCP (Model Context Protocol)](../entities/tools/mcp.md) - servers configured per embedded instance.
- [Python](../entities/tools/python.md) - a few lines is all the wiring takes.

## Sources

- [Claude Code's Real Purpose (It's Bigger Than You Think)](../sources/claude-codes-real-purpose-its-bigger-than-you-think.md) - "[0:04:08] In just a few lines of Python code, we can create our own custom instance of cloud code. We can set our own MCP servers and permission and system prompt and then we can query it."
- [Claude Code's Real Purpose (It's Bigger Than You Think)](../sources/claude-codes-real-purpose-its-bigger-than-you-think.md) - "[0:21:04] We take this lightweight wrapper like Claude code and we use it to programmatically define our own custom agents to build them into our code bases, our workflows to really suit our needs the best."
