---
type: concept
title: "Prime Command"
description: "A reusable slash command that primes an agent with focused codebase understanding at the start of a session."
tags: [prime-command, slash-commands, context-engineering, claude-code]
videos: [full-guide-to-becoming-a-principled-agentic-engineer-build-anything-with-ai, the-subagent-era-is-officially-here-learn-this-now, ive-used-claude-code-for-2000-hours-heres-how-i-build-anything-with-it, my-complete-agentic-coding-workflow-to-build-anything-no-fluff-or-overengineering, how-to-properly-use-claude-code-agent-teams-full-live-build, the-5-techniques-separating-top-agentic-engineers-right-now, are-agent-harnesses-bringing-back-vibe-coding, i-forced-claude-to-code-for-24-hours-nonstop-heres-what-happened, ai-fixes-my-code-better-than-me-now-heres-how, the-true-power-of-ai-coding-build-your-own-workflows-full-guide, a-complete-guide-to-claude-code-here-are-all-the-best-strategies]
created: 2026-07-21
updated: 2026-07-21
---

# Prime Command

A prime command is a reusable slash command whose only job is to walk a coding agent through understanding a codebase at the start of a fresh session. As Cole puts it, "this prime command quite simply its job is to walk a coding agent through understanding the codebase. We want to know what we already have to help us think about what comes next" [0:41:39]. It is the very first move in nearly every one of his workflows: "I will run a prime command at the start of every single new conversation when I want to build something new" [0:08:43].

The core problem it solves is that every new conversation drops a blank context window into an existing project. Cole frames the agent like a new hire with amnesia: "We have to imagine a software project where each new engineer arrives with no memory. And so how do we quickly fill that memory but also in a really concise way with the information it needs" [0:09:42]. The prime command answers that by scripting a guided exploration rather than dumping files. A typical prime runs `tree`, reads the `CLAUDE.md` and README, checks recent git commits, and reads the PRD: "it'll start by using the tree command... And then it'll read the claw.md and the readme. So we're priming our context here" [0:13:24]. Cole leans on git history as durable memory: "we're going to check recent git commits. I love using git as long-term memory for my coding agents" [0:42:14].

Priming is deliberately load-bearing before planning: "sometimes we need our agent to do exploration of our live codebase... That's what the prime command does is we are exploring our codebase at the start of our planning process" [0:17:52]. It is not one fixed command either. Cole keeps several, scoped to different parts of a codebase: "I have many different prime commands because there are different parts of the codebase I want the agent to understand depending on what I want to build" [0:18:22]. Once primed, the agent can read the PRD and answer the only question that matters next: what should we build?

## Part of

- [The PIV Loop](./the-piv-loop.md) - priming is the opening step that gives the agent a mental model before the plan-implement-validate cycle begins.

## Builds on

- [Slash Commands](./slash-commands.md) - a prime is implemented as a reusable slash command.
- [Commandify Everything](./commandify-everything.md) - priming is a prime example of turning a repeated manual process into a saved command.

## Prerequisites

- [Context Reset](./context-reset.md) - priming exists precisely because each new conversation starts from a clean context window.
- [Git as Long-Term Memory](./git-as-long-term-memory.md) - recent commits are a key source the prime reads to reconstruct project state.

## Related

- [Agentic Search](./agentic-search.md) - a prime drives the agent to explore the live codebase rather than rely on a static index.
- [Planning with AI](./planning-with-ai.md) - priming is the exploration phase that feeds a good plan.
- [PRD-First Development](./prd-first-development.md) - the PRD is a core file the prime reads so the agent can decide what to build next.
- [Context Isolation](./context-isolation.md) - a lightweight prime keeps the main agent's context focused before subagents fan out.
- [Subagents Pattern](./subagents-pattern.md) - Cole primes the main agent first, before any subagents are dispatched.
- [AI Coding Harness](./ai-coding-harness.md) - priming is how a harness fills a fresh agent's memory concisely.

## Tools

- [Claude Code](../entities/tools/claude-code.md) - Cole's primary driver for prime commands, invoked as `/prime` at the start of each session.

## Sources

- [FULL Guide to Becoming a Principled Agentic Engineer](../sources/full-guide-to-becoming-a-principled-agentic-engineer-build-anything-with-ai.md) - "[0:41:39] this prime command quite simply its job is to walk a coding agent through understanding the codebase. We want to know what we already have to help us think about what comes next."
- [FULL Guide to Becoming a Principled Agentic Engineer](../sources/full-guide-to-becoming-a-principled-agentic-engineer-build-anything-with-ai.md) - "[0:42:14] we're going to check recent git commits. I love using git as long-term memory for my coding agents."
- [The Subagent Era Is Officially Here](../sources/the-subagent-era-is-officially-here-learn-this-now.md) - "[0:09:39] whenever I am starting a brand new AI coding session to knock out a feature or a bug fix, I always start with my prime command. So no sub agents yet. I want to load a high-level overview of the project into the context of my main coding agent."
- [I've Used Claude Code for 2,000+ Hours](../sources/ive-used-claude-code-for-2000-hours-heres-how-i-build-anything-with-it.md) - "[0:18:22] I have many different prime commands because there are different parts of the codebase I want the agent to understand depending on what I want to build."
- [My COMPLETE Agentic Coding Workflow to Build Anything](../sources/my-complete-agentic-coding-workflow-to-build-anything-no-fluff-or-overengineering.md) - "[0:20:37] At the start of every new conversation with an AI coding assistant, we need it to catch itself up to speed on the codebase. What are we building? What comes next? That is where the prime command comes in."
- [How to Properly Use Claude Code Agent Teams](../sources/how-to-properly-use-claude-code-agent-teams-full-live-build.md) - "[0:08:43] I will run a prime command at the start of every single new conversation when I want to build something new."
- [The 5 Techniques Separating Top Agentic Engineers Right Now](../sources/the-5-techniques-separating-top-agentic-engineers-right-now.md) - "[0:03:52] the PRD is one of the core files that I always make sure my agent reads because then after it primes itself on the codebase, I can just simply ask based on the PRD, what should we build next?"
- [Are Agent Harnesses Bringing Back Vibe Coding?](../sources/are-agent-harnesses-bringing-back-vibe-coding.md) - "[0:09:42] We have to imagine a software project where each new engineer arrives with no memory. And so how do we quickly fill that memory but also in a really concise way with the information it needs."
- [I Forced Claude to Code for 24 Hours NONSTOP](../sources/i-forced-claude-to-code-for-24-hours-nonstop-heres-what-happened.md) - "[0:06:04] So it gets its bearings. I often call this priming. It's going to understand what we already have, including reading the feature list to figure out what to build next."
- [AI Fixes My Code Better than Me Now?!](../sources/ai-fixes-my-code-better-than-me-now-heres-how.md) - "[0:11:05] I invoke my prime command so that it understands the codebase and it reads the read me so there we go it gets the project analysis"
- [The True Power of AI Coding - Build Your OWN Workflows](../sources/the-true-power-of-ai-coding-build-your-own-workflows-full-guide.md) - "[0:10:44] what the primer does is it lists out instructions for files to read to quickly catch the AI coding assistant up to speed on our project when we're starting a new conversation."
- [A Complete Guide to Claude Code](../sources/a-complete-guide-to-claude-code-here-are-all-the-best-strategies.md) - "[0:13:24] So it'll start by using the tree command ... And then it'll read the claw.md and the readme. So we're priming our context here."
