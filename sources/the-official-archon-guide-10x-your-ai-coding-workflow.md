---
type: source
title: "The OFFICIAL Archon Guide - 10x Your AI Coding Workflow"
description: "Archon is a command center for AI coding that gives humans back control over the knowledge (RAG) and tasks that coding assistants otherwise handle opaquely under the hood, so you can collaborate with your agent instead of being kicked out of the driver's seat."
youtube_id: DMXyDpnzNpY
url: https://www.youtube.com/watch?v=DMXyDpnzNpY
slug: the-official-archon-guide-10x-your-ai-coding-workflow
published: 2025-10-11
duration: "0:23:19"
recency_rank: 63
raw: "../raw/the-official-archon-guide-10x-your-ai-coding-workflow.md"
tags: [archon, rag, mcp, workflow, knowledge-base]
created: 2026-07-21
updated: 2026-07-21
---

Cole introduces Archon as a tool to enable deep human-AI collaboration in the coding space, filling a gap left by coding assistants like Claude Code, Codex, and Kiro. The core problem is that those assistants take care of too much under the hood. They search the entire web for library documentation and maintain their own internal task lists, but you cannot pick which knowledge they search or interact with their tasks. Archon fixes this by being both a beautiful UI for managing projects, tasks, and curated knowledge, and an MCP server that connects to any AI coding assistant so it can search your private curated documentation (via keyword plus semantic RAG) and read and write the same Kanban task board with real-time updates.

The video then walks through a full setup: prerequisites (Docker, Supabase for the database with a free cloud tier or self-hosted local, and an LLM provider API key with OpenAI, Gemini, or Ollama support for fully local knowledge bases), cloning the stable branch, setting the Supabase URL and service role key in the .env, running the complete-setup.sql migration in Supabase's SQL editor, and spinning up three containers (UI, MCP server, API) with a single docker compose command. LLM chat and embedding providers are configured in the settings UI, the MCP connection is a one-line command (verified with claude mcp list), and recommended global rules are pasted into CLAUDE.md (or AGENTS.md for Codex) so the assistant knows how to use Archon.

The practical workflow section is the most important: it is up to you to define how Archon fits your process. Cole curates knowledge first by crawling library documentation, favoring optimal formats (llms.txt curated markdown lists, or sitemap.xml) over raw web pages, and can crawl multiple sources in parallel. He always splits work into planning and implementation, each packaged as a reusable slash command and markdown workflow. The plan command has the assistant read requirements, list crawled Archon sources, perform RAG over chunks and code examples, do codebase analysis, then produce a PRP-style implementation plan in a PRPs folder. The execute command tells the assistant to check global rules for an existing Archon project (or create one) and convert plan steps into managed Archon tasks moved live across the Kanban board. This gives observability and live editability, and crucially lets the agent write accurate code for libraries beyond its training cutoff (demonstrated by building a Pydantic AI agent that uses Mem0).

## Concepts covered

- [Knowledge Bases](../concepts/knowledge-bases.md)
- [Retrieval-Augmented Generation (RAG)](../concepts/rag.md)
- [Hybrid Search](../concepts/hybrid-search.md)
- [Model Context Protocol (MCP)](../concepts/mcp.md)
- [Human in the Loop](../concepts/human-in-the-loop.md)
- [Planning with AI](../concepts/planning-with-ai.md)
- [PRD-First Development](../concepts/prd-first-development.md)
- [Slash Commands](../concepts/slash-commands.md)
- [Agentic Workflow Engineering](../concepts/agentic-workflow-engineering.md)
- [Codebase Indexing](../concepts/codebase-indexing.md)
- [Global Rules](../concepts/global-rules.md)
- [Agentic Coding](../concepts/agentic-coding.md)

## Entities

- [Archon](../entities/tools/archon.md)
- [Cole Medin](../entities/people/cole-medin.md)
- [Claude Code](../entities/tools/claude-code.md)
- [Codex](../entities/tools/codex.md)
- [MCP (Model Context Protocol)](../entities/tools/mcp.md)
- [Supabase](../entities/tools/supabase.md)
- [Docker](../entities/tools/docker.md)
- [Pydantic AI](../entities/tools/pydantic-ai.md)
- [Mem0](../entities/tools/mem0.md)
- [Ollama](../entities/tools/ollama.md)
- [OpenAI](../entities/organizations/openai.md)

## Key moments

- **[0:00:00]** Archon introduced as a command center for AI coding, enabling deep human-AI collaboration via UI + MCP server
- **[0:01:37]** The core problem: coding assistants handle knowledge search and task lists opaquely under the hood, kicking humans out of the driver's seat
- **[0:03:06]** Demo showing Archon performing keyword + semantic RAG over curated docs and real-time task board updates
- **[0:04:46]** Quick-start setup begins: prerequisites (Docker, Supabase, LLM API key)
- **[0:07:18]** Database setup via complete-setup.sql in Supabase SQL editor, then docker compose up to build three containers
- **[0:09:44]** One-line MCP connection to Claude Code, verified with claude mcp list, plus recommended global rules pasted into CLAUDE.md
- **[0:12:06]** Supabase sponsor segment (Supabase Select conference, multigres, Series E)
- **[0:14:03]** Practical AI coding workflow: it's up to you to define how Archon fits your process
- **[0:15:22]** Curating knowledge: crawling docs, favoring llms.txt and sitemap.xml formats, parallel crawling
- **[0:17:23]** Splitting into planning vs implementation, packaged as reusable slash-command workflows
- **[0:20:44]** Execute command converts plan steps into managed Archon tasks moved live across the Kanban board
- **[0:21:54]** Payoff: Archon RAG lets the assistant write accurate code for libraries past its training cutoff (Pydantic AI + Mem0)

## Transcript

[Raw transcript](../raw/the-official-archon-guide-10x-your-ai-coding-workflow.md)
