---
type: concept
title: "Compounding Error Rates"
description: "Because agentic systems chain many steps that must each succeed, per-step error rates multiply, so a chain of 95%-reliable steps collapses to low end-to-end reliability."
tags: [reliability, multi-agent, error-compounding]
videos: [are-agent-harnesses-bringing-back-vibe-coding, my-top-20-lessons-from-building-100s-of-ai-agents-super-actionable]
created: 2026-07-21
updated: 2026-07-21
---

# Compounding Error Rates

Compounding error rates is the arithmetic that governs every multi-step agentic system: reliability multiplies, it does not average. Each step in a chain has to succeed for the run to succeed, so a per-step number that sounds excellent produces an end-to-end number that is not. "A lot of times AI agents will have something like a 95% reliability. Seems pretty good on paper, but the problem is this is reduced to a 36% reliability for the entire system if we are running 20 steps because the errors compound" [0:21:29]. Cole also names it from the agent-building side: "beware what I like to call the hallucination explosion or another word for this is uh compounding non-determinism" [0:12:00], with the same math at smaller scale - "if you have three agents that each individually work well 95% of the time... that means that your whole system is only actually going to work 86% of the time" [0:12:36].

The consequence is a hard ceiling on autonomy. Longer chains demand implausible per-step reliability: "if we were to have a harness that can truly do something completely end to end... then we would need like 99.9% reliability for this system, especially if it's like 200 steps instead of 20" [0:22:18]. No current model or harness is there, which is why fully hands-off end-to-end agents keep disappointing while short, checked loops keep working.

There are only three levers, and they all fall out of the formula. Shrink the exponent by shortening the chain, collapsing agents, and moving steps into deterministic code that succeeds by construction. Raise the base with validation, guardrails, and self-correction so a bad step is caught and retried rather than propagated. Or reset the product periodically by putting a human at a checkpoint. This is the quantitative case behind nearly every reliability practice in this knowledge base.

## Prerequisites

- [What Is an AI Agent](./what-is-an-ai-agent.md) - what a "step" is, and why each one is probabilistic.

## Contrasts with

- [Deterministic Workflows](./deterministic-workflows.md) - hard-coding a step removes it from the product entirely.
- [Agents vs. Workflows](./agents-vs-workflows.md) - the choice between many probabilistic hops and a fixed path.

## Related

- [Single vs. Multi-Agent Architecture](./single-vs-multi-agent.md) - every extra agent is another factor in the multiplication.
- [Human in the Loop](./human-in-the-loop.md) - a checkpoint that stops errors propagating downstream.
- [Guardrails](./guardrails.md), [Validation](./validation.md), [End-to-End Validation](./end-to-end-validation.md) - raising the per-step success rate.
- [Self-Correcting Agents](./self-correction.md) and [Adversarial Agents](./adversarial-agents.md) - catching a bad step before it compounds.
- [The Five Levels of AI Coding Autonomy](./five-levels-of-ai-coding-autonomy.md) - why the fully autonomous level stays out of reach.
- [AI Coding Harness](./ai-coding-harness.md), [Long-Running Agents](./long-running-agents.md), [The Ralph Loop](./the-ralph-loop.md) - the long chains where this bites hardest.
- [Granular Task Management](./granular-task-management.md) and [One Feature Per Prompt](./one-feature-per-prompt.md) - shortening the chain per run.
- [Agent Evaluation](./agent-evaluation.md) and [Hallucination Detection](./hallucination-detection.md) - measuring the per-step rate you are exponentiating.

## Sources

- [Are Agent Harnesses Bringing Back Vibe Coding?](../sources/are-agent-harnesses-bringing-back-vibe-coding.md) - "[0:21:29] a lot of times AI agents will have something like a 95% reliability. Seems pretty good on paper, but the problem is this is reduced to a 36% reliability for the entire system if we are running 20 steps because the errors compound."
- [Are Agent Harnesses Bringing Back Vibe Coding?](../sources/are-agent-harnesses-bringing-back-vibe-coding.md) - "[0:22:18] if we were to have a harness that can truly do something completely end to end... then we would need like 99.9% reliability for this system, especially if it's like 200 steps instead of 20."
- [My Top 20 Lessons from Building 100s of AI Agents (Super Actionable)](../sources/my-top-20-lessons-from-building-100s-of-ai-agents-super-actionable.md) - "[0:12:00] beware what I like to call the hallucination explosion or another word for this is uh compounding non-determinism."
- [My Top 20 Lessons from Building 100s of AI Agents (Super Actionable)](../sources/my-top-20-lessons-from-building-100s-of-ai-agents-super-actionable.md) - "[0:12:36] if you have three agents that each individually work well 95% of the time... that means that your whole system is only actually going to work 86% of the time."
