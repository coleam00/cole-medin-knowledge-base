---
type: entity
subtype: tool
title: "GPT-4"
description: "OpenAI's model cited as strong enough that it reasons step by step without being told to."
resource: "https://openai.com/gpt-4"
tags: [llm, openai, model-access]
videos: [3-most-important-prompt-engineering-techniques-you-need-to-know, how-to-use-gpt4-to-grow-on-twitter-the-right-way]
created: 2026-07-21
updated: 2026-07-21
---

# GPT-4

GPT-4 is OpenAI's flagship model from the era when Cole was teaching prompting, and he holds it up as the example of a model strong enough to reason on its own. Demonstrating [chain-of-thought](../../concepts/effective-prompting.md), he points out it needs no prompting to think step by step: "with something like gbt4 it already does that really well in fact ... it literally started the response with let's think this through step by step" [0:08:14]. That self-directed reasoning is what separates GPT-4 from weaker models that must be explicitly told to slow down.

## How Cole uses it

GPT-4 is the premium model in his early tutorials, the one worth paying for when quality matters. Introducing it he notes both its strength and its cost/access at the time: "I'm going to be using the gpt4 model which is the open ai's strongest and most recent model that isn't quite available to all the public yet I have to pay just twenty dollars a month" [0:02:59]. He uses it as the engine behind practical [prompt-engineering](../../concepts/prompt-engineering.md) demos, including a Twitter-growth workflow, showing how [role prompting](../../concepts/role-prompting.md) and well-structured requests get the most out of it.

Because GPT-4 already reasons step by step, Cole uses it to make a teaching point about [effective prompting](../../concepts/effective-prompting.md): techniques like "let's think this through step by step" help weaker models more than they help GPT-4, which has that behavior baked in. In later videos it remains the closed-model quality bar (later joined by GPT-4o) that open models like Llama are measured against.

## Related

- [Prompt Engineering](../../concepts/prompt-engineering.md) - GPT-4 as the demo engine
- [Effective Prompting](../../concepts/effective-prompting.md) - it reasons step by step unprompted
- [Role Prompting](../../concepts/role-prompting.md) - casting GPT-4 into personas
- [Few-Shot Prompting](../../concepts/few-shot-prompting.md)
- [Adversarial Agents](../../concepts/adversarial-agents.md), [Structured Outputs](../../concepts/structured-outputs.md)
- [ChatGPT](./chatgpt.md) - the interface GPT-4 powers; [GPT-4o](./gpt-4o.md), [GPT-4o Mini](./gpt-4o-mini.md) - successor OpenAI models; [Claude](./claude.md), [Llama](./llama.md) - models he benchmarks it against

## Sources

- [3 MOST Important Prompt Engineering Techniques you NEED to know!](../../sources/3-most-important-prompt-engineering-techniques-you-need-to-know.md) - "[0:08:14] with something like gbt4 it already does that really well in fact... it literally started the response with let's think this through step by step"
- [How to Use GPT4 To Grow on Twitter The Right Way](../../sources/how-to-use-gpt4-to-grow-on-twitter-the-right-way.md) - "[0:02:59] I'm going to be using the gpt4 model which is the open ai's strongest and most recent model ... I have to pay just twenty dollars a month"
