---
type: entity
subtype: tool
title: "Serena"
description: "An open-source MCP server for semantic code retrieval and editing that outperforms a coding agent's built-in codebase search as the codebase grows."
resource: "https://github.com/oraios/serena"
tags: [search, retrieval]
videos: [a-complete-guide-to-claude-code-here-are-all-the-best-strategies]
created: 2026-07-21
updated: 2026-07-21
---

# Serena

Serena is an [MCP](../../concepts/mcp.md) server that replaces a coding agent's native codebase navigation with semantic retrieval and editing. Cole's definition is a direct comparison: "it does a lot of the things that Claude Code does to understand your codebase ... except it does it better. It is an MCP server that's all about semantic retrieval and editing your code" [0:15:07]. Where [Claude Code](./claude-code.md) reaches for [grep](./ripgrep.md) and file reads to locate the code a request touches, Serena resolves symbols and their relationships, so the agent finds the right file instead of scanning toward it.

The failure mode it fixes is scale. Text search is fine on a small repo and degrades badly on a large one, burning context on near-misses. Cole is specific about when it earns its place: "it's just going to have a much better understanding of our codebase, especially as our codebase gets larger. That's when cloud code can start to fall in its face and you want to have tools like Serena" [0:18:05]. That makes it a [brownfield](../../concepts/greenfield-vs-brownfield.md) tool above all, aimed at the existing-codebase work that generic agentic search handles worst.

Setup is two steps. Install uvx, add the server with a single `claude mcp add` command, and confirm it with `claude mcp list`. Then allowlist it in settings so the agent never stops to ask: the syntax is `mcp__serena`, which grants every tool on that server at once - Cole recommends the same for any MCP server you trust, and shows a full priming run where dozens of Serena calls execute without a single approval prompt.

The bigger lever is wiring it into your workflow rather than waiting for the agent to reach for it. Cole edited his [prime command](../../concepts/prime-command.md) to instruct the agent to use Serena when exploring the codebase, and to retry with Serena on error, since it occasionally fails. The [slash command](../../concepts/slash-commands.md) still runs `tree` and reads CLAUDE.md and the README first, then hands the real code exploration to Serena, and the resulting mental model of the repo is materially better.

## Realizes

- [Codebase Indexing](../../concepts/codebase-indexing.md) - Building a searchable index or map of a codebase so the agent can retrieve the right files instead of scanning everything.
- [Semantic Search](../../concepts/semantic-search.md) - Retrieving content by meaning rather than exact keywords.
- [Language Server Protocol](../../concepts/language-server-protocol.md) - Using LSP to give agents precise code navigation (definitions, references, symbols) instead of guessing from text.
- [Model Context Protocol (MCP)](../../concepts/mcp.md) - An open protocol for packaging tools, data, and RAG capabilities as servers that any AI coding assistant or agent can connect to and call with a standard interface.
- [Agentic Search](../../concepts/agentic-search.md) - An agent answering a question by reasoning across multiple search tools instead of relying on a single retrieval call.
- [Permission Management](../../concepts/permission-management.md) - Allowlisting the specific safe tools an agent may run unattended, here via the `mcp__serena` settings entry.

## Contrasts with

- [grep (command-line search)](./ripgrep.md) - The default CLI search Claude Code uses for agentic navigation; slow and token-inefficient past six-figure line counts.
- [When RAG Is (and Isn't) Dead](../../concepts/when-rag-is-dead.md) - The argument that agents navigating files directly often beat indexed retrieval for code; Serena is the counterweight once a repo gets large.
- [Context7](./context7.md) - A hosted MCP RAG server for library docs, external knowledge rather than your own codebase.

## Works with

- [Claude Code](./claude-code.md) - Anthropic's terminal-based agentic coding assistant, added via `claude mcp add` and allowlisted in settings.
- [Archon](./archon.md) - Cole's open-source AI command center, the other MCP server connected in the same walkthrough for knowledge and task management.

## Related

- [Prime Command](../../concepts/prime-command.md) - A reusable slash command that primes an agent with focused codebase understanding, rewritten here to route exploration through Serena.
- [Slash Commands](../../concepts/slash-commands.md) - User-defined command files that package a prompt and arguments into a callable shortcut inside the coding agent.
- [Greenfield vs. Brownfield](../../concepts/greenfield-vs-brownfield.md) - The branch point between building new and working in an existing codebase, where Serena pays off most.
- [Crawl4AI RAG MCP Server](./crawl4ai-rag-mcp.md) - Cole's own MCP server giving assistants external knowledge via RAG, a complementary retrieval layer.
- [Context Window Limits](../../concepts/context-window-limits.md) - Managing finite context by sizing what you load, the budget precise retrieval protects.

## Sources

- [A Complete Guide to Claude Code - Here are ALL the Best Strategies](../../sources/a-complete-guide-to-claude-code-here-are-all-the-best-strategies.md) - "[0:15:07] it does a lot of the things that Claude Code does to understand your codebase ... except it does it better. It is an MCP server that's all about semantic retrieval and editing your code."
- [A Complete Guide to Claude Code - Here are ALL the Best Strategies](../../sources/a-complete-guide-to-claude-code-here-are-all-the-best-strategies.md) - "[0:18:05] it's just going to have a much better understanding of our codebase, especially as our codebase gets larger."
