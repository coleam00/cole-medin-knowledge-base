---
type: concept
title: "Web Crawling & Ingestion"
description: "Crawling sites and documentation (sitemaps, recursion, parallelism) and converting them to clean markdown for a knowledge base."
tags: [crawling, scraping, ingestion]
videos: [should-i-build-my-ai-agents-with-n8n-or-python, make-rag-100x-better-with-real-time-knowledge-graphs, i-built-the-ultimate-rag-mcp-server-for-ai-coding-better-than-context7, turn-any-website-into-llm-knowledge-in-seconds-evolved, the-ultimate-n8n-rag-ai-agent-template-local-ai-edition, n8n-crawl4ai-scrape-any-website-in-minutes-with-no-code, turn-any-website-into-llm-knowledge-in-seconds, stop-paying-for-gpt-claude-other-llms-get-them-all-in-one-place, effortless-rag-in-n8n-use-all-your-files-pdfs-excel-and-more, no-code-rag-agents-you-have-to-check-out-n8n-langchain]
created: 2026-07-21
updated: 2026-07-21
---

# Web Crawling & Ingestion

Web crawling is the ingestion front end of a knowledge base: fetching pages from the internet and converting their raw HTML into clean markdown that a language model can actually read. It matters because most of what we teach agents comes from the web. "scraping the internet to create knowledge for our LLMs is really important because a lot of the knowledge we give our agents comes from the internet" [0:01:32], and the whole promise is to "extract LLM knowledge from any website that you want" [0:07:08]. The conversion step is the heart of it: a good crawler "takes this ugly HTML that we get when we visit the raw content of a web page and it turns it into markdown form which is actually even human readable format" [0:03:18]. Skipping that step poisons retrieval, since "imagine pasting all of this into an llm prompt I mean it's just a mess it's definitely going to hallucinate when you try to ask a question with all of the HTML tags" [0:06:35].

Crawlers discover URLs in a few standard ways. The most common is the sitemap: "if you go to the homepage and then add /sitemap.xml it's going to give you this XML which gives you the entire structure of the website" [0:07:55], and for "documentation pages and e-commerce stores you'll get this XML right here that gives you most of the time every single web page that is available on this site" [0:03:33]. A crawler should also accept an `llms.txt`, a sitemap, or just a base URL to recurse from: it "can also handle different types of URLs that you give it like the llm's.ext or sitemaps or even if it just needs to recursively scrape from a base URL" [0:05:19]. Behind a single command it may be "crawling hundreds of thousands of tokens and adding that all into our knowledge base" [0:17:03], which is where parallelism earns its keep.

Two disciplines keep ingestion healthy. First, crawl ethically: "there are a lot of websites that block scrapers and request you to not scrape and it is important to follow those rules" [0:02:32], and you check `robots.txt` to "understand when and how you can scrape" [0:02:48]. Second, keep the knowledge base consistent on re-ingest. Before inserting a file, "if we have already added the file to the knowledge base at some point I want to delete everything" [0:18:25], so that "when I update a file the knowledge base only only contains the updated information for that file and doesn't have anything from an old version hanging around" [0:18:39]. The hard part is rarely the crawl itself but the extraction: "the hardest part of the whole setup is really just actually extracting the text from the documents that you want to put in your knowledge base especially if you want to use PDFs or other document types that don't convert as easily to Raw text" [0:00:00].

## Part of

- [Knowledge Bases](./knowledge-bases.md) - crawling is how external web content enters the knowledge base in the first place.
- [Retrieval-Augmented Generation (RAG)](./rag.md) - crawled, cleaned markdown is the corpus RAG later chunks, embeds, and retrieves over.

## Contrasts with

- [No-Code vs. Code](./no-code-vs-code.md) - the ingestion path is a classic tradeoff: n8n "does not work very well for large files... I have had n8n choke, even with 20 megabyte PDF files" [0:08:40], while in Python "you can handle tens hundreds of gigabytes easily... as long as you have the memory in your machine" [0:09:16].
- [Structured vs. Unstructured Data](./structured-vs-unstructured-data.md) - crawling turns messy, unstructured HTML into cleaner text that downstream steps can structure.

## Implemented by

- [Crawl4AI](../entities/tools/crawl4ai.md) - open-source crawler that converts pages to clean markdown and handles sitemaps and recursion.
- [Crawl4AI RAG MCP Server](../entities/tools/crawl4ai-rag-mcp.md) - wraps crawling and ingestion behind an MCP server that accepts llms.txt, sitemaps, or a base URL.
- [n8n](../entities/tools/n8n.md) - no-code workflow tool used to orchestrate crawl-and-ingest pipelines.
- [LangChain](../entities/tools/langchain.md) - pairs with n8n to build no-code RAG ingestion flows.

## Related

