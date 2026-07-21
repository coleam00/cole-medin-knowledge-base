---
type: entity
subtype: tool
title: "Supabase"
description: "A single platform providing Postgres for scalable chat memory plus the pgvector store for RAG embeddings, recommended over in-memory alternatives."
resource: "https://supabase.com"
tags: [database, postgres, vector-store, authentication, backend]
videos: [run-supabase-100-locally-for-your-ai-agents, this-rag-ai-agent-with-n8n-supabase-is-the-real-deal, the-future-of-rag-is-agentic-learn-this-strategy-now, the-official-archon-guide-10x-your-ai-coding-workflow, how-to-dominate-with-ai-in-2025, archon-beta-launch-livestream-what-you-missed, introducing-archon-the-revolutionary-operating-system-for-ai-coding, the-3-must-have-mcp-servers-for-any-ai-coding-and-how-to-use-them, build-ai-agents-that-evolve-over-time, my-top-20-lessons-from-building-100s-of-ai-agents-super-actionable, super-special-livestream-this-weekend-live-ai-agent-build, no-code-rag-agents-you-have-to-check-out-n8n-langchain, revealing-my-complete-ai-agent-blueprint]
created: 2026-07-21
updated: 2026-07-21
---

# Supabase

Supabase is the open-source backend platform Cole reaches for by default when an AI agent needs a database, and he is emphatic about why: "Supabase in my mind is the best absolute best database platform that also supports vectors for rag using PG vector" (this-rag-ai-agent-with-n8n-supabase, 0:00:30). It is Postgres under the hood, so the same account gives you a relational database, a vector store, and authentication in one place. As of the Supabase local guide, it "is an incredible open-source platform that definitely seems to be the most popular database for AI agents right now" (run-supabase-100-locally, 0:00:00), and Cole expects it to keep growing: "I really do think that Supabase is the future of Postgres. When they say scale the millions they really mean it" (the-official-archon-guide, 0:13:11).

The single-platform story is the whole appeal. Because pgvector ships as a Postgres extension, one Supabase project can hold both the RAG knowledge base and the structured agent data: "with Supabase I can have the rag and the structured data all in one place that's why I generally recommend Supabase" (the-future-of-rag-is-agentic, 0:38:35). Cole uses it for chat history and long-term memory the same way he uses it for documents, "the way that we insert memories into Supabase is using the exact same node in n8n as how we insert our documents into Supabase within our rag pipeline" (my-top-20-lessons, 0:37:52), and he steers agents away from the in-memory default toward a real store: "instead of using the default in-memory method for storing our memories, we want to use Supabase" (build-ai-agents-that-evolve, 0:12:11).

It is also the database that powers Archon. "You'll want Supabase because it's the database that powers all of Archon" (the-official-archon-guide, 0:05:00), and because state lives entirely in Supabase, teams can each run a local instance pointed at the same database: "everyone running their own Archon instances locally just pointing to the same Supabase database" (archon-beta-launch, 0:26:00). Cole uses its built-in email/password auth to scope agents per user, its dashboard MCP server to create tables and run migrations from a coding assistant, and its self-hosted stack (Studio, Kong, the auth container, and Postgres) for fully local deployments.

## Contrasts with

- [Postgres + pgvector](./postgres-pgvector.md) - A Postgres extension for storing vector embeddings, used within Supabase as a production-ready vector store for RAG.
- [Neon](./neon.md) - Serverless Postgres platform Cole favors, acquired by Databricks in 2025.
- [Pinecone](./pinecone.md) - Vector database used optionally by Auto-GPT to provide long-term memory.
- [Qdrant](./qdrant.md) - Vector database with an MCP server that lets agents do RAG without implementing custom retrieval tools.

## Works with

- [n8n](./n8n.md) - A no-code AI automation platform for building agents and workflows that integrate with 500+ applications.
- [Ollama](./ollama.md) - Local LLM runtime; works with a locally-run bolt.diy but can't be reached by a self-hosted (remote) instance.

## Related

