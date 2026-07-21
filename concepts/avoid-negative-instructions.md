---
type: concept
title: "Avoid Negative Instructions"
description: "Tell the model what to do rather than what not to do, since positive, concrete instructions are far more reliable than prohibitions."
tags: [prompting, positive-instructions, clarity, best-practices]
videos: [my-top-20-lessons-from-building-100s-of-ai-agents-super-actionable]
created: 2026-07-21
updated: 2026-07-21
---

# Avoid Negative Instructions

Avoiding negative instructions is the practice of phrasing prompts as what the model should do, not what it should not do. Cole frames it as a hard-won lesson from building hundreds of agents: "you want to avoid adding what I like to call negatives. And this is especially true for longer system prompts" ([0:23:48]). A "negative" is any prohibition, a "do not," a "never," a "don't."

## Why it matters

The failure mode is specific and reliable: models tend to drop the negation and act on the residual instruction. "LLMs, they love to drop the negative, as in they will kind of like take out the do not and then they'll do the very thing that you told them not to do" ([0:24:20]). A line like "do not mention pricing" carries the token "pricing" into the model's active context, and when the negation gets lost the model does exactly the forbidden thing. The risk compounds in longer system prompts, where a single prohibition sits far from the context that would keep it in force.

The fix is to invert every prohibition into a positive, concrete directive. Instead of "don't be verbose," say "answer in two sentences." Instead of "never call the delete tool without confirmation," say "always confirm with the user before calling the delete tool." Positive instructions give the model a target behavior to execute rather than a behavior to suppress, which is both easier to follow and easier to verify. Where a rule is genuinely hard to state positively, a concrete example of the desired output often does the work a prohibition cannot, which is why this pairs naturally with [few-shot prompting](./few-shot-prompting.md).

## Related

- [Few-Shot Prompting](./few-shot-prompting.md)
- [Reduce Assumptions](./reduce-assumptions.md)
- [System Prompt Engineering](./system-prompt-engineering.md)
- [Effective Prompting](./effective-prompting.md)
- [Prompt Engineering](./prompt-engineering.md)

## Sources

- [My Top 20 Lessons from Building 100s of AI Agents (Super Actionable)](../sources/my-top-20-lessons-from-building-100s-of-ai-agents-super-actionable.md) - "[0:24:20] LLMs, they love to drop the negative, as in they will kind of like take out the do not and then they'll do the very thing that you told them not to do."
