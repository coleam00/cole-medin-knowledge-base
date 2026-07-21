---
type: concept
title: "Knowledge Graphs"
description: "Structuring knowledge as entities and relationships (often temporal) so agents can traverse connections a vector store can't express."
tags: [graph, entities, temporal]
videos: [finally-an-open-standard-for-the-karpathy-llm-wiki-is-here, i-built-self-evolving-claude-code-memory-w-karpathys-llm-knowledge-bases, the-only-ai-tech-stack-you-need-in-2026, every-rag-strategy-explained-in-13-minutes-no-fluff, knowledge-graphs-in-n8n-are-finally-here, introducing-rag-20-agentic-rag-knowledge-graphs-free-template, ai-code-that-fixes-itself-an-mcp-you-can-try-now, all-the-best-rag-strategies-in-one-mcp-for-ai-coding-assistants, make-rag-100x-better-with-real-time-knowledge-graphs, the-proven-solution-for-unbelievable-rag-performance-lightrag-guide, build-ai-agents-that-evolve-over-time]
created: 2026-07-21
updated: 2026-07-21
---

# Knowledge Graphs

A knowledge graph stores knowledge as entities and the relationships between them, so an agent can navigate connections instead of only matching similar text. "think about people, companies, products, all of these entities we have in our data. They're very related to each other. And so we want to be able to store those relationships and give our agent the ability to actually navigate between these different nodes" - ["Knowledge Graphs in n8n are FINALLY Here!"](../sources/knowledge-graphs-in-n8n-are-finally-here.md) [0:02:21]. That traversal is the whole point: "we can look at a company and then we can from there go and search and find the executive leadership team as an example" [0:02:36], or see that "Amazon relates to anthropic because Amazon has invested into anthropic" - ["Introducing RAG 2.0: Agentic RAG + Knowledge Graphs"](../sources/introducing-rag-20-agentic-rag-knowledge-graphs-free-template.md) [0:02:24].

## How it works

A knowledge graph has two parts, and it needs an LLM to populate it. "for knowledge graphs, there's really two parts. We have the graph database and then generally you're going to use some kind of library to help you insert data and search through data" - ["The ONLY AI Tech Stack You Need in 2026"](../sources/the-only-ai-tech-stack-you-need-in-2026.md) [0:15:24]. The database is typically [Neo4j](../entities/tools/neo4j.md), and the library is what turns raw text into nodes and edges: "we need to use a large language model to extract entities and relationships from raw text and that is what Graphiti helps us with." [0:16:46]. In practice knowledge graphs sit beside vector search rather than replacing it: "We're combining traditional vector search... with a new type of database, a graph database that stores entity relationships." - ["Every RAG Strategy Explained in 13 Minutes"](../sources/every-rag-strategy-explained-in-13-minutes-no-fluff.md) [0:04:48].

## Temporal awareness

The strongest case for graphs is data that changes over time. [Graphiti](../entities/tools/graphiti.md) is "a layer on top of rag that is meant for constantly ingesting everchanging data, also keeping a historical record of how your data has changed" - ["Make RAG 100x Better with Real-Time Knowledge Graphs"](../sources/make-rag-100x-better-with-real-time-knowledge-graphs.md) [0:00:51], which is exactly where traditional RAG struggles, since updating a vector store means reinserting documents. This temporal, relational structure is why "knowledge graphs in general are just a lot more powerful than traditional rag." [0:03:05].

> **Contradiction:** Power comes at a cost, and the videos are candid about the tradeoff rather than one-sidedly bullish. Graphs are "fantastic for interconnected data. But just keep in mind since we're usually using an LLM to extract from documents. It's going to be a lot slower and more expensive" - [Every RAG Strategy Explained in 13 Minutes](../sources/every-rag-strategy-explained-in-13-minutes-no-fluff.md) [0:05:14], 2026-07-21. Treat the "100x better / more powerful" framing and the "slower and more expensive" caveat as two sides of the same design decision.

## Builds on

- [Retrieval-Augmented Generation (RAG)](./rag.md) - the retrieval base a graph layer augments.
- [Knowledge Bases](./knowledge-bases.md) - the curated corpus a graph is extracted from.

## Contrasts with

- [Traditional RAG](./traditional-rag.md) - pure vector similarity, which "often struggles to connect different documents together" where a graph excels. [LightRAG](../entities/tools/lightrag.md) "not only vectorizes your documents like traditional rag. It also builds up an all-important graph that connects topics, ideas, concepts together" - ["The PROVEN Solution for Unbelievable RAG Performance (LightRAG Guide)"](../sources/the-proven-solution-for-unbelievable-rag-performance-lightrag-guide.md) [0:01:27].

## Related

