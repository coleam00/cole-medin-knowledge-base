---
type: concept
title: "Context Window Limits"
description: "Managing finite context by summarizing, compacting, and sizing what you load so the model stays sharp on long tasks."
tags: [context, compaction, long-context]
videos: [ive-used-claude-code-for-2000-hours-heres-how-i-build-anything-with-it, my-top-20-lessons-from-building-100s-of-ai-agents-super-actionable, the-ultimate-guide-to-local-ai-and-ai-agents-the-future-is-here, the-ultimate-n8n-rag-ai-agent-template-local-ai-edition, how-to-use-boltnew-for-free-with-local-llms-and-no-rate-limits, brand-new-stealth-llm-released-on-openrouter-its-a-beast, this-slack-ai-personal-assistant-is-better-than-a-real-person]
created: 2026-07-21
updated: 2026-07-21
---

# Context Window Limits

Context window limits are the finite token budget every model carries, and managing that budget well is what keeps a model sharp across long tasks. The best strategy is to rarely hit compaction at all: "The best compression strategy is not needing compression." That follows from good isolation and selection, "you shouldn't need to compress often if you're doing the right isolate and select well... you want to avoid compressing as much as possible." When you must, summarization is the lever: "the /compact is very useful as well, especially because we can optionally provide summarization instructions."

The limit has a specific failure signature: when you exceed it, the front of the prompt is silently dropped first. "when you hit that context length, you'll see that the system prompt is the first thing to go. You start to lose those instructions for the agent." This is why an agent that suddenly ignores its tools or persona is usually out of room, not broken: "If your large language model is starting to go completely off the rails and ignore your system prompt and forget that it has these tools... it's probably because you reached the context length." So Cole's standing lesson is to "watch your context length."

Limits bite hardest in local and self-hosted setups, where defaults are tiny and must be overridden explicitly. Ollama caps every model low by default, "they limit every single large language model to 2,000 tokens for the context limit which is just tiny... you have to override that yourself with this environment variable," and you raise it by "inheriting from the base model and then just changing the context length with this parameter." Frontier hosted models push the ceiling the other way, up to "1 million tokens for its context length," but a bigger ceiling is not a mandate to fill it (that is [Context Rot](./context-rot.md)). A common tactic for staying under the limit is summarizing accumulated history: condensing "30 messages" so you do not reload them all.

## Contrasts with

- [Context Rot](./context-rot.md) - the soft quality decline that sets in well before you hit the hard token ceiling.

## Related

- [Context Reset](./context-reset.md) - resetting the window is the cleanest way to stay under the limit.
- [Memory Systems](./memory-systems.md) - offload durable state so it does not consume the window.
- [Model Selection](./model-selection.md) - context length is a key model-choice criterion.
- [Local & Self-Hosted AI](./local-ai.md), [Model Quantization](./model-quantization.md), [Open-Source & Local AI Coding](./open-source-ai-coding.md) - where small default limits must be raised manually.
- [Tool Calling](./tool-use.md) - tool instructions are among the first things lost when the limit is hit.
- [The WHISK Framework](./the-whisk-framework.md) - a workflow built around limited windows.
- [Ollama's Default Context Window](./ollama-context-window.md) - Every Ollama model ships with a 2048-token context window that silently truncates history and tool output; the fix is a two-line Modelfile that raises num_ctx.

## Tools

- [Ollama](../entities/tools/ollama.md) - defaults every model to a tiny context limit; override via env var or a custom Modelfile.
- [Claude Code](../entities/tools/claude-code.md) - `/compact` summarizes to reclaim room under the limit.

## Sources

- [I've Used Claude Code for 2,000+ Hours](../sources/ive-used-claude-code-for-2000-hours-heres-how-i-build-anything-with-it.md) - "[0:21:17] The best compression strategy is not needing compression."
- [My Top 20 Lessons from Building 100s of AI Agents](../sources/my-top-20-lessons-from-building-100s-of-ai-agents-super-actionable.md) - "[0:34:50] when you hit that context length, you'll see that the system prompt is the first thing to go. You start to lose those instructions for the agent."
- [The Ultimate Guide to Local AI and AI Agents](../sources/the-ultimate-guide-to-local-ai-and-ai-agents-the-future-is-here.md) - "[0:38:00] they limit every single large language model to 2,000 tokens for the context limit which is just tiny... you have to override that yourself with this environment variable."
- [The ULTIMATE n8n RAG AI Agent Template - Local AI Edition](../sources/the-ultimate-n8n-rag-ai-agent-template-local-ai-edition.md) - "[0:28:29] ollama models by default they only have a context length of 2,000 tokens... you start to lose things like the system prompt and the tools instructions."
- [How to Use Bolt.new for FREE with Local LLMs](../sources/how-to-use-boltnew-for-free-with-local-llms-and-no-rate-limits.md) - "[0:04:11] there is a very easy way to create a slight variation of any model you want that has an increased context length."
- [BRAND NEW "Stealth" LLM Released on OpenRouter](../sources/brand-new-stealth-llm-released-on-openrouter-its-a-beast.md) - "[0:00:18] 1 million tokens for its context length which is very impressive."
- [This Slack AI Personal Assistant is Better than a Real Person](../sources/this-slack-ai-personal-assistant-is-better-than-a-real-person.md) - "[0:10:49] you come back and you don't want to read through 30 messages."
