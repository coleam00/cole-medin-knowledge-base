---
type: concept
title: "Prompt Versioning"
description: "Treating prompts as versioned artifacts so changes can be tracked, compared, and rolled back as the agent evolves."
tags: [prompting, versioning, prompt-management, iteration]
videos: [my-top-20-lessons-from-building-100s-of-ai-agents-super-actionable]
created: 2026-07-21
updated: 2026-07-21
---

# Prompt Versioning

Prompt versioning treats a prompt as a first-class, tracked artifact rather than a string you overwrite in place. It is one of Cole's concrete system-prompt lessons from building hundreds of agents: "the next system prompt tip that I have for you guys is to version your prompts" [0:28:44]. Because a system prompt is the primary behavioral surface of an agent, changing it is a change to the product, and those changes deserve the same discipline you give code: a history you can compare against and roll back to when a "small tweak" quietly makes the agent worse.

## Why it matters

Prompts drift as the agent evolves. You add a rule to fix one edge case, tighten the persona, adjust the output format, and three iterations later you cannot say which change caused a regression. Versioning gives you that lineage. Cole points to two practical homes for it: a dedicated prompt-management tool, and plain source control. "Langfuse is a really good one for sure ... and then also just like having a separate place in your GitHub repository for your prompts" [0:29:40]. The GitHub option is the low-friction default: keep prompts in their own tracked files so every edit is a diff, reviewable and revertible, instead of an opaque overwrite buried in application code. This pairs naturally with reducing assumptions, since a clear, unambiguous prompt is the thing worth preserving and iterating on deliberately.

## Related

- [Reduce Assumptions](./reduce-assumptions.md) is the quality bar each prompt version should meet: explicit, non-contradictory instructions.
- [System Prompt Engineering](./system-prompt-engineering.md) is what you are versioning; the persona, rules, and output format that define agent behavior.

## Sources

- [My Top 20 Lessons from Building 100s of AI Agents (Super Actionable)](../sources/my-top-20-lessons-from-building-100s-of-ai-agents-super-actionable.md) - "[0:28:44] the next system prompt tip that I have for you guys is to version your prompts."
