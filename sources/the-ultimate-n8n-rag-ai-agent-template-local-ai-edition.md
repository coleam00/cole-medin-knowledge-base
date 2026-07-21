---
type: source
title: "The ULTIMATE n8n RAG AI Agent Template - Local AI Edition"
description: "Agentic RAG, giving an agent tools to explore a knowledge base in multiple ways instead of a single one-shot vector lookup, can run 100% locally and offline in n8n using Ollama and self-hosted Postgres/Supabase."
youtube_id: T2QWhXpnT5I
url: https://www.youtube.com/watch?v=T2QWhXpnT5I
slug: the-ultimate-n8n-rag-ai-agent-template-local-ai-edition
published: 2025-03-05
duration: "0:32:41"
recency_rank: 112
raw: "../raw/the-ultimate-n8n-rag-ai-agent-template-local-ai-edition.md"
tags: [agentic-rag, n8n, local-ai, ollama]
created: 2026-07-21
updated: 2026-07-21
---

# The ULTIMATE n8n RAG AI Agent Template - Local AI Edition

Driven by overwhelming viewer demand for an offline build, Cole ports his n8n agentic RAG template to run entirely on local AI. He first re-draws the distinction between naive/traditional RAG (documents are chunked, embedded, stored in a vector DB, and matched to a query vector in one shot) and agentic RAG (the agent comes first and is handed tools so it can reason about how to explore the knowledge base). Those tools let it do basic RAG lookups, list documents, read full file contents, or write SQL against tabular data. The local build keeps the cloud template's structure but swaps in local services: Ollama for the LLM (Qwen 2.5 14B) and embeddings (nomic-embed-text), plus self-hosted Postgres/Supabase for storage.

He demonstrates three tool paths. A simple RAG lookup answers "who is the CEO." A document-listing and full-read path answers "who attended the Feb 12 meeting," which naive RAG often gets wrong because the attendee and date chunks land far apart. A SQL path computes an average rating (7.89), which RAG fails at because chunks capture only part of a table and LLMs are poor at math. CSV and Excel rows are stored in a single `document_rows` table using a JSONB `row_data` column so any table structure fits, and each spreadsheet's schema is recorded in the document metadata so the LLM knows which columns exist for its SQL.

The setup covers building the tables, a RAG ingestion pipeline triggered by a local-file watcher (extracting text per file type via a switch node, deleting old records for a clean slate on re-ingest, chunking at size 400 with metadata for source citation), and the agent itself. Cole closes with two local-AI gotchas. First, n8n's Chat Ollama node throws an "expected string, received object" error on the RAG tool, so you must point the OpenAI node at Ollama's base URL instead. Second, Ollama models default to a 2000-token context that silently truncates system prompts, fixed by creating a custom Ollama model file that inherits the base model and sets an 8000-token context length.

## Concepts covered

- [Agentic RAG](../concepts/agentic-rag.md)
- [Traditional RAG](../concepts/traditional-rag.md)
- [Retrieval-Augmented Generation (RAG)](../concepts/rag.md)
- [Structured vs Unstructured Data](../concepts/structured-vs-unstructured-data.md)
- [Chunking](../concepts/chunking.md)
- [Vector Embeddings](../concepts/vector-embeddings.md)
- [Local & Self-Hosted AI](../concepts/local-ai.md)
- [Web Crawling & Ingestion](../concepts/web-crawling.md)
- [Context Window Limits](../concepts/context-window-limits.md)

## Entities

- [n8n](../entities/tools/n8n.md)
- [Ollama](../entities/tools/ollama.md)
- [Postgres / pgvector](../entities/tools/postgres-pgvector.md)
- [Supabase](../entities/tools/supabase.md)
- [Qwen](../entities/tools/qwen.md)
- [nomic-embed-text](../entities/tools/nomic-embed-text.md)
- [Weaviate](../entities/organizations/weaviate.md)
- [Cartesia](../entities/organizations/cartesia.md)
- [Cole Medin](../entities/people/cole-medin.md)

## Key moments

- **[0:00:00]** Intro: RAG alone is often not powerful enough; agentic RAG levels it up, now in a 100% local edition
- **[0:01:47]** Explains naive/traditional RAG using a Weaviate article and diagram: chunk, embed, store, match query vector, one-shot retrieval
- **[0:03:15]** Limitation of naive RAG: it is one-shot, the LLM never gets to reason about how to explore the knowledge base
- **[0:03:28]** Agentic RAG diagram: agent comes first with tools, can search multiple vector DBs and use web search
- **[0:04:39]** Shows the full local n8n template, Ollama + self-hosted Supabase, kept similar to the cloud version
- **[0:05:57]** Test 1: basic RAG lookup, who is the CEO, uses the simple rag tool
- **[0:06:57]** Test 2: who was in the Feb 12 meeting, agent lists documents then reads full file (RAG often fails this)
- **[0:08:13]** Test 3: tabular data, agent writes a SQL query to compute average overall rating (7.89)
- **[0:10:46]** Sponsor read: Cartesia voice AI / Sonic 2.0
- **[0:12:59]** Database setup: nodes to create tables; document_metadata table stores high-level doc info + schema
- **[0:14:43]** document_rows table stores all tabular records in one JSONB row_data column regardless of structure
- **[0:15:33]** documents_pg table stores embeddings; PG Vector node auto-creates it (text column differs from Supabase node)
- **[0:16:33]** RAG pipeline: local file trigger watches a mounted folder, loops per file
- **[0:18:25]** Delete old records first for a clean slate so updated files never leave stale data to hallucinate on
- **[0:19:41]** Per-file-type text extraction via switch node (PDF/CSV/text); recursive splitter chunk size 400
- **[0:22:11]** CSV/Excel path: insert rows into document_rows AND summarize into RAG, then set the schema
- **[0:24:09]** Agent setup: chat trigger + webhook, tools agent, Postgres chat memory
- **[0:25:05]** Gotcha 1: use the OpenAI node pointed at Ollama base URL (dummy key), not the Chat Ollama node
- **[0:25:38]** Chat Ollama node throws "expected string but received object" on the RAG tool invocation
- **[0:28:29]** Gotcha 2: Ollama's default 2000-token context truncates the system prompt and tool instructions
- **[0:29:35]** Fix: create an Ollama model file inheriting the base model with an 8000-token context parameter

## Transcript

[Raw transcript](../raw/the-ultimate-n8n-rag-ai-agent-template-local-ai-edition.md)
