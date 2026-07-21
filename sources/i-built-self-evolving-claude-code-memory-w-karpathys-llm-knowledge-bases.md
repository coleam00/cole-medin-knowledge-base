---
type: source
title: "I Built Self-Evolving Claude Code Memory w/ Karpathy's LLM Knowledge Bases"
description: "Karpathy's LLM-wiki pattern for organizing external knowledge can be inverted to give Claude Code a self-evolving, per-codebase memory built entirely from Claude Code hooks and the Claude Agent SDK."
youtube_id: 7huCP6RkcY4
url: https://www.youtube.com/watch?v=7huCP6RkcY4
slug: i-built-self-evolving-claude-code-memory-w-karpathys-llm-knowledge-bases
published: 2026-04-06
duration: "0:19:24"
recency_rank: 21
raw: "../raw/i-built-self-evolving-claude-code-memory-w-karpathys-llm-knowledge-bases.md"
tags: [memory-systems, self-evolving-memory, knowledge-bases, claude-code]
created: 2026-07-21
updated: 2026-07-21
---

# I Built Self-Evolving Claude Code Memory w/ Karpathy's LLM Knowledge Bases

Cole walks through Andrej Karpathy's viral LLM-knowledge-base playbook and its compiler analogy: raw source markdown (articles, papers, transcripts dumped into a `raw/` folder) is processed by an LLM 'compiler' into a queryable wiki 'executable' with cross-linked concept pages and an auto-maintained `index.md`, with a lint/test step that catches stale data and broken links, and a runtime step where the agent queries the wiki. A key insight from Karpathy is that no fancy RAG or vector database is needed because the LLM is good at maintaining index files the agent navigates directly, using Obsidian's graph view of back-links to traverse and connect knowledge.

Cole's contribution is applying the exact same architecture to INTERNAL data instead of external data: giving Claude Code a memory that evolves with your codebase. Session logs (captured automatically via Claude Code hooks) play the role of the raw folder; the Claude Agent SDK runs as a separate background process to summarize each conversation into daily logs, then a once-a-day flush extracts concepts and connections into the wiki. The whole system is driven purely by three hooks (SessionStart loads agents.md global rules plus the index; PreCompact and SessionEnd summarize the transcript before context is lost) and requires no extra installs or integrations.

The payoff is a compounding loop: every question makes the agent synthesize across wiki articles, and every answer and future session feeds new knowledge back in, so retrieval gets better over time with zero manual maintenance. Because agents.md documents the whole system to the agent, Claude Code can even customize its own memory prompts. Cole notes you can one-shot the whole setup by pasting Karpathy's PRD-style prompt (or his own repo's quick-start prompt) into Claude Code.

## Concepts covered

- [The LLM Wiki](../concepts/the-llm-wiki.md)
- [Self-Evolving Memory](../concepts/self-evolving-memory.md)
- [Memory Systems](../concepts/memory-systems.md)
- [When RAG Is (and Isn't) Dead](../concepts/when-rag-is-dead.md)
- [Progressive Disclosure](../concepts/progressive-disclosure.md)
- [Knowledge Graphs](../concepts/knowledge-graphs.md)
- [Validation](../concepts/validation.md)
- [Claude Code Hooks](../concepts/claude-code-hooks.md)
- [Global Rules](../concepts/global-rules.md)
- [Second Brain](../concepts/second-brain.md)
- [The Ralph Loop](../concepts/the-ralph-loop.md)
- [PRD-First Development](../concepts/prd-first-development.md)

## Entities

- [Andrej Karpathy](../entities/people/andrej-karpathy.md)
- [Obsidian](../entities/tools/obsidian.md)
- [Claude Code](../entities/tools/claude-code.md)
- [Claude Agent SDK](../entities/tools/claude-agent-sdk.md)
- [Dynamous](../entities/organizations/dynamous.md)
- [Cole Medin](../entities/people/cole-medin.md)

## Key moments

- **[0:00:00]** Framing: LLM knowledge bases originated from a Karpathy tweet
- **[0:01:16]** Key twist: Cole's system works on INTERNAL codebase data, not external data
- **[0:02:22]** The compiler analogy introduced (raw -> compiler -> executable -> runtime)
- **[0:04:31]** Lint/test suite over documents: gaps, stale data, broken links, data integrity
- **[0:05:17]** No fancy RAG needed; LLM auto-maintains the index file, agent navigates directly
- **[0:07:07]** agents.md as global rules describing the whole knowledge system to the agent
- **[0:07:39]** One-shot setup by pasting Karpathy's PRD-style prompt into a coding agent
- **[0:08:44]** Session logs captured by hooks are the raw folder; Claude Agent SDK extracts structured knowledge
- **[0:12:41]** Walkthrough of the three hooks: SessionStart, PreCompact, SessionEnd
- **[0:15:41]** Daily flush extracts concepts and connections from logs into the wiki
- **[0:16:44]** Self-contained system that can improve itself via agents.md awareness
- **[0:16:58]** The compounding loop: knowledge base grows and retrieval improves over time

## Transcript

[Raw transcript](../raw/i-built-self-evolving-claude-code-memory-w-karpathys-llm-knowledge-bases.md)
