---
type: concept
title: "Agent2Agent (A2A) Protocol"
description: "Google's open standard for how independently-built agents discover and talk to each other over HTTP via agent cards and tasks, the agent-to-agent counterpart to MCP."
tags: [protocols, interoperability, a2a]
videos: [google-is-quietly-revolutionizing-ai-agents-this-is-huge, ag-ui-just-released-the-new-wave-of-ai-agent-apps]
created: 2026-07-21
updated: 2026-07-21
---

# Agent2Agent (A2A) Protocol

A2A is Google's open standard for letting independently built agents find each other and work together. "Google recently introduced their agent to agent protocol which is a standard for agents to communicate effectively with each other. It's very similar to how MCP is the standard to connect agents to tools." [0:00:00] It covers the edge [MCP](./mcp.md) does not: MCP standardizes agent-to-tool, A2A standardizes agent-to-agent. "It's been the year of agent protocols like Anthropic's MCP, making it so easy to connect tools to our agents, or Google's A2A, making it very seamless to connect agents to other agents." [0:00:00]

Mechanically an A2A agent is an HTTP server, closer to a microservice than a library. It publishes an **agent card**: a single metadata file describing its capabilities, how to reach it, and its authentication requirements. A client fetches that card, generates a task ID, sends a JSON payload, and receives a structured result, with optional push notifications for long-running work. The card is what makes runtime **agent discovery** possible, so a sales agent can learn a finance agent's capabilities at call time instead of hard-coding an integration that breaks on the next update.

The value is accessibility rather than new capability. "A2A just makes the entire process more accessible and standardized. And that's very powerful for quite a few reasons." [0:04:36] Engineers could always wire specialized agents together by hand; A2A means agents written in different frameworks and hosted by different vendors interoperate without bespoke glue for every pair. Note also that A2A is an architecture, not something you pip install, so a minimal Python server and client can satisfy the spec with no A2A library at all. The transferable skill is knowing how agents should communicate.

A2A and MCP compose: A2A at the agent layer, MCP at the tool layer, together forming the backend of a multi-agent system. The honest costs are the ones distributed systems always carry, amplified by non-deterministic LLM nodes: testing and edge-case explosion, a wider security surface with data crossing more third parties, authentication that has to propagate down through sub-agents and their tools, and error attribution that gets hard to trace. These are solvable engineering problems, but adoption is the real gate - an A2A-compatible agent is only useful once there are other agents to talk to.

## Part of

- [Agent Protocols](./agent-protocols.md) - the family of interoperability standards A2A belongs to.

## Contrasts with

- [Model Context Protocol (MCP)](./mcp.md) - the same idea one layer down; MCP connects agents to tools, A2A connects agents to agents.
- [Agent Client Protocol (ACP)](./agent-client-protocol.md) - the agent-to-editor member of the family.

## Related

- [Agent Teams](./agent-teams.md) - the multi-agent systems A2A is meant to wire together.
- [Single vs. Multi-Agent Architecture](./single-vs-multi-agent.md) - deciding whether you need peer agents at all.
- [Agent as an API Endpoint](./agent-as-api-endpoint.md) - exposing one agent as a callable service, the A2A server role.
- [Agent Security](./agent-security.md) - the widened attack surface of a distributed agent network.
- [Agent Authorization](./agent-authorization.md) - propagating scoped user auth across agents and their tools.
- [Tool Standardization (USB-C for AI)](./tool-standardization.md) - the same one-implementation-many-clients argument.
- [Provider Independence](./provider-independence.md) - the strategic payoff of betting on standards.
- [The Problems With MCP Servers](./mcp-problems.md) - the maturity issues protocols inherit.

## Tools

- [Google](../entities/organizations/google.md) - published the A2A specification.
- [MCP (Model Context Protocol)](../entities/tools/mcp.md) - the tool-layer half of the pairing.
- [Pydantic AI](../entities/tools/pydantic-ai.md) - used to build the minimal A2A server and client demo.
- [AG-UI](../entities/tools/ag-ui.md) - the agent-to-front-end protocol in the same wave.

## Sources

- [Google is Quietly Revolutionizing AI Agents (This is HUGE)](../sources/google-is-quietly-revolutionizing-ai-agents-this-is-huge.md) - "[0:00:00] Google recently introduced their agent to agent protocol which is a standard for agents to communicate effectively with each other. It's very similar to how MCP is the standard to connect agents to tools."
- [Google is Quietly Revolutionizing AI Agents (This is HUGE)](../sources/google-is-quietly-revolutionizing-ai-agents-this-is-huge.md) - "[0:04:36] A2A just makes the entire process more accessible and standardized. And that's very powerful for quite a few reasons."
- [AG-UI Just Released: The NEW WAVE of AI Agent Apps](../sources/ag-ui-just-released-the-new-wave-of-ai-agent-apps.md) - "[0:00:00] even more than that, it's been the year of agent protocols like Anthropic's MCP, making it so easy to connect tools to our agents, or Google's A2A, making it very seamless to connect agents to other agents"
