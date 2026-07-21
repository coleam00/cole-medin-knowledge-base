---
type: source
title: "Build a RAG AI Agent with REAL-TIME Source Validation (CopilotKit + Pydantic AI)"
description: "A RAG agent becomes far more reliable when you put a human in the loop for source validation, letting users approve or reject retrieved chunks in real time before the agent synthesizes an answer, made simple by CopilotKit + Pydantic AI wired together through the AG-UI protocol and the useAgent hook."
youtube_id: Be2OQ3LQZcQ
url: https://www.youtube.com/watch?v=Be2OQ3LQZcQ
slug: build-a-rag-ai-agent-with-real-time-source-validation-copilotkit-pydantic-ai
published: 2025-12-21
duration: "0:17:04"
recency_rank: 47
raw: "../raw/build-a-rag-ai-agent-with-real-time-source-validation-copilotkit-pydantic-ai.md"
tags: [rag, human-in-the-loop, copilotkit, pydantic-ai, ag-ui]
created: 2026-07-21
updated: 2026-07-21
---

Cole builds a RAG agent that solves the transparency problem in most RAG systems: you never actually know which sources the agent used, and citations are not proof because agents can fabricate them. His solution is human-in-the-loop source validation. When a user asks a question, the agent's search tool returns the retrieved chunks to the front end (via a state snapshot event) instead of answering immediately. The user sees every chunk, can inspect it, and approves or rejects each one. Only the approved chunks feed the final synthesis, giving full control and visibility. He frames this as both an end-user feature and a "RAG agent harness" for debugging and evolving RAG pipelines.

The stack is CopilotKit for the front end and Pydantic AI for the backend agent, connected by the AG-UI protocol, which CopilotKit's team built to link any front end to any agent framework (LangGraph, CrewAI, Mastra, Agno, and Pydantic AI all support it). The star of the show is CopilotKit's newly released useAgent hook (from their v1 release), which gives React components direct access to a backend-hosted agent: read and set its state, watch whether it is running, manage conversation history, and subscribe to events, all without hand-writing dozens of API endpoints.

The key architectural idea is that the shared state is a contract between front end and back end: the TypeScript types on the front end exactly mirror the Python types in the backend, so AG-UI can sync them seamlessly. That state is injected as Pydantic AI runtime dependencies. One tool searches the knowledge base and emits the chunks for approval; a second tool reads the approved chunk IDs back out of state and synthesizes the answer from only those. Making a Pydantic AI agent AG-UI-compatible is a single function call that produces a mountable FastAPI app. Cole closes by noting CopilotKit's 1.5 support for Google's A2UI generative-UI spec, which lets agents generate front-end components dynamically.

## Concepts covered

- [Human in the Loop](../concepts/human-in-the-loop.md)
- [Retrieval-Augmented Generation (RAG)](../concepts/rag.md)
- [Agentic Experiences](../concepts/agentic-experiences.md)
- [Generative UI](../concepts/generative-ui.md)
- [Claude Code Hooks](../concepts/claude-code-hooks.md)
- [Contract-First Development](../concepts/contract-first.md)
- [AI Coding Harness](../concepts/ai-coding-harness.md)
- [Hybrid Search](../concepts/hybrid-search.md)
- [Validation](../concepts/validation.md)

## Entities

- [CopilotKit](../entities/tools/copilotkit.md)
- [Pydantic AI](../entities/tools/pydantic-ai.md)
- [AG-UI](../entities/tools/ag-ui.md)
- [FastAPI](../entities/tools/fastapi.md)
- [React](../entities/tools/react.md)
- [A2UI](../entities/tools/a2ui.md)
- [OpenAI](../entities/organizations/openai.md)
- [Anthropic](../entities/organizations/anthropic.md)
- [Cole Medin](../entities/people/cole-medin.md)

## Key moments

- **[0:00:00]** The core problem: RAG systems hide which sources the agent used, and citations can be hallucinated too
- **[0:00:57]** Live demo: chunks appear on the left, user checks the boxes for sources to include before the agent answers
- **[0:02:14]** Use case framing: treating the app as a RAG agent harness to test and debug any RAG agent's retrieval
- **[0:02:39]** Introduces the two core components: CopilotKit (front end) + Pydantic AI (backend agent)
- **[0:03:35]** AG-UI is the protocol connecting any app to any agent; supported by LangGraph, CrewAI, Mastra, Agno, Pydantic AI
- **[0:04:02]** The useAgent hook is the star: direct access to a securely-backend-hosted agent from React
- **[0:08:02]** Excalidraw walkthrough of the full flow: search tool emits state snapshot, front end approves, synthesize tool reads approved IDs
- **[0:10:44]** State as a contract: identical types defined in Python backend and TS front end
- **[0:12:56]** Making a Pydantic AI agent AG-UI compatible is a single function call producing a mountable app
- **[0:15:58]** CopilotKit 1.5 adds support for Google's A2UI generative-UI spec

## Transcript

[Raw transcript](../raw/build-a-rag-ai-agent-with-real-time-source-validation-copilotkit-pydantic-ai.md)
