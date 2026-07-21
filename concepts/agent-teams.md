---
type: concept
title: "Agent Teams"
description: "Coordinating multiple specialized agents, via orchestrators, routers, and handoffs, to solve a task no single agent handles well."
tags: [multi-agent, orchestration, routing]
videos: [youre-hardly-using-what-claude-code-has-to-offer-its-insane, how-to-properly-use-claude-code-agent-teams-full-live-build, claude-codes-agent-teams-are-insane-multiple-ai-agents-coding-together-in-real-time, github-is-the-future-of-ai-coding-heres-why, archon-beta-launch-livestream-what-you-missed, how-id-learn-ai-agents-fast-if-i-had-to-start-over-full-roadmap, google-anthropic-and-openais-guides-to-ai-agents-all-in-18-minutes, if-youre-serious-about-building-ai-agents-this-is-your-secret-weapon, google-is-quietly-revolutionizing-ai-agents-this-is-huge, build-a-chatgpt-style-app-for-your-n8n-ai-agents-in-minutes, build-an-army-of-ai-agents-on-autopilot-with-archon-heres-how, 10x-your-ai-agents-with-this-one-agent-architecture, openais-brand-new-agents-sdk-crash-course, this-is-hands-down-the-best-way-to-build-ai-agents, boltdiy-the-future-of-open-source-ai-coding-whats-next, ottodev-is-becoming-the-best-open-source-ai-coding-assistant, ollama-openais-swarm-easily-run-ai-agents-locally, im-building-the-best-open-source-ai-coding-assistant-with-your-help, openais-swarm-a-game-changer-for-ai-agents, the-most-profitable-ai-niche-no-one-is-talking-about, ai-agents-the-future-of-ai-or-a-passing-fad, i-will-win-the-nvidia-ai-agents-developer-contest]
created: 2026-07-21
updated: 2026-07-21
---

# Agent Teams

An agent team is several specialized agents coordinated to solve a task that overwhelms any single agent. The motivating principle is a human analogy Cole returns to constantly: "complex problems always yield better results when tackled by a team of people with different specializations and with AI agents it works exactly the same way" [0:00:00], and "just like with humans AI agents work better the more narrow their role and goals are it is all about Focus" [0:00:15]. There is a concrete technical reason to split, not just an aesthetic one: "no matter how large of a context window an agent can handle it will start to hallucinate the more tools you add into the agent so it always helps to have multiple specialized agents working together otherwise known as mixture of experts" [0:14:32].

Teams are wired together with a handful of recurring coordination patterns. The most common is orchestrator-workers, "the orchestrator and worker flow where we have one primary agent that is managing many other agents taking the task and splitting it up" [0:09:36]. Another is routing, "the solution is to use many agents that are tied together through a router and so the user will send a message here to the first AI agent which is just a router" [0:04:39], which then forwards to the specialist that owns that request. OpenAI's Swarm and Agents SDK formalize a third, handoffs, "this is how you have different agents that work together so you have specialized agents that handle different parts of tackling a problem" [0:01:50]. Cole's own setups often give each specialist an MCP server and bind them under one primary agent: "I connect them all together with this primary agent that is given a tool with Pydantic AI to call into each of these specialized subagents" [0:17:32].

Claude Code's Agent Teams feature pushes this further by letting the workers talk to each other, not just report up. "with agent teams, we have the main agent that it uh spawns all these teammates, but they all share a task list and they communicate to each other" [0:02:24], so "Teammate two can send a message back to the main agent as it's working. They can knock off tasks and like coordinate with each other" [0:02:36]. This is the step beyond static subagents: shared task list plus peer messaging lets parallel agents avoid stepping on each other. Agents built on different stacks can still cooperate if they share a wire protocol: "maybe our sales agent is built with LangGraph and then our finance agent is built without a framework at all... as long as they're all following the A2A protocol, they can communicate with each other seamlessly" [0:04:57].

> **Contradiction:** Cole is bullish on the multi-agent principle but explicit that Claude Code's Agent Teams feature is not production-ready. He warns "this is a very experimental feature. The agents don't communicate very optimally right now... I wouldn't use agent teams yet for anything that you're going to be shipping to production" [0:03:32], and names "the two downsides to agent teams, one it's very non-deterministic... And then the second downside is it's very tokenheavy when you have all of these agents running at the same time" [0:02:36]. The idea is proven; this particular implementation is a preview.

## Builds on

- [Subagents Pattern](./subagents-pattern.md) - agent teams extend subagents by letting the spawned agents communicate rather than only report back.
- [What Is an AI Agent](./what-is-an-ai-agent.md) - the single agent a team is composed of.

## Contrasts with

