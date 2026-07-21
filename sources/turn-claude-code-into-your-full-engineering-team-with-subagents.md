---
type: source
title: "Turn Claude Code into Your Full Engineering Team with Subagents"
description: "By wrapping an Anthropic-style agent harness with service-connected sub-agents (Linear, GitHub, Slack via Arcade), you can turn Claude Code into a full autonomous AI engineer that plans, codes, tracks tasks, and reports progress across many fresh-context sessions."
youtube_id: -GyX21BL1Nw
url: https://www.youtube.com/watch?v=-GyX21BL1Nw
slug: turn-claude-code-into-your-full-engineering-team-with-subagents
published: 2026-02-01
duration: "0:20:26"
recency_rank: 38
raw: "../raw/turn-claude-code-into-your-full-engineering-team-with-subagents.md"
tags: [subagents, ai-coding-harness, agentic-coding]
created: 2026-07-21
updated: 2026-07-21
---
# Turn Claude Code into Your Full Engineering Team with Subagents

Cole builds on Anthropic's open-sourced long-running-task harness to create a 'full AI engineer', an agent that does more than write code. Because agents fall apart when their context window fills, a harness wraps the coding agent with persistence, progress tracking, and a git workflow so multiple fresh sessions can be strung together to tackle work far larger than a single context can hold. His extension adds a tool belt of service integrations so the agent also communicates in Slack, manages tasks in Linear, and maintains a GitHub repo, mirroring what a real engineer does.

The harness starts from an appspec (a PRD-like source of truth) fed to an initializer agent, which scaffolds the project, creates Linear issues (including a meta progress-tracker issue that replaces the old local handoff text file), and initializes the GitHub repo. From there a coding loop runs in a fresh context window every session: it reads the Linear project, does regression testing to catch what a prior session broke, picks the next feature, implements it, commits, and updates status, looping until every Linear task is done. Sub-agents (Linear, GitHub, Slack) provide context isolation so the orchestrator's window stays lean, each defined in code via the Claude Agent SDK with its own markdown system prompt, allowed tools, and model (Haiku/Sonnet/Opus) for cost/speed tuning. Arcade is the MCP gateway that handles OAuth to all three services with a single authorization, and MCP tool discovery avoids dumping 91 tool definitions into the agent.

Cole closes by arguing the real power is building harnesses custom to your own workflow rather than off-the-shelf ones, and reframes his open-source Archon project: task management and RAG are now baked into coding tools, so Archon is pivoting to become 'the n8n for AI coding', a way to define and orchestrate your own custom AI coding workflows and harnesses.

## Concepts covered

- [AI Coding Harness](../concepts/ai-coding-harness.md)
- [Context Engineering](../concepts/context-engineering.md)
- [Subagents Pattern](../concepts/subagents-pattern.md)
- [Context Isolation](../concepts/context-isolation.md)
- [Context Reset](../concepts/context-reset.md)
- [Phases of Work](../concepts/phases-of-work.md)
- [The Issue Is the Spec](../concepts/issue-is-the-spec.md)
- [PRD-First Development](../concepts/prd-first-development.md)
- [Validation](../concepts/validation.md)
- [Model Selection](../concepts/model-selection.md)
- [Agentic Workflow Engineering](../concepts/agentic-workflow-engineering.md)
- [Progressive Disclosure](../concepts/progressive-disclosure.md)
- [The Evolution of AI Coding](../concepts/the-evolution-of-ai-coding.md)

## Entities

- [Claude Code](../entities/tools/claude-code.md)
- [Claude Agent SDK](../entities/tools/claude-agent-sdk.md)
- [Anthropic](../entities/organizations/anthropic.md)
- [Arcade](../entities/tools/arcade.md)
- [Linear](../entities/tools/linear.md)
- [GitHub](../entities/tools/github.md)
- [Slack](../entities/tools/slack.md)
- [Archon](../entities/tools/archon.md)
- [Playwright](../entities/tools/playwright.md)
- [Cole Medin](../entities/people/cole-medin.md)

## Key moments

- **[0:00:00]** Recap of agent harnesses as the next evolution of AI coding; why context management is the precious constraint
- **[0:01:10]** The gap: a real engineer also uses Slack, Linear/Jira, and GitHub, the agent needs that tool belt
- **[0:02:25]** The appspec (PRD-like) with a JSON task list per Anthropic's recommendation is the entry point
- **[0:03:29]** Demo: harness builds a second-brain research dashboard, creating 44 Linear tasks across sessions
- **[0:05:53]** Setup: Claude Code login (uses your subscription), env config, Arcade MCP gateway
- **[0:06:51]** Arcade adds all 91 GitHub/Linear/Slack tools via MCP tool discovery, not 91 raw definitions
- **[0:09:08]** Live run: initializer agent delegates to the Linear agent to scaffold the Pomodoro project
- **[0:10:21]** Walkthrough of Anthropic's original harness architecture: initializer plus coding loop
- **[0:11:52]** Coding loop detail: fresh context each session, regression testing, implement/update/commit
- **[0:12:35]** Cole's version: Linear becomes the source of truth, sub-agents orchestrate each service
- **[0:14:22]** Architecture: agents defined in code via Claude Agent SDK, prompts as markdown files, per-agent model
- **[0:18:31]** Reveal of completed apps; pitch for building your own custom workflows
- **[0:19:16]** Archon pivot: from task management/RAG to 'the n8n for AI coding'

## Transcript

[Raw transcript](../raw/turn-claude-code-into-your-full-engineering-team-with-subagents.md)

