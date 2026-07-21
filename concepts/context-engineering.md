---
type: concept
title: "Context Engineering"
description: "The deliberate practice of curating exactly what goes into an LLM's limited context window - system messages, schemas, chat history, and dynamic variables - to avoid overload and keep outputs sharp."
tags: [context, context-window, prompt-construction, system-message, state-management, context-engineering, agentic-coding, prompting]
videos: [context-engineering-is-the-new-vibe-coding-learn-this-now, context-engineering-101-the-simple-strategy-to-100x-ai-coding, build-any-ai-agent-with-this-context-engineering-blueprint, google-just-dropped-a-masterclass-on-agentic-engineering-its-so-good, ive-used-claude-code-for-2000-hours-heres-how-i-build-anything-with-it, my-complete-agentic-coding-workflow-to-build-anything-no-fluff-or-overengineering, the-5-techniques-separating-top-agentic-engineers-right-now, full-guide-to-becoming-a-principled-agentic-engineer-build-anything-with-ai, harness-engineering-what-separates-top-agentic-engineers-right-now, anthropic-just-dropped-a-masterclass-on-building-agent-harnesses-for-large-codebases, turn-claude-code-into-your-full-engineering-team-with-subagents, is-software-engineering-finally-dead, stripes-coding-agents-ship-1300-prs-every-week-heres-how-they-do-it, learn-90-of-building-ai-agents-in-30-minutes, introducing-archon-the-revolutionary-operating-system-for-ai-coding, code-100x-faster-with-ai-heres-how-no-hype-full-process]
created: 2026-07-21
updated: 2026-07-21
---

# Context Engineering

Context engineering is the deliberate curation of everything that goes into an LLM's context window so a task becomes plausibly solvable. As Cole frames it, "It is the art of providing all the context for the task to be plausibly solvable by the LLM" and "supplying all relevant facts, rules, documents, plans, tools. So the LLM has a whole ecosystem of context. That is the paradigm shift from basic prompting and vibe coding." It is explicitly a superset of prompting: "context engineering is a superset of prompt engineering. It's a part of it, but context engineering is so much more."

The discipline rests on one premise repeated across nearly every video: context is the most precious resource. The goal is a balancing act, giving the agent everything it needs to succeed while keeping the window as lean as possible: "How do we keep our context window as lean as possible while still giving the coding agent all of the context it needs? That is the context engineering that we are doing here." Overloading backfires because models degrade under too much information (see [Context Rot](./context-rot.md)): "just because you can fit a million tokens into a large language model does not mean that you should because they get overwhelmed just like people do."

A key structural distinction is static versus dynamic context. Static context (rules, guardrails, the system prompt, see [Global Rules](./global-rules.md)) is loaded every session, guaranteed but expensive. Everything else "goes in dynamic context so it's efficient and scalable because it's information that the agent has to actually seek out." The context ecosystem for a build includes "the architecture, the tech stack, the key decisions that we made around the feature or app." Curating it well is the front-loaded investment: "if you're not curating your context correctly for the AI coding assistant, it will fall on its face."

## Builds on

- [Prompt Engineering](./prompt-engineering.md) - context engineering is its superset.
- [Vibe Coding](./vibe-coding.md) - the prior paradigm it replaces for reliable output.

## Part of

- [AI Coding Harness](./ai-coding-harness.md) - harness engineering is "a direct evolution of context engineering."

## Related

- [Global Rules](./global-rules.md) - the static-context layer loaded every run.
- [Progressive Disclosure](./progressive-disclosure.md) - loading capability descriptions up front and detail on demand.
- [Context Isolation](./context-isolation.md) and [Context Reset](./context-reset.md) - protecting the main window across and between sessions.
- [Context Rot](./context-rot.md) - the failure mode context engineering exists to prevent.
- [Planning with AI](./planning-with-ai.md) and [PRD-First Development](./prd-first-development.md) - front-loaded context production.
- [RAG](./rag.md), [MCP](./mcp.md), [Memory Systems](./memory-systems.md) - dynamic context sources.
- [Skills](./skills.md) - inject docs and capabilities without bloating the window.

## Tools

