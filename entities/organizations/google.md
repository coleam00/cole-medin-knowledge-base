---
type: entity
subtype: organization
title: "Google"
description: "Author of the A2UI generative-UI specification used in the demo."
resource: "https://google.com"
tags: [ai-lab, standards, gemini]
videos: [finally-an-open-standard-for-the-karpathy-llm-wiki-is-here, google-just-dropped-a-masterclass-on-agentic-engineering-its-so-good, ai-agents-can-now-build-their-own-ui-in-real-time-personalized-to-you, the-way-we-use-ai-will-completely-change-in-2026-hot-takes, is-gemini-3-really-the-best-ai-ever, google-anthropic-and-openais-guides-to-ai-agents-all-in-18-minutes, google-is-quietly-revolutionizing-ai-agents-this-is-huge]
created: 2026-07-21
updated: 2026-07-21
---

# Google

Google is a foundational AI lab that, across Cole's videos, matters less for winning the raw model race and more for setting the standards, protocols, and educational guides the agent ecosystem builds on. Cole frames the tension directly: "I know that Google is lagging in the AI race right now. Gemini is not as good as GPT and Claude, but they have been releasing some really good stuff on how to leverage LLMs effectively" ([0:02:54]). That "how to leverage" work is the throughline: the Open Knowledge Format, the Agent2Agent protocol, the A2UI generative-UI spec, an agent whitepaper, and a full agentic-engineering masterclass.

Google's biggest contributions in this catalog are standards and pedagogy. It "released here with their open knowledge format" ([0:02:06]), a vendor-neutral formalization of the [LLM Wiki](../../concepts/the-llm-wiki.md). It introduced "their agent to agent protocol which is a standard for agents to communicate effectively with each other" ([0:00:00]), one of the core [Agent Protocols](../../concepts/agent-protocols.md). Its whitepaper gives the cleanest definition of an agent, "an application that attempts to achieve a goal by observing the world and acting upon it" ([0:02:04]), and Cole notes "Google definitely explains this the best in my opinion" ([0:05:35]). Its masterclass pushes past prompting into the rest of the harness: "Clearly Google is like okay you need to put your focus on the rest of the harness here" ([0:07:20]), reinforcing [Context Engineering](../../concepts/context-engineering.md), [Human in the Loop](../../concepts/human-in-the-loop.md), and [Agent Evaluation](../../concepts/agent-evaluation.md). Its [Generative UI](../../concepts/generative-ui.md) push comes via A2UI, "where the agent will pick components from a library" ([0:05:12]). By late 2026 the model story turned around too: "Gemini 3 is just crushing it across the board" ([0:02:48]), paired with a generalist "jack of all trades" strategy and an Antigravity Chrome integration.

## Realizes

- [The LLM Wiki](../../concepts/the-llm-wiki.md) - An LLM-maintained knowledge base of plain markdown pages that compiles sources into a navigable, self-referential wiki.
- [Progressive Disclosure](../../concepts/progressive-disclosure.md) - Loading context, skills, and tools on demand only when a task needs them instead of front-loading everything into the context window.
- [Agent Protocols](../../concepts/agent-protocols.md) - Emerging standards (A2A, agent cards, discovery) that let agents interoperate and be called across clients.
- [Agent2Agent (A2A) Protocol](../../concepts/a2a-protocol.md) - Google's open standard for how independently-built agents discover and talk to each other over HTTP via agent cards and tasks, the agent-to-agent counterpart to MCP.
- [Generative UI](../../concepts/generative-ui.md) - Interfaces the agent generates or drives at runtime, streaming tool activity and reasoning into a live, stateful UI.

## Related

- [Context Engineering](../../concepts/context-engineering.md) - The deliberate practice of curating exactly what goes into an LLM's limited context window - system messages, schemas, chat history, and dynamic variables - to avoid overload and keep outputs sharp.
- [Human in the Loop](../../concepts/human-in-the-loop.md) - Keeping a human as the approver and steerer of agentic work rather than fully automating, so AI augments engineers instead of replacing them.
- [Agent Evaluation](../../concepts/agent-evaluation.md) - Systematically scoring agent behavior with evals and benchmarks, including as a gate before deployment.
- [The PIV Loop](../../concepts/the-piv-loop.md) - Cole's core agentic-coding cycle of Plan, Implement, Validate that structures every unit of AI-driven work.
- [Model Selection](../../concepts/model-selection.md) - Choosing the right LLM per task by trading off quality, speed, and cost, often routing easy requests to cheap models and hard ones to expensive models.
- [Anthropic](./anthropic.md) - Maker of Claude and Claude Code, creator of MCP, and Cole's pick for the best coding LLM and the lab whose research most shapes his practice.
- [OpenAI](./openai.md) - Maker of GPT-4o mini (affordable-but-strong chat model) and text-embedding-3-small (recommended RAG embedding model).
- [Meta AI](./meta.md) - Cited as an example of a model trained with ~10x fewer parameters than GPT, pointing toward faster/cheaper training.
- [Vertex AI](../tools/vertex-ai.md) - Google's cloud AI platform offering powerful agent capabilities out of the box, recommended in Google's agent white paper.

## Sources

- [Finally, an Open Standard for the Karpathy LLM Wiki is HERE](../../sources/finally-an-open-standard-for-the-karpathy-llm-wiki-is-here.md) - "[0:02:06] That is what Google has released here with their open knowledge format."
- [Google, Anthropic, and OpenAI's Guides to AI Agents ALL in 18 Minutes](../../sources/google-anthropic-and-openais-guides-to-ai-agents-all-in-18-minutes.md) - "[0:02:04] Within the Google paper, they say that an agent can be defined as an application that attempts to achieve a goal by observing the world and acting upon it."
- [Google is Quietly Revolutionizing AI Agents (This is HUGE)](../../sources/google-is-quietly-revolutionizing-ai-agents-this-is-huge.md) - "[0:00:00] Google recently introduced their agent to agent protocol which is a standard for agents to communicate effectively with each other."
- [Google Just Dropped a Masterclass on Agentic Engineering (It's SO Good)](../../sources/google-just-dropped-a-masterclass-on-agentic-engineering-its-so-good.md) - "[0:07:20] there's so much here that makes up the other 90%... Clearly Google is like okay you need to put your focus on the rest of the harness here."
- [AI Agents Can Now Build Their Own UI in Real Time (Personalized to You)](../../sources/ai-agents-can-now-build-their-own-ui-in-real-time-personalized-to-you.md) - "[0:05:12] This is what I'm the most interested in... really what's following Google's A2UI specification where the agent will pick components from a library."
- [Is Gemini 3 Really the Best AI Ever?](../../sources/is-gemini-3-really-the-best-ai-ever.md) - "[0:04:39] One of the things that we have in anti-gravity that is very cool is a Google Chrome integration."
- [The Way We Use AI Will Completely Change in 2026 (Hot Takes)](../../sources/the-way-we-use-ai-will-completely-change-in-2026-hot-takes.md) - "[0:02:48] Gemini 3 is just crushing it across the board."
