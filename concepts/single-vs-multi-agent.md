---
type: concept
title: "Single vs. Multi-Agent Architecture"
description: "The core architectural decision between one capable agent and a coordinated system of specialized agents with handoffs, and when the added complexity of multi-agent orchestration is actually worth it."
tags: [multi-agent, orchestration, handoffs, swarm, agent-design]
videos: [google-anthropic-and-openais-guides-to-ai-agents-all-in-18-minutes, openais-swarm-a-game-changer-for-ai-agents]
created: 2026-07-21
updated: 2026-07-21
---

# Single vs. Multi-Agent Architecture

The first architectural decision for any agent system is whether one agent can do the job or whether the work should be split across several specialized agents with handoffs between them. Cole's default is unambiguous: start with one. "You want to use a single agent system as much as possible because it is the simplest. But then you'll start to run into issues like tool overload" [0:10:38]. A single agent is easier to build, debug, and reason about; you only add agents when a concrete problem forces you to.

## How it works

The trigger for splitting is tool overload, and Cole gives a concrete threshold: "usually you don't want more than 10 to 15 tools for one agent. Once you get to that point, you want to split your process into multiple different agents" [0:10:52]. Past that, the single agent starts picking the wrong tool because it is choosing from too large a menu. The fix is to carve the process into specialists (one agent per coherent domain of tools) with an orchestrator routing between them and clean handoffs. OpenAI's Swarm exists to teach exactly this orchestration pattern, even though it is not meant for production: "this framework is experimental and its main purpose is educational but it certainly does a good job teaching bulletproof architecture for AI agent orchestration" [0:00:36]. Cole recommends reading its source: "even if you don't use swarm to build something that is production ready you can learn from it" [0:03:22]. The governing principle is that multi-agent complexity is a cost you pay only when a single agent measurably breaks down, not a default to reach for.

## Contrasts with

- [Subagents Pattern](./subagents-pattern.md) - the industry is moving back toward one driving agent that delegates to subagents for isolated tasks, rather than sprawling networks of coordinating specialists.

## Related

- [Agent Teams](./agent-teams.md) - a multi-agent arrangement where several agents work together under coordination.
- [Agentic Workflow Engineering](./agentic-workflow-engineering.md) - designing the orchestration and handoffs that a multi-agent system needs.
- [Context Window Limits](./context-window-limits.md) - tool overload is one symptom; too many tools bloat context and degrade tool choice.

## Tools

- [OpenAI Swarm](../entities/tools/openai-swarm.md) - the experimental, educational framework Cole recommends for learning agent orchestration.

## Sources

- [Google, Anthropic, and OpenAI's Guides to AI Agents ALL in 18 Minutes](../sources/google-anthropic-and-openais-guides-to-ai-agents-all-in-18-minutes.md) - "[0:10:52] Usually you don't want more than 10 to 15 tools for one agent. Once you get to that point, you want to split your process into multiple different agents"
- [OpenAI's Swarm - a GAME CHANGER for AI Agents](../sources/openais-swarm-a-game-changer-for-ai-agents.md) - "[0:00:36] this framework is experimental and its main purpose is educational but it certainly does a good job teaching bulletproof architecture for AI agent orchestration"
