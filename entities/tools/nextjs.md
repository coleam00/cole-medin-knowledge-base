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

Next.js is the [React](./react.md) framework Cole reaches for when he wants one codebase to serve both the interface and the API behind an AI application. Its defining property, in his workflow, is that it collapses the front-end/back-end split: "if I'm using Nex.js, it can be my front end and my back end. I don't need Python wrappers for anything." That single-runtime story is why Next.js keeps showing up whenever he builds a [full-stack AI application](../../concepts/full-stack-ai-application.md) rather than a bare Python agent script.

## How Cole uses it

Across the AG-UI and CopilotKit demos, Next.js plays a specific role: it hosts the agent's HTTP endpoint. In the AG-UI build he wires the CopilotKit runtime straight into a Next.js API route, describing it as "just using this instance of the copilot runtime that works for nex.js. So we have this nex.js endpoint here." That route is what turns an agent into an [agent as an API endpoint](../../concepts/agent-as-api-endpoint.md) the React front end can call, and it is the concrete plumbing beneath a [frontend-agnostic agent](../../concepts/frontend-agnostic-agent.md): the agent logic sits behind the endpoint, the UI talks to it over a contract.

Next.js is also Cole's default scaffold for greenfield builds. In the Ralph Wiggum stream it anchors a familiar stack, "I'm going to be using Nex.js and Tailwind. I'm going to be using Drizzle for the OM ... Shad CNN as well," and in the V0 walkthrough the generated project is a Next.js app from the first command: "this will actually create a brand new nextjs project in this folder since I don't have one yet and it'll install Shad CN along with it." That makes it the substrate his [planning with AI](../../concepts/planning-with-ai.md) and [PRD-first development](../../concepts/prd-first-development.md) flows tend to target, with conventions captured in [global rules](../../concepts/global-rules.md) so the agent scaffolds consistently.

## Related

- Serves the interface layer for [generative UI](../../concepts/generative-ui.md) and [human in the loop](../../concepts/human-in-the-loop.md) experiences, where the agent drives what the page renders.
- Sibling framework and library it composes with: [React](./react.md), [CopilotKit](./copilotkit.md), [AG-UI](./ag-ui.md), and the [Vercel AI SDK](./vercel-ai-sdk.md).
- Removes the need for a separate Python API tier ([FastAPI](./fastapi.md)) in Cole's single-runtime setups, and shows up inside [Archon](./archon.md)-adjacent tooling as the management front end.

## Sources

- [I Was Wrong About Ralph Wiggum](../../sources/i-was-wrong-about-ralph-wiggum.md) - "[0:12:51] I'm going to be using Nex.js and Tailwind. I'm going to be using Drizzle for the OM ... Shad CNN as well"
- [Archon Beta Launch Livestream - What You Missed!](../../sources/archon-beta-launch-livestream-what-you-missed.md) - "[0:19:30] if I'm using Nex.js, it can be my front end and my back end. I don't need Python wrappers for anything."
- [AG-UI Just Released: The NEW WAVE of AI Agent Apps](../../sources/ag-ui-just-released-the-new-wave-of-ai-agent-apps.md) - "[0:14:52] we're just using this instance of the copilot runtime that works for nex.js. So we have this nex.js endpoint here"
- [V0 + Claude: A GAME CHANGER for Building AI Apps](../../sources/v0-claude-a-game-changer-for-building-ai-apps.md) - "[0:07:28] this will actually create a brand new nextjs project in this folder since I don't have one yet and it'll install Shad CN along with it"
