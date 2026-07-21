---
type: entity
subtype: tool
title: "GitHub Spec Kit"
description: "GitHub's spec-driven development toolkit, providing slash commands for vibe planning, initial requirements, and plan creation, cited alongside PRP and BMAD as another expression of the same plan-implement-validate philosophy."
resource: "https://github.com/github/spec-kit"
tags: [ai-coding, coding-agent]
videos: [my-complete-agentic-coding-workflow-to-build-anything-no-fluff-or-overengineering, the-true-power-of-ai-coding-build-your-own-workflows-full-guide]
created: 2026-07-21
updated: 2026-07-21
---

# GitHub Spec Kit

GitHub Spec Kit is GitHub's toolkit for [Spec-Driven Development](../../concepts/spec-driven-development.md): a package of [slash commands](../../concepts/slash-commands.md) that walks a coding agent from free-form exploration through written requirements to an implementation plan. Cole treats it as a legitimate, well-built expression of the same idea his own workflow encodes - "a lot of other tools coming out like the GitHub spec kit is rather new, really cool, provides a lot of commands to help us do a very similar thing" ([0:09:30]) - and as proof that the industry has converged on planning before implementing.

## How Cole uses it / why it matters

Cole does not run Spec Kit as his daily driver, and he is explicit about why. His recommendation is a thin, hand-rolled command set you fully understand over a prebuilt framework: "That's why I recommend something like this over a more complex framework like BMAD or the GitHub spec kit. They're really, really powerful, but it's hard to really make it your own" ([0:03:28]). The objection is ownership, not quality. A framework that ships dozens of commands, agents, and templates becomes a system you inherit rather than one you shape, and the entire point of [Agentic Workflow Engineering](../../concepts/agentic-workflow-engineering.md) is that the workflow encodes *your* process. Spec Kit still earns its place in the map because its stages line up almost one-to-one with [The PIV Loop](../../concepts/the-piv-loop.md): open-ended [Vibe Planning](../../concepts/vibe-planning.md) first, then a requirements document, then a concrete plan the agent implements against. For anyone who wants the structure without building it, Spec Kit is the on-ramp; for anyone serious about the practice, it is a reference implementation to read and then [commandify](../../concepts/commandify-everything.md) in their own repo.

## Realizes

- [Spec-Driven Development](../../concepts/spec-driven-development.md) - Anchoring the build to an explicit written spec the agent implements and validates against.
- [Slash Commands](../../concepts/slash-commands.md) - Ships the workflow as callable command files rather than prose instructions.
- [Vibe Planning](../../concepts/vibe-planning.md) - Its first stage is deliberately unstructured exploration before any requirements doc exists.
- [PRD-First Development](../../concepts/prd-first-development.md) - Produces an initial requirements document that becomes the contract for implementation.

## Contrasts with

- [BMAD Method](./bmad-method.md) - The other heavyweight spec-driven framework Cole names in the same breath as too hard to make your own.
- [PRP Framework](../../concepts/prp-framework.md) - Rasmus's lighter context-rich prompt blueprint covering the same plan-to-one-pass ground.
- [Archon](./archon.md) - Cole's own harness builder, where you author the workflow yourself instead of adopting a framework's.

## Works with

- [Claude Code](./claude-code.md) - The coding agent the commands are installed into and executed by.
- [GitHub](./github.md) - The platform the toolkit ships from and whose issues and pull requests the spec flows into.
- [Git](./git.md) - Version control for the spec and plan documents that the workflow treats as durable artifacts.

## Related

- [The PIV Loop](../../concepts/the-piv-loop.md) - Plan, Implement, Validate, the cycle Spec Kit's stages map onto.
- [Planning with AI](../../concepts/planning-with-ai.md) - Producing a reviewed blueprint before implementation instead of improvising.
- [Commandify Everything](../../concepts/commandify-everything.md) - Turning repeated workflows into reusable commands, the practice Spec Kit productizes.
- [Agentic Workflow Engineering](../../concepts/agentic-workflow-engineering.md) - Designing AI workflows as engineered systems you own end to end.
- [Two-Layer Planning](../../concepts/two-layer-planning.md) - Splitting strategic planning from detailed task planning, mirrored by Spec Kit's staged commands.

## Sources

- [My COMPLETE Agentic Coding Workflow to Build Anything (No Fluff or Overengineering)](../../sources/my-complete-agentic-coding-workflow-to-build-anything-no-fluff-or-overengineering.md) - "[0:03:28] That's why I recommend something like this over a more complex framework like BMAD or the GitHub spec kit. They're really, really powerful, but it's hard to really make it your own."
- [The True Power of AI Coding - Build Your OWN Workflows (Full Guide)](../../sources/the-true-power-of-ai-coding-build-your-own-workflows-full-guide.md) - "[0:09:30] a lot of other tools coming out like the GitHub spec kit is rather new, really cool, provides a lot of commands to help us do a very similar thing"
