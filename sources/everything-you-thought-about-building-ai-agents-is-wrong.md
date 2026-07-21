---
type: source
title: "Everything You Thought About Building AI Agents is Wrong"
description: "Whether to build an AI agent on a batteries-included coding-agent SDK or a from-scratch framework isn't a fashion choice but a use-case decision driven by who uses it and your tolerance for speed, cost, and scale."
youtube_id: gmaHRwijOXs
url: https://www.youtube.com/watch?v=gmaHRwijOXs
slug: everything-you-thought-about-building-ai-agents-is-wrong
published: 2026-03-25
duration: "0:15:53"
recency_rank: 24
raw: "../raw/everything-you-thought-about-building-ai-agents-is-wrong.md"
tags: [ai-agents, sdk-vs-framework, rag, agentic-rag]
created: 2026-07-21
updated: 2026-07-21
---

# Everything You Thought About Building AI Agents is Wrong

Cole pushes back on the mainstream narrative that agent frameworks like Pydantic AI, LangGraph, and n8n are obsolete now that coding-agent SDKs (Claude Agent SDK, Codex SDK) let you build any agent on top of a coding-assistant foundation. He concedes the SDK path is genuinely transformative for some cases: it ships with prompting, tools, conversation-history management, sub-agents, hooks, permissions, skills, and MCP support out of the box, so an entire agent can live in one TypeScript file with no custom RAG or database glue. That's what powers his own OpenClaw-inspired second-brain heartbeat system.

But the SDKs carry three hard limitations: they're significantly slower (reasoning overhead), more token-heavy (which forces API-key billing the moment more than one person uses the agent, since subscription use for multi-user agents violates ToS), and less deterministic because so much is managed for you. For production agents needing sub-second latency, cost control, observability, and full control over message history, a framework built from the ground up wins. Frameworks can still adopt modern techniques: Cole shows a Pydantic AI agent he gave custom skills support, loading skill.md files dynamically just like Claude Code but faster and cheaper. The decision framework reduces to two questions: who uses the agent, and what's your tolerance for speed/scale/cost. Solo + delay-tolerant leans SDK; multi-user + production + scale leans framework, though you can prototype on the SDK then migrate.

On RAG, Cole clarifies the 'RAG is dead' claim. In 2024 nearly every agent used semantic search; in 2025 coding agents shifted to file search (grep) because it outperforms RAG on smaller corpuses, and that's now baked into the SDKs. But for large knowledge bases with thousands of documents, semantic search remains more accurate and far cheaper. The 2026 middle ground is agentic RAG: giving the agent both semantic and keyword/grep search, plus graph RAG for massive or multi-repo codebases. RAG isn't dead; match the retrieval tool to the corpus size.

## Concepts covered

- [SDK vs. Framework Decision](../concepts/sdk-vs-framework-decision.md)
- [AI Coding Harness](../concepts/ai-coding-harness.md)
- [Agentic Workflow Engineering](../concepts/agentic-workflow-engineering.md)
- [Skills](../concepts/skills.md)
- [MCP (Model Context Protocol)](../entities/tools/mcp.md)
- [When RAG Is (and Isn't) Dead](../concepts/when-rag-is-dead.md)
- [Agentic RAG](../concepts/agentic-rag.md)
- [Semantic Search](../concepts/semantic-search.md)
- [Second Brain](../concepts/second-brain.md)
- [Heartbeat](../concepts/heartbeat.md)
- [Subagents Pattern](../concepts/subagents-pattern.md)
- [Provider Independence](../concepts/provider-independence.md)

## Entities

- [Claude Agent SDK](../entities/tools/claude-agent-sdk.md)
- [Codex](../entities/tools/codex.md)
- [Pydantic AI](../entities/tools/pydantic-ai.md)
- [Claude Code](../entities/tools/claude-code.md)
- [OpenClaw](../entities/tools/openclaw.md)
- [Neon](../entities/tools/neon.md)
- [grep (command-line search)](../entities/tools/ripgrep.md)
- [n8n](../entities/tools/n8n.md)
- [LangGraph](../entities/tools/langgraph.md)
- [Dynamous](../entities/organizations/dynamous.md)
- [Cole Medin](../entities/people/cole-medin.md)
- [Anthropic](../entities/organizations/anthropic.md)

## Key moments

- **[0:00:50]** Sets up the central nuance: building on SDKs is right for some use cases, frameworks for others
- **[0:01:48]** The old way of building agents (2024-2025): pick framework, define tools, add RAG, wire the agent loop
- **[0:03:41]** Why people shift to batteries-included SDKs: too much glue code to build agent infrastructure yourself
- **[0:04:32]** Demo: entire agent in one TypeScript file via Claude Agent SDK with sub-agents, MCP, skills
- **[0:06:39]** His second-brain heartbeat system runs entirely on the Claude Agent SDK, inspired by OpenClaw
- **[0:06:56]** Three key SDK limitations: slower, more token-heavy, less deterministic
- **[0:08:36]** Cost limitation: multi-user SDK agents force API-key billing; subscription use violates ToS
- **[0:09:43]** Frameworks can adopt skills too: custom skills support added to a Pydantic AI agent
- **[0:11:38]** The decision framework: who uses the agent + tolerance for speed/scale
- **[0:13:06]** What happened to RAG and why people say 'RAG is dead'
- **[0:14:15]** Agentic RAG as the 2026 middle ground: semantic + keyword/grep + graph RAG

## Transcript

[Raw transcript](../raw/everything-you-thought-about-building-ai-agents-is-wrong.md)