- [Archon](../entities/tools/archon.md) - supplies RAG and task management, "two of the most important components of context engineering."
- [Claude Code](../entities/tools/claude-code.md) - Cole's primary driver for these strategies.

## Sources

- [Context Engineering is the New Vibe Coding (Learn this Now)](../sources/context-engineering-is-the-new-vibe-coding-learn-this-now.md) - "[0:02:21] It is the art of providing all the context for the task to be plausibly solvable by the LLM."
- [Context Engineering 101 - The Simple Strategy to 100x AI Coding](../sources/context-engineering-101-the-simple-strategy-to-100x-ai-coding.md) - "[0:00:36] context engineering is a superset of prompt engineering. It's a part of it, but context engineering is so much more."
- [Build ANY AI Agent with this Context Engineering Blueprint](../sources/build-any-ai-agent-with-this-context-engineering-blueprint.md) - "[0:01:20] the problem here is not your AI coding assistant or LLM. It's the context that you are providing."
- [Google Just Dropped a Masterclass on Agentic Engineering (It's SO Good)](../sources/google-just-dropped-a-masterclass-on-agentic-engineering-its-so-good.md) - "[0:15:51] static context is things like your rules and core guardrails, the system prompt... but it's expensive because you're filling the context window up front."
- [I've Used Claude Code for 2,000+ Hours - Here's How I Build Anything With It](../sources/ive-used-claude-code-for-2000-hours-heres-how-i-build-anything-with-it.md) - "[0:04:31] How do we keep our context window as lean as possible while still giving the coding agent all of the context it needs? That is the context engineering that we are doing here."
- [My COMPLETE Agentic Coding Workflow to Build Anything](../sources/my-complete-agentic-coding-workflow-to-build-anything-no-fluff-or-overengineering.md) - "[0:01:58] Context is your most precious resource when working with AI coding assistants."
- [The 5 Techniques Separating Top Agentic Engineers Right Now](../sources/the-5-techniques-separating-top-agentic-engineers-right-now.md) - "[0:06:59] The goal is to protect the context window of your coding agent. That is something that a lot of people severely underestimate the importance of."
- [FULL Guide to Becoming a Principled Agentic Engineer](../sources/full-guide-to-becoming-a-principled-agentic-engineer-build-anything-with-ai.md) - "[0:47:47] just because you can fit a million tokens into a large language model does not mean that you should because they get overwhelmed just like people do."
- [Harness Engineering: What Separates Top Agentic Engineers Right Now](../sources/harness-engineering-what-separates-top-agentic-engineers-right-now.md) - "[0:01:38] This is a direct evolution of context engineering. How do we give the right ecosystem of context to our coding agent?"
- [Is Software Engineering Finally Dead?](../sources/is-software-engineering-finally-dead.md) - "[0:08:34] we're going from single inputs to get single outputs to creating this entire system of context for our AI agents."
- [Stripe's Coding Agents Ship 1,300 PRs EVERY Week](../sources/stripes-coding-agents-ship-1300-prs-every-week-heres-how-they-do-it.md) - "[0:07:29] before we even send the engineer's request to the agent, we already have a deterministic node at the start of the workflow for context curation."
- [Learn 90% of Building AI Agents in 30 Minutes](../sources/learn-90-of-building-ai-agents-in-30-minutes.md) - "[0:19:44] only giving to our agents the information it actually needs and not completely bloating our system prompts with thousands of lines of instruction."
- [Introducing Archon - The Revolutionary Operating System for AI Coding](../sources/introducing-archon-the-revolutionary-operating-system-for-ai-coding.md) - "[0:00:48] AI coding assistants almost completely lack two of the most important components of context engineering. I'm talking about rag for our knowledge and documentation and project management tools."
- [Code 100x Faster with AI, Here's How](../sources/code-100x-faster-with-ai-heres-how-no-hype-full-process.md) - "[0:02:53] the longer context you give to an LLM, the more likely it is to hallucinate."
- [Turn Claude Code into Your Full Engineering Team with Subagents](../sources/turn-claude-code-into-your-full-engineering-team-with-subagents.md) - "[0:00:18] Agents don't do that well when you start to fill their context window. It is the most precious resource when we are engineering with them."
