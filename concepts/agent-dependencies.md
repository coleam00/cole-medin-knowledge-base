---
type: concept
title: "Agent Dependency Injection"
description: "Passing runtime dependencies (clients, config, connections) into an agent and its tools via dependency injection (as in Pydantic AI) for cleaner, testable, decoupled agent code."
tags: [dependency-injection, pydantic-ai, tools, testability, decoupling]
videos: [pydantic-ai-deepseek-v3-the-best-ai-agent-combo]
created: 2026-07-21
updated: 2026-07-21
---

# Agent Dependency Injection

Agent dependency injection is the practice of passing an agent the runtime resources it needs, rather than hard-coding them, so those resources are available to the model's tools when it invokes them. Cole names them as one of the first things you define when building a Pydantic AI agent: "first of all is your dependencies for the agent this is things like the HTTP client or API keys that your agent needs when it is invoking tools" [0:08:31]. Dependencies are the ambient context of a tool call. The tool function does not construct its own HTTP session or read its own secrets; those are injected in from the outside and handed to the function at call time.

The pattern is concrete once you look at a real tool. For an agent that talks to GitHub, "our agent needs an HTTP client to interact with the GitHub API and it also needs the GitHub token" [0:12:31], so both the client and the token are declared as dependencies and threaded into every tool that touches the API. This is why the pattern matters: it keeps tool code decoupled from how its collaborators are created. The same tool can be pointed at a real API in production and a fake client in a test, because nothing inside the tool decides where its dependencies come from. That testability and separation of concerns is the whole payoff of doing injection instead of reaching for globals.

Dependencies pair naturally with the agent's other declared pieces, its model, its tools, and its structured output type, forming the typed contract a framework like Pydantic AI enforces around an agent.

## Prerequisites

- [Tool Calling](./tool-use.md) - dependencies exist to be consumed by tools; injection only matters because tools need clients and keys.

## Builds on

- [The Core Components of an Agent](./agent-core-components.md) - dependencies are one of the standard components you wire up alongside the model, tools, and output type.

## Related

- [Structured Outputs](./structured-outputs.md) - the other typed contract Pydantic AI puts around an agent, defined right next to its dependencies.
- [Production-Grade Agents](./production-grade-agents.md) - decoupled, injectable dependencies are what make an agent testable enough to ship.
- [Model Selection](./model-selection.md) - the model is chosen and injected the same way the clients and keys are.

## Tools

- [Pydantic AI](../entities/tools/pydantic-ai.md) - the framework whose dependency-injection system this pattern is drawn from.
- [DeepSeek V3](../entities/tools/deepseek-v3.md) - the model paired with Pydantic AI in the source build.

## Sources

- [Pydantic AI + DeepSeek V3 - The BEST AI Agent Combo](../sources/pydantic-ai-deepseek-v3-the-best-ai-agent-combo.md) - "[0:08:31] first of all is your dependencies for the agent this is things like the HTTP client or API keys that your agent needs when it is invoking tools"
- [Pydantic AI + DeepSeek V3 - The BEST AI Agent Combo](../sources/pydantic-ai-deepseek-v3-the-best-ai-agent-combo.md) - "[0:12:31] our agent needs an HTTP client to interact with the GitHub API and it also needs the GitHub token"
