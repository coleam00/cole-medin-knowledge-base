---
type: concept
title: "Delete-Before-Insert Re-Ingestion"
description: "Because most vector stores insert rather than upsert, you must delete a document's existing chunks (matched by file ID metadata) before re-inserting an updated version, or stale chunks linger forever."
tags: [ingestion, data-hygiene, rag, vector-database, gotcha]
videos: [the-ultimate-n8n-rag-ai-agent-template-local-ai-edition, effortless-rag-in-n8n-use-all-your-files-pdfs-excel-and-more, run-all-your-ai-locally-in-minutes-llms-rag-and-more, this-rag-ai-agent-with-n8n-supabase-is-the-real-deal]
created: 2026-07-21
updated: 2026-07-21
---

# Delete-Before-Insert Re-Ingestion

Delete-before-insert re-ingestion is the discipline of wiping every chunk a knowledge base already holds for a document before writing the new version of that document. It exists because vector-store write nodes are almost never upserts: "when you have this inserter it is not an upsert it is just an insert and so what that means is if you reinsert a document you're actually going to have duplicate vectors for that document" [0:14:18]. So the first step of any ingestion run is a wipe, not a write: "before I even insert anything into the knowledge base is I want a clean slate if we have already added the file to the knowledge base at some point I want to delete everything" [0:18:25].

## Why it matters

Without the delete step, a re-ingested file leaves both its old and new chunks in the store, and retrieval will hand the model both. Stale vectors are worse than missing ones: "we want to delete all of the old records in our Vector store for this document... to make sure that we don't have old versions of it in the knowledge base because that will confuse the llm a lot" [0:06:19]. The goal is an absolute guarantee that "when I update a file the knowledge base only only contains the updated information for that file and doesn't have anything from an old version hanging around" [0:18:39]. Cole flags it as a widespread omission: "this is another big thing that a lot of n8n tutorials miss out on" [0:12:27].

## How it works

The mechanism is metadata, not content matching. Every chunk carries its source document's file ID, so deletion is a metadata query: "any Vector that has the file ID of the current Google drive file that we are updating as a part of the metadata we're going to delete it" [0:13:33]. The same shape holds in code against a different store, using LangChain to "connect to my quadrant Vector store get all of the vector IDs where the metadata file ID is equal to the ID of the file I'm currently ingesting and then it just deletes those vectors" [0:15:05]. Stamping a stable file ID during ingestion is therefore a hard requirement, and the pattern generalizes across every store: "superbase and all the other options for Vector databases in n8n they are not upserts it won't update a vector if it already exists" [0:12:44].

## Prerequisites

- [Vector Embeddings](./vector-embeddings.md) - the chunk vectors being written and removed.
- [Chunking](./chunking.md) - one document becomes many rows, which is why deletion must be by document, not by row.
- [Metadata Filtering](./metadata-filtering.md) - the file ID metadata that makes targeted deletion possible.

## Part of

- [Production-Ready RAG](./production-ready-rag.md) - a non-negotiable hygiene step in any pipeline that re-ingests changing files.
- [Knowledge Bases](./knowledge-bases.md) - keeps the base a mirror of the source of truth rather than an append-only pile.

## Contrasts with

- [Temporal Knowledge Graphs](./temporal-knowledge-graphs.md) - handles changing facts by invalidating them over time instead of destroying and rewriting the old representation.

## Related

- [Retrieval-Augmented Generation (RAG)](./rag.md) - the retrieval quality this protects.
- [Web Crawling & Ingestion](./web-crawling.md) - re-crawls hit the same duplicate-vector trap.
- [Agentic RAG](./agentic-rag.md) - agent-driven retrieval amplifies the damage of contradictory stale chunks.

## Tools

- [n8n](../entities/tools/n8n.md) - the delete node runs ahead of the insert node in every one of Cole's RAG templates.
- [Supabase](../entities/tools/supabase.md) and [Postgres](../entities/tools/postgres-pgvector.md) - insert-only vector tables that require the explicit delete.
- [Qdrant](../entities/tools/qdrant.md) - deleted by metadata file ID via [LangChain](../entities/tools/langchain.md) in the local-first version of the pipeline.
- [Google Drive](../entities/tools/google-drive.md) - the file ID source that keys the delete.

## Sources

- [Run ALL Your AI Locally in Minutes (LLMs, RAG, and more)](../sources/run-all-your-ai-locally-in-minutes-llms-rag-and-more.md) - "[0:14:18] when you have this inserter it is not an upsert it is just an insert and so what that means is if you reinsert a document you're actually going to have duplicate vectors for that document"
- [Run ALL Your AI Locally in Minutes (LLMs, RAG, and more)](../sources/run-all-your-ai-locally-in-minutes-llms-rag-and-more.md) - "[0:15:05] uses Lang chain to connect to my quadrant Vector store get all of the vector IDs where the metadata file ID is equal to the ID of the file I'm currently ingesting and then it just deletes those vectors"
- [The ULTIMATE n8n RAG AI Agent Template - Local AI Edition](../sources/the-ultimate-n8n-rag-ai-agent-template-local-ai-edition.md) - "[0:18:25] before I even insert anything into the knowledge base is I want a clean slate if we have already added the file to the knowledge base at some point I want to delete everything"
- [The ULTIMATE n8n RAG AI Agent Template - Local AI Edition](../sources/the-ultimate-n8n-rag-ai-agent-template-local-ai-edition.md) - "[0:18:39] I want to absolutely guarantee that when I update a file the knowledge base only only contains the updated information for that file and doesn't have anything from an old version hanging around"
- [Effortless RAG in n8n - Use ALL Your Files (PDFs, Excel, and More)](../sources/effortless-rag-in-n8n-use-all-your-files-pdfs-excel-and-more.md) - "[0:06:19] we want to delete all of the old records in our Vector store for this document because that way we're going to get a fresh set of vectors for this document to make sure that we don't have old versions of it in the knowledge base because that will confuse the llm a lot"
- [This RAG AI Agent with n8n + Supabase is the Real Deal](../sources/this-rag-ai-agent-with-n8n-supabase-is-the-real-deal.md) - "[0:12:44] superbase and all the other options for Vector databases in n8n they are not upserts it won't update a vector if it already exists"
- [This RAG AI Agent with n8n + Supabase is the Real Deal](../sources/this-rag-ai-agent-with-n8n-supabase-is-the-real-deal.md) - "[0:13:33] any Vector that has the file ID of the current Google drive file that we are updating as a part of the metadata we're going to delete it"
