---
type: source
title: "Anthropic Just Dropped a Masterclass on Building Agent Harnesses (for Large Codebases)"
description: "To make coding agents work in large codebases, invest in the AI layer (the harness) around the model, lean, layered global rules, scoped skills, self-improving hooks, symbol-level LSP search, and exploration subagents, because the harness matters as much as the model."
youtube_id: efRIrLXoOVA
url: https://www.youtube.com/watch?v=efRIrLXoOVA
slug: anthropic-just-dropped-a-masterclass-on-building-agent-harnesses-for-large-codebases
published: 2026-05-20
duration: "0:28:11"
recency_rank: 13
raw: "../raw/anthropic-just-dropped-a-masterclass-on-building-agent-harnesses-for-large-codebases.md"
tags: [harness-engineering, large-codebases, ai-layer, claude-code]
created: 2026-07-21
updated: 2026-07-21
---

# Anthropic Just Dropped a Masterclass on Building Agent Harnesses (for Large Codebases)

Cole walks through Anthropic's blog post on using Claude Code in large codebases and rebuilds every strategy into a concrete demo repo (the 'helpline' plugin). The core framing is that the harness matters as much as the model: what he calls the AI layer, the set of context and tools you give a coding agent, is a third component of every codebase alongside code and tests. Claude Code navigates codebases via agentic search (command-line tools like grep and folder walking), not RAG, semantic search, or a maintained index, so the whole game becomes curating enough up-front context that the agent knows where to look.

He maps seven parts of the AI layer to seven strategies. Global rules are the foundation (loaded the entire session) and must be kept lean and layered: a root CLAUDE.md plus subdirectory CLAUDE.md files that load progressively as the agent works in each slice, or you can initialize Claude Code directly in a subdirectory to hone its working directory (it still walks up the tree loading parent rules). Hooks make the setup self-improving: a stop hook runs a separate headless Claude session at the end of each turn to reflect on changes and propose CLAUDE.md updates so rules never go stale, while a session-start hook loads dynamic context (git state, or team docs from Confluence). Skills carry reusable workflows and can be scoped to specific paths so they only activate in relevant directories, the distinction being global rules are conventions/rules and skills are workflows.

Language Server Protocol, exposed to Claude via a custom MCP server, gives the agent the same symbol-level navigation (go-to-definition, find-references) a developer has in their IDE, essential past six-figure line counts where grep becomes slow and token-inefficient. Subagents split exploration from editing: dispatch web research or codebase exploration to a subagent with its own context window that returns only a summary, keeping the primary session's context clean before it edits. Cole closes with Anthropic's organizational advice, assign a small team to champion a quiet buildout of the AI layer, then roll out a single standard so everyone gets consistent results rather than each dev evolving their own.

## Concepts covered

- [The AI Layer](../concepts/the-ai-layer.md)
- [AI Coding Harness](../concepts/ai-coding-harness.md)
- [Agentic Search](../concepts/agentic-search.md)
- [When RAG Is (and Isn't) Dead](../concepts/when-rag-is-dead.md)
- [Codebase Indexing](../concepts/codebase-indexing.md)
- [Global Rules](../concepts/global-rules.md)
- [Progressive Disclosure](../concepts/progressive-disclosure.md)
- [Claude Code Hooks](../concepts/claude-code-hooks.md)
- [Self-Evolving Memory](../concepts/self-evolving-memory.md)
- [Skills](../concepts/skills.md)
- [Language Server Protocol](../concepts/language-server-protocol.md)
- [Subagents Pattern](../concepts/subagents-pattern.md)
- [Context Isolation](../concepts/context-isolation.md)
- [Context Engineering](../concepts/context-engineering.md)

## Entities

- [Anthropic](../entities/organizations/anthropic.md)
- [Claude Code](../entities/tools/claude-code.md)
- [MCP (Model Context Protocol)](../entities/tools/mcp.md)
- [grep (command-line search)](../entities/tools/ripgrep.md)
- [Cole Medin](../entities/people/cole-medin.md)
- [Dynamous](../entities/organizations/dynamous.md)
- [Jira](../entities/tools/jira.md)
- [GitHub](../entities/tools/github.md)

## Key moments

- **[0:01:52]** How Claude Code navigates a codebase before an AI layer: agentic search with CLI tools, no RAG or indexing
- **[0:02:56]** Central thesis: the harness matters as much as the model, 'the AI layer'
- **[0:03:28]** Defining the AI layer as a third codebase component (code + tests + AI layer); seven parts map to seven strategies
- **[0:04:56]** Keep global rules lean and layered; subdirectory CLAUDE.md files load progressively
- **[0:07:00]** Initialize Claude Code inside a subdirectory to hone the working directory; it still walks up loading parent CLAUDE.md files
- **[0:10:37]** Hooks section begins: making the AI layer self-improving
- **[0:11:08]** Stop hook reflects on the session and proposes CLAUDE.md updates in headless mode
- **[0:15:14]** Skills section: scoping skills to specific paths; rules vs workflows distinction
- **[0:18:12]** LSP via a custom MCP server for symbol-level search (definitions/references)
- **[0:21:57]** Subagents split exploration from editing to protect the primary context window
- **[0:24:09]** The helpline plugin: install the whole harness in two commands
- **[0:26:19]** Anthropic's org advice: assign ownership, quiet investment period, one AI-layer standard

## Transcript

[Raw transcript](../raw/anthropic-just-dropped-a-masterclass-on-building-agent-harnesses-for-large-codebases.md)
