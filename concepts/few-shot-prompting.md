---
type: concept
title: "Few-Shot Prompting"
description: "Including a handful of concrete input/output examples in the prompt so the model infers the desired pattern instead of relying on instructions alone."
tags: [prompting, few-shot, examples, in-context-learning, prompt-engineering, output-format, llm, technique]
videos: [my-top-20-lessons-from-building-100s-of-ai-agents-super-actionable, prompt-engineering-is-a-bunch-of-bs-heres-the-5-of-it-to-learn, 3-most-important-prompt-engineering-techniques-you-need-to-know]
created: 2026-07-21
updated: 2026-07-21
---

# Few-Shot Prompting

Few-shot prompting means putting a handful of concrete input/output examples directly in the prompt so the model infers the pattern you want, rather than trying to describe that pattern in prose. The mechanism is straightforward: "you can force it to respond in exactly the way that you want and the way that you do that is by providing examples question and answer and then you ask it the question" ([0:06:26]). It sits at the top of Cole's shortlist of techniques worth knowing, alongside chain-of-thought and self-consistency ([0:01:24]).

## When and why it works

Examples are the tool of choice for two problems that instructions handle poorly: exact output format and voice. "the idea here is to give examples when you need a specific format and giving examples can also be very powerful when it doesn't quite answer the question in the kind of voice or tone that you're looking for" ([0:07:10]). Matching a particular person's style is nearly impossible to specify abstractly, so you show it instead: "you need to give it examples for it to actually understand this is how this person talks" ([0:07:28]). A demonstrated pattern carries information that a description cannot, which is why examples often succeed where a longer instruction fails.

Cole treats this as one of the most reliable levers in all of agent building. His blunt summary is "examples examples and examples... it is just so helpful" ([0:21:33]), and he points to the strongest possible evidence: the leading AI coding assistants lean on it heavily. "the most popular AI coding assistants like Vzero and Cursor and Bolt.new like they all have very concrete examples in their system prompts" ([0:22:11]). Few-shot prompting also pairs with [avoiding negative instructions](./avoid-negative-instructions.md): rather than telling the model what not to do, an example of the correct output demonstrates the target directly, and it reinforces [reduce assumptions](./reduce-assumptions.md) by pinning down the exact shape you expect.

## Builds on

- [Prompt Engineering](./prompt-engineering.md)

## Related

- [Effective Prompting](./effective-prompting.md)
- [Reduce Assumptions](./reduce-assumptions.md)
- [Avoid Negative Instructions](./avoid-negative-instructions.md)
- [Structured Outputs](./structured-outputs.md)
- [Tool Design](./tool-design.md)
- [Chain-of-Thought Prompting](./chain-of-thought.md)

## Tools

- [Cursor](../entities/tools/cursor.md)
- [Bolt.new](../entities/tools/bolt-new.md)

## Sources

- [3 MOST Important Prompt Engineering Techniques you NEED to know!](../sources/3-most-important-prompt-engineering-techniques-you-need-to-know.md) - "[0:06:26] you can force it to respond in exactly the way that you want and the way that you do that is by providing examples question and answer and then you ask it the question"
- [My Top 20 Lessons from Building 100s of AI Agents (Super Actionable)](../sources/my-top-20-lessons-from-building-100s-of-ai-agents-super-actionable.md) - "[0:22:11] the most popular AI coding assistants like Vzero and Cursor and Bolt.new like they all have very concrete examples in their system prompts."
- ["Prompt Engineering" is a Bunch of BS - Here's the 5% of it to Learn](../sources/prompt-engineering-is-a-bunch-of-bs-heres-the-5-of-it-to-learn.md) - "[0:01:24] you got few shop prompting Chain of Thought prompting um self-consistency general knowledge prompting and prompt chaining these are all really good"
