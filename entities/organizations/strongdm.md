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

StrongDM is the company Cole points to as living proof that a [Dark Factory](../../concepts/dark-factory.md) is real and running in production, not a thought experiment: "Strongdm is a company that went pretty viral a couple of months ago because they are implementing a dark factory to ship thousands of lines of production code that they never write or review" ([0:07:53]). That "never write or review" is the defining claim, and it is why StrongDM anchors his coverage of the far end of [the evolution of AI coding](../../concepts/the-evolution-of-ai-coding.md), where the human sets up the system rather than touching the code.

Crucially, Cole reads StrongDM not as evidence for pure autonomy but for disciplined [Agentic Workflow Engineering](../../concepts/agentic-workflow-engineering.md). The specific technique he takes from them is the hold-out pattern: "I want to follow the hold out pattern from strong DM. This is one of the most important things for reliability here" ([0:21:32]). Holding out a portion of work as a check on the rest is how a dark factory stays trustworthy, a form of [Validation](../../concepts/validation.md) baked into the process instead of a [Human in the Loop](../../concepts/human-in-the-loop.md) reviewing every diff.

StrongDM sits beside [Stripe](./stripe.md) as one of the "companies starting to come out of the woodworks sharing how they do have a dark factory that's actually running" ([0:08:30]). Where Stripe demonstrates harness-driven scale with heavy human oversight, StrongDM is Cole's reference for pushing autonomy further while keeping reliability through deterministic patterns like the hold-out. It is a direct influence on his own public dark-factory experiment.

## Related

- [Dark Factory](../../concepts/dark-factory.md) and [The Evolution of AI Coding](../../concepts/the-evolution-of-ai-coding.md) - StrongDM is Cole's proof a running dark factory exists.
- [Validation](../../concepts/validation.md) and [Deterministic Workflows](../../concepts/deterministic-workflows.md) - the hold-out pattern is how StrongDM keeps unreviewed code reliable.
- [AI Coding Harness](../../concepts/ai-coding-harness.md), [Agentic Workflow Engineering](../../concepts/agentic-workflow-engineering.md), and [Human in the Loop](../../concepts/human-in-the-loop.md) - the process discipline behind the autonomy.
- [Stripe](./stripe.md) - the other company cited for coming out of the woodworks with a real dark factory.

## Sources

- [I'm Building an AI Dark Factory That Ships Its Own Code (Public Experiment)](../../sources/im-building-an-ai-dark-factory-that-ships-its-own-code-public-experiment.md) - "[0:07:53] Strongdm is a company that went pretty viral a couple of months ago because they are implementing a dark factory to ship thousands of lines of production code that they never write or review."
- [I'm Building an AI Dark Factory That Ships Its Own Code (Public Experiment)](../../sources/im-building-an-ai-dark-factory-that-ships-its-own-code-public-experiment.md) - "[0:21:32] I want to follow the hold out pattern from strong DM. This is one of the most important things for reliability here."
- [The Best AI Coding Setup Isn't the Most Autonomous One (Here's Why)](../../sources/the-best-ai-coding-setup-isnt-the-most-autonomous-one-heres-why.md) - "[0:08:30] there are some companies that are starting to come out of the woodworks sharing how they do have a dark factory that's actually running. Strong DM is one example."
