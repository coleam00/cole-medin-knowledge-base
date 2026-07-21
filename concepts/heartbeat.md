---
type: concept
title: "Heartbeat"
description: "A scheduled proactive loop that lets an AI system check in and act on its own without being prompted."
tags: [heartbeat, proactive, scheduling]
videos: [the-creators-of-claude-code-and-openclaw-dont-prompt-their-agents-anymore, full-guide-build-your-own-ai-second-brain-with-claude-code, everything-you-thought-about-building-ai-agents-is-wrong, i-built-a-safer-openclaw-alternative-using-claude-code]
created: 2026-07-21
updated: 2026-07-21
---

# Heartbeat

A heartbeat is a scheduled job that wakes an agent on its own so it can decide what needs doing before the user ever asks. "It's a scheduled job that runs every 30 minutes for me right now... look at my memory, look at recent emails... calendar, my tasks in asana, and then give me notifications for anything that need my attention." - ["I Built a Safer OpenClaw Alternative Using Claude Code"](../sources/i-built-a-safer-openclaw-alternative-using-claude-code.md) [0:10:34]. It is the mechanism that converts a reactive assistant into a proactive one: "this really brings everything together because it's where we build the proactive nature of our second brain" - ["Full Guide - Build Your Own AI Second Brain with Claude Code"](../sources/full-guide-build-your-own-ai-second-brain-with-claude-code.md) [0:17:21].

## How it works

The defining design choice is that the expensive context-gathering happens deterministically, in code, *before* the LLM is invoked. "we have this deterministic part before we even go into Claude Code where we're gathering a context around my life... And then we send all of that pertinent information into Claude Code" - [Full Guide - Build Your Own AI Second Brain](../sources/full-guide-build-your-own-ai-second-brain-with-claude-code.md) [0:17:51]. On each tick the agent consults a checklist file for what would be useful right now: "we're leveraging this heartbeat.md... whenever it runs autonomously on a scheduled basis, it should look there to see what can I do for Cole right now that he would appreciate." - [I Built a Safer OpenClaw Alternative](../sources/i-built-a-safer-openclaw-alternative-using-claude-code.md) [0:06:22]. Cole runs the whole loop on the [Claude Agent SDK](../entities/tools/claude-agent-sdk.md): "I'm using the Claude agent SDK for the whole heartbeat system that I built for my own second brain inspired by OpenClaw" - ["Everything You Thought About Building AI Agents is Wrong"](../sources/everything-you-thought-about-building-ai-agents-is-wrong.md) [0:06:04], and over time it "builds memories over time. It does daily reflection to basically learn from its work and my requests over time" [0:06:14].

## Contrasts with

- [The Issue Is the Spec](./issue-is-the-spec.md) - a related trigger idea from the same "don't prompt your agents anymore" family: instead of a clock, a new GitHub issue kicks off the work. The scheduled-interval variant is the heartbeat proper: "With /loop, we set an interval for running a prompt. So like every 5 minutes, I'm going to check for new GitHub issues in this repo" - ["The Creators of Claude Code and OpenClaw don't Prompt Their Agents Anymore?!"](../sources/the-creators-of-claude-code-and-openclaw-dont-prompt-their-agents-anymore.md) [0:02:25], while "/routines... are the scheduled jobs. Like every hour I want you to wake up look at some larger spec document and handle the next task." [0:02:55].

## Part of

- [Second Brain](./second-brain.md) - the personal AI system the heartbeat makes proactive.

## Related

- [Memory Systems](./memory-systems.md) - the memory the heartbeat reads and appends to each tick.
- [Self-Evolving Memory](./self-evolving-memory.md) - the daily-reflection pass a heartbeat can schedule to promote and prune notes.
- [The Ralph Loop](./the-ralph-loop.md) - the same wake-do-one-thing-persist pattern applied to autonomous coding runs.
- [Agent Security](./agent-security.md) - the risk surface a proactive, always-on agent introduces, and why Cole framed his build as a "safer" alternative.

## Tools

- [Claude Agent SDK](../entities/tools/claude-agent-sdk.md) - the runtime the heartbeat loop is built on.
- [Claude Code](../entities/tools/claude-code.md) - where the gathered context is reasoned over each tick.
- [OpenClaw](../entities/tools/openclaw.md) - the autonomous-agent project this heartbeat design was inspired by.
- [Asana](../entities/tools/asana.md) / [Slack](../entities/tools/slack.md) - representative integrations the loop pulls tasks from and pushes notifications to.

## Sources

- [I Built a Safer OpenClaw Alternative Using Claude Code](../sources/i-built-a-safer-openclaw-alternative-using-claude-code.md) - "[0:10:34] I'm using the Claude agent SDK. It's a scheduled job that runs every 30 minutes for me right now... look at my memory, look at recent emails... calendar, my tasks in asana, and then give me notifications for anything that need my attention."
- [Full Guide - Build Your Own AI Second Brain with Claude Code](../sources/full-guide-build-your-own-ai-second-brain-with-claude-code.md) - "[0:17:21] the last thing that I want to cover... is the heartbeat. And this really brings everything together because it's where we build the proactive nature of our second brain"
- [Everything You Thought About Building AI Agents is Wrong](../sources/everything-you-thought-about-building-ai-agents-is-wrong.md) - "[0:06:04] I'm using the Claude agent SDK for the whole heartbeat system that I built for my own second brain inspired by OpenClaw"
- [The Creators of Claude Code and OpenClaw don't Prompt Their Agents Anymore?!](../sources/the-creators-of-claude-code-and-openclaw-dont-prompt-their-agents-anymore.md) - "[0:02:55] last we have /routines. And so these are the scheduled jobs. Like every hour I want you to wake up look at some larger spec document and handle the next task."
