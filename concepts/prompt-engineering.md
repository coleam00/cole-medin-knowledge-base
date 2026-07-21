---
type: concept
title: "Prompt Engineering"
description: "The craft of wording, structuring, and constraining a prompt so an LLM reliably produces the answer you want, one piece of the larger context-engineering picture that Cole considers mostly over-hyped with only a small transferable core worth learning."
tags: [prompt-engineering, prompting, llm, fundamentals, context-engineering, output-format, steering]
videos: [build-render-entire-videos-with-claude-code-full-workflow, context-engineering-is-the-new-vibe-coding-learn-this-now, how-to-dominate-with-ai-in-2025, i-found-the-limits-of-the-most-popular-llms, prompt-engineering-is-a-bunch-of-bs-heres-the-5-of-it-to-learn, the-only-ai-developer-roadmap-you-need-in-2024, chatgpt-teaches-the-secrets-to-financial-freedom, 3-most-important-prompt-engineering-techniques-you-need-to-know, how-to-use-gpt4-to-grow-on-twitter-the-right-way]
created: 2026-07-21
updated: 2026-07-21
---

# Prompt Engineering

Prompt engineering is the craft of wording a request so the model gives you the answer you actually want. As Cole puts it, "Prompt engineering is all about tweaking wording, phrasing things in a specific way to get a single good answer from the LLM" [0:03:00], or more bluntly, "all prompt engineering is is crafting your questions to the AI in a way to get the answer that you want so if you're bad at prompt engineering you're going to get bad answers from the AI" [0:00:00]. The lever is precision: being clear about the format you want ("you can also be very clear in the format you're looking for" [0:01:13]), using deliberate adjectives, and stating explicit constraints like a character limit or excluded elements.

## Why it matters (and where it's over-hyped)

Cole's strongest position is that the field is mostly noise around a small, durable core. "Prompt engineering is important but most of it is just fluff it's just a bunch of BS" [0:00:43]. His practical prescription: "in general just study prompt engineering for like 3 to 5 hours and then go build what you want to build don't spend 20 hours 40 hours 100 hours" [0:00:57]. The techniques he singles out as genuinely worth knowing are chain-of-thought, single-shot and few-shot, self-consistency, general-knowledge prompting, and prompt chaining ("self-consistency general knowledge prompting and prompt chaining these are all really good" [0:01:24]).

The high-leverage insight is portability. "learning how to prompt specifically for one llm is pretty low leverage but learning the overarching stuff in these techniques is very high leverage" [0:24:06]. Learn the transferable patterns, not one model's quirks. A recurring worked structure is the three-step "context, then the ask": give the model background, then your specifics, then "the right hook you give the ask" [0:13:40], often telling it to give its opinion directly rather than hedge. Prompt engineering also shows up in unexpected places, like adding tags, breaks, and abbreviations to "optimize for our text to speech" [0:08:25]. And clearer prompts let weaker, cheaper models succeed: "I can always make my tools clearer I can give better instructions ... to make it so weaker models can actually perform these actions" [0:26:41].

## Part of

- [Context Engineering](./context-engineering.md) is the larger picture; prompting "is just one piece" [0:03:17] of it.

## Related

- [Role Prompting](./role-prompting.md), [Few-Shot Prompting](./few-shot-prompting.md), [Chain-of-Thought Prompting](./chain-of-thought.md), and [Effective Prompting](./effective-prompting.md) are the core transferable techniques.
- [Prompting Techniques for AI Coding](./ai-coding-prompting.md) and [Agent Prompting Techniques](./agent-prompting.md) apply the craft to coding agents.
- [Reduce Assumptions](./reduce-assumptions.md), [Self-Correcting Agents](./self-correction.md), [Adversarial Agents](./adversarial-agents.md), [Model Selection](./model-selection.md), [Reasoning Models](./reasoning-models.md), [Capabilities Over Tools](./capabilities-over-tools.md), [The Agent Loop (Reason-Act-Observe)](./agent-loop.md), and [Learn by Building](./learn-by-building.md).

## Sources

- ["Prompt Engineering" is a Bunch of BS - Here's the 5% of it to Learn](../sources/prompt-engineering-is-a-bunch-of-bs-heres-the-5-of-it-to-learn.md) - "[0:00:43] prompt engineering is important but most of it is just fluff it's just a bunch of BS"
- [Context Engineering is the New Vibe Coding (Learn this Now)](../sources/context-engineering-is-the-new-vibe-coding-learn-this-now.md) - "[0:03:00] Prompt engineering is all about tweaking wording, phrasing things in a specific way to get a single good answer from the LLM."
- [How to DOMINATE with AI in 2025](../sources/how-to-dominate-with-ai-in-2025.md) - "[0:24:06] learning how to prompt specifically for one llm is pretty low leverage but learning the overarching stuff in these techniques is very high leverage"
- [3 MOST Important Prompt Engineering Techniques you NEED to know!](../sources/3-most-important-prompt-engineering-techniques-you-need-to-know.md) - "[0:00:00] all prompt engineering is is crafting your questions to the AI in a way to get the answer that you want"
- [How to Use GPT4 To Grow on Twitter The Right Way](../sources/how-to-use-gpt4-to-grow-on-twitter-the-right-way.md) - "[0:01:13] you can also be very clear in the format you're looking for which is another big thing that's super helpful"
- [The ONLY AI Developer Roadmap You Need in 2024](../sources/the-only-ai-developer-roadmap-you-need-in-2024.md) - "[0:04:21] things like Chain of Thought self-reflection one shot few shot all the different prompt engineering techniques because you want to have that in your back pocket"
- [ChatGPT Teaches the Secrets to Financial Freedom!?](../sources/chatgpt-teaches-the-secrets-to-financial-freedom.md) - "[0:13:40] it's really a three-step process you first give context about a book ... and then you give that right hook you give the ask"
- [I Found the Limits of the Most Popular LLMs](../sources/i-found-the-limits-of-the-most-popular-llms.md) - "[0:26:41] I can always make my tools clearer I can give better instructions for how to give arguments things like that to make it so weaker models can actually perform these actions"
- [Build + Render ENTIRE Videos with Claude Code (Full Workflow)](../sources/build-render-entire-videos-with-claude-code-full-workflow.md) - "[0:08:25] There is a lot of prompt engineering that goes into adding in tags and breaks and natural abbreviations to really optimize for our text to speech"
