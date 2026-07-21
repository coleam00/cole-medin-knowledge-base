---
type: concept
title: "The PIV Loop"
description: "Cole's core agentic-coding cycle of Plan, Implement, Validate that structures every unit of AI-driven work."
tags: [piv, planning, validation]
videos: [the-best-ai-coding-setup-isnt-the-most-autonomous-one-heres-why, finally-an-open-standard-for-the-karpathy-llm-wiki-is-here, google-just-dropped-a-masterclass-on-agentic-engineering-its-so-good, harness-engineering-what-separates-top-agentic-engineers-right-now, full-guide-to-becoming-a-principled-agentic-engineer-build-anything-with-ai, parallel-claude-code-git-worktrees-this-setup-will-change-how-you-ship, pi-coding-agent-archon-build-any-ai-coding-workflow-no-claude-code-bloat, the-next-evolution-of-ai-coding-is-harnesses-heres-how-to-build-them, stripes-coding-agents-ship-1300-prs-every-week-heres-how-they-do-it, is-software-engineering-finally-dead, this-one-command-makes-coding-agents-find-all-their-mistakes-use-it-now, my-complete-agentic-coding-workflow-to-build-anything-no-fluff-or-overengineering, the-way-we-use-ai-will-completely-change-in-2026-hot-takes, ai-fixes-my-code-better-than-me-now-heres-how, the-true-power-of-ai-coding-build-your-own-workflows-full-guide, a-complete-guide-to-claude-code-here-are-all-the-best-strategies]
created: 2026-07-21
updated: 2026-07-21
---

# The PIV Loop

The PIV loop is Cole's core methodology for AI coding: a repeatable three-step cycle of Plan, Implement, Validate that you run for every unit of work. As he frames it, "the PIV loop, for example, this is the primary mental model that I always teach for AI coding. Very important to have a process for yourself to plan, implement, and validate whatever you're creating with a coding agent." It is deliberately codebase-agnostic and unit-agnostic: "This is how I build any new feature or fix any bug in any codebase," and the unit is usually a single ticket, "we're going to go through the piv loop, the process that we're going to repeat for every single Jira ticket... it could be a GitHub issue, it could be a Linear ticket."

The loop's power comes from what it sandwiches. The human owns the two ends and delegates the middle: "we delegate all the coding to the agent and trust it... because we're sandwiching the implementation with a lot of planning and a lot of validation that we are very much a part of." Planning produces a concrete artifact before any code is written, "for my planning I create a structured markdown document that outlines everything that we need to build and the entire validation strategy before we go into implementation." That plan is then the handoff into a fresh implementation session, and validation gates close the loop because "whenever we do a piv loop, it is very very far from guaranteed that the implementation will be perfect. Coding agents are not perfect. They are non-deterministic by nature." Cole often prepends a research or priming step ("the R piv loop"), so the full arc becomes research, plan, implement, validate.

## Part of

- [Agentic Workflow Engineering](./agentic-workflow-engineering.md) - the discipline of designing loops like PIV as reusable harness steps.
- [Agentic Coding](./agentic-coding.md) - PIV is the process that makes delegating the code to an agent reliable.

## Implemented by

- [Planning with AI](./planning-with-ai.md) and [Two-Layer Planning](./two-layer-planning.md) - the "P" step, producing a structured plan document.
- [Prime Command](./prime-command.md) - the research/priming pass that fronts the loop.
- [Validation](./validation.md) and [End-to-End Validation](./end-to-end-validation.md) - the "V" step and its quality gates.
- [Context Isolation](./context-isolation.md) - each stage runs in a separate, token-efficient session with the plan as the handoff.

## Contrasts with

- [Vibe Coding](./vibe-coding.md) - PIV's opposite: prompting without structured planning or validation. "This is not vibe coding."

## Related

- [Human in the Loop](./human-in-the-loop.md) - the human owns the planning and validation ends of the sandwich.
- [Context Engineering](./context-engineering.md) - the plan is the curated context fed into implementation.
- [AI Coding Harness](./ai-coding-harness.md) - PIV encoded as skills/commands you can rerun.
- [System Evolution](./system-evolution.md) - the loop is refined over time into your own system.

## Tools

- [Claude Code](../entities/tools/claude-code.md) - Cole's primary driver for running each PIV stage in its own session.
- [Archon](../entities/tools/archon.md) - packages PIV as a workflow across the plan/implement/validate stages.
- [Pi](../entities/tools/pi-coding-agent.md) - a lightweight agent used to run the same loop without Claude Code bloat.

## Sources

