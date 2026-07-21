---
type: concept
title: "Memory Systems"
description: "Giving agents durable short- and long-term memory so conversations, user context, and facts persist across sessions and users."
tags: [memory, personalization, sessions, agents, long-term-memory, persistence]
videos: [this-completely-changes-the-way-we-build-production-ai-agents-vercel-eve, i-love-the-karpathy-llm-wiki-but-it-doesnt-scale-heres-what-does, i-built-self-evolving-claude-code-memory-w-karpathys-llm-knowledge-bases, full-guide-build-your-own-ai-second-brain-with-claude-code, ive-used-claude-code-for-2000-hours-heres-how-i-build-anything-with-it, i-built-a-safer-openclaw-alternative-using-claude-code, ai-agents-can-now-build-their-own-ui-in-real-time-personalized-to-you, i-was-wrong-about-ralph-wiggum, are-agent-harnesses-bringing-back-vibe-coding, the-only-ai-tech-stack-you-need-in-2026, learn-90-of-building-ai-agents-in-30-minutes, claude-code-web-just-dropped-but-i-already-built-something-better-with-codex, my-top-20-lessons-from-building-100s-of-ai-agents-super-actionable, why-is-everyone-missing-this-with-ai-agents-memory-tools-that-scale, the-ultimate-guide-to-local-ai-and-ai-agents-the-future-is-here, how-id-learn-ai-agents-fast-if-i-had-to-start-over-full-roadmap, google-anthropic-and-openais-guides-to-ai-agents-all-in-18-minutes, give-me-28-minutes-and-ill-completely-change-the-way-you-build-ai-agents, if-youre-serious-about-building-ai-agents-this-is-your-secret-weapon, the-ultimate-guide-to-building-your-own-mcp-servers-free-template, build-a-chatgpt-style-app-for-your-n8n-ai-agents-in-minutes, the-proven-solution-for-unbelievable-rag-performance-lightrag-guide, 10x-your-ai-agents-with-this-one-agent-architecture, openais-brand-new-agents-sdk-crash-course, build-ai-agents-that-evolve-over-time, i-built-the-ultimate-n8n-rag-ai-agent-template, are-you-building-real-ai-agents-or-just-using-llms, the-glow-up-every-ai-agent-needs, pydantic-ai-deepseek-v3-the-best-ai-agent-combo, use-open-webui-with-your-n8n-ai-agents-voice-chat-included, this-slack-ai-personal-assistant-is-better-than-a-real-person, build-a-full-stack-app-for-your-n8n-ai-agent-in-20-minutes, run-all-your-ai-locally-in-minutes-llms-rag-and-more, v0-claude-a-game-changer-for-building-ai-apps, this-rag-ai-agent-with-n8n-supabase-is-the-real-deal, no-code-rag-agents-you-have-to-check-out-n8n-langchain, the-most-profitable-ai-niche-no-one-is-talking-about, youre-wasting-time-coding-your-ai-agents, ai-agents-the-future-of-ai-or-a-passing-fad, i-made-a-custom-ai-chatbot-site-in-47-lines-of-code, developers-this-is-how-you-stay-relevant-with-ai-ai-agents-masterclass-1, chatgpt-is-the-gift-that-keeps-on-giving-introducing-auto-gpt]
created: 2026-07-21
updated: 2026-07-21
---

# Memory Systems

Memory systems give an agent two kinds of durable recall so it is not amnesiac between turns and between sessions. "This is going to be both for short-term memory conversation history, and long-term memory. So our agent can remember our goals and preferences and instructions between conversations." - ["Google, Anthropic, and OpenAI's Guides to AI Agents ALL in 18 Minutes"](../sources/google-anthropic-and-openais-guides-to-ai-agents-all-in-18-minutes.md) [0:05:19]. Short-term memory is the running conversation history "so it knows what we said to each other up until this point"; long-term memory holds facts about a user that are too large to keep in-context and "It just retrieves things as needed" - ["Learn 90% of Building AI Agents in 30 Minutes"](../sources/learn-90-of-building-ai-agents-in-30-minutes.md) [0:07:21], [0:22:46].

## Long-term memory is just RAG

