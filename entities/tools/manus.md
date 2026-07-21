---
type: entity
subtype: tool
title: "Manus"
description: "First-of-its-kind general AI agent that pioneered context-engineering strategies; reportedly being acquired by Meta."
resource: "https://manus.im"
tags: [general-agent, context-engineering, harness, file-system-as-context]
videos: [ai-exploded-in-2025-heres-everything-that-happened, are-agent-harnesses-bringing-back-vibe-coding]
created: 2026-07-21
updated: 2026-07-21
---

# Manus

Manus is a general-purpose AI agent that Cole credits as a category opener: "the first of its kind general AI agent that really was the pioneer for a lot of strategies around context engineering" ([0:03:33] of the 2025-recap video). Where most agents of its era were narrow, Manus took an open-ended task and ran a long, autonomous loop to completion, and in doing so it worked out many of the context-management techniques that later became standard practice.

## Why it matters across the videos

Cole's most concrete takeaway from Manus is architectural. It was one of the early platforms to implement a full agent harness: "There are a lot of platforms out there like Langchain deep agents, like Manis, for example, that we had way back at the start of this year. They've already implemented a harness" ([0:04:09] of the harness video). And the specific context-engineering move he cites is using the file system as external memory rather than cramming everything into the context window: "Manis, they have this really awesome article ... they call out here as well that they use the file system as context" ([0:14:38]). That pattern, offloading state to files and reading it back on demand, is a recurring theme in Cole's work on harnesses and long-running agents.

Manus is also a market signal in Cole's year-in-review: "Meta is going to acquire Manis" ([0:16:38]), which he reads as validation that general agents pioneered by a startup are now strategic assets for the big labs.

## Related

- [Context Engineering](../../concepts/context-engineering.md) - the discipline Manus pioneered.
- [The Problems With MCP Servers](../../concepts/mcp-problems.md) and [Progressive Disclosure](../../concepts/progressive-disclosure.md) - context-budget problems the file-system-as-context approach helps solve.
- [Skills](../../concepts/skills.md) - the later packaging of the same load-on-demand idea.
- [Vibe Coding](../../concepts/vibe-coding.md) - the harness-driven autonomy the harness video connects Manus to.
- [The Evolution of AI Coding](../../concepts/the-evolution-of-ai-coding.md) - where Manus sits in the timeline of general agents.

## Sources

- [AI Exploded in 2025 - Here's Everything That Happened](../../sources/ai-exploded-in-2025-heres-everything-that-happened.md) - "[0:03:33] Manis, the first of its kind general AI agent that really was the pioneer for a lot of strategies around context engineering"
- [AI Exploded in 2025 - Here's Everything That Happened](../../sources/ai-exploded-in-2025-heres-everything-that-happened.md) - "[0:16:38] Meta is going to acquire Manis"
- [Are Agent Harnesses Bringing Back Vibe Coding?](../../sources/are-agent-harnesses-bringing-back-vibe-coding.md) - "[0:04:09] There are a lot of platforms out there like Langchain deep agents, like Manis, for example, that we had way back at the start of this year. They've already implemented a harness."
- [Are Agent Harnesses Bringing Back Vibe Coding?](../../sources/are-agent-harnesses-bringing-back-vibe-coding.md) - "[0:14:38] Manis, they have this really awesome article... they call out here as well that they use the file system as context."
