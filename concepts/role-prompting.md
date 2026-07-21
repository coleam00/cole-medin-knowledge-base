---
type: concept
title: "Role Prompting"
description: "Assigning the model a specific role or persona (e.g. 'an expert at growing Twitter accounts') to set the tone and expectations for its response, which Cole calls the overarching concept behind all prompt engineering."
tags: [prompt-engineering, role-prompting, personas, technique, steering]
videos: [3-most-important-prompt-engineering-techniques-you-need-to-know, how-to-use-gpt4-to-grow-on-twitter-the-right-way]
created: 2026-07-21
updated: 2026-07-21
---

# Role Prompting

Role prompting is telling the model who it is before you tell it what to do. You assign a persona, an expert, a critic, an assistant of a specific kind, and that framing sets the tone and expectations for everything that follows. Cole treats it as the master technique, not just one trick among many: "I am personifying the AI I'm telling it to fulfill some role to help me which is the biggest overall important concept wrapping around all of prompt engineering" [0:04:40]. The move is simple and reliable: "all I need to do to get a better tweet is to personify the AI that you are a Critic who specializes in critiquing tweets" [0:01:49].

## Why it works

Naming a role loads the model with the right context and register in one line. "this is the first key point with prompt engineering you want to always tell ChatGPT what it is" [0:04:27], because "you're setting the stage for what kind of reply you were expecting by telling it what kind of quote-unquote person it is" [0:04:43]. A "critic who specializes in critiquing tweets" produces sharper, more critical output than a blank assistant; a "financial expert" answers with different priorities than a generalist. The persona is a compact way to steer both tone and the depth of expertise the model draws on, which is why Cole frames it as the wrapper around the other techniques rather than a standalone tip.

## Part of

- [Prompt Engineering](./prompt-engineering.md): role prompting is the overarching concept Cole places at the center of the whole craft.

## Related

- [System Prompt Engineering](./system-prompt-engineering.md) formalizes the persona into an agent's standing system prompt.
- [Adversarial Agents](./adversarial-agents.md) apply role prompting to build a dedicated critic or reviewer.
- [Effective Prompting](./effective-prompting.md) covers the complementary clarity and format tactics.

## Sources

- [3 MOST Important Prompt Engineering Techniques you NEED to know!](../sources/3-most-important-prompt-engineering-techniques-you-need-to-know.md) - "[0:04:40] I am personifying the AI I'm telling it to fulfill some role to help me which is the biggest overall important concept wrapping around all of prompt engineering"
- [How to Use GPT4 To Grow on Twitter The Right Way](../sources/how-to-use-gpt4-to-grow-on-twitter-the-right-way.md) - "[0:04:43] you're setting the stage for what kind of reply you were expecting by telling it what kind of quote-unquote person it is"
