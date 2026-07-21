---
type: entity
subtype: tool
title: "AG-UI"
description: "Open protocol (by the CopilotKit team) that standardizes connecting AI agents to front ends via emitted events; ~16 event types."
resource: "https://docs.ag-ui.com"
tags: [protocol, frontend, agentic-experiences, open-source]
videos: [ai-agents-can-now-build-their-own-ui-in-real-time-personalized-to-you, build-a-rag-ai-agent-with-real-time-source-validation-copilotkit-pydantic-ai, the-future-of-ai-and-saas-is-agentic-experiences-heres-how-to-build-them, ag-ui-just-released-the-new-wave-of-ai-agent-apps]
created: 2026-07-21
updated: 2026-07-21
---

# AG-UI

AG-UI is an open protocol that standardizes how a front-end application talks to an AI agent, the mirror image of what MCP does on the tools side. Cole's one-line definition: "AGUI standardizes how front-end applications connect to AI agents. It's like MCP, but instead of connecting agents to tools, we are connecting agents to our applications in a standard way" ([0:01:31]). It was built by the [CopilotKit](./copilotkit.md) team and is "fully open source" ([0:01:53]). The mechanism is an event stream: "what we have here is a standard for events that the agent is going to emit to keep this real-time sync between our backend and our front end" ([0:10:44]), roughly sixteen event types covering messages, tool calls, state, and generative-UI updates.

For Cole, AG-UI is the piece that finally makes agents [frontend-agnostic](../../concepts/frontend-agnostic-agent.md). Because the contract lives in the protocol rather than in bespoke wiring, "pretty much any agent framework you could ever hope to use supports agui like langraph, crewi, mra, agno" ([0:03:35]), and any compliant UI can drive any compliant agent. He calls it "the secret sauce that works under the hood to connect any application to any AI agent" ([0:03:04]). In his builds it carries a [Pydantic AI](./pydantic-ai.md) backend agent to a [CopilotKit](./copilotkit.md) React front end, streaming tokens, tool activity, and validated RAG sources to the user in real time. This is the transport layer that makes [agentic experiences](../../concepts/agentic-experiences.md) and [generative UI](../../concepts/generative-ui.md) practical, and it keeps a clean [contract-first](../../concepts/contract-first.md) boundary between backend reasoning and the rendered interface, including [human-in-the-loop](../../concepts/human-in-the-loop.md) approval steps.

Cole positions AG-UI as the connective standard for a new class of apps: "that has all changed now with the introduction of AGUI. This is a protocol for connecting your agents to your front end to your users in a very standard way" ([0:00:33]). Where AG-UI defines *how events flow* between agent and UI, Google's [A2UI](./a2ui.md) defines *what components* the agent asks the front end to render, so the two compose rather than compete.

## Related

- [Frontend-Agnostic Agents](../../concepts/frontend-agnostic-agent.md) - the property AG-UI enables.
- [Generative UI](../../concepts/generative-ui.md) - agents driving the interface AG-UI streams.
- [Agentic Experiences](../../concepts/agentic-experiences.md) - the app class AG-UI unlocks.
- [Contract-First Development](../../concepts/contract-first.md) - the standardized agent/UI boundary.
- [Human in the Loop](../../concepts/human-in-the-loop.md) - approvals surfaced over the event stream.
- [Retrieval-Augmented Generation (RAG)](../../concepts/rag.md) - streaming RAG sources to the UI.
- Tools: [CopilotKit](./copilotkit.md) (built AG-UI), [A2UI](./a2ui.md), [Pydantic AI](./pydantic-ai.md), [MCP](./mcp.md).

## Sources

- [The Future of AI and SaaS is Agentic Experiences](../../sources/the-future-of-ai-and-saas-is-agentic-experiences-heres-how-to-build-them.md) - "[0:01:31] AGUI standardizes how front-end applications connect to AI agents. It's like MCP, but instead of connecting agents to tools, we are connecting agents to our applications in a standard way."
- [AI Agents Can Now Build Their Own UI in Real Time](../../sources/ai-agents-can-now-build-their-own-ui-in-real-time-personalized-to-you.md) - "[0:10:44] what we have here is a standard for events that the agent is going to emit to keep this real-time sync between our backend and our front end."
- [Build a RAG AI Agent with REAL-TIME Source Validation](../../sources/build-a-rag-ai-agent-with-real-time-source-validation-copilotkit-pydantic-ai.md) - "[0:03:04] the C-pilot kit team also built the AGUI protocol. This is the secret sauce that works under the hood to connect any application to any AI agent."
- [AG-UI Just Released](../../sources/ag-ui-just-released-the-new-wave-of-ai-agent-apps.md) - "[0:00:33] that has all changed now with the introduction of AGUI. This is a protocol for connecting your agents to your front end to your users in a very standard way."
