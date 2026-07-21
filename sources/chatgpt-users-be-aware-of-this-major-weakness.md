---
type: source
title: "ChatGPT Users BE AWARE of this Major Weakness"
description: "The single biggest weakness of GPT and similar AI models is the training cutoff, which freezes their knowledge at a point in time and causes them to silently produce outdated answers, but fine-tuning, search plugins, and faster training are closing that gap."
youtube_id: uB9cgB6Of9k
url: https://www.youtube.com/watch?v=uB9cgB6Of9k
slug: chatgpt-users-be-aware-of-this-major-weakness
published: 2023-05-22
duration: "0:09:32"
recency_rank: 194
raw: "../raw/chatgpt-users-be-aware-of-this-major-weakness.md"
tags: [training-cutoff, fine-tuning, ai-coding-limitations, chatgpt]
created: 2026-07-21
updated: 2026-07-21
---

# ChatGPT Users BE AWARE of this Major Weakness

Cole explains that despite the hype around GPT, its greatest weakness is the training cutoff: the model is trained on data up to a fixed date (September 2021 for the GPT of this era) and knows nothing after it. You can discover the cutoff by simply asking the model. This matters most for current events and for coding, where libraries and tools change constantly. He demonstrates with a Discord bot: ChatGPT writes working code but admits it is using discord.js version 12 (not the current version 14), and cannot help with the newest version because it was released after the cutoff. Worse, the model often does not warn you that its answer is outdated because it has no way of knowing whether a newer version exists.

He walks through why relying on outdated library code is dangerous: migrating from discord.js 13 to 14 involves many breaking changes, so it can be faster to write from the current docs than to fix the model's stale output. He then covers workarounds: fine-tuning your own model on question/answer pairs derived from up-to-date documentation, and using an internet-search plugin to fetch current information.

Finally, Cole argues the training cutoff will shrink over time. Training is expensive and slow because of the billions of parameters involved, but research (he cites Meta's model trained with roughly 10x fewer parameters) is making models cheaper and faster to train. As parameter counts drop, models could be retrained daily on fresh GitHub and news data, collapsing the cutoff from years to hours or days and eventually removing the need for search plugins or custom knowledge bases at all.

## Concepts covered

- [Fine-Tuning](../concepts/fine-tuning.md)
- [Limitations of AI Coding Models](../concepts/ai-coding-limitations.md)
- [Chat Interfaces](../concepts/chat-interfaces.md)

## Entities

- [ChatGPT](../entities/tools/chatgpt.md)
- [OpenAI](../entities/organizations/openai.md)
- [Meta AI](../entities/organizations/meta.md)
- [GitHub](../entities/tools/github.md)
- [Cole Medin](../entities/people/cole-medin.md)

## Key moments

- **[0:00:31]** Defines the training cutoff and shows you can ask GPT directly (answer: September 2021)
- **[0:01:31]** Discord bot example: ChatGPT writes working code but admits it uses discord.js v12, not the current v14
- **[0:03:41]** Breaking changes between discord.js 13 and 14 mean stale generated code can be slower to fix than starting fresh
- **[0:04:49]** Workaround 1: fine-tune your own model on Q/A pairs from up-to-date documentation
- **[0:05:37]** Future fix: fewer parameters (cites Meta at 10x less) means faster, cheaper, more frequent retraining
- **[0:07:08]** Search plugins as a workaround, but daily-retrained base models could make them unnecessary
- **[0:08:20]** The real danger: the model often does not tell you its answer is outdated because it can't know

## Transcript

[Raw transcript](../raw/chatgpt-users-be-aware-of-this-major-weakness.md)
