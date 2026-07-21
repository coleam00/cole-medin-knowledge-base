---
type: concept
title: "Retrieval-Augmented Generation (RAG)"
description: "Grounding an LLM's answers by retrieving relevant documents from an external knowledge base and injecting them into the prompt at query time."
tags: [rag, knowledge-base, retrieval, embeddings, vector-search]
videos: [full-guide-build-your-own-ai-second-brain-with-claude-code, why-the-best-ai-coding-tools-abandoned-rag-and-what-they-use-instead, build-a-rag-ai-agent-with-real-time-source-validation-copilotkit-pydantic-ai, the-simplest-rag-stack-that-actually-works-complete-guide, every-rag-strategy-explained-in-13-minutes-no-fluff, learn-90-of-building-ai-agents-in-30-minutes, the-official-archon-guide-10x-your-ai-coding-workflow, turn-any-file-into-llm-knowledge-in-seconds, the-proven-solution-for-unbelievable-rag-performance-lightrag-guide, build-ai-agents-that-evolve-over-time]
created: 2026-07-21
updated: 2026-07-21
---

# Retrieval-Augmented Generation (RAG)

RAG is the method for giving an LLM access to knowledge it was never trained on by retrieving relevant documents at query time and injecting them into the prompt. Cole's plainest definition: "Retrieval augmented generation is the way to give your AI agents the ability to search and leverage your knowledge and documents" (every-rag-strategy, 0:00:00). The name spells out the mechanic, "we then pass into the large language model. So it's able to leverage that as extra context to augment its answer. That's why it's called retrieval augmented generation" (every-rag-strategy, 0:01:51). The goal is domain expertise on demand: "you can basically make it an expert on your data, your meeting notes, your business processes, literally anything you want" (turn-any-file, 0:00:19).

## Why it matters

RAG is not a niche technique, it is the default. "Probably over 80% of AI agents running out in the wild right now are using rag to some extent" (learn-90-of-building-ai-agents, 0:13:41). When people ask Cole how to make an agent useful, "tools and rag is always the answer" (learn-90, 0:13:13). It keeps its relevance even as context windows grow to millions of tokens, because pulling a focused set of chunks beats stuffing everything in: "RAG is still the way to bring external knowledge into our agents making them experts on our documents and data, and it's still as relevant as ever, even as LLMs are starting to handle millions of tokens" (lightrag guide, 0:00:00).

## How it works

The pipeline has two halves. Ingestion turns documents into searchable vectors, "we have a step to extract the text a step to embed it to prep it for the vector database and then finally the step to insert it" (build-an-army-of-ai-agents / archon; also turn-any-file). Retrieval embeds the user's question, matches it against the store, and returns the top chunks: "when we have the user query come in we're going to embed that as well. Use that to match against our knowledge base to find the most relevant chunks to aid the agent in answering our question" (the-easiest-possible-strategy). Those chunks become extra context, "here are the 10 that we finally want to send to our agent so it can enhance its context to give us the final response. That's the goal of rag overall" (the-simplest-rag-stack, 0:22:31). A concrete grounding case: source-validated RAG surfaces the exact chunks so a user can see what the agent used, addressing that "we don't actually know the sources that our AI agent is using. Did it hallucinate?" (real-time-source-validation, 0:00:00).

Cole stretches the term deliberately: "You can extend the definition of rag to really any kind of search an agent can perform because really rag is just grabbing any kind of external information pulling it into the LLM's context window so we can augment its answer" (why-ai-coding-abandoned-rag, 0:01:23). Under that lens, long-term agent memory is RAG too: "you need some way to search through a longer term set of memories which actually does use rag under the hood" (learn-90, 0:22:21).

## Implemented by

- [Archon](../entities/tools/archon.md) performs RAG under the hood for its documentation knowledge base: "It's performing rag under the hood for both keyword and semantic searching" (official-archon-guide, 0:03:06).
- [Supabase](../entities/tools/supabase.md), [Qdrant](../entities/tools/qdrant.md), [Pinecone](../entities/tools/pinecone.md), and [Chroma](../entities/tools/chroma.md) are the vector stores Cole reaches for as the retrieval backbone.
- [n8n](../entities/tools/n8n.md) makes a no-code RAG pipeline out of its vector-store and document-loader nodes.

