---
type: entity
subtype: person
title: "Cole Medin"
description: "AI engineer and educator whose YouTube channel and Dynamous community teach agentic coding; creator of Archon and the source of this entire knowledge base."
resource: "https://www.youtube.com/@ColeMedin"
tags: [ai-engineer, educator, agentic-coding, archon, dynamous]
videos: [the-best-ai-coding-setup-isnt-the-most-autonomous-one-heres-why, full-guide-to-becoming-a-principled-agentic-engineer-build-anything-with-ai, ive-used-claude-code-for-2000-hours-heres-how-i-build-anything-with-it, stripes-coding-agents-ship-1300-prs-every-week-heres-how-they-do-it, is-software-engineering-finally-dead, harness-engineering-what-separates-top-agentic-engineers-right-now, i-built-self-evolving-claude-code-memory-w-karpathys-llm-knowledge-bases, full-guide-build-your-own-ai-second-brain-with-claude-code, my-complete-agentic-coding-workflow-to-build-anything-no-fluff-or-overengineering, the-next-evolution-of-ai-coding-is-harnesses-heres-how-to-build-them, im-building-an-ai-dark-factory-that-ships-its-own-code-public-experiment, learn-90-of-building-ai-agents-in-30-minutes, how-id-learn-ai-agents-fast-if-i-had-to-start-over-full-roadmap, the-only-ai-tech-stack-you-need-in-2026, ai-youtube-is-only-claude-hype-now]
created: 2026-07-21
updated: 2026-07-21
---

# Cole Medin

