---
type: concept
title: "The Issue Is the Spec"
description: "Treating a well-written ticket or issue as the complete specification the agent implements against."
tags: [spec, issues, tickets, agentic-coding, workflow]
videos: [full-guide-to-becoming-a-principled-agentic-engineer-build-anything-with-ai, parallel-claude-code-git-worktrees-this-setup-will-change-how-you-ship, im-building-an-ai-dark-factory-that-ships-its-own-code-public-experiment, turn-claude-code-into-your-full-engineering-team-with-subagents, github-is-the-future-of-ai-coding-heres-why, a-complete-guide-to-claude-code-here-are-all-the-best-strategies]
created: 2026-07-21
updated: 2026-07-21
---

# The Issue Is the Spec

"The issue is the spec" is the principle that a well-written ticket is the complete specification the agent builds against, and the entry point to the whole development process. Cole states it as a pillar: "pillar number one is that issue is the spec. Pretty much all of my agentic coding... my input into any implementation is always a GitHub issue." The issue is not a loose note; it is the durable artifact that carries intent into implementation: "the input into our development process just is this issue... my input to writing the code is always some artifact."

Making the issue the spec gives the pipeline a clean, inspectable interface between stages. Cole maps the flow: "the issue is input into the implementation and then the pull request is going to be the input into the validation." Because the artifact lives in the issue tracker rather than a local scratch file, it is queryable, versioned, and shared across every agent: with Linear as the source of truth, "when each agent runs, it's going to start by reading the linear project." That makes remote and parallel agents possible, since each one bootstraps its context from the same canonical issue.

In practice, work begins by triaging issues against a higher-level goal, "whenever we... triage our issues, like figure out from all these issues which ones do we want to address, the mission.md is going to really give the guidance there," then handing a chosen issue to an agent. The trigger can be as light as an @-mention: "we open up a GitHub issue. This could be a bug or even a feature that we want it to build. And then we @cloudfix mention it," and the agent runs end to end, "It found the issue after reading it from GitHub, implemented the fix, tested everything, made a new branch, pushed it, and created a pull request all from a single slash command." The quality of the build is bounded by the quality of the issue, which is why clarification and context belong in it up front.

## Builds on

- [PRD-First Development](./prd-first-development.md) and [Spec-Driven Development](./spec-driven-development.md) - the issue is the concrete, per-task form of a written spec.
- [Clarifying Questions](./clarifying-questions.md) - questions answered up front are what make the issue a complete spec.

## Part of

- [The PIV Loop](./the-piv-loop.md) - the issue is the input that opens Plan, Implement, Validate.
- [Phases of Work](./phases-of-work.md) - a large spec is split into issue-sized phases.

## Related

- [Agentic Coding](./agentic-coding.md) - the issue is the standard entry point for delegating a build.
- [Deterministic Workflows](./deterministic-workflows.md) - the issue is the fixed input a workflow triages and implements against.
- [Global Rules](./global-rules.md) - persistent rules complement the per-task issue.
- [Context Reset](./context-reset.md) - the issue lets a fresh session rebuild full context from the tracker.
- [Separate Reviewer](./separate-reviewer.md) - the pull request produced from the issue becomes the reviewer's input.
- [Slash Commands](./slash-commands.md) - a single command turns an issue into an implemented pull request.

## Tools

- [GitHub](../entities/tools/github.md) - issues (and the pull requests they produce) are the canonical artifacts.
- [Linear](../entities/tools/linear.md) - an issue tracker used as the shared source of truth across agents.
- [Claude Code](../entities/tools/claude-code.md) - reads an issue and drives it to a pull request.
- [Stripe Minions](../entities/tools/stripe-minions.md) - Stripe's internal agent harness that runs 'blueprints' interweaving agent nodes with deterministic code steps, shipping 1,300+ fully AI-written PRs every week.

## Sources

- [Parallel Claude Code + Git Worktrees](../sources/parallel-claude-code-git-worktrees-this-setup-will-change-how-you-ship.md) - "[0:03:06] pillar number one is that issue is the spec... my input into any implementation is always a GitHub issue."
- [FULL Guide to Becoming a Principled Agentic Engineer](../sources/full-guide-to-becoming-a-principled-agentic-engineer-build-anything-with-ai.md) - "[0:38:03] the input into our development process just is this issue... my input to writing the code is always some artifact."
- [Parallel Claude Code + Git Worktrees](../sources/parallel-claude-code-git-worktrees-this-setup-will-change-how-you-ship.md) - "[0:08:40] the issue is input into the implementation and then the pull request is going to be the input into the validation."
- [I'm Building an AI Dark Factory That Ships Its Own Code](../sources/im-building-an-ai-dark-factory-that-ships-its-own-code-public-experiment.md) - "[0:17:16] the entry point to anything that we're going to work on in the factory is a GitHub issue."
- [Turn Claude Code into Your Full Engineering Team with Subagents](../sources/turn-claude-code-into-your-full-engineering-team-with-subagents.md) - "[0:13:10] Linear is our source of truth instead of these local files. And so now when each agent runs, it's going to start by reading the linear project."
- [GitHub is the Future of AI Coding (Here's Why)](../sources/github-is-the-future-of-ai-coding-heres-why.md) - "[0:05:40] we open up a GitHub issue. This could be a bug or even a feature that we want it to build. And then we @cloudfix mention it."
- [A Complete Guide to Claude Code](../sources/a-complete-guide-to-claude-code-here-are-all-the-best-strategies.md) - "[0:36:03] It found the issue after reading it from GitHub, implemented the fix, tested everything, made a new branch, pushed it, and created a pull request all from a single slash command."
