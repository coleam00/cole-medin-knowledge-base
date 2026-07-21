---
type: entity
subtype: organization
title: "Stripe"
description: "Payments company that is Cole's headline example of an AI coding harness at scale (1,300 AI-generated PRs per week via Stripe Minions); also the external payments API agents integrate and call."
resource: "https://stripe.com"
tags: [organization, ai-coding-harness, dark-factory, payments-api]
videos: [the-next-evolution-of-ai-coding-is-harnesses-heres-how-to-build-them, stripes-coding-agents-ship-1300-prs-every-week-heres-how-they-do-it, the-best-ai-coding-setup-isnt-the-most-autonomous-one-heres-why, claude-sonnet-45-the-new-coding-king-sonnet-45-vs-gpt-5-codex, ai-agents-the-future-of-ai-or-a-passing-fad, use-chatgpt-in-two-clicks-on-any-website-with-a-custom-chrome-extension]
created: 2026-07-21
updated: 2026-07-21
---

# Stripe

Stripe is the payments company Cole cites more than any other as proof that engineered harnesses beat raw autonomy: "Stripe, they ship 1,300 AI only generated pull requests every single week. And they did this by building their AI coding workflow, their context curation, their validation" ([0:05:13]). It is his canonical real-world case for the [AI Coding Harness](../../concepts/ai-coding-harness.md): a serious engineering org getting massive throughput not by handing an agent free rein, but by wrapping it in [Deterministic Workflows](../../concepts/deterministic-workflows.md), curated context, and [Validation](../../concepts/validation.md).

What makes the example convincing is the difficulty of the target. Stripe's codebase is hostile to naive agents: "Stripe, it has a very complicated codebase. They have a backend written in Ruby. It's an uncommon stack" ([0:00:33]). And the AI output is a fraction of a much larger human org: "Stripe does have over 3,400 engineers. They are shipping over 8,000 pull requests every week" ([0:04:02]). Cole names the internal harness itself, "Stripe Minions" ([0:20:16]), as the kind of [Agentic Workflow Engineering](../../concepts/agentic-workflow-engineering.md) that keeps a [Human in the Loop](../../concepts/human-in-the-loop.md) while still scaling. It sits alongside [StrongDM](./strongdm.md) as a company running something close to a [Dark Factory](../../concepts/dark-factory.md), and alongside [Shopify](./shopify.md) as one that built its own workflow engine.

Stripe plays a second, unrelated role: the stand-in external API in agent demos. Cole uses it as the example service an agent calls ("use the stripe API to fetch an expense," [0:04:12]), as the integration target in a head-to-head build ("build a Stripe integration into an existing agentic application," [0:02:20]) that ends at a real "Stripe checkout" ([0:06:31]), and as the obvious way to monetize a tool ("integrate it with something like stripe for credit card payments," [0:21:00]).

## Realizes

- [AI Coding Harness](../../concepts/ai-coding-harness.md) - The surrounding scaffolding (prompts, tools, rules, validation) that turns a raw model into a reliable coding system.
- [Agentic Workflow Engineering](../../concepts/agentic-workflow-engineering.md) - Designing repeatable AI workflows as engineered systems with defined steps, orchestration, and background execution rather than ad-hoc prompting.
- [Deterministic Workflows](../../concepts/deterministic-workflows.md) - Encoding known steps as fixed code paths and reserving the LLM for the genuinely fuzzy decisions, trading autonomy for reliability.

## Related

- [Validation](../../concepts/validation.md) - Building explicit checks into agentic workflows so the AI verifies its own output against real success criteria before moving on.
- [Human in the Loop](../../concepts/human-in-the-loop.md) - Keeping a human as the approver and steerer of agentic work rather than fully automating, so AI augments engineers instead of replacing them.
- [The PIV Loop](../../concepts/the-piv-loop.md) - Cole's core agentic-coding cycle of Plan, Implement, Validate that structures every unit of AI-driven work.
- [Dark Factory](../../concepts/dark-factory.md) - A self-evolving codebase where autonomous workflows build and improve a product with minimal human touch.
- [StrongDM](./strongdm.md) - Company that went viral for running a dark factory shipping thousands of lines of production code no human writes or reviews; source of the hold-out pattern Cole adopts for reliability.
- [Shopify](./shopify.md) - E-commerce platform whose CEO Toby Lütke framed context engineering vs. prompt engineering (a framing Karpathy endorsed); also built its own AI workflow engine, Roast.
- [Model Selection](../../concepts/model-selection.md) - Choosing the right LLM per task by trading off quality, speed, and cost, often routing easy requests to cheap models and hard ones to expensive models.

## Sources

- [The Next Evolution of AI Coding Is Harnesses - Here's How to Build Them](../../sources/the-next-evolution-of-ai-coding-is-harnesses-heres-how-to-build-them.md) - "[0:05:13] Stripe, they ship 1,300 AI only generated pull requests every single week. And they did this by building their AI coding workflow, their context curation, their validation."
- [Stripe's Coding Agents Ship 1,300 PRs EVERY Week - Here's How They Do It](../../sources/stripes-coding-agents-ship-1300-prs-every-week-heres-how-they-do-it.md) - "[0:04:02] Stripe does have over 3,400 engineers. They are shipping over 8,000 pull requests every week."
- [The Best AI Coding Setup Isn't the Most Autonomous One (Here's Why)](../../sources/the-best-ai-coding-setup-isnt-the-most-autonomous-one-heres-why.md) - "[0:20:16] just the idea of engineering harnesses to drive these things like what Stripe did with Stripe Minions."
- [Claude Sonnet 4.5 - The New Coding King? (Sonnet 4.5 vs. GPT 5 Codex)](../../sources/claude-sonnet-45-the-new-coding-king-sonnet-45-vs-gpt-5-codex.md) - "[0:02:20] Executing on the exact same requirements document that I have to build a Stripe integration into an existing agentic application."
- [AI Agents: The Future of AI or a Passing Fad?](../../sources/ai-agents-the-future-of-ai-or-a-passing-fad.md) - "[0:04:12] or use the stripe API to fetch an expense it won't necessarily do that."
- [Use ChatGPT in Two Clicks on ANY website with a Custom Chrome Extension](../../sources/use-chatgpt-in-two-clicks-on-any-website-with-a-custom-chrome-extension.md) - "[0:21:00] if you want people to pay for it you'll have to integrate it with something like stripe for credit card payments."
