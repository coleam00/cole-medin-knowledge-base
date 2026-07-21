---
type: concept
title: "Vibe Planning"
description: "The deliberately unstructured first stage of planning: free-form exploration of ideas, architecture, and tech stack with the coding assistant as a research companion, before any structure or requirements doc is imposed."
tags: [planning, research, context-engineering]
videos: [the-true-power-of-ai-coding-build-your-own-workflows-full-guide]
created: 2026-07-21
updated: 2026-07-21
---

# Vibe Planning

Vibe planning is the loose, exploratory front end of a planning phase, before any template or requirements document is imposed. Cole names it as his own coinage and describes it as pure exploration: "I start with vibe planning. That's what I like to call it. We're basically just exploring very free form the different ideas that we want to implement" [0:01:33]. The output at this stage is not a document but a shared understanding: "when we're in the planning phase initially, all we're doing is exploring ideas, architecture, concepts, figuring out our tech stack. We're doing that with our AI coding assistant as our research companion" [0:05:34].

The word "vibe" is doing deliberate work. It borrows the looseness of [Vibe Coding](./vibe-coding.md) and moves it upstream, where looseness is cheap and useful. Exploring three architectures in conversation costs nothing to undo; discovering mid-implementation that you picked the wrong one costs the whole build. Vibe planning is therefore the inverse of vibe coding rather than an extension of it: unstructured at the point where reversibility is free, so the structured phases downstream can be tight.

The assistant here is a research companion, not an implementer. Good vibe planning looks like reading docs together, comparing libraries, asking what breaks at scale, and letting the model surface options you had not considered - and it should end with [Clarifying Questions](./clarifying-questions.md) that expose the assumptions you were about to build on. It ends when the ambiguity is gone, at which point the conversation is compressed into a real artifact: a PRD, a spec, or a structured plan that becomes the context object for implementation.

That handoff is what makes it safe. Vibe planning is stage zero of [Two-Layer Planning](./two-layer-planning.md), feeding the layer-one project brief that then decomposes into task-level plans. Skipping it produces plans that are well-formatted but built on an unexamined tech stack; never leaving it produces endless conversation and no build.

## Part of

- [Planning with AI](./planning-with-ai.md) - vibe planning is the exploratory opening of the planning phase.
- [The PIV Loop](./the-piv-loop.md) - it is the earliest, loosest part of the "P".

## Builds on

- [Two-Layer Planning](./two-layer-planning.md) - exploration feeds the layer-one project plan before task-level breakdown.

## Contrasts with

- [Vibe Coding](./vibe-coding.md) - same looseness, opposite placement: exploratory at the cheap stage instead of the expensive one.
- [Spec-Driven Development](./spec-driven-development.md) - the structured artifact vibe planning is deliberately not producing yet.

## Related

- [PRD-First Development](./prd-first-development.md) - the document exploration gets compressed into.
- [Clarifying Questions](./clarifying-questions.md) - how the assistant closes the remaining ambiguity.
- [Intent Engineering](./intent-engineering.md) - getting your actual intent out of your head and into the plan.
- [PRP Framework](./prp-framework.md) - turning explored requirements into an executable prompt.
- [Context Engineering](./context-engineering.md) - the plan is curated context handed into implementation.
- [Rapid Prototyping](./rapid-prototyping.md) - the other cheap way to resolve an architecture question.

## Tools

- [Claude Code](../entities/tools/claude-code.md) - Cole's research companion during the exploration pass.

## Sources

- [The True Power of AI Coding - Build Your OWN Workflows (Full Guide)](../sources/the-true-power-of-ai-coding-build-your-own-workflows-full-guide.md) - "[0:01:33] I start with vibe planning. That's what I like to call it. We're basically just exploring very free form the different ideas that we want to implement"
- [The True Power of AI Coding - Build Your OWN Workflows (Full Guide)](../sources/the-true-power-of-ai-coding-build-your-own-workflows-full-guide.md) - "[0:05:34] when we're in the planning phase initially, all we're doing is exploring ideas, architecture, concepts, figuring out our tech stack. We're doing that with our AI coding assistant as our research companion."
