---
type: source
title: "Claude Plans, Gemini Designs: The Workflow to Build BEAUTIFUL Frontends"
description: "By splitting a full-stack build into single-task coding-agent sessions that pass markdown handoff documents, you can mix providers, Gemini 3.5 Flash designing the UI and Opus 4.8 handling planning, copy, and integrations, to one-shot beautiful, non-trivial web apps cheaper and better than any single model."
youtube_id: iICZTWcryac
url: https://www.youtube.com/watch?v=iICZTWcryac
slug: claude-plans-gemini-designs-the-workflow-to-build-beautiful-frontends
published: 2026-06-03
duration: "0:18:05"
recency_rank: 11
raw: "../raw/claude-plans-gemini-designs-the-workflow-to-build-beautiful-frontends.md"
tags: [frontend, provider-mixing, workflow, model-selection]
created: 2026-07-21
updated: 2026-07-21
---

# Claude Plans, Gemini Designs: The Workflow to Build BEAUTIFUL Frontends

Cole demonstrates a provider-mixing workflow that leans on each model's strengths: Gemini 3.5 Flash (cheap, fast, unusually good at handcrafted-looking UIs) designs the front end, while Opus 4.8 (a stronger reasoner) handles planning, page copy, and full-stack integrations. The core insight is that no single conversation can mix providers, and even the best model gets overwhelmed doing exploration, planning, UI, and integration at once. So the workflow is built as a chain of separate coding-agent sessions, each focused on one task, communicating only through markdown handoff documents that the next node reads at its start.

The pipeline runs: an exploration step (Sonnet) surveys the repo and spec into context.md; a plan step (Opus) produces a three-section spec covering site content/intent, integration scope, and deployment, deliberately NOT describing site structure so Gemini's design strength isn't steamrolled; a design step (Gemini via Pi or Antigravity) reads only section A of the plan and builds the UI, emitting a ui-summary; then integrations, validation (Sonnet unit tests/linting), fixes (Opus), deployment, and a final agent-browser smoke test. Each step is a skill invoked in the appropriate harness after switching the model, and the whole thing can also run autonomously as an Archon workflow.

Beyond the specific stack, Cole frames this as reusable harness-engineering practice: separate sessions make it trivial to experiment with different provider mixes, let humans verify at each handoff, and keep every agent focused on a single job. The cost benefit is real, Gemini at ~$1.50 per million input tokens lets you spend heavily on UI iteration while Opus is reserved for the reasoning-heavy parts. The result one-shots proof-of-concept and MVP-grade full-stack apps (demoed with a 'deep space catalog' site) that look handcrafted with accurate, non-hallucinated copy and a working backend.

## Concepts covered

- [Provider Independence](../concepts/provider-independence.md)
- [Model Selection](../concepts/model-selection.md)
- [Context Isolation](../concepts/context-isolation.md)
- [Phases of Work](../concepts/phases-of-work.md)
- [Two-Layer Planning](../concepts/two-layer-planning.md)
- [Planning with AI](../concepts/planning-with-ai.md)
- [Reduce Assumptions](../concepts/reduce-assumptions.md)
- [Skills](../concepts/skills.md)
- [Agentic Workflow Engineering](../concepts/agentic-workflow-engineering.md)
- [Human in the Loop](../concepts/human-in-the-loop.md)
- [End-to-End Validation](../concepts/end-to-end-validation.md)
- [Validation](../concepts/validation.md)

## Entities

- [Cole Medin](../entities/people/cole-medin.md)
- [Pydantic AI](../entities/tools/pydantic-ai.md)
- [Claude Code](../entities/tools/claude-code.md)
- [Archon](../entities/tools/archon.md)
- [Vercel Agent Browser CLI](../entities/tools/agent-browser.md)
- [OpenRouter](../entities/tools/openrouter.md)
- [Sonar (Sonar Summit)](../entities/organizations/sonar.md)
- [Vercel](../entities/organizations/vercel.md)

## Key moments

- **[0:00:00]** Sets up the two models: Gemini 3.5 Flash (cheap, fast, beautiful UIs) and Opus 4.8 (reasoning powerhouse for agentic tasks)
- **[0:00:35]** Introduces the mixed-provider workflow: Gemini designs the UI, Opus plans copy and integrations for full-stack apps
- **[0:01:42]** Gemini crushes the UI but hallucinates page copy; Opus is better at accurate copy and integrations
- **[0:04:40]** Core design principle: every step is a separate coding-agent session communicating via markdown handoff documents
- **[0:05:15]** Two reasons for separate sessions: you can't mix providers in one conversation, and it makes provider experimentation trivial
- **[0:05:46]** Second reason: each step focused on a single task because LLMs get overwhelmed doing too much at once
- **[0:07:01]** Sonar / SonarQube advanced security sponsor read on verifying AI-written code and dependencies at machine speed
- **[0:08:59]** Exploration step with Sonnet surveys the spec+repo into context.md
- **[0:11:35]** Plan step with Opus produces a three-section spec (content/intent, integration, deployment)
- **[0:13:11]** Section A deliberately omits site structure so Opus doesn't steamroll Gemini's design strength
- **[0:14:28]** Design step: Gemini via Pi or Antigravity reads only section A and builds the UI, emitting ui-summary
- **[0:16:16]** Remaining nodes repeat the handoff pattern: integrations, validation, fixes, deployment, agent-browser smoke test

## Transcript

[Raw transcript](../raw/claude-plans-gemini-designs-the-workflow-to-build-beautiful-frontends.md)