The load-bearing insight across dozens of Cole's videos is that long-term memory is not a new primitive. "long-term memory for your agents is just another rag. Like that's literally all it is." - ["My Top 20 Lessons from Building 100s of AI Agents"](../sources/my-top-20-lessons-from-building-100s-of-ai-agents-super-actionable.md) [0:37:36], so "a lot of these strategies that we learn for better rag retrieval like query expansion or re-ranking... apply to working with long-term memory as well." [0:38:09]. Operationally it is a sandwich around the LLM call: "I can search for memories inject them into the system prompt and then extract memories after." - ["The ONLY AI Tech Stack You Need in 2026"](../sources/the-only-ai-tech-stack-you-need-in-2026.md) [0:14:57]. A background process does the promotion from short- to long-term: "Redis Iris, with their agent memory, automatically is running a background process that is extracting the key information from the short-term memory to promote it to long-term memory." - ["I Love the Karpathy LLM Wiki but it Doesn't Scale"](../sources/i-love-the-karpathy-llm-wiki-but-it-doesnt-scale-heres-what-does.md) [0:14:40].

## User segregation and sessions

Multi-user memory must never leak across people, and the user ID is the key: "we have to find a way to segregate the memories between users and the user ID is the way to do that. So we would never want to accidentally fetch a memory from a different user" - ["Build AI Agents that EVOLVE Over Time"](../sources/build-ai-agents-that-evolve-over-time.md) [0:07:54]. For short-term memory, a session ID scopes each conversation, typically backed by a Postgres chat-memory table so history survives refreshes and restarts. Production systems checkpoint every turn: "every session is a checkpointed workflow that survives crashes and redeploys... every single turn and tool call, all of that is stored" - ["This Completely Changes the Way We Build Production AI Agents (Vercel Eve)"](../sources/this-completely-changes-the-way-we-build-production-ai-agents-vercel-eve.md) [0:03:54]. A repeated practical lesson: keep tool calls in the history so results are not re-fetched, since "long-term memory... you want to include tool calls in your conversation history." - [My Top 20 Lessons](../sources/my-top-20-lessons-from-building-100s-of-ai-agents-super-actionable.md) [0:38:58].

## Externalizing memory for coding agents

Coding harnesses externalize memory into files that survive a context reset, so a fresh window can catch up: progress files, decision logs, and handoffs. "you have like a handoff.md or a to-do.md communicating between different sub aents or agent teams." - ["I've Used Claude Code for 2,000+ Hours"](../sources/ive-used-claude-code-for-2000-hours-heres-how-i-build-anything-with-it.md) [0:09:56]. The Ralph loop keeps an activity file as "long-term memory for the loop" - ["I Was Wrong About Ralph Wiggum"](../sources/i-was-wrong-about-ralph-wiggum.md) [0:06:17].

## Builds on

- [Retrieval-Augmented Generation (RAG)](./rag.md) - long-term memory is an application of RAG.
- [Vector Embeddings](./vector-embeddings.md) - the representation memory retrieval runs over.

## Related

- [Self-Evolving Memory](./self-evolving-memory.md) - memory that reflects on and rewrites itself over time.
- [Git as Long-Term Memory](./git-as-long-term-memory.md) - commits and versioned files as an agent's durable memory.
- [Second Brain](./second-brain.md) - a personal system built on persistent memory.
- [Agentic RAG](./agentic-rag.md) / [Knowledge Graphs](./knowledge-graphs.md) - retrieval strategies that also power memory recall.
- [Chat Interfaces](./chat-interfaces.md) - where session-scoped short-term memory shows up for users.
- [Human in the Loop](./human-in-the-loop.md) - storing graph state so an agent can resume after an interrupt.
- [Tool Calling](./tool-use.md) - why tool calls belong in the conversation history.
- [Agent Observability](./agent-observability.md) - inspecting stored per-user conversations for debugging.
- [AI Coding Harness](./ai-coding-harness.md) / [Claude Code Hooks](./claude-code-hooks.md) - externalized progress/handoff files as harness memory.

## Tools

- [Mem0](../entities/tools/mem0.md) - a library that sandwiches an agent with searchable long-term memory.
- [Redis](../entities/tools/redis.md) - agent memory that promotes short-term to long-term in the background.
- [Postgres](../entities/tools/postgres-pgvector.md) / [Supabase](../entities/tools/supabase.md) - the SQL stores behind session-scoped chat memory.
- [Pinecone](../entities/tools/pinecone.md) - a vector database used for long-term memory.
- [Langfuse](../entities/tools/langfuse.md) - filter stored conversations by user ID for support and debugging.
- [LangGraph](../entities/tools/langgraph.md) - SQLite/Postgres memory savers for graph state.
- [Claude Agent SDK](../entities/tools/claude-agent-sdk.md) - built-in plus custom RAG memory for personal agents.
- [n8n](../entities/tools/n8n.md) - no-code Postgres/Redis chat-memory nodes keyed by session ID.

## Sources

