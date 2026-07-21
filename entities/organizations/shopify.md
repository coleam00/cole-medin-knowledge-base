---
type: entity
subtype: organization
title: "Shopify"
description: "E-commerce platform whose CEO Toby Lütke framed context engineering vs. prompt engineering (a framing Karpathy endorsed); also built its own AI workflow engine, Roast."
resource: "https://shopify.com"
tags: [organization, context-engineering, workflow-engine, ecommerce]
videos: [context-engineering-is-the-new-vibe-coding-learn-this-now, stripes-coding-agents-ship-1300-prs-every-week-heres-how-they-do-it, get-qualified-leads-while-you-sleep-with-ai]
created: 2026-07-21
updated: 2026-07-21
---

# Shopify

Shopify is the e-commerce platform company that appears in Cole's videos less as a store builder and more as a source of two ideas about AI engineering: a framing of context engineering, and a homegrown workflow engine. Its clearest role is the origin of the phrase Andrej Karpathy amplified: "This is his response to a tweet from Toby, the CEO of Shopify, where he's comparing context engineering to prompt engineering" ([0:02:21]). That tweet by Toby Lütke, endorsed by Karpathy, is the moment Cole points to for why [Context Engineering](../../concepts/context-engineering.md) supersedes plain prompt wording.

Shopify also shows up as one of the companies that, like [Stripe](./stripe.md), stopped waiting for off-the-shelf tooling and built its own: "Shopify, they created their own structured AI workflow engine as well called Roast" ([0:01:22]). Roast is Cole's evidence that serious teams treat coding agents as something to orchestrate with [Deterministic Workflows](../../concepts/deterministic-workflows.md) and [Agentic Workflow Engineering](../../concepts/agentic-workflow-engineering.md), not just prompt ad hoc. It sits in the same category as an [AI Coding Harness](../../concepts/ai-coding-harness.md): structured curation, [Validation](../../concepts/validation.md), and repeatable execution.

A third, lighter role: Shopify is a common integration target for the business automations Cole demos, alongside WordPress and Wix ([0:13:13]). Here it is just an external commerce backend an agent workflow plugs into, not a subject in itself.

## Realizes

- [Context Engineering](../../concepts/context-engineering.md) - The deliberate practice of curating exactly what goes into an LLM's limited context window - system messages, schemas, chat history, and dynamic variables - to avoid overload and keep outputs sharp.
- [Agentic Workflow Engineering](../../concepts/agentic-workflow-engineering.md) - Designing repeatable AI workflows as engineered systems with defined steps, orchestration, and background execution rather than ad-hoc prompting.
- [Deterministic Workflows](../../concepts/deterministic-workflows.md) - Encoding known steps as fixed code paths and reserving the LLM for the genuinely fuzzy decisions, trading autonomy for reliability.
- [AI Coding Harness](../../concepts/ai-coding-harness.md) - The surrounding scaffolding (prompts, tools, rules, validation) that turns a raw model into a reliable coding system.

## Related

- [Roast](../tools/roast.md) - Shopify's open-source structured AI workflow engine that combines deterministic and agentic nodes, Cole's recommended starting point for building your own harness.
- [Validation](../../concepts/validation.md) - Building explicit checks into agentic workflows so the AI verifies its own output against real success criteria before moving on.
- [RAG](../../concepts/rag.md) - Grounding an LLM's answers by retrieving relevant documents from an external knowledge base and injecting them into the prompt at query time.
- [Andrej Karpathy](../people/andrej-karpathy.md) - AI engineer who coined 'vibe coding' in February 2025 and popularized the LLM-built personal knowledge base (the 'Karpathy LLM Wiki').
- [Stripe](./stripe.md) - Payments company that is Cole's headline example of an AI coding harness at scale (1,300 AI-generated PRs per week via Stripe Minions); also the external payments API agents integrate and call.

## Sources

- [Context Engineering is the New Vibe Coding (Learn this Now)](../../sources/context-engineering-is-the-new-vibe-coding-learn-this-now.md) - "[0:02:21] This is his response to a tweet from Toby, the CEO of Shopify, where he's comparing context engineering to prompt engineering."
- [Stripe's Coding Agents Ship 1,300 PRs EVERY Week - Here's How They Do It](../../sources/stripes-coding-agents-ship-1300-prs-every-week-heres-how-they-do-it.md) - "[0:01:22] Shopify, they created their own structured AI workflow engine as well called Roast."
- [Get Qualified Leads While you Sleep with AI](../../sources/get-qualified-leads-while-you-sleep-with-ai.md) - "[0:13:13] they have a couple of different integration guides for things like Shopify or WordPress or Wix."
