---
type: concept
title: "Semantic Search"
description: "Retrieving content by embedding-based similarity so results match on meaning rather than exact keywords."
tags: [semantic-search, embeddings, vector-search, retrieval]
videos: [everything-you-thought-about-building-ai-agents-is-wrong, why-the-best-ai-coding-tools-abandoned-rag-and-what-they-use-instead, the-simplest-rag-stack-that-actually-works-complete-guide, every-rag-strategy-explained-in-13-minutes-no-fluff, your-ultimate-n8n-rag-ai-agent-template-just-got-a-massive-upgrade, all-the-best-rag-strategies-in-one-mcp-for-ai-coding-assistants, you-have-to-try-agentic-rag-with-deepseek-r1-insane-results, the-future-of-rag-is-agentic-learn-this-strategy-now, the-most-value-packed-rag-guide-on-youtube-feat-llama-31-405b]
created: 2026-07-21
updated: 2026-07-21
---

# Semantic Search

Semantic search retrieves content by meaning rather than by exact words. It embeds both the query and the stored text into vectors, then returns the chunks whose vectors are mathematically closest. The trade is captured well: "it's more of a conceptual search. And so we're able to find concepts and related ideas, but we aren't guaranteed to find exact terms" (the-simplest-rag-stack, 0:05:52). That conceptual reach is its whole appeal, "if we search for king, we will find records that mention queens as well. Berlin will find Germany. Microservices will find architecture. Cheap flights will find affordable airfare" (the-simplest-rag-stack, 0:12:07).

## How it works

An embedding model converts text into a vector, and similarity math scores how close two vectors are: "we can use cosign similarity or other mathematical functions to determine how similar one text is to another in this case it'd be how similar a user question is to a specific chunk of text" (most-value-packed-rag, 0:02:00). Retrieval returns the closest chunks, "match it with the most relevant knowledge that has this most similar Vector to the user question and then return the top K similar chunks so maybe you're going to give the five most similar chunks" (most-value-packed-rag, 0:02:32). The quality of results rides entirely on the embedding model's grasp of meaning: "we're relying on the embedding model to capture that semantic similarity" (why-ai-coding-abandoned-rag, 0:03:38).

## Why it matters

For years semantic search was synonymous with retrieval itself. "In 2024, no one really questioned rag. Pretty much every single agent was using semantic search as a way to access external information" (everything-you-thought-is-wrong, 0:13:21). Cole still leans on it heavily, "For a lot of my AI agents, I'm still spending a good amount of time in my database trying different rag strategies, building around semantic search" (everything-you-thought-is-wrong, 0:15:01). In basic RAG the two are the same thing: "rag itself is semantic search. It's not doing exact keyword matching" (all-the-best-rag-strategies, 0:10:45).

## Contrasts with

- [Keyword Search](./keyword-search.md) is the exact-match counterpart. Semantic search finds conceptually similar text but can miss literal terms; keyword search does the reverse. The classic failure: "If I simply search Star Wars spaceships there is no way that we're going to get every reference to the X-wing or the TIE fighter because it is conceptually similar to our search" (why-ai-coding-abandoned-rag, 0:03:05).
- [Hybrid Search](./hybrid-search.md) resolves the trade-off by running both and merging results (all-the-best-rag-strategies, 0:12:59).

## Builds on

- [Vector Embeddings](./vector-embeddings.md) are the representation semantic search operates on.
- [Chunking](./chunking.md) determines what units get embedded and returned.

## Related

- [Retrieval-Augmented Generation (RAG)](./rag.md) is the pipeline semantic search powers; [Traditional RAG](./traditional-rag.md) is the one-shot semantic-search baseline.
- [Reranking](./reranking.md) and [Query Expansion](./query-expansion.md) improve the precision and recall of semantic retrieval.
- [Agentic RAG](./agentic-rag.md) lets an agent choose semantic search among other tools: "maybe it can do a classic semantic search, but also if it wants to, it can read the entire text of a single document" (every-rag-strategy, 0:03:32).
- [Knowledge Bases](./knowledge-bases.md) and [Memory Systems](./memory-systems.md) are built on semantic retrieval; mem0-style memory searches "the most relevant memories" this way (build-ai-agents-that-evolve, 0:08:09).
- [Structured vs Unstructured Data](./structured-vs-unstructured-data.md) frames when embedding-based search fits and when it does not.
- [Oracle AI Database](../entities/tools/oracle-ai-database.md) - The video's sponsor; a unified AI database with built-in embeddings and semantic, keyword, and knowledge-graph search in one place, used for Cole's agentic RAG demo.

## Sources

- [The Simplest RAG Stack That Actually Works (Complete Guide)](../sources/the-simplest-rag-stack-that-actually-works-complete-guide.md) - "[0:12:07] if we search for king, we will find records that mention queens as well. Berlin will find Germany. Microservices will find architecture. Cheap flights will find affordable airfare"
- [Why the Best AI Coding Tools Abandoned RAG (And What They Use Instead)](../sources/why-the-best-ai-coding-tools-abandoned-rag-and-what-they-use-instead.md) - "[0:03:05] If I simply search Star Wars spaceships there is no way that we're going to get every reference to the X-wing or the TIE fighter or the Millennium Falcon because it is conceptually similar to our search."
- [Everything You Thought About Building AI Agents is Wrong](../sources/everything-you-thought-about-building-ai-agents-is-wrong.md) - "[0:13:21] in 2024, no one really questioned rag. Pretty much every single agent was using semantic search as a way to access external information"
- [All the BEST RAG Strategies in ONE MCP for AI Coding Assistants](../sources/all-the-best-rag-strategies-in-one-mcp-for-ai-coding-assistants.md) - "[0:10:45] Because rag itself is semantic search. It's not doing exact keyword matching."
- [The Most Value Packed RAG Guide on YouTube (Feat. Llama 3.1 405B!)](../sources/the-most-value-packed-rag-guide-on-youtube-feat-llama-31-405b.md) - "[0:02:32] match it with the most relevant knowledge that has this most similar Vector to the user question and then return the top K similar chunks so maybe you're going to give the five most similar chunks"
- [Every RAG Strategy Explained in 13 Minutes (No Fluff)](../sources/every-rag-strategy-explained-in-13-minutes-no-fluff.md) - "[0:03:32] maybe it can do a classic semantic search, but also if it wants to, it can read the entire text of a single document"
- [Your ULTIMATE n8n RAG AI Agent Template just got a Massive Upgrade](../sources/your-ultimate-n8n-rag-ai-agent-template-just-got-a-massive-upgrade.md) - "[0:17:02] we're using the semantic similarity search tool. That's the classic rag search that we've had throughout all the iterations of our template here."
- [You HAVE to Try Agentic RAG with DeepSeek R1 (Insane Results)](../sources/you-have-to-try-agentic-rag-with-deepseek-r1-insane-results.md) - "[0:09:53] the first thing that we need is an embedding model CU we have to take the user query and embed it and then match it against relevant context in the vector database"
- [The Future of RAG is Agentic - Learn this Strategy NOW](../sources/the-future-of-rag-is-agentic-learn-this-strategy-now.md) - "[0:03:36] using some mathematics under the hood some Vector math the query is essentially matched to the most relevant documents that are then given as context to the llm"
