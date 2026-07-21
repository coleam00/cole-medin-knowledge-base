---
type: source
title: "Stripe's Coding Agents Ship 1,300 PRs EVERY Week - Here's How They Do It"
description: "Stripe ships 1,300+ fully AI-written PRs weekly by building an internal agent harness (Minions) that interweaves non-deterministic agent nodes with deterministic code steps, and you can extrapolate the same pattern into a simple plan-implement-validate loop yourself."
youtube_id: NMWgXvm--to
url: https://www.youtube.com/watch?v=NMWgXvm--to
slug: stripes-coding-agents-ship-1300-prs-every-week-heres-how-they-do-it
published: 2026-03-11
duration: "0:18:51"
recency_rank: 28
raw: "../raw/stripes-coding-agents-ship-1300-prs-every-week-heres-how-they-do-it.md"
tags: [agentic-workflow-engineering, harness, deterministic-workflows, enterprise]
created: 2026-07-21
updated: 2026-07-21
---

# Stripe's Coding Agents Ship 1,300 PRs EVERY Week - Here's How They Do It

Cole breaks down Stripe's internal agent harness, 'Minions,' which now ships over 1,300 completely AI-written pull requests every week (humans review but write none of the code). The core lesson is architectural: reliability at Stripe's scale comes not from giving agents more autonomy but from a system that controls the agent. Minions runs 'blueprints', fixed workflow graphs where some nodes are agent loops and others are deterministic code (linting, type-checking with Sorbet, running a slice of the 3M+ test suite). The system forces retries when validation fails and escalates to a human after a capped number of loops, so the agent never controls the overall process.

Stripe's workflow starts from an entry point (usually Slack, sometimes CLI), then runs a deterministic context-curation node that uses MCP tools in code to pull relevant tickets and docs and to select a small subset of capabilities from 'tool shed' (a single internal MCP server with ~500 tools). Agent execution happens inside isolated, disposable AWS EC2 dev boxes ('cattle, not pets') preloaded with the codebase and lint caching, which scale better than laptop worktrees/containers and enable one engineer to run many minions in parallel. After implementation, deterministic validation runs a targeted portion of the test suite, iterating with the agent a maximum of two times before escalating to human review, never vibe coding.

Cole then generalizes the pattern. Larger companies (Shopify's open-source Roast, Airbnb, AWS) are all building structured AI workflow engines because putting LLMs in contained boxes with separate deterministic steps compounds into system-wide reliability and saves tokens. The extrapolation is his PIV loop: plan in one session, cut the context window, implement in a fresh focused agent, then add a deterministic validation node before human review and merge. He points viewers to Roast as an open-source starting point, a Dynamous workshop, and teases that Archon is becoming his own 'n8n for AI coding', a UI-driven engine to run these parallel workflows with observability.

## Concepts covered

- [AI Coding Harness](../concepts/ai-coding-harness.md)
- [Deterministic Workflows](../concepts/deterministic-workflows.md)
- [Agentic Workflow Engineering](../concepts/agentic-workflow-engineering.md)
- [Context Engineering](../concepts/context-engineering.md)
- [Validation](../concepts/validation.md)
- [The PIV Loop](../concepts/the-piv-loop.md)
- [Context Isolation](../concepts/context-isolation.md)
- [Parallel Agentic Coding](../concepts/parallel-agentic-coding.md)
- [Human in the Loop](../concepts/human-in-the-loop.md)
- [MCP (Model Context Protocol)](../entities/tools/mcp.md)

## Entities

- [Stripe](../entities/organizations/stripe.md)
- [Shopify (Toby Lutke)](../entities/organizations/shopify.md)
- [Archon](../entities/tools/archon.md)
- [Postman](../entities/tools/postman.md)
- [Claude Code](../entities/tools/claude-code.md)
- [Slack](../entities/tools/slack.md)
- [Dynamous](../entities/organizations/dynamous.md)
- [Cole Medin](../entities/people/cole-medin.md)

## Key moments

- **[0:00:00]** Stripe ships 1,300+ fully AI-written PRs weekly via its internal harness Minions
- **[0:01:22]** Other big companies building structured AI workflow engines: Shopify (Roast, open source), Airbnb, AWS
- **[0:02:44]** Core pattern: the system controls the agent, not the reverse, deterministic nodes force retries
- **[0:05:23]** Blueprints: collections of agent skills interwoven with deterministic code
- **[0:05:40]** Workflow vs agent, fixed graph of steps vs a loop deciding tool calls in real time
- **[0:07:29]** Deterministic context-curation node runs before the agent; MCP tools used in code
- **[0:08:00]** Tool shed, single Stripe MCP server with ~500 tools; a subset is selected per request
- **[0:11:16]** Agents run in isolated, disposable AWS EC2 dev boxes (cattle not pets) for scale/permissioning
- **[0:12:03]** Deterministic test node runs a slice of 3M+ tests; max two fix loops then escalate to human
- **[0:14:35]** Extrapolation to the PIV loop across separate coding sessions with a validation node
- **[0:17:46]** Archon teased as an n8n-for-AI-coding engine to run these workflows in parallel with observability

## Transcript

[Raw transcript](../raw/stripes-coding-agents-ship-1300-prs-every-week-heres-how-they-do-it.md)
