---
type: concept
title: "Guardrails"
description: "Constraints and checks that keep agents from hallucinating, going off the rails, or emitting unsafe output."
tags: [guardrails, hallucination, safety]
videos: [learn-90-of-building-ai-agents-in-30-minutes, my-top-20-lessons-from-building-100s-of-ai-agents-super-actionable, build-and-ship-any-mcp-server-in-minutes-full-guide, ai-code-that-fixes-itself-an-mcp-you-can-try-now, how-id-learn-ai-agents-fast-if-i-had-to-start-over-full-roadmap, google-anthropic-and-openais-guides-to-ai-agents-all-in-18-minutes, give-me-28-minutes-and-ill-completely-change-the-way-you-build-ai-agents, openais-brand-new-agents-sdk-crash-course, weve-been-building-ai-agents-wrong-until-now, function-calling-with-any-llm-for-local-ai-agents-feat-langchain-huggingface-and-llama-3]
created: 2026-07-21
updated: 2026-07-21
---

# Guardrails

Guardrails are deterministic checks wrapped around an agent that catch bad input before it reaches the model and bad output before it reaches the user. Cole's definition is deliberately plain: "what guardrails are is just a piece of logic that you have that runs either before you call into your agent or your LLM or after." [0:16:05] The pattern is symmetric, "we have input guardrails making sure that we don't have garbage that's sent to our agent. And then we have output guardrails, making sure that there's no garbage that is sent to the end user." [0:11:47]

They exist because hallucination is inevitable: "no matter how powerful of an LLM you are using, it is going to hallucinate. And so making sure those hallucinations don't affect our AI system as a whole is all based around how good our guard rails are." [0:11:23] Worse, errors compound. Cole warns of the "hallucination explosion... compounding non-determinism" [0:12:00]: "if you have three agents that each individually work well 95% of the time... that means that your whole system is only actually going to work 86% of the time." [0:12:36] Guardrails are what arrest that decay.

Concretely, guardrails take several forms. **Action limits**, "if it's interacting with our database maybe only making sure it can use readonly tools." [0:11:39] **Input filtering**, keeping PII and secrets out of the prompt entirely. [0:15:48] **Tripwires** that abort a run, in the OpenAI Agents SDK, "safety checks that you can create... you validate input and output for your llms and you can stop responses from happening if you detect hallucinations" [0:02:06], where a trip wire "cut[s] the execution short" when a value is unrealistic. [0:21:13] **Critic and evaluator nodes** that check output completeness before it proceeds. [0:18:30] **Model retry** on transient failures like an overload error. [0:10:49] And for coding agents, a **knowledge-graph hallucination check**: "it's all just deterministic code going out to the knowledge graph" to confirm a method actually exists on a class. [0:03:55]

Cole singles out guardrails as an underserved feature, "something super important that I don't see in Frameworks usually... I don't see guard rails enough." [0:22:47] Where they exist, they are the difference between a demo and reliability: "These kind of things are what is so important to make our AI agents actually reliable." [0:12:02]

## Prerequisites

- [Validation](./validation.md)

## Related

- [Human in the Loop](./human-in-the-loop.md) - a guardrail where the check is a person approving before the agent proceeds.
- [Adversarial Agents](./adversarial-agents.md)
- [Agent Evaluation](./agent-evaluation.md)
- [Deterministic Workflows](./deterministic-workflows.md)
- [Agents vs. Workflows](./agents-vs-workflows.md)
- [Agent Graphs](./agent-graphs.md)
- [Self-Reflective RAG](./self-reflective-rag.md)
- [Knowledge Graphs](./knowledge-graphs.md)
- [Context Window Limits](./context-window-limits.md)
- [End-to-End Validation](./end-to-end-validation.md)
- [Agent Core Components](./agent-core-components.md)

## Tools

- [OpenAI Agents SDK](../entities/tools/openai-agents-sdk.md) - first-class guardrails with custom tripwires.
- [Pydantic AI](../entities/tools/pydantic-ai.md) - built-in model retry on overload/validation errors.
- [Neo4j](../entities/tools/neo4j.md) - the knowledge graph behind deterministic hallucination detection.

## Sources

- [My Top 20 Lessons from Building 100s of AI Agents (Super Actionable)](../sources/my-top-20-lessons-from-building-100s-of-ai-agents-super-actionable.md) - "[0:16:05] what guardrails are is just a piece of logic that you have that runs either before you call into your agent or your LLM or after."
- [How I'd Learn AI Agents FAST if I Had to Start Over (Full Roadmap)](../sources/how-id-learn-ai-agents-fast-if-i-had-to-start-over-full-roadmap.md) - "[0:11:47] we have input guardrails making sure that we don't have garbage that's sent to our agent. And then we have output guardrails, making sure that there's no garbage that is sent to the end user."
- [Google, Anthropic, and OpenAI's Guides to AI Agents ALL in 18 Minutes](../sources/google-anthropic-and-openais-guides-to-ai-agents-all-in-18-minutes.md) - "[0:11:23] no matter how powerful of an LLM you are using, it is going to hallucinate... all based around how good our guard rails are."
- [My Top 20 Lessons from Building 100s of AI Agents (Super Actionable)](../sources/my-top-20-lessons-from-building-100s-of-ai-agents-super-actionable.md) - "[0:12:36] if you have three agents that each individually work well 95% of the time... that means that your whole system is only actually going to work 86% of the time."
- [OpenAI's BRAND NEW Agents SDK (Crash Course)](../sources/openais-brand-new-agents-sdk-crash-course.md) - "[0:02:06] guard rails this is something super important... you validate input and output for your llms and you can stop responses from happening if you detect hallucinations"
- [Give Me 28 Minutes and I'll Completely Change the Way You Build AI Agents](../sources/give-me-28-minutes-and-ill-completely-change-the-way-you-build-ai-agents.md) - "[0:06:35] Then we have guardrail nodes and these are crucial to make our AI agents much more reliable. You have both input guardrails and output guardrails."
- [AI Code That Fixes Itself (An MCP You Can Try Now)](../sources/ai-code-that-fixes-itself-an-mcp-you-can-try-now.md) - "[0:03:55] I even have a script that leverages the knowledge graph to check for these hallucinations... it's all just deterministic code going out to the knowledge graph."
- [We've Been Building AI Agents WRONG Until Now](../sources/weve-been-building-ai-agents-wrong-until-now.md) - "[0:10:49] model retry this is something that's so important that other Frameworks don't include I can tell it like if there is an overload error... it can retry another time"
- [Learn 90% of Building AI Agents in 30 Minutes](../sources/learn-90-of-building-ai-agents-in-30-minutes.md) - "[0:15:48] one thing that you want to avoid quite often is inserting any kind of PII, personally identifiable information into a prompt to an LLM"
- [Function Calling with ANY LLM for Local AI Agents](../sources/function-calling-with-any-llm-for-local-ai-agents-feat-langchain-huggingface-and-llama-3.md) - "[0:15:14] local models are not as powerful as GPT and Claude... there's a lot of hallucinations that can happen here"
- [Build and Ship Any MCP Server in MINUTES (Full Guide)](../sources/build-and-ship-any-mcp-server-in-minutes-full-guide.md) - "[0:19:17] You want to make sure that you handle errors gracefully, maybe even having the MCP server return an error message so the agent can communicate back to the user"
