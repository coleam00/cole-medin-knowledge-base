---
type: entity
subtype: tool
title: "Roast"
description: "Shopify's open-source structured AI workflow engine that combines deterministic and agentic nodes, Cole's recommended starting point for building your own harness."
resource: "https://github.com/Shopify/roast"
tags: [agent-framework, sdk]
videos: [stripes-coding-agents-ship-1300-prs-every-week-heres-how-they-do-it]
created: 2026-07-21
updated: 2026-07-21
---

# Roast

Roast is [Shopify](../organizations/shopify.md)'s in-house engine for running structured AI coding workflows, and the rare one you can actually read: "Shopify, they created their own structured AI workflow engine as well called Roast. They actually open sourced this" [0:01:22]. It belongs to the same generation of company-built [harnesses](../../concepts/ai-coding-harness.md) as [Stripe Minions](./stripe-minions.md) and Airbnb's test-migration tooling - internal systems built because raw prompting of a coding agent does not survive contact with a large codebase and a real release process.

The design principle Roast encodes is that reliability comes from boxing the model in. Rather than one agent free-running to a goal, a workflow is a graph of nodes where deterministic steps and agentic steps are separate kinds of node, so each LLM call has a narrow job with defined inputs and outputs. Cole's framing of why this works across all of these companies: "putting LLMs in contained boxes like having separate nodes for the agents separate for deterministic steps it compounds into systemwide reliability upside" [0:14:02]. That is the [agents vs. workflows](../../concepts/agents-vs-workflows.md) tradeoff resolved in favor of structure, with validation baked into the graph instead of remembered by the human between sessions.

Its practical value to you is as a reference implementation. Minions is closed, so Roast is the one you can open: "use Roast by Shopify as an example. So, Stripe Minions is unfortunately not open source, but Shopify did open source their version" [0:16:42]. Cole recommends starting from its quick starts, which show workflows mixing deterministic nodes with non-deterministic agentic ones, and even feeding the repository to your coding assistant as context while you build your own version.

Roast is also the explicit model for where [Archon](./archon.md) is heading. Cole describes his overhaul as "basically what Shopify roast in Stripe Minions is - a place for us to run these workflows in parallel" [0:17:46], with observability, logs, and a visual workflow builder on top: "it's basically like Minions and Roast, but you can even define your workflows in a beautiful UI" [0:18:04].

## Realizes

- [Deterministic Workflows](../../concepts/deterministic-workflows.md) - Encoding known steps as fixed code paths and reserving the LLM for the genuinely fuzzy decisions, trading autonomy for reliability.
- [AI Coding Harness](../../concepts/ai-coding-harness.md) - The surrounding scaffolding (prompts, tools, rules, validation) that turns a raw model into a reliable coding system.
- [Agentic Workflow Engineering](../../concepts/agentic-workflow-engineering.md) - Designing repeatable AI workflows as engineered systems with defined steps, orchestration, and background execution rather than ad-hoc prompting.
- [Validation](../../concepts/validation.md) - Building explicit checks into agentic workflows so the AI verifies its own output against real success criteria before moving on.
- [Parallel Agent Execution](../../concepts/parallel-agent-execution.md) - Running multiple agents or agent steps concurrently to cut wall-clock time on a task.
- [Open Source AI Coding](../../concepts/open-source-ai-coding.md) - Community-maintained, self-hostable AI coding tools that dodge API costs and rate limits.

## Contrasts with

- [Agents vs. Workflows](../../concepts/agents-vs-workflows.md) - An agent lets the LLM non-deterministically control which tools run, whereas a workflow chains a fixed sequence of steps; Roast picks the workflow side.
- [Stripe Minions](./stripe-minions.md) - Stripe's equivalent structured workflow harness, shipping 1,300 PRs a week but closed source.

## Works with

- [Archon](./archon.md) - Cole's free, open-source AI command center, being rebuilt into the same kind of parallel workflow runner with a visual builder.
- [Claude Agent SDK](./claude-agent-sdk.md) - The engine that powers Claude Code, exposed as a library so you can build these structured workflows on top of the same harness.

## Related

- [Meta-Harness](../../concepts/meta-harness.md) - A layer above individual AI coding assistants that orchestrates many of them together on larger tasks.
- [Docs as Agent Context](../../concepts/docs-as-agent-context.md) - Feeding proven reference implementations to a coding assistant so it builds from real context; Cole suggests doing exactly this with the Roast repo.
- [Shopify](../organizations/shopify.md) - E-commerce platform that built and open sourced Roast.
- [Stripe](../organizations/stripe.md) - Payments company whose Minions harness is Cole's headline example of this pattern at scale.

## Sources

- [Stripe's Coding Agents Ship 1,300 PRs EVERY Week - Here's How They Do It](../../sources/stripes-coding-agents-ship-1300-prs-every-week-heres-how-they-do-it.md) - "[0:01:22] Shopify, they created their own structured AI workflow engine as well called Roast. They actually open sourced this."
- [Stripe's Coding Agents Ship 1,300 PRs EVERY Week - Here's How They Do It](../../sources/stripes-coding-agents-ship-1300-prs-every-week-heres-how-they-do-it.md) - "[0:16:42] use Roast by Shopify as an example. So, Stripe Minions is unfortunately not open source, but Shopify did open source their version"
