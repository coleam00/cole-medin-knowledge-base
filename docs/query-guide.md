---
type: overview
title: "Query Guide"
description: "How a human or agent should ask this knowledge base questions and get grounded, cited answers."
tags: [meta, querying, navigation]
updated: 2026-07-09
---

# Query Guide

This bundle is optimized for an agent answering questions by **navigation**, not embedding search. The
retrieval algorithm is deterministic and cheap:

1. **Read `index.md`** (and this bundle's `SCHEMA.md` once). The root index's *Themes* section and the
   section indexes tell you which pages exist.
2. **Pick the entry page(s)** whose one-line description matches the question - a concept for a
   "what/how/why" question, an entity for a "what is X / how does Cole use X" question, a source page for
   "what did the video about Y say."
3. **Follow typed links.** Each page's `## Prerequisites`, `## Builds on`, `## Contrasts with`,
   `## Related`, and `## Tools` sections take you one hop to the neighboring context a good answer needs.
4. **Cite.** Answer from the page and cite the concept/entity page + the source video(s) under its
   `## Sources`. If nothing covers it, say so - the corpus is 20 videos, not all knowledge.

## Fallback: keyword scan

If the index does not obviously contain the topic, a keyword scan over the markdown is the fallback (the
bundle is small enough that this is fast). With Cole's `okf_consumer.py`:

```bash
uv run python okf_consumer.py find <bundle> "your query"
```

or plain `grep -ri "term" concepts/ entities/ sources/`.

## Example questions this bundle should answer well

**Concept / how-to**
- "What is the PIV loop and what are its steps?"
- "When is RAG actually 'dead,' and when is it still essential?"
- "What's the difference between agentic search and traditional vector RAG?"
- "How does Cole use git worktrees to run Claude Code in parallel?"
- "When should I reach for subagents vs. a single agent?"
- "What is an AI coding harness and why build one?"
- "How does the adversarial / generator-evaluator technique improve reliability?"
- "What's Cole's approach to planning before implementation?"

**Entity / comparison**
- "What is Archon and what problem does it solve?"
- "How is Pi different from Claude Code?"
- "What does Cole think MCP gets wrong, and what's his fix?"
- "What is Karpathy's LLM wiki and how does Cole apply it?"
- "Which tools does Cole use for a second brain?"

**Source / provenance**
- "What did the 2,000-hours video say about building anything with Claude Code?"
- "Summarize the live agent-teams build."

If any realistic question in these families is *not* answerable by navigation, that is a bug in the
index or the linking - fix the structure, not just the page.
