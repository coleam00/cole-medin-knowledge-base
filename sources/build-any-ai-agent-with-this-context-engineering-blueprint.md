---
type: source
title: "Build ANY AI Agent with this Context Engineering Blueprint"
description: "Context engineering via the PRP framework (describe, generate a product requirements prompt, execute) gives an AI coding assistant enough robust, repeatable context to reliably build production AI agents, demonstrated with a Pydantic AI-tuned template."
youtube_id: ni8Xl0ANx0E
url: https://www.youtube.com/watch?v=ni8Xl0ANx0E
slug: build-any-ai-agent-with-this-context-engineering-blueprint
published: 2025-07-23
duration: "0:24:52"
recency_rank: 79
raw: "../raw/build-any-ai-agent-with-this-context-engineering-blueprint.md"
tags: [context-engineering, prp, pydantic-ai]
created: 2026-07-21
updated: 2026-07-21
---

# Build ANY AI Agent with this Context Engineering Blueprint

Cole argues that building AI agents with coding assistants fails not because of the LLM or the tool, but because of the context you provide. Vibe-prompting "build me a customer support agent" yields a demo that breaks on real users and data, so you need an up-front planning phase to sharpen your axe before implementation. His preferred method is Rasmus's PRP (Product Requirements Prompt) framework: a three-step loop where you fill out an initial.md describing the feature, use a slash command to expand it into a full PRP loaded with documentation, code structure, gotchas, best practices, and validation gates, then clear context and execute the PRP to build the feature.

He ships a version of the context-engineering template hyper-tuned for Pydantic AI: the global rules (CLAUDE.md), a Pydantic-specific base PRP, curated example agents, and the generate/execute slash commands all bake in Pydantic AI best practices to drastically reduce hallucination. The initial.md is structured around the three universal parts of any agent (dependencies, the agent definition and system prompt, and tools), plus sections for examples, documentation links, and considerations/gotchas where you correct recurring mistakes like mishandled environment variables. Examples, he stresses, are even more powerful for coding assistants than documentation alone.

He live-builds a research and email agent (a primary web-research agent using the Brave API with an email-drafting sub-agent) to demonstrate. He emphasizes validation: reviewing and iterating on the generated PRP before executing, trimming over-eager validation gates, and using the "what would it take to get to a 10/10 confidence score" prompt to surface follow-up questions. After executing, with a couple of off-camera iterations to fix conversation history and failing tests, the agent nearly one-shots, and he manually validates all the output code rather than blindly trusting it.

## Concepts covered

- [Context Engineering](../concepts/context-engineering.md)
- [PRD-First Development](../concepts/prd-first-development.md)
- [Planning with AI](../concepts/planning-with-ai.md)
- [Validation](../concepts/validation.md)
- [Human in the Loop](../concepts/human-in-the-loop.md)
- [Clarifying Questions](../concepts/clarifying-questions.md)
- [Context Reset](../concepts/context-reset.md)
- [Slash Commands](../concepts/slash-commands.md)
- [Global Rules](../concepts/global-rules.md)
- [Reduce Assumptions](../concepts/reduce-assumptions.md)
- [Agentic Coding](../concepts/agentic-coding.md)
- [Subagents Pattern](../concepts/subagents-pattern.md)

## Entities

- [Cole Medin](../entities/people/cole-medin.md)
- [Pydantic AI](../entities/tools/pydantic-ai.md)
- [Claude Code](../entities/tools/claude-code.md)
- [Kiro](../entities/tools/kiro.md)
- [Dynamous](../entities/organizations/dynamous.md)
- [Scrimba](../entities/organizations/scrimba.md)
- [Windsurf](../entities/tools/windsurf.md)

## Key moments

- **[0:00:00]** Intro: Cole's obsession with context engineering for reliable, repeatable context to build anything
- **[0:00:36]** Why 'build me an AI agent for customer support' fails - you get a demo that breaks on real users/data
- **[0:01:20]** The problem is the context, not the LLM; need a planning phase to plausibly one-shot
- **[0:01:40]** Introduces Rasmus' PRP framework, hyper-tuned template for Pydantic AI
- **[0:02:11]** The three-step PRP process: initial.md -> generate PRP -> execute
- **[0:04:24]** Hyper-tuned base PRP for Pydantic AI reduces hallucination; more use-case templates coming
- **[0:06:03]** Copy template to a working directory to reuse the template repeatedly
- **[0:06:49]** Slash commands work outside Claude Code - just tell the assistant to use the command as its prompt
- **[0:11:01]** The three universal parts of any agent: dependencies, agent definition, tools
- **[0:13:03]** Examples section is more powerful for coding assistants than documentation alone
- **[0:13:48]** Considerations/gotchas section to correct recurring mistakes like env-var handling
- **[0:15:52]** Generate the PRP from initial.md via slash command
- **[0:17:15]** Validate and iterate on the PRP before executing - don't trust blindly
- **[0:19:02]** Validation gates: have it write and iterate on unit tests until passing
- **[0:19:45]** Confidence score pro tip: ask 'what would it take to get to a 10/10'
- **[0:20:31]** Clear the conversation before executing the PRP to drop stale context
- **[0:22:04]** Agent nearly one-shotted; two off-camera iterations for conversation history + tests
- **[0:23:02]** Live demo: research + draft email about latest on Claude Code

## Transcript

[Raw transcript](../raw/build-any-ai-agent-with-this-context-engineering-blueprint.md)

## Sources

- [Build ANY AI Agent with this Context Engineering Blueprint](./build-any-ai-agent-with-this-context-engineering-blueprint.md) - "[0:01:20] The problem is the context, not the LLM; need a planning phase to plausibly one-shot"
