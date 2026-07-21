---
type: concept
title: "Generative UI"
description: "Interfaces the agent generates or drives at runtime, streaming tool activity and reasoning into a live, stateful UI."
tags: [ui, generative, streaming]
videos: [build-render-entire-videos-with-claude-code-full-workflow, ai-agents-can-now-build-their-own-ui-in-real-time-personalized-to-you, build-a-rag-ai-agent-with-real-time-source-validation-copilotkit-pydantic-ai, the-future-of-ai-and-saas-is-agentic-experiences-heres-how-to-build-them, ag-ui-just-released-the-new-wave-of-ai-agent-apps, v0-claude-a-game-changer-for-building-ai-apps, ai-agents-just-got-sexy-ai-agents-masterclass-3, i-made-a-custom-ai-chatbot-site-in-47-lines-of-code, the-only-ai-developer-roadmap-you-need-in-2024]
created: 2026-07-21
updated: 2026-07-21
---

# Generative UI

Generative UI is the idea that the agent, not a fixed template, decides what appears on screen at runtime. Cole gives the plain version: "For the simplest explanation possible, generative UI is the idea that we're going to give our agent the ability to decide the layout and the components for our front end." At its fullest it means "allowing agents to play a role in determining what appears on the screen, how information is structured, and in some cases... even how the layout is composed." Google's spec frames the same mechanism: "all a generative UI spec is is giving agents or LLMs the ability to generate front-end components dynamically... so that your agents can generate dynamic user interfaces based on the conversation."

In practice the degree of agent control is a dial, not a switch. Cole is candid that his own real build sits at the conservative end: "we're using the agent to really just decide the information to display. So it's not picking the components to render. It's not defining the layout." The common middle ground is rendering rich components inside a chat instead of raw text, "We can also render out components in our chat UI. So, we're not limited to just having a bland conversation," by standardizing backend output, "we can take tool calls from the back end and standardize the format... make it look like a nice component in our React frontend." Showing tool activity is a core job of the surface: "tool orchestration... The UI oftentimes need to show progress and the results of using these tools." Generative UI also implies a review-then-commit rhythm on expensive actions, "we have the opportunity here to review things and make adjustments before we actually have it render the full MP4," with granular re-runs so "we don't have to rerun the entire render."

Why it matters is adoption: "no one is going to use your AI app if it's ugly," and yet "you and I would rather be spending most of our time building our AI agents." That tension is why generative-UI tooling exists, from AG-UI's protocol ("a protocol for connecting your agents to your front end to your users in a very standard way") to fast scaffolds. Streamlit turns a script into a UI in minutes but reruns the whole file on every change, "whenever there is any change to your user interface with stream li... streamlet will rerun your entire python script," which forces care to "not... override the list of messages that we built up in the chat history." Others lean on v0 or the Vercel AI SDK, "such a great piece of technology to help make front ends that are so robust working with things in the background."

## Part of

- [Agentic Experiences](./agentic-experiences.md) - generative UI is the rendering mechanism an agentic experience is built on.

## Builds on

- [Contract-First Development](./contract-first.md) - a shared list of renderable components and their types is the contract the agent generates against.
- [Streaming Responses](./streaming-responses.md) - tool activity and tokens stream into the live UI as they happen.

## Related

- [Frontend-Agnostic Agents](./frontend-agnostic-agent.md) - a standardized output format lets one agent drive many UIs.
- [Agent Protocols](./agent-protocols.md) and [Agent Deployment](./agent-deployment.md) - AG-UI as the transport connecting a deployed agent to its front end.
- [Human in the Loop](./human-in-the-loop.md) - review-before-render checkpoints on costly actions.
- [Memory Systems](./memory-systems.md) - chat history the reruns must preserve.
- [Stacking Context-Engineering Strategies](./strategy-stacking.md) - generative UI layered on top of a solid agent backend.

## Tools

- [AG-UI](../entities/tools/ag-ui.md) - the protocol standardizing agent-to-frontend communication.
- [CopilotKit](../entities/tools/copilotkit.md) - renders standardized tool calls as React components.
- [Streamlit](../entities/tools/streamlit.md) - rerun-on-change Python UIs for agent prototypes.
- [Vercel AI SDK](../entities/tools/vercel-ai-sdk.md) - Cole's favorite SDK for robust AI front ends.
- [Pydantic AI](../entities/tools/pydantic-ai.md) - backend agent whose typed output feeds the UI.

## Sources

- [AI Agents Can Now Build Their Own UI in Real Time (Personalized to You)](../sources/ai-agents-can-now-build-their-own-ui-in-real-time-personalized-to-you.md) - "[0:00:16] For the simplest explanation possible, generative UI is the idea that we're going to give our agent the ability to decide the layout and the components for our front end."
- [AI Agents Can Now Build Their Own UI in Real Time (Personalized to You)](../sources/ai-agents-can-now-build-their-own-ui-in-real-time-personalized-to-you.md) - "[0:05:25] So we're using the agent to really just decide the information to display. So it's not picking the components to render. It's not defining the layout."
- [Build a RAG AI Agent with REAL-TIME Source Validation (CopilotKit + Pydantic AI)](../sources/build-a-rag-ai-agent-with-real-time-source-validation-copilotkit-pydantic-ai.md) - "[0:15:58] this is Google's generative UI spec. Essentially, all a generative UI spec is is giving agents or LLMs the ability to generate front-end components dynamically."
- [AG-UI Just Released: The NEW WAVE of AI Agent Apps](../sources/ag-ui-just-released-the-new-wave-of-ai-agent-apps.md) - "[0:02:58] tool orchestration. Working with different tools that your agent will use. The UI oftentimes need to show progress and the results of using these tools."
- [The Future of AI and SaaS is Agentic Experiences (Here's How to Build Them)](../sources/the-future-of-ai-and-saas-is-agentic-experiences-heres-how-to-build-them.md) - "[0:09:08] we can take tool calls from the back end and standardize the format like actually make it look like a nice component in our React frontend."
- [V0 + Claude: A GAME CHANGER for Building AI Apps](../sources/v0-claude-a-game-changer-for-building-ai-apps.md) - "[0:00:32] no one is going to use your AI app if it's ugly."
- [AI Agents Just Got Sexy - AI Agents Masterclass #3](../sources/ai-agents-just-got-sexy-ai-agents-masterclass-3.md) - "[0:03:51] whenever there is any change to your user interface with stream li like a user enters a message... streamlet will rerun your entire python script."
- [Build + Render ENTIRE Videos with Claude Code (Full Workflow)](../sources/build-render-entire-videos-with-claude-code-full-workflow.md) - "[0:09:58] we have the opportunity here to review things and make adjustments before we actually have it render the full MP4."
- [The ONLY AI Developer Roadmap You Need in 2024](../sources/the-only-ai-developer-roadmap-you-need-in-2024.md) - "[0:13:04] the versell AIS SDK is actually my favorite... it is such a great piece of technology to help make front ends that are so robust working with things in the background."
