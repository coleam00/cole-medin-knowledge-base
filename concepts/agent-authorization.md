---
type: concept
title: "Agent Authorization"
description: "Letting an agent obtain scoped OAuth access to each user's own accounts, requested just in time when a tool is first needed, instead of hardcoding one set of credentials."
tags: [oauth, authentication, security, ux]
videos: [why-is-everyone-missing-this-with-ai-agents-memory-tools-that-scale]
created: 2026-07-21
updated: 2026-07-21
---

# Agent Authorization

Agent authorization is the practice of having an agent acquire access to each individual user's accounts at runtime, rather than shipping with one hardcoded set of credentials. Most agents and MCP servers are built for exactly one user: one Gmail account, one Slack workspace, one knowledge base. That design cannot scale past its author. "Arcade is the key here for solving the authentication and scaling nightmare for tools... we can have them dynamically request access to user accounts for different services and we go through an OOTH flow" [0:02:19] - an OAuth flow, per user, with scoped permissions and credentials cached so the agent never has to ask that user twice.

The second half of the idea is *when* to ask. Rather than an onboarding wall that demands every integration up front, permission is requested lazily: "we also are only asking for permission when the time comes for our agent to use one of these services on behalf of our user for the very first time" [0:02:45]. A user who never asks the agent to touch Asana is never asked to authorize Asana. Just-in-time authorization is a UX decision as much as a security one, and it keeps the granted scope proportional to what the agent actually does.

Structurally this becomes a branch in the [agent graph](./langgraph-nodes-edges-state.md). A decision node consults an auth manager before every tool call: "this manager tells us which one of the two paths we have to go down here from our agent whenever we are invoking a tool" [0:19:07]. If the user already holds access, the graph routes straight to the tool node. If not, it routes to an authorization node that uses an interrupt to pause the run, surfaces an OAuth URL, waits for the human to approve, then resumes into the tool call with nothing re-executed. The pattern is reusable across every service the agent touches.

Paired with per-user long-term [memory](./memory-systems.md), scoped auth is what makes an agent genuinely multi-tenant: every user gets their own tools, their own recall, and effectively their own system prompt, so a single deployed agent can serve millions instead of one.

## Prerequisites

- [Tool Calling](./tool-use.md) - authorization is a gate placed in front of a tool call.
- [Multi-Tenant Agents](./multi-tenant-agents.md) - the scaling problem that makes per-user auth necessary.

## Contrasts with

- [MCP Authentication with OAuth](./mcp-oauth.md) - the same OAuth problem solved at the MCP server boundary instead of inside the agent graph.

## Related

- [Agent Security](./agent-security.md) - scoped, revocable credentials as the security posture.
- [Securing Agent APIs](./api-security.md) - protecting the endpoint the agent itself is exposed on.
- [Human in the Loop](./human-in-the-loop.md) - the interrupt-and-wait pattern the auth node reuses.
- [Permission Management](./permission-management.md) - deciding what an agent is allowed to do once authorized.
- [Memory Systems](./memory-systems.md) - the other half of per-user personalization.
- [Production-Grade Agents](./production-grade-agents.md) - what separates a demo agent from a deployed one.
- [The Problems With MCP Servers](./mcp-problems.md) - single-user credential assumptions baked into most servers.
- [Agent2Agent (A2A) Protocol](./a2a-protocol.md) - propagating that auth across agent boundaries.

## Tools

- [Arcade](../entities/tools/arcade.md) - the service that brokers per-user OAuth, scopes, and cached credentials for agent tools.
- [LangGraph](../entities/tools/langgraph.md) - the authorization node and interrupt live in the graph.
- [Supabase](../entities/tools/supabase.md) - supplies the sign-in and unique user ID the auth and memory namespaces key off.
- [Gmail](../entities/tools/gmail.md) - the canonical hardcoded-credential example.
- [Asana](../entities/tools/asana.md) - the tool used to demo just-in-time authorization.
- [Coinbase x402](../entities/tools/x402.md) - Coinbase's payment protocol for exposing AI agents over the internet that charge other agents per use, settled in stablecoins like USDC.

## Sources

- [Why is Everyone Missing This with AI Agents?! (Memory + Tools that Scale)](../sources/why-is-everyone-missing-this-with-ai-agents-memory-tools-that-scale.md) - "[0:02:19] Arcade is the key here for solving the authentication and scaling nightmare for tools... we can have them dynamically request access to user accounts for different services and we go through an OOTH flow"
- [Why is Everyone Missing This with AI Agents?! (Memory + Tools that Scale)](../sources/why-is-everyone-missing-this-with-ai-agents-memory-tools-that-scale.md) - "[0:02:45] we also are only asking for permission when the time comes for our agent to use one of these services on behalf of our user for the very first time"
- [Why is Everyone Missing This with AI Agents?! (Memory + Tools that Scale)](../sources/why-is-everyone-missing-this-with-ai-agents-memory-tools-that-scale.md) - "[0:19:07] this manager tells us which one of the two paths we have to go down here from our agent whenever we are invoking a tool"
