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

Claude is Anthropic's family of large language models, and across Cole's videos it is the default reference point for a frontier closed-source model. It is one of the raw LLMs he lists when explaining what an agent is built from: "AI agents are large language models like Claud GPT or llama" [0:00:47]. On its own Claude is a conversational model; it becomes an agent only when wrapped with tools, memory, and an [agent loop](../../concepts/what-is-an-ai-agent.md).

## How Cole uses it

Claude is Cole's go-to model for code generation. In his top-20 lessons he is blunt about [model selection](../../concepts/model-selection.md): "I find Claude 3.7 Sonnet um to generally be the best LLM for coding um overall" [0:32:29]. He reaches for it whenever raw code output speed matters, praising how "Claude is just going to chug right through all of this code it does it so so fast" [0:03:38] when scaffolding a full-stack app with the Claude, Streamlit, and Supabase combo. He also uses it for adjacent build chores, generating SQL scripts and mock data for a database: "I actually use cloud believe it or not to generate the SQL scripts to give me all the tables that I need" [0:09:37].

Claude also anchors his access story. It is one of the models he shows unified behind a single subscription so you do not pay per provider: "we have Claude 3.5 Sonet selected right now you've got gbt 40 llama 3.1 405b Gemini 1.5 Pro even 01 is in this platform" [0:02:21]. Sonnet 3.5 recurs as the "powerful closed model" bar he measures local models against.

## Related

- [Model Selection](../../concepts/model-selection.md) - picking the right model per job; Claude wins his coding pick
- [Memory Systems](../../concepts/memory-systems.md) - what turns a Claude chat into a stateful agent
- [Chat Interfaces](../../concepts/chat-interfaces.md) - Claude as a conversational surface
- [Agent Teams](../../concepts/agent-teams.md) - Claude as a member model in multi-agent setups
- [Tool Design](../../concepts/tool-design.md) - giving Claude capabilities beyond text
- [Human in the Loop](../../concepts/human-in-the-loop.md)
- [Claude Code](./claude-code.md) - Anthropic's agentic coding tool driven by Claude
- [ChatGPT](./chatgpt.md), [GPT-4](./gpt-4.md), [Google Gemini 2.0 Flash](./gemini.md), [Llama](./llama.md) - sibling frontier and open models

## Sources

- [My Top 20 Lessons from Building 100s of AI Agents (Super Actionable)](../../sources/my-top-20-lessons-from-building-100s-of-ai-agents-super-actionable.md) - "[0:32:29] I find Claude 3.7 Sonnet um to generally be the best LLM for coding um overall."
- [STOP Paying for GPT, Claude, & Other LLMs - Get them ALL in One Place](../../sources/stop-paying-for-gpt-claude-other-llms-get-them-all-in-one-place.md) - "[0:02:21] we have Claude 3.5 Sonet selected right now you've got gbt 40 llama 3.1 405b Gemini 1.5 Pro even 01 is in this platform"
- [OpenAI's Swarm - a GAME CHANGER for AI Agents](../../sources/openais-swarm-a-game-changer-for-ai-agents.md) - "[0:09:37] I actually use cloud believe it or not to generate the SQL scripts to give me all the tables that I need for an rssv database and then some mock data as well"
- [Build a FULL Stack App for your n8n AI Agent in 20 Minutes](../../sources/build-a-full-stack-app-for-your-n8n-ai-agent-in-20-minutes.md) - "[0:03:38] Claude is just going to chug right through all of this code it does it so so fast"
- [AI Agents: The Future of AI or a Passing Fad?](../../sources/ai-agents-the-future-of-ai-or-a-passing-fad.md) - "[0:00:47] AI agents are large language models like Claud GPT or llama"
