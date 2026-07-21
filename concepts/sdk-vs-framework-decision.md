---
type: concept
title: "SDK vs. Framework Decision"
description: "Choosing between a batteries-included coding-agent SDK and a from-scratch agent framework based on who uses the agent and tolerance for speed, cost, and determinism."
tags: [sdk, framework, cost, latency]
videos: [everything-you-thought-about-building-ai-agents-is-wrong]
created: 2026-07-21
updated: 2026-07-21
---

# SDK vs. Framework Decision

When you build an agent you face an early fork: reach for a batteries-included coding-agent SDK (like the Claude Agent SDK or Codex SDK) or build on a lower-level agent framework (like Pydantic AI or LangGraph). Cole reduces the choice to two questions: "it really just comes down to two questions to ask yourself. Who is going to use your agent? And what is your tolerance for things like speed and scale?" [0:11:52] Everything else follows from those two answers.

If the agent is for you or a small team and latency is not critical, the SDK wins on speed of development: "If it is just you using the agent and some delay is okay, you don't need to scale, then I would highly recommend going with the Claude Agent SDK or Codex SDK." [0:12:05] These SDKs come pre-wired with a capable [agent loop](./agent-loop.md), tool handling, and a strong default model, so you get to a working agent fast. The trade is control: they are heavier, can be slower and pricier per run, and hide the internals.

If instead the agent ships to many users on a production platform where speed and scale matter, a framework is the better fit: "if a lot of other people are using your agent, you're deploying it to a production platform, it needs to scale and be fast, then you still should go with... a framework like Pydantic AI or LangGraph." [0:12:21] A framework gives you tighter control over cost, latency, and determinism, at the price of assembling more of the agent yourself. The decision is therefore about audience and tolerances, not about which tool is objectively "best."

## Related

- [AI Coding Harness](./ai-coding-harness.md) - what a coding-agent SDK packages for you.
- [Model Selection](./model-selection.md) - an SDK bundles a default model; a framework leaves it open.
- [Provider Independence](./provider-independence.md) - a framework makes it easier to stay portable across providers.

## Tools

- [Claude Agent SDK](../entities/tools/claude-agent-sdk.md) - the batteries-included SDK Cole recommends for solo use.
- [Codex](../entities/tools/codex.md) - OpenAI's coding-agent SDK, the other SDK option.
- [Pydantic AI](../entities/tools/pydantic-ai.md) - the framework Cole names for production, scalable agents.
- [LangGraph](../entities/tools/langgraph.md) - the other framework named for scale and speed.

## Sources

- [Everything You Thought About Building AI Agents is Wrong](../sources/everything-you-thought-about-building-ai-agents-is-wrong.md) - "[0:11:52] it really just comes down to two questions to ask yourself. Who is going to use your agent? And what is your tolerance for things like speed and scale?"
