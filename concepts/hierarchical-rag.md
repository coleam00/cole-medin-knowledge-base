---
type: concept
title: "Hierarchical RAG"
description: "A multi-level retrieval scheme that first narrows to the right documents or sections, then retrieves fine-grained chunks within them."
tags: [rag, retrieval, hierarchy, chunking]
videos: [why-the-best-ai-coding-tools-abandoned-rag-and-what-they-use-instead, every-rag-strategy-explained-in-13-minutes-no-fluff]
created: 2026-07-21
updated: 2026-07-21
---

# Hierarchical RAG

Hierarchical RAG retrieves in levels: it first zooms out to find the right document or section, then zooms in to pull the precise chunks inside it. The mechanism is parent-child chunk relationships: "We can have these parent child chunk relationships and generally we store these relationships as metadata for all of our chunks" [0:08:59]. Searching happens at the small, precise level while the returned context expands to the parent, so you get accurate matching without starving the model of surrounding context.

## How it works

The design resolves the classic chunk-size dilemma. Small chunks match queries precisely but return too little context; large chunks carry context but match noisily. Hierarchical RAG has it both ways by "balancing precision, you know, searching small with context, returning big." The parent-child links live in chunk metadata, so once a small child chunk matches, the pipeline can hand the model the larger parent it belongs to. This makes RAG accurate enough "so we can rely on just a little bit of information we pull through a few chunks" rather than dumping many marginal chunks into context.

Cole positions it as closely related to letting an agent drive retrieval: "you could argue that hierarchical rag is sort of a subset of a gentic rag," since choosing to expand from child to parent is itself a retrieval decision.

## Builds on

- [Chunking](./chunking.md) - hierarchical RAG is a chunking-and-linking strategy; parent-child relationships are stored as chunk metadata.

## Part of

- [Agentic RAG](./agentic-rag.md) - Cole frames hierarchical RAG as "sort of a subset of a gentic rag," one strategy an agent can employ.

## Related

- [Agentic Search](./agentic-search.md) - shares the narrow-then-expand instinct, applied to files rather than embedded chunks.
- [Retrieval-Augmented Generation (RAG)](./rag.md), [Traditional RAG](./traditional-rag.md) - the pipeline hierarchical retrieval improves.
- [Hybrid Search](./hybrid-search.md), [Contextual Retrieval](./contextual-retrieval.md), [Reranking](./reranking.md) - complementary accuracy strategies often combined with it.

## Sources

- [Every RAG Strategy Explained in 13 Minutes (No Fluff)](../sources/every-rag-strategy-explained-in-13-minutes-no-fluff.md) - "[0:09:25] we're balancing precision, you know, searching small with context, returning big. And you could argue that hierarchical rag is sort of a subset of a gentic rag."
- [Why the Best AI Coding Tools Abandoned RAG (And What They Use Instead)](../sources/why-the-best-ai-coding-tools-abandoned-rag-and-what-they-use-instead.md) - "[0:12:59] I want to cover more like hierarchical rag to actually make rag really accurate so we can rely on just a little bit of information we pull through a few chunks."
