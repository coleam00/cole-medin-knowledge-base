---
type: concept
title: "Self-Criticism Prompting"
description: "Having the model critique and revise its own output in the prompt loop so it catches errors and improves the answer before returning it."
tags: [prompting, self-critique, reflection, self-improvement]
videos: [chatgpt-is-the-gift-that-keeps-on-giving-introducing-auto-gpt]
created: 2026-07-21
updated: 2026-07-21
---

# Self-Criticism Prompting

Self-criticism prompting asks the model to turn on its own output: review what it just produced, find the weaknesses, and revise before returning a final answer. Cole describes it as a way to force the model off its first, single-angle response: it "uses a technique that I already showed on my YouTube channel where it criticizes itself to really make sure that it is thinking about things from different angles" [0:08:54]. The prompt loop deliberately builds in a critique step so the model does not just commit to its initial draft.

## How it works

There are two related flavors of the same move. The model can critique its answer directly, or it can critique the prompt it was given and propose a better one: "you basically have it criticize itself or have it think about a way you could give a better prompt for it so it's kind of self-aware in both cases" [0:11:47]. Both push the model to reconsider from a fresh vantage point instead of anchoring on the first completion. This is the prompting-level primitive underneath autonomous agent loops (the technique appears in Cole's Auto-GPT walkthrough), where a self-critique pass is how the agent checks and corrects itself between steps rather than blindly executing.

## Related

- [Self-Correcting Agents](./self-correction.md) is the agent-loop generalization: self-criticism wired into a runtime feedback cycle.
- [Adversarial Agents](./adversarial-agents.md) externalize the critique into a separate critic model rather than the same model reviewing itself.
- [Effective Prompting](./effective-prompting.md) and [Agentic Coding](./agentic-coding.md) are where this technique is applied in practice.

## Sources

- [ChatGPT is the GIFT that keeps on GIVING - Introducing Auto-GPT](../sources/chatgpt-is-the-gift-that-keeps-on-giving-introducing-auto-gpt.md) - "[0:08:54] it uses a technique that I already showed on my YouTube channel where it criticizes itself to really make sure that it is thinking about things from different angles"
