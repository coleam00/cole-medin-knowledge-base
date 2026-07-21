---
type: concept
title: "PRP Framework"
description: "The Product Requirements Prompt pattern: a structured, context-rich prompt blueprint that hands an agent everything it needs to one-pass a feature."
tags: [prp-framework, context-engineering, prd-first-development, planning-with-ai]
videos: [context-engineering-101-the-simple-strategy-to-100x-ai-coding]
created: 2026-07-21
updated: 2026-07-21
---

# PRP Framework

The PRP (Product Requirements Prompt) framework is a structured prompt blueprint that packs everything an agent needs to ship a feature correctly on the first attempt. Cole's own definition is precise: "a PRP is a PRD plus curated codebase intelligence plus agent runbook and it's aiming to be the minimum viable packet an AI needs to plausibly ship production ready code uh on the first pass" [0:12:18]. Where a PRD (Product Requirements Document) states *what* to build for a human audience, a PRP adds the two things an agent additionally needs: the relevant slices of the codebase (patterns, files, conventions to follow) and a runbook of steps plus validation gates the agent executes.

The framework grew out of applying product management discipline to prompting: "PRP is really my attempt at building a prompt framework around uh product management. So like bringing the context needed uh for a coding agent to build the feature or the product that I wanted to build" [0:11:36]. The "minimum viable packet" framing is the load-bearing idea. The goal is not to dump the entire repository into context, which invites context rot, but to curate exactly the intelligence required and no more. A well-built PRP front-loads the planning and context-gathering so the implementation pass is nearly deterministic, with the agent able to validate its own work against criteria baked into the runbook.

## Part of

- [Context Engineering](./context-engineering.md) - the PRP is a concrete artifact of context engineering: it is the curated packet of context handed to the agent.

## Builds on

- [PRD-First Development](./prd-first-development.md) - a PRP is a PRD plus curated codebase intelligence plus an agent runbook.
- [Planning with AI](./planning-with-ai.md) - the PRP front-loads planning so the implementation pass can run in one shot.

## Related

- [Global Rules](./global-rules.md) - global rules supply always-on conventions that a PRP references rather than restates.
- [Validation](./validation.md) - the runbook portion of a PRP embeds the validation gates the agent checks its own work against.

## Sources

- [Context Engineering 101 - The Simple Strategy to 100x AI Coding](../sources/context-engineering-101-the-simple-strategy-to-100x-ai-coding.md) - "[0:12:18] a PRP is a PRD plus curated codebase intelligence plus agent runbook and it's aiming to be the minimum viable packet an AI needs to plausibly ship production ready code uh on the first pass."
- [Context Engineering 101 - The Simple Strategy to 100x AI Coding](../sources/context-engineering-101-the-simple-strategy-to-100x-ai-coding.md) - "[0:11:36] PRP is really my attempt at building a prompt framework around uh product management. So like bringing the context needed uh for a coding agent to build the feature or the product that I wanted to build."
