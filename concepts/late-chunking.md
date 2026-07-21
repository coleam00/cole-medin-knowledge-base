---
type: concept
title: "Late Chunking"
description: "Embedding a full document first and only then splitting it, so each chunk carries whole-document context."
tags: [chunking, embeddings, context]
videos: [every-rag-strategy-explained-in-13-minutes-no-fluff, i-built-the-ultimate-rag-mcp-server-for-ai-coding-better-than-context7]
created: 2026-07-21
updated: 2026-07-21
---

# Late Chunking

Late chunking inverts the usual order of the RAG ingestion pipeline: it embeds the entire document first and splits into chunks only afterward. As Cole describes it, "we apply the embedding model onto the document before we chunk it, unlike most chunking strategies. And then we're going to chunk up the token embeddings" [0:08:34]. Because the embedding pass sees the whole document, "each of the chunks still maintain the context of the rest of the document... it's leveraging longer context embedding models" [0:08:34].

## Why it matters

In conventional chunking, each chunk is embedded in isolation, so a chunk that says "it doubled year over year" loses any idea of what "it" refers to once separated from its parent page. Late chunking solves this by embedding across the full document before segmenting, so the token embeddings that make up each chunk are already informed by everything around them. The result is chunks that retrieve accurately even when they contain pronouns, references, or claims whose meaning depends on the surrounding text. The trade-off is a dependency on long-context embedding models, since the whole document must fit through the embedder in one pass.

## Contrasts with

- [Chunking](./chunking.md) - standard chunking splits first and embeds each piece in isolation; late chunking reverses that ordering to preserve context.
- [Context-Aware Chunking](./context-aware-chunking.md) - both aim to keep context, but context-aware chunking finds better split points up front, while late chunking embeds before splitting at all.

## Related

- [Contextual Retrieval](./contextual-retrieval.md) - a related, Anthropic-published strategy that prepends document context to each chunk before embedding rather than embedding the whole document at once.
- [Traditional RAG](./traditional-rag.md) - the baseline pipeline late chunking is an upgrade over.
- [Vector Embeddings](./vector-embeddings.md) - the vectors late chunking produces, just in a different order of operations.

## Sources

- [Every RAG Strategy Explained in 13 Minutes (No Fluff)](../sources/every-rag-strategy-explained-in-13-minutes-no-fluff.md) - "[0:08:34] we apply the embedding model onto the document before we chunk it, unlike most chunking strategies. And then we're going to chunk up the token embeddings."
- [I Built the Ultimate RAG MCP Server for AI Coding (Better than Context7)](../sources/i-built-the-ultimate-rag-mcp-server-for-ai-coding-better-than-context7.md) - "[0:15:52] We could implement things like contextual retrieval which was released recently by Anthropic or late chunking or a gentic rag like I've covered on my channel."
