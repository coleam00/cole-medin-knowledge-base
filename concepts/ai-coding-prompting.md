---
type: concept
title: "Prompting Techniques for AI Coding"
description: "Structuring build prompts: precise on functionality, general on UI, a catch-all requirements section, and image-to-code inputs."
tags: [ai-coding, prompting, multimodal, ui]
videos: [insane-new-strategy-for-building-ai-agent-apps, our-boltnew-forks-most-requested-feature-is-finally-here, how-to-use-boltnew-for-free-with-local-llms-and-no-rate-limits]
created: 2026-07-21
updated: 2026-07-21
---

# Prompting Techniques for AI Coding

Prompting an AI coding assistant is a different discipline from prompting a chat model: the payoff comes from knowing where to be precise and where to leave the model room. Cole's core rule is to spend nearly all your specificity on functionality and API behavior, and almost none on the interface. "most of this prompt is really just telling it how to work with the API I don't even specify much with the front end because that is where I really need to get specific" ([0:07:45]). The reason is that modern builders are already excellent at UI: "these tools like lovable they do a fantastic job making user interfaces even without much Direction it's more the specifics the functionality that you really have to get specific with" ([0:08:02]).

## How it works

A reliable build prompt has three parts. The functionality and API contract is described in detail, the UI is described loosely (unless you have strong opinions), and everything else lands in a catch-all requirements block: "finally I just have a random list of requirements here that I have for my application and this is usually what I'll do for all of my prompts to AI coding assistance like this when I'm starting a new project" ([0:11:07]). When you do care about the look, that catch-all is where design detail belongs: "this is where I start to get detailed with the UI and ux requirements and so I have things like colors defined specifically" ([0:12:02]), because "if you know those kind of design details you can really guide it well" ([0:12:17]).

The other lever is multimodal input: handing the model an image of a target UI instead of describing it. "I have this sample web page right here that I'm uploading as an image" ([0:11:10]), and even the generated markup shows comprehension, "even just looking at the text in the HTML here that it definitely is understanding the image and then trying to replicate it" ([0:12:19]). This only works on vision-capable models, which ties prompting directly to model choice: "this is only going to work for models that actually support images like Claude for example... if you go to a llama and you try to use like Qwen coder it's not going to understand images" ([0:11:24]).

## Builds on

- [Effective Prompting](./effective-prompting.md)
- [Prompt Engineering](./prompt-engineering.md)

## Related

- [Contract-First Development](./contract-first.md)
- [Iterative Prompting](./iterative-prompting.md)
- [Model Selection](./model-selection.md)

## Tools

- [Lovable](../entities/tools/lovable.md)
- [Bolt.new](../entities/tools/bolt-new.md)
- [Bolt.diy](../entities/tools/bolt-diy.md)
- [Claude](../entities/tools/claude.md)
- [Ollama](../entities/tools/ollama.md)
- [Qwen](../entities/tools/qwen.md)
- [Prompting Guide](../entities/tools/prompting-guide.md) - promptingguide.ai, the free resource Cole names as the single prompt-engineering guide worth studying end to end.

## Sources

- [INSANE New Strategy for Building AI Agent Apps](../sources/insane-new-strategy-for-building-ai-agent-apps.md) - "[0:07:45] most of this prompt is really just telling it how to work with the API I don't even specify much with the front end because that is where I really need to get specific"
- [How to Use Bolt.new for FREE with Local LLMs (And NO Rate Limits)](../sources/how-to-use-boltnew-for-free-with-local-llms-and-no-rate-limits.md) - "[0:12:02] this is where I start to get detailed with the UI and ux requirements and so I have things like colors defined specifically"
- [Our Bolt.new Fork's Most Requested Feature is FINALLY Here](../sources/our-boltnew-forks-most-requested-feature-is-finally-here.md) - "[0:11:24] this is only going to work for models that actually support images like Claude for example... if you go to a llama and you try to use like Qwen coder it's not going to understand images"
