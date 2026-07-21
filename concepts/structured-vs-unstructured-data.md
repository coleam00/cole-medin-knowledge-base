---
type: concept
title: "Structured vs Unstructured Data"
description: "Choosing the right representation for RAG, keeping tabular data queryable as SQL while formatting prose as markdown, rather than forcing everything through vector search."
tags: [rag, structured-data, sql, markdown, data-modeling]
videos: [i-love-the-karpathy-llm-wiki-but-it-doesnt-scale-heres-what-does, why-the-best-ai-coding-tools-abandoned-rag-and-what-they-use-instead, the-only-ai-tech-stack-you-need-in-2026, turn-any-file-into-llm-knowledge-in-seconds, your-ultimate-n8n-rag-ai-agent-template-just-got-a-massive-upgrade, introducing-rag-20-agentic-rag-knowledge-graphs-free-template, turn-any-website-into-llm-knowledge-in-seconds-evolved, the-ultimate-n8n-rag-ai-agent-template-local-ai-edition, i-built-the-ultimate-n8n-rag-ai-agent-template, the-future-of-rag-is-agentic-learn-this-strategy-now, effortless-rag-in-n8n-use-all-your-files-pdfs-excel-and-more]
created: 2026-07-21
updated: 2026-07-21
---

# Structured vs Unstructured Data

Structured versus unstructured data is the modeling decision that governs how a document should be represented before an agent can query it, and it is the single question that decides whether RAG is the right tool at all. Cole frames it directly: "So the question is rag dead? The answer for you depends entirely on your data. How structured is it? So code is a good example of very structured data" [0:01:57]. Unstructured data is prose: "With our searching of unstructured data, unlike something like code, we have ambiguous natural language. We want to be able to find synonyms and find text that's similar based on conceptual meaning" [0:02:13]. That ambiguity is exactly what semantic vector search is built for. Structured data, by contrast, has a schema and precise semantics that vector search mangles.

## Why it matters

Forcing everything through vector search fails on tables. "rag usually does absolutely terribly with tables... because one rag just pulls relevant chunks and those chunks might only be a part of the table" [0:08:13]. If a table is large, RAG returns a fraction of its rows and any aggregate computed from that fragment is wrong. The fix is to keep tabular data queryable: give the agent "a tool... specifically allowing it to generate SQL queries to calculate things like sums and averages and maximums over this tabular data. That's the kind of thing that rag normally completely falls on its face with" [0:12:23]. In practice the same file is often stored both ways, as chunked text for semantic lookup and as rows the agent can query with SQL.

## How it works

For unstructured prose, the winning move is to normalize everything into markdown, "typically considered the best format for LLMs" [0:04:28], then chunk and embed it. For structured tabular data, the file is loaded so the agent can "treat Excel and CSV files as SQL tables so it can write SQL queries" [0:08:45], and Cole increasingly reaches for SQL and Postgres as defaults because "LLMs understand SQL a lot more than writing queries for NoSQL" [0:03:31]. Adding an explicit schema on top of raw key-value data is what lets an agent reason at all: "we're starting to specify a schema here. We're building the structure as the context layer on top of the database, like the different types that we have, how things are related" [0:11:41]. The same underlying data can even be projected into multiple stores at once, a vector database and a knowledge graph, "representing it very differently. So the agent can reason to itself" [0:09:36].

## Contrasts with

- [Chunking](./chunking.md) - the right approach for unstructured prose, and the wrong one for tables that need to stay queryable.
- [RAG](./rag.md) - semantic retrieval shines on unstructured data and stumbles on structured data.

## Related

