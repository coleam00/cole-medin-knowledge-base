---
type: entity
subtype: tool
title: "Llama"
description: "The open LLM model powering the agent, served via Groq in the current build."
resource: "https://www.llama.com/"
tags: [llm, open-source, meta, local-ai]
videos: [stop-paying-for-gpt-claude-other-llms-get-them-all-in-one-place, the-hard-truth-about-hosting-your-own-llms, run-all-your-ai-locally-in-minutes-llms-rag-and-more, local-vs-cloud-llmsrag-lets-finally-end-this-debate, i-found-the-limits-of-the-most-popular-llms, ai-is-too-expensive-if-you-dont-do-this, the-most-value-packed-rag-guide-on-youtube-feat-llama-31-405b, ai-agents-the-future-of-ai-or-a-passing-fad, new-llama-3-model-beats-gpt-and-claude-with-function-calling, function-calling-with-any-llm-for-local-ai-agents-feat-langchain-huggingface-and-llama-3, i-will-win-the-nvidia-ai-agents-developer-contest]
created: 2026-07-21
updated: 2026-07-21
---

# Llama

Llama is Meta's open-weight LLM family, and in Cole's videos it is the reference open model, the counterweight to closed models like GPT and Claude. He frames it as the proof that open source is catching up: "open-source models like llama are getting to the point where they're so powerful that they're actually able to compete with close Source models like GPT and clad" [0:01:05]. It is one of the three raw LLMs he uses to define what an agent is made of, alongside Claude and GPT.

## How Cole uses it

Llama shows up in two roles across his catalog. First, as the local/self-hosted option: he benchmarks whether "I can get away with using a local model like llama 3.1 or do I need something really really powerful like CLA 3.5 Sonet" [0:06:34], and covers the hardware to run it ("if you want to run something like llama 3.1 70b ... you typically would only need something like an A40" [0:09:28]). He is honest about the gap, "everyone knows that llama 3 is not as powerful as the anthropic or open AI models" [0:23:13], while stressing how fast it is closing.

Second, as the cheap [model-selection](../../concepts/model-selection.md) tier in cost-routing setups: he uses "llama 370b not just to handle the simple request but also as the router itself because it's that cheap" [0:05:14], reserving GPT-4o for the hard cases. He also uses Llama for [tool use](../../concepts/tool-use.md) and function calling (creating a real Asana task in a demo) and, in his current agent build, serves it fast through Groq: "right now I'm just using grock uh with llama for the llm" [0:05:52].

## Related

- [Model Selection](../../concepts/model-selection.md) - Llama as the cheap router/simple-request tier
- [Local & Self-Hosted AI](../../concepts/local-ai.md) - running Llama on your own hardware
- [RAG](../../concepts/rag.md) - Llama 3.1 405B as the generation model in a RAG guide
- [Tool Use](../../concepts/tool-use.md) - Llama 3 function calling
- [What Is an AI Agent](../../concepts/what-is-an-ai-agent.md) - Llama as an example base LLM
- [Agent Evaluation](../../concepts/agent-evaluation.md)
- [Ollama](./ollama.md) - local serving; [Claude](./claude.md), [GPT-4](./gpt-4.md), [Qwen 2.5 Coder 32B](./qwen.md) - models he compares it to (also served fast via Groq)

## Sources

- [Run ALL Your AI Locally in Minutes (LLMs, RAG, and more)](../../sources/run-all-your-ai-locally-in-minutes-llms-rag-and-more.md) - "[0:01:05] open-source models like llama are getting to the point where they're so powerful that they're actually able to compete with close Source models like GPT and clad"
- [Local vs. Cloud LLMs/RAG - Let's FINALLY End this Debate](../../sources/local-vs-cloud-llmsrag-lets-finally-end-this-debate.md) - "[0:06:34] can I get away with using a local model like llama 3.1 or do I need something really really powerful like CLA 3.5 Sonet"
- [AI is TOO EXPENSIVE if You Don't Do This](../../sources/ai-is-too-expensive-if-you-dont-do-this.md) - "[0:05:14] we're using llama 370b not just to handle the simple request but also as the router itself because it's that cheap"
- [New Llama 3 Model BEATS GPT and Claude with Function Calling!?](../../sources/new-llama-3-model-beats-gpt-and-claude-with-function-calling.md) - "[0:01:15] their 8 billion parameter version of their llama 3 is only 1% worse for overall accuracy this much smaller model and is number three on the leaderboard"
- [Function Calling with ANY LLM for Local AI Agents (Feat. LangChain, HuggingFace, and Llama 3)](../../sources/function-calling-with-any-llm-for-local-ai-agents-feat-langchain-huggingface-and-llama-3.md) - "[0:14:13] task mow the lawn has been created in assana ... perfect llama has made a task for us"
- [The HARD Truth About Hosting Your Own LLMs](../../sources/the-hard-truth-about-hosting-your-own-llms.md) - "[0:09:28] if you want to run something like llama 3.1 70b ... you typically would only need something like an A40"
- [I Found the Limits of the Most Popular LLMs](../../sources/i-found-the-limits-of-the-most-popular-llms.md) - "[0:23:13] everyone knows that llama 3 is not as powerful as the anthropic or open AI models"
- [The Most Value Packed RAG Guide on YouTube (Feat. Llama 3.1 405B!)](../../sources/the-most-value-packed-rag-guide-on-youtube-feat-llama-31-405b.md) - "[0:00:16] chat with our local documents using the new llama 3.1 405 billion parameter model"
- [I Will Win the Nvidia AI Agents Developer Contest](../../sources/i-will-win-the-nvidia-ai-agents-developer-contest.md) - "[0:05:52] right now I'm just using grock uh with llama for the llm"
- [AI Agents: The Future of AI or a Passing Fad?](../../sources/ai-agents-the-future-of-ai-or-a-passing-fad.md) - "[0:08:32] you can spend less money by going and routing that to the cheaper model like llama 3 in this example"
- [STOP Paying for GPT, Claude, & Other LLMs - Get them ALL in One Place](../../sources/stop-paying-for-gpt-claude-other-llms-get-them-all-in-one-place.md) - "[0:02:21] you've got gbt 40 llama 3.1 405b Gemini 1.5 Pro even 01 is in this platform as well"
