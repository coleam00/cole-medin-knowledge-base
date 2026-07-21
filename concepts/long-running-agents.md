---
type: concept
title: "Long-Running Agents"
description: "Coding agents that run autonomously for hours or days as background tasks, chaining dozens of fresh-context sessions through shared artifact files to produce a working proof of concept before a human takes over."
tags: [autonomy, background-agents]
videos: [i-forced-claude-to-code-for-24-hours-nonstop-heres-what-happened]
created: 2026-07-21
updated: 2026-07-21
---

# Long-Running Agents

A long-running agent is a coding agent left to work unattended for hours or days, chaining dozens of separate sessions into one continuous build. The deliverable is not a shipped product but a running head start: "Build auto proof of concept and then we come in and keep building on top of it." [0:00:49] The human returns to a codebase that already compiles, already passes tests, and is worth extending rather than a blank repo.

The binding constraint is the context window, so the harness never tries to stretch one session. It splits the same large task across many agents and many fresh context windows, coordinating them entirely through artifact files on disk. In Anthropic's open-sourced version, an initializer agent reads the app spec and emits three things: a feature-list JSON holding 200+ granular test cases (each with a category, description, validation steps, and a pass flag), an initialization script that scaffolds and starts the project, and a git repo. It also writes a progress file summarizing what it did.

Every coding session after that runs the same fixed loop in a brand-new context: prime by reading the spec, the feature list, the progress file, and the git log; run the init script; regression-test recently passed features through a browser MCP server; implement the next unpassed feature; flip only that feature's pass flag; commit as a save state; and rewrite the progress file for its successor. Fresh context plus durable shared state is what lets the system run essentially forever.

Cole's 24-hour run reached its 54th session with 54% of the tests passing and a surprisingly complete Claude.ai clone: "It still is really cool how much I was able to build here without laying a finger on anything." [0:23:58] Drift showed up (a mislabeled session number, rough UI polish) but alignment held across dozens of handoffs. Operationally he drove Claude Code programmatically through the Claude Agent SDK using a subscription token instead of an API key to keep cost sane, restricted file operations to the project directory, auto-accepted edits, allow-listed tools, and added a bash-command hook as a guardrail. Because the harness is only prompts plus files, the underlying agent is swappable.

## Prerequisites

- [Context Isolation](./context-isolation.md) - the reason work is split across sessions instead of one long conversation.
- [PRD-First Development](./prd-first-development.md) - the app spec the initializer decomposes into a test list.

## Builds on

- [AI Coding Harness](./ai-coding-harness.md) - the coordination layer that makes multi-hour autonomy possible.
- [Test-Driven Development](./test-driven-development.md) - pass flags on granular test cases are the progress ledger and the exit condition.

## Contrasts with

- [The Ralph Loop](./the-ralph-loop.md) - Ralph re-runs the same prompt and state; a long-running harness advances an explicit, checkable feature list one item per session.

## Tools

- [Claude Agent SDK](../entities/tools/claude-agent-sdk.md) - drives the agent programmatically with hooks, allow-lists, and a subscription token.
- [Claude Code](../entities/tools/claude-code.md) - the agent inside the loop, swappable for another.
- [Puppeteer](../entities/tools/puppeteer.md) - browser validation of features already marked passing.
- [Archon](../entities/tools/archon.md) - packages the same idea as durable, resumable workflows.
- [LangChain Deep Agents](../entities/tools/langchain-deep-agents.md) - LangChain's harness implementation for long-running (not just coding) agents that manages context by offloading to file-system tools.
- [Anthropic](../entities/organizations/anthropic.md) - open-sourced the harness this pattern is built from.

## Related

- [Context Reset](./context-reset.md) - each session starts clean and rereads state from disk.
- [Handoff Documents](./handoff-documents.md) - the progress file one session writes for the next.
- [Git as Long-Term Memory](./git-as-long-term-memory.md) - commits are save states the next agent can read and trust.
- [Prime Command](./prime-command.md) - the fixed priming step that rebuilds understanding cheaply.
- [Granular Task Management](./granular-task-management.md) - 200+ small features beat one vague goal.
- [End-to-End Validation](./end-to-end-validation.md) and [Validation](./validation.md) - regression checks keep earlier passes honest.
- [Self-Evolving Memory](./self-evolving-memory.md) - artifact files that improve as the run proceeds.
- [Loop Engineering](./loop-engineering.md) - designing the loop that keeps dispatching sessions.
- [The Five Levels of AI Coding Autonomy](./five-levels-of-ai-coding-autonomy.md) - where unattended overnight builds sit on the ladder.
- [Human in the Loop](./human-in-the-loop.md) - guardrails and the takeover point after the proof of concept.
- [Dark Factory](./dark-factory.md) and [Heartbeat](./heartbeat.md) - scheduled, humanless variants of the same idea.
- [Provider Independence](./provider-independence.md) - a prompts-and-files harness is not tied to one agent.
- [Disposable Agent Sandboxes](./disposable-agent-sandboxes.md) - Running each agent in an ephemeral, preloaded cloud dev box ('cattle, not pets') instead of a local worktree, so many unattended agents can run in parallel with scoped permissions.
- [Remote Agentic Coding](./remote-agentic-coding.md) - Kicking off a coding request from anywhere (phone, chat app) to an agent that runs entirely remotely in an isolated container, cloning the GitHub repo, branching, and deploying on its own.
- [Initializer + Task Agent Architecture](./initializer-and-task-agent.md) - The most common harness pattern: an initializer agent scaffolds the project and produces a validated feature list, then a task agent runs in a loop making incremental progress across context-reset sessions.

## Sources

- [I Forced Claude to Code for 24 Hours NONSTOP, Here's What Happened](../sources/i-forced-claude-to-code-for-24-hours-nonstop-heres-what-happened.md) - "[0:00:49] Build auto proof of concept and then we come in and keep building on top of it."
- [I Forced Claude to Code for 24 Hours NONSTOP, Here's What Happened](../sources/i-forced-claude-to-code-for-24-hours-nonstop-heres-what-happened.md) - "[0:23:58] It still is really cool how much I was able to build here without laying a finger on anything."
