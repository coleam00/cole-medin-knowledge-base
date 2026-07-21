---
type: concept
title: "Agent Request/Response Schema"
description: "Standardizing how any agent plugs in by fixing a strict input payload (query, user_id, request_id, session_id) and a minimal output (a success boolean), so agents become interchangeable behind a common contract."
tags: [api, contract, schema, standardization]
videos: [the-glow-up-every-ai-agent-needs]
created: 2026-07-21
updated: 2026-07-21
---

# Agent Request/Response Schema

An agent request/response schema is a fixed input-and-output contract that any agent must satisfy to plug into a shared system, so that agents become interchangeable behind one common interface. Cole defines the input payload precisely: "you have the query that's the user prompt you have a user ID which you won't always have to use same with the request ID... and then the session ID that represents the ID of your conversation." Four fields carry everything the host needs: the prompt itself, who is asking, an identifier for this specific request, and the conversation the request belongs to.

The output side is deliberately minimal. The agent is not required to shape its response into a rigid structure; it only has to report whether the call worked: "the only thing that it has to return is a Json with a single parameter and that is a true or false for the success of the call to your agent." Keeping the mandatory return down to a single success boolean means any agent, built with any framework, can conform without contorting its internal logic, while richer output can flow through side channels like a real-time message store.

The purpose of fixing this schema is standardization. Once every agent accepts the same input shape and returns the same success signal, the surrounding platform can treat agents as drop-in components: register a new one, route requests to it, and swap it out later without rewiring the host. This is the contract that underpins turning agents into API endpoints and building frontends that work against any conforming agent. The strictness of the input and the leanness of the output are the two design choices that make agents genuinely interchangeable.

## Builds on

- [Agent as an API Endpoint](./agent-as-api-endpoint.md) - the schema is the contract that endpoint exposes.
- [Contract-First Development](./contract-first.md) - fixing the request/response shape up front so components integrate cleanly.

## Related

- [Frontend-Agnostic Agents](./frontend-agnostic-agent.md) - a stable schema is what lets any frontend drive any agent.
- [Multi-Tenant Agents](./multi-tenant-agents.md) - the user_id and session_id fields that scope requests per user and conversation.
- [Securing Agent APIs](./api-security.md) - protecting the standardized endpoint the schema defines.
- [Machines Paying Machines](./machines-paying-machines.md) - a common contract is a prerequisite for agents calling each other.

## Implemented by

- [Live Agent Studio](../entities/tools/live-agent-studio.md) - the platform whose common request/response contract every registered agent conforms to.
- [Zod](../entities/tools/zod.md) - A TypeScript schema/validation library used to type agent tool inputs so the arguments the model passes to a function are reliable.

## Sources

- [The GLOW-UP Every AI Agent Needs](../sources/the-glow-up-every-ai-agent-needs.md) - "[0:18:19] you have the query that's the user prompt you have a user ID which you won't always have to use same with the request ID... and then the session ID that represents the ID of your conversation"
- [The GLOW-UP Every AI Agent Needs](../sources/the-glow-up-every-ai-agent-needs.md) - "[0:19:04] the only thing that it has to return is a Json with a single parameter and that is a true or false for the success of the call to your agent"
