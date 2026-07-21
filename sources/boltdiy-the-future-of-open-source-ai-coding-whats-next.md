---
type: source
title: "bolt.diy: The Future of Open Source AI Coding - What's Next?"
description: "Fresh off making bolt.diy the official open-source bolt.new, Cole walks through the community roadmap, self-hosting resources, and a wave of new maturity features aimed at building the best open-source AI coding assistant."
youtube_id: aZn8PhqUZVU
url: https://www.youtube.com/watch?v=aZn8PhqUZVU
slug: boltdiy-the-future-of-open-source-ai-coding-whats-next
published: 2024-12-18
duration: "0:20:48"
recency_rank: 132
raw: "../raw/boltdiy-the-future-of-open-source-ai-coding-whats-next.md"
tags: [bolt-diy, open-source, roadmap, ai-coding]
created: 2026-07-21
updated: 2026-07-21
---

# bolt.diy: The Future of Open Source AI Coding - What's Next?

This is a community update and roadmap video for [bolt.diy](../entities/tools/bolt-diy.md), the open-source AI web-app builder that just became the official open-source fork of [StackBlitz](../entities/organizations/stackblitz.md)'s bolt.new. Cole frames the moment as capitalizing on partnership momentum and lays out a long-term vision built on [community-driven development](../concepts/community-driven-development.md): a per-LLM prompt library (because a prompt tuned for Claude 3.5 Sonnet underperforms on Qwen, Llama 3.3, or Gemini, an argument for [provider independence](../concepts/provider-independence.md) and careful [model selection](../concepts/model-selection.md)), file walking and diffs so the tool stops rewriting whole files, one-click deploys, better repo organization (kanban board, CI/CD, releases), and an extension marketplace/plugin system that lets contributors add features without bloating the core UI or editing the main repo.

He also previews more speculative roadmap items: a pre-[planning](../concepts/planning-with-ai.md) step where a reasoning model like QwQ drafts a README/plan before any code is written, and an agentic mixture-of-experts backend where multiple smaller LLMs collaborate ([agent teams](../concepts/agent-teams.md)) to produce better results than a single call. The middle of the video points viewers to community-authored resources for getting started and self-hosting bolt.diy, recommending Cloudflare Pages as the deployment target and noting [Ollama](../entities/tools/ollama.md) will not work for hosted instances since the site cannot reach a local model.

The final third demos concrete shipped features from the maintainer team: a redesigned settings panel with toggleable providers and an experimental optimized system prompt, a debug tab that surfaces system info and connection status for troubleshooting, per-prompt token usage (prompt vs completion) for [cost visibility](../concepts/agent-observability.md), a resizable full-screen preview, and the ability to screenshot part of the preview and feed it back to the LLM to fix visual mistakes. Cole closes by inviting the community to contribute ideas and pull requests, positioning bolt.diy as a leading example of open-source [agentic coding](../concepts/agentic-coding.md) and [AI coding assistants](../concepts/ai-coding-assistant.md) with strong [local AI](../concepts/local-ai.md) and [no-code automation](../concepts/no-code-automation.md) leanings.

## Concepts covered

- [Provider Independence](../concepts/provider-independence.md)
- [Model Selection](../concepts/model-selection.md)
- [Planning with AI](../concepts/planning-with-ai.md)
- [Agent Teams](../concepts/agent-teams.md)
- [No-Code Automation](../concepts/no-code-automation.md)
- [AI Coding Assistant](../concepts/ai-coding-assistant.md)
- [Agent Observability](../concepts/agent-observability.md)
- [Agentic Coding](../concepts/agentic-coding.md)
- [Community-Driven Development](../concepts/community-driven-development.md)
- [Local & Self-Hosted AI](../concepts/local-ai.md)

## Entities

- [bolt.diy](../entities/tools/bolt-diy.md)
- [StackBlitz](../entities/organizations/stackblitz.md)
- [Cole Medin](../entities/people/cole-medin.md)
- [Ollama](../entities/tools/ollama.md)
- [Netlify](../entities/tools/netlify.md)
- [Supabase](../entities/tools/supabase.md)

## Key moments

- **[0:00:00]** bolt.diy becomes the official open-source bolt.new via partnership with StackBlitz
- **[0:01:40]** Walkthrough of the public roadmap: finished items and what's next
- **[0:04:00]** Prompt library idea: different LLMs need different prompts
- **[0:04:46]** File walking and diffs to stop rewriting whole files
- **[0:05:44]** Plugin system / extension marketplace to avoid feature bloat
- **[0:06:41]** Pre-planning with a reasoning model (QwQ) before coding
- **[0:07:24]** Agentic mixture-of-experts backend using smaller LLMs together
- **[0:11:06]** Self-hosting resources; Cloudflare Pages recommended, Ollama will not work hosted
- **[0:15:14]** New settings panel with toggleable providers and experimental optimized prompt
- **[0:15:47]** Debug tab surfacing system info and provider connection status
- **[0:17:18]** Per-prompt token usage (prompt vs completion) for cost visibility
- **[0:18:27]** Screenshot part of the preview and send it to the LLM to fix mistakes

## Transcript

[Raw transcript](../raw/boltdiy-the-future-of-open-source-ai-coding-whats-next.md)
