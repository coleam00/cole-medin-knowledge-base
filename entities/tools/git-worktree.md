---
type: entity
subtype: tool
title: "Git Worktrees"
description: "Git feature that duplicates the codebase across isolated branches so multiple coding agents can run in parallel without collisions."
resource: "https://git-scm.com/docs/git-worktree"
tags: [git, parallelism, isolation]
videos: [the-creators-of-claude-code-and-openclaw-dont-prompt-their-agents-anymore, omnigent-the-new-meta-harness-for-every-coding-agent-claude-code-codex-pi-more, parallel-claude-code-git-worktrees-this-setup-will-change-how-you-ship, im-building-an-ai-dark-factory-that-ships-its-own-code-public-experiment, youre-hardly-using-what-claude-code-has-to-offer-its-insane, this-new-protocol-will-change-ai-coding-forever-acp, a-complete-guide-to-claude-code-here-are-all-the-best-strategies]
created: 2026-07-21
updated: 2026-07-21
---

# Git Worktrees

Git worktrees are a native [Git](./git.md) feature that checks out multiple branches of one repository into separate directories at the same time, giving each an isolated copy of the codebase. Cole leans on this to run many coding agents at once: "it actually duplicates everything. So, you have a completely isolated environment in a separate branch. And then you can just change into that directory and launch cloud" ([0:42:44]). The point is not disk copies for their own sake but collision-free parallelism, which is the mechanical backbone of [Parallel Agentic Coding](../../concepts/parallel-agentic-coding.md) and [Context Isolation](../../concepts/context-isolation.md).

## How Cole uses it / why it matters

Worktrees are what let Cole fan work out to several [Claude Code](./claude-code.md) (or [Codex](./codex.md), [Pi](./pi-coding-agent.md)) instances without them overwriting each other: "Work trees are also a really important part of loop engineering... we need to make sure they're running in isolation so they're not stepping on each other's toes" ([0:14:03]). Each agent gets its own environment mapped to a feature branch and ultimately a pull request, mirroring how humans already work: "we have a copy of our repo living in the .claude/workreees folder for each of our work trees. And real development is always working with feature branches and different pull requests" ([0:04:04]). Protocol- and harness-driven agents automate the whole lifecycle: "the agent will kind of spin up its own work tree, its own environment where it will can do whatever it wants and it will come back to you with a PR" ([0:18:39]). This is why worktrees are baked into [Archon](./archon.md), which "gives us the work tree and isolation support so that we can manage all of these different implementations at the exact same time" ([0:20:47]), enabling [Agentic Workflow Engineering](../../concepts/agentic-workflow-engineering.md) at scale and supporting [Provider Independence](../../concepts/provider-independence.md) since each isolated branch can run a different model chosen by [Model Selection](../../concepts/model-selection.md). A [Human in the Loop](../../concepts/human-in-the-loop.md) then reviews the resulting PRs.

## Related

- [Parallel Agentic Coding](../../concepts/parallel-agentic-coding.md) and [Context Isolation](../../concepts/context-isolation.md) - worktrees are the mechanism that makes both possible.
- [Agentic Workflow Engineering](../../concepts/agentic-workflow-engineering.md) - managing many isolated implementations at once.
- [Provider Independence](../../concepts/provider-independence.md) and [Model Selection](../../concepts/model-selection.md) - each branch can run a different agent or model.
- [Human in the Loop](../../concepts/human-in-the-loop.md) - the reviewer of the PRs each worktree produces.
- Realized by: [Git](./git.md), and orchestrated in [Archon](./archon.md); driven by [Claude Code](./claude-code.md), [Codex](./codex.md), [Pi](./pi-coding-agent.md).

## Sources

- [A Complete Guide to Claude Code - Here are ALL the Best Strategies](../../sources/a-complete-guide-to-claude-code-here-are-all-the-best-strategies.md) - "[0:42:44] it actually duplicates everything. So, you have a completely isolated environment in a separate branch. And then you can just change into that directory and launch cloud."
- [The Creators of Claude Code and OpenClaw don't Prompt Their Agents Anymore?!](../../sources/the-creators-of-claude-code-and-openclaw-dont-prompt-their-agents-anymore.md) - "[0:14:03] Work trees are also a really important part of loop engineering... we need to make sure they're running in isolation so they're not stepping on each other's toes."
- [Parallel Claude Code + Git Worktrees: This Setup Will Change How You Ship](../../sources/parallel-claude-code-git-worktrees-this-setup-will-change-how-you-ship.md) - "[0:05:38] if I go into doclaude work trees, we can see that we have the folder issue 10... the exact same codebase duplicated here. That is the beauty of work trees"
- [You're Hardly Using What Claude Code Has to Offer, it's Insane](../../sources/youre-hardly-using-what-claude-code-has-to-offer-its-insane.md) - "[0:04:04] we have a copy of our repo living in the.claude/workreees folder for each of our work trees. And real development is always working with feature branches and different pull requests."
- [This New Protocol Will Change AI Coding Forever (ACP)](../../sources/this-new-protocol-will-change-ai-coding-forever-acp.md) - "[0:18:39] the agent will kind of spin up its own work tree, its own environment where it will can do whatever it wants and it will come back to you with a PR"
- [I'm Building an AI Dark Factory That Ships Its Own Code (Public Experiment)](../../sources/im-building-an-ai-dark-factory-that-ships-its-own-code-public-experiment.md) - "[0:20:47] Archon gives us the work tree and isolation support so that we can manage all of these different implementations at the exact same time"
- [Omnigent: The New Meta-Harness for EVERY Coding Agent - Claude Code, Codex, Pi, More](../../sources/omnigent-the-new-meta-harness-for-every-coding-agent-claude-code-codex-pi-more.md) - "[0:05:36] I can even do work trees which are very important for parallel development."
