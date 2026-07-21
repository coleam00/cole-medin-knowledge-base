---
type: entity
subtype: person
title: "Rasmus"
description: "Creator of the PRP framework and a Dynamous community member; a former product manager who built PRP over a year for working on existing codebases."
tags: [prp, context-engineering, dynamous]
videos: [this-new-protocol-will-change-ai-coding-forever-acp, context-engineering-101-the-simple-strategy-to-100x-ai-coding, context-engineering-is-the-new-vibe-coding-learn-this-now]
created: 2026-07-21
updated: 2026-07-21
---

# Rasmus

Rasmus is a Dynamous community member and Cole's collaborator, best known here as the creator of the [PRP Framework](../../concepts/prp-framework.md). Cole names him as a direct inspiration for how he teaches [Context Engineering](../../concepts/context-engineering.md): "A lot of what I'm about to dive into with you here is inspired by someone in the Dynamous community, Rasmus. He did a workshop last month in our community and it was an absolute killer" ([0:07:21]), and he builds his own material on Rasmus's template: "A lot of this is based off of the PRP base template that I uh used from Rasmus" ([0:17:16]).

What gives PRP its weight is Rasmus's background and the time he put in. He is a former product manager, not a career engineer: "I've spent many years as a product manager and business analyst writing a lot of technical documentation and PRDS in particular" ([0:11:36]), and PRP is the product of long iteration: "I've been developing this for kind of over a year. It has had in that year it has many many shapes and forms" ([0:12:18]). That lineage is why the framework is strong at [PRD-First Development](../../concepts/prd-first-development.md) and [Planning with AI](../../concepts/planning-with-ai.md), and why it is aimed at real, existing codebases rather than greenfield demos. It packages up reusable structure through [Slash Commands](../../concepts/slash-commands.md) and [Global Rules](../../concepts/global-rules.md), and Cole frames it as the disciplined successor to [Vibe Coding](../../concepts/vibe-coding.md). Rasmus also contributed engineering directly: "I actually had Rasmus on my team. He did a proof of concept integrating [Archon](../tools/archon.md) with ACP" ([0:15:59]).

## Realizes

- [PRP Framework](../../concepts/prp-framework.md) - The Product Requirements Prompt pattern: a structured, context-rich prompt blueprint that hands an agent everything it needs to one-pass a feature.

## Contrasts with

- [Vibe Coding](../../concepts/vibe-coding.md) - Building software by conversationally prompting an AI without closely reading the code, useful for prototypes but risky for production.

## Related

- [Context Engineering](../../concepts/context-engineering.md) - The deliberate practice of curating exactly what goes into an LLM's limited context window - system messages, schemas, chat history, and dynamic variables - to avoid overload and keep outputs sharp.
- [PRD-First Development](../../concepts/prd-first-development.md) - Starting every build from a written product requirements document that becomes the contract the agent implements against.
- [Planning with AI](../../concepts/planning-with-ai.md) - Using the AI to produce a detailed plan before implementation so execution follows a reviewed blueprint instead of improvising.
- [Slash Commands](../../concepts/slash-commands.md) - User-defined command files that package a prompt and arguments into a callable shortcut inside the coding agent.
- [Global Rules](../../concepts/global-rules.md) - Persistent project- or user-level rule files that inject standing context and conventions into every agent run.
- [Archon](../tools/archon.md) - Cole's free, open-source AI command center and harness builder for AI coding; started as an AI agent that builds other AI agents.
- [Cole Medin](./cole-medin.md) - AI engineer and educator whose YouTube channel and Dynamous community teach agentic coding; creator of Archon and the source of this entire knowledge base.

## Sources

- [Context Engineering is the New Vibe Coding (Learn this Now)](../../sources/context-engineering-is-the-new-vibe-coding-learn-this-now.md) - "[0:07:21] A lot of what I'm about to dive into with you here is inspired by someone in the Dynamous community, Rasmus. He did a workshop last month in our community and it was an absolute killer."
- [Context Engineering 101 - The Simple Strategy to 100x AI Coding](../../sources/context-engineering-101-the-simple-strategy-to-100x-ai-coding.md) - "[0:12:18] I've been developing this for kind of over a year. It has had in that year it has many many shapes and forms."
- [This New Protocol Will Change AI Coding Forever (ACP)](../../sources/this-new-protocol-will-change-ai-coding-forever-acp.md) - "[0:15:59] I actually had Rasmus on my team. He did a proof of concept integrating Archon with ACP."
