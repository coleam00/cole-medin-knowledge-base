---
type: concept
title: "Subagents Pattern"
description: "Delegating scoped tasks to isolated subagents to parallelize work and protect the main agent's context window."
tags: [subagents, delegation, context, ai-coding, anti-pattern]
videos: [this-completely-changes-the-way-we-build-production-ai-agents-vercel-eve, google-just-dropped-a-masterclass-on-agentic-engineering-its-so-good, anthropic-just-dropped-a-masterclass-on-building-agent-harnesses-for-large-codebases, full-guide-to-becoming-a-principled-agentic-engineer-build-anything-with-ai, parallel-claude-code-git-worktrees-this-setup-will-change-how-you-ship, everything-you-thought-about-building-ai-agents-is-wrong, youre-hardly-using-what-claude-code-has-to-offer-its-insane, the-subagent-era-is-officially-here-learn-this-now, ive-used-claude-code-for-2000-hours-heres-how-i-build-anything-with-it, this-one-command-makes-coding-agents-find-all-their-mistakes-use-it-now, my-complete-agentic-coding-workflow-to-build-anything-no-fluff-or-overengineering, how-to-properly-use-claude-code-agent-teams-full-live-build, claude-codes-agent-teams-are-insane-multiple-ai-agents-coding-together-in-real-time, turn-claude-code-into-your-full-engineering-team-with-subagents, learn-90-of-building-ai-agents-in-30-minutes, the-true-power-of-ai-coding-build-your-own-workflows-full-guide, i-built-my-claude-code-subagents-dream-team-to-create-any-ai-agent, my-top-20-lessons-from-building-100s-of-ai-agents-super-actionable, archon-beta-launch-livestream-what-you-missed, introducing-archon-the-revolutionary-operating-system-for-ai-coding, a-complete-guide-to-claude-code-here-are-all-the-best-strategies, build-any-ai-agent-with-this-context-engineering-blueprint, give-me-28-minutes-and-ill-completely-change-the-way-you-build-ai-agents, build-an-army-of-ai-agents-on-autopilot-with-archon-heres-how, 10x-your-ai-agents-with-this-one-agent-architecture, introducing-archon-an-ai-agent-that-builds-ai-agents, coding-subagents-the-next-evolution-of-ai-ides]
created: 2026-07-21
updated: 2026-07-21
---

# Subagents Pattern

A subagent is a subprocess agent that a primary agent spins up to go do a bounded job in its own context window and report back only a summary. "Sub agents is basically a way for you to spin up a subprocess, another agent that runs under the hood to go and look at a bunch of things... and then report back a summary" [0:46:40]. The whole reason the pattern exists is context economy: the subagent can burn enormous context internally while the main agent pays almost nothing. "We've already used over a 100,000 tokens here, but we only have a few thousand tokens that are returned back to our main agent" [0:47:31].

## How it works

The primary agent holds the ability to call any of its subagents and is the one that prompts them; each subagent carries its own specialized system prompt, a restricted tool set, and works autonomously on the delegated task [0:26:08], [0:26:37]. Crucially there is **no coordination between subagents**: "the primary idea with sub agents is context isolation. We want some way to be able to dish out a request that could take tens or even hundreds of thousands of tokens, but all we need back is a summary" [0:10:23], and "there's no coordination at all. These sub agents work completely in isolation, which does make them very token efficient because they're honed in on a single task" [0:11:28]. A main agent spawns them, they work, they report back, and that is the extent of the interaction [0:02:09].

Two benefits compound: isolation and speed, because subagents can run in parallel [0:13:22]. Cole cites Anthropic research of a "90.2%... improvement... using sub agents to load in context upfront for our research instead of having our main agent taking care of everything" [0:12:17]. Mechanically, subagents are "really just prompts" you point the coder at, which is why the pattern ports to any assistant, even ones without native subagent support [0:15:20].

## The research-not-implementation rule

Cole's sharpest guidance is where **not** to use them: "my word of warning is do not try to use sub agents for implementation. It doesn't work. I only use it for research" [0:06:49]. The reason is that implementation needs the full context of what was done to stay coherent, whereas research and validation are exactly the isolatable, summarize-and-return jobs subagents excel at [0:14:02]. He uses them for research upfront and a validator specialist, but "on purpose did not use any sub agents during the implementation" [0:22:46].

> **Contradiction:** Some videos frame subagents as coding specialists that "handle different parts of our development workflow" (I Built My Claude Code Subagents DREAM TEAM, 2026 [0:00:29]), while others insist implementation via subagents "doesn't work" and reserve them for research and validation (The Subagent Era Is Officially Here [0:06:49]; The True Power of AI Coding [0:22:46]). The reconciling read is that subagents shine for parallel research/planning/validation, and delegating implementation to them remains contested.

## Contrasts with

- [Single vs. Multi-Agent Architecture](./single-vs-multi-agent.md) - the industry moved away from complex networks of coordinating specialists toward one driving agent that delegates to isolated subagents: "keep it simple. You really only need one agent to drive most of your agentic engineering" [0:17:40].

