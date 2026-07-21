---
type: source
title: "Build AI Agents that EVOLVE Over Time"
description: "AI agents become far more human-like and personalized when you give them long-term memory that learns from conversations, which the open-source Mem0 library makes simple by extracting, storing, and retrieving per-user memories from a vector database."
youtube_id: iOZpiXLT7iY
url: https://www.youtube.com/watch?v=iOZpiXLT7iY
slug: build-ai-agents-that-evolve-over-time
published: 2025-03-09
duration: "0:25:06"
recency_rank: 111
raw: "../raw/build-ai-agents-that-evolve-over-time.md"
tags: [memory, self-evolving-memory, mem0, personalization]
created: 2026-07-21
updated: 2026-07-21
---

# Build AI Agents that EVOLVE Over Time

Cole argues that most people conflate RAG over documents with memory, but they are not the same thing. True long-term memory lets an agent learn from the actual conversations it has with a user, remembering goals, preferences, instructions, and corrections across sessions. He opens by contrasting a stock Gemini chatbot, which forgets a described tech stack the moment a new conversation starts, with a Pydantic AI agent backed by Mem0 that recalls those same details in a fresh chat. That difference is what personalization feels like in practice.

The bulk of the video is a from-scratch walkthrough of Mem0 in three iterations. Version one is a minimal Python loop: a `chat_with_memories` function searches Mem0 for the most relevant memories, injects them into the system prompt, calls GPT-4o mini with only the system prompt plus the latest user message (deliberately no conversation history), then calls Mem0's `add` to extract and store new memories. Because no chat history is retained, recall provably comes from long-term memory rather than the context window. Version two swaps the default in-memory store for a Supabase (pgvector) vector store with a one-line config change, so memories persist and can be inspected. Version three adds a Streamlit UI plus Supabase authentication so each signed-in user's memories are segregated by a real user ID.

A closing segment opens the box on Mem0's internals. Adding memories uses a dedicated LLM prompted to pull key facts from the conversation, then writes them to a per-user vector database with built-in conflict resolution to avoid duplicates. Searching rewrites the query with an LLM before retrieval and layers on advanced RAG techniques like reranking, relevance scoring, and timestamp metadata. Mem0 is framework-agnostic, works with any agent, and can be pushed further with graph-based entity and relation memory.

## Concepts covered

- [Self-Evolving Memory](../concepts/self-evolving-memory.md)
- [Memory Systems](../concepts/memory-systems.md)
- [Retrieval-Augmented Generation (RAG)](../concepts/rag.md)
- [Knowledge Bases](../concepts/knowledge-bases.md)
- [Vector Embeddings](../concepts/vector-embeddings.md)
- [Semantic Search](../concepts/semantic-search.md)
- [Query Expansion](../concepts/query-expansion.md)
- [Reranking](../concepts/reranking.md)
- [Knowledge Graphs](../concepts/knowledge-graphs.md)

## Entities

- [Mem0](../entities/tools/mem0.md)
- [Pydantic AI](../entities/tools/pydantic-ai.md)
- [Supabase](../entities/tools/supabase.md)
- [OpenAI](../entities/organizations/openai.md)
- [Streamlit](../entities/tools/streamlit.md)
- [Gemini](../entities/tools/gemini.md)
- [Cole Medin](../entities/people/cole-medin.md)

## Key moments

- **[0:00:19]** Framing: agents are human-like but have terrible memory; RAG over documents is not the same as memory
- **[0:01:42]** Demo: Gemini 2.0 Flash forgets the described tech stack in a new conversation
- **[0:03:00]** Contrast demo: Pydantic AI + Mem0 agent recalls the tech stack in a fresh conversation
- **[0:06:49]** Version 1 code walkthrough: `chat_with_memories`, search + inject + add
- **[0:08:58]** Key point: no conversation history is kept; recall comes purely from long-term memory
- **[0:12:11]** Version 2: swap in Supabase as the vector store with a one-line config change
- **[0:15:53]** Version 3: Streamlit UI + Supabase auth so memories are segregated by real user ID
- **[0:22:10]** Bonus: how Mem0 works internally, add (LLM extraction + conflict resolution) and search (query rewrite + reranking)

## Transcript

[Raw transcript](../raw/build-ai-agents-that-evolve-over-time.md)
