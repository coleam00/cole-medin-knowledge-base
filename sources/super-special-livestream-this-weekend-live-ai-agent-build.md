---
type: source
title: "Super Special Livestream this Weekend! (LIVE AI Agent Build)"
description: "Cole announces his first live AI agent build stream where he'll construct a full-stack personal AI coach powered by advanced agentic RAG over his YouTube content."
youtube_id: pjF-0dliYhg
url: https://www.youtube.com/watch?v=pjF-0dliYhg
slug: super-special-livestream-this-weekend-live-ai-agent-build
published: 2025-10-24
duration: "0:07:13"
recency_rank: 59
raw: "../raw/super-special-livestream-this-weekend-live-ai-agent-build.md"
tags: [livestream, agentic-rag, announcement]
created: 2026-07-21
updated: 2026-07-21
---

# Super Special Livestream this Weekend! (LIVE AI Agent Build)

This is a short announcement video for Cole's first-ever live AI agent build livestream (Sunday, October 26th). Rather than the Q&A format of past streams, this one is a hands-on build of a complete, practical AI agent: a personal AI coach trained on all of Cole's YouTube content, intended as a resource alongside the channel and later extended to other sources.

Cole previews the four core technologies the build will focus on. YouTube is the primary data source for a RAG pipeline that extracts metadata and timestamps, generalizable to any channel. Pydantic AI is the agent framework, built in Python and made LLM-agnostic so it works with OpenRouter, Ollama, Anthropic, and OpenAI. The agent gets RAG tools that apply advanced retrieval strategies plus the ability to pull full transcripts, making it an agentic RAG solution where the agent reasons about how it searches. Supabase serves as the database for transcripts, embeddings, and metadata (enabling metadata filtering) plus authentication for a cloud-deployed full-stack front end with token streaming. Docling handles hybrid chunking locally for accurate RAG over transcripts, with room to later ingest PDFs.

The build uses a full AI coding assistant workflow (Claude Code, plus Archon for task management and RAG). Cole ties the stream to the release of the Dynamous Agentic Coding course, whose core mental model he shares: every mistake AI makes is an opportunity to evolve your system rather than just fix the code yourself, and iterating on that repeatedly yields a system perfectly crafted for you.

## Concepts covered

- [Agentic RAG](../concepts/agentic-rag.md)
- [Retrieval-Augmented Generation (RAG)](../concepts/rag.md)
- [Provider Independence](../concepts/provider-independence.md)
- [Context-Aware Chunking](../concepts/context-aware-chunking.md)
- [Chunking](../concepts/chunking.md)
- [System Evolution](../concepts/system-evolution.md)
- [Agentic Coding](../concepts/agentic-coding.md)

## Entities

- [Cole Medin](../entities/people/cole-medin.md)
- [Pydantic AI](../entities/tools/pydantic-ai.md)
- [Docling](../entities/tools/docling.md)
- [Supabase](../entities/tools/supabase.md)
- [Claude Code](../entities/tools/claude-code.md)
- [Archon](../entities/tools/archon.md)
- [Dynamous](../entities/organizations/dynamous.md)
- [Anthropic](../entities/organizations/anthropic.md)
- [OpenAI](../entities/organizations/openai.md)

## Key moments

- **[0:00:00]** Announces first-ever live AI agent build stream, Sunday Oct 26th 11am Central
- **[0:00:30]** Reveals the use case: a personal AI coach trained on all of Cole's YouTube content
- **[0:01:31]** Introduces the four core technologies for the build
- **[0:01:44]** YouTube as the primary RAG data source with metadata + timestamp extraction
- **[0:02:15]** Pydantic AI as the framework, made LLM-agnostic across providers
- **[0:02:45]** Agentic RAG: advanced retrieval + agent can pull transcripts and reason about search
- **[0:03:02]** Full-stack app with token streaming and Supabase for storage + auth
- **[0:03:48]** Docling for hybrid chunking, critical for accurate transcript RAG
- **[0:04:36]** Uses Claude Code + Archon in a full AI coding assistant workflow
- **[0:05:04]** Ties stream to the Dynamous Agentic Coding course release
- **[0:06:24]** Core mental model: every mistake is an opportunity to evolve your system

## Transcript

[Raw transcript](../raw/super-special-livestream-this-weekend-live-ai-agent-build.md)
