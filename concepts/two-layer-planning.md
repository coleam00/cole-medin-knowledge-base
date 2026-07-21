---
type: concept
title: "Two-Layer Planning"
description: "Separating high-level strategic planning from detailed task planning, using a stronger model for the former."
tags: [planning, strategy, decomposition]
videos: [claude-plans-gemini-designs-the-workflow-to-build-beautiful-frontends, full-guide-to-becoming-a-principled-agentic-engineer-build-anything-with-ai, my-complete-agentic-coding-workflow-to-build-anything-no-fluff-or-overengineering, the-5-techniques-separating-top-agentic-engineers-right-now, the-true-power-of-ai-coding-build-your-own-workflows-full-guide, code-100x-faster-with-ai-heres-how-no-hype-full-process]
created: 2026-07-21
updated: 2026-07-21
---

# Two-Layer Planning

Two-layer planning is the discipline of splitting planning into two distinct altitudes: a high-level project layer and a detailed task layer. Cole states the rule directly: "for planning with AI coding, you always have two layers. You have the project level planning... the PM level planning and then you have the task planning and that is the individual ticket level." The two layers differ in what they touch. Layer one stays out of the code, "the layer one planning is higher level here are the features that we want to build... we are not digging into the code," while layer two is where "we get more in the weeds" on a single ticket.

The first layer is the project brief: vision, architecture, constraints, and the feature set. "Our planning document, this is where we have the highle vision, architecture constraints, all of these highlevel pieces of information that we want to give as context to the LLM." In Cole's workflow this layer is the PRD plus global rules, "the top level project planning. That is what we already did creating our PRD and our rules." A rich variant is a three-section spec that names the content/intent, the integrations, and the deployment up front: "we have to describe the information in the UI, how we're going to do any kinds of integrations like a back-end or authentication. And then also, how we're going to deploy the application."

The second layer takes one feature from that project plan and expands it into a task-by-task build sheet: "at a slightly lower level, we have the task markdown file," which is "just very focused on an individual feature and all of the tasks that come with that." This structured plan then becomes the context object handed into implementation: "we create our structured plan. This is the markdown document that we're going to output that we use as context going into execution." Separating the layers keeps each planning pass focused and lets you reserve your strongest reasoning model for the high-level architecture decisions while cheaper passes handle task breakdown.

## Part of

- [Planning with AI](./planning-with-ai.md) - two-layer planning is how planning is structured across altitudes.
- [The PIV Loop](./the-piv-loop.md) - both layers front-load the "P" step; layer-two plans feed implementation.

## Builds on

- [PRD-First Development](./prd-first-development.md) - the layer-one project plan is the PRD plus global rules.
- [Phases of Work](./phases-of-work.md) - layer-two plans are often scoped to a single phase or feature.
- [Spec-Driven Development](./spec-driven-development.md) - the multi-section spec is the artifact the layers produce.

## Related

- [Context Engineering](./context-engineering.md) - each plan is curated context handed into the next stage.
- [Context Isolation](./context-isolation.md) - the two layers run in separate, focused sessions.
- [Context Reset](./context-reset.md) - the layer-two plan lets you start implementation with a clean window.
- [PRP Framework](./prp-framework.md) - turning initial requirements into a structured, task-level prompt.

## Tools

- [Claude Code](../entities/tools/claude-code.md) - Cole's planner, used with a strong model for the high-level layer.

## Sources

- [FULL Guide to Becoming a Principled Agentic Engineer](../sources/full-guide-to-becoming-a-principled-agentic-engineer-build-anything-with-ai.md) - "[0:39:00] for planning with AI coding, you always have two layers. You have the project level planning... the PM level planning and then you have the task planning and that is the individual ticket level."
- [FULL Guide to Becoming a Principled Agentic Engineer](../sources/full-guide-to-becoming-a-principled-agentic-engineer-build-anything-with-ai.md) - "[0:39:28] the layer one planning is higher level here are the features that we want to build... we are not digging into the code now that we're peaking a single ticket for layer 2. This is where we get more in the weeds."
- [My COMPLETE Agentic Coding Workflow to Build Anything](../sources/my-complete-agentic-coding-workflow-to-build-anything-no-fluff-or-overengineering.md) - "[0:23:49] we have two layers of planning. We have the top level project planning. That is what we already did creating our PRD and our rules. And now we have the taskspecific planning."
- [My COMPLETE Agentic Coding Workflow to Build Anything](../sources/my-complete-agentic-coding-workflow-to-build-anything-no-fluff-or-overengineering.md) - "[0:24:22] the structure plan is just very focused on an individual feature and all of the tasks that come with that."
- [Code 100x Faster with AI, Here's How](../sources/code-100x-faster-with-ai-heres-how-no-hype-full-process.md) - "[0:05:59] our planning document, this is where we have the highle vision, architecture constraints, all of these highlevel pieces of information that we want to give as context to the LLM."
- [Code 100x Faster with AI, Here's How](../sources/code-100x-faster-with-ai-heres-how-no-hype-full-process.md) - "[0:06:30] at a slightly lower level, we have the task markdown file."
- [Claude Plans, Gemini Designs: The Workflow to Build BEAUTIFUL Frontends](../sources/claude-plans-gemini-designs-the-workflow-to-build-beautiful-frontends.md) - "[0:12:41] It's a three-section spec because we have to describe the information in the UI, how we're going to do any kinds of integrations like a back-end or authentication. And then also, how we're going to deploy the application."
- [The 5 Techniques Separating Top Agentic Engineers Right Now](../sources/the-5-techniques-separating-top-agentic-engineers-right-now.md) - "[0:10:48] we create our structured plan. This is the markdown document that we're going to output that we use as context going into execution."
- [The True Power of AI Coding - Build Your OWN Workflows](../sources/the-true-power-of-ai-coding-build-your-own-workflows-full-guide.md) - "[0:08:43] this is exactly what the PRP framework accomplishes... When you generate a PRP, you're taking your initial requirements and turning it into a much more structured document for the coding assistant."
