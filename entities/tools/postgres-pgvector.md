---
type: entity
subtype: tool
title: "Postgres"
description: "A Postgres extension for storing vector embeddings, used within Supabase as a production-ready vector store for RAG."
resource: "https://www.postgresql.org"
tags: [database, postgres, pgvector, vector-store, backend]
videos: [the-only-ai-tech-stack-you-need-in-2026, every-rag-strategy-explained-in-13-minutes-no-fluff, turn-any-file-into-llm-knowledge-in-seconds, introducing-rag-20-agentic-rag-knowledge-graphs-free-template, why-is-everyone-missing-this-with-ai-agents-memory-tools-that-scale, build-and-ship-any-mcp-server-in-minutes-full-guide, your-ultimate-n8n-rag-ai-agent-template-just-got-a-massive-upgrade, i-built-the-ultimate-n8n-rag-ai-agent-template, run-supabase-100-locally-for-your-ai-agents, the-proven-solution-for-unbelievable-rag-performance-lightrag-guide, i-built-a-safer-openclaw-alternative-using-claude-code, context-engineering-101-the-simple-strategy-to-100x-ai-coding]
created: 2026-07-21
updated: 2026-07-21
---

# Postgres

Postgres is Cole's default database for AI agents, and the pgvector extension is what lets a plain SQL database double as a vector store for RAG. The pitch is that you do not need a separate specialized service: "for storage, I love using Postgres... thanks to pgvector, I can basically use Postgres as a vector database" (the-only-ai-tech-stack, 0:13:35). Across his RAG builds it is the constant, "I love using Postgres with pgvector for most of my rag AI agents" (every-rag-strategy, 0:03:54), because the extension turns a relational table into a similarity-searchable one: "we got Postgres with the pgvector extension to essentially turn a SQL database into what can act as a vector database" (introducing-rag-20, 0:05:41).

Postgres does double duty for Cole. Alongside embeddings it holds chat memory and long-term agent state: "we're using Postgres first of all to store our checkpointers... And then also we have this new concept of a store. The store is for our long-term memory" (why-is-everyone-missing-this, 0:23:01). The retrieval itself is a SQL function the agent calls as a tool, "we have our match chunks function. This is the SQL that our agent actually invokes as a tool to search our knowledge base" (turn-any-file, 0:16:45). Because it is just Postgres, it is portable across hosts: "this can really be any Postgres platform. It can be Supabase Neon you could host Postgres yourself" (build-and-ship-any-mcp-server, 0:10:44), and templates are written so "you can use any Postgres database like Supabase or self-hosted Postgres" (your-ultimate-n8n-rag-template-upgrade, 0:04:37).

Compared with the fuller Supabase platform, Cole reaches for raw Postgres when he wants something lighter or more control over SQL. In n8n it exposes better primitives: "Postgres offers some better nodes for things like running SQL queries doing upserts... you don't have those options for the Supabase nodes" (i-built-the-ultimate-n8n-rag-template, 0:19:15). He also uses SQLite for local single-machine builds and swaps to Postgres for remote deployment: "SQLite for the database, and I'm using Postgres when I deploy it remotely" (i-built-a-safer-openclaw-alternative, 0:09:45). For heavier RAG, Postgres can even back the graph layer via Apache AGE alongside the vector layer.

## Contrasts with

- [Supabase](./supabase.md) is Postgres plus a managed dashboard, auth, and pgvector pre-wired; Cole picks bare Postgres when he wants lighter nodes or self-hosting.
- [Neon](./neon.md) is serverless Postgres with autoscaling and branching, Cole's more recent go-to for the same pgvector workloads.
- [Pinecone](./pinecone.md) and [Qdrant](./qdrant.md) are the dedicated vector databases pgvector lets you skip.

## Realizes

