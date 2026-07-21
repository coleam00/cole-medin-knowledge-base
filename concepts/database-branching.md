---
type: concept
title: "Database Branching"
description: "Giving each git worktree its own isolated copy of the database (a Neon branch or local SQLite DB) so parallel coding agents' schema and data changes don't collide - database isolation as the counterpart to worktree code isolation."
tags: [database, isolation, parallel-development]
videos: [parallel-claude-code-git-worktrees-this-setup-will-change-how-you-ship]
created: 2026-07-21
updated: 2026-07-21
---

# Database Branching

Database branching gives every parallel agent its own database, the same way a git worktree gives it its own copy of the code. It exists because worktrees only solve half the collision problem: "if different feature implementations are changing the database, we will actually break different work trees if they're all pointing to the same database... we need something like a work tree for the database as well" [0:17:36]. Three agents running migrations against one shared instance will corrupt each other's schema, seed data, and test runs no matter how cleanly their branches are separated.

The fix mirrors git exactly: "We have our main production database and then we have a special branch for each one of the work trees. So we essentially have not just codebase isolation with work trees but now we have database isolation as well" [0:18:56]. A branch is a copy-on-write fork of the real schema and data, cheap enough to create per worktree and disposable when the branch merges or is thrown away. Managed Postgres with a branching feature does this natively; for smaller projects, a per-worktree local database file achieves the same isolation with no infrastructure at all.

The operational discipline is what makes it work: create the branch when the worktree is created, point that worktree's connection string at it, and delete both together. Agents then run migrations, wipe tables, and seed fixtures freely, because the blast radius stops at their own branch. Without it, parallel agentic coding degrades into serialized work whenever a task touches the schema - which, for most real feature work, is most of the time.

## Part of

- [Parallel Agentic Coding](./parallel-agentic-coding.md) - the workflow this completes; worktrees isolate code, branches isolate state.

## Prerequisites

- [Parallel Agent Execution](./parallel-agent-execution.md) - running several agents at once is what creates the collision in the first place.

## Contrasts with

- [Disposable Agent Sandboxes](./disposable-agent-sandboxes.md) - isolating the whole environment per agent, versus isolating just the data layer.
- [Containerization & Docker Networking](./containerization.md) - process-level isolation that does not by itself separate persistent state.

## Related

- [End-to-End Validation](./end-to-end-validation.md) - each branch gives an agent a real database to validate against rather than mocks.
- [Agent Teams](./agent-teams.md) - concurrent agents in one repo need the same state separation.
- [Code Review](./code-review.md) - a branch's schema changes are reviewed alongside its diff before merging back.
- [Dark Factory](./dark-factory.md) and [Agentic Workflow Engineering](./agentic-workflow-engineering.md) - automated dispatch that must provision and tear down isolation per run.
- [Test-Driven Development](./test-driven-development.md) - isolated data is what makes per-branch test runs trustworthy.

## Tools

- [Git Worktrees](../entities/tools/git-worktree.md) - the code-side isolation this pairs with one-to-one.
- [Neon](../entities/tools/neon.md) - managed Postgres whose branching feature makes a per-worktree database cheap.
- [SQLite](../entities/tools/sqlite.md) - the zero-infrastructure version: one database file per worktree.
- [Postgres](../entities/tools/postgres-pgvector.md) - the production database the branches fork from.

## Sources

- [Parallel Claude Code + Git Worktrees: This Setup Will Change How You Ship](../sources/parallel-claude-code-git-worktrees-this-setup-will-change-how-you-ship.md) - "[0:17:36] if different feature implementations are changing the database, we will actually break different work trees if they're all pointing to the same database... we need something like a work tree for the database as well."
- [Parallel Claude Code + Git Worktrees: This Setup Will Change How You Ship](../sources/parallel-claude-code-git-worktrees-this-setup-will-change-how-you-ship.md) - "[0:18:56] We have our main production database and then we have a special branch for each one of the work trees. So we essentially have not just codebase isolation with work trees but now we have database isolation as well."
