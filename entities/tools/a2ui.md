---
type: entity
subtype: tool
title: "A2UI"
description: "Google's generative-UI specification for how an agent defines the components (id, name, children, props) the front end renders."
tags: [protocol, generative-ui, google, frontend]
videos: [ai-agents-can-now-build-their-own-ui-in-real-time-personalized-to-you, build-a-rag-ai-agent-with-real-time-source-validation-copilotkit-pydantic-ai]
created: 2026-07-21
updated: 2026-07-21
---

# A2UI

A2UI is Google's generative-UI specification: a standard for how an agent describes the components a front end should render. Cole introduces it directly: "For our generative UI protocol, we're using A2UI from Google. This is the specification exactly how does the agent define the components that we're going to render in our front end" ([0:02:15]). The spec is component-shaped, describing each element by fields like id, name, children, and props, so the agent's output is a structured UI tree rather than free-form text. In short, "A2UI is for specifying the components and the standard there" ([0:02:34]).

A2UI matters to Cole because it makes [generative UI](../../concepts/generative-ui.md) portable. Instead of an agent hard-coding markup for one front end, it emits a component description against a shared [contract](../../concepts/contract-first.md), and any renderer that understands A2UI can turn it into a live interface. This is what lets an agent build its own UI in real time, personalized per user and per request. It arrived as first-class support in a CopilotKit release: "the other thing I want to call out for the 1.50 release is their support for A2UI. So, this is Google's generative UI spec" ([0:15:58]).

A2UI sits alongside [AG-UI](./ag-ui.md) in Cole's stack, and the division of labor is the key point. AG-UI is the event transport that keeps agent and front end in sync; A2UI is the component vocabulary the agent speaks over that channel. Together they support [agentic experiences](../../concepts/agentic-experiences.md) where the interface itself is agent-generated, including [human-in-the-loop](../../concepts/human-in-the-loop.md) moments and RAG-backed views. Cole uses A2UI with [CopilotKit](./copilotkit.md) on the front end and a Pydantic AI agent on the back end.

## Realizes

- [Generative UI](../../concepts/generative-ui.md) - interfaces the agent generates or drives at runtime, streaming tool activity and reasoning into a live, stateful UI.

## Works with

- [AG-UI](./ag-ui.md) - open protocol that standardizes connecting AI agents to front ends via emitted events; A2UI is the component vocabulary spoken over that channel.
- [CopilotKit](./copilotkit.md) - open-source front-end library for building agentic applications; ships first-class A2UI support.

## Related

- [Contract-First Development](../../concepts/contract-first.md) - define the shared interface between an agent's frontend and backend before building either side.
- [Agentic Experiences](../../concepts/agentic-experiences.md) - building apps where the agent drives a live, generative UI instead of a static chat box.
- [Human in the Loop](../../concepts/human-in-the-loop.md) - keeping a human as the approver and steerer of agentic work rather than fully automating.
- [Retrieval-Augmented Generation (RAG)](../../concepts/rag.md) - grounding an LLM's answers by retrieving documents and injecting them into the prompt at query time.
- [Claude Code Hooks](../../concepts/claude-code-hooks.md) - lifecycle hooks that run deterministic code at defined points in a Claude Code session.

## Sources

- [AI Agents Can Now Build Their Own UI in Real Time](../../sources/ai-agents-can-now-build-their-own-ui-in-real-time-personalized-to-you.md) - "[0:02:15] For our generative UI protocol, we're using A2UI from Google. This is the specification exactly how does the agent define the components that we're going to render in our front end."
- [Build a RAG AI Agent with REAL-TIME Source Validation](../../sources/build-a-rag-ai-agent-with-real-time-source-validation-copilotkit-pydantic-ai.md) - "[0:15:58] the other thing I want to call out for the 1.50 release is their support for A2UI. So, this is Google's generative UI spec."