- [Retrieval-Augmented Generation (RAG)](../../concepts/rag.md) - the primary workload pgvector powers by turning a SQL table into a similarity-searchable store.
- [Agentic RAG](../../concepts/agentic-rag.md) - the match-chunks SQL function an agent invokes as a retrieval tool.
- [Memory Systems](../../concepts/memory-systems.md) - Postgres checkpointers and stores hold agent chat history and long-term recall.

## Works with

- [n8n](./n8n.md) - drives Postgres and its pgvector store through dedicated SQL and vector-store nodes.

## Related

- [Vector Embeddings](../../concepts/vector-embeddings.md) - the numeric vectors that land in a pgvector column.
- [Chunking](../../concepts/chunking.md) - the preprocessing that produces the rows pgvector indexes.
- [Local & Self-Hosted AI](../../concepts/local-ai.md) - a self-hosted Postgres container as the database for a fully local stack.

## Sources

- [The ONLY AI Tech Stack You Need in 2026](../../sources/the-only-ai-tech-stack-you-need-in-2026.md) - "[0:13:35] for storage, I love using Postgres... thanks to pgvector, I can basically use Postgres as a vector database."
- [Every RAG Strategy Explained in 13 Minutes (No Fluff)](../../sources/every-rag-strategy-explained-in-13-minutes-no-fluff.md) - "[0:03:54] I love using Postgres with pgvector for most of my rag AI agents."
- [Turn ANY File into LLM Knowledge in SECONDS](../../sources/turn-any-file-into-llm-knowledge-in-seconds.md) - "[0:16:45] we have our match chunks function. This is the SQL that our agent actually invokes as a tool to search our knowledge base."
- [Introducing RAG 2.0: Agentic RAG + Knowledge Graphs (FREE Template)](../../sources/introducing-rag-20-agentic-rag-knowledge-graphs-free-template.md) - "[0:05:41] we got Postgres with the pgvector extension to essentially turn a SQL database into what can act as a vector database."
- [Why is Everyone Missing This with AI Agents?! (Memory + Tools that Scale)](../../sources/why-is-everyone-missing-this-with-ai-agents-memory-tools-that-scale.md) - "[0:23:01] we're using Postgres first of all to store our checkpointers... And then also we have this new concept of a store. The store is for our long-term memory."
- [Build and Ship Any MCP Server in MINUTES (Full Guide)](../../sources/build-and-ship-any-mcp-server-in-minutes-full-guide.md) - "[0:10:44] Depending on your platform this can really be any Postgres platform. It can be Supabase Neon you could host Postgres yourself."
- [Your ULTIMATE n8n RAG AI Agent Template just got a Massive Upgrade](../../sources/your-ultimate-n8n-rag-ai-agent-template-just-got-a-massive-upgrade.md) - "[0:04:37] this template uses Postgres. I've actually evolved it. So you can use any Postgres database like Supabase or self-hosted Postgres."
- [I Built the ULTIMATE n8n RAG AI Agent Template](../../sources/i-built-the-ultimate-n8n-rag-ai-agent-template.md) - "[0:19:15] Postgres offers some better nodes for things like running SQL queries doing upserts... you don't have those options for the Supabase nodes"
- [Run Supabase 100% LOCALLY for Your AI Agents](../../sources/run-supabase-100-locally-for-your-ai-agents.md) - "[0:00:17] you can also use the pgvector extension to literally turn it into a vector database for rag"
- [The PROVEN Solution for Unbelievable RAG Performance (LightRAG Guide)](../../sources/the-proven-solution-for-unbelievable-rag-performance-lightrag-guide.md) - "[0:04:38] You can use Postgres for both the vector database and for the graph DB with Apache age."
- [I Built a Safer OpenClaw Alternative Using Claude Code](../../sources/i-built-a-safer-openclaw-alternative-using-claude-code.md) - "[0:09:45] SQLite for the database, and I'm using Postgres when I deploy it remotely."
- [Context Engineering 101 - The Simple Strategy to 100x AI Coding](../../sources/context-engineering-101-the-simple-strategy-to-100x-ai-coding.md) - "[0:30:31] We're using Postgres to manage everything in our database."
