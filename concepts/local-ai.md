---
type: concept
title: "Local & Self-Hosted AI"
description: "Running open-weight models on your own hardware or cloud for privacy, cost control, and independence from API providers."
tags: [local-llms, self-hosting, privacy, open-weights]
videos: [the-next-evolution-of-ai-coding-is-harnesses-heres-how-to-build-them, the-way-we-use-ai-will-completely-change-in-2026-hot-takes, the-only-ai-tech-stack-you-need-in-2026, should-i-build-my-ai-agents-with-n8n-or-python, turn-any-file-into-llm-knowledge-in-seconds, the-ultimate-guide-to-local-ai-and-ai-agents-the-future-is-here, how-id-learn-ai-agents-fast-if-i-had-to-start-over-full-roadmap, i-built-the-ultimate-rag-mcp-server-for-ai-coding-better-than-context7, if-youre-serious-about-building-ai-agents-this-is-your-secret-weapon, build-a-chatgpt-style-app-for-your-n8n-ai-agents-in-minutes, create-your-own-private-local-ai-cloud-stack-in-under-20-minutes, the-ultimate-n8n-rag-ai-agent-template-local-ai-edition, run-supabase-100-locally-for-your-ai-agents, you-have-to-try-agentic-rag-with-deepseek-r1-insane-results, deepseek-r1-just-revolutionized-ai-forever, how-to-dominate-with-ai-in-2025, boltdiy-the-future-of-open-source-ai-coding-whats-next, breaking-news-ottodev-is-now-the-official-open-source-boltnew, weve-been-building-ai-agents-wrong-until-now, flowise-n8n-the-best-no-code-local-ai-agent-combo, ottodev-is-becoming-the-best-open-source-ai-coding-assistant, qwen-just-casually-started-the-local-ai-revolution, how-to-use-boltnew-for-free-with-local-llms-and-no-rate-limits, ollama-openais-swarm-easily-run-ai-agents-locally, this-boltnew-fork-is-exploding-dont-miss-out-on-whats-happening, use-open-webui-with-your-n8n-ai-agents-voice-chat-included, im-building-the-best-open-source-ai-coding-assistant-with-your-help, i-forked-boltnew-and-made-it-way-better, the-hard-truth-about-hosting-your-own-llms, run-all-your-ai-locally-in-minutes-llms-rag-and-more, local-vs-cloud-llmsrag-lets-finally-end-this-debate, youre-wasting-time-coding-your-ai-agents, new-llama-3-model-beats-gpt-and-claude-with-function-calling, function-calling-with-any-llm-for-local-ai-agents-feat-langchain-huggingface-and-llama-3]
created: 2026-07-21
updated: 2026-07-21
---

# Local & Self-Hosted AI

Local AI means owning the whole stack. "Very simply put local AI is running your own large language models and infrastructure like your database and your UI entirely on your own machine 100% offline" [0:02:00]. The definition stretches to rented boxes you control: "local AI is still considered local as long as it's running on a machine in the cloud that you control" [1:33:00] and "deploying your local AI stack to the cloud solves for all of this and it is still considered local as long as you manage the cloud instance" [0:00:52]. The through-line is control of the data and the weights, not the physical location.

## Why it matters

Three benefits recur. Privacy: "if we can solve the problem of hardware then we have 100% data privacy and zero millisecond latency for our agents. And that is the dream" [0:04:33], and self-hosting "guarantee[s] that everything stays in your own infrastructure" [0:03:16]. Cost: "if you're using a local model with oama you're going to pay for nothing have unlimited credits and have a lot of power right on your computer" [0:08:40], which matters most for "agents I want to have running constantly on my machine where it wouldn't be practical to pay for an API" [0:15:17]. And [provider independence](./provider-independence.md): "we're not stuck to just using apis from anthropic or open AI but we can actually run these models ourselves" [0:20:30].

## How it works

