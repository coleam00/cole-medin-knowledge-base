---
type: entity
subtype: tool
title: "OpenAI Swarm"
description: "OpenAI's experimental multi-agent framework for building teams of agents that hand off to each other; defaults to OpenAI models but accepts a custom client."
resource: "https://github.com/openai/swarm"
tags: [agent-framework, multi-agent, handoffs, openai, experimental]
videos: [openais-brand-new-agents-sdk-crash-course, ollama-openais-swarm-easily-run-ai-agents-locally, openais-swarm-a-game-changer-for-ai-agents]
created: 2026-07-21
updated: 2026-07-21
---

# OpenAI Swarm

OpenAI Swarm is OpenAI's lightweight, open-source framework for orchestrating teams of agents that hand off work to each other, released as an experiment in clean multi-agent design: "swarm is an open-source AI agent orchestration tool that allows you to write super clean and simple python code to build AI agents" [0:00:00]. Cole covered it the moment it landed, "the initial commit was 5 days ago so swarm is brand spanking new" [0:02:20], and its appeal was how little ceremony it took to stand up cooperating agents, "an incredible new experimental tool called swarm which makes it so easy to create a bunch of AI agents that work together" [0:00:00].

Its defining trait, and its limit, is that OpenAI shipped it as a teaching tool, not a product: "open AI made it very clear that swarm was experimental and meant mostly for educational purposes not a production ready framework" [0:00:15]. That framing matters because it is the direct ancestor of the [OpenAI Agents SDK](./openai-agents-sdk.md), which was built on top of Swarm and rebranded as production-ready. By default it is tied to OpenAI, "in the default setup for swarm it instantiates a client with no parameters which means it just looks for your openai API key environment variable" [0:03:17], but because that client is swappable, Cole demonstrated pointing it at Ollama to run the whole agent team locally, an early example of [provider independence](../../concepts/provider-independence.md) and [local models as agents](../../concepts/local-ai.md).

Cole positioned Swarm as a clean, minimal-abstraction alternative to heavier stacks, weighing whether it beat "Frameworks like Lang chain plus Lang graph or tools like n8n" [0:20:21] for [agent teams](../../concepts/agent-teams.md) built on handoffs and [tool use](../../concepts/tool-use.md). The honest verdict was that its value was educational and as a preview of where OpenAI's agent tooling was heading, which the Agents SDK later delivered.

## Related

- [Agent Teams](../../concepts/agent-teams.md) - Swarm's core model is agents that hand off tasks to each other.
- [Tool Calling](../../concepts/tool-use.md) - agents in a swarm invoke tools to get work done.
- [Provider Independence](../../concepts/provider-independence.md) - a custom client lets Swarm run on non-OpenAI models.
- [Local & Self-Hosted AI](../../concepts/local-ai.md) - Cole ran a Swarm agent team locally via Ollama.
- [Agentic Workflow Engineering](../../concepts/agentic-workflow-engineering.md) - designing the handoff structure between agents.
- [Context Engineering](../../concepts/context-engineering.md) and [Tool Design](../../concepts/tool-design.md) - shaping what each agent sees and can do.
- [OpenAI Agents SDK](./openai-agents-sdk.md) - the production-ready successor built directly on Swarm.
- [Ollama](./ollama.md) - the local runtime Cole pointed Swarm's client at.
- [LangGraph](./langgraph.md) and [LangChain](./langchain.md) - heavier alternatives he benchmarked it against.
- [n8n](./n8n.md) - the no-code alternative he weighed it against.

## Sources

- [OpenAI's Swarm - a GAME CHANGER for AI Agents](../../sources/openais-swarm-a-game-changer-for-ai-agents.md) - "[0:00:00] swarm is an open-Source AI agent orchestration tool that allows you to write super clean and simple python code to build AI agents"
- [OpenAI's BRAND NEW Agents SDK (Crash Course)](../../sources/openais-brand-new-agents-sdk-crash-course.md) - "[0:00:15] open AI made it very clear that swarm was experimental and meant mostly for educational purposes not a production ready framework"
- [Ollama + OpenAI's Swarm - EASILY Run AI Agents Locally](../../sources/ollama-openais-swarm-easily-run-ai-agents-locally.md) - "[0:03:17] in the default setup for swarm it instantiates a client with no parameters which means it just looks for your openai API key environment variable"
- [OpenAI's Swarm - a GAME CHANGER for AI Agents](../../sources/openais-swarm-a-game-changer-for-ai-agents.md) - "[0:20:21] is it better than Frameworks like Lang chain plus Lang graph or tools like n8n"