- [Temporal-Aware Knowledge Graphs](./temporal-knowledge-graphs.md) - a knowledge graph that never overwrites a changed fact but stores the new one alongside the old with valid_at/invalidated_at timestamps, so an agent knows both what is true now and how the knowledge evolved.
- [Agentic RAG](./agentic-rag.md) - combining graph traversal with agent-driven retrieval strategy.
- [Memory Systems](./memory-systems.md) - a graph backend makes long-term memory relational and time-aware.
- [The LLM Wiki](./the-llm-wiki.md) - wiki back-links let an agent "traverse through our wiki like a knowledge graph." - ["Finally, an Open Standard for the Karpathy LLM Wiki is HERE"](../sources/finally-an-open-standard-for-the-karpathy-llm-wiki-is-here.md) [0:03:27].
- [Second Brain](./second-brain.md) - Obsidian's graph view is the same idea for personal notes.
- [Structured vs Unstructured Data](./structured-vs-unstructured-data.md) - graphs impose structure on otherwise unstructured text.
- [Codebase Indexing](./codebase-indexing.md) - an entire repo turned relational and queryable as a graph.
- [Model Selection](./model-selection.md) / [Reranking](./reranking.md) / [Progressive Disclosure](./progressive-disclosure.md) - retrieval-quality levers that apply alongside graph search.
- [Hallucination Detection](./hallucination-detection.md) - Deterministically checking AI-generated code against a ground-truth structure (a parsed knowledge graph of the library) to flag methods and parameters that don't actually exist, then feeding the report back so the agent can fix them.

## Tools

- [Neo4j](../entities/tools/neo4j.md) - the graph database engine behind the scenes.
- [Graphiti](../entities/tools/graphiti.md) - extracts entities and relationships and maintains temporal history.
- [LightRAG](../entities/tools/lightrag.md) - combines vector and graph indexing in one library.
- [GraphRAG](../entities/tools/graphrag.md) - A popular knowledge-graph RAG implementation Cole groups with LightRAG as built for static, rarely-changing document summarization rather than dynamic incrementally-updated data.
- [Mem0](../entities/tools/mem0.md) - memory that can be extended with a graph knowledge implementation.
- [n8n](../entities/tools/n8n.md) - no-code knowledge-graph construction.

## Sources

- [Knowledge Graphs in n8n are FINALLY Here!](../sources/knowledge-graphs-in-n8n-are-finally-here.md) - "[0:02:21] think about people, companies, products, all of these entities we have in our data. They're very related to each other. And so we want to be able to store those relationships and give our agent the ability to actually navigate between these different nodes"
- [The ONLY AI Tech Stack You Need in 2026](../sources/the-only-ai-tech-stack-you-need-in-2026.md) - "[0:16:46] we need to use a large language model to extract entities and relationships from raw text and that is what Graphiti helps us with."
- [Make RAG 100x Better with Real-Time Knowledge Graphs](../sources/make-rag-100x-better-with-real-time-knowledge-graphs.md) - "[0:00:51] it's a layer on top of rag that is meant for constantly ingesting everchanging data, also keeping a historical record of how your data has changed"
- [Every RAG Strategy Explained in 13 Minutes (No Fluff)](../sources/every-rag-strategy-explained-in-13-minutes-no-fluff.md) - "[0:05:14] knowledge graphs are fantastic for interconnected data. But just keep in mind since we're usually using an LLM to extract from documents. It's going to be a lot slower and more expensive"
- [The PROVEN Solution for Unbelievable RAG Performance (LightRAG Guide)](../sources/the-proven-solution-for-unbelievable-rag-performance-lightrag-guide.md) - "[0:01:27] Light rag not only vectorizes your documents like traditional rag. It also builds up an all-important graph that connects topics, ideas, concepts together"
- [Introducing RAG 2.0: Agentic RAG + Knowledge Graphs (FREE Template)](../sources/introducing-rag-20-agentic-rag-knowledge-graphs-free-template.md) - "[0:02:11] I also have it in my knowledge graph. So I'm representing information in a different way very relationally here to give the agent the ability to explore the knowledge in a different way."
- [Finally, an Open Standard for the Karpathy LLM Wiki is HERE](../sources/finally-an-open-standard-for-the-karpathy-llm-wiki-is-here.md) - "[0:03:27] This is one of the most important things to let the agent traverse through our wiki like a knowledge graph."
- [I Built Self-Evolving Claude Code Memory w/ Karpathy's LLM Knowledge Bases](../sources/i-built-self-evolving-claude-code-memory-w-karpathys-llm-knowledge-bases.md) - "[0:04:14] this is powerful because it gives our agent the ability to traverse through the graph to search better and even connect different pieces of knowledge together to give us a more comprehensive answer"
- [AI Code That Fixes Itself (An MCP You Can Try Now)](../sources/ai-code-that-fixes-itself-an-mcp-you-can-try-now.md) - "[0:01:44] I have taken the entire repository in GitHub for Pydantic AI... and I have turned it into a knowledge graph that can be queried by AI coding assistance."
- [Build AI Agents that EVOLVE Over Time](../sources/build-ai-agents-that-evolve-over-time.md) - "[0:22:42] you can take mem even further as well with a graph knowledge implementation... you can store entities and relations as well to make it even more powerful"
