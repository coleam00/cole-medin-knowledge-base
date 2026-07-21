---
type: source
title: "I Built the ULTIMATE n8n RAG AI Agent Template"
description: "Traditional RAG fails because it can't zoom out to whole documents or do real data analysis, so give the agent multiple tools (RAG, list-documents, get-file-contents, SQL-over-tables) and let it reason about how to explore the knowledge base, which is agentic RAG in n8n."
youtube_id: mQt1hOjBH9o
url: https://www.youtube.com/watch?v=mQt1hOjBH9o
slug: i-built-the-ultimate-n8n-rag-ai-agent-template
published: 2025-02-26
duration: "0:34:03"
recency_rank: 114
raw: "../raw/i-built-the-ultimate-n8n-rag-ai-agent-template.md"
tags: [agentic-rag, n8n, supabase, sql]
created: 2026-07-21
updated: 2026-07-21
---

# I Built the ULTIMATE n8n RAG AI Agent Template

Cole argues that plain RAG often disappoints. A single vector lookup misses key context, pulls the wrong document even when the answer sits in the title, cannot stitch related documents together, and has no way to zoom out to an entire document or a set of documents unless they are tiny. It also has no concept of real data analysis, so you cannot reliably get sums or maximums over a spreadsheet when the lookup returns only a fraction of the chunks. His fix is agentic RAG: instead of arming the agent with a single RAG tool, give it several tools and let it reason about which to use for a given question.

The walkthrough builds a version-three n8n template backed by Supabase/Postgres with three tables. A `documents` table holds embeddings, metadata, and chunk contents for RAG. A `document_metadata` table holds high-level info like title and URL for source citation, plus each spreadsheet's schema. A `document_rows` table stores tabular data as flexible JSONB so CSV and Excel files can be queried with SQL without creating a dedicated table per file. The agent's toolbelt is RAG lookup (now citing sources via returned metadata), list-documents, get-file-contents (pull an entire file when RAG fails), and a SQL tool that queries the JSONB rows for real aggregations. The system prompt tells it to start with RAG, fall back to the other tools, and be honest when it cannot find the answer, which alone cuts hallucinations.

The RAG pipeline ingests from a Google Drive trigger (polling for created or updated files, looping to handle several files per minute), clears old data for a file before re-inserting to avoid stale chunks, and routes files through a type switch to the right extractor. For spreadsheets it does two things in parallel: insert each row into `document_rows` and aggregate the table into a text document that gets chunked and embedded like anything else. Embeddings use OpenAI text-embedding-3, LLMs use GPT-4o-mini, and Cole stresses that insert and retrieval must share the same embedding model. He frames it as a starting template to extend, not an out-of-the-box solution.

## Concepts covered

- [Agentic RAG](../concepts/agentic-rag.md)
- [Retrieval-Augmented Generation (RAG)](../concepts/rag.md)
- [When RAG Is (and Isn't) Dead](../concepts/when-rag-is-dead.md)
- [Structured vs Unstructured Data](../concepts/structured-vs-unstructured-data.md)
- [Agentic Search](../concepts/agentic-search.md)
- [Chunking](../concepts/chunking.md)
- [Vector Embeddings](../concepts/vector-embeddings.md)
- [Memory Systems](../concepts/memory-systems.md)
- [Knowledge Bases](../concepts/knowledge-bases.md)
- [Human in the Loop](../concepts/human-in-the-loop.md)

## Entities

- [n8n](../entities/tools/n8n.md)
- [Supabase](../entities/tools/supabase.md)
- [Postgres / pgvector](../entities/tools/postgres-pgvector.md)
- [OpenAI](../entities/organizations/openai.md)
- [Google Drive](../entities/tools/google-drive.md)
- [Anthropic](../entities/organizations/anthropic.md)
- [Cole Medin](../entities/people/cole-medin.md)

## Key moments

- **[0:00:18]** Why plain RAG sucks: lookups miss key context, pull wrong-date documents, can't connect documents
- **[0:01:05]** Two core RAG limitations: can't zoom out to whole documents, no concept of data analysis
- **[0:03:14]** Definition of agentic RAG: give agents the ability to reason about how they explore the knowledge base
- **[0:04:41]** Fallback pattern: when RAG fails, list documents and get full file contents instead
- **[0:04:55]** Query Excel/CSV files as SQL tables for sums and maximums RAG can't produce
- **[0:05:36]** Three-table Supabase schema: documents, document_metadata, document_rows
- **[0:06:34]** Demo: agent writes a SQL query to find the month with most new customers
- **[0:13:19]** Storing tabular rows as JSONB avoids creating a dedicated SQL table per file
- **[0:17:39]** Clear all old data for a file before re-inserting to avoid stale chunks
- **[0:24:25]** OpenAI text-embedding-3 for embeddings, GPT-4o-mini for the LLMs
- **[0:27:12]** System prompt: start with RAG, fall back to other tools, be honest when no answer
- **[0:32:36]** Live example: RAG fails to find employees, agent lists documents and finds the meeting minutes

## Transcript

[Raw transcript](../raw/i-built-the-ultimate-n8n-rag-ai-agent-template.md)
