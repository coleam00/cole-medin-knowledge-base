---
type: entity
subtype: tool
title: "Pydantic"
description: "Python's de facto data-validation library (also the foundation of FastAPI), used as the validation layer by OpenAI, Anthropic, LangChain, and LlamaIndex, and the reason Pydantic AI puts validation at an agent framework's core."
resource: "https://docs.pydantic.dev"
tags: [agent-framework, sdk]
videos: [weve-been-building-ai-agents-wrong-until-now]
created: 2026-07-21
updated: 2026-07-21
---

# Pydantic

Pydantic is the data-validation library that most of the Python AI ecosystem quietly runs on. Cole introduces it as long-settled infrastructure rather than anything new: "pantic itself has been around for a long time it's essentially a validation library in Python" [0:01:38]. The idea is simple and old, which is why it holds up. You declare the shape you expect (typed models and fields), and Pydantic guarantees that what arrives actually matches, raising a clear error when it does not. [FastAPI](./fastapi.md) is built on top of it for exactly that reason: an endpoint declares its payload, and the framework enforces it before your code ever runs.

The reason it matters for agents is that an LLM is another untrusted input boundary. When you ask for [Structured Outputs](../../concepts/structured-outputs.md), specific keys in specific types, you need something to check that the model complied, and the whole field converged on the same answer. As Cole puts it, "open Ai and anthropic use it Lang chain llama index crew AI all these other things... they all use pantic as the validation later" [0:02:27]. The [OpenAI](../organizations/openai.md) and [Anthropic](../organizations/anthropic.md) SDKs, [LangChain](./langchain.md), LlamaIndex, and [CrewAI](./crewai.md) all lean on it, which makes Pydantic the closest thing the Python agent ecosystem has to a shared type system.

That lineage is the whole argument for [Pydantic AI](./pydantic-ai.md). The team that built the validation layer everyone else depends on then built an agent framework, and Cole trusts it specifically because of what they already care about: validation of LLM output, tool invocation, and tests are all the same problem wearing different hats. Type-safe dependency injection, structured and streamed responses, and typed tool arguments in Pydantic AI are all classic Pydantic showing through. This is why [Validation](../../concepts/validation.md) is not an afterthought bolted onto the framework but the property the framework was designed around, and it is the difference between an agent that occasionally returns malformed JSON and one that fails loudly and retries.

## Realizes

- [Structured Outputs](../../concepts/structured-outputs.md) - declaring the exact schema an LLM must return, and enforcing it.
- [Validation](../../concepts/validation.md) - checking that what you got is what you expected, at every boundary.

## Works with

- [Pydantic AI](./pydantic-ai.md) - the agent framework built by the same team, with Pydantic validation at its core.
- [FastAPI](./fastapi.md) - built on top of Pydantic; the canonical example Cole uses to explain what validation means.
- [Python](./python.md) - the language whose type hints Pydantic turns into runtime guarantees.
- [LangChain](./langchain.md) - one of the frameworks that uses Pydantic as its validation layer.
- [CrewAI](./crewai.md) - another framework named as depending on the same layer.
- [OpenAI Agents SDK](./openai-agents-sdk.md) - part of the OpenAI Python tooling that leans on Pydantic models.
- [Guardrails AI](./guardrails-ai.md) - Open-source Python framework Cole leans on for agent input/output guardrails, blocking things like PII entering a prompt or unsafe content leaving the LLM.

## Related

- [Agent Dependency Injection](../../concepts/agent-dependencies.md) - the type-safe dependency system Pydantic AI inherits from Pydantic.
- [Docstrings as Tool Descriptions](../../concepts/docstrings-as-tool-descriptions.md) - typed function signatures plus docstrings become the tool contract.
- [Tool Design](../../concepts/tool-design.md) - well-typed arguments are what make a tool reliably callable.
- [Tool Calling](../../concepts/tool-use.md) - validating tool arguments is the same problem as validating model output.
- [Structured vs Unstructured Data](../../concepts/structured-vs-unstructured-data.md) - the boundary Pydantic exists to police.

## Sources

- [We've Been Building AI Agents WRONG Until Now](../../sources/weve-been-building-ai-agents-wrong-until-now.md) - "[0:01:38] pantic itself has been around for a long time it's essentially a validation library in Python"
- [We've Been Building AI Agents WRONG Until Now](../../sources/weve-been-building-ai-agents-wrong-until-now.md) - "[0:02:27] open Ai and anthropic use it Lang chain llama index crew AI all these other things... they all use pantic as the validation later"
