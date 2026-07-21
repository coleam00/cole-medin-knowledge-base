---
type: entity
subtype: tool
title: "Claude"
description: "Named as an example of a large language model that can be turned into an agent."
resource: "https://claude.ai"
tags: [llm, anthropic, model-access]
videos: [my-top-20-lessons-from-building-100s-of-ai-agents-super-actionable, stop-paying-for-gpt-claude-other-llms-get-them-all-in-one-place, openais-swarm-a-game-changer-for-ai-agents, build-a-full-stack-app-for-your-n8n-ai-agent-in-20-minutes, ai-agents-the-future-of-ai-or-a-passing-fad]
created: 2026-07-21
updated: 2026-07-21
---

# Claude

Claude is Anthropic's family of large language models, and across Cole's videos it is the default reference point for a frontier closed-source model. It is one of the raw LLMs he lists when explaining what an agent is built from: "AI agents are large language models like Claude GPT or llama" [0:00:47]. On its own Claude is a conversational model; it becomes an agent only when wrapped with tools, memory, and an [agent loop](../../concepts/what-is-an-ai-agent.md).

## How Cole uses it

Claude is Cole's go-to model for code generation. In his top-20 lessons he is blunt about [model selection](../../concepts/model-selection.md): "I find Claude 3.7 Sonnet um to generally be the best LLM for coding um overall" [0:32:29]. He reaches for it whenever raw code output speed matters, praising how "Claude is just going to chug right through all of this code it does it so so fast" [0:03:38] when scaffolding a full-stack app with the Claude, Streamlit, and Supabase combo. He also uses it for adjacent build chores, generating SQL scripts and mock data for a database: "I actually use Claude believe it or not to generate the SQL scripts to give me all the tables that I need" [0:09:37].

Claude also anchors his access story. It is one of the models he shows unified behind a single subscription so you do not pay per provider: "we have Claude 3.5 Sonnet selected right now you've got GPT-4o llama 3.1 405b Gemini 1.5 Pro even 01 is in this platform" [0:02:21]. Sonnet 3.5 recurs as the "powerful closed model" bar he measures local models against.

## Works with

- [Memory Systems](../../concepts/memory-systems.md) - Giving agents durable short- and long-term memory so conversations, user context, and facts persist across sessions and users.
- [Chat Interfaces](../../concepts/chat-interfaces.md) - Wrapping agents in chat surfaces (websites, DMs, platforms) with adapters, a shared message format, and durable history.
- [Tool Design](../../concepts/tool-design.md) - Designing agent tools to be few, single-purpose, and well-described (often via docstrings) so the model uses them reliably.
- [Agent Teams](../../concepts/agent-teams.md) - Coordinating multiple specialized agents, via orchestrators, routers, and handoffs, to solve a task no single agent handles well.
- [Claude Code](./claude-code.md) - Anthropic's terminal-based agentic coding assistant that is the subject of this complete-guide walkthrough.

## Contrasts with

- [ChatGPT](./chatgpt.md) - The AI chat model used throughout as the example interface for prompting.
- [GPT-4](./gpt-4.md) - OpenAI's model cited as strong enough that it reasons step by step without being told to.
- [Gemini](./gemini.md) - Google's LLM line; Gemini 2.5 led general-purpose models for months and Gemini 3 is considered the most powerful general LLM at year-end.
- [Llama](./llama.md) - The open LLM model powering the agent, served via Groq in the current build.

## Related

- [Claude Opus 4.8](./claude-opus-4-8.md) - Anthropic's reasoning-heavy Claude release that owns planning, page copy, integrations, and fixes in Cole's mixed-provider frontend workflow.
- [Claude Sonnet 4.5](./claude-sonnet-4-5.md) - Anthropic's coding-focused model release that topped the coding and agentic-tool-use benchmarks over Opus 4.1 and shipped as the default model in Claude Code 2.0.
- [Claude 3.5 Sonnet](./claude-3-5-sonnet.md) - Anthropic's mid-2024 flagship model and the only LLM Cole could not break in his agentic stress test, making it his clear winner for multi-step tool-using workflows.
- [Model Selection](../../concepts/model-selection.md) - Choosing the right LLM per task by trading off quality, speed, and cost, often routing easy requests to cheap models and hard ones to expensive models.
- [Human in the Loop](../../concepts/human-in-the-loop.md) - Keeping a human as the approver and steerer of agentic work rather than fully automating, so AI augments engineers instead of replacing them.

## Sources

- [My Top 20 Lessons from Building 100s of AI Agents (Super Actionable)](../../sources/my-top-20-lessons-from-building-100s-of-ai-agents-super-actionable.md) - "[0:32:29] I find Claude 3.7 Sonnet um to generally be the best LLM for coding um overall."
- [STOP Paying for GPT, Claude, & Other LLMs - Get them ALL in One Place](../../sources/stop-paying-for-gpt-claude-other-llms-get-them-all-in-one-place.md) - "[0:02:21] we have Claude 3.5 Sonnet selected right now you've got GPT-4o llama 3.1 405b Gemini 1.5 Pro even 01 is in this platform"
- [OpenAI's Swarm - a GAME CHANGER for AI Agents](../../sources/openais-swarm-a-game-changer-for-ai-agents.md) - "[0:09:37] I actually use Claude believe it or not to generate the SQL scripts to give me all the tables that I need for an rssv database and then some mock data as well"
- [Build a FULL Stack App for your n8n AI Agent in 20 Minutes](../../sources/build-a-full-stack-app-for-your-n8n-ai-agent-in-20-minutes.md) - "[0:03:38] Claude is just going to chug right through all of this code it does it so so fast"
- [AI Agents: The Future of AI or a Passing Fad?](../../sources/ai-agents-the-future-of-ai-or-a-passing-fad.md) - "[0:00:47] AI agents are large language models like Claude GPT or llama"
