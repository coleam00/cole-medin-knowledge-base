---
type: entity
subtype: tool
title: "grep (command-line search)"
description: "The default CLI search Claude Code uses for agentic navigation; the video argues it becomes slow and token-inefficient past six-figure line counts, motivating LSP."
resource: "https://github.com/BurntSushi/ripgrep"
tags: [code-search, cli, agentic-coding]
videos: [anthropic-just-dropped-a-masterclass-on-building-agent-harnesses-for-large-codebases, everything-you-thought-about-building-ai-agents-is-wrong, why-the-best-ai-coding-tools-abandoned-rag-and-what-they-use-instead]
created: 2026-07-21
updated: 2026-07-21
---

# grep (command-line search)

grep (and its faster cousin ripgrep) is the plain command-line search that modern coding agents lean on to find their way around a codebase, the same way a human engineer would. As Cole describes the harness pattern, an agent "is going to navigate a codebase more as an engineer would with command line tools like GP, just looking at the folder structure" ([0:02:08]). This is the concrete mechanism behind the shift away from vector search: instead of embedding a repo and retrieving chunks, the agent runs literal text searches over the files. "Coding agents especially stopped using vector databases. They were using tools like Grep" ([0:13:39]), and those tools now ship "built right into the operating system like Rip Grep and Glob" ([0:05:16]), wired directly into the agent's toolset.

## How Cole uses it / why it matters

grep is the workhorse of [agentic search](../../concepts/agentic-search.md) and the reason Cole argues [RAG is (and isn't) dead](../../concepts/when-rag-is-dead.md) for coding. The insight from the [AI coding harness](../../concepts/ai-coding-harness.md) videos is that for a codebase an agent can navigate, exploring folder structure and grepping for symbols beats maintaining a brittle [codebase index](../../concepts/codebase-indexing.md) of embeddings. Because these search primitives are so central, "that's why we see all of this built directly into the SDKs for smaller corpuses of knowledge" ([0:13:52]) rather than bolted on as an external retrieval service.

But Cole is careful not to oversell it. grep has a scaling ceiling: "Grep by itself is going to be slow and really token inefficient as you're trying to navigate through a codebase" ([0:20:48]) once the repo grows past six figures of lines, because the agent burns context reading noisy match output and re-searching. That limitation is the motivation for pairing grep with structured tools, the [Language Server Protocol](../../concepts/language-server-protocol.md) in particular, which lets the agent jump to definitions and references semantically instead of scanning text. The practical takeaway across these videos: grep is the right default for small-to-medium codebases and the entry point of the harness, but on large codebases it becomes a supplement to LSP-driven navigation rather than the whole answer.

## Related

- [Agentic Search](../../concepts/agentic-search.md) - grep is the canonical primitive that makes agentic (search-as-you-go) navigation work.
- [When RAG Is (and Isn't) Dead](../../concepts/when-rag-is-dead.md) - the argument that coding agents replaced vector retrieval with command-line search.
- [AI Coding Harness](../../concepts/ai-coding-harness.md) - grep and glob are the built-in tools the harness gives the agent.
- [Codebase Indexing](../../concepts/codebase-indexing.md) and [Language Server Protocol](../../concepts/language-server-protocol.md) - the structured alternatives that pick up where grep gets slow on large repos.
- [Keyword Search](../../concepts/keyword-search.md) and [RAG](../../concepts/rag.md) - the retrieval approaches grep is defined against.
- [Skills](../../concepts/skills.md) and [Subagents Pattern](../../concepts/subagents-pattern.md) - the wider harness capabilities grep-based navigation feeds into.
- Sibling tools: [Brave Search API](./brave-search.md) and [SearXNG](./searxng.md) (search the web rather than a local codebase).

## Sources

- [Anthropic Just Dropped a Masterclass on Building Agent Harnesses (for Large Codebases)](../../sources/anthropic-just-dropped-a-masterclass-on-building-agent-harnesses-for-large-codebases.md) - "[0:02:08] It's going to navigate a codebase more as an engineer would with command line tools like GP, just looking at the folder structure."
- [Anthropic Just Dropped a Masterclass on Building Agent Harnesses (for Large Codebases)](../../sources/anthropic-just-dropped-a-masterclass-on-building-agent-harnesses-for-large-codebases.md) - "[0:20:48] Grep by itself is going to be slow and really token inefficient as you're trying to navigate through a codebase."
- [Everything You Thought About Building AI Agents is Wrong](../../sources/everything-you-thought-about-building-ai-agents-is-wrong.md) - "[0:13:39] Coding agents especially stopped using vector databases. They were using tools like Grep."
- [Everything You Thought About Building AI Agents is Wrong](../../sources/everything-you-thought-about-building-ai-agents-is-wrong.md) - "[0:13:52] that's why we see all of this built directly into the SDKs for smaller corpuses of knowledge."
- [Why the Best AI Coding Tools Abandoned RAG (And What They Use Instead)](../../sources/why-the-best-ai-coding-tools-abandoned-rag-and-what-they-use-instead.md) - "[0:05:16] They have access to all these pretty powerful search tools built right into the operating system like Rip Grep and Glob."
