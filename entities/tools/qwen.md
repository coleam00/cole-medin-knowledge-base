---
type: entity
subtype: tool
title: "Qwen 2.5 Coder 32B"
description: "Alibaba's open-source LLM family Cole cites as among his favorites that stood the test of time."
resource: "https://ollama.com/library/qwen2.5-coder"
tags: [llm, open-source, local-ai, alibaba]
videos: [ai-exploded-in-2025-heres-everything-that-happened, the-ultimate-n8n-rag-ai-agent-template-local-ai-edition, you-have-to-try-agentic-rag-with-deepseek-r1-insane-results, breaking-news-ottodev-is-now-the-official-open-source-boltnew, weve-been-building-ai-agents-wrong-until-now, turn-any-ai-agent-into-a-live-person-voice-chat-setup-in-minutes, qwen-just-casually-started-the-local-ai-revolution, how-to-use-boltnew-for-free-with-local-llms-and-no-rate-limits, ollama-openais-swarm-easily-run-ai-agents-locally]
created: 2026-07-21
updated: 2026-07-21
---

# Qwen 2.5 Coder 32B

Qwen is Alibaba's open-source LLM family, and it is Cole's outright favorite open model, the one he reaches for whenever a demo needs to run [locally](../../concepts/local-ai.md). He says so plainly: "a new version of my favorite open source large language model quen was released and it is quen 2.5 coder 32b" [0:00:32], and he still rates the Qwen 3 line among his favorites that stood the test of time. Qwen 2.5 Coder 32B is the specific checkpoint he credits with making serious local agent work practical.

## How Cole uses it

Qwen is the workhorse behind most of his local builds, run through [Ollama](./ollama.md). He explains the appeal in terms of power-per-parameter: "quen 2.5 coder 32b is honestly the biggest reason ... I absolutely love how much power I get with this model for my agents" [0:15:33]. He was fast to test it, standing it up in Bolt.diy "within like six hours of it being released" [0:04:29], and he uses it as the primary conversation driver in local [agentic RAG](../../concepts/agentic-rag.md) and voice-chat agents.

He also leans on Qwen's range of sizes for [model selection](../../concepts/model-selection.md) within a single system: smaller variants for routing, coder variants for generation, "I'm using quen 2.5 3B for the router and then quen 2.5 coder 7B for our agents writing the SQL queries" [0:10:08]. Even the 7B and 14B models impress him, "it's very impressive that llms can do this especially smaller ones like quen 2.51 14b" [0:09:18], and he ranks the family above Meta's open models: "quen 2.5 is one of my favorites in fact I think it actually performs even better than llama 3.2 and 3.1" [0:17:25].

## Related

- [Local & Self-Hosted AI](../../concepts/local-ai.md) - Qwen is his default local model
- [Model Selection](../../concepts/model-selection.md) - mixing Qwen sizes for router vs. agent roles
- [Agentic RAG](../../concepts/agentic-rag.md) - Qwen as the conversation driver
- [RAG](../../concepts/rag.md), [Agentic Coding](../../concepts/agentic-coding.md)
- [Provider Independence](../../concepts/provider-independence.md) - open weights you fully control
- [Ollama](./ollama.md) - how Cole serves Qwen locally
- [Llama](./llama.md), [DeepSeek R1](./deepseek-r1.md) - sibling open models he benchmarks it against

## Sources

- [Qwen Just Casually Started the Local AI Revolution](../../sources/qwen-just-casually-started-the-local-ai-revolution.md) - "[0:00:32] a new version of my favorite open source large language model quen was released and it is quen 2.5 coder 32b"
- [We've Been Building AI Agents WRONG Until Now](../../sources/weve-been-building-ai-agents-wrong-until-now.md) - "[0:08:24] the model I'm using right now is quen 2.5 coder 32b so we will be using AMA for the demonstration"
- [Ollama + OpenAI's Swarm - EASILY Run AI Agents Locally](../../sources/ollama-openais-swarm-easily-run-ai-agents-locally.md) - "[0:17:25] quen 2.5 is one of my favorites in fact I think it actually performs even better than llama 3.2 and 3.1"
- [BREAKING NEWS: oTToDev is Now the OFFICIAL Open Source Bolt.new](../../sources/breaking-news-ottodev-is-now-the-official-open-source-boltnew.md) - "[0:04:29] when quen 2.5 coder 32b came out within like six hours of it being released I had it up and running with bolt. DIY"
- [The ULTIMATE n8n RAG AI Agent Template - Local AI Edition](../../sources/the-ultimate-n8n-rag-ai-agent-template-local-ai-edition.md) - "[0:09:18] it's very impressive that llms can do this especially smaller ones like quen 2.51 14b"
- [You HAVE to Try Agentic RAG with DeepSeek R1 (Insane Results)](../../sources/you-have-to-try-agentic-rag-with-deepseek-r1-insane-results.md) - "[0:19:57] our primary conversation driver quen 2.5 7B instruct and right away it decides to use our rag with Reasoner tool"
- [Turn ANY AI Agent into a Live Person - Voice Chat Setup in Minutes](../../sources/turn-any-ai-agent-into-a-live-person-voice-chat-setup-in-minutes.md) - "[0:13:41] I've got AMA running quen 2.5 coder 32b locally as the model to build this out"
- [How to Use Bolt.new for FREE with Local LLMs (And NO Rate Limits)](../../sources/how-to-use-boltnew-for-free-with-local-llms-and-no-rate-limits.md) - "[0:00:35] we're going to be using a smaller model Quin 2.5 coder 7B to create this full application and it actually does really really well"
- [AI Exploded in 2025 - Here's Everything That Happened](../../sources/ai-exploded-in-2025-heres-everything-that-happened.md) - "[0:05:07] Alibaba released their Quen 3 models at the very end of April. And these are still some of my favorite open-source large language models to use"
