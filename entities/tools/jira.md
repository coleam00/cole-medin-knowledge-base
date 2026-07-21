---
type: entity
subtype: tool
title: "Jira"
description: "Example issue tracker whose scoped tickets tell the engineer (and agent) which slice of the codebase to work in."
resource: "https://www.atlassian.com/software/jira"
tags: [issue-tracking, project-management, productivity, integration]
videos: [anthropic-just-dropped-a-masterclass-on-building-agent-harnesses-for-large-codebases, full-guide-to-becoming-a-principled-agentic-engineer-build-anything-with-ai, parallel-claude-code-git-worktrees-this-setup-will-change-how-you-ship, why-is-everyone-missing-this-with-ai-agents-memory-tools-that-scale]
created: 2026-07-21
updated: 2026-07-21
---

# Jira

Jira is Atlassian's issue and project tracker, and in Cole's agentic-coding videos it plays a specific structural role: the ticket is the scoped unit of work that tells both the engineer and the agent which slice of a large codebase to touch. "If I know for example that based on a Jira ticket or GitHub issue I'm only going to be working in the API service then I can ... change my directory to that path." A well-scoped ticket is, in effect, the spec and the context boundary at once, which is why Jira keeps showing up wherever Cole talks about keeping an agent focused inside a big repo.

## How Cole uses it

Two uses recur. First, Jira as **the planning destination for AI-scoped work**. In the principled-agentic-engineer walkthrough Cole uses Claude Code to break an epic into stories and then pushes them to Jira: "I'm going to be using Jira as my place to manage all of the work that we scope out with the help of Claude code," ending with the agent asking, "do you want to push to Jira now?" The human-authored epic becomes a set of tracked tickets, and each ticket is later fed back in as the input to implementation. This is the concrete form of [The Issue Is the Spec](../../concepts/issue-is-the-spec.md) and of good [context engineering](../../concepts/context-engineering.md): the ticket both narrows scope (see [Context Isolation](../../concepts/context-isolation.md)) and carries the acceptance criteria the agent works against.

Second, Jira as **the input into parallel implementation**. In the worktrees setup Cole notes that "if you're using some kind of task management platform like Linear or Jira, the ticket is going to be the input into the implementation," so each ticket can seed its own worktree and its own agent run, the pattern he pairs with [subagents](../../concepts/subagents-pattern.md). Jira also shows up as a stock connector in agent-tooling ecosystems, listed alongside "Firecrawl or Gmail or Asauna ... or Slack or Jira, Reddit" as one of the preconfigured integrations a memory-and-tools platform ships. Cole treats Jira and [Linear](./linear.md) as interchangeable here; the choice matters less than the discipline of letting a scoped ticket, rather than a vague prompt, define the work.

## Related

- [The Issue Is the Spec](../../concepts/issue-is-the-spec.md) - a scoped Jira ticket is the unit of agentic work
- [Context Isolation](../../concepts/context-isolation.md) - the ticket bounds which service the agent touches
- [The AI Layer](../../concepts/the-ai-layer.md) - meeting teams inside the tracker they already use
- [Subagents Pattern](../../concepts/subagents-pattern.md) - one ticket per parallel agent run
- [Global Rules](../../concepts/global-rules.md)
- [Skills](../../concepts/skills.md)
- [Context Engineering](../../concepts/context-engineering.md)
- [Linear](./linear.md) - the interchangeable tracker Cole uses in the same role
- [GitHub](./github.md) - GitHub issues as the alternate ticket source

## Sources

- [Anthropic Just Dropped a Masterclass on Building Agent Harnesses (for Large Codebases)](../../sources/anthropic-just-dropped-a-masterclass-on-building-agent-harnesses-for-large-codebases.md) - "[0:07:00] If I know for example that based on a Jira ticket or GitHub issue I'm only going to be working in the API service then I can ... change my directory to that path."
- [FULL Guide to Becoming a Principled Agentic Engineer (Build Anything with AI)](../../sources/full-guide-to-becoming-a-principled-agentic-engineer-build-anything-with-ai.md) - "[0:03:20] I'm going to be using Jira as my place to manage all of the work that we scope out with the help of Claude code"
- [Parallel Claude Code + Git Worktrees: This Setup Will Change How You Ship](../../sources/parallel-claude-code-git-worktrees-this-setup-will-change-how-you-ship.md) - "[0:03:22] if you're using some kind of task management platform like Linear or Jira, the ticket is going to be the input into the implementation."
- [Why is Everyone Missing This with AI Agents?! (Memory + Tools that Scale)](../../sources/why-is-everyone-missing-this-with-ai-agents-memory-tools-that-scale.md) - "[0:08:37] they have all these preconfigured tools for things like Firecrawl or Gmail or Asauna like we saw or Slack or Jira, Reddit."
