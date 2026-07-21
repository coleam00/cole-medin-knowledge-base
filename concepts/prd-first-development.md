---
type: concept
title: "PRD-First Development"
description: "Starting every build from a written product requirements document that becomes the contract the agent implements against."
tags: [prd, spec, planning]
videos: [full-guide-to-becoming-a-principled-agentic-engineer-build-anything-with-ai, i-built-self-evolving-claude-code-memory-w-karpathys-llm-knowledge-bases, full-guide-build-your-own-ai-second-brain-with-claude-code, my-complete-agentic-coding-workflow-to-build-anything-no-fluff-or-overengineering, turn-claude-code-into-your-full-engineering-team-with-subagents, i-was-wrong-about-ralph-wiggum, ralph-wiggum-is-the-final-evolution-of-vibe-coding-heres-what-comes-next, the-5-techniques-separating-top-agentic-engineers-right-now, are-agent-harnesses-bringing-back-vibe-coding, i-forced-claude-to-code-for-24-hours-nonstop-heres-what-happened, the-official-archon-guide-10x-your-ai-coding-workflow, claude-sonnet-45-the-new-coding-king-sonnet-45-vs-gpt-5-codex, the-true-power-of-ai-coding-build-your-own-workflows-full-guide, archon-beta-launch-livestream-what-you-missed, introducing-archon-the-revolutionary-operating-system-for-ai-coding, build-any-ai-agent-with-this-context-engineering-blueprint, context-engineering-101-the-simple-strategy-to-100x-ai-coding, context-engineering-is-the-new-vibe-coding-learn-this-now, pydantic-ai-deepseek-v3-the-best-ai-agent-combo]
created: 2026-07-21
updated: 2026-07-21
---

# PRD-First Development

PRD-first development starts every build from a written product requirements document that becomes the single source of truth the agent implements against. Cole defines it plainly: "PRD is short for product requirement document... in this context it is a markdown document, a single place to define the entire scope of work for your project." It is "the initial scope of work that we have to create the minimum viable product for our application," and once written it is durable in a way the conversation is not: "The PRD is the only thing that's going to survive. So we need to make sure that the entire conversation that we have with our agent is really put in here."

The PRD is produced by moving from exploration to structure: "the first command is a process guiding the coding agent from an unstructured conversation into a structured PRD... we go from exploration to structure," where "the input is the conversation. The output is a single document, a source of truth that we could check into source control." That single document then drives decomposition: "you use the PRD as a way to split your project into more granular features like implementing the API, implementing the user interface, building the authentication," and in Archon you "shard the PRD into tasks, no more than 20 tasks." For brownfield work it shifts emphasis: "it's more documenting what you already have in your project and then what you want to build next."

The same artifact reappears under many names across the ecosystem. In autonomous harnesses it is the appspec: "Everything starts with the app spec text file. I typically call this a PRD. It's basically the scope of work for what you want to build for your MVP," and it is "the single source of truth for what we are building here with Ralph Wiggum." A close cousin is the PRP, or product requirements prompt, "a process for creating a structured plan of attack for a feature implementation with your coding agent before you send the task off," which unlike a PRD is "actually creating a prompt that we're going to run with cloud code" rather than an architecture document. Cole notes these approaches are complementary, not competing: PRD-first "is not a replacement for these different strategies like the PRP framework or spec-driven development or the BMAD method. It's actually congruent with those things."

## Builds on

- [Planning with AI](./planning-with-ai.md) - the PRD is the structured output of a planning conversation.
- [Context Engineering](./context-engineering.md) - the PRD is the primary context artifact fed into a build.

## Part of

- [Spec-Driven Development](./spec-driven-development.md) - PRD-first is the spec-first discipline applied as a product document.
- [Two-Layer Planning](./two-layer-planning.md) - the PRD is the higher layer, sharded into per-feature plans.

## Related