Cole Medin is the AI engineer and educator behind [the YouTube channel](https://www.youtube.com/@ColeMedin) this entire knowledge base is mined from, and the creator of [Archon](../tools/archon.md). His arc is the through-line of the catalog: a former traditional software engineer who now builds almost entirely through coding agents. As he puts it, "I myself haven't written a single line of code for over a year now, which is crazy to think because I've spent years and years of my life writing code every single day" ([0:04:07]). He has been building AI agents since 2022 and, by his own count, has logged over 2,000 hours in [Claude Code](../tools/claude-code.md) alone.

His central teaching is a repeatable process he returns to constantly: "This is what I call the PIV loop" ([0:14:35]), the plan-implement-validate mental model that anchors [Planning with AI](../../concepts/planning-with-ai.md) and keeps a [Human in the Loop](../../concepts/human-in-the-loop.md) on every build. Around that loop he stacks the disciplines this catalog is organized by, [Context Engineering](../../concepts/context-engineering.md), [Model Selection](../../concepts/model-selection.md), [Memory Systems](../../concepts/memory-systems.md), and [RAG](../../concepts/rag.md), and a strong bias toward [Provider Independence](../../concepts/provider-independence.md) over any single vendor.

Cole is also a builder in public. He created his own [Second Brain](../../concepts/second-brain.md) on top of [Andrej Karpathy](./andrej-karpathy.md)'s LLM-wiki idea, ran the [Dark Factory](../../concepts/dark-factory.md) experiment, and packaged his workflow into [Archon](../tools/archon.md) and harnesses he open-sources. Much of his deeper teaching lives in [Dynamous](../organizations/dynamous.md), his community and agentic-coding course, and he increasingly frames his content around real engineering over news: "showing you the real systems and real engineering principles of AI coding, not just the news" ([0:00:31]).

## Works with

- [Archon](../tools/archon.md) - Cole's free, open-source AI command center and harness builder for AI coding; started as an AI agent that builds other AI agents.
- [Claude Code](../tools/claude-code.md) - Anthropic's terminal-based agentic coding assistant that is the subject of this complete-guide walkthrough.
- [Pydantic AI](../tools/pydantic-ai.md) - Cole's framework for the individual agents, structured around three parts: dependencies, the agent definition, and tools.

## Related

- [Planning with AI](../../concepts/planning-with-ai.md) - Using the AI to produce a detailed plan before implementation so execution follows a reviewed blueprint instead of improvising.
- [Human in the Loop](../../concepts/human-in-the-loop.md) - Keeping a human as the approver and steerer of agentic work rather than fully automating, so AI augments engineers instead of replacing them.
- [Context Engineering](../../concepts/context-engineering.md) - The deliberate practice of curating exactly what goes into an LLM's limited context window - system messages, schemas, chat history, and dynamic variables - to avoid overload and keep outputs sharp.
- [Model Selection](../../concepts/model-selection.md) - Choosing the right LLM per task by trading off quality, speed, and cost, often routing easy requests to cheap models and hard ones to expensive models.
- [RAG](../../concepts/rag.md) - Grounding an LLM's answers by retrieving relevant documents from an external knowledge base and injecting them into the prompt at query time.
- [Memory Systems](../../concepts/memory-systems.md) - Giving agents durable short- and long-term memory so conversations, user context, and facts persist across sessions and users.
- [Provider Independence](../../concepts/provider-independence.md) - Architecting agents so the underlying model, framework, or client can be swapped without a rewrite, avoiding lock-in through low-level abstractions.
- [Second Brain](../../concepts/second-brain.md) - A personal, always-on AI system that captures, recalls, and acts on your knowledge and daily context.
- [Dark Factory](../../concepts/dark-factory.md) - A self-evolving codebase where autonomous workflows build and improve a product with minimal human touch.
- [The Evolving Role of the Software Engineer](../../concepts/evolving-role-of-the-engineer.md) - The argument that software engineering is not dying but shifting: as agents absorb the typing, the human owns requirements, architecture, orchestration, and review.
- [Andrej Karpathy](./andrej-karpathy.md) - AI engineer who coined 'vibe coding' in February 2025 and popularized the LLM-built personal knowledge base (the 'Karpathy LLM Wiki').
- [Andrew Ng](./andrew-ng.md) - AI educator behind the Coursera 'AI for Everyone' course and the machine learning, deep learning, and NLP specializations Cole recommends for AI fundamentals.
- [Dynamous](../organizations/dynamous.md) - Cole's community for early AI adopters, home of the Agentic Coding course, weekly workshops, and the shared Context Engineering Hub.
- [oTTomator](../organizations/ottomator.md) - Cole's earlier open-source AI community (ottomator.ai), pitched as a one-stop shop for AI tools, networking, and knowledge; home of the Live Agent Studio.

## Sources

- [The Best AI Coding Setup Isn't the Most Autonomous One (Here's Why)](../../sources/the-best-ai-coding-setup-isnt-the-most-autonomous-one-heres-why.md) - "[0:04:07] I myself haven't written a single line of code for over a year now, which is crazy to think because I've spent years and years of my life writing code every single day."
- [Stripe's Coding Agents Ship 1,300 PRs EVERY Week - Here's How They Do It](../../sources/stripes-coding-agents-ship-1300-prs-every-week-heres-how-they-do-it.md) - "[0:14:35] This is what I call the PIV loop. I've covered this a lot on my channel before."
- [Is Software Engineering Finally Dead?](../../sources/is-software-engineering-finally-dead.md) - "[0:05:51] I went from being that engineer that refused to use AI coding tools to now teaching thousands of individuals and teams at large companies how to use them effectively."
- [I've Used Claude Code for 2,000+ Hours - Here's How I Build Anything With It](../../sources/ive-used-claude-code-for-2000-hours-heres-how-i-build-anything-with-it.md) - "[0:00:30] I've bundled everything up together into what I call the Whisk framework. And here's the thing, these strategies are legit."
- [How I'd Learn AI Agents FAST if I Had to Start Over (Full Roadmap)](../../sources/how-id-learn-ai-agents-fast-if-i-had-to-start-over-full-roadmap.md) - "[0:00:00] I've been building AI agents since 2022 and in the grand scheme of things that's not a lot of time, but for AI agents, it certainly is."
- [FULL Guide to Becoming a Principled Agentic Engineer (Build Anything with AI)](../../sources/full-guide-to-becoming-a-principled-agentic-engineer-build-anything-with-ai.md) - "[0:00:35] So I boil things down into the core principles for AI coding here in three phases."
- [I Built Self-Evolving Claude Code Memory w/ Karpathy's LLM Knowledge Bases](../../sources/i-built-self-evolving-claude-code-memory-w-karpathys-llm-knowledge-bases.md) - "[0:00:17] I built my own memory system on top of this. I think you're really going to like it's simple, but super effective."
- [Full Guide - Build Your Own AI Second Brain with Claude Code](../../sources/full-guide-build-your-own-ai-second-brain-with-claude-code.md) - "[0:00:00] I've been building my second brain with Claude code for the last 3 months and it's gotten to the point where it saves me at least a dozen hours of work."
- [I'm Building an AI Dark Factory That Ships Its Own Code (Public Experiment)](../../sources/im-building-an-ai-dark-factory-that-ships-its-own-code-public-experiment.md) - "[0:00:36] Join me as I push the limits of what is possible with AI. Literally, ever since I started my channel in 2024, I've had this line."
- [The Next Evolution of AI Coding Is Harnesses - Here's How to Build Them](../../sources/the-next-evolution-of-ai-coding-is-harnesses-heres-how-to-build-them.md) - "[0:00:57] in this video, I want to talk about what makes Archon so powerful. I want to show you how to get started with it."
- [Harness Engineering: What Separates Top Agentic Engineers Right Now](../../sources/harness-engineering-what-separates-top-agentic-engineers-right-now.md) - "[0:06:13] And by the way, I call this system evolution. It's very in line with something that I've been focusing on a lot recently."
- [My COMPLETE Agentic Coding Workflow to Build Anything (No Fluff or Overengineering)](../../sources/my-complete-agentic-coding-workflow-to-build-anything-no-fluff-or-overengineering.md) - "[0:00:30] This is my dead simple framework that I use every single time I'm starting a new project with my coding agent."
- [Learn 90% of Building AI Agents in 30 Minutes](../../sources/learn-90-of-building-ai-agents-in-30-minutes.md) - "[0:00:00] Not only have I built hundreds of AI agents myself, I've seen other people build thousands for every use case under the sun."
- [The ONLY AI Tech Stack You Need in 2026](../../sources/the-only-ai-tech-stack-you-need-in-2026.md) - "[0:00:00] what I have never done before is created a single video going over my entire tech stack and why I use the tools that I use."
- [AI YouTube Is Only Claude Hype Now](../../sources/ai-youtube-is-only-claude-hype-now.md) - "[0:00:31] I want to do a lot more live streaming now, showing you the real systems and real engineering principles of AI coding, not just the news."
