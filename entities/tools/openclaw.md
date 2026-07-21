---
type: entity
subtype: tool
title: "OpenClaw"
description: "The agent project (formerly Claudebot) that Cole's second brain was researching; that research is the demo's input document."
tags: [coding-agent, open-source, loop-engineering]
videos: [pydantic-ai-20-the-new-best-way-to-build-ai-agents-is-composing-capabilities, the-creators-of-claude-code-and-openclaw-dont-prompt-their-agents-anymore, pi-coding-agent-archon-build-any-ai-coding-workflow-no-claude-code-bloat, full-guide-build-your-own-ai-second-brain-with-claude-code, everything-you-thought-about-building-ai-agents-is-wrong, i-built-a-safer-openclaw-alternative-using-claude-code, ai-agents-can-now-build-their-own-ui-in-real-time-personalized-to-you]
created: 2026-07-21
updated: 2026-07-21
---

# OpenClaw

[OpenClaw](./openclaw.md), previously known as Claudebot, is the wildly popular open-source agent project that became a design template for Cole's own systems. "I of course have been following along with all the developments with OpenClaw, otherwise known or previously known as Claudebot." Its reach is hard to overstate: "they exploded up to 185,000 stars. I have not seen a repository on GitHub with this many stars," and critically "it's MIT licensed. You can do anything you want with the code."

Its creator, Peter Steinberger, is one of the figures Cole credits with "pushing this new fad, whether they like it or not, of loop engineering," the idea that you stop hand-prompting and instead let the agent run in a [loop](../../concepts/agentic-workflow-engineering.md). That thread runs through Cole's [agentic workflow engineering](../../concepts/agentic-workflow-engineering.md) and [heartbeat](../../concepts/heartbeat.md)-style autonomy.

OpenClaw's biggest influence, though, is on his [second brain](../../concepts/second-brain.md). "As I built my second brain on top of [Claude Code](./claude-code.md), I pointed it to the Openclaw GitHub repository" for inspiration, adopting its memory system and "my own rag setup that's actually inspired by OpenClaw... for semantic search." He later "built a safer OpenClaw alternative using Claude Code," treating it as a reference architecture rather than a dependency. It also anchors a [provider independence](../../concepts/provider-independence.md) point: [Pi](./pi-coding-agent.md) "actually runs OpenClaw under the hood," and because leaning on it alone is not enough for production, "you can't just lean on those coding agent SDKs or something like Hermes or Open Claw. You need a framework." It is best understood as an [AI coding harness](../../concepts/ai-coding-harness.md) and idea source, not a tool Cole ships on directly.

## Related

- [Agentic Workflow Engineering](../../concepts/agentic-workflow-engineering.md)
- [Heartbeat](../../concepts/heartbeat.md)
- [Second Brain](../../concepts/second-brain.md)
- [Provider Independence](../../concepts/provider-independence.md)
- [Skills](../../concepts/skills.md)
- [AI Coding Harness](../../concepts/ai-coding-harness.md)
- [Claude Code](./claude-code.md)
- [Pi](./pi-coding-agent.md)
- [Archon](./archon.md)

## Sources

- [Pydantic AI 2.0: The New Best Way to Build AI Agents is Composing Capabilities](../../sources/pydantic-ai-20-the-new-best-way-to-build-ai-agents-is-composing-capabilities.md)
- [The Creators of Claude Code and OpenClaw don't Prompt Their Agents Anymore?!](../../sources/the-creators-of-claude-code-and-openclaw-dont-prompt-their-agents-anymore.md) - "[0:00:15] Like Peter Steinberger, the creator of OpenClaw... they're pushing this new fad, whether they like it or not, of loop engineering."
- [Pi Coding Agent + Archon: Build ANY AI Coding Workflow (No Claude Code Bloat)](../../sources/pi-coding-agent-archon-build-any-ai-coding-workflow-no-claude-code-bloat.md) - "[0:06:37] I believe it's against Anthropic's terms of service to use your subscription with Pi. It's the same thing that Pi actually runs OpenClaw under the hood."
- [Full Guide - Build Your Own AI Second Brain with Claude Code](../../sources/full-guide-build-your-own-ai-second-brain-with-claude-code.md) - "[0:08:17] we're going to do is take inspiration from Openclaw. So literally as I built my second brain on top of Claude code, I pointed it to the Openclaw GitHub repository"
- [Everything You Thought About Building AI Agents is Wrong](../../sources/everything-you-thought-about-building-ai-agents-is-wrong.md) - "[0:05:48] I built for my own second brain inspired by OpenClaw"
- [I Built a Safer OpenClaw Alternative Using Claude Code](../../sources/i-built-a-safer-openclaw-alternative-using-claude-code.md) - "[0:00:14] it is a fully open-source tool. And so this is the GitHub repository. They exploded up to 185,000 stars. I have not seen a repository on GitHub with this many stars."
- [AI Agents Can Now Build Their Own UI in Real Time (Personalized to You)](../../sources/ai-agents-can-now-build-their-own-ui-in-real-time-personalized-to-you.md) - "[0:08:31] I of course have been following along with all the developments with OpenClaw, otherwise known or previously known as Claudebot."
