---
type: source
title: "Pydantic AI 2.0: The New Best Way to Build AI Agents is Composing Capabilities"
description: "Pydantic AI 2.0 reframes agent-building around a single composable primitive, the capability, which bundles instructions, tools, hooks, guardrails, and model settings into reusable units that snap together like Lego blocks."
youtube_id: PY7xIxybYNc
url: https://www.youtube.com/watch?v=PY7xIxybYNc
slug: pydantic-ai-20-the-new-best-way-to-build-ai-agents-is-composing-capabilities
published: 2026-07-10
duration: "0:15:02"
recency_rank: 3
raw: "../raw/pydantic-ai-20-the-new-best-way-to-build-ai-agents-is-composing-capabilities.md"
tags: [pydantic-ai, capabilities, agent-frameworks]
created: 2026-07-21
updated: 2026-07-21
---

Cole reviews Pydantic AI's 2.0 release, which centers the entire framework on one primitive called the capability. A capability packages an agent's instructions, tools, lifecycle hooks, guardrails, and model settings into a single composable unit, so an agent becomes simply a set of these units combined together. Because they're composable, capabilities can be reused across multiple agents in a business (e.g. a shared knowledge-base capability feeding both a support agent and an FAQ widget), and improvements to one capability propagate to every agent that uses it. Cole frames capabilities as the layer above MCP servers: MCP bundles tools, but a capability bundles tools plus instructions, settings, hooks, and guardrails.

A key feature is progressive disclosure: each capability exposes a brief description so the agent keeps a lightweight catalog, and only loads a capability's full instructions and tools when the current prompt actually needs it. This lets you supply dozens or hundreds of capabilities without overwhelming the LLM or wasting tokens. Cole demonstrates with a CLI agent that answers a knowledge-base question using only thinking + knowledge-base capabilities (skipping escalation), then escalates a duplicate-charge refund request by loading the escalation capability on demand.

Cole also covers the framework's new two-layer architecture: a lean core of critical capabilities (thinking, web search, tool search) imported directly from Pydantic AI, and a harness layer of supported-but-non-critical capabilities like code mode (writing and executing code in a sandbox, powered by Pydantic's own open-source Monty sandbox). He argues you should no longer hand-write Pydantic AI code, instead pointing your coding agent at the capabilities docs, and that while coding-agent SDKs (Claude Agent SDK, Codex SDK) are great for personal agents, you still need a real framework like Pydantic AI to ship production agents used by other people.

## Concepts covered

- [Capabilities Over Tools](../concepts/capabilities-over-tools.md)
- [Progressive Disclosure](../concepts/progressive-disclosure.md)
- [AI Coding Harness](../concepts/ai-coding-harness.md)
- [Code Execution](../concepts/code-execution.md)
- [Human in the Loop](../concepts/human-in-the-loop.md)
- [Agentic RAG](../concepts/agentic-rag.md)
- [Provider Independence](../concepts/provider-independence.md)
- [Commandify Everything](../concepts/commandify-everything.md)
- [Claude Code Hooks](../concepts/claude-code-hooks.md)

## Entities

- [Pydantic AI](../entities/tools/pydantic-ai.md)
- [MCP (Model Context Protocol)](../entities/tools/mcp.md)
- [Claude Agent SDK](../entities/tools/claude-agent-sdk.md)
- [Codex](../entities/tools/codex.md)
- [OpenClaw](../entities/tools/openclaw.md)
- [Cole Medin](../entities/people/cole-medin.md)
- [GitHub](../entities/tools/github.md)

## Key moments

- **[0:00:35]** Pydantic AI 2.0 centers on a single primitive: the capability
- **[0:01:23]** Definition: a capability bundles instructions, tools, lifecycle hooks, and model settings into one composable unit
- **[0:02:11]** Capabilities are reusable Lego-like units shared across agents; the layer above MCP servers
- **[0:03:33]** Why Pydantic AI had fallen behind: rise of coding-agent SDKs (Claude Agent SDK, Codex SDK)
- **[0:08:41]** Pydantic AI 2.0 constructor: model + a set of capabilities vs 1.0's hodgepodge
- **[0:09:11]** Reuse example: knowledge-base capability shared by support agent and FAQ widget
- **[0:09:43]** How a capability is defined: instructions, tool set, model settings, a pre-tool-use hook
- **[0:10:13]** Progressive disclosure: brief descriptions cataloged, full instructions loaded only when needed
- **[0:10:59]** CLI demo: agent uses thinking + knowledge-base capabilities, skips escalation
- **[0:11:56]** Demo: refund/duplicate-charge query triggers loading the escalation capability
- **[0:12:36]** The harness and lean core: two layers of capabilities
- **[0:13:21]** Harness layer: code mode + Pydantic's open-source Monty sandbox

## Transcript

[Raw transcript](../raw/pydantic-ai-20-the-new-best-way-to-build-ai-agents-is-composing-capabilities.md)