- [Phases of Work](./phases-of-work.md) - the PRD is sharded into ordered, buildable phases and tasks.
- [The PRP Framework](./prp-framework.md) and [Issue Is the Spec](./issue-is-the-spec.md) - sibling ways to encode the scope of work as a contract.
- [Prime Command](./prime-command.md) and [Slash Commands](./slash-commands.md) - commands that generate and consume the PRD.
- [AI Coding Harness](./ai-coding-harness.md) - harnesses treat the appspec/PRD as their single source of truth.
- [Validation](./validation.md) - the PRD defines the success criteria the build is checked against.
- [Agent Graphs](./agent-graphs.md) and [Agentic Coding](./agentic-coding.md) - downstream consumers of the requirements document.

## Tools

- [Archon](../entities/tools/archon.md) - turns a research brief into a PRD, then shards it into no more than 20 tasks.

## Sources

- [The 5 Techniques Separating Top Agentic Engineers Right Now](../sources/the-5-techniques-separating-top-agentic-engineers-right-now.md) - "[0:00:47] PRD is short for product requirement document... in this context it is a markdown document a single place to define the entire scope of work for your project."
- [FULL Guide to Becoming a Principled Agentic Engineer (Build Anything with AI)](../sources/full-guide-to-becoming-a-principled-agentic-engineer-build-anything-with-ai.md) - "[0:12:30] the first command is a process guiding the coding agent from an unstructured conversation into a structured PRD. Like I said, we go from exploration to structure"
- [FULL Guide to Becoming a Principled Agentic Engineer (Build Anything with AI)](../sources/full-guide-to-becoming-a-principled-agentic-engineer-build-anything-with-ai.md) - "[0:19:44] The input is the conversation. The output is a single document, a source of truth that we could... check into source control"
- [My COMPLETE Agentic Coding Workflow to Build Anything (No Fluff or Overengineering)](../sources/my-complete-agentic-coding-workflow-to-build-anything-no-fluff-or-overengineering.md) - "[0:14:31] The PRD is the only thing that's going to survive. So we need to make sure that the entire conversation that we have with our agent is really put in here."
- [I Forced Claude to Code for 24 Hours NONSTOP, Here's What Happened](../sources/i-forced-claude-to-code-for-24-hours-nonstop-heres-what-happened.md) - "[0:03:41] Everything starts with the app spec text file. I typically call this a PRD. It's basically the scope of work for what you want to build for your MVP."
- [I Was Wrong About Ralph Wiggum](../sources/i-was-wrong-about-ralph-wiggum.md) - "[0:13:44] This is the single source of truth for what we are building here with Ralph Wiggum"
- [Ralph Wiggum is the Final Evolution of Vibe Coding (Here's What Comes Next)](../sources/ralph-wiggum-is-the-final-evolution-of-vibe-coding-heres-what-comes-next.md) - "[0:13:46] PRP or the product requirement prompt is a process for creating a structured plan of attack for a feature implementation with your coding agent before you send the task off and have it knock everything out."
- [Context Engineering is the New Vibe Coding (Learn this Now)](../sources/context-engineering-is-the-new-vibe-coding-learn-this-now.md) - "[0:13:18] We're not creating like an architecture document. We're actually creating a prompt that we're going to run with Claude Code."
- [Introducing Archon - The Revolutionary Operating System for AI Coding](../sources/introducing-archon-the-revolutionary-operating-system-for-ai-coding.md) - "[0:21:10] it's not a replacement for these different strategies like the PRP framework or spec-driven development or the BMAD method. It's actually congruent with those things"
- [The 5 Techniques Separating Top Agentic Engineers Right Now](../sources/the-5-techniques-separating-top-agentic-engineers-right-now.md) - "[0:01:41] for brownfield development, if you are working on an existing codebase... it's more documenting what you already have in your project and then what you want to build next"
- [Archon Beta Launch Livestream - What You Missed!](../sources/archon-beta-launch-livestream-what-you-missed.md) - "[0:31:00] shard the PRD into tasks uh no more than 20 tasks and put those in the tasks for the archon project"
- [Full Guide - Build Your Own AI Second Brain with Claude Code](../sources/full-guide-build-your-own-ai-second-brain-with-claude-code.md) - "[0:19:29] I have this requirements document that you can fill out, and then you can feed this in as context to your coding agent to create the PRD. This is your initial scope of work"
