---
type: source
title: "Your ULTIMATE n8n RAG AI Agent Template just got a Massive Upgrade"
description: "A basic RAG implementation is not enough; combining agentic chunking, agentic RAG, and reranking into a single n8n template solves both the knowledge-curation and knowledge-search halves of RAG."
youtube_id: iV5RZ_XKXBc
url: https://www.youtube.com/watch?v=iV5RZ_XKXBc
slug: your-ultimate-n8n-rag-ai-agent-template-just-got-a-massive-upgrade
published: 2025-09-03
duration: "0:19:20"
recency_rank: 72
raw: "../raw/your-ultimate-n8n-rag-ai-agent-template-just-got-a-massive-upgrade.md"
tags: [rag, n8n, retrieval]
created: 2026-07-21
updated: 2026-07-21
---

# Your ULTIMATE n8n RAG AI Agent Template just got a Massive Upgrade

Cole walks through the latest evolution of his n8n RAG agent template, arguing that basic RAG only seems fundamentally flawed because people are not strategic about it. Every RAG system has two components: the pipeline that chunks and curates documents into a knowledge base, and the agent tools that search that knowledge base. If either half is weak, the whole agent falls apart, so the upgraded template attacks both at once.

Three strategies anchor the upgrade. Agentic chunking uses an LLM (via n8n's LangChain code node, itself built with Claude Code) to decide where to split documents so complete ideas stay together, fixing the context loss caused by fixed-size character splitting or even semantic chunking. Agentic RAG gives the agent multiple ways to explore the knowledge base, tuned through its system prompt: SQL queries over tabular data stored row by row, listing document metadata, and pulling an entire short document instead of scattered chunks. Reranking uses a dedicated Cohere reranker model to pull a large candidate set of 25 chunks and then filter to the top four, avoiding both the limitation of only ever fetching four chunks and the hallucination risk of dumping 25 into the LLM.

Throughout, Cole stresses flexibility and adaptation. The template runs on any Postgres (he uses Neon), the chunking prompt can be tuned per use case, and viewers are invited to extend it further with knowledge graphs or contextual embedding. This is a system meant to evolve, not a fixed recipe.

## Concepts covered

- [Retrieval-Augmented Generation (RAG)](../concepts/rag.md)
- [Chunking](../concepts/chunking.md)
- [Context-Aware Chunking](../concepts/context-aware-chunking.md)
- [Agentic RAG](../concepts/agentic-rag.md)
- [Structured vs Unstructured Data](../concepts/structured-vs-unstructured-data.md)
- [Reranking](../concepts/reranking.md)
- [Semantic Search](../concepts/semantic-search.md)
- [Knowledge Bases](../concepts/knowledge-bases.md)
- [System Evolution](../concepts/system-evolution.md)

## Entities

- [n8n](../entities/tools/n8n.md)
- [Neon](../entities/tools/neon.md)
- [Postgres](../entities/tools/postgres-pgvector.md)
- [Cohere](../entities/organizations/cohere.md)
- [Claude Code](../entities/tools/claude-code.md)
- [Google Drive](../entities/tools/google-drive.md)
- [Archon](../entities/tools/archon.md)
- [Cole Medin](../entities/people/cole-medin.md)

## Key moments

- **[0:01:03]** Every RAG implementation has two components: the pipeline (chunk/curate) and the agent search tools
- **[0:02:50]** Three strategies covered: agentic chunking, agentic RAG, reranking
- **[0:03:31]** Agentic chunking explained: an LLM decides split points to keep ideas together
- **[0:06:38]** Built agentic chunking in n8n's LangChain code node using Claude Code
- **[0:10:59]** Agentic RAG: give the agent multiple search modes tuned by the system prompt
- **[0:11:46]** Tabular data stored row-by-row so the agent can run SQL sums/averages
- **[0:13:12]** Document metadata table lets the agent pull an entire short document
- **[0:15:41]** Reranking: Cohere reranker takes 25 chunks, returns the top 4

## Transcript

[Raw transcript](../raw/your-ultimate-n8n-rag-ai-agent-template-just-got-a-massive-upgrade.md)

## Sources

- [Your ULTIMATE n8n RAG AI Agent Template just got a Massive Upgrade](./your-ultimate-n8n-rag-ai-agent-template-just-got-a-massive-upgrade.md) - "[0:01:03] Every RAG implementation has two components: the pipeline (chunk/curate) and the agent search tools"
