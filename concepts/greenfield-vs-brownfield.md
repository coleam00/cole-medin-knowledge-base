---
type: concept
title: "Greenfield vs. Brownfield Projects"
description: "The branch point in AI-assisted planning between building a brand-new project, where the agent grounds itself in external documentation research, and working in an existing codebase, where it must reference the repo's existing patterns instead."
tags: [planning, bmad-method]
videos: [archon-beta-launch-livestream-what-you-missed]
created: 2026-07-21
updated: 2026-07-21
---

# Greenfield vs. Brownfield Projects

Greenfield and brownfield are the two starting conditions for any AI-assisted build, and they demand different planning workflows. Cole draws the line plainly: "a green field project, you can think of it like fresh green pastures... brownfield is when you're working in an existing codebase. And the BMAD method has different workflows depending on if you're working on an existing codebase or not."

The distinction matters because it decides **where the agent's ground truth comes from**. On a greenfield build there is no repo to imitate, so the planning phase is external research: "With a new project, it's let's look at the documentation for pideantic for example to figure out the patterns." On a brownfield build the repo itself is the authority, and the planning phase is internal reconnaissance: "brownfield projects, it's more let's reference the existing codebase to figure out the patterns." Feed a brownfield agent library docs instead of the codebase and it will write technically correct code that fights the conventions already there; feed a greenfield agent a codebase-scan prompt and it finds nothing to scan.

Practically, this is a branch you make explicit rather than hope the model infers. Serious planning frameworks encode it as two distinct entry paths, and the artifact each produces differs: a greenfield plan cites documentation and reference implementations, a brownfield plan cites files, modules, and the existing naming and error-handling conventions it intends to extend. Brownfield also carries a regression surface that greenfield does not, so its plans lean harder on reading before writing and on validating that nothing already working broke.

## Prerequisites

- [Planning with AI](./planning-with-ai.md) - the branch is chosen at the top of the planning phase, before any code.
- [Agentic Coding](./agentic-coding.md) - both modes assume an agent doing the implementation.

## Part of

- [Spec-Driven Development](./spec-driven-development.md) - the spec's research section is what greenfield and brownfield fill differently.
- [Two-Layer Planning](./two-layer-planning.md) - the high-level layer picks the mode; the detailed layer inherits its research strategy.

## Contrasts with

- [Vibe Coding](./vibe-coding.md) - skipping the branch entirely and letting the model guess at patterns is exactly what produces off-convention code.

## Tools

- [BMAD Method](../entities/tools/bmad-method.md) - ships separate greenfield and brownfield workflows, the clearest implementation of the split.
- [Archon](../entities/tools/archon.md) - workflows are pointed at a repo, so brownfield reconnaissance is the default posture.
- [Context7](../entities/tools/context7.md) - supplies the up-to-date library documentation a greenfield plan researches.

## Related

- [Codebase Indexing](./codebase-indexing.md) and [Agentic Search](./agentic-search.md) - how a brownfield agent actually finds the patterns it must match.
- [Prime Command](./prime-command.md) - a repeatable brownfield orientation pass at the start of a session.
- [Docs and Templates as Coding-Assistant Context](./docs-as-agent-context.md) and [llms.txt](./llms-txt.md) - the greenfield equivalent: pulling framework docs into context.
- [Global Rules](./global-rules.md) - encodes the conventions a brownfield agent would otherwise have to rediscover every session.
- [PRD-First Development](./prd-first-development.md) and [PRP Framework](./prp-framework.md) - the plan artifacts whose research sections this branch determines.
- [Reduce Assumptions](./reduce-assumptions.md) - researching real patterns instead of guessing is the point of the branch.
- [Prototype as a Coding Blueprint](./prototype-as-blueprint.md) - one way a greenfield build converts into a brownfield one.

## Sources

- [Archon Beta Launch Livestream - What You Missed!](../sources/archon-beta-launch-livestream-what-you-missed.md) - "[0:11:00] a green field project, you can think of it like fresh green pastures... brownfield is when you're working in an existing codebase. And the BMAD method has different workflows depending on if you're working on an existing codebase or not."
- [Archon Beta Launch Livestream - What You Missed!](../sources/archon-beta-launch-livestream-what-you-missed.md) - "[0:11:30] brownfield projects, it's more let's reference the existing codebase to figure out the patterns... With a new project, it's let's look at the documentation for pideantic for example to figure out the patterns"
