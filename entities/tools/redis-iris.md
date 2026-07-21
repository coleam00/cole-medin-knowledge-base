---
type: entity
subtype: tool
title: "Redis Iris"
description: "A preview Redis product that wraps the database with a Context Retriever (auto-generated MCP tools over defined entities/schema) and Agent Memory (short/long-term with background promotion to vector-indexed memory), demoed as the production-agent substitute for markdown second brains."
resource: "https://redis.io/"
tags: [database, backend]
videos: [i-love-the-karpathy-llm-wiki-but-it-doesnt-scale-heres-what-does]
created: 2026-07-21
updated: 2026-07-21
---

# Redis Iris

Redis Iris is a layer that sits on top of a Redis database and hands agents structured, tool-mediated access to whatever is stored in it. Cole introduces it as the thing you reach for when a markdown knowledge base stops scaling: "they recently put out Redis Iris. This is in preview right now, but it is extremely powerful. It really is the entire wrapper over Redis as the database to give your agents better access" [0:04:48]. It has exactly two halves, matching the two things a production agent needs from its database - business context and user memory - and Cole demos both against one [Pydantic AI](./pydantic-ai.md) agent.

**Context Retriever** solves the schema problem. Raw Redis is key-value, so "there's no schema. Everything is just key-value pairs" [0:08:48] and the agent has no idea what it may query, much less how. You define entities and their field types (customer, product, order), which "maps pretty much one-to-one to the different tables that we have in our underlying Redis database" [0:11:23], and the service auto-generates an [MCP](../../concepts/mcp.md) server whose tools cover every access path - filter by any attribute, full-text search across text fields. Attaching it is ordinary MCP wiring: Cole handed the docs to [Claude Code](./claude-code.md) and it "one-shot the whole thing" [0:12:58]. The payoff is token economy. A question that would cost an [LLM wiki](../../concepts/the-llm-wiki.md) agent a chain of file reads collapses into one MCP call.

**Agent Memory** is the same idea over a different transport: "our agent memory works just like context retriever where we create a service. This time though, it's not an MCP server, it's just an API endpoint" [0:15:47]. Every conversation lands in session (short-term) memory, and a background process extracts the durable facts and promotes them to long-term memory, vector-indexed so "each individual user can have millions of memories" [0:15:31] and the right ones still surface. The promoted memories stay plain keys in your own database, readable and deletable.

Cole is explicit about the boundary: personal agents do not need this, and the LLM wiki in [Obsidian](./obsidian.md) is still ideal there. Iris is the production layer, where multi-tenant scale and managed memory extraction matter more than flexibility.

## Realizes

- [Memory Systems](../../concepts/memory-systems.md) - Giving agents durable short- and long-term memory so conversations, user context, and facts persist across sessions and users.
- [Self-Evolving Memory](../../concepts/self-evolving-memory.md) - A memory system that reflects on and rewrites its own notes over time, promoting and pruning what it stores.
- [Model Context Protocol (MCP)](../../concepts/mcp.md) - An open protocol for packaging tools, data, and RAG capabilities as servers that any AI coding assistant or agent can connect to and call with a standard interface.
- [Structured vs Unstructured Data](../../concepts/structured-vs-unstructured-data.md) - Choosing the right representation for RAG, keeping tabular data queryable as SQL while formatting prose as markdown, rather than forcing everything through vector search.
- [Semantic Search](../../concepts/semantic-search.md) - Retrieving content by embedding-based similarity so results match on meaning rather than exact keywords.
- [Multi-Tenant Agents](../../concepts/multi-tenant-agents.md) - Building a single agent that serves many users, each with personalized tools, memory, and securely authorized access to their own accounts.
- [Production-Grade Agents](../../concepts/production-grade-agents.md) - Real agents need validation, error handling, testing, logging, observability, and monitoring rather than just an LLM plus tools stitched together.

## Contrasts with

- [The LLM Wiki](../../concepts/the-llm-wiki.md) - An LLM-maintained knowledge base of plain markdown pages that compiles sources into a navigable, self-referential wiki.
- [Production vs. Personal Agents](../../concepts/production-vs-personal-agents.md) - The architectural divide between quick personal-use agents and systems built to scale in production, and what has to change to cross that line.

## Works with

- [Redis](./redis.md) - The underlying key-value database Iris wraps and structures.
- [Pydantic AI](./pydantic-ai.md) - Cole's agent framework for the demo agent that consumes both the retriever MCP and the memory API.
- [Claude Code](./claude-code.md) - Used to wire the MCP connection and the memory tools into the agent from the Iris documentation alone.

## Related

- [Mem0](./mem0.md) - Open-source Python library for building per-user long-term memory for AI agents via memory extraction, vector storage, and retrieval.
- [Obsidian](./obsidian.md) - Free, local, markdown-based knowledge app Cole uses as the storage layer for his AI second brain, still his pick for personal agents.
- [Second Brain](../../concepts/second-brain.md) - A personal, always-on AI system that captures, recalls, and acts on your knowledge and daily context.
- [Andrej Karpathy](../people/andrej-karpathy.md) - Popularized the LLM-built personal knowledge base whose structure Iris mirrors in database form.

## Sources

- [I Love the Karpathy LLM Wiki but it Doesn't Scale. Here's What Does.](../../sources/i-love-the-karpathy-llm-wiki-but-it-doesnt-scale-heres-what-does.md) - "[0:04:48] they recently put out Redis Iris. This is in preview right now, but it is extremely powerful. It really is the entire wrapper over Redis as the database to give your agents better access."
- [I Love the Karpathy LLM Wiki but it Doesn't Scale. Here's What Does.](../../sources/i-love-the-karpathy-llm-wiki-but-it-doesnt-scale-heres-what-does.md) - "[0:15:47] our agent memory works just like context retriever where we create a service. This time though, it's not an MCP server, it's just an API endpoint."