- [The Best AI Coding Setup Isn't the Most Autonomous One (Here's Why)](../sources/the-best-ai-coding-setup-isnt-the-most-autonomous-one-heres-why.md) - "[0:13:34] it's going to converge into the exact same process that I call the R piv loop. This is how I build any new feature or fix any bug in any codebase."
- [Finally, an Open Standard for the Karpathy LLM Wiki is HERE](../sources/finally-an-open-standard-for-the-karpathy-llm-wiki-is-here.md) - "[0:14:48] The PIV loop, for example, this is the primary mental model that I always teach for AI coding. Very important to have a process for yourself to plan, implement, and validate whatever you're creating with a coding agent."
- [FULL Guide to Becoming a Principled Agentic Engineer](../sources/full-guide-to-becoming-a-principled-agentic-engineer-build-anything-with-ai.md) - "[0:02:03] then I'm going to pick one of those and we're going to go through the piv loop, the process that we're going to repeat for every single Jira ticket."
- [My COMPLETE Agentic Coding Workflow to Build Anything](../sources/my-complete-agentic-coding-workflow-to-build-anything-no-fluff-or-overengineering.md) - "[0:23:12] PIV is short for plan, implement, validate. We take focused work, usually a phase from a PRD, and we run it through this entire process."
- [Harness Engineering: What Separates Top Agentic Engineers Right Now](../sources/harness-engineering-what-separates-top-agentic-engineers-right-now.md) - "[0:10:30] You want to do your planning, implementation, and validation all in separate coding agent sessions to keep each one of them token efficient and focused."
- [Stripe's Coding Agents Ship 1,300 PRs EVERY Week](../sources/stripes-coding-agents-ship-1300-prs-every-week-heres-how-they-do-it.md) - "[0:15:24] That'll output a single structured plan... I'm going to cut off the context window. So brand new context window. Feed this plan into a second agent to do the implementation."
- [This One Command Makes Coding Agents Find All Their Mistakes](../sources/this-one-command-makes-coding-agents-find-all-their-mistakes-use-it-now.md) - "[0:17:14] for my planning I create a structured markdown document that outlines everything that we need to build and the entire validation strategy before we go into implementation."
- [Is Software Engineering Finally Dead?](../sources/is-software-engineering-finally-dead.md) - "[0:06:37] I delegate all of my coding... to the AI coding assistants because I put myself in the driver seat for the planning and the validation at the end, sandwiching the implementation."
- [Pi Coding Agent + Archon: Build ANY AI Coding Workflow](../sources/pi-coding-agent-archon-build-any-ai-coding-workflow-no-claude-code-bloat.md) - "[0:13:19] the piv loop which is my core methodology for AI coding."
- [Google Just Dropped a Masterclass on Agentic Engineering](../sources/google-just-dropped-a-masterclass-on-agentic-engineering-its-so-good.md) - "[0:11:30] we plan with the agent, we have it build, and then we have our quality gates at the end for testing and evaling with an iterative loop here for the agent to improve its output autonomously."
- [FULL Guide to Becoming a Principled Agentic Engineer](../sources/full-guide-to-becoming-a-principled-agentic-engineer-build-anything-with-ai.md) - "[0:57:19] whenever we do a piv loop, it is very very far from guaranteed that the implementation will be perfect. Coding agents are not perfect. They are non-deterministic by nature."
- [Parallel Claude Code + Git Worktrees](../sources/parallel-claude-code-git-worktrees-this-setup-will-change-how-you-ship.md) - "[0:04:53] we're going to go through the stages of planning, building, and validating, but each one of the coding agents working with their own local copy of the codebase."
- [The Next Evolution of AI Coding Is Harnesses](../sources/the-next-evolution-of-ai-coding-is-harnesses-heres-how-to-build-them.md) - "[0:01:42] So we want to plan, implement tasks in a loop, run the tests, have it do a review, even adding in a human approval gate... and then ending with a pull request."
- [AI Fixes My Code Better than Me Now?!](../sources/ai-fixes-my-code-better-than-me-now-heres-how.md) - "[0:11:32] it's going through this entire piv loop of priming then planning then executing this entire process that now I don't have to test myself."
- [The Way We Use AI Will Completely Change in 2026 (Hot Takes)](../sources/the-way-we-use-ai-will-completely-change-in-2026-hot-takes.md) - "[0:05:24] We define our objectives and the system that our agents will operate under. And then we orchestrate by delegating the coding to our agents. And then we validate the outputs."
- [The True Power of AI Coding - Build Your OWN Workflows](../sources/the-true-power-of-ai-coding-build-your-own-workflows-full-guide.md) - "[0:01:18] the primary mental model that guides most of my coding is the three-step process of planning, then implementing and then validating."
- [A Complete Guide to Claude Code](../sources/a-complete-guide-to-claude-code-here-are-all-the-best-strategies.md) - "[0:23:04] Then we get into validation loops aka validation gates ... telling the AI coding assistant how it can validate itself to make sure that its output is good."
