---
type: entity
subtype: tool
title: "CopilotKit"
description: "Open-source front-end library for building agentic applications; the team that built AG-UI, providing React components to wire agents into a UI."
resource: "https://www.copilotkit.ai"
tags: [frontend, react, agentic-experiences, open-source]
videos: [ai-agents-can-now-build-their-own-ui-in-real-time-personalized-to-you, build-a-rag-ai-agent-with-real-time-source-validation-copilotkit-pydantic-ai, the-future-of-ai-and-saas-is-agentic-experiences-heres-how-to-build-them, ag-ui-just-released-the-new-wave-of-ai-agent-apps]
created: 2026-07-21
updated: 2026-07-21
---

# CopilotKit

CopilotKit is an open-source React library for building user-facing agentic applications. As Cole describes it, "here is the official announcement for AG-UI that was developed by the CopilotKit team, which if you didn't know, CopilotKit is an open-source front-end library for building agentic applications" ([0:01:04]). It supplies the React components and hooks that connect an agent to an interface, and the same team authored the [AG-UI](./ag-ui.md) protocol that CopilotKit integrates with natively: "for our front end, we're going to be using CopilotKit. This is a React library that makes it very easy for us to build userfacing agentic applications. It integrates natively with AG-UI" ([0:02:36]).

Cole reaches for CopilotKit because it collapses an enormous amount of plumbing. "This would be hundreds or even thousands of lines of code if I wasn't using CopilotKit, AG-UI, and Pydantic AI" ([0:11:41]). In his reference stack it owns the entire front end while a [Pydantic AI](./pydantic-ai.md) agent owns the backend, wired together over AG-UI: "they recently added a direct firstparty integration between CopilotKit and Pydantic AI through AG-UI" ([0:02:54]). The version 1 release added the useAgent hook ("CopilotKit recently had their big version 1 release that came with the use agent hook" [0:15:23]), and later releases brought support for Google's [A2UI](./a2ui.md) generative-UI spec, so the same UI can render agent-defined components.

CopilotKit is the tool Cole most associates with what he calls [agentic experiences](../../concepts/agentic-experiences.md): "CopilotKit is what enables agentic experiences as I like to call it" ([0:02:39]). It delivers [generative UI](../../concepts/generative-ui.md), real-time streaming, RAG source validation, and [human-in-the-loop](../../concepts/human-in-the-loop.md) controls out of the box, while keeping the agent [frontend-agnostic](../../concepts/frontend-agnostic-agent.md) through the AG-UI [contract](../../concepts/contract-first.md). It integrates directly with the rest of his tech stack, which is why it recurs as his default front-end choice for agent apps.

## Realizes

- [Agentic Experiences](../../concepts/agentic-experiences.md) - Building apps where the agent drives a live, generative UI and front-end/back-end state stay in sync, instead of a static chat box.
- [Generative UI](../../concepts/generative-ui.md) - Interfaces the agent generates or drives at runtime, streaming tool activity and reasoning into a live, stateful UI.
- [Frontend-Agnostic Agents](../../concepts/frontend-agnostic-agent.md) - Decouple the agent backend from any specific UI by emitting standardized events and subscribing to real-time messages, so the same agent can power any frontend.
- [Contract-First Development](../../concepts/contract-first.md) - Define the shared interface or data contract between an agent's frontend, backend, and collaborating agents before building either side, so components can be developed independently.
- [Human in the Loop](../../concepts/human-in-the-loop.md) - Keeping a human as the approver and steerer of agentic work rather than fully automating, so AI augments engineers instead of replacing them.
- [Retrieval-Augmented Generation (RAG)](../../concepts/rag.md) - Grounding an LLM's answers by retrieving relevant documents from an external knowledge base and injecting them into the prompt at query time.

## Works with

- [AG-UI](./ag-ui.md) - Open protocol (by the CopilotKit team) that standardizes connecting AI agents to front ends via emitted events; ~16 event types.
- [A2UI](./a2ui.md) - Google's generative-UI specification for how an agent defines the components (id, name, children, props) the front end renders.
- [Pydantic AI](./pydantic-ai.md) - Cole's framework for the individual agents, structured around three parts: dependencies, the agent definition, and tools.
- [MCP](./mcp.md) - The protocol used to connect agents and coding assistants to external tools and servers.

## Sources

- [The Future of AI and SaaS is Agentic Experiences](../../sources/the-future-of-ai-and-saas-is-agentic-experiences-heres-how-to-build-them.md) - "[0:02:36] for our front end, we're going to be using CopilotKit. This is a React library that makes it very easy for us to build userfacing agentic applications. It integrates natively with AG-UI."
- [AI Agents Can Now Build Their Own UI in Real Time](../../sources/ai-agents-can-now-build-their-own-ui-in-real-time-personalized-to-you.md) - "[0:11:41] This would be hundreds or even thousands of lines of code if I wasn't using CopilotKit, AG-UI, and Pydantic AI."
- [Build a RAG AI Agent with REAL-TIME Source Validation](../../sources/build-a-rag-ai-agent-with-real-time-source-validation-copilotkit-pydantic-ai.md) - "[0:02:39] CopilotKit is what enables agentic experiences as I like to call it."
- [AG-UI Just Released](../../sources/ag-ui-just-released-the-new-wave-of-ai-agent-apps.md) - "[0:01:04] CopilotKit is an open-source front-end library for building agentic applications."
