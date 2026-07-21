---
type: entity
subtype: tool
title: "Next.js"
description: "React framework hosting the demo's CopilotKit runtime API route for the agent."
resource: "https://nextjs.org"
tags: [react-framework, full-stack]
videos: [i-was-wrong-about-ralph-wiggum, archon-beta-launch-livestream-what-you-missed, ag-ui-just-released-the-new-wave-of-ai-agent-apps, v0-claude-a-game-changer-for-building-ai-apps]
created: 2026-07-21
updated: 2026-07-21
---

# Next.js

Next.js is the [React](./react.md) framework Cole reaches for when he wants one codebase to serve both the interface and the API behind an AI application. Its defining property, in his workflow, is that it collapses the front-end/back-end split: "if I'm using Next.js, it can be my front end and my back end. I don't need Python wrappers for anything." That single-runtime story is why Next.js keeps showing up whenever he builds a [full-stack AI application](../../concepts/full-stack-ai-application.md) rather than a bare Python agent script.

## How Cole uses it

Across the AG-UI and CopilotKit demos, Next.js plays a specific role: it hosts the agent's HTTP endpoint. In the AG-UI build he wires the CopilotKit runtime straight into a Next.js API route, describing it as "just using this instance of the copilot runtime that works for Next.js. So we have this Next.js endpoint here." That route is what turns an agent into an [agent as an API endpoint](../../concepts/agent-as-api-endpoint.md) the React front end can call, and it is the concrete plumbing beneath a [frontend-agnostic agent](../../concepts/frontend-agnostic-agent.md): the agent logic sits behind the endpoint, the UI talks to it over a contract.

Next.js is also Cole's default scaffold for greenfield builds. In the Ralph Wiggum stream it anchors a familiar stack, "I'm going to be using Next.js and Tailwind. I'm going to be using Drizzle for the OM ... Shad CNN as well," and in the V0 walkthrough the generated project is a Next.js app from the first command: "this will actually create a brand new nextjs project in this folder since I don't have one yet and it'll install Shad CN along with it." That makes it the substrate his [planning with AI](../../concepts/planning-with-ai.md) and [PRD-first development](../../concepts/prd-first-development.md) flows tend to target, with conventions captured in [global rules](../../concepts/global-rules.md) so the agent scaffolds consistently.

## Realizes

- [Full-Stack AI Application](../../concepts/full-stack-ai-application.md) - Combining an AI agent with a real front end, database, and API integrations, with the agent acting as the brain connecting the UI to back-end services.
- [Agent as an API Endpoint](../../concepts/agent-as-api-endpoint.md) - Wrapping an AI agent in a web API (typically FastAPI) turns it from a terminal-bound script into a deployable, scalable service any frontend, SaaS, or client can call remotely.
- [Frontend-Agnostic Agents](../../concepts/frontend-agnostic-agent.md) - Decouple the agent backend from any specific UI by emitting standardized events and subscribing to real-time messages (AG-UI, agentic experiences), so the same agent can power any frontend.

## Works with

- [React](./react.md) - Front-end library used for the AG-UI demo application connecting to the agent.
- [CopilotKit](./copilotkit.md) - Open-source front-end library for building agentic applications; the team that built AG-UI, providing React components to wire agents into a UI.
- [AG-UI](./ag-ui.md) - Open protocol (by the CopilotKit team) that standardizes connecting AI agents to front ends via emitted events; ~16 event types.
- [Vercel AI SDK](./vercel-ai-sdk.md) - The front-end AI library whose llms.txt documentation Cole crawls as the demo knowledge base and uses to build a Claude 4 chat UI.

## Contrasts with

- [FastAPI](./fastapi.md) - Python web framework used to serve the swapped-in Python agent endpoint that streams AG-UI events.

## Related

- [Generative UI](../../concepts/generative-ui.md) - Interfaces the agent generates or drives at runtime, streaming tool activity and reasoning into a live, stateful UI.
- [Human in the Loop](../../concepts/human-in-the-loop.md) - Keeping a human as the approver and steerer of agentic work rather than fully automating, so AI augments engineers instead of replacing them.
- [Planning with AI](../../concepts/planning-with-ai.md) - Using the AI to produce a detailed plan before implementation so execution follows a reviewed blueprint instead of improvising.
- [PRD-First Development](../../concepts/prd-first-development.md) - Starting every build from a written product requirements document that becomes the contract the agent implements against.
- [Global Rules](../../concepts/global-rules.md) - Persistent project- or user-level rule files that inject standing context and conventions into every agent run.
- [Strategy Stacking](../../concepts/strategy-stacking.md) - Composing complementary methods (e.g. BMAD for planning, PRP for execution) rather than replacing one with another.
- [Archon](./archon.md) - Cole's free, open-source AI command center and harness builder for AI coding; started as an AI agent that builds other AI agents.

## Sources

- [I Was Wrong About Ralph Wiggum](../../sources/i-was-wrong-about-ralph-wiggum.md) - "[0:12:51] I'm going to be using Next.js and Tailwind. I'm going to be using Drizzle for the OM ... Shad CNN as well"
- [Archon Beta Launch Livestream - What You Missed!](../../sources/archon-beta-launch-livestream-what-you-missed.md) - "[0:19:30] if I'm using Next.js, it can be my front end and my back end. I don't need Python wrappers for anything."
- [AG-UI Just Released: The NEW WAVE of AI Agent Apps](../../sources/ag-ui-just-released-the-new-wave-of-ai-agent-apps.md) - "[0:14:52] we're just using this instance of the copilot runtime that works for Next.js. So we have this Next.js endpoint here"
- [V0 + Claude: A GAME CHANGER for Building AI Apps](../../sources/v0-claude-a-game-changer-for-building-ai-apps.md) - "[0:07:28] this will actually create a brand new nextjs project in this folder since I don't have one yet and it'll install Shad CN along with it"