- [Google, Anthropic, and OpenAI's Guides to AI Agents ALL in 18 Minutes](../sources/google-anthropic-and-openais-guides-to-ai-agents-all-in-18-minutes.md) - "[0:05:19] This is going to be both for short-term memory conversation history, and long-term memory. So our agent can remember our goals and preferences and instructions between conversations."
- [My Top 20 Lessons from Building 100s of AI Agents (Super Actionable)](../sources/my-top-20-lessons-from-building-100s-of-ai-agents-super-actionable.md) - "[0:37:36] long-term memory for your agents is just another rag. Like that's literally all it is."
- [The ONLY AI Tech Stack You Need in 2026](../sources/the-only-ai-tech-stack-you-need-in-2026.md) - "[0:14:57] I can search for memories inject them into the system prompt and then extract memories after. So I can kind of just sandwich my agent no matter how I build it with mem zero."
- [I Love the Karpathy LLM Wiki but it Doesn't Scale. Here's What Does.](../sources/i-love-the-karpathy-llm-wiki-but-it-doesnt-scale-heres-what-does.md) - "[0:14:40] Redis Iris, with their agent memory, automatically is running a background process that is extracting the key information from the short-term memory to promote it to long-term memory."
- [Build AI Agents that EVOLVE Over Time](../sources/build-ai-agents-that-evolve-over-time.md) - "[0:07:54] we have to find a way to segregate the memories between users and the user ID is the way to do that."
- [This Completely Changes the Way We Build Production AI Agents (Vercel Eve)](../sources/this-completely-changes-the-way-we-build-production-ai-agents-vercel-eve.md) - "[0:03:54] every session is a checkpointed workflow that survives crashes and redeploys... every single turn and tool call, all of that is stored"
- [Learn 90% of Building AI Agents in 30 Minutes](../sources/learn-90-of-building-ai-agents-in-30-minutes.md) - "[0:22:46] you're able to basically have infinite memory for an agent, but you don't have to give it all to the LLM at once. It just retrieves things as needed"
- [Give Me 28 Minutes and I'll Completely Change the Way You Build AI Agents](../sources/give-me-28-minutes-and-ill-completely-change-the-way-you-build-ai-agents.md) - "[0:10:02] Before the input goes directly into the LLM, we're actually adding in this memory retrieval step... a step at the end of the graph execution as well to extract relevant memories"
- [Why is Everyone Missing This with AI Agents?! (Memory + Tools that Scale)](../sources/why-is-everyone-missing-this-with-ai-agents-memory-tools-that-scale.md) - "[0:05:44] I set it up in a way where I can say remember, that's my keyword here, telling the agent to remember something for later for my user specifically"
- [I've Used Claude Code for 2,000+ Hours - Here's How I Build Anything With It](../sources/ive-used-claude-code-for-2000-hours-heres-how-i-build-anything-with-it.md) - "[0:09:56] the last strategy that I have for externalizing agent memory is progress files and decision logs... you have like a handoff.md or a to-do.md"
- [I Was Wrong About Ralph Wiggum](../sources/i-was-wrong-about-ralph-wiggum.md) - "[0:06:17] the activity MD. This is the markdown file where we keep track of what has happened in previous loops... this basically long-term memory for the loop"
- [The ULTIMATE Guide to Building Your Own MCP Servers (Free Template)](../sources/the-ultimate-guide-to-building-your-own-mcp-servers-free-template.md) - "[0:04:56] It integrates with mem which is a library to give long-term memory to our AI agents."
- [If You're Serious About Building AI Agents, This is Your Secret Weapon](../sources/if-youre-serious-about-building-ai-agents-this-is-your-secret-weapon.md) - "[0:24:12] we can go into the sessions tab in Langfuse and we can take a look at all of the individual conversations that users are having with our agent and we can even filter by user ID."
- [OpenAI's BRAND NEW Agents SDK (Crash Course)](../sources/openais-brand-new-agents-sdk-crash-course.md) - "[0:23:33] now we give this third parameter which is the user context and when you do this it's not given to the llm"
- [I Built Self-Evolving Claude Code Memory w/ Karpathy's LLM Knowledge Bases](../sources/i-built-self-evolving-claude-code-memory-w-karpathys-llm-knowledge-bases.md) - "[0:10:48] It'll immediately level up the long-term memory for your coding agent when it's working on that project specifically."
- [Full Guide - Build Your Own AI Second Brain with Claude Code](../sources/full-guide-build-your-own-ai-second-brain-with-claude-code.md) - "[0:09:45] you'll recognize some of these files like the soul.md, the user.md, the memory.md. That architecture is genius and it's so simple"
- [I Built a Safer OpenClaw Alternative Using Claude Code](../sources/i-built-a-safer-openclaw-alternative-using-claude-code.md) - "[0:06:04] there's also a SQLite database with a very light implementation of rag built in as well. So again, super elegant but super simple."
- [Are Agent Harnesses Bringing Back Vibe Coding?](../sources/are-agent-harnesses-bringing-back-vibe-coding.md) - "[0:17:14] we also have the claude progress text file. This is the core file for handoffs."
- [How I'd Learn AI Agents FAST if I Had to Start Over (Full Roadmap)](../sources/how-id-learn-ai-agents-fast-if-i-had-to-start-over-full-roadmap.md) - "[0:11:30] we also have other components like memory systems for long-term memory, guard rails for input and output, fallback mechanisms"
- [10x Your AI Agents with this ONE Agent Architecture](../sources/10x-your-ai-agents-with-this-one-agent-architecture.md) - "[0:35:41] you can set up a SQL light or a postgress memory saver if you want to use superbase or something to store all this state"
- [The Ultimate Guide to Local AI and AI Agents (The Future is Here)](../sources/the-ultimate-guide-to-local-ai-and-ai-agents-the-future-is-here.md)
- [Claude Code Web JUST Dropped but I Already Built Something BETTER (with Codex!)](../sources/claude-code-web-just-dropped-but-i-already-built-something-better-with-codex.md)
- [The PROVEN Solution for Unbelievable RAG Performance (LightRAG Guide)](../sources/the-proven-solution-for-unbelievable-rag-performance-lightrag-guide.md)
- [Build a ChatGPT Style App for Your n8n AI Agents in MINUTES](../sources/build-a-chatgpt-style-app-for-your-n8n-ai-agents-in-minutes.md)
- [AI Agents Can Now Build Their Own UI in Real Time (Personalized to You)](../sources/ai-agents-can-now-build-their-own-ui-in-real-time-personalized-to-you.md)
- [I Built the ULTIMATE n8n RAG AI Agent Template](../sources/i-built-the-ultimate-n8n-rag-ai-agent-template.md)
- [Are You Building REAL AI Agents or Just Using LLMs?](../sources/are-you-building-real-ai-agents-or-just-using-llms.md)
- [The GLOW-UP Every AI Agent Needs](../sources/the-glow-up-every-ai-agent-needs.md)
- [Pydantic AI + DeepSeek V3 - The BEST AI Agent Combo](../sources/pydantic-ai-deepseek-v3-the-best-ai-agent-combo.md)
- [Use Open WebUI with Your N8N AI Agents - Voice Chat Included!](../sources/use-open-webui-with-your-n8n-ai-agents-voice-chat-included.md)
- [This Slack AI Personal Assistant is Better than a Real Person](../sources/this-slack-ai-personal-assistant-is-better-than-a-real-person.md)
- [Build a FULL Stack App for your n8n AI Agent in 20 Minutes](../sources/build-a-full-stack-app-for-your-n8n-ai-agent-in-20-minutes.md)
- [Run ALL Your AI Locally in Minutes (LLMs, RAG, and more)](../sources/run-all-your-ai-locally-in-minutes-llms-rag-and-more.md)
- [V0 + Claude: A GAME CHANGER for Building AI Apps](../sources/v0-claude-a-game-changer-for-building-ai-apps.md)
- [This RAG AI Agent with n8n + Supabase is the Real Deal](../sources/this-rag-ai-agent-with-n8n-supabase-is-the-real-deal.md)
- [No Code RAG Agents? You HAVE to Check out n8n + LangChain](../sources/no-code-rag-agents-you-have-to-check-out-n8n-langchain.md)
- [The MOST Profitable AI Niche NO ONE is Talking About](../sources/the-most-profitable-ai-niche-no-one-is-talking-about.md)
- [You're WASTING TIME Coding Your AI Agents](../sources/youre-wasting-time-coding-your-ai-agents.md)
- [AI Agents: The Future of AI or a Passing Fad?](../sources/ai-agents-the-future-of-ai-or-a-passing-fad.md)
- [I Made a Custom AI Chatbot Site in 47 Lines of Code](../sources/i-made-a-custom-ai-chatbot-site-in-47-lines-of-code.md)
- [Developers, THIS is How you Stay Relevant with AI - AI Agents Masterclass #1](../sources/developers-this-is-how-you-stay-relevant-with-ai-ai-agents-masterclass-1.md)
- [ChatGPT is the GIFT that keeps on GIVING - Introducing Auto-GPT](../sources/chatgpt-is-the-gift-that-keeps-on-giving-introducing-auto-gpt.md)
