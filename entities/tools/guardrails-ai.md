---
type: entity
subtype: tool
title: "Guardrails AI"
description: "Open-source Python framework Cole leans on for agent input/output guardrails, blocking things like PII entering a prompt or unsafe content leaving the LLM."
resource: "https://github.com/guardrails-ai/guardrails"
tags: [observability, validation]
videos: [learn-90-of-building-ai-agents-in-30-minutes]
created: 2026-07-21
updated: 2026-07-21
---

# Guardrails AI

Guardrails AI is an open-source Python framework that sits on both sides of an LLM call and enforces rules on what goes in and what comes out. Cole introduces it as his standing answer to agent safety, in a line whose aside is the point: "there's a super popular open source repository that I lean on all the time to help with guardrails and very creatively called guardrails AI" [0:15:21]. Input guardrails catch things like personally identifiable information before it ever reaches the prompt; output guardrails catch unsafe, off-policy, or malformed content before it reaches a user or a downstream tool.

The framing matters as much as the tool. It appears in the security portion of Cole's four-component agent primer, where the advice is deliberately anti-heroic: handle security with existing tools instead of trying to become a security expert overnight. Alongside no hardcoded keys and dependency scanning, a guardrails library is one of the small number of things worth wiring in early, because the failure modes it prevents (leaked data, unsafe output) are the ones you cannot walk back after the fact.

Guardrails AI is the concrete implementation of the [Guardrails](../../concepts/guardrails.md) concept, and it pairs naturally with schema-level enforcement. Where [Pydantic](./pydantic.md) constrains the *shape* of a response and retries when validation fails, Guardrails AI constrains its *content* and its inputs. Both are checks that run outside the model's goodwill, which is the whole reason they work: an agent asked nicely in a system prompt not to leak PII will comply most of the time, and a validator that rejects the payload will comply all of the time. That distinction is what separates a demo agent from a [production-grade](../../concepts/production-grade-agents.md) one.

## Realizes

- [Guardrails](../../concepts/guardrails.md) - Constraints and checks that keep agents from hallucinating, going off the rails, or emitting unsafe output.
- [Agent Security](../../concepts/agent-security.md) - Scoping what an agent can see and say to limit blast radius, here at the prompt boundary.
- [Validation](../../concepts/validation.md) - Explicit checks the system runs rather than instructions the model is trusted to follow.
- [Production-Grade Agents](../../concepts/production-grade-agents.md) - The layer of validation, error handling, and monitoring that a real deployment needs beyond an LLM plus tools.

## Works with

- [Pydantic](./pydantic.md) - The data-validation library that enforces response *shape*, complementary to Guardrails AI enforcing response *content*.
- [Pydantic AI](./pydantic-ai.md) - The agent framework Cole builds in, where guardrails wrap the agent's inputs and outputs.
- [Langfuse](./langfuse.md) - Production agent monitoring, which shows you the behavior guardrails are catching or missing.

## Contrasts with

- [Logfire](./logfire.md) - Observability that records what the agent did, where guardrails prevent it from doing certain things at all.

## Related

- [The Core Components of an Agent](../../concepts/agent-core-components.md) - The LLM, tools, system prompt, and memory primer this recommendation sits inside.
- [Structured Outputs](../../concepts/structured-outputs.md) - Schema-constrained responses with retries, the shape-level sibling of content guardrails.
- [Human in the Loop](../../concepts/human-in-the-loop.md) - Keeping an approver in the path for the decisions no automated check should own.
- [Hallucination Detection](../../concepts/hallucination-detection.md) - Deterministically checking generated output against ground truth and feeding the report back for a fix.
- [Agent Observability](../../concepts/agent-observability.md) - Tracing, logging, and cost metrics that make guardrail behavior visible in production.

## Sources

- [Learn 90% of Building AI Agents in 30 Minutes](../../sources/learn-90-of-building-ai-agents-in-30-minutes.md) - "[0:15:21] there's a super popular open source repository that I lean on all the time to help with guardrails and very creatively called guardrails AI"