- [Chunking](./chunking.md) - once a page is clean markdown, it is split into chunks for embedding.
- [Knowledge Graphs](./knowledge-graphs.md) - crawled episodes can feed a graph where "we have this dynamic creation of our knowledge graph just based on how the LLM is understanding the data" [0:10:52].
- [No-Code Automation](./no-code-automation.md) - crawling is a frequent building block in automated ingestion workflows.
- [Agentic Coding](./agentic-coding.md) - crawled documentation is a prime source of up-to-date context for coding agents.
- [llms.txt](./llms-txt.md) - An emerging convention where a project publishes all of its documentation as a single LLM-formatted page (llms.txt / llms-full.txt), so one fetch yields complete, chunk-ready knowledge for an agent.

## Sources

- [Turn ANY Website into LLM Knowledge in SECONDS](../sources/turn-any-website-into-llm-knowledge-in-seconds.md) - "[0:03:18] it takes this ugly HTML that we get when we visit the raw content of a web page and it turns it into markdown form which is actually even human readable format"
- [Turn ANY Website into LLM Knowledge in SECONDS](../sources/turn-any-website-into-llm-knowledge-in-seconds.md) - "[0:07:55] for most Pages out there on the internet right now if you go to the homepage and then add SLS sitemap.xml it's going to give you this XML which gives you the entire structure of the website"
- [Turn ANY Website into LLM Knowledge in Seconds - EVOLVED](../sources/turn-any-website-into-llm-knowledge-in-seconds-evolved.md) - "[0:01:32] scraping the internet to create knowledge for our LLMs is really important because a lot of the knowledge we give our agents comes from the internet"
- [Turn ANY Website into LLM Knowledge in Seconds - EVOLVED](../sources/turn-any-website-into-llm-knowledge-in-seconds-evolved.md) - "[0:05:17] the first main way that you can crawl websites is through what is called a sitemap... usually it's going to be /sitemap.xml"
- [n8n + Crawl4AI - Scrape ANY Website in Minutes with NO Code](../sources/n8n-crawl4ai-scrape-any-website-in-minutes-with-no-code.md) - "[0:02:32] you want to scrape ethically there are a lot of websites that block scrapers and request you to not scrape and it is important to follow those rules"
- [n8n + Crawl4AI - Scrape ANY Website in Minutes with NO Code](../sources/n8n-crawl4ai-scrape-any-website-in-minutes-with-no-code.md) - "[0:03:33] if you add /sitemap.xml to the end of a lot of websites like documentation pages and e-commerce stores you'll get this XML right here that gives you most of the time every single web page that is available on this site"
- [I Built the Ultimate RAG MCP Server for AI Coding (Better than Context7)](../sources/i-built-the-ultimate-rag-mcp-server-for-ai-coding-better-than-context7.md) - "[0:05:19] This MCP server can also handle different types of URLs that you give it like the llm's.ext or sitemaps or even if it just needs to recursively scrape from a base URL."
- [I Built the Ultimate RAG MCP Server for AI Coding (Better than Context7)](../sources/i-built-the-ultimate-rag-mcp-server-for-ai-coding-better-than-context7.md) - "[0:17:03] Under the hood, it actually is crawling hundreds of thousands of tokens and adding that all into our knowledge base."
- [The ULTIMATE n8n RAG AI Agent Template - Local AI Edition](../sources/the-ultimate-n8n-rag-ai-agent-template-local-ai-edition.md) - "[0:18:39] I want to absolutely guarantee that when I update a file the knowledge base only only contains the updated information for that file and doesn't have anything from an old version hanging around"
- [Effortless RAG in n8n - Use ALL Your Files (PDFs, Excel, and More)](../sources/effortless-rag-in-n8n-use-all-your-files-pdfs-excel-and-more.md) - "[0:00:00] the hardest part of the whole setup is really just actually extracting the text from the documents that you want to put in your knowledge base especially if you want to use PDFs or other document types that don't convert as easily to Raw text"
- [Should I Build My AI Agents with n8n or Python?](../sources/should-i-build-my-ai-agents-with-n8n-or-python.md) - "[0:09:16] you can handle tens hundreds of gigabytes easily in your Python code as long as you have the memory in your machine"
- [Make RAG 100x Better with Real-Time Knowledge Graphs](../sources/make-rag-100x-better-with-real-time-knowledge-graphs.md) - "[0:10:52] we have this dynamic creation of our knowledge graph just based on how the LLM is understanding the data that we are giving it. That's what makes it so powerful."
- [No Code RAG Agents? You HAVE to Check out n8n + LangChain](../sources/no-code-rag-agents-you-have-to-check-out-n8n-langchain.md) - "[0:13:09] this way I have control over exactly what I give to my agent to have knowledge of later on"
- [STOP Paying for GPT, Claude, & Other LLMs - Get them ALL in One Place](../sources/stop-paying-for-gpt-claude-other-llms-get-them-all-in-one-place.md) - "[0:05:25] you can actually summarize videos that you upload into the platform here not something I have seen before within a interface like this"
