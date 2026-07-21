---
type: concept
title: "Open Knowledge Format (OKF)"
description: "A minimal open standard layered on the Karpathy LLM wiki that fixes how a knowledge base is organized and what metadata its pages carry, so any agent can navigate one it has never seen."
tags: [standards, knowledge-bases, llm-wiki, okf]
videos: [finally-an-open-standard-for-the-karpathy-llm-wiki-is-here, this-completely-changes-the-way-we-build-production-ai-agents-vercel-eve]
created: 2026-07-21
updated: 2026-07-21
---

# Open Knowledge Format (OKF)

The Open Knowledge Format is Google's open standard for structuring an LLM knowledge base: plain markdown pages with YAML frontmatter, organized into index, entity, and concept documents. It exists because the [LLM wiki](./the-llm-wiki.md) pattern worked but did not travel. Everyone built one their own way, so nobody could hand theirs to someone else's agent. "We need a standard so that everyone's building wikis in the same way so that we can share them freely. And so that is what Google has released here with their open knowledge format" [0:02:06].

It standardizes exactly two things and deliberately nothing else: "There are two things that they're standardizing here. The first is how we are organizing information like our entity documents and our concepts. And then the second standardization is the exact fields that we're going to have in our metadata" [0:03:10]. Layout plus metadata. No storage engine, no embedding scheme, no retrieval API. A bundle is a directory of files a human can read and git can diff.

The minimalism is the design goal rather than a gap: "It's the bare minimum layer that we need on top so that we can produce and consume these wikis in exactly the same way across everyone's agents that lean into OKF" [0:18:37]. Two properties fall out of that. Production and consumption become symmetric, so the agent that writes a bundle and the agent that reads one need no private agreement. And because navigation is index plus relative links, the compiled bundle IS the search index, which is what makes it a [progressive disclosure](./progressive-disclosure.md) surface instead of another retrieval stack to operate.

## Why it matters for agents

A standard format turns knowledge into a portable dependency: a team can publish a bundle the way it publishes a library, and any conforming agent can mount it without a migration. That reframes the knowledge layer of production agents: "OKF is the standard for how we structure the knowledge bases that we attach the agents to. So, I think there's also a really cool combination that we can do here with Eve plus OKF" [0:06:13]. Pair a format for what the agent knows with a runtime for what the agent does, and the knowledge stops being locked inside one product. Conformance is also mechanically checkable, so linting frontmatter, links, and index coverage is a real [validation](./validation.md) gate.

## Builds on

- [The LLM Wiki](./the-llm-wiki.md) - the Karpathy pattern OKF formalizes.
- [Knowledge Bases](./knowledge-bases.md) - the broader problem OKF gives a wire format to.
- [Progressive Disclosure](./progressive-disclosure.md) - index-then-follow-links navigation is how a bundle is read.

## Contrasts with

- [Traditional RAG](./traditional-rag.md), [When RAG Is Dead](./when-rag-is-dead.md) - no embeddings and no vector store; the links are the retrieval mechanism.
- [Knowledge Graphs](./knowledge-graphs.md) - a heavier structured representation of the same external knowledge.

## Implemented by

- [Google](../entities/organizations/google.md) - published the standard.
- [Eve (Vercel)](../entities/tools/eve.md) - the production agent runtime Cole pairs OKF with as the knowledge layer.
- [Claude Code](../entities/tools/claude-code.md) - the harness used to produce and consume bundles in practice.

## Related

- [Andrej Karpathy](../entities/people/andrej-karpathy.md) - originated the LLM wiki idea the standard sits on top of.
- [Memory Systems](./memory-systems.md), [Self-Evolving Memory](./self-evolving-memory.md), [Second Brain](./second-brain.md) - what a conforming bundle is usually built to serve.
- [Docs as Agent Context](./docs-as-agent-context.md), [llms.txt](./llms-txt.md) - neighboring attempts to make written knowledge agent-legible.
- [Tool Standardization](./tool-standardization.md) - the same interoperability argument MCP made for tools, applied to knowledge.
- [Context Engineering](./context-engineering.md), [Validation](./validation.md) - feeding an agent exactly the right pages, and keeping the bundle honest.
- [File-System-Based Agents](./file-system-based-agents.md) - An architecture where an entire AI agent is defined as a single folder of organized markdown and TypeScript primitives rather than hand-wired framework code.

## Sources

- [Finally, an Open Standard for the Karpathy LLM Wiki is HERE](../sources/finally-an-open-standard-for-the-karpathy-llm-wiki-is-here.md) - "[0:02:06] We need a standard so that everyone's building wikis in the same way so that we can share them freely. And so that is what Google has released here with their open knowledge format."
- [Finally, an Open Standard for the Karpathy LLM Wiki is HERE](../sources/finally-an-open-standard-for-the-karpathy-llm-wiki-is-here.md) - "[0:03:10] There are two things that they're standardizing here. The first is how we are organizing information like our entity documents and our concepts. And then the second standardization is the exact fields that we're going to have in our metadata."
- [Finally, an Open Standard for the Karpathy LLM Wiki is HERE](../sources/finally-an-open-standard-for-the-karpathy-llm-wiki-is-here.md) - "[0:18:37] It's the bare minimum layer that we need on top so that we can produce and consume these wikis in exactly the same way across everyone's agents that lean into OKF."
- [This Completely Changes the Way We Build Production AI Agents (Vercel Eve)](../sources/this-completely-changes-the-way-we-build-production-ai-agents-vercel-eve.md) - "[0:06:13] OKF is the standard for how we structure the knowledge bases that we attach the agents to. So, I think there's also a really cool combination that we can do here with Eve plus OKF."
