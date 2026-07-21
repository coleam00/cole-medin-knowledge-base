---
type: entity
subtype: tool
title: "Cline"
description: "An early AI coding driver alongside Aider; PRP was inspired by the Cline community's memory-prompting framework."
resource: "https://github.com/cline/cline"
tags: [coding-agent, open-source, ai-ide]
videos: [this-completely-changes-the-way-we-build-production-ai-agents-vercel-eve, why-the-best-ai-coding-tools-abandoned-rag-and-what-they-use-instead, is-gemini-3-really-the-best-ai-ever, github-is-the-future-of-ai-coding-heres-why, context-engineering-101-the-simple-strategy-to-100x-ai-coding, introducing-archon-an-ai-agent-that-builds-ai-agents, stop-paying-for-gpt-claude-other-llms-get-them-all-in-one-place]
created: 2026-07-21
updated: 2026-07-21
---

# Cline

[Cline](./cline.md) (styled "Klein" in Cole's auto-transcripts) is one of the original open-source AI coding drivers, and its fingerprints are on Cole's methodology. His [PRP framework](../../concepts/prp-framework.md) grew out of it: the approach is "very inspired by the devdan and the client community and the memory prompting framework that a lot of people use over there," where "it started out using like aer and klein as the main drivers." So Cline sits upstream of much of his [context engineering](../../concepts/context-engineering.md) thinking, alongside [Aider](./aider.md).

Cline's creators also shaped the field's move away from retrieval. "Nick Pash is one of the original creators of Klein" who "put out this article, why I no longer recommend rag for autonomous coding agents," a pivot Cole cites repeatedly when explaining why frontier agents favor [agentic search](../../concepts/agentic-search.md) over [RAG](../../concepts/rag.md). More recently Cline pushed into evaluation: "that is what Klein is going to be leveraging with Kleinbench... they're on the frontier now of LLM evals, especially as it relates to [agentic coding](../../concepts/agentic-coding.md)," with a privacy-first, opt-in data model.

For everyday use Cole positions Cline as a solid [human-in-the-loop](../../concepts/human-in-the-loop.md) assistant, "fantastic at generating functions scripts or components within your existing code base," configurable via [global rules](../../concepts/global-rules.md) and a first-class Archon integration ("super easy to get up and running with wind surf cursor and Klein"). It also ships GitHub-action documentation, making it viable for the same automated flows he builds with the bigger tools, whatever the chosen [model](../../concepts/model-selection.md).

## Related

- [PRP Framework](../../concepts/prp-framework.md)
- [Context Engineering](../../concepts/context-engineering.md)
- [Agentic Search](../../concepts/agentic-search.md)
- [Retrieval-Augmented Generation (RAG)](../../concepts/rag.md)
- [Agentic Coding](../../concepts/agentic-coding.md)
- [Global Rules](../../concepts/global-rules.md)
- [Human in the Loop](../../concepts/human-in-the-loop.md)
- [Model Selection](../../concepts/model-selection.md)
- [Aider](./aider.md)
- [Cursor](./cursor.md)
- [Windsurf](./windsurf.md)
- [Claude Code](./claude-code.md)
- [Archon](./archon.md)

## Sources

- [This Completely Changes the Way We Build Production AI Agents (Vercel Eve)](../../sources/this-completely-changes-the-way-we-build-production-ai-agents-vercel-eve.md)
- [Why the Best AI Coding Tools Abandoned RAG (And What They Use Instead)](../../sources/why-the-best-ai-coding-tools-abandoned-rag-and-what-they-use-instead.md) - "[0:08:40] Nick Pash is one of the original creators of Klein put out this article, why I no longer recommend rag for autonomous coding agents."
- [Is Gemini 3 Really the Best AI Ever?](../../sources/is-gemini-3-really-the-best-ai-ever.md) - "[0:08:13] that is what Klein is going to be leveraging with Kleinbench... I really do think that they're on the frontier now of LLM evals, especially as it relates to agentic coding."
- [GitHub is the Future of AI Coding (Here's Why)](../../sources/github-is-the-future-of-ai-coding-heres-why.md)
- [Context Engineering 101 - The Simple Strategy to 100x AI Coding](../../sources/context-engineering-101-the-simple-strategy-to-100x-ai-coding.md) - "[0:12:41] it's very inspired by in the devdan and the client community and the memory prompting uh framework uh that that a lot of people use over there"
- [Introducing Archon - an AI Agent that BUILDS AI Agents](../../sources/introducing-archon-an-ai-agent-that-builds-ai-agents.md) - "[0:02:56] so I make it super easy to get up and running with wind surf cursor and Klein for archon"
- [STOP Paying for GPT, Claude, & Other LLMs - Get them ALL in One Place](../../sources/stop-paying-for-gpt-claude-other-llms-get-them-all-in-one-place.md)
