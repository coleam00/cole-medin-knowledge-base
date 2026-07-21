---
type: source
title: "No Code RAG Agents? You HAVE to Check out n8n + LangChain"
description: "You can build a full RAG AI agent with tool calling and a Google Drive knowledge base entirely with no code by combining n8n's workflow automation with its built-in LangChain nodes."
youtube_id: Xifzdn7zW3A
url: https://www.youtube.com/watch?v=Xifzdn7zW3A
slug: no-code-rag-agents-you-have-to-check-out-n8n-langchain
published: 2024-08-25
duration: "0:17:47"
recency_rank: 171
raw: "../raw/no-code-rag-agents-you-have-to-check-out-n8n-langchain.md"
tags: [no-code-agents, rag, n8n, langchain, knowledge-bases]
created: 2026-07-21
updated: 2026-07-21
---

Building an advanced RAG AI agent is not limited to custom-coded applications. Using n8n, a self-hostable workflow automation tool, together with its native LangChain integration, Cole builds a fully functional RAG agent with zero lines of code. n8n workflows are made of triggers (here a chat message) and action nodes; the LangChain "AI agent" node bundles a chat model, memory, and tools together, each configurable by dropdown, so any model (OpenAI, Anthropic, Groq/Llama, Ollama), memory backend (in-memory, Postgres, Redis), and vector store (in-memory, Supabase, Pinecone) can be swapped in without code.

The agent is wired with two tools. The first is a built-in vector store retrieval tool that answers questions from an in-memory vector store, using OpenAI's text-embedding-3-large for embeddings and GPT-4o-mini to process retrieved chunks. The second is an n8n-workflow-as-a-tool: a separate workflow triggered by a webhook that searches Google Drive for a file by query, downloads it, extracts its text, chunks it with a 1,000-character splitter, and inserts it into the vector database on demand. This lets the user tell the chatbot "add my 8/22 meeting notes to your knowledge base," then ask questions the agent could only answer from that document, giving deliberate control over what enters the knowledge base rather than bulk-syncing every file.

Cole calls out practical gotchas and production advice. The in-memory vector store prefixes its memory key with the workflow ID, so insertion and retrieval must happen in the same workflow, which forces a workaround where a second workflow calls back into the original via webhook. For production he recommends Supabase (a Postgres table for chat memory plus a Supabase vector store) so everything lives in one place and the memory key can be defined dynamically, avoiding the workaround. The finished chatbot can even be embedded into any website via a copy-paste widget.

## Concepts covered

- [Retrieval-Augmented Generation (RAG)](../concepts/rag.md)
- [Knowledge Bases](../concepts/knowledge-bases.md)
- [Chunking](../concepts/chunking.md)
- [Vector Embeddings](../concepts/vector-embeddings.md)
- [Semantic Search](../concepts/semantic-search.md)
- [Memory Systems](../concepts/memory-systems.md)
- [No-Code Automation](../concepts/no-code-automation.md)
- [Web Crawling & Ingestion](../concepts/web-crawling.md)

## Entities

- [n8n](../entities/tools/n8n.md)
- [LangChain](../entities/tools/langchain.md)
- [OpenAI](../entities/organizations/openai.md)
- [Google Drive](../entities/tools/google-drive.md)
- [Supabase](../entities/tools/supabase.md)
- [Cole Medin](../entities/people/cole-medin.md)

## Key moments

- **[0:00:00]** Premise: building advanced RAG agents is not limited to custom code, do it with n8n + LangChain, zero code
- **[0:01:21]** Import prebuilt workflows from GitHub JSON files via the three-dots > import from file
- **[0:01:48]** n8n workflow anatomy: triggers vs action nodes; the trigger here is a chat message
- **[0:03:00]** The chat message flows into a LangChain "AI agent" tools node, model, memory, tools all no-code
- **[0:03:46]** Chat model is swappable: OpenAI, Anthropic/Claude, Groq/Llama, Ollama by dropdown
- **[0:04:28]** Memory options: in-memory chat memory, Postgres chat memory, Redis
- **[0:04:59]** Tools: calculator, vector store retrieval, and calling any n8n workflow as a tool
- **[0:05:42]** First tool: built-in vector store retrieval with an in-memory vector store; Supabase/Pinecone as alternatives
- **[0:06:59]** Embeddings via OpenAI text-embedding-3-large; GPT-4o-mini processes retrieved chunks
- **[0:07:46]** Second tool: an n8n workflow that ingests a Google Drive file into the knowledge base
- **[0:09:15]** Ingestion workflow: webhook -> search Drive -> download -> extract text -> chunk (1000) -> insert to vector DB
- **[0:11:31]** Live demo: ask before ingestion (no answer), ingest 8/22 meeting notes, ask again (answered)
- **[0:12:41]** Why on-demand ingestion over bulk-syncing every file: avoids vector DB bloat, gives control
- **[0:14:07]** In-memory vector store memory-key-prefixed-by-workflow-ID gotcha and the second-workflow webhook workaround
- **[0:15:11]** Supabase (Postgres memory + vector store) recommended for production to dodge the workaround
- **[0:16:08]** Embed the chatbot as a widget into any website with copy-paste code

## Transcript

[Raw transcript](../raw/no-code-rag-agents-you-have-to-check-out-n8n-langchain.md)
