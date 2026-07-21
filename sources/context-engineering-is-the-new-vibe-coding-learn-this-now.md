---
type: source
title: "Context Engineering is the New Vibe Coding (Learn this Now)"
description: "Vibe coding fails in production because AI coding assistants lack context. Context engineering, architecting all the rules, docs, examples, and plans an LLM needs, is the durable skill that replaces it, demonstrated by a Claude Code template that plans and implements a full project via PRPs and slash commands."
youtube_id: Egeuql3Lrzg
url: https://www.youtube.com/watch?v=Egeuql3Lrzg
slug: context-engineering-is-the-new-vibe-coding-learn-this-now
published: 2025-07-02
duration: "0:22:57"
recency_rank: 82
raw: "../raw/context-engineering-is-the-new-vibe-coding-learn-this-now.md"
tags: [context-engineering, vibe-coding, planning, prd]
created: 2026-07-21
updated: 2026-07-21
---

# Context Engineering is the New Vibe Coding (Learn this Now)

Cole argues that the honeymoon phase of vibe coding (relying 100% on an AI assistant with no validation) is over. Vibe coding is fine for weekend hacks and prototypes but collapses when you try to productionize and scale, because AI coding assistants most often fail when they simply do not have the context they need. He frames the successor paradigm as context engineering: treating context (instructions, rules, documentation, examples, plans, and tools) as an engineered resource that deserves careful architecture, a level up from prompt engineering, which only tweaks the wording of a single prompt. He grounds this in Karpathy's and Toby Lütke's tweets and LangChain's "The Rise of Context Engineering" article, noting the components: prompt engineering, structured output, state/history/memory, examples, and RAG.

The second half is a hands-on Claude Code walkthrough of Cole's "context engineering intro" template repo. The workflow layers markdown context files: CLAUDE.md holds global rules (best practices, testing conventions, task management, style guides); initial.md describes the feature to build with sections for the feature description, examples, documentation/RAG sources, and other gotchas. Two Claude Code slash commands then drive the build. generate-prp reads initial.md, does research on APIs and the codebase, and produces a PRP (Product Requirements Prompt) from a base template; execute-prp then implements the whole project end to end with a comprehensive to-do list, tests, and iteration.

Cole demos building a Pydantic AI research agent this way: Claude Code researches Pydantic AI, plans the desired file structure ahead of time, and after roughly 30 minutes ships a tested agent (GPT-4.1-mini model, Brave + OpenAI web search). He needed only one round of iteration (the tool and dependency setup was not idiomatic Pydantic AI). His closing lesson: do not vibe code, validate the output, but with context engineering set up beforehand you are set. He credits Rasmus from the Dynamous community for the PRP base template and much of the approach, and previews deeper future coverage of RAG and memory.

## Concepts covered

- [Context Engineering](../concepts/context-engineering.md)
- [Vibe Coding](../concepts/vibe-coding.md)
- [PRD-First Development](../concepts/prd-first-development.md)
- [Planning with AI](../concepts/planning-with-ai.md)
- [Slash Commands](../concepts/slash-commands.md)
- [Global Rules](../concepts/global-rules.md)
- [Validation](../concepts/validation.md)
- [Retrieval-Augmented Generation (RAG)](../concepts/rag.md)
- [Prompt Engineering](../concepts/prompt-engineering.md)

## Entities

- [Cole Medin](../entities/people/cole-medin.md)
- [Claude Code](../entities/tools/claude-code.md)
- [Pydantic AI](../entities/tools/pydantic-ai.md)
- [Andrej Karpathy](../entities/people/andrej-karpathy.md)
- [Dynamous](../entities/organizations/dynamous.md)
- [Rasmus](../entities/people/rasmus.md)
- [LangChain](../entities/tools/langchain.md)
- [Shopify](../entities/organizations/shopify.md)
- [Snyk](../entities/organizations/snyk.md)
- [GitHub](../entities/tools/github.md)

## Key moments

- **[0:00:00]** Thesis: vibe coding's honeymoon is over; context engineering is the new paradigm
- **[0:00:52]** Cites Qodo "State of AI Code Quality", 76.4% of developers low-confidence shipping AI code without review
- **[0:01:11]** "Intuition does not scale. Structure does", the core problem is missing context
- **[0:02:21]** Karpathy endorses Toby Lütke's context-engineering framing; definition of context engineering
- **[0:03:00]** Context engineering vs prompt engineering: whole ecosystem of context, not just wording
- **[0:03:50]** GitHub diagram of context-engineering components: prompt eng, structured output, memory, examples, RAG
- **[0:04:38]** Abraham Lincoln axe-sharpening analogy for upfront context investment
- **[0:05:20]** LangChain "Rise of Context Engineering", "most important skill an AI engineer can develop"
- **[0:06:20]** Into Claude Code with the context-engineering template repo
- **[0:09:44]** Walkthrough of context files: CLAUDE.md global rules, initial.md feature spec
- **[0:12:58]** PRPs (Product Requirements Prompts) and Claude Code slash commands introduced
- **[0:14:41]** Runs /generate-prp with initial.md as $ARGUMENTS
- **[0:16:31]** PRP generated in PRPs folder after research + codebase/docs analysis
- **[0:18:47]** Runs /execute-prp to implement the project end to end
- **[0:19:36]** After roughly 30 min, Claude Code has built and tested the Pydantic AI agent; one round of iteration needed
- **[0:20:22]** Lesson: don't vibe code, validate output, but with context engineering set up you're set

## Transcript

[Raw transcript](../raw/context-engineering-is-the-new-vibe-coding-learn-this-now.md)
