---
type: concept
title: "Disposable Agent Sandboxes"
description: "Running each agent in an ephemeral, preloaded cloud dev box ('cattle, not pets') instead of a local worktree, so many unattended agents can run in parallel with scoped permissions."
tags: [isolation, infrastructure, parallelism, throughput]
videos: [stripes-coding-agents-ship-1300-prs-every-week-heres-how-they-do-it]
created: 2026-07-21
updated: 2026-07-21
---

# Disposable Agent Sandboxes

A disposable agent sandbox is a fresh, throwaway machine spun up for a single agent run and destroyed when that run ends. At Stripe this is literal infrastructure: "every single time a minion runs, it runs in an isolated AWS EC2 instance running in the cloud." [0:11:16] The framing that makes it work is an operations idiom borrowed from cloud infrastructure: "they call it cattle, not pets, as in these instances are not important. We can spin them up and tear them down willy-nilly" [0:11:31]. No box accumulates state, so no box is worth protecting.

## Why it matters

The sandbox is what makes unattended autonomy safe enough to attempt at volume, because "the goal with minions is to allow unattended agents to oneshot tasks." [0:04:21] An agent that nobody is watching needs a blast radius that ends at the instance boundary: it can install packages, mutate databases, and wreck its own filesystem without touching a human's machine or another agent's run. Scoped credentials on a throwaway box mean the worst case is a discarded instance rather than a compromised laptop, which is the practical answer to much of [Agent Security](./agent-security.md) and [Permission Management](./permission-management.md).

The second payoff is throughput. Local parallelism is bounded by one developer's CPU, disk, and ports; cloud sandboxes are bounded by budget. Because each instance is preloaded with the repo and toolchain, startup cost stays low enough that fan-out to many simultaneous agents is routine rather than an event, which is how a fleet reaches the volume of PRs the pattern is famous for.

## Prerequisites

- [Context Isolation](./context-isolation.md) - the sandbox is the environment-level counterpart to giving each agent its own context window.
- [Containerization & Docker Networking](./containerization.md) - the packaging discipline that makes an environment reproducible enough to throw away.

## Part of

- [Parallel Agent Execution](./parallel-agent-execution.md) - sandboxes are the substrate that lets many agents run at once.
- [Long-Running Agents](./long-running-agents.md) - unattended runs need somewhere to live that is not a developer's terminal.

## Contrasts with

- [Parallel Agentic Coding](./parallel-agentic-coding.md) and [Git Worktrees](../entities/tools/git-worktree.md) - the local answer to the same isolation problem: separate checkouts on one machine, capped by that machine.
- [Remote Agentic Coding](./remote-agentic-coding.md) - remote sessions a human drives, versus sandboxes nobody watches.

## Related

- [The Ralph Loop](./the-ralph-loop.md) and [Loop Engineering](./loop-engineering.md) - loops that only pay off when each iteration runs somewhere expendable.
- [Agentic Coding](./agentic-coding.md) - the practice this scales into a fleet.
- [Human in the Loop](./human-in-the-loop.md) - moves from mid-run supervision to PR review once runs are unattended.

## Tools

- [Stripe Minions](../entities/tools/stripe-minions.md) - the internal agent fleet that runs each task on its own EC2 instance.
- [AWS](../entities/organizations/aws.md) - EC2 provides the ephemeral instances.
- [Docker](../entities/tools/docker.md) - the usual way a sandbox image is preloaded and reproduced.
- [Omnigent](../entities/tools/omnigent.md) - Open-source meta-harness from Databricks that orchestrates multiple AI coding agents (Claude Code, Codex, Pi) from one customizable AI layer with sandboxing, guardrails, and cross-device collaboration.

## Sources

- [Stripe's Coding Agents Ship 1,300 PRs EVERY Week - Here's How They Do It](../sources/stripes-coding-agents-ship-1300-prs-every-week-heres-how-they-do-it.md) - "[0:11:16] every single time a minion runs, it runs in an isolated AWS EC2 instance running in the cloud."
- [Stripe's Coding Agents Ship 1,300 PRs EVERY Week - Here's How They Do It](../sources/stripes-coding-agents-ship-1300-prs-every-week-heres-how-they-do-it.md) - "[0:11:31] they call it cattle, not pets, as in these instances are not important. We can spin them up and tear them down willy-nilly"
- [Stripe's Coding Agents Ship 1,300 PRs EVERY Week - Here's How They Do It](../sources/stripes-coding-agents-ship-1300-prs-every-week-heres-how-they-do-it.md) - "[0:04:21] the goal with minions is to allow unattended agents to oneshot tasks."
