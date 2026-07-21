---
type: entity
subtype: tool
title: "Ollama"
description: "Local LLM runtime; works with a locally-run bolt.diy but can't be reached by a self-hosted (remote) instance."
resource: "https://ollama.com"
tags: [llm, local-ai]
videos: [the-official-archon-guide-10x-your-ai-coding-workflow, introducing-archon-the-revolutionary-operating-system-for-ai-coding, the-ultimate-guide-to-local-ai-and-ai-agents-the-future-is-here, make-rag-100x-better-with-real-time-knowledge-graphs, i-built-the-ultimate-rag-mcp-server-for-ai-coding-better-than-context7, build-a-chatgpt-style-app-for-your-n8n-ai-agents-in-minutes, openais-brand-new-agents-sdk-crash-course, create-your-own-private-local-ai-cloud-stack-in-under-20-minutes, the-ultimate-n8n-rag-ai-agent-template-local-ai-edition, run-supabase-100-locally-for-your-ai-agents, this-is-hands-down-the-best-way-to-build-ai-agents, you-have-to-try-agentic-rag-with-deepseek-r1-insane-results, deepseek-r1-just-revolutionized-ai-forever, how-to-dominate-with-ai-in-2025, boltdiy-the-future-of-open-source-ai-coding-whats-next, weve-been-building-ai-agents-wrong-until-now, flowise-n8n-the-best-no-code-local-ai-agent-combo, our-boltnew-forks-most-requested-feature-is-finally-here, ottodev-is-becoming-the-best-open-source-ai-coding-assistant, turn-any-ai-agent-into-a-live-person-voice-chat-setup-in-minutes, qwen-just-casually-started-the-local-ai-revolution, how-to-use-boltnew-for-free-with-local-llms-and-no-rate-limits, were-taking-this-ai-coding-assistant-to-the-moon-plus-installation-instructions, ollama-openais-swarm-easily-run-ai-agents-locally, this-boltnew-fork-is-exploding-dont-miss-out-on-whats-happening, use-open-webui-with-your-n8n-ai-agents-voice-chat-included, im-building-the-best-open-source-ai-coding-assistant-with-your-help, i-forked-boltnew-and-made-it-way-better, deploy-any-ai-app-to-the-cloud-fast, run-all-your-ai-locally-in-minutes-llms-rag-and-more, local-vs-cloud-llmsrag-lets-finally-end-this-debate, function-calling-with-any-llm-for-local-ai-agents-feat-langchain-huggingface-and-llama-3]
created: 2026-07-21
updated: 2026-07-21
---

# Ollama

Ollama is the runtime that lets you download and run large language models on your own machine, and it is the single most-referenced tool in Cole's local-AI catalog. He introduces it plainly: "This is one of the open-source platforms that allows us to very easily download and run local large language models." Install it, run `ollama pull` to grab a model like Llama 3.1 or Qwen 2.5 Coder, and you have a private model server listening on `localhost:11434`, no API key required.

That local endpoint is the key to how Ollama plugs into everything else. Because it exposes an OpenAI-compatible API, Cole wires agents to it the same way he wires any provider: "we're going to take advantage of the fact that Ollama is OpenAI API compatible so we set up an OpenAI server model but we're changing the base URL to just point to Ollama." The same trick connects it to Pydantic AI, the OpenAI Agents SDK, OpenAI's Swarm, n8n, Flowise, and his Bolt.new forks, which support "literally any local model that you can run with Ollama." For Archon it is the privacy story: "you can run everything completely locally with Ollama with your own private knowledge base and MCP server if you want to do so."

Cole is candid about the trade-offs. Local models run "on your computer," so a CPU-only box is slow and a self-hosted (remote) instance can't reach an Ollama living on your laptop. The default context window is small ("the default context length for any Ollama model is 248 tokens"), forcing custom model files with larger context to fit big prompts. Streaming has been flaky inside Pydantic AI, tool support and OpenAI compatibility only arrived over time, and smaller local models like Qwen Coder can't process images. These are the concrete frictions behind his broader [Local vs. Cloud](../../concepts/local-ai.md) verdict: Ollama buys you privacy and zero marginal cost, at the price of capability and speed. When that price is too high, Cole reaches for [OpenRouter](./openrouter.md) instead and keeps the rest of the stack local.

