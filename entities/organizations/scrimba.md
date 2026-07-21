---
type: entity
subtype: organization
title: "Scrimba"
description: "Interactive coding-education platform where tutorials become pair-programming sessions you can edit in real time; a recurring sponsor of Cole's videos."
resource: "https://scrimba.com"
tags: [education, sponsor, interactive-learning]
videos: [why-the-best-ai-coding-tools-abandoned-rag-and-what-they-use-instead, coding-agent-reliability-explodes-when-they-argue-new-adversarial-dev-technique, build-any-ai-agent-with-this-context-engineering-blueprint]
created: 2026-07-21
updated: 2026-07-21
---

# Scrimba

Scrimba (scrimba.com) is an interactive coding-education platform and a recurring sponsor of Cole's videos. What sets it apart, and what Cole highlights in every read, is that its lessons are not passive video: "a platform that turns coding tutorials into pair programming sessions where you can literally edit the instructor's code in real time" ([0:08:57]). He frames it as "a coding education platform that works completely differently from anything else out there" ([0:06:21]).

In Cole's coverage, Scrimba shows up specifically for its **AI Engineering path**, which he calls out as the relevant track and praises as dense with hands-on work: "not their AI engineering path. And it is very valuepacked" ([0:06:46]). He notes the pedigree behind it, "they built it in partnership with [Hugging Face](./hugging-face.md) and [Langchain](../tools/langchain.md), and you get to build things the entire time you're going through the course" ([0:07:04]), which lines up with his own [Learn by Building](../../concepts/learn-by-building.md) bias and his emphasis on real practice over lecture.

Because the sponsored videos span both AI-coding-workflow and retrieval topics, Scrimba appears alongside a range of the catalog's concepts, from [Planning with AI](../../concepts/planning-with-ai.md) and [Validation](../../concepts/validation.md) in the adversarial-agents build to the [RAG](../../concepts/rag.md) reappraisal that weighs [Traditional RAG](../../concepts/traditional-rag.md) against [when RAG is dead](../../concepts/when-rag-is-dead.md) and the [structured vs. unstructured data](../../concepts/structured-vs-unstructured-data.md) split. Its role in this knowledge base is as a sponsor and learning resource, not as a tool Cole builds with.

## Realizes

- [Learn by Building](../../concepts/learn-by-building.md) - Learning AI engineering by building real projects, forking open source, and rebuilding from docs rather than passive study.

## Works with

- [Hugging Face](./hugging-face.md) - AI platform whose blog post and AI Agents course provide the starting definition: programs where LLM outputs control the workflow to achieve a goal.
- [Langchain](../tools/langchain.md) - The framework used in prior masterclass videos to build the Asana agent; its message objects and invoke/stream methods underpin the chatbot logic.

## Related

- [Planning with AI](../../concepts/planning-with-ai.md) - Using the AI to produce a detailed plan before implementation so execution follows a reviewed blueprint instead of improvising.
- [Validation](../../concepts/validation.md) - Building explicit checks into agentic workflows so the AI verifies its own output against real success criteria before moving on.
- [RAG](../../concepts/rag.md) - Grounding an LLM's answers by retrieving relevant documents from an external knowledge base and injecting them into the prompt at query time.
- [Traditional RAG](../../concepts/traditional-rag.md) - The classic one-shot, static RAG pipeline that embeds a query, runs a single vector similarity search, and stuffs the top chunks into the prompt.
- [when RAG is dead](../../concepts/when-rag-is-dead.md) - The argument that for code, agents navigating files directly often beats indexed RAG, and when traditional retrieval still earns its place.
- [structured vs. unstructured data](../../concepts/structured-vs-unstructured-data.md) - Choosing the right representation for RAG, keeping tabular data queryable as SQL while formatting prose as markdown, rather than forcing everything through vector search.
- [Cole Medin](../people/cole-medin.md) - AI engineer and educator whose YouTube channel and Dynamous community teach agentic coding; creator of Archon and the source of this entire knowledge base.
- [Andrew Ng](../people/andrew-ng.md) - AI educator behind the Coursera 'AI for Everyone' course and the machine learning, deep learning, and NLP specializations Cole recommends for AI fundamentals.

## Sources

- [Build ANY AI Agent with this Context Engineering Blueprint](../../sources/build-any-ai-agent-with-this-context-engineering-blueprint.md) - "[0:08:57] The sponsor of today's video is Scrimba, a platform that turns coding tutorials into pair programming sessions where you can literally edit the instructor's code in real time."
- [Why the Best AI Coding Tools Abandoned RAG (And What They Use Instead)](../../sources/why-the-best-ai-coding-tools-abandoned-rag-and-what-they-use-instead.md) - "[0:06:21] The sponsor of today's video is Scrimba, a coding education platform that works completely differently from anything else out there."
- [Coding Agent Reliability EXPLODES When They Argue (New Adversarial Dev Technique)](../../sources/coding-agent-reliability-explodes-when-they-argue-new-adversarial-dev-technique.md) - "[0:07:04] they built it in partnership with Hugging Face and LangChain, and you get to build things the entire time you're going through the course."
