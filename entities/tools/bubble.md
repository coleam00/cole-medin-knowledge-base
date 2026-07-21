---
type: entity
subtype: tool
title: "Bubble"
description: "Popular no-code app builder Cole criticizes for 'workload unit' usage-based pricing that makes AI app costs unpredictable and ruinous at scale."
resource: "https://bubble.io"
tags: [no-code, app-builder]
videos: [bubble-is-my-biggest-regret-for-no-code-ai-apps-what-i-use-instead]
created: 2026-07-21
updated: 2026-07-21
---

# Bubble

Bubble is one of the best-known no-code app builders, a visual canvas for assembling a database, a front end, and workflows without writing code, and it is where most non-developers land the moment they want to ship a generative-AI product. Cole names it as exactly that default, and then names the catch: "they just go to one of the more popular app builders that are starting to integrate with generative AI like bubble I'm sure you've heard of bubble before but here is the big problem with these platforms they have a ton of hidden fees" ([0:00:31](../../sources/bubble-is-my-biggest-regret-for-no-code-ai-apps-what-i-use-instead.md)).

The hidden fee has a name: **workload units**. Bubble meters the application rather than the seat. Every database request, every API call, every page load spends units, and once a plan's allowance is gone you pay roughly 30 cents per 1,000 operations. A single page reload can burn around ten cents. That structure is fine for a demo and brutal for anything with real users, because an AI app is exactly the kind of app that fans out into many operations per interaction: a chat turn hits the database, calls the model, calls a tool, writes back. The bill therefore tracks usage instead of value, and it is unknowable in advance. Cole cites a competitor test to make the gap concrete: "something they were able to do really really quickly on moment took a minute and 18 seconds and $155 on bubble" ([0:04:23](../../sources/bubble-is-my-biggest-regret-for-no-code-ai-apps-what-i-use-instead.md)).

His objection is to the meter, not to no-code itself. The alternative he reaches for is a platform priced on fixed infrastructure (cores, memory, storage) where cost is flat no matter how hard users hammer the app, and where the agent and the front end live in one place so a [full-stack AI application](../../concepts/full-stack-ai-application.md) does not need two vendors. Bubble is the cautionary anchor of that argument, and Cole generalizes it into a rule for evaluating any service: prefer predictable infrastructure pricing over per-operation metering.

## Realizes

- [Usage-Based Pricing Trap](../../concepts/usage-based-pricing-trap.md) - Metering a no-code app per database or API operation makes costs unpredictable and explode at scale; Bubble's workload units are the canonical example.
- [No-Code AI Agents](../../concepts/no-code-agents.md) - Building functional AI agents by wiring nodes on a visual canvas instead of writing code.
- [Full-Stack AI Application](../../concepts/full-stack-ai-application.md) - Combining an AI agent with a real front end, database, and API integrations in one product.

## Contrasts with

- [n8n](./n8n.md) - The no-code automation platform Cole self-hosts, where the cost is the box you run it on rather than a per-operation meter.
- [Lovable](./lovable.md) - AI app builder he uses for front ends, generated from prompts rather than assembled on a drag-and-drop canvas.

## Related

- [LLM Cost Optimization](../../concepts/llm-cost-optimization.md) - Cutting the bill for running LLM applications at scale, the same instinct applied to the model layer.
- [Buy vs. Build](../../concepts/buy-vs-build.md) - When leaning on an existing platform beats building it yourself, and what the platform's pricing model costs you later.
- [No-Code vs. Code](../../concepts/no-code-vs-code.md) - The use-case-by-use-case decision to build visually or in code.
- [Rapid Prototyping](../../concepts/rapid-prototyping.md) - Building fast with managed services first, then hardening only what proves out.
- [Agent Deployment](../../concepts/agent-deployment.md) - Getting agents to production on a provider-agnostic, cost-predictable host.
- [Google Calendar](./google-calendar.md) - Google's calendar service, integrated via API as the action target for agents that turn extracted meeting action items into scheduled events.

## Sources

- [Bubble is My BIGGEST Regret for No Code AI Apps - What I Use Instead](../../sources/bubble-is-my-biggest-regret-for-no-code-ai-apps-what-i-use-instead.md) - "[0:00:31] they just go to one of the more popular app builders that are starting to integrate with generative AI like bubble I'm sure you've heard of bubble before but here is the big problem with these platforms they have a ton of hidden fees"
- [Bubble is My BIGGEST Regret for No Code AI Apps - What I Use Instead](../../sources/bubble-is-my-biggest-regret-for-no-code-ai-apps-what-i-use-instead.md) - "[0:04:23] something they were able to do really really quickly on moment took a minute and 18 seconds and $155 on bubble"
