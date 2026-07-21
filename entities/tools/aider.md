---
type: entity
subtype: tool
title: "Aider"
description: "An early AI coding driver Rasmus used when first developing the PRP framework."
resource: "https://aider.chat"
tags: [coding-agent, open-source, terminal]
videos: [why-the-best-ai-coding-tools-abandoned-rag-and-what-they-use-instead, context-engineering-101-the-simple-strategy-to-100x-ai-coding]
created: 2026-07-21
updated: 2026-07-21
---

# Aider

[Aider](./aider.md) is one of the earliest AI coding drivers in Cole's story, and he keeps it in the frame for two reasons. First, provenance: it was a main driver when the [PRP framework](../../concepts/prp-framework.md) was being developed. "It started out using like aer and klein as the main drivers," he notes, placing Aider alongside [Cline](./cline.md) at the roots of his [context engineering](../../concepts/context-engineering.md) and [PRD-first](../../concepts/prd-first-development.md) methodology (Rasmus used it while first building PRP).

Second, and more technically interesting, is how Aider feeds the codebase to the model. "Ader is another coding agent that's done something very interesting. What they've done is they've implemented a tree sitter... they're giving an index of the codebase up front to the coding agent as a part of its system prompt essentially." That approach, a precomputed structural map injected into context, contrasts with the on-demand [agentic search](../../concepts/agentic-search.md) that [Claude Code](./claude-code.md) later popularized, and Cole uses the comparison to illustrate that there is more than one way to give an agent codebase awareness.

As a terminal-first, open-source tool, Aider fits the same [human-in-the-loop](../../concepts/human-in-the-loop.md), [validation](../../concepts/validation.md)-driven [vibe-coding](../../concepts/vibe-coding.md) loops Cole teaches with newer agents, just from an earlier generation of the tooling.

## Related

- [PRP Framework](../../concepts/prp-framework.md)
- [PRD-First Development](../../concepts/prd-first-development.md)
- [Context Engineering](../../concepts/context-engineering.md)
- [Agentic Search](../../concepts/agentic-search.md)
- [Human in the Loop](../../concepts/human-in-the-loop.md)
- [Validation](../../concepts/validation.md)
- [Vibe Coding](../../concepts/vibe-coding.md)
- [Cline](./cline.md)
- [Claude Code](./claude-code.md)
- [Cursor](./cursor.md)
- [Windsurf](./windsurf.md)

## Sources

- [Why the Best AI Coding Tools Abandoned RAG (And What They Use Instead)](../../sources/why-the-best-ai-coding-tools-abandoned-rag-and-what-they-use-instead.md) - "[0:09:42] Ader is another coding agent that's done something very interesting. What they've done is they've implemented a tree sitter... they're giving an index of the codebase up front to the coding agent as a part of its system prompt essentially."
- [Context Engineering 101 - The Simple Strategy to 100x AI Coding](../../sources/context-engineering-101-the-simple-strategy-to-100x-ai-coding.md) - "[0:12:41] it started out using like aer and klein as the main drivers"
