---
type: entity
subtype: tool
title: "iTerm2"
description: "macOS terminal application with split-pane support; one of only two terminals Claude Code can drive to display agent teams live."
resource: "https://iterm2.com"
tags: [terminal, agent-teams, claude-code, productivity]
videos: [claude-codes-agent-teams-are-insane-multiple-ai-agents-coding-together-in-real-time]
created: 2026-07-21
updated: 2026-07-21
---

# iTerm2

iTerm2 is a macOS terminal replacement, and in this knowledge base it matters for one narrow but hard requirement: it is one of only two terminals Claude Code can drive when running [agent teams](../../concepts/agent-teams.md). "you need to install either T-Mox or iTerm 2. These are terminal applications that support the split pane mode and these are just the two that are supported by claude code right now" [0:04:09] (the transcript renders tmux phonetically). Without one of the two installed, the feature simply has nowhere to put the agents.

The dependency exists because agent teams are not a background abstraction. Claude Code spawns several real Claude Code instances that collaborate on one shared task list, and it needs a terminal that can programmatically create and address split panes so each teammate gets a visible pane you can watch in real time. That visibility is a large part of the value: unlike the [subagents pattern](../../concepts/subagents-pattern.md), where a dispatched task is a black box that returns only a summary, an agent team is legible while it runs, so you can see the frontend agent react when the API agent changes a contract.

Practically this makes iTerm2 the macOS-native answer and [tmux](./tmux.md) the cross-platform one. Neither adds intelligence; both are plumbing. But it is a useful reminder that agentic features increasingly reach down into the local environment, and that the [AI coding harness](../../concepts/ai-coding-harness.md) includes the terminal you happen to run it in. The feature is still experimental and must be explicitly enabled through an environment variable or `settings.json`, so terminal setup is only the first prerequisite.

## Realizes

- [Agent Teams](../../concepts/agent-teams.md) - Coordinating multiple specialized agents on a shared task list with peer-to-peer handoffs; the split panes are where that team actually lives.
- [Parallel Agent Execution](../../concepts/parallel-agent-execution.md) - Running multiple agents concurrently to cut wall-clock time, made observable one pane per agent.

## Contrasts with

- [tmux](./tmux.md) - The other terminal multiplexer Claude Code supports for agent teams, and the cross-platform option where iTerm2 is macOS only.
- [Visual Studio Code](./vs-code.md) - The editor-centric surface for AI coding, versus the terminal-centric surface agent teams require.

## Works with

- [Claude Code](./claude-code.md) - Anthropic's terminal-based agentic coding assistant; agent teams is its experimental multi-instance feature.

## Related

- [Subagents Pattern](../../concepts/subagents-pattern.md) - Delegating scoped tasks to isolated subagents; the black-box alternative agent teams are defined against.
- [Context Isolation](../../concepts/context-isolation.md) - Giving each agent its own clean context window, the property subagents keep and agent teams trade away for coordination.
- [Parallel Agentic Coding](../../concepts/parallel-agentic-coding.md) - Dispatching agents to background tasks in isolated worktrees, each returning a reviewable PR.
- [Git Worktrees](./git-worktree.md) - Git feature that duplicates a codebase across isolated branches so parallel agents do not collide.
- [AI Coding Harness](../../concepts/ai-coding-harness.md) - The scaffolding of prompts, tools, rules, and environment that turns a raw model into a reliable coding system.

## Sources

- [Claude Code's Agent Teams Are Insane - Multiple AI Agents Coding Together in Real Time](../../sources/claude-codes-agent-teams-are-insane-multiple-ai-agents-coding-together-in-real-time.md) - "[0:04:09] you need to install either T-Mox or iTerm 2. These are terminal applications that support the split pane mode and these are just the two that are supported by claude code right now."
