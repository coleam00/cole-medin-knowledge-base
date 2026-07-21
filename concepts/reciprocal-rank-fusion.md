---
type: concept
title: "Reciprocal Rank Fusion"
description: "A ranking method that merges results from multiple retrievers (e.g. keyword + semantic) into one fused ordering."
tags: [ranking, hybrid-search, fusion]
videos: [the-simplest-rag-stack-that-actually-works-complete-guide]
created: 2026-07-21
updated: 2026-07-21
---

# Reciprocal Rank Fusion

Reciprocal Rank Fusion (RRF) is the algorithm that merges two separately-ranked result lists, typically a keyword search and a semantic search, into a single ordering. It exists to solve a scoring problem that appears the moment you combine retrievers: "the reason that we need an algorithm in the first place is because the similarity scores from our two pipelines have a completely different scale" (the-simplest-rag-stack, 0:20:56). You cannot just concatenate or average raw scores when they live in different number systems.

## Why raw scores fail

The two pipelines report confidence on incompatible scales. "Your similarity score for a vector search is going to be between zero and one. But for a text search or our keyword search, it's going to be something different like 15 or 13 or 11" (the-simplest-rag-stack, 0:21:04). A naive merge would let the keyword pipeline's larger raw numbers dominate purely because of scale, not relevance.

## How it works

RRF sidesteps the scale mismatch by throwing away the raw scores entirely and using only where each item landed in its list. "We have this formula where we're going to use rank positions instead of raw scores" (the-simplest-rag-stack, 0:21:20). Each document earns points based on its reciprocal rank in each list (roughly 1 over its position), and those points are summed across pipelines. An item that ranks near the top of both lists rises to the top of the fused result; an item strong in only one still contributes. Because rank position is unitless, the two retrievers combine fairly regardless of how their native scores are calibrated.

## Part of

- [Hybrid Search](./hybrid-search.md) is the pattern RRF completes. Hybrid search runs keyword and semantic retrieval in parallel; RRF is the fusion step that reconciles their outputs into one ranked list.

## Contrasts with

- [Keyword Search](./keyword-search.md) and [Semantic Search](./semantic-search.md) are the two input pipelines whose incompatible score scales make RRF necessary in the first place.

## Sources

- [The Simplest RAG Stack That Actually Works (Complete Guide)](../sources/the-simplest-rag-stack-that-actually-works-complete-guide.md) - "[0:20:56] the reason that we need an algorithm in the first place is because the similarity scores from our two pipelines have a completely different scale"
- [The Simplest RAG Stack That Actually Works (Complete Guide)](../sources/the-simplest-rag-stack-that-actually-works-complete-guide.md) - "[0:21:20] we have this formula where we're going to use rank positions instead of raw scores"
