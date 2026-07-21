---
type: entity
subtype: tool
title: "tmux"
description: "Terminal multiplexer (Cole's recommended option) that Claude Code drives to create the split-pane windows showing each agent-team teammate working in real time."
resource: "https://github.com/tmux/tmux"
tags: [integration, productivity]
videos: [claude-codes-agent-teams-are-insane-multiple-ai-agents-coding-together-in-real-time]
created: 2026-07-21
updated: 2026-07-21
---

# tmux

tmux is a terminal multiplexer: one terminal window hosting many panes and sessions that persist independently of the window you launched them from. In this knowledge base it earns a page for one specific job, which is being the surface [Claude Code](./claude-code.md) draws an agent team onto. Cole's setup instruction is direct: "So if you install T-Mox which is my recommendation or iTerm 2 then claude code can leverage that directly to create those terminals and you can watch them appear in real time" ([0:04:24]).

That last clause is the point. Without a multiplexer, spawning multiple collaborating Claude Code instances is a black box; with tmux, each teammate gets its own pane and you watch the whole team work simultaneously. Navigation is the standard tmux prefix: "one thing you can do is you can press CtrlB and then you can press an arrow key to navigate between the different T-Mox terminals" ([0:07:34]). Enabling agent teams itself is separate (an environment variable or a settings.json flag); tmux only supplies the panes.

Cole recommends it over [iTerm2](./iterm2.md) mainly because it is cross-platform and not tied to macOS, and because the panes are scriptable, which is what lets the harness manage terminal creation for you. The observability it buys matters more than it sounds: agent teams sacrifice token efficiency for peer-to-peer coordination, and the failure modes Cole flags (hallucinated team compositions, a backend agent racing ahead of the database agent) are only catchable if you can see each agent's stream as it runs. tmux is therefore less a productivity nicety than the monitoring layer for [parallel agentic coding](../../concepts/parallel-agentic-coding.md).

## Realizes

- [Agent Teams](../../concepts/agent-teams.md) - Multiple collaborating agents on a shared task list, each rendered in its own pane.
- [Parallel Agent Execution](../../concepts/parallel-agent-execution.md) - Running several agents concurrently to cut wall-clock time on a task.
- [Parallel Agentic Coding](../../concepts/parallel-agentic-coding.md) - Dispatching agents to work simultaneously and reviewing what each produced.

## Contrasts with

- [iTerm2](./iterm2.md) - The macOS-only alternative Claude Code can also drive for split panes.

## Works with

- [Claude Code](./claude-code.md) - Drives tmux directly to create and lay out the terminals for each teammate.
- [Git Worktrees](./git-worktree.md) - The other half of parallel work, isolating each agent's branch while tmux isolates each agent's view.

## Related

- [Subagents Pattern](../../concepts/subagents-pattern.md) - The context-isolating alternative to agent teams, with no coordination and no panes to watch.
- [Context Isolation](../../concepts/context-isolation.md) - Why subagents exist, and what agent teams deliberately trade away for coordination.
- [Skills](../../concepts/skills.md) - Cole's /build-with-agent-team skill wraps team formation and terminal management so the setup is repeatable.
- [Slash Commands](../../concepts/slash-commands.md) - How that packaged team-formation workflow is invoked.
- [Human in the Loop](../../concepts/human-in-the-loop.md) - Watching the panes is the practical form review takes while a team runs.

## Sources

- [Claude Code's Agent Teams Are Insane - Multiple AI Agents Coding Together in Real Time](../../sources/claude-codes-agent-teams-are-insane-multiple-ai-agents-coding-together-in-real-time.md) - "[0:04:24] So if you install T-Mox which is my recommendation or iTerm 2 then claude code can leverage that directly to create those terminals and you can watch them appear in real time."
