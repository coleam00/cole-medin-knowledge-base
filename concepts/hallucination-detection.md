---
type: concept
title: "Hallucination Detection"
description: "Deterministically checking AI-generated code against a ground-truth structure (a parsed knowledge graph of the library) to flag methods and parameters that don't actually exist, then feeding the report back so the agent can fix them."
tags: [hallucination-detection, validation]
videos: [ai-code-that-fixes-itself-an-mcp-you-can-try-now]
created: 2026-07-21
updated: 2026-07-21
---

# Hallucination Detection

Hallucination detection is a validation pass that compares AI-generated code against a **ground-truth map of the libraries it imports** and reports every call that does not exist. Cole's implementation parses a library's repository into a knowledge graph of classes, methods, and parameters, then walks the generated file against it: "I even have a script that leverages the knowledge graph to check for these hallucinations... it's all just deterministic code going out to the knowledge graph."

The crucial word is *deterministic*. No model judges the code; a script resolves each symbol against the graph and either finds it or does not. That gives a verdict with no false confidence behind it, of the form "It says that the method invoked async is not found on the class panticai." Because the graph carries signatures, the same pass catches wrong or invented parameters, not just invented method names, which is where models drift most quietly after a library's API moves past their [training cutoff](./training-cutoff.md).

The second half of the pattern is the feedback loop. The report is not a human-facing lint result but an agent-facing one: "we can give this kind of hallucination detection reporter as a tool to our AI coding assistant." Exposed over MCP, the checker becomes something the coding agent calls on its own output, reads the failures from, and repairs, closing a self-correction loop without a human in the middle. That turns a static verification artifact into a continuously enforced constraint on every file the agent writes.

## Prerequisites

- [Knowledge Graphs](./knowledge-graphs.md) - the parsed class/method/parameter structure that supplies ground truth.
- [Parametric Knowledge](./parametric-knowledge.md) - hallucinated APIs are exactly where a model's baked-in memory of a library goes stale.

## Part of

- [Validation](./validation.md) - one deterministic gate inside the broader validation layer.
- [Self-Correcting Agents](./self-correction.md) - the report is fed back so the agent repairs its own output.

## Contrasts with

- [Code Review](./code-review.md) - an LLM reviewer reasons probabilistically about quality; this pass answers a factual question with a lookup.
- [Retrieval-Augmented Generation (RAG)](./rag.md) - semantic retrieval surfaces likely-relevant docs; the graph query returns an exact structural fact.

## Implemented by

- [Crawl4AI RAG MCP Server](../entities/tools/crawl4ai-rag-mcp.md) - ships the graph parser plus the hallucination-check script and exposes both as tools.
- [Neo4j](../entities/tools/neo4j.md) - stores the repository knowledge graph the checker queries.
- [Model Context Protocol (MCP)](./mcp.md) - the interface that hands the reporter to the coding assistant as a callable tool.

## Related

- [Agentic RAG](./agentic-rag.md) - the same server pairs semantic doc search with the structural graph query.
- [Limitations of AI Coding Models](./ai-coding-limitations.md) - inventing plausible-looking APIs is the failure mode this targets.
- [Guardrails](./guardrails.md) - a deterministic check is the strongest kind of guardrail available.
- [Deterministic Workflows](./deterministic-workflows.md) - reliability comes from taking the model out of the verdict.
- [End-to-End Validation](./end-to-end-validation.md) and [Separate Reviewer](./separate-reviewer.md) - the other layers a generated file should pass through.
- [Docs and Templates as Coding-Assistant Context](./docs-as-agent-context.md) and [Context7](../entities/tools/context7.md) - prevention: give the agent current API surfaces before it writes.
- [Tool Calling](./tool-use.md) - the mechanism by which the agent invokes the reporter on itself.

## Sources

- [AI Code That Fixes Itself (An MCP You Can Try Now)](../sources/ai-code-that-fixes-itself-an-mcp-you-can-try-now.md) - "[0:03:55] I even have a script that leverages the knowledge graph to check for these hallucinations... it's all just deterministic code going out to the knowledge graph."
- [AI Code That Fixes Itself (An MCP You Can Try Now)](../sources/ai-code-that-fixes-itself-an-mcp-you-can-try-now.md) - "[0:04:25] It says that the method invoked async is not found on the class panticai. And we can give this kind of hallucination detection reporter as a tool to our AI coding assistant."
