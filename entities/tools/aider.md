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

[Aider](./aider.md) is one of the earliest AI coding drivers in Cole's story, and he keeps it in the frame for two reasons. First, provenance: it was a main driver when the [PRP framework](../../concepts/prp-framework.md) was being developed. "It started out using like Aider and Cline as the main drivers," he notes, placing Aider alongside [Cline](./cline.md) at the roots of his [context engineering](../../concepts/context-engineering.md) and [PRD-first](../../concepts/prd-first-development.md) methodology (Rasmus used it while first building PRP).

Second, and more technically interesting, is how Aider feeds the codebase to the model. "Aider is another coding agent that's done something very interesting. What they've done is they've implemented a tree sitter... they're giving an index of the codebase up front to the coding agent as a part of its system prompt essentially." That approach, a precomputed structural map injected into context, contrasts with the on-demand [agentic search](../../concepts/agentic-search.md) that [Claude Code](./claude-code.md) later popularized, and Cole uses the comparison to illustrate that there is more than one way to give an agent codebase awareness.

As a terminal-first, open-source tool, Aider fits the same [human-in-the-loop](../../concepts/human-in-the-loop.md), [validation](../../concepts/validation.md)-driven [vibe-coding](../../concepts/vibe-coding.md) loops Cole teaches with newer agents, just from an earlier generation of the tooling.

## Contrasts with

- [Claude Code](./claude-code.md) - popularized on-demand agentic search, contrasting Aider's precomputed tree-sitter index injected into the system prompt.
- [Cursor](./cursor.md) - AI coding assistant from a later generation of the tooling.
- [Windsurf](./windsurf.md) - AI coding IDE from a later generation of the tooling.

## Works with

- [Cline](./cline.md) - the other early AI coding driver alongside Aider at the roots of the PRP framework.

## Related

- [PRP Framework](../../concepts/prp-framework.md) - a structured, context-rich prompt blueprint that hands an agent everything it needs to one-pass a feature.
- [PRD-First Development](../../concepts/prd-first-development.md) - starting every build from a written product requirements document the agent implements against.
- [Context Engineering](../../concepts/context-engineering.md) - deliberately curating exactly what goes into an LLM's limited context window.
- [Agentic Search](../../concepts/agentic-search.md) - answering a question by reasoning across search tools instead of a single retrieval call.
- [Vibe Coding](../../concepts/vibe-coding.md) - conversationally prompting an AI without closely reading the code.
- [Validation](../../concepts/validation.md) - building explicit checks so the AI verifies its own output against real success criteria.
- [Human in the Loop](../../concepts/human-in-the-loop.md) - keeping a human as the approver and steerer of agentic work.

## Sources

- [Why the Best AI Coding Tools Abandoned RAG (And What They Use Instead)](../../sources/why-the-best-ai-coding-tools-abandoned-rag-and-what-they-use-instead.md) - "[0:09:42] Aider is another coding agent that's done something very interesting. What they've done is they've implemented a tree sitter... they're giving an index of the codebase up front to the coding agent as a part of its system prompt essentially."
- [Context Engineering 101 - The Simple Strategy to 100x AI Coding](../../sources/context-engineering-101-the-simple-strategy-to-100x-ai-coding.md) - "[0:12:41] it started out using like Aider and Cline as the main drivers"
