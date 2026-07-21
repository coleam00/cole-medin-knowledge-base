---
type: source
title: "I Forced Claude to Code for 24 Hours NONSTOP, Here's What Happened"
description: "Anthropic's open-sourced long-running-agent harness lets a coding agent build a complex app over 24 hours by splitting work across fresh context windows, coordinated through a few shared artifact files and test-driven development."
youtube_id: usQ2HBTTWxs
url: https://www.youtube.com/watch?v=usQ2HBTTWxs
slug: i-forced-claude-to-code-for-24-hours-nonstop-heres-what-happened
published: 2025-12-03
duration: "0:26:48"
recency_rank: 50
raw: "../raw/i-forced-claude-to-code-for-24-hours-nonstop-heres-what-happened.md"
tags: [harness, test-driven-development, context-isolation, claude-agent-sdk]
created: 2026-07-21
updated: 2026-07-21
---

Cole takes Anthropic's newly open-sourced harness for long-running agents, drops Claude Code into it via the Claude Agent SDK, and lets it build a clone of Claude.ai for 24 hours straight. A harness, he explains, is just a coordination layer on top of coding agents that lets them work for hours without overwhelming a single context window by splitting the same large task across many agents and fresh context windows. The whole system is essentially a set of prompts and artifact files, so it is agent-agnostic: you could swap Claude Code for Codex or OpenCode with the same harness.

The harness is built on test-driven development. An initializer agent reads the app spec (a PRD) and produces three core artifacts: a feature-list JSON with 200+ granular test cases (each with category, description, validation steps, and a pass true/false flag), an initialization script that scaffolds and spins up the project, and a git repo. It also writes a CLAUDE_PROGRESS file summarizing what it did. Then coding agents loop indefinitely, each in a brand-new context window: they prime by reading the PRD, feature list, CLAUDE_PROGRESS, and git log; run the init script; do light regression testing against recently-passed features using the Puppeteer MCP server for visual and browser validation; implement the next unpassed feature; mark only its pass flag true; commit to git as a save state; and rewrite CLAUDE_PROGRESS for the next agent. The fresh-context-plus-shared-artifacts pattern is what lets it run essentially forever.

Cole runs it programmatically with the Claude Agent SDK (using a Claude subscription token, not an API key, to avoid huge costs), restricting file ops to the project directory, auto-accepting edits, allow-listing tools, and adding a bash-command hook for safety. After 24 hours it reached the 54th coding session with 54% of tests passing (100+ tests) and a surprisingly feature-rich, near-functional Claude clone. He notes minor drift (CLAUDE_PROGRESS mislabeling a session number) and imperfect UI, but is impressed that the agent stayed aligned across dozens of sessions and encourages viewers to clone the repo and adapt the app spec to build anything.

## Concepts covered

- [AI Coding Harness](../concepts/ai-coding-harness.md)
- [Test-Driven Development](../concepts/test-driven-development.md)
- [Context Isolation](../concepts/context-isolation.md)
- [Prime Command](../concepts/prime-command.md)
- [PRD-First Development](../concepts/prd-first-development.md)
- [Self-Evolving Memory](../concepts/self-evolving-memory.md)
- [Git as Long-Term Memory](../concepts/git-as-long-term-memory.md)
- [End-to-End Validation](../concepts/end-to-end-validation.md)
- [Validation](../concepts/validation.md)
- [Provider Independence](../concepts/provider-independence.md)
- [Human in the Loop](../concepts/human-in-the-loop.md)
- [Agentic Coding](../concepts/agentic-coding.md)

## Entities

- [Anthropic](../entities/organizations/anthropic.md)
- [Claude Agent SDK](../entities/tools/claude-agent-sdk.md)
- [Claude Code](../entities/tools/claude-code.md)
- [MCP (Model Context Protocol)](../entities/tools/mcp.md)
- [Codex](../entities/tools/codex.md)
- [Cole Medin](../entities/people/cole-medin.md)
- [Dynamous](../entities/organizations/dynamous.md)

## Key moments

- **[0:00:00]** Anthropic open-sources a harness for long-running agents; a harness is a coordination layer that splits work across context windows
- **[0:01:47]** The build target: a 24-hour clone of Claude.ai, matching the demo in Anthropic's article
- **[0:02:51]** Harness overview begins; built on test-driven development with success criteria defined up front
- **[0:03:41]** The initializer agent: reads the app spec / PRD and sets up the project
- **[0:04:13]** Three core artifacts introduced: feature-list JSON (200+ test cases), init script, CLAUDE_PROGRESS
- **[0:05:35]** The coding-agent loop: prime, regression test, implement next feature, commit, rewrite progress, repeat n times
- **[0:07:23]** Puppeteer MCP validation and bash-command guardrails for a secure autonomous system
- **[0:07:39]** Not the Claude Code CLI; the harness drives Claude Code programmatically via the Claude Agent SDK
- **[0:08:58]** Using a Claude subscription token (claude setup-token) instead of an Anthropic API key to control cost
- **[0:22:13]** 24-hour result: 54th coding session, 54% of tests passing (100+ tests), a near-functional Claude clone
- **[0:24:44]** Remaining false features are nitpicky details (scrollbars, mobile styling); minor CLAUDE_PROGRESS session-number drift noted

## Transcript

[Raw transcript](../raw/i-forced-claude-to-code-for-24-hours-nonstop-heres-what-happened.md)