- [Single vs. Multi-Agent Architecture](./single-vs-multi-agent.md) - the decision of whether a team is warranted at all versus one focused agent.

## Related

- [Agent Architecture Patterns](./agent-architecture-patterns.md) - orchestrator-workers, routing, and handoffs are the patterns teams are built from.
- [Parallel Agent Execution](./parallel-agent-execution.md) - teams whose members run at the same time.
- [Synthesizer Agent](./synthesizer-agent.md) - the final agent in a parallel architecture that takes every sub-agent's output and summarizes, formats, and optionally validates it into one coherent answer, replacing a dumb non-LLM aggregator.
- [Parallel Agentic Coding](./parallel-agentic-coding.md) - agent teams applied to shipping code on separate branches.
- [Multi-Model Agents](./multi-model-agent.md) - mixture of experts where teammates run on different models.
- [Agent Protocols](./agent-protocols.md) - A2A and friends, the wire protocols that let cross-framework agents coordinate.
- [Model Selection](./model-selection.md) - routing cheap/fast models for metadata and stronger models for the real work.
- [Context Rot](./context-rot.md) - the degradation that splitting responsibility across agents avoids.
- [Contract-First Development](./contract-first.md) - clear boundaries between what each agent owns.
- [Memory Systems](./memory-systems.md) - shared state and task lists the team coordinates over.
- [Planning with AI](./planning-with-ai.md) - decomposing the task before assigning slices to agents.
- [Provider Independence](./provider-independence.md) - mixing agents from different vendors on one team.
- [Agentic Workflow Engineering](./agentic-workflow-engineering.md) - the discipline of assembling these coordinated systems.

## Tools

