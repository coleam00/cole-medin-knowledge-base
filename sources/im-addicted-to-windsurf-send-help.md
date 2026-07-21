---
type: source
title: "I'm Addicted to Windsurf, Send Help"
description: "Windsurf's flow-state IDE fuses co-pilot and agent into one experience, and a handful of disciplined habits (resetting long conversations, one request at a time, scoping context with @-references, and switching models when stuck) turn it into a massive time-saver."
youtube_id: ukhe1013Jpk
url: https://www.youtube.com/watch?v=ukhe1013Jpk
slug: im-addicted-to-windsurf-send-help
published: 2024-11-27
duration: "0:19:33"
recency_rank: 138
raw: "../raw/im-addicted-to-windsurf-send-help.md"
tags: [windsurf, ai-coding, flow-state, workflow]
created: 2026-07-21
updated: 2026-07-21
---

# I'm Addicted to Windsurf, Send Help

Cole makes the case that [Windsurf](../entities/tools/windsurf.md) is the best AI IDE of the moment because it collapses the two separate processes of writing code and consulting an agent into a single "flow state" experience where the agent is aware of every change you make and you can see every change it makes. He frames this against [the evolution of AI coding](../concepts/the-evolution-of-ai-coding.md): manual coding, then co-pilots (autocomplete) in 2022, then agents in 2024 (powerful but with unreasonable waiting periods, inconsistent results, and a disjointed IDE experience), and now flows that sync the human and agent timelines, an [AI coding harness](../concepts/ai-coding-harness.md) with tight [human-in-the-loop](../concepts/human-in-the-loop.md) control. He is candid that it does not produce production-ready code on its own, but insists that using it to lay groundwork, write tests, and document code frees up time for the highest-quality work, an example of separating the [phases of work](../concepts/phases-of-work.md).

The bulk of the video is a set of power-user habits that amount to deliberate [context engineering](../concepts/context-engineering.md). When long conversations make Claude 3.5 Sonnet start hallucinating ([context rot](../concepts/context-rot.md)), start a brand-new conversation to clear context rather than fighting it (a [context reset](../concepts/context-reset.md)). Give the agent one request at a time instead of spamming a list, because even a Chain-of-Thought agent confuses itself with too many simultaneous requirements, a form of [context isolation](../concepts/context-isolation.md). Take advantage of granular accept/reject of changes across files (changes are applied immediately so you can test before deciding, keeping [validation](../concepts/validation.md) in the loop). Use @-references to point the agent at exact files or functions so it edits the right thing, and be extremely specific, defining your tech stack ([FastAPI](../entities/tools/fastapi.md), Python, Postgres/[Supabase](../entities/tools/supabase.md), schema) up front rather than issuing vague prompts, which [reduces assumptions](../concepts/reduce-assumptions.md).

He also recommends switching to [OpenAI](../entities/organizations/openai.md)'s o1 when Sonnet gets stuck on a hard bug (paste the code and error, get the fix, paste it back and continue in flow), a [model-selection](../concepts/model-selection.md) move, using the function-scoped Refactor and Explain buttons to hone context on a single function, and leaning on the IDE to document code (telling it not to change code while documenting) and to scaffold test boilerplate. These habits stack together as a compounding practice. He closes by describing his broader workflow of building initial front ends in v0 or [Bolt](../entities/tools/bolt-new.md), then bringing them into Windsurf to finish, and predicting a near-future fully agentic IDE running locally with full machine access.

## Concepts covered

- [AI Coding Harness](../concepts/ai-coding-harness.md)
- [The Evolution of AI Coding](../concepts/the-evolution-of-ai-coding.md)
- [Context Rot](../concepts/context-rot.md)
- [Context Reset](../concepts/context-reset.md)
- [Phases of Work](../concepts/phases-of-work.md)
- [Human in the Loop](../concepts/human-in-the-loop.md)
- [Context Engineering](../concepts/context-engineering.md)
- [Reduce Assumptions](../concepts/reduce-assumptions.md)
- [Model Selection](../concepts/model-selection.md)
- [Context Isolation](../concepts/context-isolation.md)
- [Stacking Context-Engineering Strategies](../concepts/strategy-stacking.md)
- [Validation](../concepts/validation.md)

## Entities

- [Windsurf](../entities/tools/windsurf.md)
- [bolt.new](../entities/tools/bolt-new.md)
- [Anthropic](../entities/organizations/anthropic.md)
- [OpenAI](../entities/organizations/openai.md)
- [Cole Medin](../entities/people/cole-medin.md)
- [Supabase](../entities/tools/supabase.md)
- [FastAPI](../entities/tools/fastapi.md)

## Key moments

- **[0:02:01]** Windsurf's core pitch: built to keep you in flow state, unifying agent and co-pilot
- **[0:02:45]** History of AI coding: manual (pre-2022), co-pilots (2022), agents (2024), flows (Nov 2024)
- **[0:04:29]** Cole's general workflow: build front ends in v0/Bolt, finish in Windsurf
- **[0:08:25]** Tip 1: long conversations make the model hallucinate; start a new conversation to reset context
- **[0:09:20]** Tip 2: give one request at a time instead of spamming a list of fixes
- **[0:10:15]** Granular accept/reject of changes; changes are applied to code immediately so you can test first
- **[0:12:09]** Use @-references to point the agent at specific files or functions
- **[0:13:20]** Be specific and define your tech stack up front (FastAPI, Python, Postgres/Supabase)
- **[0:14:21]** Switch to o1 when Sonnet gets stuck on a hard bug, then continue in flow
- **[0:15:18]** Function-scoped Refactor and Explain buttons to hone context on one function
- **[0:16:13]** Use Windsurf to document code (tell it not to change the code) and to scaffold tests

## Transcript

[Raw transcript](../raw/im-addicted-to-windsurf-send-help.md)
