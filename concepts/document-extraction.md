---
type: concept
title: "Document Extraction"
description: "Pulling clean raw text out of source files (PDFs, Excel, HTML, JSON) is the real bottleneck in RAG ingestion, solved by branching on each file's MIME type to a format-specific extractor rather than one universal node."
tags: [document-extraction, rag, ingestion]
videos: [turn-any-file-into-llm-knowledge-in-seconds, effortless-rag-in-n8n-use-all-your-files-pdfs-excel-and-more]
created: 2026-07-21
updated: 2026-07-21
---

# Document Extraction

Document extraction is the step that turns a source file into the clean raw text everything downstream depends on, and it is where most RAG pipelines actually break. Cole is blunt that it outranks the glamorous parts: "the hardest part of the whole setup is really just actually extracting the text from the documents that you want to put in your knowledge base especially if you want to use PDFs or other document types that don't convert as easily to Raw text" [0:00:00]. Embeddings, retrieval, and reranking are all downstream of this; garbage extraction poisons every one of them.

## Why one universal node fails

The naive pipeline uses a single extract-text node for everything, which quietly works only for the easy half of the world: "in the old workflow we have a single node that extracts the document text now the problem with this is it only works for file types where you can just extract the raw text... when we have more complex file types like Excel documents or PDF documents it's not that simple" [0:07:18]. A PDF carries layout, columns, and tables; a spreadsheet carries rows and headers with no prose at all. Flattening both through the same code path produces text that reads as noise to an embedding model.

## How it works

The fix is to branch. Ingestion inspects each file's MIME type and routes it to a format-specific extractor - one path for plain text and markdown, one for PDFs, one for spreadsheets that converts rows into text an LLM can read, one for HTML and JSON. The routing is mechanical, and libraries do it for you: "under the hood, it recognizes the file extension and it knows what to do to work with those different file types without us having to do that much more in our code." [0:06:19] That is the argument for reaching for a purpose-built tool rather than hand-rolling parsers: "It is a free and open-source tool I'm going to show you how to use today to work with all these complex data types so you can properly curate your data no matter how complex it is" [0:01:10].

## Part of

- [Production-Ready RAG](./production-ready-rag.md) - extraction is the first stage of the ingestion pipeline.
- [Knowledge Bases](./knowledge-bases.md) - the quality ceiling of a knowledge base is set here.

## Contrasts with

- [Web Crawling & Ingestion](./web-crawling.md) - crawlers usually hand back markdown already, so the hard part shifts from parsing to boundary detection.
- [Structured vs Unstructured Data](./structured-vs-unstructured-data.md) - spreadsheets and databases often want SQL access instead of being flattened into prose at all.

## Related

- [Retrieval-Augmented Generation (RAG)](./rag.md) - the pipeline this feeds.
- [Chunking](./chunking.md) and [Context-Aware Chunking](./context-aware-chunking.md) - splitting only works if the extracted text preserved the document's structure.
- [Vector Embeddings](./vector-embeddings.md) - what finally gets embedded is whatever survived extraction.
- [Delete-Before-Insert Re-Ingestion](./delete-before-insert-reingestion.md) - the hygiene step that pairs with every re-extraction of a changed file.
- [Metadata Filtering](./metadata-filtering.md) - extraction is where file type, source, and IDs get stamped onto the text.

## Tools

- [Docling](../entities/tools/docling.md) - open-source extraction across complex file types, dispatching on file extension.
- [n8n](../entities/tools/n8n.md) - a switch node on MIME type routes each file to its own extractor branch.
- [Crawl4AI](../entities/tools/crawl4ai.md) - the web-side counterpart, returning markdown from pages.
- [Google Drive](../entities/tools/google-drive.md) - the file source whose mixed formats force the branching.
- [Python](../entities/tools/python.md) - where the code-based extraction path lives.

## Sources

- [Effortless RAG in n8n - Use ALL Your Files (PDFs, Excel, and More)](../sources/effortless-rag-in-n8n-use-all-your-files-pdfs-excel-and-more.md) - "[0:00:00] the hardest part of the whole setup is really just actually extracting the text from the documents that you want to put in your knowledge base especially if you want to use PDFs or other document types that don't convert as easily to Raw text"
- [Effortless RAG in n8n - Use ALL Your Files (PDFs, Excel, and More)](../sources/effortless-rag-in-n8n-use-all-your-files-pdfs-excel-and-more.md) - "[0:07:18] in the old workflow we have a single node that extracts the document text now the problem with this is it only works for file types where you can just extract the raw text... when we have more complex file types like Excel documents or PDF documents it's not that simple"
- [Turn ANY File into LLM Knowledge in SECONDS](../sources/turn-any-file-into-llm-knowledge-in-seconds.md) - "[0:01:10] It is a free and open-source tool I'm going to show you how to use today to work with all these complex data types so you can properly curate your data no matter how complex it is"
- [Turn ANY File into LLM Knowledge in SECONDS](../sources/turn-any-file-into-llm-knowledge-in-seconds.md) - "[0:06:19] under the hood, it recognizes the file extension and it knows what to do to work with those different file types without us having to do that much more in our code."
