---
type: entity
subtype: tool
title: "SQLite"
description: "Embedded, file-based SQL database that lets example projects run with zero external database setup."
resource: "https://www.sqlite.org"
tags: [database, backend]
videos: [openais-swarm-a-game-changer-for-ai-agents]
created: 2026-07-21
updated: 2026-07-21
---

# SQLite

SQLite is a full SQL database that lives in a single file on disk, with no server to install, no connection string to provision, and no credentials to hand out. In Cole's teaching builds that property is the entire selling point: viewers can clone the repo and run the demo immediately. Describing the Swarm project he says "you can immediately run this entire thing without even without a SQL database because I'm using SQL light here" [0:08:35]. The point is not that SQLite is the production answer, it is that the database stops being a prerequisite so the agent architecture is the only thing you have to think about.

## How Cole uses it

The pattern is a seed script plus a stock library import. He ships SQL scripts that create the tables and load mock data, so "by the time the script is run we will have a full sqlite database with all the tables created and all of the mock data ready for our agents to query" [0:10:39], and the only imports the project needs are the agent framework and Python's built-in `sqlite3`. On top of that sits the [OpenAI Swarm](./openai-swarm.md) demo: a router agent hands each question to a specialist (RSS feed, user, analytics), every specialist shares a base prompt with the table schemas injected, and each one holds a single run-a-SELECT tool. The database schema doubles as agent context, which is what makes a text-to-SQL [agent team](../../concepts/agent-teams.md) legible in under a hundred lines.

That framing also sets the upgrade path. SQLite is the zero-setup starting point for a prototype; when the same system needs concurrency, hosted access, chat memory, or vector search, Cole moves to [Postgres](./postgres-pgvector.md) and [Supabase](./supabase.md) or serverless [Neon](./neon.md). Keeping tabular data in SQL at all, rather than flattening it into embeddings, is itself the deliberate choice: structured data stays queryable instead of being forced through [semantic search](../../concepts/semantic-search.md).

## Realizes

- [Rapid Prototyping](../../concepts/rapid-prototyping.md) - Building a fast proof of concept with managed services first, then hardening only what proves out, instead of over-engineering up front.
- [Structured vs Unstructured Data](../../concepts/structured-vs-unstructured-data.md) - Choosing the right representation for RAG, keeping tabular data queryable as SQL while formatting prose as markdown, rather than forcing everything through vector search.
- [Learn by Building](../../concepts/learn-by-building.md) - Learning AI engineering by building real projects, forking open source, and rebuilding from docs rather than passive study.

## Contrasts with

- [Postgres](./postgres-pgvector.md) - A Postgres extension for storing vector embeddings, used within Supabase as a production-ready vector store for RAG.
- [Supabase](./supabase.md) - A single platform providing Postgres for scalable chat memory plus the pgvector store for RAG embeddings, recommended over in-memory alternatives.
- [Neon](./neon.md) - Serverless Postgres platform Cole favors, acquired by Databricks in 2025.
- [MongoDB](./mongodb.md) - NoSQL database used here as both the document store and vector database, with aggregation pipelines and preview Rank Fusion features that make it optimal for hybrid search.

## Works with

- [OpenAI Swarm](./openai-swarm.md) - OpenAI's experimental multi-agent framework for building teams of agents that hand off to each other; defaults to OpenAI models but accepts a custom client.
- [Python](./python.md) - Language Auto-GPT is built in; requires Python 3.8+ to run.

## Related

- [Agent Teams](../../concepts/agent-teams.md) - Coordinating multiple specialized agents, via orchestrators, routers, and handoffs, to solve a task no single agent handles well.
- [Tool Design](../../concepts/tool-design.md) - Designing agent tools to be few, single-purpose, and well-described (often via docstrings) so the model uses them reliably.
- [Single vs. Multi-Agent Architecture](../../concepts/single-vs-multi-agent.md) - The core architectural decision between one capable agent and a coordinated system of specialized agents with handoffs, and when the added complexity of multi-agent orchestration is actually worth it.
- [Context Engineering](../../concepts/context-engineering.md) - The deliberate practice of curating exactly what goes into an LLM's limited context window - system messages, schemas, chat history, and dynamic variables - to avoid overload and keep outputs sharp.

## Sources

- [OpenAI's Swarm - a GAME CHANGER for AI Agents](../../sources/openais-swarm-a-game-changer-for-ai-agents.md) - "[0:08:35] you can immediately run this entire thing without even without a SQL database because I'm using SQL light here"
- [OpenAI's Swarm - a GAME CHANGER for AI Agents](../../sources/openais-swarm-a-game-changer-for-ai-agents.md) - "[0:10:39] by the time the script is run we will have a full sqlite database with all the tables created and all of the mock data ready for our agents to query"
