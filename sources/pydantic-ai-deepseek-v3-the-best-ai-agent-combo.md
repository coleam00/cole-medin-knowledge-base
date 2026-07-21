---
type: source
title: "Pydantic AI + DeepSeek V3 - The BEST AI Agent Combo"
description: "You can turn a no-code n8n agent prototype into a production-grade, model-agnostic Python agent using Pydantic AI and DeepSeek V3 through OpenRouter, keeping it powerful, flexible, and cheap."
youtube_id: zf_D2Eafvk0
url: https://www.youtube.com/watch?v=zf_D2Eafvk0
slug: pydantic-ai-deepseek-v3-the-best-ai-agent-combo
published: 2025-01-05
duration: "0:29:21"
recency_rank: 128
raw: "../raw/pydantic-ai-deepseek-v3-the-best-ai-agent-combo.md"
tags: [agents, pydantic-ai, deepseek, provider-independence]
created: 2026-07-21
updated: 2026-07-21
---

# Pydantic AI + DeepSeek V3 - The BEST AI Agent Combo

This is the third video in Cole's AI agent build series: after planning a GitHub code Q&A agent and prototyping it in n8n, he ports that prototype into a custom-coded Python agent using Pydantic AI. The core argument is that starting with a no-code tool (n8n, Voiceflow, Flowise) gives you a visual blueprint that makes the subsequent coding phase far easier, since the workflow's system prompt, memory model, and tool boundaries are already worked out. You don't always have to graduate from no-code to code, but Cole does it when he needs the control and customization that owning the code provides.

The Pydantic AI build breaks into three parts: dependencies (the HTTP client and API keys tools need), the agent instance (system prompt, model, built-in retry logic), and tools (plain Python functions decorated with @agent.tool, where the docstring tells the LLM when and how to use them). DeepSeek V3 is wired in by pointing Pydantic AI's OpenAIModel at OpenRouter via an overridden base URL and API key, which also makes swapping to Gemini, Claude, Qwen, Mistral, or GPT-4o a one-line environment-variable change. The agent gets three tools against the GitHub API: repo metadata, repo structure, and specific file contents (with a master-branch fallback the n8n version lacked).

Cole emphasizes a division of labor with AI coding assistants: they don't know agent frameworks like Pydantic AI well, so he follows the documentation closely for framework setup, but they excel at writing tool code against well-established APIs like GitHub, especially when handed the downloaded n8n workflow JSON as context. He closes by building a ~50-line CLI, showing careful conversation-history management (including tool calls so the LLM can reference earlier results), and demonstrating the finished agent answering questions about the bolt.diy repo.

## Concepts covered

- [PRD-First Development](../concepts/prd-first-development.md)
- [Vibe Coding](../concepts/vibe-coding.md)
- [Prototype as a Coding Blueprint](../concepts/prototype-as-blueprint.md)
- [Provider Independence](../concepts/provider-independence.md)
- [Model Selection](../concepts/model-selection.md)
- [Agentic Coding](../concepts/agentic-coding.md)
- [Tool Calling](../concepts/tool-use.md)
- [Agent Dependency Injection](../concepts/agent-dependencies.md)
- [Memory Systems](../concepts/memory-systems.md)
- [Agentic Search](../concepts/agentic-search.md)
- [Reduce Assumptions](../concepts/reduce-assumptions.md)

## Entities

- [Pydantic AI](../entities/tools/pydantic-ai.md)
- [DeepSeek](../entities/organizations/deepseek.md)
- [OpenRouter](../entities/tools/openrouter.md)
- [n8n](../entities/tools/n8n.md)
- [GitHub](../entities/tools/github.md)
- [Windsurf](../entities/tools/windsurf.md)
- [Live Agent Studio](../entities/tools/live-agent-studio.md)
- [bolt.diy](../entities/tools/bolt-diy.md)
- [Cole Medin](../entities/people/cole-medin.md)

## Key moments

- **[0:00:18]** Frames the video: port an n8n prototype into a production Python agent with Pydantic AI + DeepSeek V3 via OpenRouter
- **[0:02:07]** Reviews the AI agent roadmap: plan -> prototype (n8n) -> database -> move to Pydantic AI code
- **[0:02:36]** Caveat: you don't always have to move from no-code to custom code; Cole does it for control and customization
- **[0:04:23]** The n8n workflow as a visual blueprint; download the workflow JSON to feed an AI coding assistant
- **[0:08:17]** Three parts of a Pydantic AI agent: dependencies, the agent instance, the tools
- **[0:09:00]** Tools are plain Python functions with an @agent.tool decorator; the docstring tells the LLM when/how to use them
- **[0:11:22]** Begins coding: imports, env vars, and setting the DeepSeek V3 default model
- **[0:11:48]** Override OpenAIModel base URL + API key to route through OpenRouter to DeepSeek V3
- **[0:13:34]** Pydantic AI has retry logic baked in for rate-limit / transient LLM errors
- **[0:14:36]** Pro tip: AI coding assistants don't know frameworks but nail tool code against well-known APIs like GitHub
- **[0:21:08]** Builds a ~50-line CLI to chat with the agent in the terminal
- **[0:23:08]** Conversation-history management: include tool calls so the LLM can reference earlier tool results
- **[0:26:31]** Demo: asks about a specific file; agent reuses cached repo structure instead of re-fetching
- **[0:27:17]** Swap the model by editing one env var (deepseek-chat -> gpt-4o); not tied to a model or framework

## Transcript

[Raw transcript](../raw/pydantic-ai-deepseek-v3-the-best-ai-agent-combo.md)
