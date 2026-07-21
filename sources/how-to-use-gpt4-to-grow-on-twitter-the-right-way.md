---
type: source
title: "How to Use GPT4 To Grow on Twitter The Right Way"
description: "Good prompt engineering, setting a role, giving context and format constraints, then having the model critique and rewrite its own output, turns generic, cringey ChatGPT tweet replies into human-sounding ones."
youtube_id: 0bSppwVxVr4
url: https://www.youtube.com/watch?v=0bSppwVxVr4
slug: how-to-use-gpt4-to-grow-on-twitter-the-right-way
published: 2023-04-05
duration: "0:11:21"
recency_rank: 198
raw: "../raw/how-to-use-gpt4-to-grow-on-twitter-the-right-way.md"
tags: [prompt-engineering, role-prompting, context-engineering, validation]
created: 2026-07-21
updated: 2026-07-21
---

# How to Use GPT4 To Grow on Twitter The Right Way

In this early (April 2023) video, Cole introduces prompt engineering through a concrete use case: generating good Twitter reply drafts for his "Tweet Genie" feature inside Cardinal/Kernel branding software. His central rule is that "the quality of your output is determined by the quality of your input": a bare ask like "give me YouTube video ideas" yields bland, jumbled results, while a prompt that adds context, descriptive adjectives (original, engaging), and an explicit output format ("a list of 10 ideas") gets usable output.

He walks through his GPT-4 prompt for tweet replies, which starts by telling the model who it is ("you are an expert at growing Twitter accounts through engaging and insightful tweets and replies"), then asks for an informal, engaging reply without hashtags and under 280 characters. The first reply is decent but too formal, so he applies the "critic model" pattern: a second prompt that reassigns the model as an open, opinionated Critic and expert, feeds it the original tweet and the prior reply, asks it to critique and suggest improvements, then rewrite, forcing step-by-step self-reflection that produces a more human result.

A key aside: because he'll ship this through the OpenAI API rather than the ChatGPT UI, every request must carry all its own context. The UI remembers prior conversation, but an API call is stateless, the model only knows what you send it (unless you use a fine-tuned model, which he defers to a later video). This is why he re-pastes the tweet and reply into the critic prompt instead of relying on remembered context.

## Concepts covered

- [Prompt Engineering](../concepts/prompt-engineering.md)
- [Validation](../concepts/validation.md)
- [Role Prompting](../concepts/role-prompting.md)
- [Context Engineering](../concepts/context-engineering.md)

## Entities

- [Cole Medin](../entities/people/cole-medin.md)
- [GPT-4](../entities/tools/gpt-4.md)
- [ChatGPT](../entities/tools/chatgpt.md)
- [OpenAI](../entities/organizations/openai.md)

## Key moments

- **[0:00:01]** Defines prompt engineering as crafting prompts so the AI understands what you want
- **[0:00:28]** Core rule: quality of output is determined by quality of input
- **[0:00:58]** Improve prompts with context, descriptive adjectives, and explicit output format
- **[0:02:05]** Motivating use case: Tweet Genie, avoiding bland/cringey third-person, hashtag-heavy replies
- **[0:04:08]** Walks through the role-setting reply prompt (expert Twitter grower, informal, no hashtags, <280 chars)
- **[0:05:43]** Introduces the critic model, having the AI criticize its own reply
- **[0:07:10]** API statelessness: an API request only knows what you give it, unlike the UI
- **[0:09:40]** Second (critiqued) reply sounds more human than the first

## Transcript

[Raw transcript](../raw/how-to-use-gpt4-to-grow-on-twitter-the-right-way.md)
