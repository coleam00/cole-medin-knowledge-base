---
type: source
title: "Turn ANY Website into LLM Knowledge in SECONDS"
description: "Crawl4AI is an open-source, fast, memory-efficient web crawler that converts any website into clean markdown ready to ingest into an LLM knowledge base for RAG."
youtube_id: JWfNLF_g_V0
url: https://www.youtube.com/watch?v=JWfNLF_g_V0
slug: turn-any-website-into-llm-knowledge-in-seconds
published: 2025-01-12
duration: "0:18:46"
recency_rank: 126
raw: "../raw/turn-any-website-into-llm-knowledge-in-seconds.md"
tags: [rag, web-crawling, knowledge-bases]
created: 2026-07-21
updated: 2026-07-21
---

# Turn ANY Website into LLM Knowledge in SECONDS

Cole opens with the core limitation of LLMs: their knowledge is general and frozen at a training cutoff, so they fail on new tools like Pydantic AI. RAG (retrieval augmented generation) fixes this by feeding curated external knowledge into the model, but the curation/ingestion step is usually slow and painful, especially when the source is an entire website. The video positions Crawl4AI as the solution: an open-source crawling framework purpose-built to scrape sites and output LLM-friendly markdown, handling proxies, sessions, and irrelevant-content removal under the hood.

The walkthrough builds up in stages. First, a basic single-page scrape shows how ugly raw HTML becomes clean markdown via a tiny script (pip install plus a Playwright setup command). Then Cole tackles scaling: rather than hand-listing URLs, he pulls a site's sitemap.xml to enumerate every page, pausing to cover web-scraping ethics (checking robots.txt before crawling). He progresses from a naive per-URL loop (spins up a new browser each time) to reusing a single browser session for sequential crawling, and finally to parallel batch crawling (10 pages at once) that stays remarkably memory-efficient (peak ~119MB).

The payoff is a full RAG agent that is a Pydantic AI expert: Cole scraped all 42 Pydantic AI docs pages with Crawl4AI, embedded them into a Supabase pgvector database, wrapped a Pydantic AI agent around it with a Streamlit front end, and demos it answering questions (supported models, the weather agent example) with source links. He frames scraping-to-knowledge-base as the most common way to make an agent an expert, teasing a follow-up build video.

## Concepts covered

- [Retrieval-Augmented Generation (RAG)](../concepts/rag.md)
- [Knowledge Bases](../concepts/knowledge-bases.md)
- [Web Crawling & Ingestion](../concepts/web-crawling.md)
- [Vector Embeddings](../concepts/vector-embeddings.md)

## Entities

- [Crawl4AI](../entities/tools/crawl4ai.md)
- [Pydantic AI](../entities/tools/pydantic-ai.md)
- [Playwright](../entities/tools/playwright.md)
- [Postgres](../entities/tools/postgres-pgvector.md)
- [Streamlit](../entities/tools/streamlit.md)
- [GitHub](../entities/tools/github.md)
- [Cole Medin](../entities/people/cole-medin.md)

## Key moments

- **[0:00:00]** The problem: LLM knowledge is general and frozen at training cutoff (Claude has no clue what Pydantic AI is)
- **[0:00:32]** RAG defined: retrieval augmented generation gives curated external knowledge to an LLM to make it an expert
- **[0:01:11]** Introduces Crawl4AI as an open-source crawler that formats output as LLM-friendly markdown
- **[0:03:18]** Core value: converts messy raw HTML into clean markdown; removes irrelevant content, handles proxies/sessions
- **[0:04:46]** Getting started: pip install plus setup command that installs Playwright under the hood
- **[0:07:38]** Scaling via sitemap.xml to extract every page URL automatically instead of hand-listing
- **[0:09:01]** Web-scraping ethics: check robots.txt before crawling (YouTube, GitHub examples)
- **[0:10:39]** Efficiency progression: naive loop vs reusing one browser session for sequential crawling
- **[0:12:45]** Parallel batch crawling: 10 pages at once, peak RAM only ~119MB
- **[0:15:09]** The gift: a full Pydantic AI RAG expert agent (pgvector + Supabase + Streamlit) demoed live

## Transcript

[Raw transcript](../raw/turn-any-website-into-llm-knowledge-in-seconds.md)
