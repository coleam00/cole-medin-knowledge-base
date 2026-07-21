---
type: concept
title: "Agent Evaluation"
description: "Systematically scoring agent behavior with evals and benchmarks, including as a gate before deployment."
tags: [evals, benchmarks, testing]
videos: [this-completely-changes-the-way-we-build-production-ai-agents-vercel-eve, claude-skills-arent-just-for-claude-heres-how-to-build-them-for-any-agent, is-gemini-3-really-the-best-ai-ever, how-id-learn-ai-agents-fast-if-i-had-to-start-over-full-roadmap, google-anthropic-and-openais-guides-to-ai-agents-all-in-18-minutes, revealing-my-complete-ai-agent-blueprint, weve-been-building-ai-agents-wrong-until-now, i-found-the-limits-of-the-most-popular-llms, new-llama-3-model-beats-gpt-and-claude-with-function-calling]
created: 2026-07-21
updated: 2026-07-21
---

# Agent Evaluation

Agent evaluation is the systematic scoring of whether an agent actually behaves correctly, distinct from ordinary software testing. Cole draws the line sharply: "evaluation is ensuring the agent actually gives correct responses and takes correct action so you give it certain inputs and you say is it doing the right thing" [0:12:39], and it "is one of the more hard things to do with agents especially because there's not a lot of tools out there to make it possible but it's very different than testing." [0:12:23] Where a unit test checks deterministic code, an eval checks non-deterministic *behavior*: did the agent choose the right tools, follow the right steps, and land the right answer.

The recurring claim across the catalog is where the real work lives: building an agent "is 25% coding or automating and then 75% evaluating because it's easy to get to that first 90% for your agent" [0:14:10]. That last stretch, "to really make your agent great, you have to evaluate constantly and you have to constantly be tweaking your tools and your fine-tuning and your system prompt and your knowledge base." [0:14:10] Evaluation is the loop that closes over every other lever.

The dominant technique is LLM-as-a-judge: "using another large language model to evaluate the output of our agent." [0:15:54] Evals are often packaged as a folder of test cases with expected tool calls, then run as "a deploy gate... making sure that you get green check marks across the board before you deploy that update." [0:04:27] In one skills example, "25 out of 25 cases have passed" after sending "a lot of different requests to make sure the agent properly understands all of the skills." [0:21:54] To keep this affordable, agents are wired with a test/mock model so "you don't actually have to call a large language model to run your unit or integration test... you never really want to pay real money when you're running your tests." [0:05:26]

Public benchmarks are treated with suspicion. "Our benchmarks just don't resemble how we are actually using large language models in the wild... for coding specifically, it's all just a bunch of leak code style puzzles." [0:08:40] Standardized leaderboards (like the Berkeley function-calling leaderboard) have their place, but Cole's honest bar is to "try it yourself, wait for millions of other people to try it, and then establish a kind of common opinion." [0:00:52]

## Prerequisites

- [Validation](./validation.md)
- [End-to-End Validation](./end-to-end-validation.md)

## Related

- [Agent Observability](./agent-observability.md)
- [Guardrails](./guardrails.md)
- [Adversarial Agents](./adversarial-agents.md)
- [Production-Grade Agents](./production-grade-agents.md)
- [Real-World Coding Benchmarks](./coding-benchmarks.md)
- [Deterministic Workflows](./deterministic-workflows.md)
- [Model Selection](./model-selection.md)
- [Agentic Workflow Engineering](./agentic-workflow-engineering.md)
- [AI Coding Harness](./ai-coding-harness.md)

## Tools

- [Pydantic AI](../entities/tools/pydantic-ai.md) - its test/mock model lets you run evals without paying for real LLM calls.
- [Claude Code](../entities/tools/claude-code.md)

## Sources

- [Revealing my COMPLETE AI Agent Blueprint](../sources/revealing-my-complete-ai-agent-blueprint.md) - "[0:12:39] evaluation is ensuring the agent actually gives correct responses and takes correct action so you give it certain inputs and you say is it doing the right thing"
- [Google, Anthropic, and OpenAI's Guides to AI Agents ALL in 18 Minutes](../sources/google-anthropic-and-openais-guides-to-ai-agents-all-in-18-minutes.md) - "[0:14:10] building AI agents is 25% coding or automating and then 75% evaluating because it's easy to get to that first 90% for your agent"
- [How I'd Learn AI Agents FAST if I Had to Start Over (Full Roadmap)](../sources/how-id-learn-ai-agents-fast-if-i-had-to-start-over-full-roadmap.md) - "[0:15:54] We have the whole idea of LLM as a judge, like using another large language model to evaluate the output of our agent."
- [This Completely Changes the Way We Build Production AI Agents (Vercel Eve)](../sources/this-completely-changes-the-way-we-build-production-ai-agents-vercel-eve.md) - "[0:04:27] they also have evals as a deploy gate... making sure that you get green check marks across the board before you deploy that update."
- [Claude Skills Aren't Just for Claude - Here's How to Build Them for ANY Agent](../sources/claude-skills-arent-just-for-claude-heres-how-to-build-them-for-any-agent.md) - "[0:21:54] at the bottom here, 25 out of 25 cases have passed."
- [We've Been Building AI Agents WRONG Until Now](../sources/weve-been-building-ai-agents-wrong-until-now.md) - "[0:05:26] being able to have a test model so you don't actually have to call a large language model to run your unit or integration test because you never really want to pay real money when you're running your tests"
- [Is Gemini 3 Really the Best AI Ever?](../sources/is-gemini-3-really-the-best-ai-ever.md) - "[0:08:40] Our benchmarks just don't resemble how we are actually using large language models in the wild."
- [I Found the Limits of the Most Popular LLMs](../sources/i-found-the-limits-of-the-most-popular-llms.md) - "[0:02:23] you could throw it into this framework and it would actually run automated tests to try to break the llm and then spit out some sort of score"
- [New Llama 3 Model BEATS GPT and Claude with Function Calling!?](../sources/new-llama-3-model-beats-gpt-and-claude-with-function-calling.md) - "[0:00:48] The way that they're benchmarking this is with the Berkeley function calling leaderboard"
