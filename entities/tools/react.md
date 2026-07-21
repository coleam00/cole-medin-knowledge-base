---
type: entity
subtype: tool
title: "React"
description: "Front-end library used for the AG-UI demo application connecting to the agent."
resource: "https://react.dev"
tags: [front-end, ui-library]
videos: [ai-agents-can-now-build-their-own-ui-in-real-time-personalized-to-you, build-a-rag-ai-agent-with-real-time-source-validation-copilotkit-pydantic-ai, ag-ui-just-released-the-new-wave-of-ai-agent-apps, the-only-ai-developer-roadmap-you-need-in-2024]
created: 2026-07-21
updated: 2026-07-21
---

# React

React is the front-end library Cole builds his agent applications on, and in the AG-UI era it becomes the surface an agent can drive directly. The sharpest framing comes from the generative-UI demo: "It really is just a basic React component, but it's the agent that decides when we render this. And it decides all the values." The component is ordinary React; what is new is that the agent, not a click handler, decides when it appears and what it holds.

## How Cole uses it

React is the "application built with something like React" that sits on the client side of every AG-UI and CopilotKit build. It is the layer that makes [generative UI](../../concepts/generative-ui.md) concrete: instead of hard-coding every screen, Cole exposes React components the agent can choose to render, so the interface personalizes itself at runtime. It is equally the home of [human in the loop](../../concepts/human-in-the-loop.md) controls, where a rendered component pauses the agent and hands the decision back to the user.

The other recurring use is as a direct client for the agent. In the CopilotKit + Pydantic AI RAG build, Cole notes "we can access and interact with our direct to LLM agents directly from React components," so a [RAG](../../concepts/rag.md) agent's retrieval and source-validation results stream straight into React state. This only works because the agent lives behind a stable interface: React talks to a [frontend-agnostic agent](../../concepts/frontend-agnostic-agent.md) over [agent protocols](../../concepts/agent-protocols.md) like AG-UI, which is a [contract-first](../../concepts/contract-first.md) arrangement where the UI and the agent are decoupled by an agreed schema.

React is also, plainly, Cole's preferred framework. In his developer-roadmap video he calls it out directly: "you got Frameworks like react which is my favorite because of nextjs" - the library he likes precisely because of the [Next.js](./nextjs.md) full-stack framework built on top of it.

## Related

- Realizes [generative UI](../../concepts/generative-ui.md) and [human in the loop](../../concepts/human-in-the-loop.md); connects to agents via [agent protocols](../../concepts/agent-protocols.md) and a [contract-first](../../concepts/contract-first.md), [frontend-agnostic](../../concepts/frontend-agnostic-agent.md) boundary.
- Composed with [Next.js](./nextjs.md), [CopilotKit](./copilotkit.md), [AG-UI](./ag-ui.md), the [Vercel AI SDK](./vercel-ai-sdk.md), and [Pydantic AI](./pydantic-ai.md) agents behind the endpoint.

## Sources

- [AI Agents Can Now Build Their Own UI in Real Time (Personalized to You)](../../sources/ai-agents-can-now-build-their-own-ui-in-real-time-personalized-to-you.md) - "[0:13:12] It really is just a basic React component, but it's the agent that decides when we render this. And it decides all the values."
- [Build a RAG AI Agent with REAL-TIME Source Validation (CopilotKit + Pydantic AI)](../../sources/build-a-rag-ai-agent-with-real-time-source-validation-copilotkit-pydantic-ai.md) - "[0:04:57] we can access and interact with our direct to LLM agents directly from React components."
- [AG-UI Just Released: The NEW WAVE of AI Agent Apps](../../sources/ag-ui-just-released-the-new-wave-of-ai-agent-apps.md) - "[0:01:21] our application built with something like React"
- [The ONLY AI Developer Roadmap You Need in 2024](../../sources/the-only-ai-developer-roadmap-you-need-in-2024.md) - "[0:12:37] you got Frameworks like react which is my favorite because of nextjs"