## Builds on

- [Context Isolation](./context-isolation.md) - the core mechanism: each subagent's own context window keeps heavy work out of the primary conversation.
- [Context Engineering](./context-engineering.md) - subagents are a context-management tactic, returning summaries instead of raw exploration.

## Related

- [Agent Teams](./agent-teams.md) - subagents with no inter-agent coordination contrast with team setups where agents work together.
- [Parallel Agent Execution](./parallel-agent-execution.md) - subagents are the unit most often fanned out to run concurrently.
- [Parallel Agentic Coding](./parallel-agentic-coding.md) - spinning up specialized subagents to check that an implementation is ideal.
- [Model Selection](./model-selection.md) - assigning a specific model per subagent to manage cost and tokens.
- [Validation](./validation.md) - a validator subagent with a tight system prompt is a favored use.
- [Code Review](./code-review.md) - running review as isolated subagents that find mistakes in parallel.
- [Planning with AI](./planning-with-ai.md) - subagents are used heavily for research and PRD/planning passes.
- [Agentic Coding](./agentic-coding.md) - subagents are a staple of Cole's coding workflow.
- [AI Coding Harness](./ai-coding-harness.md) - harnesses for large codebases split exploration from editing via subagents.
- [Agent Graphs](./agent-graphs.md) - an alternative structure for wiring specialized agents together.
- [The Agent Loop (Reason-Act-Observe)](./agent-loop.md) - each subagent runs its own loop before returning.

## Tools

- [Claude Code](../entities/tools/claude-code.md) - provides native subagents (research only, no built-in implementation agents) plus per-subagent hooks and rules.
- [Archon](../entities/tools/archon.md) - treats subagents as role-based prompts that hand off to one another, usable even in assistants without native subagent support.

## Sources

