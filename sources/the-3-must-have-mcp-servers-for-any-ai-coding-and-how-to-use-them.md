---
type: source
title: "The 3 MUST Have MCP Servers for Any AI Coding (and How to Use Them)"
description: "Every AI coding workflow should run on three core MCP servers, a RAG documentation knowledge base, a database manager, and a web search, used together from the very start of a build so the assistant has real knowledge before it writes any code."
youtube_id: MBaTuJfICP4
url: https://www.youtube.com/watch?v=MBaTuJfICP4
slug: the-3-must-have-mcp-servers-for-any-ai-coding-and-how-to-use-them
published: 2025-05-14
duration: "0:19:57"
recency_rank: 92
raw: "../raw/the-3-must-have-mcp-servers-for-any-ai-coding-and-how-to-use-them.md"
tags: [mcp, ai-coding, rag, workflow]
created: 2026-07-21
updated: 2026-07-21
---

# The 3 MUST Have MCP Servers for Any AI Coding (and How to Use Them)

Cole argues that a reliable AI coding workflow rests on three categories of MCP server that he uses no matter what he's building. The first brings external knowledge (library and tool docs) into the assistant as a RAG knowledge base, he recommends the Crawl4AI RAG MCP server he built himself, which crawls any documentation site and stores it in your own private Supabase, with Context7 as a more out-of-the-box alternative. The second manages your database in natural language: the Supabase MCP server can create tables, list projects, and run any SQL query so the assistant provisions the backend, not just the code (Neon's serverless-Postgres MCP is a similar option). The third is web search via the Brave MCP server, used in tandem with the RAG server to pull supplemental resources like forum posts and examples the knowledge base missed.

He then does a live build to show the servers working together: a RAG AI agent built with Pydantic AI and Supabase, with a local-folder ingestion pipeline and a Streamlit chat interface. The setup mirrors his full AI-coding process, global/workspace rules that tell the assistant how to use the MCP servers, a planning file, and a task file, so his kickoff prompt can stay high-level. He stresses giving concrete examples (a past Streamlit interface, pre-written SQL) as a major lever, and being explicit that the assistant must use the MCP servers at the very start so it has documentation before writing code, not after.

The agent reads the planning and task files, fires multiple RAG queries against the crawled Pydantic AI and Supabase docs, pulls integration examples via Brave, then scaffolds a full application with tests. It wasn't perfect, it created a stray task file, needed a re-ask to actually run the Supabase migration, and the chunker/ingestion needed fixes, but the Pydantic AI and Supabase code came out error-free because it leveraged the docs. After ~20 minutes of off-camera iteration he has a working Streamlit app that ingests a document into Supabase and answers questions over it, all in under an hour.

## Concepts covered

- [Model Context Protocol (MCP)](../concepts/mcp.md)
- [Agentic RAG](../concepts/agentic-rag.md)
- [Knowledge Bases](../concepts/knowledge-bases.md)
- [Stacking Context-Engineering Strategies](../concepts/strategy-stacking.md)
- [Global Rules](../concepts/global-rules.md)
- [Planning with AI](../concepts/planning-with-ai.md)
- [Reduce Assumptions](../concepts/reduce-assumptions.md)
- [Context Engineering](../concepts/context-engineering.md)
- [Multi-Query RAG](../concepts/multi-query-rag.md)
- [Human in the Loop](../concepts/human-in-the-loop.md)

## Entities

- [MCP (Model Context Protocol)](../entities/tools/mcp.md)
- [Archon](../entities/tools/archon.md)
- [Context7](../entities/tools/context7.md)
- [Supabase](../entities/tools/supabase.md)
- [Neon](../entities/tools/neon.md)
- [Brave Search API](../entities/tools/brave-search.md)
- [Pydantic AI](../entities/tools/pydantic-ai.md)
- [Windsurf](../entities/tools/windsurf.md)
- [Streamlit](../entities/tools/streamlit.md)
- [Dynamous](../entities/organizations/dynamous.md)
- [Cole Medin](../entities/people/cole-medin.md)

## Key moments

- **[0:00:00]** Intro: current AI coding workflow revolves around three core MCP servers, plus a live build
- **[0:01:11]** Server 1, external knowledge / RAG for docs; recommends his own Crawl4AI RAG MCP server (private Supabase), Context7 as alternative
- **[0:02:28]** Server 2, database management; Supabase MCP server creates tables and runs SQL, Neon as alternative
- **[0:03:41]** Server 3, web search via Brave MCP, used in tandem with RAG for supplemental resources
- **[0:05:16]** Configuring MCP servers in Windsurf's cascade JSON; all three have generous free tiers
- **[0:06:54]** DataButton sponsor segment
- **[0:08:34]** Live build setup: workspace rules, planning file (made with Claude desktop), task file
- **[0:10:39]** Walkthrough of the kickoff prompt, read planning/task first, give examples, use MCP servers at the start
- **[0:13:05]** Agent runs: reads planning/tasks, performs multiple RAG queries, uses Brave for integration examples, scaffolds the app
- **[0:15:57]** Post-build fixes: had to re-ask for the Supabase migration; fixed chunker/ingestion; Pydantic/Supabase code was error-free
- **[0:17:07]** Working Streamlit demo: upload a doc, five chunks into Supabase, agent answers over the knowledge base

## Transcript

[Raw transcript](../raw/the-3-must-have-mcp-servers-for-any-ai-coding-and-how-to-use-them.md)