## Part of

- [Context Engineering](./context-engineering.md) treats RAG as a major lever: "Rag is a huge component of context engineering, being able to supply external documentation and knowledge to our AI coding assistants" (context-engineering, 0:04:21).

## Related

- [Semantic Search](./semantic-search.md) is the classic retrieval mechanism at RAG's core; "rag itself is semantic search" in its basic form (all-the-best-rag-strategies, 0:10:45).
- [Hybrid Search](./hybrid-search.md), [Reranking](./reranking.md), [Query Expansion](./query-expansion.md), and [Multi-Query RAG](./multi-query-rag.md) are the strategies that turn basic RAG into something production-grade.
- [Traditional RAG](./traditional-rag.md) is the naive one-shot baseline; [Agentic RAG](./agentic-rag.md) is the reasoning-driven successor.
- [Knowledge Bases](./knowledge-bases.md), [Vector Embeddings](./vector-embeddings.md), and [Chunking](./chunking.md) are the ingredients RAG is built from.
- [Memory Systems](./memory-systems.md) use RAG to give each user long-term recall.
- [Model Context Protocol (MCP)](./mcp.md) is how Cole exposes RAG to coding assistants as a tool.

## Sources

- [Every RAG Strategy Explained in 13 Minutes (No Fluff)](../sources/every-rag-strategy-explained-in-13-minutes-no-fluff.md) - "[0:01:51] we then pass into the large language model. So it's able to leverage that as extra context to augment its answer. That's why it's called retrieval augmented generation."
- [Why the Best AI Coding Tools Abandoned RAG (And What They Use Instead)](../sources/why-the-best-ai-coding-tools-abandoned-rag-and-what-they-use-instead.md) - "[0:01:23] You can extend the definition of rag to really any kind of search an agent can perform because really rag is just grabbing any kind of external information pulling it into the LLM's context window so we can augment its answer."
- [The Simplest RAG Stack That Actually Works (Complete Guide)](../sources/the-simplest-rag-stack-that-actually-works-complete-guide.md) - "[0:22:31] here are the 10 that we finally want to send to our agent so it can enhance its context to give us the final response. That's the goal of rag overall"
- [Learn 90% of Building AI Agents in 30 Minutes](../sources/learn-90-of-building-ai-agents-in-30-minutes.md) - "[0:13:41] probably over 80% of AI agents running out in the wild right now are using rag to some extent"
- [The PROVEN Solution for Unbelievable RAG Performance (LightRAG Guide)](../sources/the-proven-solution-for-unbelievable-rag-performance-lightrag-guide.md) - "[0:00:00] RAG is still the way to bring external knowledge into our agents making them experts on our documents and data, and it's still as relevant as ever, even as LLMs are starting to handle millions of tokens"
- [Build a RAG AI Agent with REAL-TIME Source Validation (CopilotKit + Pydantic AI)](../sources/build-a-rag-ai-agent-with-real-time-source-validation-copilotkit-pydantic-ai.md) - "[0:00:00] One of the biggest problems with most rag systems is that we don't actually know the sources that our AI agent is using. Did it hallucinate? Did it pull from irrelevant documents?"
- [Turn ANY File into LLM Knowledge in SECONDS](../sources/turn-any-file-into-llm-knowledge-in-seconds.md) - "[0:00:19] It is a method for curating external knowledge for a large language model. So you can basically make it an expert on your data, your meeting notes, your business processes, literally anything you want."
- [The OFFICIAL Archon Guide - 10x Your AI Coding Workflow](../sources/the-official-archon-guide-10x-your-ai-coding-workflow.md) - "[0:03:06] It's performing rag under the hood for both keyword and semantic searching. Very, very powerful rag strategies that we have for this."
- [Full Guide - Build Your Own AI Second Brain with Claude Code](../sources/full-guide-build-your-own-ai-second-brain-with-claude-code.md) - "[0:12:54] we index all of our daily logs into a SQLite database, and you could do Postgres as well so our agent can search through all of the daily logs"
- [Build AI Agents that EVOLVE Over Time](../sources/build-ai-agents-that-evolve-over-time.md) - "[0:00:19] everyone is very focused on using their documents to teach AI agents through RAG. And that is certainly important, but it isn't really memory"
