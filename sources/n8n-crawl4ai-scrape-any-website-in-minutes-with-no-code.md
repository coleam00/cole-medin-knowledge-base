---
type: source
title: "n8n + Crawl4AI - Scrape ANY Website in Minutes with NO Code"
description: "You can deploy Crawl4AI as a Dockerized API endpoint and drive it entirely from an n8n workflow to scrape any website and build a Supabase RAG knowledge base with no code."
youtube_id: c5dw_jsGNBk
url: https://www.youtube.com/watch?v=c5dw_jsGNBk
slug: n8n-crawl4ai-scrape-any-website-in-minutes-with-no-code
published: 2025-01-26
duration: "0:33:47"
recency_rank: 122
raw: "../raw/n8n-crawl4ai-scrape-any-website-in-minutes-with-no-code.md"
tags: [rag, web-crawling, no-code, n8n]
created: 2026-07-21
updated: 2026-07-21
---

# n8n + Crawl4AI - Scrape ANY Website in Minutes with NO Code

This video is the no-code counterpart to Cole's earlier Python-based Crawl4AI tutorials. Instead of importing Crawl4AI as a Python library, he shows how to deploy it as a Dockerized HTTP API endpoint (using DigitalOcean's App Platform, or locally alongside an existing n8n instance) and then call that endpoint from n8n's HTTP Request nodes. Because Crawl4AI runs a full headless browser, it is a CPU/RAM hog and is best hosted on its own instance; an optional bearer token protects the endpoint.

The end-to-end n8n workflow discovers every page of a site by fetching its sitemap.xml, converts the XML to JSON, splits the URL list into individual items, and loops over each one. For each page it POSTs to Crawl4AI's /crawl endpoint, which returns a task ID (scraping is async), then polls the /task/{id} endpoint every 5 seconds via a wait node and an if-statement loop until the status is 'completed' and the markdown/HTML/links come back. The returned markdown is chunked (5,000-char text splitter), embedded with OpenAI text-embedding-3-small, and inserted into a Supabase vector store, with the source page saved as metadata.

He caps the demo at scraping the Pydantic AI docs (148 vectors across ~30 pages) and wires up a minimal AI agent (GPT-4o-mini + Supabase chat memory + the Supabase vector store as a retrieval tool) that correctly answers questions by pulling the right documentation pages. Cole frames the whole thing as a reusable proof of concept and stresses ethical scraping: check robots.txt and terms of use before crawling any site.

## Concepts covered

- [Retrieval-Augmented Generation (RAG)](../concepts/rag.md)
- [Knowledge Bases](../concepts/knowledge-bases.md)
- [Chunking](../concepts/chunking.md)
- [Vector Embeddings](../concepts/vector-embeddings.md)
- [Semantic Search](../concepts/semantic-search.md)
- [Web Crawling & Ingestion](../concepts/web-crawling.md)
- [Containerization & Docker Networking](../concepts/containerization.md)
- [No-Code Automation](../concepts/no-code-automation.md)
- [Agent Graphs](../concepts/agent-graphs.md)
- [Agentic RAG](../concepts/agentic-rag.md)

## Entities

- [Crawl4AI](../entities/tools/crawl4ai.md)
- [n8n](../entities/tools/n8n.md)
- [Docker](../entities/tools/docker.md)
- [Supabase](../entities/tools/supabase.md)
- [DigitalOcean](../entities/organizations/digital-ocean.md)
- [Pydantic AI](../entities/tools/pydantic-ai.md)
- [OpenAI](../entities/organizations/openai.md)
- [Cole Medin](../entities/people/cole-medin.md)

## Key moments

- **[0:00:00]** Recap: last video introduced Crawl4AI in Python; this one rebuilds the RAG scraper in n8n with no code
- **[0:02:32]** Ethical scraping warning: check robots.txt and terms of use before crawling
- **[0:03:33]** Using sitemap.xml to discover every page URL on a site
- **[0:04:38]** Why Docker is needed: n8n can't pip-install, so Crawl4AI must be an API endpoint
- **[0:07:49]** Deploying Crawl4AI as a dedicated API on DigitalOcean App Platform from the DockerHub image
- **[0:10:36]** Config details: port 11235, bearer-token env var for endpoint security
- **[0:13:08]** Sponsor read: TEN Agent open-source voice/multimodal agent framework
- **[0:16:29]** Building the n8n workflow: fetch sitemap, convert XML to JSON, split into items, loop
- **[0:22:35]** First /crawl request returns a task ID (async scrape), not the page content
- **[0:23:39]** Polling pattern: wait 5s, hit /task/{id}, loop until status completed
- **[0:25:57]** Chunk markdown, embed with text-embedding-3-small, insert into Supabase vector store
- **[0:30:33]** 148 vectors inserted; scrape is genuinely async (some pages need multiple polls)
- **[0:31:22]** Minimal AI agent (GPT-4o-mini + Supabase vector tool) answers Pydantic AI questions from the KB

## Transcript

[Raw transcript](../raw/n8n-crawl4ai-scrape-any-website-in-minutes-with-no-code.md)