Ollama is the model engine at the heart of Cole's [Local AI Package](./local-ai-package.md), pairing with [Open Web UI](./open-web-ui.md) for a chat frontend and embedding models like `nomic-embed-text` for fully-local [RAG](../../concepts/rag.md) and [agentic RAG](../../concepts/agentic-rag.md).

## Realizes

- [Local & Self-Hosted AI](../../concepts/local-ai.md) - Running open-weight models on your own hardware or cloud for privacy, cost control, and independence from API providers.
- [Local LLMs as Agents](../../concepts/local-llms-as-agents.md) - Using openly downloadable, self-hosted models for agentic work, which hinges on the model's ability to do reliable function calling.
- [Provider Independence](../../concepts/provider-independence.md) - Architecting agents so the underlying model, framework, or client can be swapped without a rewrite, avoiding lock-in through low-level abstractions.
- [Ollama's Default Context Window](../../concepts/ollama-context-window.md) - Every Ollama model ships with a 2048-token context window that silently truncates history and tool output; the fix is a two-line Modelfile that raises num_ctx.
- [Model-Specific Prompts](../../concepts/model-specific-prompts.md) - Different LLMs need different prompts, so a serious system keeps a library of model-tuned system prompts instead of reusing one prompt written for a single frontier model.

## Contrasts with

- [OpenRouter](./openrouter.md) - Unified API gateway to many LLMs; here it hosts Quasar Alpha, its first stealth/cloaked pre-release Foundation model, free to use.
- [LM Studio](./lm-studio.md) - Desktop app for downloading and running open-weight LLMs locally, the main alternative to Ollama and a requested provider integration for the bolt.new fork.

## Works with

- [Local AI Package](./local-ai-package.md) - Cole's bundled collection of self-hosted AI services (database, n8n, Ollama, Open Web UI) that installs the whole stack together for free.
- [n8n Self-Hosted AI Starter Kit](./n8n-self-hosted-ai-starter-kit.md) - n8n's official Docker Compose package bundling Ollama, Qdrant, Postgres, and n8n so a fully local AI stack (LLMs, vector DB, SQL DB, orchestration) starts with one command.
- [Open Web UI](./open-web-ui.md) - Free, open-source, self-hostable ChatGPT-style chat interface; the frontend used to give n8n agents a polished UI with history, functions, and voice.
- [Qwen](./qwen.md) - Alibaba's open-source LLM family Cole cites as among his favorites that stood the test of time.
- [Llama](./llama.md) - The open LLM model powering the agent, served via Groq in the current build.
- [nomic-embed-text](./nomic-embed-text.md) - Embedding model added to the Ollama container pull so RAG embeddings are available in the workflows.
- [Code Llama](./code-llama.md) - Meta's open-source code-specialized LLM family whose larger 34B variant fails builds that the smaller Qwen 2.5 Coder 32B handles, showing capability beats parameter count.

## Related

- [Model Selection](../../concepts/model-selection.md) - Choosing the right LLM per task by trading off quality, speed, and cost, often routing easy requests to cheap models and hard ones to expensive models.
- [Retrieval-Augmented Generation (RAG)](../../concepts/rag.md) - Grounding an LLM's answers by retrieving relevant documents from an external knowledge base and injecting them into the prompt at query time.
- [Agentic RAG](../../concepts/agentic-rag.md) - Giving an agent retrieval as a tool so it decides when and how to search a knowledge base, picking strategies and issuing follow-up queries instead of a single static lookup.
- [Agent Teams](../../concepts/agent-teams.md) - Coordinating multiple specialized agents, via orchestrators, routers, and handoffs, to solve a task no single agent handles well.
- [LLM Data Privacy Tiers](../../concepts/llm-data-privacy-tiers.md) - The privacy ladder from closed models that may train on your data, to hosted open-model providers, to true self-hosting - and using mock data until you reach the tier your workload requires.
- [Local LLM Hardware Requirements](../../concepts/local-llm-hardware-requirements.md) - The VRAM-per-parameter-tier ladder for local models (7B chat, 14B basic tool-calling, 32B genuinely impressive, 70B near-cloud) that decides which model your hardware can actually run.

## Sources

- [The Ultimate Guide to Local AI and AI Agents (The Future is Here)](../../sources/the-ultimate-guide-to-local-ai-and-ai-agents-the-future-is-here.md) - "[0:03:00] This is one of the open-source platforms that allows us to very easily download and run local large language models"
- [You HAVE to Try Agentic RAG with DeepSeek R1 (Insane Results)](../../sources/you-have-to-try-agentic-rag-with-deepseek-r1-insane-results.md) - "[0:08:00] we're going to take advantage of the fact that Ollama is OpenAI API compatible so we set up an OpenAI server model but we're changing the base URL to just point to Ollama"
- [Introducing Archon - The Revolutionary Operating System for AI Coding](../../sources/introducing-archon-the-revolutionary-operating-system-for-ai-coding.md) - "[0:03:29] You can run everything completely locally with Ollama with your own private knowledge base and MCP server if you want to do so."
- [How to Use Bolt.new for FREE with Local LLMs (And NO Rate Limits)](../../sources/how-to-use-boltnew-for-free-with-local-llms-and-no-rate-limits.md) - "[0:03:54] the default context length for any Ollama model is 248 tokens and that unfortunately is not big enough to fit the Bolt.new prompt"
- [This is Hands Down the BEST Way to Build AI Agents](../../sources/this-is-hands-down-the-best-way-to-build-ai-agents.md) - "[0:25:47] Ollama within Pydantic AI doesn't support streaming like the other providers do I'm not really sure why I think it's a bug in Pydantic AI"
- [DeepSeek R1 Just Revolutionized AI Forever](../../sources/deepseek-r1-just-revolutionized-ai-forever.md) - "[0:06:06] we're here right now in the Ollama page for DeepSeek R1 this is one of the platforms where we can run these models ourselves"
- [I Forked Bolt.new and Made it WAY Better](../../sources/i-forked-boltnew-and-made-it-way-better.md) - "[0:04:16] literally any local model that you can run with Ollama you can have in this platform"
- [Ollama + OpenAI's Swarm - EASILY Run AI Agents Locally](../../sources/ollama-openais-swarm-easily-run-ai-agents-locally.md) - "[0:01:52] Ollama added tool support and the very important thing that I want to call out here... they have OpenAI compatibility"
- [Qwen Just Casually Started the Local AI Revolution](../../sources/qwen-just-casually-started-the-local-ai-revolution.md) - "[0:01:53] my recommended way to use local large language models is with Ollama so you just go to ollama.com click on this nice big download button"
- [Use Open WebUI with Your N8N AI Agents - Voice Chat Included!](../../sources/use-open-webui-with-your-n8n-ai-agents-voice-chat-included.md) - "[0:02:33] Ollama for our large language models"
- [We've Been Building AI Agents WRONG Until Now](../../sources/weve-been-building-ai-agents-wrong-until-now.md) - "[0:08:38] override the base URL right here to point to Local Host Port 11434 where Ollama is currently running on my computer"
- [The OFFICIAL Archon Guide - 10x Your AI Coding Workflow](../../sources/the-official-archon-guide-10x-your-ai-coding-workflow.md) - "[0:05:16] if you want to run things 100% locally to have your own private knowledge base, you can do that with Ollama."
- [I Built the Ultimate RAG MCP Server for AI Coding (Better than Context7)](../../sources/i-built-the-ultimate-rag-mcp-server-for-ai-coding-better-than-context7.md) - "[0:11:34] I also want to make it so you can use Ollama for the embedding model."
- [Local vs. Cloud LLMs/RAG - Let's FINALLY End this Debate](../../sources/local-vs-cloud-llmsrag-lets-finally-end-this-debate.md) - "[0:01:59] we've got Ollama for the large language model because you can use Ollama to host a very wide variety of llms"
- [Run ALL Your AI Locally in Minutes (LLMs, RAG, and more)](../../sources/run-all-your-ai-locally-in-minutes-llms-rag-and-more.md) - "[0:07:32] you can go into the Ollama container ... Ollama pull llama 3.1 ... 70b so I can pull models in real time"
- [Function Calling with ANY LLM for Local AI Agents (Feat. LangChain, HuggingFace, and Llama 3)](../../sources/function-calling-with-any-llm-for-local-ai-agents-feat-langchain-huggingface-and-llama-3.md) - "[0:14:42] I could use Ollama it doesn't matter I have function calling that will work for every single agent"
- [Our Bolt.new Fork's Most Requested Feature is FINALLY Here](../../sources/our-boltnew-forks-most-requested-feature-is-finally-here.md) - "[0:11:39] if you go to Ollama and you try to use like you know Qwen coder for example it's not going to understand images"
- [Make RAG 100x Better with Real-Time Knowledge Graphs](../../sources/make-rag-100x-better-with-real-time-knowledge-graphs.md) - "[0:06:24] something like Ollama if you want this entire implementation to be 100% local which will work because we can host Neo4j completely locally"
- [Build a ChatGPT Style App for Your n8n AI Agents in MINUTES](../../sources/build-a-chatgpt-style-app-for-your-n8n-ai-agents-in-minutes.md) - "[0:04:14] you can use it to chat with your Ollama LLMs. You can use completely self-hosted n8n and connect it into Open WebUI."
- [OpenAI's BRAND NEW Agents SDK (Crash Course)](../../sources/openais-brand-new-agents-sdk-crash-course.md) - "[0:25:24] especially if you're using like OpenRouter or Ollama you won't have access to those traces in the OpenAI dashboard"
- [Create Your Own Private Local AI Cloud Stack in Under 20 Minutes](../../sources/create-your-own-private-local-ai-cloud-stack-in-under-20-minutes.md) - "[0:13:30] since we just have a CPU instance I'm going to run this command to run the Ollama instance on my CPU because I don't have a GPU"
- [The ULTIMATE n8n RAG AI Agent Template - Local AI Edition](../../sources/the-ultimate-n8n-rag-ai-agent-template-local-ai-edition.md) - "[0:29:35] the ones that I installed directly from Ollama and then I have these versions that I created that have 8,000 context"
- [Run Supabase 100% LOCALLY for Your AI Agents](../../sources/run-supabase-100-locally-for-your-ai-agents.md) - "[0:12:26] if you do D- profile none it's actually just going to not run the Ollama container at all so if you have Ollama running outside just on your computer you can still reference that"
- [How to DOMINATE with AI in 2025](../../sources/how-to-dominate-with-ai-in-2025.md) - "[0:15:09] there's just way more options for local llms available that you can download yourself and run yourself from like Hugging Face or Ollama"
- [bolt.diy: The Future of Open Source AI Coding - What's Next?](../../sources/boltdiy-the-future-of-open-source-ai-coding-whats-next.md) - "[0:12:19] there's still that back in making the requests to the large language model that would usually be running on your computer"
- [Flowise + n8n - The BEST No Code + Local AI Agent Combo](../../sources/flowise-n8n-the-best-no-code-local-ai-agent-combo.md) - "[0:12:12] you just go into your terminal run the Ollama list command and this gives you all the models that you have installed with Ollama"
- [Turn ANY AI Agent into a Live Person - Voice Chat Setup in Minutes](../../sources/turn-any-ai-agent-into-a-live-person-voice-chat-setup-in-minutes.md) - "[0:13:41] I've got Ollama running Qwen 2.5 coder 32b locally as the model to build this out"
- [We're Taking this AI Coding Assistant to the MOON [Plus Installation Instructions!]](../../sources/were-taking-this-ai-coding-assistant-to-the-moon-plus-installation-instructions.md) - "[0:00:15] a way to help you all use a bunch of different llms including local ones with [Ollama] within Bolt.new"
- [This Bolt.new Fork is EXPLODING - Don't Miss out on What's Happening!](../../sources/this-boltnew-fork-is-exploding-dont-miss-out-on-whats-happening.md) - "[0:11:10] adding the further changes to support the Ollama API base URL this was a problem initially when we added some more functionality around Ollama"
- [I'm Building the BEST Open Source AI Coding Assistant with YOUR Help](../../sources/im-building-the-best-open-source-ai-coding-assistant-with-your-help.md) - "[0:00:17] you can even use local llms with tools like Ollama so you can generate an infinite amount of code completely for free"
- [Deploy ANY AI App to the Cloud FAST](../../sources/deploy-any-ai-app-to-the-cloud-fast.md) - "[0:18:08] we specifically call our Ollama container just Ollama so I can reference it like this the port is 11434"
