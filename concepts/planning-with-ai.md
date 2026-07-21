---
type: concept
title: "Planning with AI"
description: "Using the AI to produce a detailed plan before implementation so execution follows a reviewed blueprint instead of improvising."
tags: [planning, prd, design]
videos: [the-best-ai-coding-setup-isnt-the-most-autonomous-one-heres-why, googles-agents-cli-the-cli-skills-combination-to-ship-ai-agents-easily, claude-plans-gemini-designs-the-workflow-to-build-beautiful-frontends, full-guide-to-becoming-a-principled-agentic-engineer-build-anything-with-ai, coding-agent-reliability-explodes-when-they-argue-new-adversarial-dev-technique, ive-used-claude-code-for-2000-hours-heres-how-i-build-anything-with-it, is-software-engineering-finally-dead, how-to-properly-use-claude-code-agent-teams-full-live-build, claude-codes-agent-teams-are-insane-multiple-ai-agents-coding-together-in-real-time, i-was-wrong-about-ralph-wiggum, ralph-wiggum-is-the-final-evolution-of-vibe-coding-heres-what-comes-next, ai-fixes-my-code-better-than-me-now-heres-how, the-official-archon-guide-10x-your-ai-coding-workflow, the-true-power-of-ai-coding-build-your-own-workflows-full-guide, i-built-my-claude-code-subagents-dream-team-to-create-any-ai-agent, my-top-20-lessons-from-building-100s-of-ai-agents-super-actionable, archon-beta-launch-livestream-what-you-missed, introducing-archon-the-revolutionary-operating-system-for-ai-coding, build-any-ai-agent-with-this-context-engineering-blueprint, context-engineering-101-the-simple-strategy-to-100x-ai-coding, context-engineering-is-the-new-vibe-coding-learn-this-now, introducing-rag-20-agentic-rag-knowledge-graphs-free-template, the-3-must-have-mcp-servers-for-any-ai-coding-and-how-to-use-them, i-built-the-ultimate-rag-mcp-server-for-ai-coding-better-than-context7, code-100x-faster-with-ai-heres-how-no-hype-full-process, boltdiy-the-future-of-open-source-ai-coding-whats-next, this-boltnew-fork-is-exploding-dont-miss-out-on-whats-happening]
created: 2026-07-21
updated: 2026-07-21
---

# Planning with AI

Planning with AI is the practice of using the coding agent itself to produce a detailed, reviewed plan before any implementation begins, so execution follows a blueprint instead of improvising. The workflow is a clean split: "when I am creating code with an AI coding assistant, I always split things up between planning and implementation." The plan is not a throwaway to-do list; it is "a structured plan that has things like my validation strategy and the task list that I have for the agent," carried into a fresh session as its only context: "I have one conversation to plan with the coding agent. I'll create some kind of markdown that has my structured plan and then I will send that in as the only context to a new session going into the implementation."

Planning matters because a plan is the highest-leverage artifact in the whole build: "Your plan is very high leverage, right? Like one error in your plan can lead to hundreds of lines of bad code. But one line of bad code is just one line of bad code." Cole is explicit that "the planning process is just as important as the actual implementation if not more," and that skimping costs you later, "if you spend five hours planning your agent, that could end up saving you 20 hours of development down the line." This inverts a common instinct. His own view evolved: he "was one of those people that thought that large language models were great for helping you plan your development. But why in the world would you trust them for implementing," before concluding the plan is where AI adds the most value.

The process starts unstructured and converges to structure. "I start really unstructured at first. I just give a big brain dump of what I wanted to look into," then "we're having the conversation with the coding agent to establish things, having it grill us with questions, to remove assumptions, and then we create that final plan that we then send into implementation." Only "once we feel confident that we're on the same page with the coding agent then we'll run a command that'll create a structured markdown document for our plan." Research feeds the plan, "it's subagents for research, feed that into a plan, and then send that plan into an agent team", and the human stays the decider: "I keep myself in the driver's seat by still having it make recommendations to me but in the end I'm the final one to say yes this is our tech stack." Critically, planning does not mean surrendering control, since "we can't just vibe code and skip right to implementation."

## Builds on

- [Clarifying Questions](./clarifying-questions.md) - the agent grills you to remove assumptions before the plan is written.
- [Reduce Assumptions](./reduce-assumptions.md) - the goal that shapes the planning conversation.
- [Context Engineering](./context-engineering.md) - planning is how you generate the context ecosystem the build runs on.

## Part of

- [The PIV Loop](./the-piv-loop.md) - planning is the P that opens every plan-implement-validate cycle.
- [Two-Layer Planning](./two-layer-planning.md) - the higher-level structure that separates PRD-level planning from per-feature planning.

## Contrasts with

- [Vibe Coding](./vibe-coding.md) - skipping straight to implementation without a reviewed plan.

## Related

