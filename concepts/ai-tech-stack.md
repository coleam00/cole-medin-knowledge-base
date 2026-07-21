---
type: concept
title: "AI Tech Stack"
description: "Your chosen collection of tools and services (LLM, framework, database, automation, hosting) combined into one working AI system - pick a stack that fits, keep it simple and reusable, and stick with it instead of over-researching every option."
tags: [tech-stack, tooling]
videos: [how-to-dominate-with-ai-in-2025]
created: 2026-07-21
updated: 2026-07-21
---

# AI Tech Stack

An AI tech stack is the specific set of pieces you commit to. "An AI Tech stack is really just your collection of tools and services that you're combining together to create the system for yourself or your business" [0:15:54]. In practice that means an LLM provider, an agent framework, a database and vector store, an automation layer, a front end, and somewhere to host it. Choosing them is itself one of the high-leverage skills of the era, because the market ships a plausible new option every week.

The governing advice is to stop shopping. "The important thing is to find what works for you and your business and just stick with it. Don't spend a month diving into the weeds of all these services." [0:16:52] Two old engineering principles carry the decision: keep it simple, and don't repeat yourself. Pick the smallest stack that covers your use case, then reuse it across projects so the second build is faster than the first. Cole shares his own stack as an example explicitly not as a prescription, and notes it changes often - which is precisely why the transferable skill is stack *selection*, a [capability, not a tool](./capabilities-over-tools.md).

One decision dominates the rest. "The biggest decision as you're building out your Tech stack, the most important one, is whether or not you want to go local with your large language model." [0:17:41] Local versus cloud cascades into everything downstream: hardware and [quantization](./model-quantization.md) constraints, [data privacy](./llm-data-privacy-tiers.md) posture, per-token cost versus fixed infrastructure cost, latency, and which frameworks and hosting options remain available. Settle it first, then let the rest of the stack follow.

Everything else is a fit question rather than a best-tool question: whether you build in code or a [visual builder](./no-code-vs-code.md), which [model](./model-selection.md) each step of a workflow deserves, and whether an off-the-shelf product already solves the problem for a monthly fee. A stack you know deeply beats a marginally better stack you have to relearn.

## Prerequisites

- [Capabilities Over Tools](./capabilities-over-tools.md) - why stack choice matters more than stack mastery.

## Contrasts with

- [Buy vs. Build](./buy-vs-build.md) - the prior question of whether you need a stack for this at all.

## Related

- [Local vs. Cloud Decision Framework](./local-vs-cloud-decision-framework.md) - the dominant fork in the stack.
- [Local & Self-Hosted AI](./local-ai.md) - what committing to local actually requires.
- [Model Selection](./model-selection.md) - choosing the LLM layer of the stack.
- [LLM Cost Optimization](./llm-cost-optimization.md) - the running cost the stack locks you into.
- [Self-Hosting Cost Crossover](./self-hosting-cost-crossover.md) - when local infrastructure becomes cheaper than tokens.
- [LLM Data Privacy Tiers](./llm-data-privacy-tiers.md) - the privacy constraint that can force the decision.
- [No-Code vs. Code](./no-code-vs-code.md) - the build-surface layer of the stack.
- [SDK vs. Framework Decision](./sdk-vs-framework-decision.md) - how much abstraction to accept.
- [Provider Independence](./provider-independence.md) - keeping the stack swappable after you commit.
- [AI Agent Learning Roadmap](./ai-agent-learning-roadmap.md) - the learning path that assembles these pieces.

## Tools

- [Ollama](../entities/tools/ollama.md) - the local LLM runtime the local branch of the decision leads to.
- [Postgres](../entities/tools/postgres-pgvector.md) - database and vector store in one.
- [Supabase](../entities/tools/supabase.md) - hosted Postgres plus auth for the application layer.
- [n8n](../entities/tools/n8n.md) - the automation and workflow layer.
- [Pydantic AI](../entities/tools/pydantic-ai.md) - the coded agent framework layer.
- [LangGraph](../entities/tools/langgraph.md) - the multi-agent orchestration layer.
- [Docker](../entities/tools/docker.md) - packaging and deployment across the stack.
- [OpenRouter](../entities/tools/openrouter.md) - one endpoint for many models, keeping the LLM slot swappable.

## Sources

- [How to DOMINATE with AI in 2025](../sources/how-to-dominate-with-ai-in-2025.md) - "[0:15:54] An AI Tech stack is really just your collection of tools and services that you're combining together to create the system for yourself or your business"
- [How to DOMINATE with AI in 2025](../sources/how-to-dominate-with-ai-in-2025.md) - "[0:16:52] the important thing is to find what works for you and your business and just stick with it don't spend a month diving into the weeds of all these services"
- [How to DOMINATE with AI in 2025](../sources/how-to-dominate-with-ai-in-2025.md) - "[0:17:41] the biggest decision as you're building out your Tech stack the most important one is whether or not you want to go local with your large language model"
