---
type: entity
subtype: tool
title: "Pydantic AI"
description: "Cole's framework for the individual agents, structured around three parts: dependencies, the agent definition, and tools."
resource: "https://ai.pydantic.dev"
tags: [agent-framework, python, pydantic, favorite]
videos: [pydantic-ai-20-the-new-best-way-to-build-ai-agents-is-composing-capabilities, i-love-the-karpathy-llm-wiki-but-it-doesnt-scale-heres-what-does, googles-agents-cli-the-cli-skills-combination-to-ship-ai-agents-easily, claude-plans-gemini-designs-the-workflow-to-build-beautiful-frontends, everything-you-thought-about-building-ai-agents-is-wrong, ai-agents-can-now-build-their-own-ui-in-real-time-personalized-to-you, claude-skills-arent-just-for-claude-heres-how-to-build-them-for-any-agent, build-a-rag-ai-agent-with-real-time-source-validation-copilotkit-pydantic-ai, the-simplest-rag-stack-that-actually-works-complete-guide, github-is-the-future-of-ai-coding-heres-why, the-only-ai-tech-stack-you-need-in-2026, learn-90-of-building-ai-agents-in-30-minutes, super-special-livestream-this-weekend-live-ai-agent-build, the-official-archon-guide-10x-your-ai-coding-workflow, turn-any-file-into-llm-knowledge-in-seconds, the-future-of-ai-and-saas-is-agentic-experiences-heres-how-to-build-them, i-built-my-claude-code-subagents-dream-team-to-create-any-ai-agent, my-top-20-lessons-from-building-100s-of-ai-agents-super-actionable, introducing-archon-the-revolutionary-operating-system-for-ai-coding, a-complete-guide-to-claude-code-here-are-all-the-best-strategies, build-any-ai-agent-with-this-context-engineering-blueprint, context-engineering-is-the-new-vibe-coding-learn-this-now, introducing-rag-20-agentic-rag-knowledge-graphs-free-template, ai-code-that-fixes-itself-an-mcp-you-can-try-now, the-ultimate-guide-to-local-ai-and-ai-agents-the-future-is-here, make-rag-100x-better-with-real-time-knowledge-graphs, how-id-learn-ai-agents-fast-if-i-had-to-start-over-full-roadmap, ag-ui-just-released-the-new-wave-of-ai-agent-apps, google-anthropic-and-openais-guides-to-ai-agents-all-in-18-minutes, the-3-must-have-mcp-servers-for-any-ai-coding-and-how-to-use-them, give-me-28-minutes-and-ill-completely-change-the-way-you-build-ai-agents, i-built-the-ultimate-rag-mcp-server-for-ai-coding-better-than-context7, turn-any-website-into-llm-knowledge-in-seconds-evolved, if-youre-serious-about-building-ai-agents-this-is-your-secret-weapon, this-mcp-server-for-ai-coding-assistants-will-10x-your-productivity, google-is-quietly-revolutionizing-ai-agents-this-is-huge, the-ultimate-guide-to-building-your-own-mcp-servers-free-template, the-proven-solution-for-unbelievable-rag-performance-lightrag-guide, build-an-army-of-ai-agents-on-autopilot-with-archon-heres-how, the-mcp-integration-everyone-is-sleeping-on-mcp-custom-ai-agents, 10x-your-ai-agents-with-this-one-agent-architecture, claude-mcp-has-changed-ai-forever-heres-what-you-need-to-know, openais-brand-new-agents-sdk-crash-course, build-ai-agents-that-evolve-over-time, introducing-archon-an-ai-agent-that-builds-ai-agents, are-you-building-real-ai-agents-or-just-using-llms, coding-subagents-the-next-evolution-of-ai-ides, this-is-hands-down-the-best-way-to-build-ai-agents, you-have-to-try-agentic-rag-with-deepseek-r1-insane-results, deploying-billions-of-ai-agents-is-easier-than-you-think, n8n-crawl4ai-scrape-any-website-in-minutes-with-no-code, insane-new-strategy-for-building-ai-agent-apps, the-future-of-rag-is-agentic-learn-this-strategy-now, turn-any-website-into-llm-knowledge-in-seconds, the-glow-up-every-ai-agent-needs, pydantic-ai-deepseek-v3-the-best-ai-agent-combo, how-to-dominate-with-ai-in-2025, revealing-my-complete-ai-agent-blueprint, i-created-the-best-ai-agent-platform-in-just-2-months, weve-been-building-ai-agents-wrong-until-now]
created: 2026-07-21
updated: 2026-07-21
---

# Pydantic AI

Pydantic AI is an open-source Python framework for building production-grade AI agents, and it is the tool Cole reaches for more than any other: "Pydantic AI has been my favorite AI agent framework for a long time now" [0:00:00]. Across dozens of videos it is his default for individual agents, chosen because it makes agents easy to build while keeping full control. As he puts it, "it is a python agent framework that makes it super easy to build AI agents while still giving us all of the customizability and control that we need" [0:01:52]. The name is deliberate: the team "have validation at the core of what they believe in" [0:02:44], so structured, type-validated inputs and outputs are the foundation rather than an afterthought.

Cole's mental model for the framework is a repeatable three-part shape. "you can think of building Pydantic AI agents as building three distinct parts" [0:08:20]: first the dependencies, "things like the API keys and database connections that your agent tools need" [0:08:37]; then the agent definition itself with its model and system prompt; then the tools, where "this doc string that you have at the start of a function is how you tell the agent when and how to use this tool" [0:30:56]. This is the concrete realization of [agent dependency injection](../../concepts/agent-dependencies.md), [docstrings as tool descriptions](../../concepts/docstrings-as-tool-descriptions.md), and the general [agent core components](../../concepts/agent-core-components.md) pattern. He builds [RAG](../../concepts/rag.md) and [agentic RAG](../../concepts/agentic-rag.md) agents on it constantly, injecting vector stores and knowledge-graph clients as runtime dependencies.

