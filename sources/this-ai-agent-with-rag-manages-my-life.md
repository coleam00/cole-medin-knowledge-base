---
type: source
title: "This AI Agent with RAG Manages MY LIFE"
description: "An AI agent becomes genuinely useful for daily life when it can intelligently decide whether to search documents via RAG and then act on what it finds through external tools like Asana."
youtube_id: 7dKQPbSXiB8
url: https://www.youtube.com/watch?v=7dKQPbSXiB8
slug: this-ai-agent-with-rag-manages-my-life
published: 2024-08-04
duration: "0:10:53"
recency_rank: 177
raw: "../raw/this-ai-agent-with-rag-manages-my-life.md"
tags: [agentic-rag, rag, tool-design, asana, chroma]
created: 2026-07-21
updated: 2026-07-21
---

Cole walks through upgrading a basic RAG chatbot into a practical AI agent that searches his meeting notes and creates Asana tasks from the action items it finds. He calls out three flaws in the earlier RAG-only implementation: it always ran RAG regardless of the prompt, it did nothing beyond RAG (no other tools or APIs), and it rebuilt the vector database in memory from scratch on every run. The fix is to make retrieval agentic (the LLM decides when to search), to combine RAG with action-taking tools, and to persist the vector store locally so documents are only embedded once.

The build has two scripts. The first creates a local Chroma vector database: it loads PDF and text meeting notes with LangChain's directory loader, splits them into 1,000-character chunks, embeds them with an open-source Hugging Face model, and saves everything to a chroma_db folder (a SQLite file plus supporting data). The second script is the Asana agent, which already had tools for creating projects and updating tasks bound to an OpenAI or Anthropic chat model. Cole adds a document-query tool that loads the persisted Chroma instance and runs a cosine-similarity search returning the top three matching chunks; the tool's docstring tells the LLM when and how to use it, so retrieval joins the same tool-calling loop as the Asana actions.

The payoff is a Streamlit chatbot where a single prompt can retrieve an answer from the notes (what Emily proposed for the wellness program) and turn it into a new Asana project with tasks. Cole argues the real value is not just time saved per meeting but reduced friction: pulling action items manually is annoying and often skipped, so offloading that grunt work keeps you more organized over time. He closes by teasing a follow-up on moving documents to Google Drive and the vector database to the cloud for a production deployment.

## Concepts covered

- [Agentic RAG](../concepts/agentic-rag.md)
- [Retrieval-Augmented Generation (RAG)](../concepts/rag.md)
- [Chunking](../concepts/chunking.md)
- [Vector Embeddings](../concepts/vector-embeddings.md)
- [Semantic Search](../concepts/semantic-search.md)
- [Agentic Workflow Engineering](../concepts/agentic-workflow-engineering.md)
- [Tool Design](../concepts/tool-design.md)
- [Agentic Automation](../concepts/agentic-automation.md)

## Entities

- [LangChain](../entities/tools/langchain.md)
- [Chroma](../entities/tools/chroma.md)
- [Asana](../entities/tools/asana.md)
- [Hugging Face](../entities/organizations/hugging-face.md)
- [Streamlit](../entities/tools/streamlit.md)
- [OpenAI](../entities/organizations/openai.md)
- [Anthropic](../entities/organizations/anthropic.md)
- [Cole Medin](../entities/people/cole-medin.md)
- [GitHub](../entities/tools/github.md)

## Key moments

- **[0:00:29]** Three flaws in the prior RAG-only build: always retrieves, no other tools, rebuilds DB every run
- **[0:01:54]** Script 1: create a local Chroma vector database and load meeting notes into it
- **[0:03:56]** Chunking documents at 1,000 characters per chunk
- **[0:04:25]** Embedding with an open-source Hugging Face model and persisting Chroma to disk
- **[0:05:07]** Script 2: add RAG as a tool to the existing Asana tool-calling agent
- **[0:06:41]** Query tool does a top-3 cosine similarity search over the persisted Chroma DB
- **[0:08:07]** Live test: retrieve Emily's wellness program proposal from the notes
- **[0:08:35]** Chain RAG into action: create an Asana project and tasks from the retrieved answer

## Transcript

[Raw transcript](../raw/this-ai-agent-with-rag-manages-my-life.md)
