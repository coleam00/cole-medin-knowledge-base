---
type: entity
subtype: organization
title: "StrongDM"
description: "Company that went viral for running a dark factory shipping thousands of lines of production code no human writes or reviews; source of the hold-out pattern Cole adopts for reliability."
resource: "https://www.strongdm.com"
tags: [organization, dark-factory, ai-coding-harness, reliability]
videos: [im-building-an-ai-dark-factory-that-ships-its-own-code-public-experiment, the-best-ai-coding-setup-isnt-the-most-autonomous-one-heres-why]
created: 2026-07-21
updated: 2026-07-21
---

# StrongDM

StrongDM is the company Cole points to as living proof that a [Dark Factory](../../concepts/dark-factory.md) is real and running in production, not a thought experiment: "StrongDM is a company that went pretty viral a couple of months ago because they are implementing a dark factory to ship thousands of lines of production code that they never write or review" ([0:07:53]). That "never write or review" is the defining claim, and it is why StrongDM anchors his coverage of the far end of [the evolution of AI coding](../../concepts/the-evolution-of-ai-coding.md), where the human sets up the system rather than touching the code.

Crucially, Cole reads StrongDM not as evidence for pure autonomy but for disciplined [Agentic Workflow Engineering](../../concepts/agentic-workflow-engineering.md). The specific technique he takes from them is the hold-out pattern: "I want to follow the hold out pattern from StrongDM. This is one of the most important things for reliability here" ([0:21:32]). Holding out a portion of work as a check on the rest is how a dark factory stays trustworthy, a form of [Validation](../../concepts/validation.md) baked into the process instead of a [Human in the Loop](../../concepts/human-in-the-loop.md) reviewing every diff.

StrongDM sits beside [Stripe](./stripe.md) as one of the "companies starting to come out of the woodworks sharing how they do have a dark factory that's actually running" ([0:08:30]). Where Stripe demonstrates harness-driven scale with heavy human oversight, StrongDM is Cole's reference for pushing autonomy further while keeping reliability through deterministic patterns like the hold-out. It is a direct influence on his own public dark-factory experiment.

## Realizes

- [Dark Factory](../../concepts/dark-factory.md) - A self-evolving codebase where autonomous workflows build and improve a product with minimal human touch.
- [Agentic Workflow Engineering](../../concepts/agentic-workflow-engineering.md) - Designing repeatable AI workflows as engineered systems with defined steps, orchestration, and background execution rather than ad-hoc prompting.

## Related

- [The Evolution of AI Coding](../../concepts/the-evolution-of-ai-coding.md) - How AI coding assistants moved from novelty to daily driver, and where the landscape, adoption, and commentary are heading.
- [Validation](../../concepts/validation.md) - Building explicit checks into agentic workflows so the AI verifies its own output against real success criteria before moving on.
- [Deterministic Workflows](../../concepts/deterministic-workflows.md) - Encoding known steps as fixed code paths and reserving the LLM for the genuinely fuzzy decisions, trading autonomy for reliability.
- [AI Coding Harness](../../concepts/ai-coding-harness.md) - The surrounding scaffolding (prompts, tools, rules, validation) that turns a raw model into a reliable coding system.
- [Human in the Loop](../../concepts/human-in-the-loop.md) - Keeping a human as the approver and steerer of agentic work rather than fully automating, so AI augments engineers instead of replacing them.
- [Stripe](./stripe.md) - Payments company that is Cole's headline example of an AI coding harness at scale (1,300 AI-generated PRs per week via Stripe Minions); also the external payments API agents integrate and call.

## Sources

- [I'm Building an AI Dark Factory That Ships Its Own Code (Public Experiment)](../../sources/im-building-an-ai-dark-factory-that-ships-its-own-code-public-experiment.md) - "[0:07:53] StrongDM is a company that went pretty viral a couple of months ago because they are implementing a dark factory to ship thousands of lines of production code that they never write or review."
- [I'm Building an AI Dark Factory That Ships Its Own Code (Public Experiment)](../../sources/im-building-an-ai-dark-factory-that-ships-its-own-code-public-experiment.md) - "[0:21:32] I want to follow the hold out pattern from StrongDM. This is one of the most important things for reliability here."
- [The Best AI Coding Setup Isn't the Most Autonomous One (Here's Why)](../../sources/the-best-ai-coding-setup-isnt-the-most-autonomous-one-heres-why.md) - "[0:08:30] there are some companies that are starting to come out of the woodworks sharing how they do have a dark factory that's actually running. StrongDM is one example."
