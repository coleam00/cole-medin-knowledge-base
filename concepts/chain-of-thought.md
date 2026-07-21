---
type: concept
title: "Chain-of-Thought Prompting"
description: "Prompting the model to reason step by step before answering, optionally sampling multiple reasoning paths and taking the most consistent answer (self-consistency) to improve reliability."
tags: [prompt-engineering, reasoning, chain-of-thought, self-consistency, technique, prompting, step-by-step]
videos: [this-boltnew-fork-is-exploding-dont-miss-out-on-whats-happening, prompt-engineering-is-a-bunch-of-bs-heres-the-5-of-it-to-learn]
created: 2026-07-21
updated: 2026-07-21
---

# Chain-of-Thought Prompting

Chain-of-thought prompting asks the model to reason step by step before it commits to an answer, so the intermediate reasoning becomes part of the context that shapes the final output. Cole lists it among the small set of prompting techniques actually worth learning: "few shot prompting Chain of Thought prompting um self-consistency general knowledge prompting and prompt chaining" ([0:01:24]). Its close cousin, self-consistency, samples several independent reasoning paths and takes the most common answer, trading a few extra tokens for higher reliability on problems where a single pass might slip.

## How it works and why it matters

The technique is deployed structurally inside real coding systems, not just in chat. In the Bolt.new fork, a deliberate reasoning step was baked into the main system prompt: "a little bit of Chain of Thought prompting within the main Bolt.new prompt just to get the llm to think a little bit before it spits out all the code" ([0:05:06]). A community contributor then formalized it: "Kofi added the structured planning step like kind of like that Chain of Thought to improve the prompting" ([0:09:35]). The lesson is that forcing a plan-before-code beat measurably improves output quality, because the model reasons about the whole task before producing any single line.

Chain-of-thought is a prompting technique that induces reasoning in an ordinary model, which is a useful contrast with [reasoning models](./reasoning-models.md) that do this reasoning natively and internally. When the model already reasons on its own, an explicit "think step by step" instruction adds less. It also underpins structured [planning with AI](./planning-with-ai.md), where the reasoning step is elevated into an explicit, reviewable plan.

## Builds on

- [Prompt Engineering](./prompt-engineering.md)

## Contrasts with

- [Reasoning Models](./reasoning-models.md)

## Related

- [Planning with AI](./planning-with-ai.md)
- [The Agent Loop (Reason-Act-Observe)](./agent-loop.md)
- [Few-Shot Prompting](./few-shot-prompting.md)
- [Effective Prompting](./effective-prompting.md)

## Tools

- [Bolt.new](../entities/tools/bolt-new.md)
- [Bolt.diy](../entities/tools/bolt-diy.md)

## Sources

- [This Bolt.new Fork is EXPLODING - Don't Miss out on What's Happening!](../sources/this-boltnew-fork-is-exploding-dont-miss-out-on-whats-happening.md) - "[0:05:06] a little bit of Chain of Thought prompting within the main Bolt.new prompt just to get the llm to think a little bit before it spits out all the code"
- ["Prompt Engineering" is a Bunch of BS - Here's the 5% of it to Learn](../sources/prompt-engineering-is-a-bunch-of-bs-heres-the-5-of-it-to-learn.md) - "[0:01:24] few shot prompting Chain of Thought prompting um self-consistency general knowledge prompting and prompt chaining"
