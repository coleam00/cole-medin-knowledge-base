---
type: source
title: "I Love the Karpathy LLM Wiki but it Doesn't Scale. Here's What Does."
description: "Markdown-driven second-brain / LLM-wiki agents are ideal for personal use but don't scale to production; shipping an agent to many users requires a database with a context-retrieval layer and managed agent memory instead of markdown files."
youtube_id: R-5_2nsF_ZM
url: https://www.youtube.com/watch?v=R-5_2nsF_ZM
slug: i-love-the-karpathy-llm-wiki-but-it-doesnt-scale-heres-what-does
published: 2026-07-08
duration: "0:18:58"
recency_rank: 4
raw: "../raw/i-love-the-karpathy-llm-wiki-but-it-doesnt-scale-heres-what-does.md"
tags: [second-brain, memory-systems, production-agents]
created: 2026-07-21
updated: 2026-07-21
---

Cole draws a hard line between two kinds of AI agents. Personal agents (second brains, Karpathy-style LLM wikis) run locally on a coding-agent SDK against a pile of interconnected markdown documents. That setup is the simplest and most flexible thing for one person because it lives on your own machine and needs no governance, access control, or auditability. But the moment you ship an agent to many concurrent users with live data, markdown stops working: files don't scale for organization/search, coding-agent SDK subscriptions can't be used commercially, and reading whole markdown documents burns far too many tokens.

The production architecture keeps the benefits of a second brain (user memory, well-organized retrievable context) but swaps the substrate for a database with a context layer wrapped around it. Cole demos this with Redis (via the preview product Redis Iris) and a Pydantic AI agent, which he still prefers over coding-agent SDKs for production because SDKs are slow and token-heavy. Two pieces sit on top of the database: a Context Retriever that documents entities/schema over otherwise-unstructured key-value data and auto-generates MCP tools to filter and text-search at scale, and Agent Memory that stores short-term session memory and runs a background process promoting the "golden nuggets" into vector-indexed long-term memory.

The payoff demo: an e-commerce support agent answers a loaded, memory-dependent request in a single-digit number of tool calls and under a thousand tokens, recalling a stored preference ("reshipments over refunds") from a prior session and querying orders/shipments by their relationships. Cole stresses the ideas generalize to any production infrastructure; Redis Iris just handles the memory-extraction and tool-generation plumbing for you. He closes by reaffirming both lanes matter: keep markdown/LLM-wiki for personal agents, move to this layered database architecture the instant other people log in.

## Concepts covered

- [The LLM Wiki](../concepts/the-llm-wiki.md)
- [Second Brain](../concepts/second-brain.md)
- [Production vs. Personal Agents](../concepts/production-vs-personal-agents.md)
- [Context Engineering](../concepts/context-engineering.md)
- [Memory Systems](../concepts/memory-systems.md)
- [Self-Evolving Memory](../concepts/self-evolving-memory.md)
- [Traditional RAG](../concepts/traditional-rag.md)
- [Structured vs Unstructured Data](../concepts/structured-vs-unstructured-data.md)
- [Model Context Protocol (MCP)](../concepts/mcp.md)
- [Model Selection](../concepts/model-selection.md)
- [Provider Independence](../concepts/provider-independence.md)

## Entities

- [Cole Medin](../entities/people/cole-medin.md)
- [Andrej Karpathy](../entities/people/andrej-karpathy.md)
- [Pydantic AI](../entities/tools/pydantic-ai.md)
- [MCP (Model Context Protocol)](../entities/tools/mcp.md)
- [Claude Code](../entities/tools/claude-code.md)
- [Claude Agent SDK](../entities/tools/claude-agent-sdk.md)
- [Codex](../entities/tools/codex.md)
- [Obsidian](../entities/tools/obsidian.md)

## Key moments

- **[0:00:00]** Two kinds of agents: personal (local, markdown) vs shipped-to-others; everyone is over-fixated on personal
- **[0:01:53]** Why personal-agent markdown breaks in production: access control, retrieval at scale, SDK subscription cost, token bloat
- **[0:03:43]** Production architecture: a database with a context layer; introduces Context Retriever + Agent Memory on Redis
- **[0:07:37]** Live demo: Pydantic AI agent answers a memory + business-data request as customer Jordan Rivera
- **[0:09:49]** Excalidraw walkthrough of Context Retriever over unstructured Redis data
- **[0:11:05]** Redis dashboard: defining entities/schema, then auto-generating MCP tools per attribute
- **[0:14:40]** Agent Memory: short-term session memory + background promotion to long-term vector memory
- **[0:16:45]** New-session demo proves long-term memory recall of the reshipment-over-refund preference

## Transcript

[Raw transcript](../raw/i-love-the-karpathy-llm-wiki-but-it-doesnt-scale-heres-what-does.md)
