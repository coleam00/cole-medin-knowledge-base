---
type: source
title: "I Built My Second Brain with Claude Code + Obsidian + Skills (Here's How)"
description: "Claude Code paired with Obsidian and Skills is a powerful second-brain system for research, ideation, and organization, not just coding."
youtube_id: jYMhDEzNAN0
url: https://www.youtube.com/watch?v=jYMhDEzNAN0
slug: i-built-my-second-brain-with-claude-code-obsidian-skills-heres-how
published: 2026-01-25
duration: "0:20:44"
recency_rank: 40
raw: "../raw/i-built-my-second-brain-with-claude-code-obsidian-skills-heres-how.md"
tags: [second-brain, claude-code, obsidian, skills]
created: 2026-07-21
updated: 2026-07-21
---
# I Built My Second Brain with Claude Code + Obsidian + Skills (Here's How)

Cole argues that Claude Code was mistakenly pigeonholed as a coding-only tool. Stripping away code intelligence, a coding agent is really a powerful general assistant with file operations, search, terminal execution, and web search running on your machine, which is exactly what a second brain needs for its three jobs: research, ideation, and organization. He walks through the capabilities he has built (AI-news research, content ideas, Excalidraw diagrams, YouTube scripts, Remotion video generation, on-brand PowerPoint slides) while stressing the system augments rather than replaces the human and requires a lot of human touch.

The core of the video is why the Claude Code + Obsidian + Skills triad works. Obsidian is the canvas: everything stores as local, private markdown, which is both an ideal LLM format and a native file system that the agent can operate on directly (unlike Notion, which would require an MCP server). Skills are what tie it together, giving the agent your own capabilities, processes, and guidelines through progressive disclosure. Rather than dumping every tool into context up front like MCP servers do, a skill exposes only a short description, then loads its SKILL.md when relevant, then optionally loads deeper reference files or Python scripts. This keeps context efficient even as capabilities grow into the hundreds, and lets Claude Code specialize itself per session.

He then demos a shared template repo of skills: a brand-and-voice generator that captures your tone so downstream skills are personalized, Anthropic's skill-creator, a PowerPoint generator that uses code execution via a cookbook of Python scripts, and an MCP-to-skill client that wraps any MCP server behind a Python script so its tools never bloat the context window. He connects a read-only Zapier MCP (Gmail, Calendar, Slack, Asana) and recommends documenting MCP gotchas in global rules (CLAUDE.md) to improve reliability over time.

## Concepts covered

- [Second Brain](../concepts/second-brain.md)
- [The AI Layer](../concepts/the-ai-layer.md)
- [Skills](../concepts/skills.md)
- [Progressive Disclosure](../concepts/progressive-disclosure.md)
- [Context Engineering](../concepts/context-engineering.md)
- [The Problems With MCP Servers](../concepts/mcp-problems.md)
- [Code Execution](../concepts/code-execution.md)
- [Global Rules](../concepts/global-rules.md)
- [Human in the Loop](../concepts/human-in-the-loop.md)
- [Community-Driven Development](../concepts/community-driven-development.md)

## Entities

- [Claude Code](../entities/tools/claude-code.md)
- [Obsidian](../entities/tools/obsidian.md)
- [Model Context Protocol (MCP)](../entities/tools/mcp.md)
- [Anthropic](../entities/organizations/anthropic.md)
- [Dynamous](../entities/organizations/dynamous.md)
- [Zapier](../entities/tools/zapier.md)
- [Remotion](../entities/tools/remotion.md)
- [Cole Medin](../entities/people/cole-medin.md)

## Key moments

- **[0:00:00]** Hook: Claude Code is not just for coding; with Obsidian and Skills it becomes a second brain
- **[0:01:46]** Purpose of a second brain: research, ideation, organization; augment not automate, no AI slop
- **[0:04:51]** The five capabilities of a coding agent; remove code intelligence and you have a general assistant
- **[0:06:16]** Why Obsidian: local private markdown is ideal LLM format and native file system; better than Notion
- **[0:07:34]** Why Skills: give the agent your capabilities in a flexible, context-efficient way
- **[0:09:49]** Progressive disclosure explained across three layers: description, SKILL.md, reference files/scripts
- **[0:12:55]** Template repo walkthrough: brand-and-voice generator, skill-creator, MCP client, PowerPoint generator
- **[0:15:56]** PowerPoint generator demo via code execution and Python cookbook scripts
- **[0:16:48]** MCP-to-skill client: wrap any MCP behind a Python script to avoid context bloat
- **[0:18:35]** Document MCP gotchas in global rules (CLAUDE.md) to improve reliability over time

## Transcript

[Raw transcript](../raw/i-built-my-second-brain-with-claude-code-obsidian-skills-heres-how.md)