- [Vibe Planning](./vibe-planning.md) - the deliberately unstructured first stage of planning: free-form exploration of ideas, architecture, and tech stack with the coding assistant as a research companion, before any structure or requirements doc is imposed.
- [PRD-First Development](./prd-first-development.md) and [Spec-Driven Development](./spec-driven-development.md) - the artifacts a planning session produces.
- [Phases of Work](./phases-of-work.md) - the plan is sharded into ordered, buildable phases.
- [Global Rules](./global-rules.md) - static guidance loaded alongside the plan.
- [Context Reset](./context-reset.md) - the finished plan becomes the only context for a fresh implementation session.
- [Agent Teams](./agent-teams.md) - research subagents feed a plan that an agent team then implements.
- [AI Coding Harness](./ai-coding-harness.md) - harnesses "do not work well if you don't have very clearly defined goals."
- [Greenfield vs. Brownfield Projects](./greenfield-vs-brownfield.md) - The branch point in AI-assisted planning between building a brand-new project, where the agent grounds itself in external documentation research, and working in an existing codebase, where it must reference the repo's existing patterns instead.

## Tools

- [Archon](../entities/tools/archon.md) - splits planning from implementation, turning a research brief into a PRD sharded into tasks.

## Sources

- [The Best AI Coding Setup Isn't the Most Autonomous One (Here's Why)](../sources/the-best-ai-coding-setup-isnt-the-most-autonomous-one-heres-why.md) - "[0:14:24] We're having the conversation with the coding agent to establish things, having it grill us with questions, to remove assumptions, and then we create that final plan that we then send into implementation."
- [I've Used Claude Code for 2,000+ Hours - Here's How I Build Anything With It](../sources/ive-used-claude-code-for-2000-hours-heres-how-i-build-anything-with-it.md) - "[0:08:42] my workflow is always I have one conversation to plan with the coding agent. I'll create some kind of markdown that has my structured plan and then I will send that in as the only context to a new session going into the implementation."
- [How to Properly Use Claude Code Agent Teams (FULL LIVE BUILD)](../sources/how-to-properly-use-claude-code-agent-teams-full-live-build.md) - "[0:28:15] Your plan is very high leverage, right? Like one error in your plan can lead to hundreds of lines of bad code. But one line of bad code is just one line of bad code."
- [How to Properly Use Claude Code Agent Teams (FULL LIVE BUILD)](../sources/how-to-properly-use-claude-code-agent-teams-full-live-build.md) - "[0:06:31] the planning process is just as important as the actual implementation if not more."
- [FULL Guide to Becoming a Principled Agentic Engineer (Build Anything with AI)](../sources/full-guide-to-becoming-a-principled-agentic-engineer-build-anything-with-ai.md) - "[0:40:16] just like creating our PRD, when we are creating the actual implementation, we start very unstructured. We're just going to have a conversation with our coding agent figuring out how should we go about solving this problem"
- [FULL Guide to Becoming a Principled Agentic Engineer (Build Anything with AI)](../sources/full-guide-to-becoming-a-principled-agentic-engineer-build-anything-with-ai.md) - "[0:48:53] once we feel confident that we're on the same page with the coding agent then we'll run a command that'll create a structured markdown document for our plan"
- [My Top 20 Lessons from Building 100s of AI Agents (Super Actionable)](../sources/my-top-20-lessons-from-building-100s-of-ai-agents-super-actionable.md) - "[0:11:09] if you spend five hours planning your agent, that could end up saving you 20 hours of development down the line."
- [AI Fixes My Code Better than Me Now?! (Here's How)](../sources/ai-fixes-my-code-better-than-me-now-heres-how.md) - "[0:00:00] I was one of those people that thought that large language models were great for helping you plan your development. But why in the world would you trust them for implementing and validating?"
- [I Was Wrong About Ralph Wiggum](../sources/i-was-wrong-about-ralph-wiggum.md) - "[0:11:55] I keep myself in the driver's seat by still having it make recommendations to me but in the end I'm the final one to say yes this is our tech stack"
- [Claude Code's Agent Teams Are Insane](../sources/claude-codes-agent-teams-are-insane-multiple-ai-agents-coding-together-in-real-time.md) - "[0:14:05] it's subagents for research, feed that into a plan, and then send that plan into an agent team."
- [The OFFICIAL Archon Guide - 10x Your AI Coding Workflow](../sources/the-official-archon-guide-10x-your-ai-coding-workflow.md) - "[0:17:23] when I am creating code with an AI coding assistant, I always split things up between planning and implementation."
- [How to Properly Use Claude Code Agent Teams (FULL LIVE BUILD)](../sources/how-to-properly-use-claude-code-agent-teams-full-live-build.md) - "[0:10:41] that's what I do with my planning is I start really struct unstructured at first. I just give a big brain dump of what I wanted to look into."
- [Build ANY AI Agent with this Context Engineering Blueprint](../sources/build-any-ai-agent-with-this-context-engineering-blueprint.md) - "[0:01:20] We can't just vibe code and skip right to implementation."
- [Ralph Wiggum is the Final Evolution of Vibe Coding (Here's What Comes Next)](../sources/ralph-wiggum-is-the-final-evolution-of-vibe-coding-heres-what-comes-next.md) - "[0:14:13] it assumes that you have a good prompt. And that, my friend, is a terrible assumption because creating a good structured plan is probably the most difficult part for working with coding agents in the first place."
