---
type: entity
subtype: tool
title: "Zod"
description: "A TypeScript schema/validation library used to type agent tool inputs so the arguments the model passes to a function are reliable."
resource: "https://zod.dev"
tags: [agent-framework, sdk, typescript]
videos: [this-completely-changes-the-way-we-build-production-ai-agents-vercel-eve]
created: 2026-07-21
updated: 2026-07-21
---

# Zod

Zod is a TypeScript schema declaration and validation library, and in agent work its job is narrow but load-bearing: it declares the exact shape of the arguments a model is allowed to hand a tool, then enforces that shape at runtime. Cole states the purpose plainly while walking the tools folder of a [Vercel Eve](./eve.md) agent: "We're using Zod here for typing to make it so that the inputs the agent gives to the function is reliable in what it really needs" [0:11:17].

That sentence carries the whole argument. A tool call is just JSON emitted by a probabilistic system, so it is a guess until something checks it. A Zod schema turns the guess into a contract in both directions from a single declaration: the schema is what gets serialized into the tool definition the model reads (field names, types, which arguments are required), and the same schema rejects a malformed call before the function body ever runs. Describing the tool and defending the tool stop being two separate pieces of work.

In Eve, that compresses a tool down to one [TypeScript](./typescript.md) file - the function plus its Zod-typed input - which is what makes the framework's compile-time auto-discovery safe. There is no hand-wiring step where a schema and an implementation can drift apart, because the folder walk picks up both at once. The same pattern is how tools are defined in the [Vercel AI SDK](./vercel-ai-sdk.md), and it is the TypeScript-side answer to the role [Pydantic](./pydantic.md) plays across the Python agent ecosystem.

The practical payoff is fewer silent failures in the class of bug that is hardest to debug: an agent that "worked" but passed a string where a number belonged, or omitted a field entirely and let a downstream call fail three layers away. Typed inputs push that failure to the boundary, where it can be caught, reported back to the model, and retried.

## Realizes

- [Tool Design](../../concepts/tool-design.md) - Designing agent tools to be few, single-purpose, and well-described so the model uses them reliably.
- [Structured Outputs](../../concepts/structured-outputs.md) - Constraining LLM output to a validated schema (with retries on failure) so downstream code can rely on its shape.
- [Contract-First Development](../../concepts/contract-first.md) - Define the interface between components before building either side, so they can be developed independently and wired together reliably.
- [Guardrails](../../concepts/guardrails.md) - Constraints and checks that keep agents from going off the rails or emitting unsafe output.

## Contrasts with

- [Pydantic](./pydantic.md) - Python's de facto data-validation library, filling the identical role in Python agent frameworks that Zod fills in TypeScript ones.

## Works with

- [TypeScript](./typescript.md) - The language Zod schemas and the tool files that carry them are written in.
- [Eve (Vercel)](./eve.md) - Vercel's file-system-first agent framework, where each tool is a TypeScript file typed with Zod.
- [Vercel AI SDK](./vercel-ai-sdk.md) - Vercel's lower-level AI library, which uses the same schema-typed tool definitions.
- [MCP (Model Context Protocol)](./mcp.md) - The protocol whose TypeScript servers declare their tool inputs the same way.
- [Next.js](./nextjs.md) - The React framework these typed agent routes are commonly served from.

## Related

- [Tool Calling](../../concepts/tool-use.md) - Letting an LLM invoke external functions and APIs so it can act beyond its parametric knowledge.
- [Docstrings as Tool Descriptions](../../concepts/docstrings-as-tool-descriptions.md) - The prose half of the same contract: what the model reads to decide when to call a tool.
- [Agent Request/Response Schema](../../concepts/request-response-schema.md) - Fixing a strict input payload and minimal output so agents become interchangeable behind a common contract.
- [File-System-Based Agents](../../concepts/file-system-based-agents.md) - An architecture where an agent is a folder of markdown and TypeScript primitives rather than hand-wired framework code.
- [Production-Grade Agents](../../concepts/production-grade-agents.md) - Real agents need validation, error handling, testing, and observability, not just an LLM plus tools.
- [Validation](../../concepts/validation.md) - Building explicit checks into agentic workflows so the AI verifies its own output before moving on.

## Sources

- [This Completely Changes the Way We Build Production AI Agents (Vercel Eve)](../../sources/this-completely-changes-the-way-we-build-production-ai-agents-vercel-eve.md) - "[0:11:17] We're using Zod here for typing to make it so that the inputs the agent gives to the function is reliable in what it really needs."
