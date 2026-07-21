---
type: concept
title: "AI Agent Learning Roadmap"
description: "Cole's ordered path for learning to build AI agents, from Python and LLM fundamentals through no-code prototyping, coded agents, RAG, and multi-agent architectures."
tags: [learning-path, roadmap, ai-agents, function-calling]
videos: [how-id-learn-ai-agents-fast-if-i-had-to-start-over-full-roadmap, the-only-ai-developer-roadmap-you-need-in-2024]
created: 2026-07-21
updated: 2026-07-21
---

# AI Agent Learning Roadmap

The roadmap is an ordered sequence for going from nothing to shipping agents, designed so each phase makes the next one cheap. "This developer map is meant to take you from Zero to Hero with artificial intelligence. You might be somewhere in the middle." [0:00:46] The promise is completeness rather than speed: "if you follow these 10 steps and learn AI in this way you're going to be comfortable creating any AI application you could possibly dream of" [0:00:18].

**Foundations, moved through fast.** Python basics, then how LLMs are trained and where they fail, then [prompt engineering](./prompt-engineering.md) - a few hours, not a career. Deep learning, ML theory, and NLP are explicitly optional; frontier models are strong enough that you only train your own for genuinely specialized tasks. The early trap is over-investing here.

**Build small things against the raw SDKs.** Chatbots, summarizers, idea generators written directly against the OpenAI and Anthropic SDKs, with documentation as the primary teacher instead of tutorials. Frameworks come next, not first, so you know what they are abstracting.

**Knowledge and tools.** [RAG](./rag.md) via [vector embeddings](./vector-embeddings.md) and a vector database, so a model has the context it needs, then [tool calling](./tool-use.md), which is the actual dividing line between an LLM app and an agent.

**Agents, then architecture.** "Now step number eight we get to the AI agents which is of course my favorite topic and where I spend most of my time teaching." [0:10:26] In the later restatement of the roadmap the ordering gets more opinionated: prototype in [no-code](./no-code-agents.md) tools first, pick up [AI coding assistants](./ai-coding-assistant.md), rebuild the same agent in Python, then level it up with [multi-agent architecture](./single-vs-multi-agent.md), long-term [memory](./memory-systems.md), and [guardrails](./guardrails.md). Deployment, [observability](./agent-observability.md), and [evaluation](./agent-evaluation.md) close it out, and evaluation is not a footnote: roughly 25 percent of agent work is coding and 75 percent is evaluating and improving.

Two meta-rules govern the whole path. Prioritize [capabilities over tools](./capabilities-over-tools.md), because the specific software churns every month while the architecture skills transfer. And [learn by building](./learn-by-building.md) the same agent forward through every phase rather than reading ahead. A community to learn alongside is the closing, non-technical step.

## Prerequisites

- [What Is an AI Agent](./what-is-an-ai-agent.md) - the definition the whole path is aimed at.

## Builds on

- [Capabilities Over Tools](./capabilities-over-tools.md) - the principle that sets the ordering.
- [Learn by Building](./learn-by-building.md) - the method applied at every phase.

## Related

- [Agents vs. Workflows](./agents-vs-workflows.md) - the distinction the foundation phase has to land.
- [No-Code AI Agents](./no-code-agents.md) - the fastest first prototype.
- [No-Code vs. Code](./no-code-vs-code.md) - when to graduate off the visual builder.
- [Retrieval-Augmented Generation (RAG)](./rag.md) - the knowledge phase.
- [Tool Calling](./tool-use.md) - the capability that turns an LLM into an agent.
- [Single vs. Multi-Agent Architecture](./single-vs-multi-agent.md) - the advanced-architecture phase.
- [Agent Deployment](./agent-deployment.md), [Agent Observability](./agent-observability.md), [Agent Evaluation](./agent-evaluation.md) - the production phases most learners skip.
- [AI Tech Stack](./ai-tech-stack.md) - choosing the tools you will actually build on.
- [Community-Driven Development](./community-driven-development.md) - the final, non-technical step.

## Tools

- [Python](../entities/tools/python.md) - the language the coded phases assume.
- [n8n](../entities/tools/n8n.md) - the no-code prototyping phase.
- [Pydantic AI](../entities/tools/pydantic-ai.md) - a recommended first Python agent framework.
- [LangGraph](../entities/tools/langgraph.md) - the multi-agent architecture phase.
- [LangChain](../entities/tools/langchain.md) - the framework layer in the earlier version of the roadmap.
- [Docker](../entities/tools/docker.md) - the deployment phase.
- [Langfuse](../entities/tools/langfuse.md) - the observability phase.
- [Cole Medin](../entities/people/cole-medin.md) - the roadmap's author, teaching it across both videos.
- [Perplexity](../entities/tools/perplexity.md) - AI-powered deep research search engine Cole uses daily to research new LLMs, frameworks, and AI tech.
- [Prompting Guide](../entities/tools/prompting-guide.md) - promptingguide.ai, the free resource Cole names as the single prompt-engineering guide worth studying end to end.

## Sources

- [The ONLY AI Developer Roadmap You Need in 2024](../sources/the-only-ai-developer-roadmap-you-need-in-2024.md) - "[0:00:18] if you follow these 10 steps and learn AI in this way you're going to be comfortable creating any AI application you could possibly dream of"
- [The ONLY AI Developer Roadmap You Need in 2024](../sources/the-only-ai-developer-roadmap-you-need-in-2024.md) - "[0:00:46] this developer map is meant to take you from Zero to Hero with artificial intelligence you might be somewhere in the middle"
- [The ONLY AI Developer Roadmap You Need in 2024](../sources/the-only-ai-developer-roadmap-you-need-in-2024.md) - "[0:10:26] now step number eight we get to the AI agents which is of course my favorite topic and where I spend most of my time teaching"
- [How I'd Learn AI Agents FAST if I Had to Start Over (Full Roadmap)](../sources/how-id-learn-ai-agents-fast-if-i-had-to-start-over-full-roadmap.md)
