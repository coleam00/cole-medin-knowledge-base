---
type: entity
subtype: tool
title: "Stripe Minions"
description: "Stripe's internal agent harness that runs 'blueprints' interweaving agent nodes with deterministic code steps, shipping 1,300+ fully AI-written PRs every week."
tags: [ai-coding, coding-agent]
videos: [stripes-coding-agents-ship-1300-prs-every-week-heres-how-they-do-it]
created: 2026-07-21
updated: 2026-07-21
---

# Stripe Minions

Stripe Minions is Stripe's internal agent harness for delegated coding work: "for anything that they want to just try to have the agent knock out like a GitHub issue, they just want to send off some requests in Slack. That is what Stripe Minions is for" ([0:04:41]). An engineer files a request from [Slack](./slack.md) (or the CLI), a minion picks it up, and the output is a pull request a human reviews but did not write. At the time Cole covered it, Minions was shipping over 1,300 completely AI-authored PRs every week.

The unit of execution is a blueprint: "the core idea behind Stripe Minions that I'll show in my diagram as well is blueprints" ([0:05:23]). A blueprint is a fixed graph where some nodes are agent loops and the rest are ordinary code, so the system controls the agent rather than the reverse. A deterministic context-curation node runs first, calling [MCP](./mcp.md) tools programmatically to pull the ticket and docs and to select a small slice of capabilities out of "tool shed," a single internal MCP server holding roughly 500 tools. Implementation happens on isolated, disposable EC2 dev boxes preloaded with the codebase and lint caches. A deterministic validation node then runs linting, type-checking, and a targeted portion of a 3M+ test suite, forcing retries on failure and escalating to a human after two loops. Nothing is vibe coded.

Cole's point in covering it is that this is the enterprise-scale version of the pattern any individual can run: plan, implement in a fresh context, validate deterministically, then review. [Archon](./archon.md) and Shopify's [Roast](./roast.md) are the equivalents you can actually pick up and use.

## Realizes

- [AI Coding Harness](../../concepts/ai-coding-harness.md) - The scaffolding of prompts, tools, rules, and validation that turns a raw model into a reliable coding system.
- [Deterministic Workflows](../../concepts/deterministic-workflows.md) - Encoding known steps as fixed code paths and reserving the LLM for the genuinely fuzzy decisions.
- [Agentic Workflow Engineering](../../concepts/agentic-workflow-engineering.md) - Designing repeatable AI workflows as engineered systems with defined steps and orchestration.
- [Agents vs. Workflows](../../concepts/agents-vs-workflows.md) - A blueprint is a fixed graph of steps, not an agent loop deciding its own tool calls.
- [Disposable Agent Sandboxes](../../concepts/disposable-agent-sandboxes.md) - Ephemeral, preloaded cloud dev boxes ('cattle, not pets') so many unattended agents run in parallel.
- [Validation](../../concepts/validation.md) - Explicit checks the workflow must pass before work moves forward.
- [The PIV Loop](../../concepts/the-piv-loop.md) - The plan, implement, validate cycle Cole extrapolates from Minions for individual engineers.
- [The Issue Is the Spec](../../concepts/issue-is-the-spec.md) - A GitHub issue dropped into Slack is the whole specification a minion implements against.

## Contrasts with

- [Claude Code](./claude-code.md) - A general-purpose agent you steer interactively, where the agent controls the process rather than a fixed graph.
- [Roast](./roast.md) - Shopify's open-source AI workflow engine, the closest thing to Minions you can actually run.
- [Archon](./archon.md) - Cole's open-source harness builder, positioned as an 'n8n for AI coding' for these same parallel workflows.

## Works with

- [MCP (Model Context Protocol)](./mcp.md) - Tool shed exposes ~500 internal tools through one MCP server; a subset is selected per request in code.
- [Slack](./slack.md) - The primary entry point where engineers dispatch minion requests.
- [GitHub](./github.md) - Issues in, reviewed pull requests out.

## Related

- [Stripe](../organizations/stripe.md) - The payments company that built and runs Minions internally.
- [Shopify (Toby Lutke)](../organizations/shopify.md) - Another large company building a structured AI workflow engine, in its case the open-source Roast.
- [Context Engineering](../../concepts/context-engineering.md) - The deterministic curation node exists purely to control what enters the agent's window.
- [Context Isolation](../../concepts/context-isolation.md) - Each blueprint node gets only the context its job requires.
- [Parallel Agentic Coding](../../concepts/parallel-agentic-coding.md) - One engineer running many minions at once is the throughput story.
- [Human in the Loop](../../concepts/human-in-the-loop.md) - Humans review every PR and take over after two failed fix loops.
- [AWS](../organizations/aws.md) - Cloud provider whose EC2 instances host Stripe's isolated minion dev boxes, and which is building its own internal agentic coding tooling.

## Sources

- [Stripe's Coding Agents Ship 1,300 PRs EVERY Week - Here's How They Do It](../../sources/stripes-coding-agents-ship-1300-prs-every-week-heres-how-they-do-it.md) - "[0:04:41] for anything that they want to just try to have the agent knock out like a GitHub issue, they just want to send off some requests in Slack. That is what Stripe Minions is for."