- [Agentic RAG](./agentic-rag.md) - gives the agent a choice of tools (SQL query, vector search) matched to the data type.
- [Knowledge Bases](./knowledge-bases.md) - often hold both representations of the same source.
- [Knowledge Graphs](./knowledge-graphs.md) - the structured, relationship-first representation stored alongside vectors.
- [Vector Embeddings](./vector-embeddings.md) - the representation for the unstructured half.
- [Keyword Search](./keyword-search.md) - precise matching that complements semantic search on more structured text.
- [Code Execution](./code-execution.md) - letting the agent run queries over structured data rather than retrieve it.
- [Context Engineering](./context-engineering.md) - the schema-as-context layer that makes structured data legible to an agent.
- [Web Crawling & Ingestion](./web-crawling.md) - the crawl step that yields markdown-normalized unstructured data.
- [When RAG Is (and Isn't) Dead](./when-rag-is-dead.md) - the "is RAG dead" debate resolves to this data-structure question.

## Tools

- [Docling](../entities/tools/docling.md) - converts many file types into markdown, "all of the different file types we're working with, they all just end up as markdown" [0:09:39].
- [Crawl4AI](../entities/tools/crawl4ai.md) - produces AI-ready markdown from webpages instead of raw HTML.
- [Supabase](../entities/tools/supabase.md) - Postgres-backed, holding both SQL tables and pgvector RAG in one platform.
- [Neon](../entities/tools/neon.md) - serverless Postgres used as the structured store behind agentic RAG.

## Sources

- [Why the Best AI Coding Tools Abandoned RAG (And What They Use Instead)](../sources/why-the-best-ai-coding-tools-abandoned-rag-and-what-they-use-instead.md) - "[0:01:57] So the question is rag dead? The answer for you depends entirely on your data. How structured is it? So code is a good example of very structured data."
- [The ULTIMATE n8n RAG AI Agent Template - Local AI Edition](../sources/the-ultimate-n8n-rag-ai-agent-template-local-ai-edition.md) - "[0:08:13] we're going to be testing with tabular data because rag usually does absolutely terribly with tables ... because one rag just pulls relevant chunks and those chunks might only be a part of the table"
- [Your ULTIMATE n8n RAG AI Agent Template just got a Massive Upgrade](../sources/your-ultimate-n8n-rag-ai-agent-template-just-got-a-massive-upgrade.md) - "[0:12:23] we're giving a tool for our agents specifically allowing it to generate SQL queries to calculate things like sums and averages and maximums over this tabular data. That's the kind of thing that rag normally completely falls on its face with."
- [The ONLY AI Tech Stack You Need in 2026](../sources/the-only-ai-tech-stack-you-need-in-2026.md) - "[0:03:31] I switched a lot more to SQL recently because it's definitely the industry standard for building AI agents. And I feel like LLMs understand SQL a lot more than writing queries for NoSQL"
- [I Love the Karpathy LLM Wiki but it Doesn't Scale. Here's What Does.](../sources/i-love-the-karpathy-llm-wiki-but-it-doesnt-scale-heres-what-does.md) - "[0:11:41] we're starting to specify a schema here. We're building the structure as the context layer on top of the database, like the different types that we have, how things are related"
- [Turn ANY File into LLM Knowledge in SECONDS](../sources/turn-any-file-into-llm-knowledge-in-seconds.md) - "[0:04:28] Markdown is typically considered the best format for LLMs like I said at the start of this video."
- [Introducing RAG 2.0: Agentic RAG + Knowledge Graphs (FREE Template)](../sources/introducing-rag-20-agentic-rag-knowledge-graphs-free-template.md) - "[0:09:36] We're storing the same data in a vector database and then also in a knowledge graph representing it very differently. So the agent can reason to itself."
- [I Built the ULTIMATE n8n RAG AI Agent Template](../sources/i-built-the-ultimate-n8n-rag-ai-agent-template.md) - "[0:02:19] you need to add tables differently from csvs and Excel files to the knowledge base compared to other things you can't just treat it as a text document CU you have to be able to query that table"
- [Turn ANY Website into LLM Knowledge in Seconds - EVOLVED](../sources/turn-any-website-into-llm-knowledge-in-seconds-evolved.md) - "[0:03:49] I could just take the raw HTML of this page and give it to an LLM, but it's not going to be able to pick out different sections very well"
- [The Future of RAG is Agentic - Learn this Strategy NOW](../sources/the-future-of-rag-is-agentic-learn-this-strategy-now.md) - "[0:38:18] I have reg for this function right here and then also structur data that I have to store in a SQL database used in this function all in the same platform because I am using Supabase"
- [Effortless RAG in n8n - Use ALL Your Files (PDFs, Excel, and More)](../sources/effortless-rag-in-n8n-use-all-your-files-pdfs-excel-and-more.md) - "[0:16:09] there's a lot of different things you can do to play around with how you inest documents in a table format like this I would say a lot of it depends on your use case"
