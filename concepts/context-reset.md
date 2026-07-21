---
type: concept
title: "Context Reset"
description: "Clearing or compacting an agent's context window between phases of work to avoid context rot and keep reasoning sharp."
tags: [context-reset, context-rot, context-engineering, agentic-coding]
videos: [my-complete-agentic-coding-workflow-to-build-anything-no-fluff-or-overengineering, the-5-techniques-separating-top-agentic-engineers-right-now, ive-used-claude-code-for-2000-hours-heres-how-i-build-anything-with-it, full-guide-to-becoming-a-principled-agentic-engineer-build-anything-with-ai, how-to-properly-use-claude-code-agent-teams-full-live-build, context-engineering-101-the-simple-strategy-to-100x-ai-coding, build-any-ai-agent-with-this-context-engineering-blueprint, archon-beta-launch-livestream-what-you-missed, are-agent-harnesses-bringing-back-vibe-coding, turn-claude-code-into-your-full-engineering-team-with-subagents, i-was-wrong-about-ralph-wiggum, this-one-command-makes-coding-agents-find-all-their-mistakes-use-it-now, code-100x-faster-with-ai-heres-how-no-hype-full-process, im-addicted-to-windsurf-send-help]
created: 2026-07-21
updated: 2026-07-21
---

# Context Reset

Context reset is clearing or compacting an agent's window between phases of work so the next phase starts sharp. The golden rule surfaces most concretely between planning and coding: "in between the planning and the implementation, I am going to be resetting the context. This is one of the golden rules. Context is very precious." The reset is safe precisely because the phase before it produced a durable artifact: "I can have a fresh conversation where the plan is the only thing I send in because it has all the documentation to reference. It has the entire task list."

Two motivations drive the reset. First, accumulated bias: a long planning session builds up commitments, so "we wanted to have a fresh set of eyes on the problem going into implementation," and you "always start a brand new context window whenever you are writing any code." Second, accumulated bloat: after heavy testing "the context window is going to be pretty bloated... So if there's anything more that I want to work with the agent to reason about, I want to do that in a new context window." The mechanic in Claude Code is literal: "I will literally do /clear. So completely wiping the context window. And then I call the execute command and the parameter for this command is that plan that I want it to read" (often paired with a [Prime Command](./prime-command.md) to re-orient the fresh session).

The pattern generalizes into loop-based harnesses, where a reset per iteration is what lets an agent run indefinitely without collapsing: "just one agent that we're running in a loop because we're clearing the context window periodically so it can handle a longer task and not run into context rot." Each reset is paired with a catch-up step: "we're just restarting the context window and having some kind of process for the next agent to quickly catch itself up to speed on where we're at." The requirement is strict enough that Cole rejects tools that skip it: "why we're not using anthropic plugin because it doesn't even reset the context window. like it's just a bad idea to use it."

## Prerequisites

- [Planning with AI](./planning-with-ai.md) - the reset only works because planning emits a self-contained plan to reload.
- [PRD-First Development](./prd-first-development.md) and [The Issue Is the Spec](./issue-is-the-spec.md) - the durable artifact that survives the wipe.

## Part of

- [Context Engineering](./context-engineering.md) - one of its golden rules for protecting the window.
- [The PIV Loop](./the-piv-loop.md) and [Phases of Work](./phases-of-work.md) - the reset lives at the seams between phases.

## Contrasts with

- [Context Isolation](./context-isolation.md) - isolation runs separate windows in parallel; reset clears one window across time.

## Related

- [Context Rot](./context-rot.md) - the degradation a periodic reset is designed to prevent.
- [Prime Command](./prime-command.md) - re-orients a freshly reset agent to the project.
- [Two-Layer Planning](./two-layer-planning.md), [Human in the Loop](./human-in-the-loop.md), [Memory Systems](./memory-systems.md) - practices around the reset boundary.
- [AI Coding Harness](./ai-coding-harness.md) - loops reset the window every iteration.

## Tools

- [Claude Code](../entities/tools/claude-code.md) - `/clear` wipes the window; `/compact` summarizes it.

## Sources

- [My COMPLETE Agentic Coding Workflow to Build Anything](../sources/my-complete-agentic-coding-workflow-to-build-anything-no-fluff-or-overengineering.md) - "[0:26:29] in between the planning and the implementation, I am going to be resetting the context. This is one of the golden rules. Context is very precious."
- [The 5 Techniques Separating Top Agentic Engineers Right Now](../sources/the-5-techniques-separating-top-agentic-engineers-right-now.md) - "[0:10:56] right here I will literally do /clear. So completely wiping the context window. And then I call the execute command and the parameter for this command is that plan that I want it to read."
- [I've Used Claude Code for 2,000+ Hours](../sources/ive-used-claude-code-for-2000-hours-heres-how-i-build-anything-with-it.md) - "[0:08:42] the second right strategy is to always start a brand new context window whenever you are writing any code."
- [FULL Guide to Becoming a Principled Agentic Engineer](../sources/full-guide-to-becoming-a-principled-agentic-engineer-build-anything-with-ai.md) - "[0:53:58] the coding agent has probably built up a lot of bias throughout this conversation... We wanted to have a fresh set of eyes on the problem going into implementation."
- [How to Properly Use Claude Code Agent Teams (FULL LIVE BUILD)](../sources/how-to-properly-use-claude-code-agent-teams-full-live-build.md) - "[0:27:39] after you create your plan, that's all the context your agent needs. You can now reset the context window and then go into the implementation."
- [Are Agent Harnesses Bringing Back Vibe Coding?](../sources/are-agent-harnesses-bringing-back-vibe-coding.md) - "[0:06:38] we're clearing the context window periodically so it can handle a longer task and not run into context rot."
- [This One Command Makes Coding Agents Find All Their Mistakes](../sources/this-one-command-makes-coding-agents-find-all-their-mistakes-use-it-now.md) - "[0:08:55] the context window is going to be pretty bloated with the coding agent going through all this testing... I want to do that in a new context window."
- [I Was Wrong About Ralph Wiggum](../sources/i-was-wrong-about-ralph-wiggum.md) - "[0:04:06] why we're not using anthropic plugin because it doesn't even reset the context window. like it's just a bad idea to use it."
- [Build ANY AI Agent with this Context Engineering Blueprint](../sources/build-any-ai-agent-with-this-context-engineering-blueprint.md) - "[0:21:02] clearing your conversation before you execute the PRP because you don't want to have all of the old context left over from when you were generating it."
- [Context Engineering 101](../sources/context-engineering-101-the-simple-strategy-to-100x-ai-coding.md) - "[0:33:17] you want to clear the context so you're starting with a blank slate when you move on to executing the PRP."
- [Archon Beta Launch Livestream - What You Missed!](../sources/archon-beta-launch-livestream-what-you-missed.md) - "[0:26:00] what the founder of BMAD recommends doing is clearing the conversation entirely when we go on to the next agent."
- [Turn Claude Code into Your Full Engineering Team with Subagents](../sources/turn-claude-code-into-your-full-engineering-team-with-subagents.md) - "[0:11:52] Every single time the agent runs, we're running in a fresh context window."
- [Code 100x Faster with AI](../sources/code-100x-faster-with-ai-heres-how-no-hype-full-process.md) - "[0:03:10] You want to start fresh conversations often because longer conversations can really bog down an LLM."
- [I'm Addicted to Windsurf, Send Help](../sources/im-addicted-to-windsurf-send-help.md) - "[0:08:52] the best thing I found to do in these situations where it starts to hallucinate is literally just... start a brand new conversation."
