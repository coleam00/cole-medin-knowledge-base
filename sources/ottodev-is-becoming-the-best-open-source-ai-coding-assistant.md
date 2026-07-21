---
type: source
title: "oTToDev is Becoming the BEST Open Source AI Coding Assistant"
description: "oTToDev, a community-driven open-source fork of bolt.new, is rapidly adding features (code streaming, an integrated terminal, provider auto-fetching, local-model support) and a clear roadmap to become the best open-source AI coding assistant."
youtube_id: 5I9VgwauuzU
url: https://www.youtube.com/watch?v=5I9VgwauuzU
slug: ottodev-is-becoming-the-best-open-source-ai-coding-assistant
published: 2024-11-17
duration: "0:14:55"
recency_rank: 141
raw: "../raw/ottodev-is-becoming-the-best-open-source-ai-coding-assistant.md"
tags: [open-source, ai-coding, community, local-ai, roadmap]
created: 2026-07-21
updated: 2026-07-21
---

This is a project-update video for [oTToDev](../entities/tools/ottodev.md), the open-source, browser-based AI coding assistant that [Cole Medin](../entities/people/cole-medin.md) forked from the commercial [bolt.new](../entities/tools/bolt-new.md). Cole walks through recently merged community pull requests and demos the new UI: a standardized provider layer that auto-fetches every available model from providers like [OpenRouter](../entities/tools/openrouter.md) (with pricing and a one-click "get API key" link), out-of-the-box support for [Ollama](../entities/tools/ollama.md) local models (fixing the default 2,000-token context limit), live code streaming so you watch the LLM type each file, and an integrated "bolt terminal" attached to the workbench that surfaces the actual command output the model runs.

He then shares an initial public roadmap built on roadmap.sh and stresses that the project needs a clear vision so it does not die from implementing features willy-nilly. High-priority items include stopping Bolt from rewriting too many files, better prompting for smaller LLMs, loading local projects, attaching images to prompts, running backend agents (a mixture-of-agents or chain-of-thought system), one-click Netlify deploy, per-model prompt templates, and an extension marketplace so features can be toggled on and off without bloating the core UI. He also floats crowdfunding, possibly a Kickstarter, to fund bounties on features.

The final section is a practical troubleshooting guide. The generic "there was an error processing your request" message is unhelpful; instead look at the terminal for backend 500 errors and the browser dev-tools console for frontend 400 and 404 errors. A blank preview is usually not an oTToDev bug but the LLM hallucinating bad code, file structure, or commands, so the fix is to use a larger model. The recurring lesson: smaller and local models mess up often, so use the largest model you can when building real apps.

## Concepts covered

- [Open-Source & Local AI Coding](../concepts/open-source-ai-coding.md)
- [Community-Driven Development](../concepts/community-driven-development.md)
- [Model Selection](../concepts/model-selection.md)
- [Local & Self-Hosted AI](../concepts/local-ai.md)
- [AI Coding Assistant UX Patterns](../concepts/ai-coding-ux.md)
- [Extensible Plugin Architecture](../concepts/extension-marketplace.md)
- [Agent Teams](../concepts/agent-teams.md)
- [Agentic Coding](../concepts/agentic-coding.md)

## Entities

- [oTToDev (autod Dev)](../entities/tools/ottodev.md)
- [bolt.new](../entities/tools/bolt-new.md)
- [Ollama](../entities/tools/ollama.md)
- [OpenRouter](../entities/tools/openrouter.md)
- [GitHub](../entities/tools/github.md)
- [Anthropic](../entities/organizations/anthropic.md)
- [OpenAI](../entities/organizations/openai.md)
- [Cole Medin](../entities/people/cole-medin.md)

## Key moments

- **[0:00:59]** Shout-outs to merged community PRs (provider choice respected, Groq/Sonnet/Haiku support, Ollama context-length fix)
- **[0:01:41]** New features: code streaming (watch the LLM type each file) and the integrated bolt terminal showing command output
- **[0:02:40]** Standardized provider code auto-fetches all models (e.g. OpenRouter) plus a "get API key" button
- **[0:03:49]** UI demo: OpenRouter model list with pricing, then generating code with GPT-4o
- **[0:05:44]** Roadmap walkthrough on roadmap.sh and the case for a clear community vision
- **[0:07:12]** High-priority roadmap items: local projects, image attachments, backend agents, per-model prompts
- **[0:08:30]** Extension marketplace concept to avoid feature bloat
- **[0:09:36]** Crowdfunding update (possible Kickstarter, feature bounties)
- **[0:10:21]** Troubleshooting: terminal for backend 500s, dev-tools console for frontend errors
- **[0:12:15]** Blank preview is usually an LLM hallucination, not an oTToDev bug; fix by using a larger model

## Transcript

[Raw transcript](../raw/ottodev-is-becoming-the-best-open-source-ai-coding-assistant.md)
