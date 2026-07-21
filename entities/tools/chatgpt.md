---
type: entity
subtype: tool
title: "ChatGPT"
description: "The AI chat model used throughout as the example interface for prompting."
resource: "https://chat.openai.com"
tags: [llm, openai, chat-interface]
videos: [are-you-building-real-ai-agents-or-just-using-llms, chatgpt-teaches-the-secrets-to-financial-freedom, 3-most-important-prompt-engineering-techniques-you-need-to-know, chatgpt-users-be-aware-of-this-major-weakness, chatgpt-is-the-gift-that-keeps-on-giving-introducing-auto-gpt, how-to-use-gpt4-to-grow-on-twitter-the-right-way]
created: 2026-07-21
updated: 2026-07-21
---

# ChatGPT

ChatGPT is OpenAI's chat product, and in Cole's catalog it is the canonical example of a plain conversational LLM interface, the thing an agent is defined against. He is precise about that boundary: "chat gbt domcom because really it's just a conversational chat bot" [0:16:24], and "it's not like it's an agent that could decide it needs to search the web again to refine its search" [0:16:40]. ChatGPT answers; it does not autonomously loop, choose tools, or act. That distinction is the seed of his whole [what is an AI agent](../../concepts/what-is-an-ai-agent.md) framing.

## How Cole uses it

ChatGPT is the surface he teaches prompting on. His prompt-engineering lessons open on it because most people underuse it: "when they use chat GPT or other AI models they can often be disappointed with the results they get but really it's because they didn't ask the questions in the right way" [0:00:17]. He walks through turning it into a role-played assistant (a "personal financial coach") and notes the UI's implicit context handling: "even though in this UI the chat GPT model recognizes previous context from our conversation like it knows the Tweet I'm talking about" [0:07:10].

He is equally clear about its limits, warning that "these AI models like GPT are far from perfect" [0:00:00] and using ChatGPT to motivate hallucination and reliability discussions. Historically it is also his on-ramp story: the tool "given extremely robust artificial technology into the hands of everybody across the world to use for free" [0:00:00], which later videos push past toward true agents and [Auto-GPT](../../concepts/what-is-an-ai-agent.md)-style autonomy.

## Related

- [Prompt Engineering](../../concepts/prompt-engineering.md) - ChatGPT is his teaching surface for it
- [Effective Prompting](../../concepts/effective-prompting.md) - asking questions "the right way"
- [Role Prompting](../../concepts/role-prompting.md) - casting ChatGPT as a coach or persona
- [Fine-Tuning](../../concepts/fine-tuning.md) - going beyond prompting
- [Reasoning Models](../../concepts/reasoning-models.md) - the successor class to plain chat
- [Tool Use](../../concepts/tool-use.md) - the capability chat alone lacks
- [GPT-4](./gpt-4.md) - the model behind the ChatGPT he demos
- [Claude](./claude.md), [Google Gemini 2.0 Flash](./gemini.md), [Llama](./llama.md) - sibling models

## Sources

- [Are You Building REAL AI Agents or Just Using LLMs?](../../sources/are-you-building-real-ai-agents-or-just-using-llms.md) - "[0:16:40] it's not like it's an agent that could decide it needs to search the web again to refine its search"
- [3 MOST Important Prompt Engineering Techniques you NEED to know!](../../sources/3-most-important-prompt-engineering-techniques-you-need-to-know.md) - "[0:00:17] when they use chat GPT or other AI models they can often be disappointed with the results they get but really it's because they didn't ask the questions in the right way"
- [ChatGPT Teaches the Secrets to Financial Freedom!?](../../sources/chatgpt-teaches-the-secrets-to-financial-freedom.md) - "[0:00:42] you can make that author your personal financial coach using chat gbt"
- [ChatGPT Users BE AWARE of this Major Weakness](../../sources/chatgpt-users-be-aware-of-this-major-weakness.md) - "[0:00:00] these AI models like GPT are far from perfect"
- [ChatGPT is the GIFT that keeps on GIVING - Introducing Auto-GPT](../../sources/chatgpt-is-the-gift-that-keeps-on-giving-introducing-auto-gpt.md) - "[0:00:00] for the first time it's given extremely robust artificial technology into the hands of everybody across the world to use for free"
- [How to Use GPT4 To Grow on Twitter The Right Way](../../sources/how-to-use-gpt4-to-grow-on-twitter-the-right-way.md) - "[0:07:10] even though in this UI the chat GPT model recognizes previous context from our conversation like it knows the Tweet I'm talking about"
