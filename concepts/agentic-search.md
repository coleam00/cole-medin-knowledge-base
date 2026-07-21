---
type: concept
title: "Agentic Search"
description: "An agent answering a question by reasoning across multiple search tools and full-document fallbacks instead of relying on a single retrieval call."
tags: [agents, search, web-search, retrieval, agentic-search, codebase-search]
videos: [anthropic-just-dropped-a-masterclass-on-building-agent-harnesses-for-large-codebases, the-subagent-era-is-officially-here-learn-this-now, why-the-best-ai-coding-tools-abandoned-rag-and-what-they-use-instead, your-ai-coding-workflow-needs-this-new-agent-browser-cli, i-built-the-ultimate-n8n-rag-ai-agent-template, pydantic-ai-deepseek-v3-the-best-ai-agent-combo, weve-been-building-ai-agents-wrong-until-now]
created: 2026-07-21
updated: 2026-07-21
---

# Agentic Search

"The tool out of the box, it uses something called a gentic search. So we're not performing traditional rag or semantic search. There's no codebase indexing with cloud code" [0:01:52]. Agentic search is retrieval by navigation: instead of embedding a corpus into a vector index and pulling the nearest chunks, the agent is handed direct tools (list files, read a file, grep, browse the web) and reasons its way to the right information one call at a time. Cole notes the same idea in the coding-tool context: "We're giving our agent these tools directly in the terminal to navigate through our file structure and view our code. And so this is technically still rag."

## How it works

The agent chains tool calls to assemble context on demand: "if I'm going to get the contents of this file I need to first get the structure of the repo to know where all the files are then pick out the one I need to analyze get the contents of it." The upside is that there is no index to build or keep in sync, which matters enormously for large, fast-moving codebases. The tradeoff is the flip side of that coin: "claude works best when it has enough starting context to know where to look." A full-document listing is a natural fallback, "if a rag lookup fails for whatever reason then instead of doing that lookup we can look at the files available" and read a file wholesale.

Because search is exploratory rather than a single vector lookup, agentic search pairs naturally with strategies that manage the volume of context it uncovers, like farming exploration out to [subagents](./subagents-pattern.md) so the main thread stays clean.

## Contrasts with

- [When RAG Is Dead](./when-rag-is-dead.md) - the argument that agentic navigation is replacing index-based retrieval for coding.
- [Codebase Indexing](./codebase-indexing.md) - the vector-index approach agentic search deliberately avoids ("no index that you have to keep in sync").
- [Traditional RAG](./traditional-rag.md) - one-shot semantic retrieval before the model runs.

## Builds on

- [Retrieval-Augmented Generation (RAG)](./rag.md) - agentic search is "technically still rag"; grounding via retrieved context, just retrieved by tool calls.
- [Tool Use](./tool-use.md) - the ability to call file, grep, and web tools is what makes the loop work.

## Related

- [Agentic RAG](./agentic-rag.md) - the same reason-then-retrieve loop over a knowledge base rather than a filesystem or the web.
- [Keyword Search](./keyword-search.md) - grep and regex are the exact-term backbone of codebase agentic search.
- [Subagents Pattern](./subagents-pattern.md), [Context Isolation](./context-isolation.md) - how the exploration cost is kept off the main context window.
- [Memory Systems](./memory-systems.md), [Global Rules](./global-rules.md), [Prime Command](./prime-command.md), [Tool Design](./tool-design.md) - the starting context and tooling that make agentic search effective.

## Tools

- [Claude Code](../entities/tools/claude-code.md) - ships agentic search by default; earlier versions used a local vector database before switching.
- [Ripgrep](../entities/tools/ripgrep.md) - "a directed and focused search and that's definitely better when working with a codebase."
- [Pydantic AI](../entities/tools/pydantic-ai.md), [n8n](../entities/tools/n8n.md) - used to build agents that list and read documents as a retrieval fallback.

## Sources

- [Anthropic Just Dropped a Masterclass on Building Agent Harnesses (for Large Codebases)](../sources/anthropic-just-dropped-a-masterclass-on-building-agent-harnesses-for-large-codebases.md) - "[0:01:52] The tool out of the box, it uses something called a gentic search. So we're not performing traditional rag or semantic search. There's no codebase indexing with cloud code."
- [Why the Best AI Coding Tools Abandoned RAG (And What They Use Instead)](../sources/why-the-best-ai-coding-tools-abandoned-rag-and-what-they-use-instead.md) - "[0:07:35] early versions of cloud code actually did use rag with a local vector database, but they found pretty quickly that a gentic search generally works better."
- [I Built the ULTIMATE n8n RAG AI Agent Template](../sources/i-built-the-ultimate-n8n-rag-ai-agent-template.md) - "[0:04:00] if a rag lookup fails for whatever reason then instead of doing that lookup we can look at the files available"
- [Pydantic AI + DeepSeek V3 - The BEST AI Agent Combo](../sources/pydantic-ai-deepseek-v3-the-best-ai-agent-combo.md) - "[0:06:11] I need to first get the structure of the repo to know where all the files are then pick out the one I need to analyze get the contents of it and then get the answer for the user"
- [The Subagent Era Is Officially Here - Learn this Now](../sources/the-subagent-era-is-officially-here-learn-this-now.md) - "[0:10:26] I don't want to just dive right in and say like, hey, look at my codebase and try to find the right files to address this feature. I want to use sub agents"
- [Your AI Coding Workflow NEEDS This New Agent Browser CLI](../sources/your-ai-coding-workflow-needs-this-new-agent-browser-cli.md) - "[0:03:11] old approaches like with the playright MCP, they use selectors and searching... it's non-deterministic. The agent doesn't understand the structure of the site. They just know how to search."
- [We've Been Building AI Agents WRONG Until Now](../sources/weve-been-building-ai-agents-wrong-until-now.md) - "[0:06:48] we'll be building a web search agent it's one of the hottest kind of Agents right now it's just so important to connect your agent to the real world with web search"
