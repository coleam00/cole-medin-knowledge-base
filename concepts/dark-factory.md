---
type: concept
title: "Dark Factory"
description: "A self-evolving codebase where autonomous workflows build and improve a product with minimal human touch."
tags: [self-evolving, autonomous, dark-factory]
videos: [the-best-ai-coding-setup-isnt-the-most-autonomous-one-heres-why, im-building-an-ai-dark-factory-that-ships-its-own-code-public-experiment, ai-youtube-is-only-claude-hype-now]
created: 2026-07-21
updated: 2026-07-21
---

# Dark Factory

A dark factory is a development pipeline that takes a specification in and produces shipped code out, with as little human intervention as possible. Borrowing the manufacturing term for a lights-out, fully automated plant, Cole defines it precisely: "the way that a dark factory works is your input is your spec, the large document that outlines everything you want to build. And what you get out of the dark factory is shipped code." The aspiration is stark, "if your business can get to the point where you have a process where you can send in a spec and get out shipped code, that my friend is the dream."

What separates a dark factory from "AI writes code" is structure. "A dark factory isn't just AI writes code. It's a system with distinct components that handle different stages of the development pipeline." Those stages, planning, code generation, review, and validation, are the same specialist components of an engineered [AI coding harness](./ai-coding-harness.md), stitched together so a spec can flow through them autonomously. The dark factory is therefore the harness pushed to its logical endpoint: instead of a human driving each handoff, deterministic workflows and reviewer agents carry the work from spec to merged, shipped code.

Cole runs this as a deliberately extreme public experiment. "I've also been working on my Dark Factory experiment, which is a code base and I'm handing the reins over completely to AI coding assistants," with a hard rule: "no human is allowed to review code or even write any code." He frames it on a ladder of autonomy where the top rung is radical, "the dark factory level five, this is where we aren't even reviewing the code before it goes to production. It is a crazy idea." Notably, Cole's broader thesis is that maximum autonomy is not the same as best, the dark factory is the frontier to learn from, not necessarily the setup he recommends for everyday work.

## Builds on

- [AI Coding Harness](./ai-coding-harness.md) - the dark factory is a harness run end to end with the human removed.
- [The Evolution of AI Coding](./the-evolution-of-ai-coding.md) - the dark factory sits at the autonomous frontier of that progression.

## Part of

- [System Evolution](./system-evolution.md) - a self-evolving codebase that builds and improves itself over time.

## Related

- [Agentic Coding](./agentic-coding.md) - the practice the dark factory automates fully.
- [Deterministic Workflows](./deterministic-workflows.md) - the repeatable pipeline stages a spec flows through.
- [Spec-Driven Development](./spec-driven-development.md) - the spec is the sole input to the factory.
- [Separate Reviewer](./separate-reviewer.md) - the independent review stage in the pipeline.
- [MiniMax M2.7](../entities/tools/minimax-m2.md) - A cheap, fast, capable LLM that Cole routes Claude Code to (via environment variables) to drive the entire dark factory economically at high throughput instead of Anthropic models.
- [Agents That Build Agents](./agents-that-build-agents.md) - A meta-agent whose specialty is generating, iterating on, and eventually running other AI agents on demand, so the agents it produces become reusable sub-agents themselves.
- [The Five Levels of AI Coding Autonomy](./five-levels-of-ai-coding-autonomy.md) - Dan Shapiro's framework mapping the SAE five levels of driving automation onto how much control you hand a coding agent, from 'spicy autocomplete' (level 0) to the 'dark factory' (level 5).

## Sources

- [The Best AI Coding Setup Isn't the Most Autonomous One (Here's Why)](../sources/the-best-ai-coding-setup-isnt-the-most-autonomous-one-heres-why.md) - "[0:07:02] the way that a dark factory works is your input is your spec, the large document that outlines everything you want to build. And what you get out of the dark factory is shipped code."
- [The Best AI Coding Setup Isn't the Most Autonomous One (Here's Why)](../sources/the-best-ai-coding-setup-isnt-the-most-autonomous-one-heres-why.md) - "[0:16:49] a dark factory isn't just AI writes code. It's a system with distinct components that handle different stages of the development pipeline."
- [I'm Building an AI Dark Factory That Ships Its Own Code (Public Experiment)](../sources/im-building-an-ai-dark-factory-that-ships-its-own-code-public-experiment.md) - "[0:00:19] What we're doing with a dark factory is building an entire system where we hand the reigns of a codebase over to AI entirely."
- [I'm Building an AI Dark Factory That Ships Its Own Code (Public Experiment)](../sources/im-building-an-ai-dark-factory-that-ships-its-own-code-public-experiment.md) - "[0:06:33] the dark factory level five, this is where we aren't even reviewing the code before it goes to production. It is a crazy idea."
- [AI YouTube Is Only Claude Hype Now](../sources/ai-youtube-is-only-claude-hype-now.md) - "[0:05:05] No human is allowed to review code or even write any code."
