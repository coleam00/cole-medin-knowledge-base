---
type: concept
title: "Zero-Shot Prompting"
description: "Asking an LLM to perform a task with no examples at all, relying purely on the instruction and the model's pretrained knowledge; the baseline counterpart to few-shot prompting."
tags: [prompt-engineering, llm, prompting, technique, baseline]
videos: [prompt-engineering-is-a-bunch-of-bs-heres-the-5-of-it-to-learn]
created: 2026-07-21
updated: 2026-07-21
---

# Zero-Shot Prompting

Zero-shot prompting is the plain case: you state the task and nothing else. No worked examples, no demonstration of the output format, no sample of the voice you want. The model has to bridge the gap from instruction to answer using only what it absorbed in pretraining. It is the default mode almost every user is already in without naming it, which is exactly why it is worth naming - once it has a label, "add examples" becomes a deliberate move rather than an accident.

Cole puts it on the short list of techniques actually worth learning, at the front of a group he singles out from the sprawl of named prompt-engineering tricks: "The first like six of these techniques here I'd recommend learning like zero shot prompting" [0:01:24]. That framing matters because his broader argument is that most of [prompt engineering](./prompt-engineering.md) is noise and only a small fraction earns its keep. Zero-shot makes the cut not because it is clever but because it is the baseline you measure everything else against.

The practical discipline is to treat zero-shot as the thing you try first and escalate from. Modern instruction-tuned models handle a large share of ordinary tasks - summarize this, classify that, rewrite this paragraph - with no examples at all, and every example you add spends context budget and biases the output toward the shape you demonstrated. So the sequence is: write a clear zero-shot instruction, look at what breaks, and only then reach for a heavier technique. If the *reasoning* is wrong, [chain-of-thought](./chain-of-thought.md) is the escalation. If the *format or voice* is wrong, [few-shot prompting](./few-shot-prompting.md) is - examples are how you pin down an output shape that prose cannot describe. If the model is answering as the wrong kind of expert, [role prompting](./role-prompting.md) is.

The failure mode of skipping the baseline is over-engineering: piling examples, personas, and step-by-step scaffolding onto a prompt that a single clear sentence would have handled, and then having no idea which piece is doing the work. Zero-shot is also the honest test of whether a task needs [effective prompting](./effective-prompting.md) technique at all, or just a clearer request.

## Prerequisites

- [Prompt Engineering](./prompt-engineering.md)

## Contrasts with

- [Few-Shot Prompting](./few-shot-prompting.md)
- [Chain-of-Thought Prompting](./chain-of-thought.md)

## Related

- [Effective Prompting](./effective-prompting.md)
- [Role Prompting](./role-prompting.md)
- [Iterative Prompting](./iterative-prompting.md)
- [Self-Criticism Prompting](./self-criticism-prompting.md)
- [System Prompt Engineering](./system-prompt-engineering.md)
- [Agent Prompting Techniques](./agent-prompting.md)
- [Prompting Techniques for AI Coding](./ai-coding-prompting.md)
- [Structured Outputs](./structured-outputs.md)

## Tools

- [Prompt Engineering Guide](../entities/tools/prompting-guide.md)

## Sources

- ["Prompt Engineering" is a Bunch of BS - Here's the 5% of it to Learn](../sources/prompt-engineering-is-a-bunch-of-bs-heres-the-5-of-it-to-learn.md) - "[0:01:24] The first like six of these techniques here I'd recommend learning like zero shot prompting"
