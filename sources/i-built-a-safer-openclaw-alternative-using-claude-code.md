---
type: source
title: "I Built a Safer OpenClaw Alternative Using Claude Code"
description: "Rather than run the insecure but magical OpenClaw personal assistant, clone its MIT-licensed repo, point a coding agent at it, and rebuild its four core components (memory, heartbeat, channel adapters, skills) into your own secure, customized second brain."
youtube_id: XmweZ4fLkcI
url: https://www.youtube.com/watch?v=XmweZ4fLkcI
slug: i-built-a-safer-openclaw-alternative-using-claude-code
published: 2026-02-11
duration: "0:15:15"
recency_rank: 35
raw: "../raw/i-built-a-safer-openclaw-alternative-using-claude-code.md"
tags: [second-brain, agent-security, memory-systems]
created: 2026-07-21
updated: 2026-07-21
---
# I Built a Safer OpenClaw Alternative Using Claude Code

Cole opens on OpenClaw, the explosively popular (185k+ GitHub stars) open-source personal AI assistant that feels magical because it remembers your context and acts proactively, but carries severe security problems: a one-click remote-code-execution vulnerability that leaks OAuth tokens, plaintext credential storage, and a public skills marketplace (Claw Hub) riddled with hundreds of malicious packages stealing API keys and SSH credentials. Beyond codebase flaws, he argues the deeper issue is that OpenClaw is a huge, poorly-understood codebase being handed enormous agent power, which most people are not ready for.

His solution is to treat OpenClaw as a reference implementation rather than something to run. He identifies the four components that make it feel magical, memory system, heartbeat (proactive scheduled action), channel adapters, and the skills registry, and rebuilds each himself in a couple thousand lines of Python and markdown. The method is repeatable: clone the repo locally, point Claude Code at it, ask it to explain how a component works, then have it rebuild that component adapted to your own tech stack with your customizations. Coding agents thrive on a simple, elegant, working example as context.

His own build mirrors OpenClaw's markdown-driven memory (soul.md, user.md, memory.md, agents.md, daily session logs) with a light SQLite RAG layer, adds Obsidian for storage/sync, uses Postgres when deployed to a VPS, and drives everything through the Claude Agent SDK so he can use his Anthropic subscription instead of expensive API credits (running OpenClaw against a Claude subscription violates Anthropic's ToS and has gotten accounts banned; Claude Code / Agent SDK in your own environment is allowed). The heartbeat is a scheduled Agent SDK job every 30 minutes checking email, calendar, and Asana for notifications. He keeps just one channel adapter (Slack) plus the terminal, and leans on Claude Code's built-in skills, including a skill for creating more skills, to evolve capabilities securely without a public registry.

## Concepts covered

- [Second Brain](../concepts/second-brain.md)
- [Memory Systems](../concepts/memory-systems.md)
- [Heartbeat](../concepts/heartbeat.md)
- [Chat Interfaces](../concepts/chat-interfaces.md)
- [Skills](../concepts/skills.md)
- [Learn by Building](../concepts/learn-by-building.md)
- [Agent Protocols](../concepts/agent-protocols.md)
- [Agent Security](../concepts/agent-security.md)
- [Provider Independence](../concepts/provider-independence.md)

## Entities

- [OpenClaw](../entities/tools/openclaw.md)
- [Claude Code](../entities/tools/claude-code.md)
- [Claude Agent SDK](../entities/tools/claude-agent-sdk.md)
- [Obsidian](../entities/tools/obsidian.md)
- [Postgres](../entities/tools/postgres-pgvector.md)
- [Slack](../entities/tools/slack.md)
- [Anthropic](../entities/organizations/anthropic.md)
- [Dynamous](../entities/organizations/dynamous.md)
- [Cole Medin](../entities/people/cole-medin.md)

## Key moments

- **[0:00:00]** OpenClaw introduced as the explosively popular open-source personal AI assistant (185k+ stars)
- **[0:02:18]** Security lane 1: codebase architecture flaws (one-click RCE, plaintext credentials)
- **[0:03:06]** Security lane 1b: Claw Hub marketplace has hundreds of malicious skill packages
- **[0:04:11]** Security lane 2: huge unaudited codebase handing too much power to the agent
- **[0:05:14]** The four magical components: memory, heartbeat, channel adapters, skills registry
- **[0:05:46]** Memory system is markdown-driven (soul.md, user.md, memory.md, agents.md) + light SQLite RAG
- **[0:08:27]** Rebuild method: clone repo, point Claude Code at it, ask it to adapt the component to your stack
- **[0:09:45]** His tech stack: Obsidian, Markdown, SQLite/Postgres, Claude Agent SDK, Claude Code
- **[0:10:00]** Uses Claude Code so he can use his Anthropic subscription; OpenClaw+subscription violates ToS and gets bans
- **[0:10:34]** Heartbeat is a 30-min scheduled Agent SDK job checking email, calendar, Asana
- **[0:11:18]** Keeps only one adapter (Slack) plus terminal; can one-shot more if needed
- **[0:12:12]** Skills built into Claude Code/Agent SDK; has a skill for creating more skills; no public registry = more secure
- **[0:13:42]** The repeatable process recap: clone MIT-licensed repo, point agent at it, rebuild each part

## Transcript

[Raw transcript](../raw/i-built-a-safer-openclaw-alternative-using-claude-code.md)

