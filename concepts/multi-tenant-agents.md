---
type: concept
title: "Multi-Tenant Agents"
description: "Building a single agent that serves many users, each with personalized tools, memory, and securely authorized access to their own accounts."
tags: [multi-tenant, memory, oauth, scale]
videos: [the-only-ai-tech-stack-you-need-in-2026, why-is-everyone-missing-this-with-ai-agents-memory-tools-that-scale]
created: 2026-07-21
updated: 2026-07-21
---

# Multi-Tenant Agents

A multi-tenant agent is one codebase that serves many distinct users at once, each seeing their own tools, memory, and connected accounts. The failure mode it corrects is baking a single identity into the build: "most agents are built with a single Gmail account in mind or a single Slack account or a single rag knowledge base and that my friend will not scale" [0:00:29]. The moment an agent has to help thousands of people, every per-user resource (mailbox, calendar, knowledge base, memory) must be keyed to *whose* request is being served, not hard-wired at deploy time.

## How it works

Two problems separate a demo agent from a multi-tenant one. First, **per-user memory and knowledge** so retrieval, preferences, and history are scoped to the requesting user rather than a shared pool. Second, and harder, **per-user authorization**: the agent must act on each user's own accounts without the developer ever handling their credentials. Cole frames this as the gap frameworks leave open: "frameworks like Pydantic AI make it very easy to add tools into our AI agents but what they don't handle is agent authorization and tool security that is where arcade comes in" [0:08:42]. The authorization layer brokers OAuth so a user connects their own Gmail or Slack and the agent receives a scoped token, never the password. Cole is blunt about the difficulty: "the agent needs some sort of way to authorize with those accounts... That is a very hard thing to engineer without a tool like Arcade" [0:10:32]. Solve both and you reach the payoff: "this is the kind of personalized agent that we can bring to everyone and scale to millions" [0:06:34].

## Builds on

- [Production vs. Personal Agents](./production-vs-personal-agents.md) - multi-tenancy is exactly the line a personal agent cannot cross without re-architecting for other users' live data and access control.

## Related

- [Memory Systems](./memory-systems.md) - per-user memory is one half of what makes each tenant's agent feel personalized.
- [Agent Security](./agent-security.md) - scoped tokens and least-privilege access are the security backbone of serving many users.
- [Model Context Protocol (MCP)](./mcp.md) - a common way to expose the per-user tools an agent authorizes into.

## Tools

- [Arcade](../entities/tools/arcade.md) - the authorization/tool-security layer Cole reaches for to broker per-user OAuth at scale.
- [Pydantic AI](../entities/tools/pydantic-ai.md) - makes adding tools easy but deliberately leaves authorization to a dedicated layer.

## Sources

- [Why is Everyone Missing This with AI Agents?! (Memory + Tools that Scale)](../sources/why-is-everyone-missing-this-with-ai-agents-memory-tools-that-scale.md) - "[0:00:29] most agents are built with a single Gmail account in mind or a single Slack account or a single rag knowledge base and that my friend will not scale"
- [The ONLY AI Tech Stack You Need in 2026](../sources/the-only-ai-tech-stack-you-need-in-2026.md) - "[0:10:32] the agent needs some sort of way to authorize with those accounts... That is a very hard thing to engineer without a tool like Arcade"
