---
type: source
title: "This RAG AI Agent with n8n + Supabase is the Real Deal"
description: "You can build a production-ready, cost-effective RAG AI agent with no code by combining n8n for workflow automation and Supabase for both the vector store (pgvector) and Postgres-backed chat memory."
youtube_id: PEI_ePNNfJQ
url: https://www.youtube.com/watch?v=PEI_ePNNfJQ
slug: this-rag-ai-agent-with-n8n-supabase-is-the-real-deal
published: 2024-09-04
duration: "0:16:28"
recency_rank: 168
raw: "../raw/this-rag-ai-agent-with-n8n-supabase-is-the-real-deal.md"
tags: [rag, no-code, n8n, supabase]
created: 2026-07-21
updated: 2026-07-21
---

# This RAG AI Agent with n8n + Supabase is the Real Deal

Cole argues that most YouTube RAG tutorials ("chat with your PDF") are not production-ready: they break as the knowledge base grows, documents get updated, and users ask unexpected questions. His alternative is a no-code RAG agent built in n8n (a low-cost workflow automation tool like Make or Zapier) backed by Supabase, which serves double duty as the pgvector vector database and the Postgres store for chat memory. He demos the agent answering a question it initially cannot ("the 8/25 action items"), then drops meeting notes into a watched Google Drive folder, watches an n8n workflow embed and insert them into Supabase, and re-asks to get the correct answer.

The build walkthrough covers the two halves of the n8n workflow. The query side is a chat-trigger into an AI agent node wired to a chat model (GPT-4o-mini, swappable for Anthropic), Postgres-backed chat memory, and a Supabase vector-store retrieval tool. Cole stresses using Postgres and Supabase for chat memory instead of the default local windowed buffer memory, which would overload the n8n server and is not scalable. n8n auto-creates the memory table, and Supabase's docs provide copy-paste SQL to enable pgvector and create the documents table plus the match function.

The ingestion side polls a Google Drive folder for created or updated files. Cole highlights a step most tutorials miss: before re-inserting an updated document you must delete the old vectors for that file ID, because Supabase (and other n8n vector stores) insert rather than upsert, so re-ingesting a file otherwise piles up duplicate vectors and corrupts retrieval. Files are downloaded, converted to text, chunked with a recursive character text splitter via the default document loader, embedded with OpenAI embeddings, and inserted. He notes semantic and keyword search enhancements as natural next steps.

## Concepts covered

- [Retrieval-Augmented Generation (RAG)](../concepts/rag.md)
- [Agentic RAG](../concepts/agentic-rag.md)
- [Knowledge Bases](../concepts/knowledge-bases.md)
- [Vector Embeddings](../concepts/vector-embeddings.md)
- [Semantic Search](../concepts/semantic-search.md)
- [Chunking](../concepts/chunking.md)
- [Memory Systems](../concepts/memory-systems.md)
- [Agent Deployment](../concepts/agent-deployment.md)
- [No-Code AI Agents](../concepts/no-code-agents.md)

## Entities

- [n8n](../entities/tools/n8n.md)
- [Supabase](../entities/tools/supabase.md)
- [Postgres](../entities/tools/postgres-pgvector.md)
- [OpenAI](../entities/organizations/openai.md)
- [Google Drive](../entities/tools/google-drive.md)
- [Cole Medin](../entities/people/cole-medin.md)

## Key moments

- **[0:00:00]** Thesis: most RAG tutorials are not production-ready and break as the knowledge base grows and documents update
- **[0:00:30]** Introduces the stack: n8n for no-code workflows plus Supabase (pgvector) for the vector database
- **[0:01:38]** Live demo: agent cannot answer the 8/25 meeting question with an empty knowledge base
- **[0:02:34]** Drops meeting notes into a Google Drive folder; n8n workflow embeds and inserts them into Supabase
- **[0:03:45]** Re-asks the question and the agent now answers correctly from the newly ingested document
- **[0:05:05]** Supabase setup: free tier, Postgres connection creds for memory plus API url and service-role secret for vectors
- **[0:06:29]** Query side: chat trigger, AI agent, chat model, Postgres memory, Supabase vector-store tool
- **[0:09:02]** Use Postgres and Supabase chat memory, not the default local windowed buffer memory that overloads the server
- **[0:10:01]** Copy-paste SQL from Supabase docs enables pgvector and creates the documents table plus match function
- **[0:12:11]** Ingestion: extract Google Drive file ID to reference the file downstream
- **[0:12:27]** Critical step: delete old vectors for the file ID before re-inserting to avoid duplicates (no upsert)
- **[0:14:31]** Download, convert to text, chunk with recursive character splitter, embed with OpenAI, insert into Supabase

## Transcript

[Raw transcript](../raw/this-rag-ai-agent-with-n8n-supabase-is-the-real-deal.md)
