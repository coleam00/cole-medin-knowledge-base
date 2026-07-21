---
type: concept
title: "The Ralph Loop"
description: "Re-running an agent against the same prompt/state in a tight loop, letting each pass fix errors and compound reliability."
tags: [loop, ralph, reliability]
videos: [i-turned-claude-code-into-a-complete-video-generation-system-with-archon, the-creators-of-claude-code-and-openclaw-dont-prompt-their-agents-anymore, harness-engineering-what-separates-top-agentic-engineers-right-now, i-built-self-evolving-claude-code-memory-w-karpathys-llm-knowledge-bases, i-was-wrong-about-ralph-wiggum, are-agent-harnesses-bringing-back-vibe-coding, introducing-archon-an-ai-agent-that-builds-ai-agents, lets-settle-the-o3-mini-vs-r1-debate-for-coding-once-and-for-all]
created: 2026-07-21
updated: 2026-07-21
---

# The Ralph Loop

The Ralph loop (after the "Ralph Wiggum" technique) is the simplest possible agentic harness: run a coding agent against the same prompt and state over and over in a bash loop, letting each pass make more progress and fix the last pass's mistakes until the work is done. Cole reduces it to its essence: "this is the classic bash script because all Ralph is is just running Claude Code in a bash loop." The controlling insight, borrowed from the technique's origins, is that the human stops hand-prompting and instead engineers the loop itself: "I don't prompt Claude anymore. I write loops and the loops do the work. My job is to write loops." At that level, "the real skill is designing loops that prompt your agents so they work for you 24/7."

Mechanically, the loop needs a work source and an exit condition. You feed it a large scope of work and it self-decomposes: "You give it a larger scope of work, like a massive PRD, and it's going to be responsible for splitting that up into individual tasks and then running coding agent sessions to handle them one at a time until everything is done." The only clean way out is an agent-signaled completion token: "The only way that we can exit the main while loop here is if we have this done.ext text and the coding agent is confident that the implementation is done and all the validation is there." The pattern generalizes past code, "they're both just Ralph loops just for content creation instead of AI coding."

Why loop at all? Because reliability compounds against you. "A lot of times AI agents will have something like a 95% reliability. Seems pretty good on paper, but the problem is this is reduced to a 36% reliability for the entire system if we are running 20 steps because the errors compound." Re-running is the cheap corrective: each pass catches and repairs the residue of the last. Cole treats Ralph as a philosophy rather than a shiny framework, and folds it into the broader craft: "Really, I would just fold loop engineering into harness engineering. It doesn't quite deserve its own buzzword."

## Part of

- [AI Coding Harness](./ai-coding-harness.md) - Ralph is the minimal harness; loop engineering folds into harness engineering.
- [Agentic Workflow Engineering](./agentic-workflow-engineering.md) - designing the loop and its exit condition is the engineering work.

## Builds on

- [Context Reset](./context-reset.md) - each pass starts fresh, reading state from disk rather than a long conversation.
- [PRD-First Development](./prd-first-development.md) - a large PRD is the scope the loop decomposes and grinds through.

## Contrasts with

- [Vibe Coding](./vibe-coding.md) - naive Ralph can drift toward vibes; Cole insists on planning and a validated exit gate to keep it principled.

## Related

- [Self-Correcting Agents](./self-correction.md) - re-running lets the agent fix its own earlier mistakes, the core of the reliability gain.
- [Self-Evolving Memory](./self-evolving-memory.md) and [Memory Systems](./memory-systems.md) - a knowledge base that "just gets better and better" as the loop runs.
- [Heartbeat](./heartbeat.md) - a scheduled trigger that keeps a loop running without a human present.
- [Parallel Agentic Coding](./parallel-agentic-coding.md) - many loops running at once across worktrees.
- [System Evolution](./system-evolution.md) - the loop compounds progress over time with little maintenance.
- [Human in the Loop](./human-in-the-loop.md) - approval gates keep an autonomous loop honest.
- [The LLM Wiki](./the-llm-wiki.md) - a knowledge base grown by a question-answer-file loop.

## Tools

- [Claude Code](../entities/tools/claude-code.md) - the agent most commonly wrapped in the bash loop.
- [Archon](../entities/tools/archon.md) - packages Ralph-style loops as workflows (video generation, autonomous iteration).

## Sources

- [I Was Wrong About Ralph Wiggum](../sources/i-was-wrong-about-ralph-wiggum.md) - "[0:07:06] this is the classic bash script because all Ralph is is just running Claude Code in a bash loop."
- [The Creators of Claude Code and OpenClaw don't Prompt Their Agents Anymore?!](../sources/the-creators-of-claude-code-and-openclaw-dont-prompt-their-agents-anymore.md) - "[0:01:40] He said, \"I don't prompt Claude anymore. I write loops and the loops do the work. My job is to write loops.\""
- [The Creators of Claude Code and OpenClaw don't Prompt Their Agents Anymore?!](../sources/the-creators-of-claude-code-and-openclaw-dont-prompt-their-agents-anymore.md) - "[0:24:23] Really, I would just fold loop engineering into harness engineering. It doesn't quite deserve its own buzzword."
- [Harness Engineering: What Separates Top Agentic Engineers Right Now](../sources/harness-engineering-what-separates-top-agentic-engineers-right-now.md) - "[0:15:49] The only way that we can exit the main while loop here is if we have this done.ext text and the coding agent is confident that the implementation is done and all the validation is there."
- [Harness Engineering: What Separates Top Agentic Engineers Right Now](../sources/harness-engineering-what-separates-top-agentic-engineers-right-now.md) - "[0:15:09] You give it a larger scope of work, like a massive PRD, and it's going to be responsible for splitting that up into individual tasks and then running coding agent sessions to handle them one at a time until everything is done."
- [Are Agent Harnesses Bringing Back Vibe Coding?](../sources/are-agent-harnesses-bringing-back-vibe-coding.md) - "[0:21:29] a lot of times AI agents will have something like a 95% reliability... this is reduced to a 36% reliability for the entire system if we are running 20 steps because the errors compound."
- [I Turned Claude Code Into a Complete Video Generation System (with Archon)](../sources/i-turned-claude-code-into-a-complete-video-generation-system-with-archon.md) - "[0:07:09] The cool part about this workflow and the other one I'll show you is that they're both just Ralph loops just for content creation instead of AI coding."
- [I Built Self-Evolving Claude Code Memory w/ Karpathy's LLM Knowledge Bases](../sources/i-built-self-evolving-claude-code-memory-w-karpathys-llm-knowledge-bases.md) - "[0:17:32] we're building up our knowledge base over time... it just gets better and better and better. And we really don't have to do anything to maintain this."
- [Introducing Archon - an AI Agent that BUILDS AI Agents](../sources/introducing-archon-an-ai-agent-that-builds-ai-agents.md) - "[0:15:13] right now archon when it produces the agent code immediately goes to you as the user to give feedback but what if you want it to autonomously iterate on the agent."
- [Let's Settle the o3-mini Vs. R1 Debate for Coding](../sources/lets-settle-the-o3-mini-vs-r1-debate-for-coding-once-and-for-all.md) - "[0:12:00] whenever you get an error in the front end just click a button... it'll paste in this entire error... and then it'll give it to the llm to fix."
