---
type: source
title: "Claude Skills Aren't Just for Claude - Here's How to Build Them for ANY Agent"
description: "Anthropic's skills are a universal, framework-agnostic pattern built on progressive disclosure that you can reimplement in any agent (here Pydantic AI) with a dynamic system prompt plus a couple of file-reading tools, then verify with evals and observability."
youtube_id: -iTNOaCmLcw
url: https://www.youtube.com/watch?v=-iTNOaCmLcw
slug: claude-skills-arent-just-for-claude-heres-how-to-build-them-for-any-agent
published: 2026-01-28
duration: "0:24:28"
recency_rank: 39
raw: "../raw/claude-skills-arent-just-for-claude-heres-how-to-build-them-for-any-agent.md"
tags: [skills, progressive-disclosure, pydantic-ai]
created: 2026-07-21
updated: 2026-07-21
---
# Claude Skills Aren't Just for Claude - Here's How to Build Them for ANY Agent

Cole argues that Anthropic's skills feature, while credited to Anthropic for popularizing it, is really a universal concept rather than something locked to the Claude ecosystem. Its power comes from progressive disclosure: instead of dumping every capability and tool into the context window up front (as an MCP server or a bloated global-rules file would), you give the agent only short skill descriptions in the system prompt and let it discover the full instructions and reference files as it needs them. The three layers are the ~50-100 word YAML front-matter description (layer 1, ~5% of the skill's context), the skill.md with the full instructions (layer 2, often 300-500 lines / ~30% of context), and optional reference documents and scripts (layer 3, unlimited depth).

He then demonstrates a GitHub template that recreates skills in Pydantic AI. The mechanism is simple: a dynamic system prompt scans a skills directory, extracts each skill.md's front-matter description and path, and injects them into the base prompt (which itself teaches the LLM what skills are and how to invoke them). A small tool set gives the agent a load_skill tool (reads and returns a skill.md), a read_reference tool (reads a layer-3 file), and a list_references helper. Whatever a tool returns lands in the agent's short-term memory, so capabilities load on demand. The approach works with any framework or model (Open Router, Ollama, OpenAI, local AI). He also shows Claude Desktop's built-in skill-creator skill as a meta way to author new skills.

The final third covers reliability: with dozens of skills you need to know the agent actually pulls the right one for a given request. Pydantic AI's built-in eval framework lets you define YAML test cases with custom evaluators (e.g. asking about New York weather must load the weather skill) and run them as a fast, cheap Haiku smoke test (25/25 passing) every time you change the system prompt or add skills. For production, Logfire (also by the Pydantic team) instruments the agent to capture traces, token usage, cost, and tool-call parameters so you can debug real user interactions in the wild.

## Concepts covered

- [Skills](../concepts/skills.md)
- [Progressive Disclosure](../concepts/progressive-disclosure.md)
- [Context Engineering](../concepts/context-engineering.md)
- [The Problems With MCP Servers](../concepts/mcp-problems.md)
- [Provider Independence](../concepts/provider-independence.md)
- [Global Rules](../concepts/global-rules.md)
- [Code Execution](../concepts/code-execution.md)
- [Agent Evaluation](../concepts/agent-evaluation.md)
- [Agent Observability](../concepts/agent-observability.md)

## Entities

- [Pydantic AI](../entities/tools/pydantic-ai.md)
- [Anthropic](../entities/organizations/anthropic.md)
- [Claude Code](../entities/tools/claude-code.md)
- [Logfire](../entities/tools/logfire.md)
- [Claude Desktop](../entities/tools/claude-desktop.md)
- [OpenRouter](../entities/tools/openrouter.md)
- [Cole Medin](../entities/people/cole-medin.md)

## Key moments

- **[0:00:00]** Framing: skills are one of the most important recent AI advances, and beautifully simple
- **[0:00:56]** Core claim: skills are a universal concept, not limited to the Claude ecosystem
- **[0:03:26]** The problem skills solve: giving capabilities without overwhelming the context window
- **[0:04:23]** Progressive disclosure explained via Anthropic's PDF-processing skill diagram; three layers
- **[0:06:06]** Best practices: description 50-100 words (~5%), skill.md 300-500 lines (~30%)
- **[0:06:31]** Dynamic system prompt: collect all skill descriptions + paths into the prompt
- **[0:07:28]** The load_skill tool takes a path, returns skill.md content into short-term memory
- **[0:09:41]** Live demo of the Pydantic AI skills agent (recipe finder, weather)
- **[0:13:30]** Code walkthrough: dynamic system prompt via agent.system_prompt decorator
- **[0:15:41]** Three tools: load_skill, read_reference, list_references
- **[0:17:44]** Meta tip: use Claude Desktop's skill-creator skill to author skills
- **[0:18:34]** Reliability question: how to know the agent leverages the right skill
- **[0:19:46]** Evals with Pydantic AI's built-in framework, YAML test cases, custom evaluators
- **[0:21:54]** 25/25 eval cases pass using Haiku as a cheap fast smoke test
- **[0:22:20]** Observability with Logfire for production traces, token usage, cost, tool params

## Transcript

[Raw transcript](../raw/claude-skills-arent-just-for-claude-heres-how-to-build-them-for-any-agent.md)

