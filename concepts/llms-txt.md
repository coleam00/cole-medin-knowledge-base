---
type: concept
title: "llms.txt"
description: "An emerging convention where a project publishes all of its documentation as a single LLM-formatted page (llms.txt / llms-full.txt), so one fetch yields complete, chunk-ready knowledge for an agent."
tags: [web-crawling, documentation]
videos: [turn-any-website-into-llm-knowledge-in-seconds-evolved]
created: 2026-07-21
updated: 2026-07-21
---

# llms.txt

`llms.txt` is a convention for shipping a whole documentation site as one machine-readable file. Instead of making a crawler discover, fetch, and clean dozens of HTML pages, the project publishes the corpus itself: "they've started to put out what's called an LLMs.ext... /lms.ext orlms-full.ext... they take every single page for their documentation and they combine it together into a single page" [0:06:15]. The two variants split by depth - the short file is an index or condensed map, the `-full` variant is the entire body of documentation concatenated.

What makes it more than a convenience is that the output is already in the shape a knowledge pipeline wants: "It's formatted specifically for LLM knowledge. And so that is the third method of scraping data from a website" [0:06:52]. It is clean markdown with a sane heading hierarchy, so the HTML-to-markdown conversion step that normally introduces noise is skipped entirely, and the headings give a chunker natural boundaries to split on.

It sits alongside the other two discovery methods as the best case of the three. A sitemap tells you which URLs exist and still leaves you to fetch and clean each one. Recursive crawling from a base URL discovers pages by following links, which is the slowest and dirtiest path. `llms.txt` collapses discovery, fetching, and cleaning into a single HTTP request, which is why crawlers now branch on it: if a site publishes one, take it, and fall back to a sitemap or recursion only when it does not.

The practical caveats are adoption and freshness. Only projects that opt in have one, the file is generated on the project's own schedule rather than yours, and `llms-full.txt` for a large framework can be hundreds of thousands of tokens - far past any context window, so it still has to be chunked and embedded rather than pasted whole.

## Part of

- [Web Crawling & Ingestion](./web-crawling.md) - the third and cleanest of the three ingestion entry points, next to sitemaps and recursive crawling.
- [Knowledge Bases](./knowledge-bases.md) - a fetched `llms.txt` is a corpus, not an answer; it still lands in a knowledge base to be retrieved from.

## Contrasts with

- [Context7](../entities/tools/context7.md) - the hosted alternative, where someone else indexes library docs and serves snippets on demand instead of you fetching and owning the file.
- [Training Cutoff](./training-cutoff.md) - the problem it exists to solve: parametric knowledge of a library goes stale, a freshly fetched `llms.txt` does not.

## Implemented by

- [Crawl4AI](../entities/tools/crawl4ai.md) - the crawler that fetches and converts these files as part of an ingestion run.
- [Crawl4AI RAG MCP Server](../entities/tools/crawl4ai-rag-mcp.md) - accepts an `llms.txt`, a sitemap, or a base URL and picks the right strategy per input.

## Related

- [Chunking](./chunking.md) - a full docs file is far too large for one context, so heading-aware splitting is the immediate next step.
- [Retrieval-Augmented Generation (RAG)](./rag.md), [Vector Embeddings](./vector-embeddings.md) - what the chunks feed once ingested.
- [Docs and Templates as Coding-Assistant Context](./docs-as-agent-context.md) - the payoff, giving a coding agent current library documentation instead of half-remembered APIs.
- [Open Knowledge Format (OKF)](./open-knowledge-format.md), [The LLM Wiki](./the-llm-wiki.md) - the same instinct pushed further: publish knowledge in a format agents read natively.
- [Progressive Disclosure](./progressive-disclosure.md) - why the short `llms.txt` index variant matters, letting an agent open only the sections it needs.

## Sources

- [Turn ANY Website into LLM Knowledge in Seconds - EVOLVED](../sources/turn-any-website-into-llm-knowledge-in-seconds-evolved.md) - "[0:06:15] they've started to put out what's called an LLMs.ext... /lms.ext orlms-full.ext... they take every single page for their documentation and they combine it together into a single page"
- [Turn ANY Website into LLM Knowledge in Seconds - EVOLVED](../sources/turn-any-website-into-llm-knowledge-in-seconds-evolved.md) - "[0:06:52] It's formatted specifically for LLM knowledge. And so that is the third method of scraping data from a website"
