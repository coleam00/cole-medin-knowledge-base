---
type: source
title: "This Bolt.new Fork is EXPLODING - Don't Miss out on What's Happening!"
description: "Cole's open-source fork of bolt.new is rapidly becoming a community-driven project whose core mission is to let any LLM (especially local ones) power an in-browser AI coding assistant, with backend agentic workflows as the most exciting next frontier."
youtube_id: jm007pw2v1A
url: https://www.youtube.com/watch?v=jm007pw2v1A
slug: this-boltnew-fork-is-exploding-dont-miss-out-on-whats-happening
published: 2024-10-27
duration: "0:16:47"
recency_rank: 148
raw: "../raw/this-boltnew-fork-is-exploding-dont-miss-out-on-whats-happening.md"
tags: [open-source, community, provider-independence, roadmap, agentic-workflows]
created: 2026-07-21
updated: 2026-07-21
---

Two weeks after releasing a fork of [bolt.new](../entities/tools/bolt-new.md) whose original purpose was to break the official version's single-model limitation and support any LLM (especially local ones via [Ollama](../entities/tools/ollama.md)), [Cole Medin](../entities/people/cole-medin.md) reports the project has exploded into a genuine open-source community with 20 pull requests in a single week. He announces four updates: a long-term maintenance commitment, an upcoming Discourse community, applications to become a core contributor or maintainer, and regular (possibly weekly) content plus a setup tutorial built around [Docker](../entities/tools/docker.md).

He then walks the README changelog of recently merged contributions: chain-of-thought and structured-planning prompt improvements, [DeepSeek](../entities/organizations/deepseek.md) and Mistral API integrations, and a generic OpenAI-compatible API integration (swap the base URL so any OpenAI-compatible provider like [Groq](../entities/organizations/groq.md), Fireworks, or Together works through one env var). Additional merged features include one-way file sync to a local folder, Docker containerization, and publishing generated projects directly to [GitHub](../entities/tools/github.md), all credited to specific contributors.

Finally he lays out the roadmap and high-priority items: better prompting so smaller and local models reliably open the web container, native image attachments, and the standout ambition of running true agentic workflows in the backend (multi-model interaction, self-reflection, self-improvement, echoing patterns from [LangChain](../entities/tools/langchain.md)) rather than a single model call, plus integrations (LM Studio, Azure OpenAI, Hugging Face, perplexity), deploy to [Vercel](../entities/organizations/vercel.md) or Netlify, code reverting, prompt caching, in-UI API keys via [OpenRouter](../entities/tools/openrouter.md) and others, and having the LLM write its plan to a markdown file in the project.

## Concepts covered

- [Provider Independence](../concepts/provider-independence.md)
- [Local & Self-Hosted AI](../concepts/local-ai.md)
- [Community-Driven Development](../concepts/community-driven-development.md)
- [Chain-of-Thought Prompting](../concepts/chain-of-thought.md)
- [Agentic Workflow Engineering](../concepts/agentic-workflow-engineering.md)
- [Planning with AI](../concepts/planning-with-ai.md)

## Entities

- [bolt.new](../entities/tools/bolt-new.md)
- [Ollama](../entities/tools/ollama.md)
- [DeepSeek](../entities/organizations/deepseek.md)
- [Groq](../entities/organizations/groq.md)
- [OpenRouter](../entities/tools/openrouter.md)
- [Docker](../entities/tools/docker.md)
- [GitHub](../entities/tools/github.md)
- [Vercel](../entities/organizations/vercel.md)
- [LangChain](../entities/tools/langchain.md)
- [Cole Medin](../entities/people/cole-medin.md)

## Key moments

- **[0:00:00]** Origin of the fork: make bolt.new work with any LLM, especially local ones, vs the official single-model limitation
- **[0:01:04]** 20 pull requests in one week; Cole commits to long-term maintenance of the fork
- **[0:01:35]** Announces upcoming Discourse community and a larger channel-wide community
- **[0:02:06]** Opening applications to become a core contributor / maintainer with repo access
- **[0:04:35]** Walks the README changelog of recently merged features
- **[0:05:53]** Explains the generic OpenAI-compatible API integration via base-URL swap
- **[0:06:59]** One-way file sync to a local folder and project-as-zip download
- **[0:07:43]** Docker containerization added; will anchor the setup tutorial
- **[0:08:10]** Publish generated projects directly to GitHub
- **[0:13:23]** High-priority roadmap: running agents in the backend instead of a single model call

## Transcript

[Raw transcript](../raw/this-boltnew-fork-is-exploding-dont-miss-out-on-whats-happening.md)
