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

Llama is Meta's open-weight LLM family, and in Cole's videos it is the reference open model, the counterweight to closed models like GPT and Claude. He frames it as the proof that open source is catching up: "open-source models like llama are getting to the point where they're so powerful that they're actually able to compete with close Source models like GPT and Claude" [0:01:05]. It is one of the three raw LLMs he uses to define what an agent is made of, alongside Claude and GPT.

## How Cole uses it

Llama shows up in two roles across his catalog. First, as the local/self-hosted option: he benchmarks whether "I can get away with using a local model like llama 3.1 or do I need something really really powerful like Claude 3.5 Sonnet" [0:06:34], and covers the hardware to run it ("if you want to run something like llama 3.1 70b ... you typically would only need something like an A40" [0:09:28]). He is honest about the gap, "everyone knows that llama 3 is not as powerful as the anthropic or open AI models" [0:23:13], while stressing how fast it is closing.

Second, as the cheap [model-selection](../../concepts/model-selection.md) tier in cost-routing setups: he uses "llama 370b not just to handle the simple request but also as the router itself because it's that cheap" [0:05:14], reserving GPT-4o for the hard cases. He also uses Llama for [tool use](../../concepts/tool-use.md) and function calling (creating a real Asana task in a demo) and, in his current agent build, serves it fast through Groq: "right now I'm just using Groq uh with llama for the llm" [0:05:52].

## Realizes

- [What Is an AI Agent](../../concepts/what-is-an-ai-agent.md) - an AI agent is a large language model given tools to interact with the outside world and take actions, making it far more capable than the LLM alone.
- [Local & Self-Hosted AI](../../concepts/local-ai.md) - running open-weight models on your own hardware or cloud for privacy, cost control, and independence from API providers.
- [Model Selection](../../concepts/model-selection.md) - choosing the right LLM per task by trading off quality, speed, and cost, often routing easy requests to cheap models and hard ones to expensive models.
- [Tool Use](../../concepts/tool-use.md) - letting an LLM invoke external functions and APIs so it can take actions and fetch data beyond its parametric knowledge.

## Contrasts with

- [Claude](./claude.md) - named as an example of a large language model that can be turned into an agent.
- [GPT-4](./gpt-4.md) - OpenAI's model cited as strong enough that it reasons step by step without being told to.
- [Qwen 2.5 Coder 32B](./qwen.md) - Alibaba's open-source LLM family Cole cites as among his favorites that stood the test of time.
- [Code Llama](./code-llama.md) - Meta's open-source code-specialized LLM family whose larger 34B variant fails builds that the smaller Qwen 2.5 Coder 32B handles, showing capability beats parameter count.

## Works with

- [Ollama](./ollama.md) - local LLM runtime; works with a locally-run bolt.diy but can't be reached by a self-hosted (remote) instance.
- [Together AI](../organizations/together-ai.md) - Pay-per-token inference provider serving open models like Llama 3.1; cheaper on its lite 70B variant but pricier than Groq once you want turbo-speed inference.

## Related

- [RAG](../../concepts/rag.md) - grounding an LLM's answers by retrieving relevant documents from an external knowledge base and injecting them into the prompt at query time.
- [Agent Evaluation](../../concepts/agent-evaluation.md) - systematically scoring agent behavior with evals and benchmarks, including as a gate before deployment.
- [Berkeley Function Calling Leaderboard](./berkeley-function-calling-leaderboard.md) - A public benchmark that ranks LLMs on function-calling accuracy using tasks meant to represent real agent and enterprise workflows.

## Sources

- [Run ALL Your AI Locally in Minutes (LLMs, RAG, and more)](../../sources/run-all-your-ai-locally-in-minutes-llms-rag-and-more.md) - "[0:01:05] open-source models like llama are getting to the point where they're so powerful that they're actually able to compete with close Source models like GPT and Claude"
- [Local vs. Cloud LLMs/RAG - Let's FINALLY End this Debate](../../sources/local-vs-cloud-llmsrag-lets-finally-end-this-debate.md) - "[0:06:34] can I get away with using a local model like llama 3.1 or do I need something really really powerful like Claude 3.5 Sonnet"
- [AI is TOO EXPENSIVE if You Don't Do This](../../sources/ai-is-too-expensive-if-you-dont-do-this.md) - "[0:05:14] we're using llama 370b not just to handle the simple request but also as the router itself because it's that cheap"
- [New Llama 3 Model BEATS GPT and Claude with Function Calling!?](../../sources/new-llama-3-model-beats-gpt-and-claude-with-function-calling.md) - "[0:01:15] their 8 billion parameter version of their llama 3 is only 1% worse for overall accuracy this much smaller model and is number three on the leaderboard"
- [Function Calling with ANY LLM for Local AI Agents (Feat. LangChain, HuggingFace, and Llama 3)](../../sources/function-calling-with-any-llm-for-local-ai-agents-feat-langchain-huggingface-and-llama-3.md) - "[0:14:13] task mow the lawn has been created in Asana ... perfect llama has made a task for us"
- [The HARD Truth About Hosting Your Own LLMs](../../sources/the-hard-truth-about-hosting-your-own-llms.md) - "[0:09:28] if you want to run something like llama 3.1 70b ... you typically would only need something like an A40"
- [I Found the Limits of the Most Popular LLMs](../../sources/i-found-the-limits-of-the-most-popular-llms.md) - "[0:23:13] everyone knows that llama 3 is not as powerful as the anthropic or open AI models"
- [The Most Value Packed RAG Guide on YouTube (Feat. Llama 3.1 405B!)](../../sources/the-most-value-packed-rag-guide-on-youtube-feat-llama-31-405b.md) - "[0:00:16] chat with our local documents using the new llama 3.1 405 billion parameter model"
- [I Will Win the Nvidia AI Agents Developer Contest](../../sources/i-will-win-the-nvidia-ai-agents-developer-contest.md) - "[0:05:52] right now I'm just using Groq uh with llama for the llm"
- [AI Agents: The Future of AI or a Passing Fad?](../../sources/ai-agents-the-future-of-ai-or-a-passing-fad.md) - "[0:08:32] you can spend less money by going and routing that to the cheaper model like llama 3 in this example"
- [STOP Paying for GPT, Claude, & Other LLMs - Get them ALL in One Place](../../sources/stop-paying-for-gpt-claude-other-llms-get-them-all-in-one-place.md) - "[0:02:21] you've got GPT-4o llama 3.1 405b Gemini 1.5 Pro even 01 is in this platform as well"