The serving layer is usually Ollama, which downloads open-weight models and exposes an OpenAI-compatible endpoint you point your code at: "we're going to create a custom asynchronous open AI instance where we override the base URL right here to point to Local Host Port 11434 where olama is currently running" [0:08:38]. Cole bundles the surrounding services into his **local AI package**: "all of these I have them incorporated into the local AI package, including Olama for serving local LLMs" [0:32:20], which "started out with just n8n olama quadrant and postgress" [0:02:30] and grew to add self-hosted [Supabase](../entities/tools/supabase.md), [Open Web UI](../entities/tools/open-web-ui.md), and [Langfuse](../entities/tools/langfuse.md).

Two hardware realities shape everything. Larger models need [quantization](./model-quantization.md) and offloading to fit: "all offloading is is splitting the layers for your large language model between your GPU and your CPU and RAM" [0:32:00]. And context is tight by default: "every single olama model defaults to 248 tokens for the window size so anything that is past that is going to be cut off" [0:12:42], a gotcha that repeatedly breaks local coding tools until the context length is manually raised.

## Contrasts with

- [Model Selection](./model-selection.md) - the honest tradeoff is capability. Closed models "are still better than the local ones... but going into 2025 this Gap is diminishing very very quickly" [0:14:07], and "if you have advanced tool calling or really specific structured output requirements things that the local models fail with then you're pretty much forced to go with managed Services" [0:07:05].

> **Contradiction:** Cole's evangelist framing says "the future of AI is ultimately going to be running everything locally your llms your reg pipeline your workflow automations and the list goes on" (Flowise + n8n, 2025-01-05) [0:00:31], but his own "Local vs. Cloud" video pushes back on that absolutism: "a lot of what I've seen on YouTube is people saying that you have to go local with your AI solution or it is completely bust... there is a lot of nuance to this" [0:00:16], landing on hybrid as "a really common approach for a lot of businesses" [0:03:34].

## Related

- [Model Quantization](./model-quantization.md) - the compression that makes big models fit local GPUs.
- [Fine-Tuning](./fine-tuning.md) - customizing the open-weight models you self-host.
- [Provider Independence](./provider-independence.md) - the strategic reason to avoid a single API vendor.
- [Agent Deployment](./agent-deployment.md) - shipping self-hosted agents to a cloud box you own.
- [Retrieval-Augmented Generation (RAG)](./rag.md), [Agentic RAG](./agentic-rag.md), [Knowledge Bases](./knowledge-bases.md), [Vector Embeddings](./vector-embeddings.md) - the local RAG stack (Ollama plus a self-hosted vector store).
- [Tool Calling](./tool-use.md) - the capability many smaller local models lack out of the box.
- [No-Code vs. Code](./no-code-vs-code.md), [Chat Interfaces](./chat-interfaces.md) - n8n and Open Web UI as no-code local building blocks.

## Tools

- [Ollama](../entities/tools/ollama.md) - the default local model server behind almost every setup here.
- [Open Web UI](../entities/tools/open-web-ui.md) - the offline ChatGPT-style front end for local models and n8n agents.
- [n8n](../entities/tools/n8n.md) - open-source, self-hostable workflow automation for local agents.
- [Supabase](../entities/tools/supabase.md) - self-hosted Postgres and vector store, folded into the local AI package.
- [Langfuse](../entities/tools/langfuse.md) - open-source, self-hostable agent observability.
- [Docling](../entities/tools/docling.md) - local document parsing that pulls its models from Hugging Face.
- [Llama](../entities/tools/llama.md), [Qwen](../entities/tools/qwen.md), [DeepSeek R1](../entities/tools/deepseek-r1.md) - the open-weight models people actually run locally.
- [bolt.diy](../entities/tools/bolt-diy.md), [Flowise](../entities/tools/flowise.md) - open-source coding and agent tools that can point at local LLMs.
- [Hugging Face](../entities/organizations/hugging-face.md) - the hub the open-weight models are downloaded from.

## Sources