- [Retrieval-Augmented Generation (RAG)](../../concepts/rag.md) - Grounding an LLM's answers by retrieving relevant documents from an external knowledge base and injecting them into the prompt at query time.
- [Agentic RAG](../../concepts/agentic-rag.md) - Giving an agent retrieval as a tool so it decides when and how to search a knowledge base, picking strategies and issuing follow-up queries instead of a single static lookup.
- [Knowledge Bases](../../concepts/knowledge-bases.md) - Curated bodies of knowledge an agent can retrieve from, distinct from raw model weights, that ground responses in trusted source material.
- [Vector Embeddings](../../concepts/vector-embeddings.md) - Numeric representations of text that enable semantic similarity search, stored and managed in a vector database for retrieval.
- [Chunking](../../concepts/chunking.md) - Splitting source documents into appropriately sized, embeddable segments, the foundational preprocessing step that determines RAG retrieval quality.
- [Model Selection](../../concepts/model-selection.md) - Choosing the right LLM per task by trading off quality, speed, and cost, often routing easy requests to cheap models and hard ones to expensive models.

## Sources

- [Run Supabase 100% LOCALLY for Your AI Agents](../../sources/run-supabase-100-locally-for-your-ai-agents.md) - "[0:00:00] everyone loves Supabase it is an incredible open-source platform that definitely seems to be the most popular database for AI agents right now"
- [This RAG AI Agent with n8n + Supabase is the Real Deal](../../sources/this-rag-ai-agent-with-n8n-supabase-is-the-real-deal.md) - "[0:00:30] Supabase in my mind is the best absolute best database platform that also supports vectors for rag using PG vector"
- [The Future of RAG is Agentic - Learn this Strategy NOW](../../sources/the-future-of-rag-is-agentic-learn-this-strategy-now.md) - "[0:38:35] with Supabase I can have the rag and the structured data all in one place that's why I generally recommend Supabase"
- [The OFFICIAL Archon Guide - 10x Your AI Coding Workflow](../../sources/the-official-archon-guide-10x-your-ai-coding-workflow.md) - "[0:13:11] I really do think that Supabase is the future of Postgres. When they say scale the millions they really mean it."
- [How to DOMINATE with AI in 2025](../../sources/how-to-dominate-with-ai-in-2025.md) - "[0:21:32] for my database I basically exclusively use Supabase for the Postgres under the hood um because it also has PG Vector for rag"
- [Archon Beta Launch Livestream - What You Missed!](../../sources/archon-beta-launch-livestream-what-you-missed.md) - "[0:26:00] you can have everyone running their own Archon instances locally just pointing to the same Supabase database"
- [Introducing Archon - The Revolutionary Operating System for AI Coding](../../sources/introducing-archon-the-revolutionary-operating-system-for-ai-coding.md) - "[0:03:29] You need a Supabase account for the database that manages everything under the hood."
- [The 3 MUST Have MCP Servers for Any AI Coding (and How to Use Them)](../../sources/the-3-must-have-mcp-servers-for-any-ai-coding-and-how-to-use-them.md) - "[0:02:57] This can create tables for you, list your projects that you have in your Supabase organization. It can write queries like pretty much any SQL query you could want."
- [Build AI Agents that EVOLVE Over Time](../../sources/build-ai-agents-that-evolve-over-time.md) - "[0:12:11] instead of using the default in-memory method for storing our memories, we want to use Supabase"
- [My Top 20 Lessons from Building 100s of AI Agents (Super Actionable)](../../sources/my-top-20-lessons-from-building-100s-of-ai-agents-super-actionable.md) - "[0:37:52] the way that we insert memories into Supabase is using the exact same node in n8n as how we insert our documents into Supabase within our rag pipeline."
- [Super Special Livestream this Weekend! (LIVE AI Agent Build)](../../sources/super-special-livestream-this-weekend-live-ai-agent-build.md) - "[0:03:17] for our database, we will be using a Supabase. And so this will be where we store all of our YouTube videos, including the transcripts and the embeddings"
- [No Code RAG Agents? You HAVE to Check out n8n + LangChain](../../sources/no-code-rag-agents-you-have-to-check-out-n8n-langchain.md) - "[0:06:43] you can have everything managed for your Rag and your chat memories all within one place in Supabase so that's my recommendation if you want to take something like this to production"
- [Revealing my COMPLETE AI Agent Blueprint](../../sources/revealing-my-complete-ai-agent-blueprint.md) - "[0:06:44] use Supabase you can use it for free it uses Postgres under the hood it's super powerful you can use it for rag as well"
