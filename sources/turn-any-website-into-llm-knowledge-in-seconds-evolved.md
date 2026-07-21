---
type: source
title: "Turn ANY Website into LLM Knowledge in Seconds - EVOLVED"
description: "Crawl4AI lets you turn any website into clean, LLM-ready markdown knowledge for RAG using one of three strategies (sitemap, recursive navigation crawl, or llms.txt), automatically chunked and loaded into a vector database."
youtube_id: FQlCWrsUpHo
url: https://www.youtube.com/watch?v=FQlCWrsUpHo
slug: turn-any-website-into-llm-knowledge-in-seconds-evolved
published: 2025-04-30
duration: "0:26:39"
recency_rank: 96
raw: "../raw/turn-any-website-into-llm-knowledge-in-seconds-evolved.md"
tags: [rag, web-crawling, crawl4ai, knowledge-base]
created: 2026-07-21
updated: 2026-07-21
---

# Turn ANY Website into LLM Knowledge in Seconds - EVOLVED

Cole revisits Crawl4AI, an open-source (42k-star) web crawler that scrapes essentially any website and outputs AI-ready markdown that LLMs parse far better than raw HTML. After a single-page basic example against the Pydantic AI docs, he focuses on the real goal: crawling entire websites to build RAG knowledge bases. He lays out three general strategies that together cover any site. First, a sitemap (usually /sitemap.xml) gives a structured list of every URL to crawl in parallel batches. Second, when there's no sitemap, a recursive crawl starts from the homepage and follows 'internal links' (same-domain) to a configurable depth, dynamically building a sitemap over time. Third, an llms.txt (or llms-full.txt) is a single page combining all of a project's docs, so you fetch one URL and chunk it.

He ships a GitHub repo with granular example scripts (single page, sequential, sitemap-parallel, llms.txt, recursive) plus a full Pydantic AI RAG agent whose insert_docs tool auto-detects which of the three strategies a given URL needs and applies it. The agent uses ChromaDB as a simple local vector database (swappable for Supabase, Qdrant, Pinecone) and a Streamlit chat UI. Live demos show Crawl4AI's speed: 457 chunks from the Crawl4AI sitemap, 2,420 from recursively crawling Pydantic AI, and 788 from the LangGraph llms.txt, with insertion into Chroma being slower than the scraping itself.

He touches chunking, splitting markdown on primary headers and subsections so distinct sections stay intact and contextual meaning isn't lost (a 'smart_chunk_markdown' function), and teases a dedicated chunking-strategies video. He closes by floating a major direction change for Archon: pivoting it from an all-in-one agent builder that also writes code (which duplicates work AI IDEs already do) toward being a knowledge engine, a better open-source Context7 that supplies RAG documentation to AI coding assistants rather than generating agent code itself.

## Concepts covered

- [Retrieval-Augmented Generation (RAG)](../concepts/rag.md)
- [Structured vs Unstructured Data](../concepts/structured-vs-unstructured-data.md)
- [Web Crawling & Ingestion](../concepts/web-crawling.md)
- [Chunking](../concepts/chunking.md)
- [Context-Aware Chunking](../concepts/context-aware-chunking.md)
- [Knowledge Bases](../concepts/knowledge-bases.md)

## Entities

- [Crawl4AI](../entities/tools/crawl4ai.md)
- [Archon](../entities/tools/archon.md)
- [Pydantic AI](../entities/tools/pydantic-ai.md)
- [Chroma](../entities/tools/chroma.md)
- [LangGraph](../entities/tools/langgraph.md)
- [Context7](../entities/tools/context7.md)
- [Aqua Voice](../entities/tools/aqua-voice.md)
- [Windsurf](../entities/tools/windsurf.md)
- [Streamlit](../entities/tools/streamlit.md)
- [Cole Medin](../entities/people/cole-medin.md)

## Key moments

- **[0:00:00]** Intro: revisiting Crawl4AI to handle every kind of website for LLM knowledge
- **[0:01:14]** Crawl4AI is open source with 42k GitHub stars; produces AI-ready markdown
- **[0:03:20]** Single-page example: async web crawler scrapes Pydantic AI docs into markdown
- **[0:05:17]** Strategy 1 - sitemap.xml gives all URLs to crawl in parallel
- **[0:06:01]** Strategy 2 - recursive crawl from homepage via navigation links
- **[0:06:15]** Strategy 3 - llms.txt / llms-full.txt combines all docs into one page
- **[0:09:30]** Sponsor: Aqua Voice
- **[0:11:12]** The unified insert_docs agent auto-detects URL type and picks the strategy
- **[0:12:32]** Demo: sitemap crawl of Crawl4AI creates 457 chunks in ChromaDB
- **[0:15:15]** Demo: Pydantic AI RAG agent answering questions via Streamlit
- **[0:19:41]** Chunking markdown by headers and subsections to preserve context
- **[0:21:33]** Recursive crawl uses internal links to build a sitemap dynamically
- **[0:23:12]** Archon direction change: pivot toward a knowledge engine / better Context7

## Transcript

[Raw transcript](../raw/turn-any-website-into-llm-knowledge-in-seconds-evolved.md)
