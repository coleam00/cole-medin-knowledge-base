---
type: source
title: "Why the Best AI Coding Tools Abandoned RAG (And What They Use Instead)"
description: "Traditional RAG (semantic search over a vector database) is dead only for coding because code is highly structured; for the majority of unstructured-data use cases it remains essential, and the real frontier is letting agents choose which retrieval strategy to use per query."
youtube_id: 60G93MXT4DI
url: https://www.youtube.com/watch?v=60G93MXT4DI
slug: why-the-best-ai-coding-tools-abandoned-rag-and-what-they-use-instead
published: 2026-02-18
duration: "0:14:53"
recency_rank: 33
raw: "../raw/why-the-best-ai-coding-tools-abandoned-rag-and-what-they-use-instead.md"
tags: [rag, retrieval, agentic-search]
created: 2026-07-21
updated: 2026-07-21
---
# Why the Best AI Coding Tools Abandoned RAG (And What They Use Instead)

Cole pushes back on the popular 'RAG is dead' narrative by drawing a precise distinction: what people mean is traditional RAG (chunking documents, embedding them into a vector database, and doing semantic similarity search). RAG properly defined is just retrieval-augmented generation, any method of pulling external information into an LLM's context, so agentic search over a codebase is still RAG, just a different kind. Whether traditional RAG is dead depends entirely on how structured your data is.

Code is the poster child for structured data: identifiers are exactly spelled, files give built-in organization, and coding agents live in the terminal with powerful tools like ripgrep and glob. That means keyword/regex search and file navigation work extremely well and there is no need to index a codebase into a vector database, which is also hard to keep in sync as code changes rapidly. Industry leaders confirm the shift: Claude Code started with a local vector-database RAG and moved to agentic search (Boris Cherny), Cline's Nick Baumann calls the reflexive reach for RAG a 'mind virus,' and Aider uses tree-sitter to hand the agent a high-level index of files and core classes in its system prompt rather than a vector index.

But for unstructured knowledge (Google Drive, SharePoint, customer support, legal/compliance) semantic search is still critical, because you must find synonyms and conceptually similar text buried across thousands of documents (the Star Wars spaceships example). Chunking is a feature, not just a cost: pulling small chunks is roughly 100x cheaper at scale than having an agent grep and cat entire documents. The emerging bridge is smart retrieval, giving agents both toolsets and letting them decide per query whether to use a regex/keyword tool or embed the query and hit the vector database.

## Concepts covered

- [Traditional RAG](../concepts/traditional-rag.md)
- [Retrieval-Augmented Generation (RAG)](../concepts/rag.md)
- [When RAG Is (and Isn't) Dead](../concepts/when-rag-is-dead.md)
- [Structured vs Unstructured Data](../concepts/structured-vs-unstructured-data.md)
- [Agentic Search](../concepts/agentic-search.md)
- [Semantic Search](../concepts/semantic-search.md)
- [Keyword Search](../concepts/keyword-search.md)
- [Codebase Indexing](../concepts/codebase-indexing.md)
- [Chunking](../concepts/chunking.md)
- [Vector Embeddings](../concepts/vector-embeddings.md)
- [Knowledge Bases](../concepts/knowledge-bases.md)
- [Hierarchical RAG](../concepts/hierarchical-rag.md)
- [Agentic RAG](../concepts/agentic-rag.md)

## Entities

- [Claude Code](../entities/tools/claude-code.md)
- [Boris Cherny](../entities/people/boris-cherny.md)
- [Nick Baumann](../entities/people/nick-baumann.md)
- [Cline](../entities/tools/cline.md)
- [Aider](../entities/tools/aider.md)
- [grep (command-line search)](../entities/tools/ripgrep.md)
- [Archon](../entities/tools/archon.md)
- [Scrimba](../entities/organizations/scrimba.md)
- [Cole Medin](../entities/people/cole-medin.md)

## Key moments

- **[0:00:00]** Opens on the 'RAG is dead' narrative and says it's mostly false but nuanced
- **[0:01:04]** Key distinction: 'RAG is dead' really means traditional RAG / semantic search over a vector database
- **[0:01:57]** Whether RAG is dead depends entirely on how structured your data is
- **[0:02:45]** Star Wars spaceships example: why semantic search beats keyword search for unstructured data
- **[0:04:11]** Why code is structured: exact identifiers, file organization, terminal tools like ripgrep and glob
- **[0:05:16]** Codebase indexing is another pipeline to maintain and hard to keep in sync with frequently-changing code
- **[0:07:19]** Boris Cherny: early Claude Code used a local vector DB but agentic search worked better
- **[0:08:40]** Nick Baumann (Cline): the RAG narrative is a 'mind virus' for autonomous coding agents
- **[0:09:42]** Aider uses tree-sitter to give the agent a high-level index in its system prompt
- **[0:11:16]** Chunking is a feature: ~100x cheaper than agentic grep over large knowledge bases
- **[0:13:16]** The bridge: give agents both toolsets and let them choose retrieval strategy per query

## Transcript

[Raw transcript](../raw/why-the-best-ai-coding-tools-abandoned-rag-and-what-they-use-instead.md)

