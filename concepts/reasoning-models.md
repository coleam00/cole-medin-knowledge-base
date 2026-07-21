---
type: concept
title: "Reasoning Models"
description: "Models that produce explicit reasoning before answering, and when that extra thinking helps versus hurts."
tags: [reasoning, chain-of-thought, models]
videos: [google-anthropic-and-openais-guides-to-ai-agents-all-in-18-minutes, lets-settle-the-o3-mini-vs-r1-debate-for-coding-once-and-for-all, deepseek-r1-just-revolutionized-ai-forever, how-to-dominate-with-ai-in-2025, 3-most-important-prompt-engineering-techniques-you-need-to-know, chatgpt-is-the-gift-that-keeps-on-giving-introducing-auto-gpt]
created: 2026-07-21
updated: 2026-07-21
---

# Reasoning Models

Reasoning models think before they answer. "Reasoning models these are llms that are able to think to themselves before giving a final answer to the user and you get some insane results with this kind of setup" [0:00:00]. Put another way, "all a reasoning llm is kind of as the name suggests is a large language model that is able to reason with itself about your prompt before giving you the final answer" [0:11:18]. Mechanically, the model emits a hidden thinking pass first: "this kind of grade out text right here is it thinking to itself before it then gives us the final answer in more bolded text" [0:02:08]. The extra deliberation usually pays off, "this kind of reasoning approach always gives better answers maybe not always but almost always" [0:02:23], and it targets two core failure modes: reasoning models "solve two of the big problems with generative AI right now... the issues of hallucinations and llms just making bad decisions as agents" [0:12:03].

## How it works

The idea is the training-time internalization of [chain-of-thought](./chain-of-thought.md) prompting. The names are interchangeable: "you'll also hear Chain of Thought inference time compute all of this means the same thing" [0:11:32]. Because the reasoning is a distinct block wrapped in thinking tags, agent builders strip it before display: "if you're building an AI agent where you only want to display the final output... you would just take the output from the llm and then remove everything that is Within These thinking tags" [0:08:18].

Not all reasoning models behave alike. o3-mini and R1 "operate entirely differently under the hood" [0:02:41]: "o3 mini is considered to be better at more directed tasks that we see and a lot of AI agents but then R1 is considered better at more logical freethinking tasks like solving logic problems and deep research" [0:01:22]. Choosing between them is a [model selection](./model-selection.md) decision, not a formality.

## When it hurts

Reasoning is not free, and on already-capable models, manually forcing step-by-step thinking is redundant. "A lot of times people tell you that you need to tell the AI to think through their answer step by step now that can be powerful if you're working with a less powerful AI model but with something like gbt4 it already does that really well" [0:08:00]. Cole watched it happen live: "I asked this mathematical question and it literally started the response with let's think this through step by step so it already knows to do that" [0:08:14]. The takeaway is to reserve explicit reasoning prompts, and slower reasoning models, for the hard cases rather than paying the latency and token tax everywhere.

## Builds on

- [Chain-of-Thought Prompting](./chain-of-thought.md) - the prompting technique reasoning models bake into their weights.

## Related

- [Model Selection](./model-selection.md) - reasoning models are the "route the hard, logical work here" branch; keep fast conversational turns on lighter models.
- [Effective Prompting](./effective-prompting.md), [Prompt Engineering](./prompt-engineering.md) - why "think step by step" adds little on frontier models that already reason.
- [The Agent Loop (Reason-Act-Observe)](./agent-loop.md) - reasoning models strengthen the "reason" step of the loop.
- [Agentic Coding](./agentic-coding.md), [Agentic Workflow Engineering](./agentic-workflow-engineering.md) - where a reasoning model is often placed at the planning front of a workflow.

## Tools

- [DeepSeek R1](../entities/tools/deepseek-r1.md) - the open-weight reasoning model whose thinking tags and distilled variants Cole dissects.

## Sources

- [DeepSeek R1 Just Revolutionized AI Forever](../sources/deepseek-r1-just-revolutionized-ai-forever.md) - "[0:00:00] reasoning models these are llms that are able to think to themselves before giving a final answer to the user and you get some insane results with this kind of setup"
- [How to DOMINATE with AI in 2025](../sources/how-to-dominate-with-ai-in-2025.md) - "[0:11:18] all a reasoning llm is kind of as the name suggests is a large language model that is able to reason with itself about your prompt before giving you the final answer"
- [Let's Settle the o3-mini Vs. R1 Debate for Coding ONCE and for ALL](../sources/lets-settle-the-o3-mini-vs-r1-debate-for-coding-once-and-for-all.md) - "[0:01:22] a lot of times 03 mini is considered to be better at more directed tasks that we see and a lot of AI agents but then R1 is considered better at more logical freethinking tasks like solving logic problems and deep research"
- [3 MOST Important Prompt Engineering Techniques you NEED to know!](../sources/3-most-important-prompt-engineering-techniques-you-need-to-know.md) - "[0:08:00] a lot of times people tell you that you need to tell the AI to think through their answer step by step now that can be powerful if you're working with a less powerful AI model but with something like gbt4 it already does that really well"
- [Google, Anthropic, and OpenAI's Guides to AI Agents ALL in 18 Minutes](../sources/google-anthropic-and-openais-guides-to-ai-agents-all-in-18-minutes.md) - "[0:06:35] Then we have chain of thought. So, stepby-step logic. This is your classic telling an LLM to think through a problem step by step. And that generally does give us better results."
- [ChatGPT is the GIFT that keeps on GIVING - Introducing Auto-GPT](../sources/chatgpt-is-the-gift-that-keeps-on-giving-introducing-auto-gpt.md) - "[0:01:09] any kind of AI that is strong enough to be an AGI is something that can think on its own act on its own and actually come up with its own goals and reach those goals through steps that it defines itself"
