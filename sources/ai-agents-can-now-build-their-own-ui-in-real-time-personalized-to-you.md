---
type: source
title: "AI Agents Can Now Build Their Own UI in Real Time (Personalized to You)"
description: "Generative UI lets an agent choose the components and layout of a front end on the fly, and a Gen-UI-agnostic stack (Pydantic AI + A2UI + AG-UI + CopilotKit) makes it practical to build ultra-personalized, self-adapting interfaces."
youtube_id: MD8VQzvMVek
url: https://www.youtube.com/watch?v=MD8VQzvMVek
slug: ai-agents-can-now-build-their-own-ui-in-real-time-personalized-to-you
published: 2026-02-04
duration: "0:15:18"
recency_rank: 37
raw: "../raw/ai-agents-can-now-build-their-own-ui-in-real-time-personalized-to-you.md"
tags: [generative-ui, agents, pydantic-ai]
created: 2026-07-21
updated: 2026-07-21
---
# AI Agents Can Now Build Their Own UI in Real Time (Personalized to You)

Cole demos a personalized research dashboard whose layout and components were generated entirely on the fly by an agent, with nothing preconfigured. This is generative UI: giving the agent the ability to decide what appears on screen, how information is structured, and even how the layout is composed, rather than just feeding data into a fixed layout. He frames it as the future of software, where sites like Amazon or Google could look different for every user because the interface is personalized to their behavior and interests.

He lays out a spectrum of how much control is handed to the agent versus the programmer: static UI (agent only decides the data/values), open-ended UI (agent generates raw HTML/CSS/JSX on the fly, maximally flexible but a security and performance risk), and the middle option he favors, declarative UI (agent picks from a preconfigured component library and supplies props, keeping freedom within controllable bounds). Google's A2UI specification exemplifies the declarative approach.

The demo's architecture is a Pydantic AI backend agent that emits A2UI-format JSON (component id, name, children for layout, and props for data), streamed to the front end over the AG-UI protocol for real-time backend/frontend sync (a progress percentage updates live as the agent classifies the doc and selects components), with CopilotKit rendering the chosen components as React. The key idea is a contract on both sides: the system prompt describes the available components, when to use them, and the A2UI output format, while the front end maps each component name to concrete JSX and props. Cole notes the stack is Gen-UI-agnostic and swappable, and that the system can be evolved just by adjusting the agent's prompt, the same principle he teaches for agentic coding.

## Concepts covered

- [Generative UI](../concepts/generative-ui.md)
- [Memory Systems](../concepts/memory-systems.md)
- [Contract-First Development](../concepts/contract-first.md)
- [System Evolution](../concepts/system-evolution.md)

## Entities

- [Cole Medin](../entities/people/cole-medin.md)
- [Pydantic AI](../entities/tools/pydantic-ai.md)
- [A2UI](../entities/tools/a2ui.md)
- [AG-UI](../entities/tools/ag-ui.md)
- [CopilotKit](../entities/tools/copilotkit.md)
- [Google](../entities/organizations/google.md)
- [OpenClaw](../entities/tools/openclaw.md)
- [React](../entities/tools/react.md)

## Key moments

- **[0:00:00]** Demo: a fully personalized dashboard generated on the fly, nothing preconfigured
- **[0:00:16]** Defines generative UI and predicts personalized interfaces are the direction of software
- **[0:02:00]** Overview of the tech stack: Pydantic AI agent + A2UI + AG-UI + CopilotKit
- **[0:04:57]** Introduces the spectrum: static, declarative, and open-ended generative UI
- **[0:06:32]** Argues for declarative UI (component library the agent picks from) as the sweet spot
- **[0:08:16]** Walks the use case live: paste OpenClaw research markdown, agent classifies then selects components
- **[0:09:59]** Agent emits A2UI JSON (id, name, children, props); AG-UI streams events for real-time sync
- **[0:12:00]** Shows the contract: system prompt lists components + A2UI spec; front end maps names to JSX

## Transcript

[Raw transcript](../raw/ai-agents-can-now-build-their-own-ui-in-real-time-personalized-to-you.md)

