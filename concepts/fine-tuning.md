---
type: concept
title: "Fine-Tuning"
description: "Adapting a base model to a task or domain via additional training, weighed against just prompting a stronger general model."
tags: [fine-tuning, training, distillation]
videos: [the-ultimate-guide-to-local-ai-and-ai-agents-the-future-is-here, deepseek-r1-just-revolutionized-ai-forever, how-to-dominate-with-ai-in-2025, the-only-ai-developer-roadmap-you-need-in-2024, chatgpt-teaches-the-secrets-to-financial-freedom, chatgpt-users-be-aware-of-this-major-weakness]
created: 2026-07-21
updated: 2026-07-21
---

# Fine-Tuning

Fine-tuning is taking an existing model and training it further on your own data so it specializes. As Cole puts it, "you can take any open-source large language model and add additional training on top with your own data. Basically making it a domain expert on your business" [0:09:00]. It is the classic way to bend a general model toward a narrow task or domain: "using a little bit of your own data to take a general AI like GPT and make it work even better on your use case" [0:14:00]. Done well, the ceiling is high. Cole claims "you can make models through fine-tuning more powerful than the best of the best in the cloud depending on what you are able to fine-tune with" [0:09:30].

## How it works

At the data level, fine-tuning is supervised training on curated examples, often question/answer pairs: "you can actually give your own key value pairs like here's a question here's an answer and you could take like the entire documentation for discord.js version 14 and have questions and answers based on that documentation to actually train GPT your own custom model" [0:05:03]. The result is a new set of weights, not a new prompt.

A powerful special case is **distillation**, where a smaller model is fine-tuned on outputs from a larger one. DeepSeek did exactly this with R1: "they took their competitors Qwen and Llama and they made smaller versions of R1 based on those models" [0:03:42], "basically fine-tuned added in all the R1 reasoning to these models like Qwen and Llama so you can download these yourself" [0:03:57]. The payoff is dramatic compression of capability: "even their 14 billion parameter model right here their Qwen version is on par with 01 mini which is incredible" [0:04:12].

## Contrasts with

- [Knowledge Bases](./knowledge-bases.md) and [When RAG Is (and Isn't) Dead](./when-rag-is-dead.md) - retrieval injects fresh facts at query time without retraining. Fine-tuning bakes behavior and style into the weights but does not fix the training cutoff: a model "is stuck at a point in time where it's trained it has all the past knowledge but nothing in the future and so this is the biggest weakness" [0:01:03].
- [Training Cutoff](./training-cutoff.md) - an AI model's knowledge is frozen at the date its training data ends, so it silently knows nothing about events, libraries, or versions released afterward.
- [Model Selection](./model-selection.md) - often the cheaper move is to just prompt a stronger general model that already knows your domain. On finance books: "GPT is trained on so much information it already knows about Rich Dad poordin and a lot of other really popular Finance books and so that's all you have to say for it to have all the context it needs" [0:02:29].

## Related

- [Local & Self-Hosted AI](./local-ai.md) - fine-tuning is most compelling on open-weight models you can download and own.
- [Reasoning Models](./reasoning-models.md) - R1's reasoning was distilled into smaller open models via fine-tuning.
- [Model Quantization](./model-quantization.md) - a complementary compression lever; quantize the fine-tuned model to fit local hardware.
- [The LLM Wiki](./the-llm-wiki.md) - an alternative to fine-tuning for teaching a model your material: curate knowledge as readable pages instead of retraining.
- [Andrew Ng](../entities/people/andrew-ng.md) - AI educator behind the Coursera 'AI for Everyone' course and the machine learning, deep learning, and NLP specializations Cole recommends for AI fundamentals.

## Tools

- [DeepSeek R1](../entities/tools/deepseek-r1.md) - its distilled variants are fine-tuned [Qwen](../entities/tools/qwen.md) and [Llama](../entities/tools/llama.md) models.
- [ChatGPT](../entities/tools/chatgpt.md) / [GPT-4](../entities/tools/gpt-4.md) - the general models Cole contrasts against custom fine-tunes.
- [Hugging Face](../entities/organizations/hugging-face.md) - where fine-tuned and distilled open-weight models are published.
- [Builder.io](../entities/tools/builder-io.md) - Figma-to-code product Cole cites as the canonical case where training a custom model beat general GPT, then used GPT to refine the generated code.

## Sources

- [The Ultimate Guide to Local AI and AI Agents (The Future is Here)](../sources/the-ultimate-guide-to-local-ai-and-ai-agents-the-future-is-here.md) - "[0:09:00] you can take any open-source large language model and add additional training on top with your own data. Basically making it a domain expert on your business"
- [DeepSeek R1 Just Revolutionized AI Forever](../sources/deepseek-r1-just-revolutionized-ai-forever.md) - "[0:03:57] basically fine-tuned added in all the R1 reasoning to these models like Qwen and Llama so you can download these yourself"
- [How to DOMINATE with AI in 2025](../sources/how-to-dominate-with-ai-in-2025.md) - "[0:14:24] fine-tuning that I already mentioned being able to take a large language model and train it on your own data so it can perform better on your use case"
- [The ONLY AI Developer Roadmap You Need in 2024](../sources/the-only-ai-developer-roadmap-you-need-in-2024.md) - "[0:14:00] fine-tuning large language models which is basically using a little bit of your own data to take a general AI like GPT and make it work even better on your use case"
- [ChatGPT Users BE AWARE of this Major Weakness](../sources/chatgpt-users-be-aware-of-this-major-weakness.md) - "[0:05:03] you can actually give your own key value pairs like here's a question here's an answer and you could take like the entire documentation for discord.js version 14 and have questions and answers based on that documentation to actually train GPT your own custom model"
- [ChatGPT Teaches the Secrets to Financial Freedom!?](../sources/chatgpt-teaches-the-secrets-to-financial-freedom.md) - "[0:02:29] GPT is trained on so much information it already knows about Rich Dad poordin and a lot of other really popular Finance books and so that's all you have to say for it to have all the context it needs"
