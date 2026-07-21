---
type: source
title: "Effortless RAG in n8n - Use ALL Your Files (PDFs, Excel, and More)"
description: "The hardest part of building a RAG agent in n8n is not the vector store but reliably extracting text from varied file types, which you solve by branching on a file's MIME type to a matching extract node."
youtube_id: T1ZKEmDN8AA
url: https://www.youtube.com/watch?v=T1ZKEmDN8AA
slug: effortless-rag-in-n8n-use-all-your-files-pdfs-excel-and-more
published: 2024-10-09
duration: "0:18:18"
recency_rank: 155
raw: "../raw/effortless-rag-in-n8n-use-all-your-files-pdfs-excel-and-more.md"
tags: [rag, n8n, document-extraction, no-code]
created: 2026-07-21
updated: 2026-07-21
---

# Effortless RAG in n8n - Use ALL Your Files (PDFs, Excel, and More)

Cole extends a previously-built n8n RAG AI agent so its knowledge base can ingest not just plain text and Google Docs but PDFs, Excel spreadsheets, and virtually any other file type. He argues the vector-store side of RAG (Supabase/pgvector plus OpenAI embeddings) is already easy and works well; the genuine friction is extracting clean raw text from documents that don't convert trivially, because n8n has no single universal extract-from-any-file node.

The solution is a MIME-type router. A Google Drive trigger fires when a file is created or updated in a watched folder; the trigger output exposes a `mimeType` parameter (for example `application/pdf`, the xlsx notation, or `application/vnd.google-apps.document`) that Cole captures into a file-type field. Before re-ingesting he deletes the document's old vectors so stale versions don't confuse the LLM, downloads the binary onto the n8n instance, then feeds a Switch node that routes to a dedicated extract node per type: extract-from-PDF, extract-from-xlsx, or a raw-text extractor as the default fallback for Google Docs, CSVs, markdown, and text files.

He flags a key gotcha: different extract nodes write their output to different fields (raw text goes to `data`, PDF extraction goes to `text`, the Excel path summarizes/concatenates to a `concatenated data` field), so the document loader that chunks the text must reference the correct attribute, using JavaScript fallback expressions to try each. For Excel he keeps it simple by aggregating all rows into a single string and chunking it like raw text, while noting there are many use-case-dependent strategies. He closes by uploading a PDF and Excel file, watching the Switch pick the right branch, inserting the resulting chunks into the Supabase vector store, and querying the agent to confirm it retrieves answers from the PDF.

## Concepts covered

- [Retrieval-Augmented Generation (RAG)](../concepts/rag.md)
- [Web Crawling & Ingestion](../concepts/web-crawling.md)
- [Vector Embeddings](../concepts/vector-embeddings.md)
- [Chunking](../concepts/chunking.md)
- [Structured vs Unstructured Data](../concepts/structured-vs-unstructured-data.md)
- [Structured Outputs](../concepts/structured-outputs.md)
- [Knowledge Bases](../concepts/knowledge-bases.md)
- [Agent Protocols](../concepts/agent-protocols.md)

## Entities

- [n8n](../entities/tools/n8n.md)
- [Supabase](../entities/tools/supabase.md)
- [OpenAI](../entities/organizations/openai.md)
- [Google Drive](../entities/tools/google-drive.md)
- [Cole Medin](../entities/people/cole-medin.md)

## Key moments

- **[0:00:00]** Premise: n8n makes RAG agents easy; the hard part is extracting text from documents like PDFs
- **[0:01:34]** Overview of the existing RAG agent workflow being extended
- **[0:02:44]** Two triggers: chat input and a webhook (agent usable as an API)
- **[0:03:27]** Agent stack: GPT-4o mini, Supabase Postgres chat history, retrieve-documents tool plus Supabase vector store, OpenAI embeddings
- **[0:04:47]** Google Drive triggers on file created/updated in a watched folder, polled every minute
- **[0:05:27]** MIME type identifies the file type (application/vnd.google-apps.document for a Google Doc)
- **[0:06:19]** Delete old vectors for the document to avoid stale versions confusing the LLM
- **[0:07:35]** The extract-from-file node has many variants (PDF, Excel, HTML, JSON) for different types
- **[0:08:10]** Switch node routes on file-type/MIME to the correct extract node, with a raw-text default fallback
- **[0:09:46]** Google workspace MIME-type reference doc for extending to more file types
- **[0:12:42]** Running a PDF: extract-from-PDF outputs to a 'text' field, not 'data'
- **[0:13:01]** Golden nugget: document loader's data field must match the extract node's output attribute; use JS fallbacks
- **[0:15:22]** Excel path: aggregate rows into one string, treat the whole sheet as raw text to chunk
- **[0:17:06]** Query the agent about the PDF; it retrieves the right chunks and answers correctly

## Transcript

[Raw transcript](../raw/effortless-rag-in-n8n-use-all-your-files-pdfs-excel-and-more.md)
