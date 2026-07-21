---
type: source
title: "The Most Value Packed RAG Guide on YouTube (Feat. Llama 3.1 405B!)"
description: "RAG works by chunking documents into embeddings, matching a user's question to the most similar chunks via vector math, and feeding those chunks to an LLM as context, and you can build a working local-document chatbot on Llama 3.1 405B from scratch in minutes."
youtube_id: BrUW8_cCTew
url: https://www.youtube.com/watch?v=BrUW8_cCTew
slug: the-most-value-packed-rag-guide-on-youtube-feat-llama-31-405b
published: 2024-07-28
duration: "0:11:33"
recency_rank: 179
raw: "../raw/the-most-value-packed-rag-guide-on-youtube-feat-llama-31-405b.md"
tags: [rag, chunking, vector-embeddings, semantic-search, llama]
created: 2026-07-21
updated: 2026-07-21
---

This is a concise, beginner-oriented RAG (retrieval augmented generation) tutorial. Cole first explains the mental model: instead of the LLM answering a question directly, the question is routed to a knowledge database where vector mathematics matches it against the most relevant stored knowledge, which is then handed to the LLM as extra context. He walks through the ingestion side, where every document is split into chunks (100 to 1000 characters) and each chunk is turned into a vector and stored as an embedding in a vector database, and the retrieval side, where the user's question is embedded with the same function, compared via cosine similarity, and the top-K most similar chunks (for example five) are injected into the prompt.

The back half is a from-scratch build of a Streamlit chatbot that talks to local PDF and text documents. Cole uses LangChain (directory loader plus text splitter), a Hugging Face inference endpoint to access Llama 3.1 405B (with commented-out code to run Llama locally instead), an open-source Hugging Face embedding model, and Chroma as an in-memory local vector database. He defines functions to load and chunk documents, build the Chroma store, run a similarity search returning the five most relevant chunks, and prompt the LLM by replacing the last user message with a context-augmented version. He teases that a future video will add tool calling so an agent decides when to invoke RAG rather than doing it every time.

He demonstrates the finished app against a folder of made-up meeting notes (two PDFs, three text files), asking questions like what wellness programs Emily proposed and what was discussed in a specific meeting, showing the system correctly retrieves and concisely summarizes the right information. He frames this as a baseline foundation, noting RAG can be optimized and extended much further in later videos.

## Concepts covered

- [Retrieval-Augmented Generation (RAG)](../concepts/rag.md)
- [Chunking](../concepts/chunking.md)
- [Vector Embeddings](../concepts/vector-embeddings.md)
- [Semantic Search](../concepts/semantic-search.md)
- [Knowledge Bases](../concepts/knowledge-bases.md)
- [Agentic RAG](../concepts/agentic-rag.md)

## Entities

- [Cole Medin](../entities/people/cole-medin.md)
- [Llama](../entities/tools/llama.md)
- [LangChain](../entities/tools/langchain.md)
- [Streamlit](../entities/tools/streamlit.md)
- [Chroma](../entities/tools/chroma.md)
- [Hugging Face](../entities/organizations/hugging-face.md)
- [GitHub](../entities/tools/github.md)

## Key moments

- **[0:00:31]** Basic definition of RAG: question routed to knowledge DB, vector math matches relevant knowledge, fed to LLM as context
- **[0:01:26]** Ingestion: split documents into chunks, turn chunks into vectors stored as embeddings
- **[0:02:00]** Cosine similarity to measure how similar a user question is to a chunk
- **[0:02:19]** Retrieval: embed the question with the same function, return top-K similar chunks into the prompt
- **[0:03:01]** Transition to building a from-scratch Streamlit chatbot for local docs
- **[0:03:39]** Imports: LangChain, Streamlit, Hugging Face for Llama 3.1 405B
- **[0:04:21]** Hugging Face inference endpoint vs commented-out code to run Llama locally
- **[0:04:50]** LangChain directory loader loads all PDF and text documents from a folder
- **[0:05:29]** Chroma as the in-memory local vector database
- **[0:06:14]** Query function uses Chroma similarity search to return five most relevant chunks
- **[0:07:25]** Prompting: replace the last user message with a context+question augmented message
- **[0:09:32]** Live demo querying local meeting-notes documents, correct answers returned

## Transcript

[Raw transcript](../raw/the-most-value-packed-rag-guide-on-youtube-feat-llama-31-405b.md)
