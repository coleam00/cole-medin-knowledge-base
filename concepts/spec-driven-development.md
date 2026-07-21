---
type: concept
title: "Spec-Driven Development"
description: "Anchoring the build to an explicit written spec that the agent implements and validates against."
tags: [spec, planning, contract]
videos: [the-best-ai-coding-setup-isnt-the-most-autonomous-one-heres-why, google-just-dropped-a-masterclass-on-agentic-engineering-its-so-good]
created: 2026-07-21
updated: 2026-07-21
---

# Spec-Driven Development

Spec-driven development anchors a build to an explicit written specification that the agent implements against, with human direction concentrated up front and human validation at the end. In the most autonomous setups "we're letting the agent rip through larger sets of work based on something like an epic, a PRD, or a spec," where the human role narrows to bookends: "here we're just doing the very high level direction setting up front and then the validation at the very end like a set of pull requests." The spec is the interface between human intent and autonomous execution, dense enough that the agent can run a large batch of work without constant steering.

Because the agent leans so heavily on the spec, the quality of that spec becomes the limiting factor for the whole build. Cole endorses the framing that "the specification quality is the new bottleneck. And that is so true because there's so much that still has to be human-driven with the validation at the end and the requirement gathering up front." This is what separates disciplined agentic engineering from ad hoc prompting: "when you get to agentic engineering, this is where you really have a repeatable process and you have specifications that are actually engineered just like the code." A spec is not a loose wish list; it is a treated as an engineered artifact, versioned and refined with the same rigor as the implementation it drives.

The practical trade is control for throughput. Handing off larger units of work against a spec is faster, but it moves the human effort earlier (requirement gathering) and later (validation) rather than eliminating it. This is the concept realized in autonomous harnesses and self-evolving pipelines, where a strong spec plus end-to-end validation is what makes hands-off execution trustworthy.

## Builds on

- [Planning with AI](./planning-with-ai.md) - the planning conversation is how a strong spec is produced.

## Related

- [PRD-First Development](./prd-first-development.md) - the PRD is the concrete spec artifact this discipline runs on.
- [Validation](./validation.md) and [End-to-End Validation](./end-to-end-validation.md) - the back-end human/automated check the spec is measured against.
- [Agentic Coding](./agentic-coding.md) - spec-driven work is the disciplined end of the agentic-coding spectrum.
- [Dark Factory](./dark-factory.md) - fully autonomous execution that depends on spec quality.
- [The Evolution of AI Coding](./the-evolution-of-ai-coding.md) - spec-driven development as the current stage of that arc.

## Sources

- [The Best AI Coding Setup Isn't the Most Autonomous One (Here's Why)](../sources/the-best-ai-coding-setup-isnt-the-most-autonomous-one-heres-why.md) - "[0:05:07] we're letting the agent rip through larger sets of work based on something like an epic, a PRD, or a spec."
- [The Best AI Coding Setup Isn't the Most Autonomous One (Here's Why)](../sources/the-best-ai-coding-setup-isnt-the-most-autonomous-one-heres-why.md) - "[0:05:24] here we're just doing the very high level direction setting up front and then the validation at the very end like a set of pull requests"
- [Google Just Dropped a Masterclass on Agentic Engineering (It's SO Good)](../sources/google-just-dropped-a-masterclass-on-agentic-engineering-its-so-good.md) - "[0:02:21] Now the specification quality is the new bottleneck. And that is so true because there's so much that still has to be human-driven with the validation at the end and the requirement gathering up front."
- [Google Just Dropped a Masterclass on Agentic Engineering (It's SO Good)](../sources/google-just-dropped-a-masterclass-on-agentic-engineering-its-so-good.md) - "[0:05:38] when you get to aentic engineering, this is where you really have a repeatable process and you have specifications that are actually engineered just like the code."
