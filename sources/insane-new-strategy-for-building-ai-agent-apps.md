---
type: source
title: "INSANE New Strategy for Building AI Agent Apps"
description: "The fastest, cheapest way to build a custom frontend for an AI agent is to chain three kinds of AI coding tools together: a single-LLM builder to lay a strong foundation, an open-source local editor to iterate for free, and an AI IDE for final directed changes."
youtube_id: yRIEpNlacd0
url: https://www.youtube.com/watch?v=yRIEpNlacd0
slug: insane-new-strategy-for-building-ai-agent-apps
published: 2025-01-19
duration: "0:27:02"
recency_rank: 124
raw: "../raw/insane-new-strategy-for-building-ai-agent-apps.md"
tags: [ai-coding, frontend, workflow, tools]
created: 2026-07-21
updated: 2026-07-21
---

# INSANE New Strategy for Building AI Agent Apps

Cole walks through his production process for building custom frontends for AI agents, using a GitHub code-Q&A agent (a Pydantic AI agent already exposed as an API endpoint) as the running example. Rather than committing to a single AI coding tool, he combines three tool classes to get the best of each: Lovable (or bolt.new) is best at generating a strong initial foundation because it optimizes for one LLM; bolt.DIY is open source, runs locally, and lets you iterate with free models forever so you never burn out credits; and an AI IDE like Windsurf or Cursor is best for directed, fine-grained changes at the end. The workflow is: build in Lovable, push to GitHub, pull into bolt.DIY, tweak for free, download the zip, then open in an AI IDE and deploy.

The core reason the workflow is so smooth is that the agent is decoupled behind an API endpoint, so the same agent code from the previous video is reused unchanged while different frontends hook into it. Cole's prompting philosophy is to be general about the UI (these tools design good interfaces without much direction) but very specific about the functionality and API contract: the agent URL, the input schema (payload), the output schema, the Supabase URL and public anon key, the messages table schema, and the fact that realtime is enabled so the frontend can subscribe to new messages. He ends every build prompt with a catch-all requirements dump for stray asks (markdown support, a loading indicator, Supabase email/password auth).

Practical gotchas and tips: paste the Supabase project URL and public/anon key directly (they are not secret), but never the service role key; bolt's web container blocks requests to a localhost agent so live chat only works in Lovable and the downloaded local build, not inside bolt; you can drag/screenshot images into bolt.DIY/Gemini to give visual context; and the single best tip for iterating is to request one change at a time so the LLM understands and implements it correctly. The result is a free, flexible, fast blend for building all his agent frontends.

## Concepts covered

- [Stacking Context-Engineering Strategies](../concepts/strategy-stacking.md)
- [Contract-First Development](../concepts/contract-first.md)
- [Prompting Techniques for AI Coding](../concepts/ai-coding-prompting.md)
- [Iterative Prompting](../concepts/iterative-prompting.md)
- [Browser-Based AI Coding Tools](../concepts/browser-based-ai-coding.md)
- [Open-Source & Local AI Coding](../concepts/open-source-ai-coding.md)
- [Frontend-Agnostic Agents](../concepts/frontend-agnostic-agent.md)
- [Agent Security](../concepts/agent-security.md)

## Entities

- [Cole Medin](../entities/people/cole-medin.md)
- [Lovable](../entities/tools/lovable.md)
- [bolt.diy](../entities/tools/bolt-diy.md)
- [bolt.new](../entities/tools/bolt-new.md)
- [Windsurf](../entities/tools/windsurf.md)
- [Cursor](../entities/tools/cursor.md)
- [Supabase](../entities/tools/supabase.md)
- [Pydantic AI](../entities/tools/pydantic-ai.md)
- [GitHub](../entities/tools/github.md)
- [Live Agent Studio](../entities/tools/live-agent-studio.md)
- [Google Gemini 2.0 Flash](../entities/tools/gemini.md)

## Key moments

- **[0:00:33]** Introduces the three tool classes: Lovable/bolt.new (single-LLM builders), bolt.DIY (open-source local), and AI IDEs like Windsurf/Cursor
- **[0:02:46]** Reusing the prior video's Pydantic AI agent turned into an API endpoint so any frontend can hook into it
- **[0:04:15]** Why start with Lovable/bolt.new: optimizing for a single LLM gives the best initial foundation
- **[0:05:01]** Why move to bolt.DIY: run it yourself with free models to iterate endlessly without burning credits
- **[0:06:45]** Walkthrough of the Lovable build prompt: general on UI, specific on API/input/output schema
- **[0:08:34]** Bake the Supabase URL and public key directly into the code; include the messages table schema
- **[0:10:19]** Enable realtime on the messages table so the frontend subscribes to new messages
- **[0:13:24]** Full frontend built in one shot with Lovable, auth and conversation history working, talking to the local agent
- **[0:14:20]** Publish to GitHub, then clone/pull into bolt.DIY (install via node.js, pnpm install, pnpm run dev)
- **[0:20:14]** bolt's web container blocks requests to a localhost agent, so live chat only works in Lovable / local build
- **[0:21:11]** Key iteration tip: request one change at a time; drag/screenshot images for visual context
- **[0:22:26]** Download the zip from bolt.DIY, run npm install / npm run dev locally, then take into an AI IDE

## Transcript

[Raw transcript](../raw/insane-new-strategy-for-building-ai-agent-apps.md)
