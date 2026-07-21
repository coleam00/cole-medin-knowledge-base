---
type: concept
title: "Production vs. Personal Agents"
description: "The architectural divide between quick personal-use agents and systems built to scale in production, and what has to change (structure, storage, reliability) to cross that line."
tags: [production, scaling, personal-agents, reliability, knowledge-bases]
videos: [i-love-the-karpathy-llm-wiki-but-it-doesnt-scale-heres-what-does]
created: 2026-07-21
updated: 2026-07-21
---

# Production vs. Personal Agents

There is a hard line between an agent you run for yourself and an agent you ship to other people, and the two demand different architectures. Cole draws it explicitly: "there is a line that has to be drawn where personal agents they don't scale. And really it's when you want to ship an agent to other people, you no longer can use the LLM Wiki locally running agent setup" [0:00:32]. A personal agent can lean on a local file store, a single set of credentials, and no concurrency; a production agent cannot.

## How it works

The moment other people log in, three new requirements appear that a personal setup ignores: concurrency, live data, and access control. "As soon as other people are using your agent, so many users at once, you have live data, you need to care about things like access control and retrieval at scale, that is when this just it doesn't cut it anymore" [0:02:11]. Crossing the line means replacing local-file knowledge with a real database, adding per-user isolation, and hardening for reliability and retrieval at scale. Cole ties this directly to where value actually lives: "almost anything that's really providing real business value is an agent that is shipped as a part of a platform to a production environment with other people logging in and talking to the agent" [0:03:26]. The takeaway is not that personal setups are bad, they are excellent for a single user, but that shipping to others is a re-architecture, not a deployment step.

## Contrasts with

- [Second Brain](./second-brain.md) - the local, single-user knowledge-agent setup (Karpathy-style LLM wiki) that Cole says stops scaling once you ship to others.

## Related

- [Multi-Tenant Agents](./multi-tenant-agents.md) - the concrete architecture on the far side of this line: many users, per-user memory and authorized access.
- [Production-Grade Agents](./production-grade-agents.md) - the reliability, testing, and observability work a shipped agent requires.
- [Memory Systems](./memory-systems.md) - moving from a local store to per-user memory at scale.
- [Retrieval-Augmented Generation (RAG)](./rag.md) - retrieval at scale is one of the pieces that has to change when going to production.

## Sources

- [I Love the Karpathy LLM Wiki but it Doesn't Scale. Here's What Does.](../sources/i-love-the-karpathy-llm-wiki-but-it-doesnt-scale-heres-what-does.md) - "[0:00:32] there is a line that has to be drawn where personal agents they don't scale. And really it's when you want to ship an agent to other people, you no longer can use the LLM Wiki locally running agent setup."
- [I Love the Karpathy LLM Wiki but it Doesn't Scale. Here's What Does.](../sources/i-love-the-karpathy-llm-wiki-but-it-doesnt-scale-heres-what-does.md) - "[0:03:26] almost anything that's really providing real business value is an agent that is shipped as a part of a platform to a production environment with other people logging in and talking to the agent."