- [FULL Guide to Becoming a Principled Agentic Engineer (Build Anything with AI)](../sources/full-guide-to-becoming-a-principled-agentic-engineer-build-anything-with-ai.md) - "[0:46:40] sub agents is basically a way for you to spin up a subprocess, another agent that runs under the hood to go and look at a bunch of things... and then report back a summary"
- [Claude Code's Agent Teams Are Insane - Multiple AI Agents Coding Together in Real Time](../sources/claude-codes-agent-teams-are-insane-multiple-ai-agents-coding-together-in-real-time.md) - "[0:10:23] the primary idea with sub agents is context isolation. We want some way to be able to dish out a request that could take tens or even hundreds of thousands of tokens, but all we need back is a summary."
- [The Subagent Era Is Officially Here - Learn this Now](../sources/the-subagent-era-is-officially-here-learn-this-now.md) - "[0:06:49] My word of warning is do not try to use sub agents for implementation. It doesn't work. I only use it for research"
- [Anthropic Just Dropped a Masterclass on Building Agent Harnesses (for Large Codebases)](../sources/anthropic-just-dropped-a-masterclass-on-building-agent-harnesses-for-large-codebases.md) - "[0:22:12] We send in a task and it runs with its own context window. It does all the analysis it needs to and then it returns a summary back to our primary cloud code session."
- [I've Used Claude Code for 2,000+ Hours - Here's How I Build Anything With It](../sources/ive-used-claude-code-for-2000-hours-heres-how-i-build-anything-with-it.md) - "[0:12:17] we have a 90.2% ... improvement according to some enthropic research using sub agents to load in context upfront for our research instead of having our main agent taking care of everything."
- [Google Just Dropped a Masterclass on Agentic Engineering (It's SO Good)](../sources/google-just-dropped-a-masterclass-on-agentic-engineering-its-so-good.md) - "[0:17:40] keep it simple. You really only need one agent to drive most of your agentic engineering."
- [A Complete Guide to Claude Code - Here are ALL the Best Strategies](../sources/a-complete-guide-to-claude-code-here-are-all-the-best-strategies.md) - "[0:26:37] sub agents are very powerful because they each have a specialized system prompt. We can limit the tools that they have access to and they work autonomously on delegated tasks."
- [I Built My Claude Code Subagents DREAM TEAM to Create Any AI Agent](../sources/i-built-my-claude-code-subagents-dream-team-to-create-any-ai-agent.md) - "[0:00:29] With sub agents, we get specialized agentic coders to handle different parts of our development workflow."
- [The True Power of AI Coding - Build Your OWN Workflows (Full Guide)](../sources/the-true-power-of-ai-coding-build-your-own-workflows-full-guide.md) - "[0:22:46] for the validation that's when we go back to using sub aents. So planning and validation we use sub aents but I on purpose did not use any sub aents during the implementation."
- [10x Your AI Agents with this ONE Agent Architecture](../sources/10x-your-ai-agents-with-this-one-agent-architecture.md) - "[0:00:36] fragmenting your AI agent into different sub agents to handle different components is one of the best ways to solve for this and take your AI agents to that next level"
- [Introducing Archon - The Revolutionary Operating System for AI Coding](../sources/introducing-archon-the-revolutionary-operating-system-for-ai-coding.md) - "[0:26:22] with sub agents, being able to define them as roles and what they do and how they hand off to each one of another and those interactions is the context that you need, not necessarily the technology on the back end."
- [Turn Claude Code into your Full Engineering Team with Subagents](../sources/turn-claude-code-into-your-full-engineering-team-with-subagents.md) - "[0:09:51] Remember, we're using sub aents for context isolation. So we're not bloating the main context window for our primary orchestrator here."
- [Build an ARMY of AI Agents on Autopilot with Archon, Here's How](../sources/build-an-army-of-ai-agents-on-autopilot-with-archon-heres-how.md) - "[0:12:38] so now it only has to worry about which agent to call on not which specific tool so instead of having to pick from 30 different tools it only has to pick from six different agents"
- [My Top 20 Lessons from Building 100s of AI Agents (Super Actionable)](../sources/my-top-20-lessons-from-building-100s-of-ai-agents-super-actionable.md) - "[0:20:58] this primary orchestrator that has to figure out which specialized agent to use, it very rarely picks the wrong one, especially if the roles for each of these agents are very distinct."
- [Build ANY AI Agent with this Context Engineering Blueprint](../sources/build-any-ai-agent-with-this-context-engineering-blueprint.md) - "[0:14:45] I'm just building a padantic AI agent that has another agent as a tool because we're going to have our primary research agent and then an email draft agent as a sub aent."
- [This Completely Changes the Way We Build Production AI Agents (Vercel Eve)](../sources/this-completely-changes-the-way-we-build-production-ai-agents-vercel-eve.md) - "[0:10:00] We have a subagent, an investigator... we want to dispatch that to a worker."
- [How to Properly Use Claude Code Agent Teams (FULL LIVE BUILD)](../sources/how-to-properly-use-claude-code-agent-teams-full-live-build.md) - "[0:02:09] we have our main agent that spawns sub aents. they do some work... they report back to the main agent, but there's no coordination."
- [Parallel Claude Code + Git Worktrees: This Setup Will Change How You Ship](../sources/parallel-claude-code-git-worktrees-this-setup-will-change-how-you-ship.md) - "[0:22:36] use this model for this sub agent to do this thing. So I highly recommend doing that a lot to manage the tokens"
- [You're Hardly Using What Claude Code Has to Offer, it's Insane](../sources/youre-hardly-using-what-claude-code-has-to-offer-its-insane.md) - "[0:07:27] now we can do it at a granular level for individual sub aents because different agents need different rules that we're adding in through hooks."
- [This One Command Makes Coding Agents Find All Their Mistakes (Use it Now)](../sources/this-one-command-makes-coding-agents-find-all-their-mistakes-use-it-now.md) - "[0:04:50] the cool part about this is we have three sub agents that run in parallel. This is built directly into the workflow."
- [My COMPLETE Agentic Coding Workflow to Build Anything (No Fluff or Overengineering)](../sources/my-complete-agentic-coding-workflow-to-build-anything-no-fluff-or-overengineering.md) - "[0:09:48] claude code doesn't have any built-in agents for implementation it's just for research"
- [Learn 90% of Building AI Agents in 30 Minutes](../sources/learn-90-of-building-ai-agents-in-30-minutes.md) - "[0:13:41] When you have a system that starts to have more than 10 tools, that is generally when you start to split into specialized sub aents and you have routing between them"
- [Everything You Thought About Building AI Agents is Wrong](../sources/everything-you-thought-about-building-ai-agents-is-wrong.md) - "[0:07:15] the convenience of having all these tools and support for things like sub agents and skills and the prompting that's already there for you"
- [Give Me 28 Minutes and I'll Completely Change the Way You Build AI Agents](../sources/give-me-28-minutes-and-ill-completely-change-the-way-you-build-ai-agents.md) - "[0:24:17] You just have to have bunch of these agents strung together, or you can use agents as tools, like sub agents."
- [Introducing Archon - an AI Agent that BUILDS AI Agents](../sources/introducing-archon-an-ai-agent-that-builds-ai-agents.md) - "[0:11:07] I want to take the primary coding agent... and split it up into sub agents that specialize in different parts of the code generation"
- [Archon Beta Launch Livestream - What You Missed!](../sources/archon-beta-launch-livestream-what-you-missed.md) - "[0:15:20] sub agents, even in cloud code, it's really just prompts. Like you have some file that you tell cloud code to look at and you say read the instructions here to act as this persona."
- [Coding Subagents - The Next Evolution of AI IDEs](../sources/coding-subagents-the-next-evolution-of-ai-ides.md) - "[0:01:41] imagine having specialized agents that are created specifically to code with a certain tool or framework and these agents can be called upon by the general AI coders like wind surf or cursor when necessary"
