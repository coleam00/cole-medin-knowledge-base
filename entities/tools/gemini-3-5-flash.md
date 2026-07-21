---
type: entity
subtype: tool
title: "Gemini 3.5 Flash"
description: "Google's cheap, fast LLM that builds unusually beautiful, handcrafted-looking frontends; the design half of Cole's provider-mixing workflow, paired with Opus 4.8 for planning and integrations."
tags: [llm, model, google, frontend, cost]
videos: [claude-plans-gemini-designs-the-workflow-to-build-beautiful-frontends]
created: 2026-07-21
updated: 2026-07-21
---

# Gemini 3.5 Flash

Gemini 3.5 Flash is Google's cheap, extremely fast model whose distinguishing trait is aesthetic rather than analytical. Cole opens with the claim the whole workflow rests on: "Google released Gemini 3.5 flash, an LLM that's cheap, insanely fast, and a lot of people are finding builds beautiful front-ends" ([0:00:00](../../sources/claude-plans-gemini-designs-the-workflow-to-build-beautiful-frontends.md)). Its UIs look handcrafted instead of template-generated, which is the one thing stronger reasoning models reliably fail to produce.

The price is what makes that trait usable at volume: "the price here $1.50 for every 1 million input tokens" ([0:02:34](../../sources/claude-plans-gemini-designs-the-workflow-to-build-beautiful-frontends.md)). Cheap tokens mean you can iterate hard on the visual layer, the step that most benefits from many attempts, while reserving expensive reasoning tokens for the parts that need judgment.

Its weakness is equally specific: Gemini crushes the UI but hallucinates page copy, and it is not the model you want wiring integrations. So Cole splits the build by strength. [Claude Opus 4.8](./claude-opus-4-8.md) does exploration, planning, copy, integrations, and fixes; Gemini 3.5 Flash owns exactly the design step. Because no single conversation can mix providers, each step is a separate coding-agent session that communicates only through markdown [handoff documents](../../concepts/handoff-documents.md). The design session reads only section A of the plan (content and intent, deliberately excluding site structure so the planner does not steamroll Gemini's strength) and emits a `ui-summary` for the integration session that follows.

Practically, it is driven through whichever harness supports it: [Pi](./pi-coding-agent.md) or [Google Antigravity](./google-antigravity.md) for the design node, [OpenRouter](./openrouter.md) as the gateway, [Claude Code](./claude-code.md) for the Opus nodes, and [Archon](./archon.md) to run the whole chain autonomously. The lesson generalizes past this model: single-task sessions make provider mixing trivial, so when a cheaper or prettier model ships you swap one node instead of rebuilding the workflow.

## Contrasts with

- [Claude Opus 4.8](./claude-opus-4-8.md) - The reasoning half of the pairing, better at accurate copy, planning, and integrations, and far more expensive.
- [Gemini 3](./gemini-3.md) - The flagship sibling release, strong on abstract reasoning rather than cheap high-volume design work.
- [Google Gemini 2.0 Flash](./gemini.md) - The earlier Flash line Cole used as a free prototyping default.

## Works with

- [Pi](./pi-coding-agent.md) - Minimal open-source harness used to run the Gemini design node.
- [Google Antigravity](./google-antigravity.md) - Alternative environment for driving Gemini models on the design step.
- [OpenRouter](./openrouter.md) - Gateway for reaching the model without committing the whole stack to one provider.
- [Claude Code](./claude-code.md) - Runs the Opus-driven planning, integration, and fix nodes on either side of the design step.
- [Archon](./archon.md) - Runs the entire multi-provider chain as an autonomous workflow.
- [Vercel Agent Browser CLI](./agent-browser.md) - Smoke-tests the site the design node produced.

## Related

- [Model Selection](../../concepts/model-selection.md) - Routing each step to the model that is actually best at it.
- [Provider Independence](../../concepts/provider-independence.md) - Structuring the workflow so any node's model can be swapped without a rewrite.
- [Handoff Documents](../../concepts/handoff-documents.md) - Markdown files are the only channel between sessions that share no history.
- [Context Isolation](../../concepts/context-isolation.md) - One clean context per step so no agent is doing four jobs at once.
- [Phases of Work](../../concepts/phases-of-work.md) - Explore, plan, design, integrate, validate, deploy, each finished before the next.
- [LLM Cost Optimization](../../concepts/llm-cost-optimization.md) - Spend cheap tokens on iteration, premium tokens only on reasoning.

## Sources

- [Claude Plans, Gemini Designs: The Workflow to Build BEAUTIFUL Frontends](../../sources/claude-plans-gemini-designs-the-workflow-to-build-beautiful-frontends.md) - "[0:00:00] Google released Gemini 3.5 flash, an LLM that's cheap, insanely fast, and a lot of people are finding builds beautiful front-ends"
- [Claude Plans, Gemini Designs: The Workflow to Build BEAUTIFUL Frontends](../../sources/claude-plans-gemini-designs-the-workflow-to-build-beautiful-frontends.md) - "[0:02:34] the price here $1.50 for every 1 million input tokens."
