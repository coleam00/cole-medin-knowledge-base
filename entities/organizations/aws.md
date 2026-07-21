---
type: entity
subtype: organization
title: "AWS"
description: "Cloud provider whose EC2 instances host Stripe's isolated minion dev boxes, and which is building its own internal agentic coding tooling."
resource: "https://aws.amazon.com"
tags: [organization, cloud, agent-sandboxes, ai-coding-harness]
videos: [stripes-coding-agents-ship-1300-prs-every-week-heres-how-they-do-it]
created: 2026-07-21
updated: 2026-07-21
---

# AWS

AWS is the cloud provider that shows up in Cole's harness coverage as infrastructure rather than as a product he reviews: it is where serious coding agents actually execute. In [Stripe](./stripe.md)'s [Minions](../tools/stripe-minions.md) harness, agent work never touches an engineer's laptop, "it runs in an isolated AWS EC2 instance running in the cloud" ([0:11:16]). Each box is preloaded with the codebase and lint caching and treated as cattle rather than pets, which is the concrete implementation of [Disposable Agent Sandboxes](../../concepts/disposable-agent-sandboxes.md) and the reason one engineer can supervise many agents at once.

That choice is load-bearing for scale. Local isolation via [Git Worktrees](../tools/git-worktree.md) or containers works for a handful of parallel sessions, but it is bounded by one machine's CPU, disk, and patience. Moving the sandbox to EC2 turns [Parallel Agentic Coding](../../concepts/parallel-agentic-coding.md) into a capacity question instead of a hardware question, gives each run scoped credentials for [Agent Security](../../concepts/agent-security.md), and makes [Remote Agentic Coding](../../concepts/remote-agentic-coding.md) natural, since the agent is already in the cloud and the human is just an entry point in Slack.

AWS also appears on the other side of the ledger, as an org building the same kind of system for itself: "AWS has their own internal tooling as well that they've started to share about in a blog post" ([0:01:31]). Cole cites it alongside [Shopify](./shopify.md)'s open-source [Roast](../tools/roast.md) and Airbnb as evidence that large engineering organizations are independently converging on structured workflow engines. That convergence is the argument of the whole video: reliability at scale comes from an [AI Coding Harness](../../concepts/ai-coding-harness.md) with [Deterministic Workflows](../../concepts/deterministic-workflows.md) and real [Validation](../../concepts/validation.md) nodes, not from handing a model more autonomy.

## Works with

- [Stripe](./stripe.md) - Payments company whose Minions harness runs its agents on AWS EC2 dev boxes.
- [Stripe Minions](../tools/stripe-minions.md) - Stripe's internal agent harness that runs blueprints interweaving agent nodes with deterministic code steps.
- [Docker](../tools/docker.md) - Containerization used to preload and reproduce the agent environment.

## Contrasts with

- [Git Worktrees](../tools/git-worktree.md) - Local branch-level isolation for parallel agents; cheap to start with, but it does not scale past a single machine the way cloud dev boxes do.

## Related

- [Disposable Agent Sandboxes](../../concepts/disposable-agent-sandboxes.md) - Running each agent in an ephemeral, preloaded cloud dev box instead of a local worktree.
- [Parallel Agentic Coding](../../concepts/parallel-agentic-coding.md) - Dispatching agents to background tasks in isolated environments, each returning a reviewable PR.
- [Remote Agentic Coding](../../concepts/remote-agentic-coding.md) - Kicking off a coding request from anywhere to an agent that runs entirely remotely in an isolated container.
- [AI Coding Harness](../../concepts/ai-coding-harness.md) - The surrounding scaffolding that turns a raw model into a reliable coding system.
- [Deterministic Workflows](../../concepts/deterministic-workflows.md) - Encoding known steps as fixed code paths and reserving the LLM for the genuinely fuzzy decisions.
- [Agentic Workflow Engineering](../../concepts/agentic-workflow-engineering.md) - Designing repeatable AI workflows as engineered systems with defined steps and orchestration.
- [Containerization](../../concepts/containerization.md) - Running services and agents as containers on a private network.
- [Agent Deployment](../../concepts/agent-deployment.md) - Getting agents to production, containerizing, networking, and choosing a host.
- [Cloud GPU Hosting](../../concepts/cloud-gpu-hosting.md) - Renting GPU machines in the cloud to self-host models without owning hardware.
- [Shopify](./shopify.md) - E-commerce platform that built Roast, its own open-source AI workflow engine.
- [DigitalOcean](./digital-ocean.md) - Cloud host used elsewhere in Cole's stack for running services in the cloud.

## Sources

- [Stripe's Coding Agents Ship 1,300 PRs EVERY Week - Here's How They Do It](../../sources/stripes-coding-agents-ship-1300-prs-every-week-heres-how-they-do-it.md) - "[0:11:16] it runs in an isolated AWS EC2 instance running in the cloud."
- [Stripe's Coding Agents Ship 1,300 PRs EVERY Week - Here's How They Do It](../../sources/stripes-coding-agents-ship-1300-prs-every-week-heres-how-they-do-it.md) - "[0:01:31] AWS has their own internal tooling as well that they've started to share about in a blog post."