- [The Ultimate Guide to Local AI and AI Agents (The Future is Here)](../sources/the-ultimate-guide-to-local-ai-and-ai-agents-the-future-is-here.md) - "[0:02:00] very simply put local AI is running your own large language models and infrastructure like your database and your UI entirely on your own machine 100% offline"
- [The HARD Truth About Hosting Your Own LLMs](../sources/the-hard-truth-about-hosting-your-own-llms.md) - "[0:01:28] we want to use local llms they give us the most flexibility privacy and ability to scale because we aren't paying per token but on the other hand running the more powerful llms locally can cost hundreds or thousands of dollars up front"
- [Local vs. Cloud LLMs/RAG - Let's FINALLY End this Debate](../sources/local-vs-cloud-llmsrag-lets-finally-end-this-debate.md) - "[0:00:16] a lot of what I've seen on YouTube is people saying that you have to go local with your AI solution or it is completely bust"
- [How to DOMINATE with AI in 2025](../sources/how-to-dominate-with-ai-in-2025.md) - "[0:14:39] you also have utmost data privacy because the llm is run on your own infrastructure you have better cost depending on the use case"
- [DeepSeek R1 Just Revolutionized AI Forever](../sources/deepseek-r1-just-revolutionized-ai-forever.md) - "[0:20:30] we're not stuck to just using apis from anthropic or open AI but we can actually run these models ourselves"
- [Qwen Just Casually Started the Local AI Revolution](../sources/qwen-just-casually-started-the-local-ai-revolution.md) - "[0:15:17] it's especially important for agents I want to have running constantly on my machine where it wouldn't be practical to pay for an API to use a model like CLA 3.5 Sonet because I be racking up a huge bill"
- [The ONLY AI Tech Stack You Need in 2026](../sources/the-only-ai-tech-stack-you-need-in-2026.md) - "[0:32:20] all of these I have them incorporated into the local AI package, including Olama for serving local LLMs"
- [Create Your Own Private Local AI Cloud Stack in Under 20 Minutes](../sources/create-your-own-private-local-ai-cloud-stack-in-under-20-minutes.md) - "[0:00:52] deploying your local AI stack to the cloud solves for all of this and it is still considered local as long as you manage the cloud instance"
- [We've Been Building AI Agents WRONG Until Now](../sources/weve-been-building-ai-agents-wrong-until-now.md) - "[0:08:38] we're going to create a custom asynchronous open AI instance where we override the base URL right here to point to Local Host Port 11434 where olama is currently running on my computer"
- [Flowise + n8n - The BEST No Code + Local AI Agent Combo](../sources/flowise-n8n-the-best-no-code-local-ai-agent-combo.md) - "[0:00:31] the future of AI is ultimately going to be running everything locally your llms your reg pipeline your workflow automations and the list goes on"
- [The Way We Use AI Will Completely Change in 2026 (Hot Takes)](../sources/the-way-we-use-ai-will-completely-change-in-2026-hot-takes.md) - "[0:04:33] if we can solve the problem of hardware then we have 100% data privacy and zero millisecond latency for our agents. And that is the dream."
- [If You're Serious About Building AI Agents, This is Your Secret Weapon](../sources/if-youre-serious-about-building-ai-agents-this-is-your-secret-weapon.md) - "[0:03:16] you can guarantee that everything stays in your own infrastructure when you host Langfuse yourself"
- [Run Supabase 100% LOCALLY for Your AI Agents](../sources/run-supabase-100-locally-for-your-ai-agents.md) - "[0:02:30] it started out with just n8n olama quadrant and postgress those were the four services in the local AI package"
- [I Forked Bolt.new and Made it WAY Better](../sources/i-forked-boltnew-and-made-it-way-better.md) - "[0:08:40] if you're using a local model with oama you're going to pay for nothing have unlimited credits and have a lot of power right on your computer"
- [Flowise + n8n - The BEST No Code + Local AI Agent Combo](../sources/flowise-n8n-the-best-no-code-local-ai-agent-combo.md) - "[0:12:42] every single olama model defaults to 248 tokens for the window size so anything that is past that is going to be cut off from the current context"
- [The Ultimate Guide to Local AI and AI Agents (The Future is Here)](../sources/the-ultimate-guide-to-local-ai-and-ai-agents-the-future-is-here.md) - "[0:32:00] All offloading is is splitting the layers for your large language model between your GPU and your CPU and RAM"
- [Turn ANY File into LLM Knowledge in SECONDS](../sources/turn-any-file-into-llm-knowledge-in-seconds.md) - "[0:08:47] Everything here with Dockling is local by the way, just grabbing models from Hugging Face. It is a beautiful thing."
- [Should I Build My AI Agents with n8n or Python?](../sources/should-i-build-my-ai-agents-with-n8n-or-python.md) - "[0:05:07] N8N is open- source and self-hostable, which also means we can build our AI agents to run completely locally if we're working with sensitive data"
- [The ULTIMATE n8n RAG AI Agent Template - Local AI Edition](../sources/the-ultimate-n8n-rag-ai-agent-template-local-ai-edition.md) - "[0:00:48] I truly believe that local AI where you control all of your data and your llms is the direction we need to head for generative AI as a whole"
- [Run ALL Your AI Locally in Minutes (LLMs, RAG, and more)](../sources/run-all-your-ai-locally-in-minutes-llms-rag-and-more.md) - "[0:00:47] running your own AI infrastructure is the way of the future especially because of how accessible is becoming and because open-source models like llama are getting to the point where they're so powerful"
- [Ollama + OpenAI's Swarm - EASILY Run AI Agents Locally](../sources/ollama-openais-swarm-easily-run-ai-agents-locally.md) - "[0:00:34] function calling in agents they take up a lot of tokens and so using swarm with GPT is definitely not cheap but with olama it is completely free"
- [You HAVE to Try Agentic RAG with DeepSeek R1 (Insane Results)](../sources/you-have-to-try-agentic-rag-with-deepseek-r1-insane-results.md) - "[0:00:34] we're going to be doing everything locally with the R1 distill models"
- [Build a ChatGPT Style App for Your n8n AI Agents in MINUTES](../sources/build-a-chatgpt-style-app-for-your-n8n-ai-agents-in-minutes.md) - "[0:04:14] the beauty of Open Web UI is you can run it entirely offline on your computer"
- [The Next Evolution of AI Coding Is Harnesses - Here's How to Build Them](../sources/the-next-evolution-of-ai-coding-is-harnesses-heres-how-to-build-them.md)
- [How I'd Learn AI Agents FAST if I Had to Start Over (Full Roadmap)](../sources/how-id-learn-ai-agents-fast-if-i-had-to-start-over-full-roadmap.md)
- [I Built the Ultimate RAG MCP Server for AI Coding (Better than Context7)](../sources/i-built-the-ultimate-rag-mcp-server-for-ai-coding-better-than-context7.md)
- [bolt.diy: The Future of Open Source AI Coding - What's Next?](../sources/boltdiy-the-future-of-open-source-ai-coding-whats-next.md)
- [BREAKING NEWS: oTToDev is Now the OFFICIAL Open Source Bolt.new](../sources/breaking-news-ottodev-is-now-the-official-open-source-boltnew.md)
- [oTToDev is Becoming the BEST Open Source AI Coding Assistant](../sources/ottodev-is-becoming-the-best-open-source-ai-coding-assistant.md)
- [How to Use Bolt.new for FREE with Local LLMs (And NO Rate Limits)](../sources/how-to-use-boltnew-for-free-with-local-llms-and-no-rate-limits.md)
- [This Bolt.new Fork is EXPLODING - Don't Miss out on What's Happening!](../sources/this-boltnew-fork-is-exploding-dont-miss-out-on-whats-happening.md)
- [Use Open WebUI with Your N8N AI Agents - Voice Chat Included!](../sources/use-open-webui-with-your-n8n-ai-agents-voice-chat-included.md)
- [I'm Building the BEST Open Source AI Coding Assistant with YOUR Help](../sources/im-building-the-best-open-source-ai-coding-assistant-with-your-help.md)
- [You're WASTING TIME Coding Your AI Agents](../sources/youre-wasting-time-coding-your-ai-agents.md)
- [New Llama 3 Model BEATS GPT and Claude with Function Calling!?](../sources/new-llama-3-model-beats-gpt-and-claude-with-function-calling.md)
- [Function Calling with ANY LLM for Local AI Agents (Feat. LangChain, HuggingFace, and Llama 3)](../sources/function-calling-with-any-llm-for-local-ai-agents-feat-langchain-huggingface-and-llama-3.md)
