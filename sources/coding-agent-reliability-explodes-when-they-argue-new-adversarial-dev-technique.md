---
type: source
title: "Coding Agent Reliability EXPLODES When They Argue (New Adversarial Dev Technique)"
description: "Pairing a coding agent with a separate, adversarial evaluator agent (a GAN-inspired harness) dramatically improves reliability by defeating the sycophancy that ruins single-agent self-review."
youtube_id: HAkSUBdsd6M
url: https://www.youtube.com/watch?v=HAkSUBdsd6M
slug: coding-agent-reliability-explodes-when-they-argue-new-adversarial-dev-technique
published: 2026-03-30
duration: "0:17:37"
recency_rank: 23
raw: "../raw/coding-agent-reliability-explodes-when-they-argue-new-adversarial-dev-technique.md"
tags: [ai-coding-harness, adversarial-agents, reliability, validation]
created: 2026-07-21
updated: 2026-07-21
---

# Coding Agent Reliability EXPLODES When They Argue (New Adversarial Dev Technique)

Cole argues that the biggest problem in AI coding is sycophancy: models are biased toward agreeing with the user and toward giving their own work a gold star, so having a coding agent evaluate its own output is like a student grading their own homework. The fix is 'adversarial dev', spinning up a totally separate coding agent, with its own context session, whose only job is to nitpick and rip apart the main agent's implementation. He grounds this in a new Anthropic blog post on long-running coding-agent harnesses, which takes inspiration from generative adversarial networks (GANs): a generator tries to satisfy (or 'trick') an evaluator/discriminator, and the pressure produces better output over time.

Anthropic's harness uses three agents, a planner that expands the user prompt into a full spec, then a generator/evaluator loop. Cole rebuilt the whole thing from scratch in both Claude and Codex versions (which can be mixed, e.g. Claude implements, Codex evaluates) because Anthropic didn't open-source it. The most interesting mechanic: before any code is written, the generator and evaluator negotiate a contract up front, agreeing on the phases/sprints to break the spec into and the scored 1-10 criteria (with thresholds) each phase will be judged against. The generator retries up to three times per phase to appease the evaluator; if the evaluator judges honestly against criteria that point at the app actually working, then 'appeasing' it means the app really works.

He demonstrates by one-shotting an elaborate full-stack RAG app over his YouTube content (streaming, sources, polished UI) in ~4 hours, something a single agent couldn't produce. The tradeoff is token cost from the long specking + implement + evaluate + iterate loop, but Cole considers the reliability worth it, and notes harnesses let you lean on cheaper/faster models: he built the whole app with Sonnet 4.6, which the harness lifted above what even Opus 4.6 could one-shot alone. He also clarifies that using an Anthropic or Codex subscription with the Agent SDK / headless mode is allowed for local development and experimentation (but not for a business others use).

## Concepts covered

- [Sycophancy](../concepts/sycophancy.md)
- [Adversarial Agents](../concepts/adversarial-agents.md)
- [Separate Reviewer](../concepts/separate-reviewer.md)
- [AI Coding Harness](../concepts/ai-coding-harness.md)
- [Contract-First Development](../concepts/contract-first.md)
- [Phases of Work](../concepts/phases-of-work.md)
- [Validation](../concepts/validation.md)
- [Planning with AI](../concepts/planning-with-ai.md)
- [Model Selection](../concepts/model-selection.md)
- [Provider Independence](../concepts/provider-independence.md)

## Entities

- [Anthropic](../entities/organizations/anthropic.md)
- [Claude Code](../entities/tools/claude-code.md)
- [Codex](../entities/tools/codex.md)
- [Claude Agent SDK](../entities/tools/claude-agent-sdk.md)
- [Cole Medin](../entities/people/cole-medin.md)
- [Scrimba](../entities/organizations/scrimba.md)

## Key moments

- **[0:00:00]** Sycophancy defined as the biggest problem in AI, and it's getting worse as models get more powerful
- **[0:00:32]** Why sycophancy is worst in AI coding: an agent grading its own work stuffs the big problems under the rug
- **[0:01:04]** The fix: give the agent an adversarial sparring partner, a separate agent whose job is to rip apart the implementation ('adversarial dev')
- **[0:02:56]** Anthropic's harness takes inspiration from GANs (generator vs discriminator)
- **[0:03:48]** Three-agent structure: planner creates the spec, then the generator/evaluator loop
- **[0:04:19]** Anthropic's retro game-maker test: single agent's gameplay didn't work; harness version was playable
- **[0:05:33]** Cole one-shots an elaborate full-stack RAG YouTube-chat app with the harness
- **[0:08:05]** Planner expands the user prompt into a harness-optimized spec so you don't have to over-specify
- **[0:09:52]** Before writing code, generator and evaluator negotiate a contract: phases and per-phase evaluation criteria
- **[0:11:16]** Spec split into sprints with 1-10 scored criteria and thresholds; pass to move to the next sprint
- **[0:12:22]** Generator retries a maximum of three times to appease the evaluator
- **[0:13:39]** You can use an Anthropic/Codex subscription with the harness for local dev; API key required if building a business on the SDK
- **[0:16:32]** Built entirely with Sonnet 4.6; the harness let a cheaper model beat what Opus 4.6 could one-shot alone

## Transcript

[Raw transcript](../raw/coding-agent-reliability-explodes-when-they-argue-new-adversarial-dev-technique.md)
