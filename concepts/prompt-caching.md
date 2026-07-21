---
type: concept
title: "Prompt Caching"
description: "Caching repeated portions of prompts to cut cost and latency across an AI coding session."
tags: [ai-coding, optimization, cost, llm]
videos: [the-easiest-possible-strategy-for-accurate-rag-step-by-step-guide, our-boltnew-forks-most-requested-feature-is-finally-here]
created: 2026-07-21
updated: 2026-07-21
---

# Prompt Caching

Prompt caching lets a model provider store the repeated prefix of a prompt so you are not billed full price to re-send the same tokens on every call. The savings are large and provider-dependent: "For OpenAI, it's a 50% reduced cost. And then for Anthropic and I think Gemini as well, it's like a 90% reduced cost" [0:13:08]. Because so much of an AI coding or RAG prompt is a fixed preamble (system rules, a document being annotated, project context) that stable portion is exactly what caching makes nearly free to reuse.

## How it works

The technique earns its keep wherever the same block of context is fed to the model many times. In [contextual retrieval](./contextual-retrieval.md), every chunk is sent to an LLM alongside the whole source document to be situated, which is expensive if the document is re-sent each time: "This is where we can take advantage of the idea of prompt caching... We can use prompt caching to reduce the cost of contextual retrieval." The document is cached once, then each per-chunk call reuses it at the discounted rate. The same lever applies to interactive coding tools, where a long, stable project context precedes every user turn. In the Bolt.new fork, prompt caching was a top community request precisely because it slashes the running cost of a session: it was shipped as "the big high priority task" and Cole flags "this is super important as well with the prompt caching."

## Related

- [Contextual Retrieval](./contextual-retrieval.md) - the flagship use case, where caching the source document makes per-chunk situating affordable.
- [Model Selection](./model-selection.md) - cache discounts differ sharply by provider (roughly 50% vs 90%), which factors into cost-driven model choice.
- [LLM Cost Optimization](./llm-cost-optimization.md) - Systematically cutting the bill for running LLM applications at scale by sending the bulk of cheap-to-serve traffic to far cheaper models and paying premium rates only for the rare hard requests.

## Sources

- [The EASIEST Possible Strategy for Accurate RAG (Step by Step Guide)](../sources/the-easiest-possible-strategy-for-accurate-rag-step-by-step-guide.md) - "[0:12:19] This is where we can take advantage of the idea of prompt caching... We can use prompt caching to reduce the cost of contextual retrieval"
- [The EASIEST Possible Strategy for Accurate RAG (Step by Step Guide)](../sources/the-easiest-possible-strategy-for-accurate-rag-step-by-step-guide.md) - "[0:13:08] For OpenAI, it's a 50% reduced cost. And then for Anthropic and I think Gemini as well, it's like a 90% reduced cost"
- [Our Bolt.new Fork's Most Requested Feature is FINALLY Here](../sources/our-boltnew-forks-most-requested-feature-is-finally-here.md) - "[0:08:00] he's the one who worked on the UI and helped me bring in the prompt caching request... this is super important as well with the prompt caching"
