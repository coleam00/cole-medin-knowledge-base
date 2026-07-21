---
type: source
title: "Are Agent Harnesses Bringing Back Vibe Coding?"
description: "Agent harnesses are the natural evolution of prompt and context engineering that connect many agent sessions to reliably run long tasks, and they can make a heavily-engineered, human-in-the-loop form of vibe coding viable once two problems (bounded attention and compounding reliability) are solved."
youtube_id: 13HP_bSeNjU
url: https://www.youtube.com/watch?v=13HP_bSeNjU
slug: are-agent-harnesses-bringing-back-vibe-coding
published: 2025-12-17
duration: "0:25:42"
recency_rank: 48
raw: "../raw/are-agent-harnesses-bringing-back-vibe-coding.md"
tags: [harness, context-engineering, context-rot, human-in-the-loop]
created: 2026-07-21
updated: 2026-07-21
---

Cole traces a three-stage timeline of how we interact with LLMs: prompt engineering (optimizing single interactions, born around GPT-3 in 2020) evolved into context engineering (optimizing whole sessions and context windows), which has now evolved into agent harnesses (a wrapper that connects many context windows and sessions together to handle long-running tasks). Crucially, harnesses do not replace context engineering. Each individual session inside a harness still uses all the context-engineering strategies (RAG, memory systems, sub-agent isolation, validation, prompt optimization), and the harness layer adds checkpoints, handoffs, human-in-the-loop, and guardrails on top. This matters now because raw LLM power has hit a scaling wall, so the layer we build on top of the model (reasoning, memory, tooling, harnesses) is where the gains come from.

He gets concrete about the architecture, focusing on the most common pattern: an initializer agent that sets the stage (reads an appspec or PRD, produces a feature-list of 200+ features with validation, scaffolds the project, inits git) followed by a task agent run in a loop, clearing the context window between sessions so it never hits context rot. Each new session must prime itself from scratch (progress files, git log, the codebase itself), run checkpoints and regression tests, pick the highest-priority feature, implement and self-validate, then leave clean handoff artifacts and commit. Git and the file system serve as long-term memory. He cites Anthropic's open-sourced long-running harness (which he re-implemented using Linear instead of local files to track progress), and references LangChain deep agents and Manus as prior art.

Two unsolved problems keep harnesses experimental. Bounded attention (context rot) is only partially solved: summarization in handoffs frequently drops critical information (like a validation failure and its fix), causing the same mistake to repeat across sessions, and you cannot predict which observation becomes critical ten steps later. Reliability compounds badly: a 95%-reliable agent over 20 steps is only 0.95^20, about 36% reliable for the whole system, and true end-to-end vibe coding would need roughly 99.9% reliability, which agents will not hit. The partial fix is checkpoints, git rollback, and structured handoffs, but the missing piece is smart, strategic human-in-the-loop injection points. Cole's take: 2025 was the year of vibe coding; 2026 will be the year of harnesses, and a heavily-engineered harness with the right human checkpoints can make a very different, disciplined form of vibe coding viable.

## Concepts covered

- [AI Coding Harness](../concepts/ai-coding-harness.md)
- [The Evolution of AI Coding](../concepts/the-evolution-of-ai-coding.md)
- [Context Engineering](../concepts/context-engineering.md)
- [Context Rot](../concepts/context-rot.md)
- [Context Reset](../concepts/context-reset.md)
- [The AI Layer](../concepts/the-ai-layer.md)
- [Human in the Loop](../concepts/human-in-the-loop.md)
- [Validation](../concepts/validation.md)
- [Git as Long-Term Memory](../concepts/git-as-long-term-memory.md)
- [Prime Command](../concepts/prime-command.md)
- [Memory Systems](../concepts/memory-systems.md)
- [Context Isolation](../concepts/context-isolation.md)
- [Vibe Coding](../concepts/vibe-coding.md)
- [The Ralph Loop](../concepts/the-ralph-loop.md)
- [Agent Graphs](../concepts/agent-graphs.md)
- [PRD-First Development](../concepts/prd-first-development.md)

## Entities

- [Cole Medin](../entities/people/cole-medin.md)
- [Anthropic](../entities/organizations/anthropic.md)
- [Linear](../entities/tools/linear.md)
- [Manus](../entities/tools/manus.md)
- [Git](../entities/tools/git.md)
- [Dynamous](../entities/organizations/dynamous.md)

## Key moments

- **[0:01:21]** The timeline: prompt engineering -> context engineering -> agent harnesses, all about how we interact with the LLM
- **[0:04:41]** The harsh truth: raw LLM power is no longer exploding; the layer on top of LLMs is where gains come from
- **[0:06:06]** Transition into what an agent harness actually looks like
- **[0:06:38]** Core mechanic: connecting sessions, or one agent looped with context clears to avoid context rot
- **[0:07:10]** Most common architecture: an initializer agent + a task agent run in a loop
- **[0:09:10]** Guardrails, checkpoints, and handoffs as the key parts of harnesses
- **[0:12:53]** Concrete coding-session flow: prime -> checkpoint -> pick feature -> implement -> validate -> handoff
- **[0:15:56]** Walkthrough of Anthropic's open-sourced harness: appspec -> initializer -> feature-list -> looped coding agent
- **[0:17:55]** Cole ran the harness 24 hours straight and it built a full Claude.ai clone
- **[0:19:21]** Unsolved problem 1: bounded attention / context rot, only partially solved
- **[0:21:12]** Unsolved problem 2: reliability compounds; 0.95^20 = ~36% over 20 steps
- **[0:23:38]** Conclusion: a heavily-engineered harness with human-in-the-loop makes a different kind of vibe coding viable; 2026 is the year of harnesses

## Transcript

[Raw transcript](../raw/are-agent-harnesses-bringing-back-vibe-coding.md)