- [Claude Code](../entities/tools/claude-code.md) - its Agent Teams feature gives spawned teammates a shared task list and peer messaging.
- [OpenAI Swarm](../entities/tools/openai-swarm.md) - a lightweight framework showcasing the handoff and routing patterns.
- [OpenAI Agents SDK](../entities/tools/openai-agents-sdk.md) - productionizes handoffs between specialized agents.
- [Pydantic AI](../entities/tools/pydantic-ai.md) - used to bind specialized subagents under one primary agent as tools.
- [Archon](../entities/tools/archon.md) - assigns tasks and documents to distinct agents that coordinate on a shared plan.
- [n8n](../entities/tools/n8n.md) - routes to a primary agent or a cheap metadata model based on session state.
- [Ollama](../entities/tools/ollama.md) - runs a local router-plus-specialists team over a database.
- [BMAD Method](../entities/tools/bmad-method.md) - An open-source context-engineering framework (installed via npx bmad-method install) that ships expert sub-agent personas (analyst, PM, architect, scrum master, dev, QA) as markdown prompts driving separate greenfield and brownfield planning and development workflows.
- [iTerm2](../entities/tools/iterm2.md) - macOS terminal application with split-pane support; one of only two terminals Claude Code can drive to display agent teams live.
- [tmux](../entities/tools/tmux.md) - Terminal multiplexer (Cole's recommended option) that Claude Code drives to create the split-pane windows showing each agent-team teammate working in real time.

## Sources

- [10x Your AI Agents with this ONE Agent Architecture](../sources/10x-your-ai-agents-with-this-one-agent-architecture.md) - "[0:00:00] complex problems always yield better results when tackled by a team of people with different specializations and with AI agents it works exactly the same way"
- [You're Hardly Using What Claude Code Has to Offer, it's Insane](../sources/youre-hardly-using-what-claude-code-has-to-offer-its-insane.md) - "[0:03:32] this is a very experimental feature. The agents don't communicate very optimally right now... I wouldn't use agent teams yet for anything that you're going to be shipping to production."
- [How to Properly Use Claude Code Agent Teams (FULL LIVE BUILD)](../sources/how-to-properly-use-claude-code-agent-teams-full-live-build.md) - "[0:02:24] with agent teams, we have the main agent that it uh spawns all these teammates, but they all share a task list and they communicate to each other."
- [Claude Code's Agent Teams Are Insane - Multiple AI Agents Coding Together in Real Time](../sources/claude-codes-agent-teams-are-insane-multiple-ai-agents-coding-together-in-real-time.md) - "[0:00:33] our primary agent, it actually decided the team to form based on the request that I gave it... under the hood, each one of these agents is working on the exact same task list together."
- [Google, Anthropic, and OpenAI's Guides to AI Agents ALL in 18 Minutes](../sources/google-anthropic-and-openais-guides-to-ai-agents-all-in-18-minutes.md) - "[0:09:36] we have the orchestrator and worker flow where we have one primary agent that is managing many other agents taking the task and splitting it up"
- [Google is Quietly Revolutionizing AI Agents (This is HUGE)](../sources/google-is-quietly-revolutionizing-ai-agents-this-is-huge.md) - "[0:04:57] maybe our sales agent is built with LangGraph and then our finance agent is built without a framework at all... as long as they're all following the A2A protocol, they can communicate with each other seamlessly."
- [OpenAI's BRAND NEW Agents SDK (Crash Course)](../sources/openais-brand-new-agents-sdk-crash-course.md) - "[0:14:32] no matter how large of a context window an agent can handle it will start to hallucinate the more tools you add into the agent so it always helps to have multiple specialized agents working together otherwise known as mixture of experts"
- [If You're Serious About Building AI Agents, This is Your Secret Weapon](../sources/if-youre-serious-about-building-ai-agents-this-is-your-secret-weapon.md) - "[0:17:32] I connect them all together with this primary agent that is given a tool with Pydantic AI to call into each of these specialized subagents."
- [OpenAI's Swarm - a GAME CHANGER for AI Agents](../sources/openais-swarm-a-game-changer-for-ai-agents.md) - "[0:04:41] the solution to that is to actually have multiple agents that are working together tackling different parts of the problem or handling different parts of the system"
- [AI Agents: The Future of AI or a Passing Fad?](../sources/ai-agents-the-future-of-ai-or-a-passing-fad.md) - "[0:04:39] the solution is to use many agents that are tied together through a router and so the user will send a message here to the first AI agent which is just a router"
- [How I'd Learn AI Agents FAST if I Had to Start Over (Full Roadmap)](../sources/how-id-learn-ai-agents-fast-if-i-had-to-start-over-full-roadmap.md) - "[0:11:30] it's just so important for us for more complex systems to distribute responsibility between agents just like it's powerful to distribute responsibility between people."
- [Build an ARMY of AI Agents on Autopilot with Archon, Here's How](../sources/build-an-army-of-ai-agents-on-autopilot-with-archon-heres-how.md) - "[0:00:47] Archon to build an AI agent army it's a bunch of specialized subagents that are each leveraging an MCP server so that my primary agent can be connected to a bunch of different services super easily"
- [Archon Beta Launch Livestream - What You Missed!](../sources/archon-beta-launch-livestream-what-you-missed.md) - "[0:24:30] different tasks can be assigned to different agents like we can have Mary tasked with the research... then have like the project manager tasked with the things that we have related to creating the PRD"
- [Ollama + OpenAI's Swarm - EASILY Run AI Agents Locally](../sources/ollama-openais-swarm-easily-run-ai-agents-locally.md) - "[0:08:11] we have this router agent that takes in the initial request from the user and it determines which specialized agent is going to best be able to create a SQL query"
- [This is Hands Down the BEST Way to Build AI Agents](../sources/this-is-hands-down-the-best-way-to-build-ai-agents.md) - "[0:04:46] you can think about it as these agents like the researcher the chart generator the router these can all be large language models that are each agents built with Pydantic AI"
- [GitHub is the Future of AI Coding (Here's Why)](../sources/github-is-the-future-of-ai-coding-heres-why.md) - "[0:08:41] all of our branches are named with a suffix representing the coding assistant that's actually operating on that branch... distinguish between the different dev team members that we have our different AI dev team members."
- [The MOST Profitable AI Niche NO ONE is Talking About](../sources/the-most-profitable-ai-niche-no-one-is-talking-about.md) - "[0:10:03] you have some automation workflows that can put specific tags on leads and that's what determines what agent actually applies to that specific contact"
- [Build a ChatGPT Style App for Your n8n AI Agents in MINUTES](../sources/build-a-chatgpt-style-app-for-your-n8n-ai-agents-in-minutes.md) - "[0:20:18] if the session ID is none... it'll just go to this very simple cheap and fast LLM. Otherwise it'll go to our primary agent."
- [bolt.diy: The Future of Open Source AI Coding - What's Next?](../sources/boltdiy-the-future-of-open-source-ai-coding-whats-next.md) - "[0:07:24] you could have agents behind the scenes like a mixture of experts that create the code instead of just a sing single call to a single llm"
- [oTToDev is Becoming the BEST Open Source AI Coding Assistant](../sources/ottodev-is-becoming-the-best-open-source-ai-coding-assistant.md)
- [I'm Building the BEST Open Source AI Coding Assistant with YOUR Help](../sources/im-building-the-best-open-source-ai-coding-assistant-with-your-help.md)
- [I Will Win the Nvidia AI Agents Developer Contest](../sources/i-will-win-the-nvidia-ai-agents-developer-contest.md)
