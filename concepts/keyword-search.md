---
type: concept
title: "Keyword Search"
description: "Exact-term (lexical) search that complements semantic search, especially for identifiers and rare tokens."
tags: [keyword, search, lexical]
videos: [why-the-best-ai-coding-tools-abandoned-rag-and-what-they-use-instead, the-simplest-rag-stack-that-actually-works-complete-guide, all-the-best-rag-strategies-in-one-mcp-for-ai-coding-assistants]
created: 2026-07-21
updated: 2026-07-21
---

# Keyword Search

Keyword search is exact-term, lexical matching: if a word or phrase appears in the corpus, the search is guaranteed to find the chunk that contains it. "with keyword search... We're able to find exact terms with very high accuracy because if I search for a certain term and that exact word or phrase appears in my knowledge base, I am guaranteed to find that chunk" [0:05:26]. Because it does not rely on meaning or synonyms, it shines exactly where semantic search struggles: identifiers, error codes, tickers, and other rare tokens.

## How it works

Keyword search matches on literal strings rather than vector proximity, so "we're not relying on ambiguous natural language or having to find things based on synonyms and conceptual meaning." The canonical examples are precise lookups: "if we're in code searching for a 409 error, it'll find the exact code in the docs that references this error... we search AAPL, we'll find the stock and not the fruit." It exists precisely to plug a semantic-search failure mode, where "if you are looking for open AAI and you search for open AAI, the chunks that you get back from rag don't necessarily have the word open AAI in it." In a knowledge base this is often implemented as a case-insensitive text match, "a case insensitive keyword search in Superbase, pulling from our code examples or from the crawled pages table."

In a codebase, keyword search generalizes to regex and grep-style tooling, which Cole calls "a directed and focused search and that's definitely better when working with a codebase."

## Contrasts with

- [Semantic Search](./semantic-search.md) - meaning-based vector retrieval that captures synonyms and concepts but can miss exact tokens; keyword search is its complement.

## Part of

- [Hybrid Search](./hybrid-search.md) - combines keyword and semantic legs so retrieval catches both exact terms and concepts.

## Related

- [Agentic Search](./agentic-search.md) - grep and regex are the exact-term backbone of codebase navigation.
- [Agentic RAG](./agentic-rag.md) - an agent can choose keyword search as its retrieval strategy per question.
- [Structured vs. Unstructured Data](./structured-vs-unstructured-data.md) - exact matching suits structured, identifier-heavy data.

## Tools

- [Supabase](../entities/tools/supabase.md) - case-insensitive keyword search over crawled pages and code examples.
- [Ripgrep](../entities/tools/ripgrep.md) - directed regex/keyword search well suited to codebases.

## Sources

- [The Simplest RAG Stack That Actually Works (Complete Guide)](../sources/the-simplest-rag-stack-that-actually-works-complete-guide.md) - "[0:05:26] if I search for a certain term and that exact word or phrase appears in my knowledge base, I am guaranteed to find that chunk"
- [Why the Best AI Coding Tools Abandoned RAG (And What They Use Instead)](../sources/why-the-best-ai-coding-tools-abandoned-rag-and-what-they-use-instead.md) - "[0:04:26] Regular expression searching, keyword searching, all that is going to work very well. We're not relying on ambiguous natural language or having to find things based on synonyms and conceptual meaning."
- [All the BEST RAG Strategies in ONE MCP for AI Coding Assistants](../sources/all-the-best-rag-strategies-in-one-mcp-for-ai-coding-assistants.md) - "[0:10:45] if you are looking for open AAI and you search for open AAI, the chunks that you get back from rag don't necessarily have the word open AAI in it"
