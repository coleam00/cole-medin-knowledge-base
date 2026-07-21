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

[Cline](./cline.md) (styled "Klein" in Cole's auto-transcripts) is one of the original open-source AI coding drivers, and its fingerprints are on Cole's methodology. His [PRP framework](../../concepts/prp-framework.md) grew out of it: the approach is "very inspired by the devdan and the client community and the memory prompting framework that a lot of people use over there," where "it started out using like Aider and Cline as the main drivers." So Cline sits upstream of much of his [context engineering](../../concepts/context-engineering.md) thinking, alongside [Aider](./aider.md).

Cline's creators also shaped the field's move away from retrieval. "Nick Pash is one of the original creators of Cline" who "put out this article, why I no longer recommend rag for autonomous coding agents," a pivot Cole cites repeatedly when explaining why frontier agents favor [agentic search](../../concepts/agentic-search.md) over [RAG](../../concepts/rag.md). More recently Cline pushed into evaluation: "that is what Cline is going to be leveraging with Clinebench... they're on the frontier now of LLM evals, especially as it relates to [agentic coding](../../concepts/agentic-coding.md)," with a privacy-first, opt-in data model.

For everyday use Cole positions Cline as a solid [human-in-the-loop](../../concepts/human-in-the-loop.md) assistant, "fantastic at generating functions scripts or components within your existing code base," configurable via [global rules](../../concepts/global-rules.md) and a first-class Archon integration ("super easy to get up and running with Windsurf cursor and Cline"). It also ships GitHub-action documentation, making it viable for the same automated flows he builds with the bigger tools, whatever the chosen [model](../../concepts/model-selection.md).

## Realizes

- [PRP Framework](../../concepts/prp-framework.md) - The Product Requirements Prompt pattern: a structured, context-rich prompt blueprint that hands an agent everything it needs to one-pass a feature.
- [Context Engineering](../../concepts/context-engineering.md) - The deliberate practice of curating exactly what goes into an LLM's limited context window - system messages, schemas, chat history, and dynamic variables - to avoid overload and keep outputs sharp.
- [Agentic Coding](../../concepts/agentic-coding.md) - Letting an AI agent drive software development end-to-end, from planning through implementation and validation, with human steering.
- [Agentic Search](../../concepts/agentic-search.md) - An agent answering a question by reasoning across multiple search tools and full-document fallbacks instead of relying on a single retrieval call.
- [Global Rules](../../concepts/global-rules.md) - Persistent project- or user-level rule files that inject standing context and conventions into every agent run.
- [Human in the Loop](../../concepts/human-in-the-loop.md) - Keeping a human as the approver and steerer of agentic work rather than fully automating, so AI augments engineers instead of replacing them.
- [Model Selection](../../concepts/model-selection.md) - Choosing the right LLM per task by trading off quality, speed, and cost, often routing easy requests to cheap models and hard ones to expensive models.
- [Vibe Coding](../../concepts/vibe-coding.md) - Building software by conversationally prompting an AI without closely reading the code, useful for prototypes but risky for production.

## Contrasts with

- [Cursor](./cursor.md) - AI coding assistant that can consume AG-UI's llms.txt docs to help build with the protocol.
- [Windsurf](./windsurf.md) - AI coding IDE Cole used to build the Python AG-UI backend and consume the protocol docs.
- [Claude Code](./claude-code.md) - Anthropic's terminal-based agentic coding assistant that is the subject of this complete-guide walkthrough.

## Works with

- [Aider](./aider.md) - An early AI coding driver Rasmus used when first developing the PRP framework.
- [Archon](./archon.md) - Cole's free, open-source AI command center and harness builder for AI coding; started as an AI agent that builds other AI agents.

## Related

- [Retrieval-Augmented Generation (RAG)](../../concepts/rag.md) - Grounding an LLM's answers by retrieving relevant documents from an external knowledge base and injecting them into the prompt at query time.

## Sources

- [This Completely Changes the Way We Build Production AI Agents (Vercel Eve)](../../sources/this-completely-changes-the-way-we-build-production-ai-agents-vercel-eve.md)
- [Why the Best AI Coding Tools Abandoned RAG (And What They Use Instead)](../../sources/why-the-best-ai-coding-tools-abandoned-rag-and-what-they-use-instead.md) - "[0:08:40] Nick Pash is one of the original creators of Cline put out this article, why I no longer recommend rag for autonomous coding agents."
- [Is Gemini 3 Really the Best AI Ever?](../../sources/is-gemini-3-really-the-best-ai-ever.md) - "[0:08:13] that is what Cline is going to be leveraging with Clinebench... I really do think that they're on the frontier now of LLM evals, especially as it relates to agentic coding."
- [GitHub is the Future of AI Coding (Here's Why)](../../sources/github-is-the-future-of-ai-coding-heres-why.md)
- [Context Engineering 101 - The Simple Strategy to 100x AI Coding](../../sources/context-engineering-101-the-simple-strategy-to-100x-ai-coding.md) - "[0:12:41] it's very inspired by in the devdan and the client community and the memory prompting uh framework uh that that a lot of people use over there"
- [Introducing Archon - an AI Agent that BUILDS AI Agents](../../sources/introducing-archon-an-ai-agent-that-builds-ai-agents.md) - "[0:02:56] so I make it super easy to get up and running with Windsurf cursor and Cline for archon"
- [STOP Paying for GPT, Claude, & Other LLMs - Get them ALL in One Place](../../sources/stop-paying-for-gpt-claude-other-llms-get-them-all-in-one-place.md)
