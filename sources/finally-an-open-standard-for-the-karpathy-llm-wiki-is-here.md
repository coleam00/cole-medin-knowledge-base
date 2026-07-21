---
type: source
title: "Finally, an Open Standard for the Karpathy LLM Wiki is HERE"
description: "Google's Open Knowledge Format (OKF) is a minimal open standard on top of Karpathy's LLM wiki that lets everyone build and share LLM knowledge bases in the same producible/consumable structure."
youtube_id: T33iI6izAKw
url: https://www.youtube.com/watch?v=T33iI6izAKw
slug: finally-an-open-standard-for-the-karpathy-llm-wiki-is-here
published: 2026-07-01
duration: "0:19:39"
recency_rank: 6
raw: "../raw/finally-an-open-standard-for-the-karpathy-llm-wiki-is-here.md"
tags: [okf, llm-wiki, knowledge-bases]
created: 2026-07-21
updated: 2026-07-21
---

Cole reviews Google's Open Knowledge Format (OKF), a lightweight standard layered on top of Andrej Karpathy's viral LLM wiki pattern. The LLM wiki lets you build a personal second brain not by dumping documents for RAG, but by having an LLM incrementally read each new source, extract key information, and integrate it into a persistent, interlinked collection of markdown entity/concept pages with an index at the top. The core problem Cole identifies: because there's no standard, every person's wiki is structured differently (different folders, different metadata fields like "tags" vs "categories"), so wikis can't be reliably shared or searched by someone else's agent.

OKF standardizes exactly two things: how information is organized (top-level index plus per-folder indexes, bundles as the unit of sharing) and the YAML front-matter metadata fields on each document. Only one field is required, "type," which provides the categorization that lets an agent filter and traverse the wiki like a knowledge graph; the rest (title, tags, related-videos links) are optional but recommended. You adopt it the same way as Karpathy's gist: copy the spec.md into a coding agent and tell it to build a new wiki or refactor an existing one (using sub-agents to scale the refactor). OKF is explicitly a standard for both consuming (searching) and producing (evolving) knowledge bases.

To demonstrate, Cole ships an OKF "bundle" packaging his best AI-coding YouTube videos plus extracted concept pages (like the PIV loop), which viewers can clone into Obsidian/Notion and query directly instead of re-feeding transcripts. He shows an agent answering "what's Cole's biggest idea for reliable AI code?" by progressively disclosing: reading the top index, drilling into concepts, then reading the context-engineering page. He addresses the main critique, that OKF is too simple and adds little over Karpathy's wiki, arguing that being minimally opinionated is the whole point: it's the bare-minimum shared layer that makes wikis interoperable, analogous to what MCP did for agent-to-tool communication.

## Concepts covered

- [The LLM Wiki](../concepts/the-llm-wiki.md)
- [Knowledge Bases](../concepts/knowledge-bases.md)
- [Progressive Disclosure](../concepts/progressive-disclosure.md)
- [Knowledge Graphs](../concepts/knowledge-graphs.md)
- [Second Brain](../concepts/second-brain.md)
- [The PIV Loop](../concepts/the-piv-loop.md)
- [Context Engineering](../concepts/context-engineering.md)

## Entities

- [Andrej Karpathy](../entities/people/andrej-karpathy.md)
- [Google](../entities/organizations/google.md)
- [MCP (Model Context Protocol)](../entities/tools/mcp.md)
- [Obsidian](../entities/tools/obsidian.md)
- [Archon](../entities/tools/archon.md)
- [GitHub](../entities/tools/github.md)
- [Cole Medin](../entities/people/cole-medin.md)

## Key moments

- **[0:00:00]** Intro: Karpathy's LLM wiki gist hit 40k stars; one-shot buildable, incrementally maintained knowledge base
- **[0:01:23]** The core problem: no standard means everyone's wiki is structured differently and can't be shared
- **[0:02:06]** Google releases Open Knowledge Format (OKF) as the shared standard
- **[0:03:10]** OKF standardizes two things: information organization and metadata fields
- **[0:04:01]** Walkthrough of a traditional Karpathy wiki: index file, metadata, progressive disclosure, related links / graph view
- **[0:06:44]** Adopting OKF: copy spec.md into a coding agent to build or refactor a wiki
- **[0:07:59]** PostHog sponsor segment (product analytics for Archon)
- **[0:09:36]** OKF is to agent-to-knowledge-base what MCP is to agent-to-tool; standard for both consuming and producing
- **[0:11:10]** Cole ships an OKF bundle of his best AI-coding videos as a shareable gift
- **[0:12:53]** His setup: top-level index doc + per-bundle indexes + a CLI to list/read bundles by concept ID
- **[0:14:48]** Inside a bundle: the PIV loop concept page, required "type" field, optional title/tags/related
- **[0:16:17]** Live demo: agent answers a question via progressive disclosure, landing on context-engineering
- **[0:17:41]** Addresses the "OKF is too simple" critique; minimally opinionated is the point

## Transcript

[Raw transcript](../raw/finally-an-open-standard-for-the-karpathy-llm-wiki-is-here.md)
