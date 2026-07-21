---
type: source
title: "AI Code That Fixes Itself (An MCP You Can Try Now)"
description: "Turning an open-source library's entire GitHub repo into a knowledge graph lets an MCP server deterministically detect and self-correct the function/parameter hallucinations that plague AI coding assistants."
youtube_id: 8Mib-hb6Fcg
url: https://www.youtube.com/watch?v=8Mib-hb6Fcg
slug: ai-code-that-fixes-itself-an-mcp-you-can-try-now
published: 2025-06-18
duration: "0:23:28"
recency_rank: 84
raw: "../raw/ai-code-that-fixes-itself-an-mcp-you-can-try-now.md"
tags: [knowledge-graphs, self-correction, guardrails, mcp, archon]
created: 2026-07-21
updated: 2026-07-21
---

# AI Code That Fixes Itself (An MCP You Can Try Now)

Cole demonstrates a new capability he added to his Crawl4AI RAG MCP server: parsing an entire GitHub repository (here, Pydantic AI) into a Neo4j knowledge graph of repositories, files, functions, classes, methods, and attributes. Because AI coding assistants routinely hallucinate methods and parameters that do not exist on a library's classes, this graph becomes a source of ground truth. A deterministic (no-LLM) hallucination-detection script walks the code an agent generated and checks every use of the library against the graph, flagging non-existent methods (e.g. a hallucinated `invoke_async`) and invalid parameters, then suggesting the correct call (e.g. `run_stream`).

By exposing this as MCP tools (run the hallucination check, query the knowledge graph, parse a GitHub repo), Cole gives Claude Code the ability to self-correct as it codes: research the docs via RAG, drill into exact method signatures via the knowledge graph, generate code, then validate against the detector and fix mistakes. He walks through a CLAUDE.md-defined multi-phase workflow (ensure sources exist, RAG research, knowledge-graph deep dive, generate, validate) and shows Claude Code build a working Pydantic AI agent first-try with zero hallucinations.

Cole is candid that the knowledge-graph strategy is experimental and still being refined, and that some domains (front-end via Lovable/Bolt.diy, browser automation via Browserbase/Stagehand) already have good self-correction built in and do not need this. The whole approach is a step toward Archon v2, a free and open-source overhaul that will combine task/project management, RAG strategies, and eventually this knowledge-graph hallucination detection into one MCP server for AI coding.

## Concepts covered

- [Knowledge Graphs](../concepts/knowledge-graphs.md)
- [Guardrails](../concepts/guardrails.md)
- [Self-Correcting Agents](../concepts/self-correction.md)
- [Validation](../concepts/validation.md)
- [Codebase Indexing](../concepts/codebase-indexing.md)
- [Retrieval-Augmented Generation (RAG)](../concepts/rag.md)
- [Agentic Workflow Engineering](../concepts/agentic-workflow-engineering.md)
- [The Problems With MCP Servers](../concepts/mcp-problems.md)

## Entities

- [Cole Medin](../entities/people/cole-medin.md)
- [Archon](../entities/tools/archon.md)
- [Crawl4AI RAG MCP Server](../entities/tools/crawl4ai-rag-mcp.md)
- [Neo4j](../entities/tools/neo4j.md)
- [Pydantic AI](../entities/tools/pydantic-ai.md)
- [Claude Code](../entities/tools/claude-code.md)
- [Windsurf](../entities/tools/windsurf.md)
- [GitHub](../entities/tools/github.md)
- [Browserbase](../entities/tools/browserbase.md)
- [bolt.diy](../entities/tools/bolt-diy.md)
- [Dynamous](../entities/organizations/dynamous.md)

## Key moments

- **[0:00:47]** Core idea introduced: combining knowledge graphs with AI coding assistants
- **[0:01:27]** Neo4j visualization of the Pydantic AI repo as a knowledge graph (repos, files, functions, classes, methods, attributes)
- **[0:02:35]** Concrete example: Windsurf + Claude 3.7 hallucinated invoke_async on the agent class
- **[0:03:55]** Deterministic (no-LLM) hallucination-check script finds the hallucination against the graph
- **[0:05:00]** Self-correction: agent finds run_stream is the real method, fixes code to 0% hallucination
- **[0:05:32]** Parameter-level detection: invalid function arguments are caught too
- **[0:07:00]** Caveat: some domains (front-end, browser automation) already have self-correction and don't need this
- **[0:09:52]** Back to the point: most hallucination-heavy use cases benefit from this MCP
- **[0:10:53]** This feeds into the Archon v2 overhaul teaser (tasks + RAG + knowledge graph)
- **[0:13:12]** Walkthrough of the three new MCP tools: run hallucination check, query graph, parse GitHub repo
- **[0:16:20]** CLAUDE.md defines a multi-phase workflow for using the MCP server
- **[0:20:13]** Claude Code builds a working Pydantic AI agent first-try with zero hallucinations

## Transcript

[Raw transcript](../raw/ai-code-that-fixes-itself-an-mcp-you-can-try-now.md)
