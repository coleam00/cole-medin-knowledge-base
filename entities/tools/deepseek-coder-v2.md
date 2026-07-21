---
type: entity
subtype: tool
title: "DeepSeek Coder V2"
description: "Open-source 236B-parameter coding model available via OpenRouter or the DeepSeek API, recommended as roughly 20x cheaper than Claude while remaining highly capable for AI coding."
resource: "https://www.deepseek.com"
tags: [llm, model, open-source]
videos: [the-king-of-no-code-ai-agent-builders, how-to-use-boltnew-for-free-with-local-llms-and-no-rate-limits, im-building-the-best-open-source-ai-coding-assistant-with-your-help]
created: 2026-07-21
updated: 2026-07-21
---

# DeepSeek Coder V2

DeepSeek Coder V2 is DeepSeek's open-source coding model, and its 236-billion-parameter version was Cole's standing recommendation through late 2024 for anyone who wanted frontier-adjacent code generation without a frontier bill. He names it without hedging: "using my favorite open source model for coding which is deep SE coder version 2 the 236 billion parameter version I'm doing this through open router" [0:17:29]. Access is either [OpenRouter](./openrouter.md) or the DeepSeek API directly, and he treats those as interchangeable front doors to the same weights.

The argument for it is almost entirely economic. Pricing it out against the closed models, he lands on "14 cents per million input tokens and 28 cents per million output tokens this is so much better than Claude" [0:09:28], roughly a twentieth of the cost. That is the reason it shows up as the default recommendation in his browser-based coding tools rather than as a curiosity: cheap tokens change what you are willing to iterate on, which is the whole premise of [LLM cost optimization](../../concepts/llm-cost-optimization.md) and of [iterative prompting](../../concepts/iterative-prompting.md) where you deliberately burn several passes getting from an ugly baseline to a real app.

It is also fast enough to feel free. Generating a front-end wrapper for a [Voiceflow](./voiceflow.md) agent through his [autodev](./autodev.md) fork, he notes the turnaround: "like 15 seconds later and deep SE coder has now given us the HTML file for our voice flow agent interface" [0:17:45], for well under a penny. And when planning the roadmap for his community fork he calls out first-party access as a priority "integration with the Deep seek API because the deep-seat coder models especially the 236 billion parameter one absolutely kick butt" [0:11:36].

Positioned in his model lineup, Coder V2 is the code-specialized sibling to the general-purpose [DeepSeek V3](./deepseek-v3.md) and the reasoning-focused [DeepSeek R1](./deepseek-r1.md). It is open-weight, so it can in principle be self-hosted, but in every appearance he routes to it as an API because 236B parameters is far past what a laptop running [Ollama](./ollama.md) can serve.

## Realizes

- [LLM Cost Optimization](../../concepts/llm-cost-optimization.md) - Systematically cutting the bill for running LLM applications at scale by sending the bulk of cheap-to-serve traffic to far cheaper models and paying premium rates only for the rare hard requests.
- [Open-Source & Local AI Coding](../../concepts/open-source-ai-coding.md) - Community-maintained, self-hostable AI coding tools and local models that dodge API costs and rate limits.

## Works with

- [OpenRouter](./openrouter.md) - Unified API gateway to many LLMs; the route Cole uses to reach Coder V2 without a DeepSeek account.
- [autodev (bolt.new fork)](./autodev.md) - Cole's community-built fork of bolt.new, driven by Coder V2 to generate a front-end wrapper for under a penny.
- [oTToDev (autod Dev)](./ottodev.md) - Community fork of bolt.new that adds support for any LLM, including local models via Ollama; the tool this recommendation lands in.
- [bolt.new](./bolt-new.md) - StackBlitz's commercial AI coding platform that generates entire full-stack applications; the stable product the forks branch from.

## Contrasts with

- [Claude](./claude.md) - The closed frontier model Coder V2 is priced against at roughly 20x the cost.
- [DeepSeek V3](./deepseek-v3.md) - New open model Cole cites as evidence the local-vs-closed gap is closing fast; the general-purpose successor to the Coder line.
- [DeepSeek R1](./deepseek-r1.md) - Open-source MIT-licensed reasoning LLM that rivals OpenAI o1, ships in distilled sizes, and is far cheaper to run.
- [Qwen 2.5 Coder 32B](./qwen.md) - Alibaba's open-source LLM family, small enough to actually run locally where Coder V2's 236B is not.

## Related

- [Model Selection](../../concepts/model-selection.md) - Choosing the right LLM per task by trading off quality, speed, and cost, often routing easy requests to cheap models and hard ones to expensive models.
- [Provider Independence](../../concepts/provider-independence.md) - Architecting agents so the underlying model, framework, or client can be swapped without a rewrite, avoiding lock-in through low-level abstractions.
- [Browser-Based AI Coding Tools](../../concepts/browser-based-ai-coding.md) - In-browser coding tools that import git repos and local projects to get you started fast, but stall on directed refinement vs AI IDEs.
- [Iterative Prompting](../../concepts/iterative-prompting.md) - Build complex software by prompting for a minimal baseline first and adding one change at a time to minimize hallucination.
- [Community-Driven Development](../../concepts/community-driven-development.md) - Building products and open source in public with a community, using a public roadmap and shared learning.

## Sources

- [The KING of No Code AI Agent Builders?!](../../sources/the-king-of-no-code-ai-agent-builders.md) - "[0:17:29] using my favorite open source model for coding which is deep SE coder version 2 the 236 billion parameter version I'm doing this through open router"
- [The KING of No Code AI Agent Builders?!](../../sources/the-king-of-no-code-ai-agent-builders.md) - "[0:17:45] like 15 seconds later and deep SE coder has now given us the HTML file for our voice flow agent interface"
- [How to Use Bolt.new for FREE with Local LLMs (And NO Rate Limits)](../../sources/how-to-use-boltnew-for-free-with-local-llms-and-no-rate-limits.md) - "[0:08:52] I would highly recommend using deepseeker version 2 the 236 billion parameter version you can get this either through open router or through the Deep seek API directly"
- [How to Use Bolt.new for FREE with Local LLMs (And NO Rate Limits)](../../sources/how-to-use-boltnew-for-free-with-local-llms-and-no-rate-limits.md) - "[0:09:28] 14 cents per million input tokens and 28 cents per million output tokens this is so much better than Claude"
- [I'm Building the BEST Open Source AI Coding Assistant with YOUR Help](../../sources/im-building-the-best-open-source-ai-coding-assistant-with-your-help.md) - "[0:11:36] integration with the Deep seek API because the deep-seat coder models especially the 236 billion parameter one absolutely kick butt"
