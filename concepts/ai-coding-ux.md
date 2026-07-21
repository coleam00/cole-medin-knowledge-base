---
type: concept
title: "AI Coding Assistant UX Patterns"
description: "Interaction patterns of coding assistants: streamed code output, inline vs manual suggestions, and schema inference from a name."
tags: [ai-coding, ux, autocomplete]
videos: [ottodev-is-becoming-the-best-open-source-ai-coding-assistant, you-need-these-5-tools-for-coding-better-than-chatgpt]
created: 2026-07-21
updated: 2026-07-21
---

# AI Coding Assistant UX Patterns

How a coding assistant presents its work is a design choice with real ergonomic weight. One pattern is code streaming, where you watch the model write in real time instead of getting a silent dump. As Cole describes it, "code streaming is a really big thing so you can actually see the large language model type out the code in each file as it is generating it." The contrast is stark against the older behavior, "before it used to just create the package.json behind the scenes and then dump it all in... but now we can see it type things out." Seeing the code appear builds trust and lets you catch a wrong direction early.

A second axis is inline versus manual suggestions. Some assistants push completions at you as you type, "a lot of these AI coding assistants will give you suggestions automatically as you're typing It'll like fill in lines of code for you," while others wait to be asked, "others you have to manually request it and different people are going to prefer different things." Neither is strictly better; the preference is personal. Some developers want the assistant to stay out of the way, "sometimes you don't want the AI to just be spitting out suggestions all the time you want to be able to just call on it to interact with it and then otherwise just do your regular code."

A subtler UX pattern is intent inference, where the assistant fills in structure from almost nothing. In one example the model designs a data schema purely from its name: "the user in this case isn't even saying what they want the schema to be that's all being determined based off of the name of the schema which is blog schema so it decided that it wants a title a slug and an excerpt." This is the assistant reading intent from context rather than an explicit spec, powerful when it guesses right, and a reminder that naming carries signal.

## Related

- [AI Coding Assistant](./ai-coding-assistant.md) - the tool whose interaction surface these patterns describe.

## Tools

- [oTToDev](../entities/tools/ottodev.md) - the open-source assistant demonstrating real-time code streaming.
- [GitHub](../entities/tools/github.md) Copilot - contrasted for inline autocomplete versus manual, on-demand suggestions.

## Sources

- [oTToDev is Becoming the BEST Open Source AI Coding Assistant](../sources/ottodev-is-becoming-the-best-open-source-ai-coding-assistant.md) - "[0:01:41] code streaming is a really big thing so you can actually see the large language model type out the code in each file as it is generating it"
- [You NEED These 5 Tools For Coding!! (Better Than ChatGPT)](../sources/you-need-these-5-tools-for-coding-better-than-chatgpt.md) - "[0:00:57] a lot of these AI coding assistants will give you suggestions automatically as you're typing It'll like fill in lines of code for you others you have to manually request it and different people are going to prefer different things"