Why it keeps winning: it stays fast and provider-flexible while adopting new standards early. "Pydantic AI is constantly supporting new protocols like MCP when that first came out, A2A for UI event streams" [0:07:23], it supports OpenAI-compatible endpoints for [local models](../../concepts/local-ai.md), it has retry logic and built-in evaluation, and it wires cleanly into observability through Logfire. The 2.0 release reframed everything around "a single primitive called the capability" [0:00:17], composing agents from reusable capabilities. Cole pairs it with LangGraph for multi-agent orchestration and increasingly weighs it against coding-agent SDKs for personal agents, where he still favors a framework for sub-second, scalable production work.

## Realizes

- [The Core Components of an Agent](../../concepts/agent-core-components.md) - the dependencies, agent, tools shape Cole codes against.
- [Agent Dependency Injection](../../concepts/agent-dependencies.md) - runtime dependencies (API keys, DB connections, vector stores) injected into the agent.
- [Docstrings as Tool Descriptions](../../concepts/docstrings-as-tool-descriptions.md) - how a tool function's docstring tells the agent when to call it.

## Works with

- [LangGraph](./langgraph.md) - the multi-agent orchestrator Cole pairs it with; Pydantic AI builds the individual agents.
- [Logfire](./logfire.md) - the observability library Pydantic AI uses under the hood.
- [MCP](./mcp.md) - Pydantic AI adopted MCP-server tool integration early.
- [Archon](./archon.md) - curates Pydantic AI documentation so coding assistants produce correct agent code.

## Contrasts with

- [Claude Agent SDK](./claude-agent-sdk.md) - the coding-agent SDK he weighs against a framework for personal agents.
- [Codex](./codex.md) - another coding-agent SDK contrasted with a framework for personal agents.
- [CrewAI](./crewai.md) - a sibling framework named as an interchangeable AG-UI backend.
- [SDK vs. Framework Decision](../../concepts/sdk-vs-framework-decision.md) - Pydantic AI is the "framework" side of that fork.

## Related

- [Retrieval-Augmented Generation (RAG)](../../concepts/rag.md) - the most common agents Cole builds on Pydantic AI.
- [Agentic RAG](../../concepts/agentic-rag.md) - retrieval wired in as an agent tool on top of Pydantic AI.
- [Memory Systems](../../concepts/memory-systems.md) - Mem0 and Graphiti wired in as agent tools/dependencies.
- [Human in the Loop](../../concepts/human-in-the-loop.md) - a review gate layered onto Pydantic AI agents.
- [Context Engineering](../../concepts/context-engineering.md) - curating exactly what each agent's prompt receives.
- [Provider Independence](../../concepts/provider-independence.md) - swap the model with one line, a core reason Cole favors it.

## Sources

- [Pydantic AI 2.0: The New Best Way to Build AI Agents is Composing Capabilities](../../sources/pydantic-ai-20-the-new-best-way-to-build-ai-agents-is-composing-capabilities.md) - "[0:00:00] Pydantic AI has been my favorite AI agent framework for a long time now."
- [Pydantic AI 2.0: The New Best Way to Build AI Agents is Composing Capabilities](../../sources/pydantic-ai-20-the-new-best-way-to-build-ai-agents-is-composing-capabilities.md) - "[0:00:17] They just put out their 2.0 release and this is a big evolution in the way that we build AI agents. This version of the framework centers around a single primitive called the capability."
- [10x Your AI Agents with this ONE Agent Architecture](../../sources/10x-your-ai-agents-with-this-one-agent-architecture.md) - "[0:08:20] you can think of building Pydantic AI agents as building three distinct parts"
- [10x Your AI Agents with this ONE Agent Architecture](../../sources/10x-your-ai-agents-with-this-one-agent-architecture.md) - "[0:08:37] the first component is defining the dependencies these are things like the API keys and database connections that your agent tools need"
- [This is Hands Down the BEST Way to Build AI Agents](../../sources/this-is-hands-down-the-best-way-to-build-ai-agents.md) - "[0:01:52] it is a python agent framework that makes it super easy to build AI agents while still giving us all of the customizability and control that we need"
- [The Future of RAG is Agentic - Learn this Strategy NOW](../../sources/the-future-of-rag-is-agentic-learn-this-strategy-now.md) - "[0:30:56] in Pydantic AI this doc string that you have at the start of a function is how you tell the agent when and how to use this tool"
- [The ONLY AI Tech Stack You Need in 2026](../../sources/the-only-ai-tech-stack-you-need-in-2026.md) - "[0:07:23] Pydantic AI is constantly supporting new protocols like MCP when that first came out, A2A for UI event streams."
- [If You're Serious About Building AI Agents, This is Your Secret Weapon](../../sources/if-youre-serious-about-building-ai-agents-this-is-your-secret-weapon.md) - "[0:11:36] Right now, Pydantic AI is my favorite AI agent framework. They just do everything so well, including logging and monitoring because Pydantic AI uses a library called Logfire under the hood."
- [We've Been Building AI Agents WRONG Until Now](../../sources/weve-been-building-ai-agents-wrong-until-now.md) - "[0:02:44] this team is who are going ahead and making Pydantic AI... because they have validation at the core of what they believe in"
- [Everything You Thought About Building AI Agents is Wrong](../../sources/everything-you-thought-about-building-ai-agents-is-wrong.md) - "[0:07:59] I'm still using Pydantic AI all of the time. Building with these frameworks is what's going to allow you to build agents with sub-second response times"
