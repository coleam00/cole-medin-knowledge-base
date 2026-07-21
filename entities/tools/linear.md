---
type: entity
subtype: tool
title: "Linear"
description: "Project/issue tracker Cole used in place of the local file system to track a harness's feature list and progress, adding human-in-the-loop where teams already work."
resource: "https://linear.app"
tags: [issue-tracking, project-management, productivity, integration]
videos: [full-guide-to-becoming-a-principled-agentic-engineer-build-anything-with-ai, parallel-claude-code-git-worktrees-this-setup-will-change-how-you-ship, turn-claude-code-into-your-full-engineering-team-with-subagents, are-agent-harnesses-bringing-back-vibe-coding]
created: 2026-07-21
updated: 2026-07-21
---

# Linear

Linear is a fast, developer-focused issue and project tracker, and in Cole's harness videos it earns a distinctive role: he swaps it in for the local file system as an agent's source of truth for a feature list and its progress. Describing his own modified harness, he says, "I even made my own version where I'm using linear as the place to track the task progression instead of using the local file system like they do." Moving state out of scratch files and into a tracker means the plan lives where a team already works, so a human can watch, comment, and intervene while the agent grinds through the backlog.

## How Cole uses it

The defining move is **Linear as the harness's source of truth**. Rather than let the agent keep its task list in local markdown, Cole points the harness at Linear: "Linear is our source of truth instead of these local files." In one build the harness planned the whole project into the tracker, "Using the harness to build this, it decided to create 44 tasks in total in linear," then worked them one by one. He also wires up a **meta task** that the agent narrates against over a long run: "the cloud progress I turned into this more like meta task that I have in linear. So it like updates this over time and makes comments as it goes through each of the sessions." That running commentary is a lightweight [human-in-the-loop](../../concepts/human-in-the-loop.md) and observability surface, you can read where the agent is without stopping it.

The second theme is **Linear as the input into implementation**, the same point Cole makes about [Jira](./jira.md): "if you're using some kind of task management platform like Linear or Jira, the ticket is going to be the input into the implementation." A well-formed ticket is the spec ([The Issue Is the Spec](../../concepts/issue-is-the-spec.md)) and the context boundary ([Context Isolation](../../concepts/context-isolation.md)) that keeps each agent, often a [subagent](../../concepts/subagents-pattern.md), focused on one slice of work. He is explicit that the MCP integration is the plumbing: "you're going to use the GitHub CLI to create issues instead of the Jira MCP server or you're going to use the linear MCP server." The larger idea is [The AI Layer](../../concepts/the-ai-layer.md), agents that meet a team inside the tools it already runs rather than forcing new ones.

## Realizes

- [The Issue Is the Spec](../../concepts/issue-is-the-spec.md) - Treating a well-written ticket or issue as the complete specification the agent implements against.
- [The AI Layer](../../concepts/the-ai-layer.md) - The layer of rules, commands, skills, and context you own on top of a codebase that makes AI coding effective and portable.

## Contrasts with

- [Jira](./jira.md) - Example issue tracker whose scoped tickets tell the engineer (and agent) which slice of the codebase to work in.
- [GitHub](./github.md) - The gh command-line tool that lets Claude Code manage issues and pull requests directly on a remote GitHub repository.

## Related

- [Context Isolation](../../concepts/context-isolation.md) - Giving each agent or subagent its own clean context window so unrelated tokens never dilute the task at hand.
- [Subagents Pattern](../../concepts/subagents-pattern.md) - Delegating scoped tasks to isolated subagents to parallelize work and protect the main agent's context window.
- [PRD-First Development](../../concepts/prd-first-development.md) - Starting every build from a written product requirements document that becomes the contract the agent implements against.
- [Context Engineering](../../concepts/context-engineering.md) - The deliberate practice of curating exactly what goes into an LLM's limited context window - system messages, schemas, chat history, and dynamic variables - to avoid overload and keep outputs sharp.

## Sources

- [Are Agent Harnesses Bringing Back Vibe Coding?](../../sources/are-agent-harnesses-bringing-back-vibe-coding.md) - "[0:15:27] I even made my own version where I'm using linear as the place to track the task progression instead of using the local file system like they do."
- [Turn Claude Code into Your Full Engineering Team with Subagents](../../sources/turn-claude-code-into-your-full-engineering-team-with-subagents.md) - "[0:13:10] Linear is our source of truth instead of these local files."
- [FULL Guide to Becoming a Principled Agentic Engineer (Build Anything with AI)](../../sources/full-guide-to-becoming-a-principled-agentic-engineer-build-anything-with-ai.md) - "[0:30:10] you're going to use the GitHub CLI to create issues instead of the Jira MCP server or you're going to use the linear MCP server"
- [Parallel Claude Code + Git Worktrees: This Setup Will Change How You Ship](../../sources/parallel-claude-code-git-worktrees-this-setup-will-change-how-you-ship.md) - "[0:03:22] if you're using some kind of task management platform like Linear or Jira, the ticket is going to be the input into the implementation."
