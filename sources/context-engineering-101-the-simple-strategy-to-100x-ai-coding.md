---
type: source
title: "Context Engineering 101 - The Simple Strategy to 100x AI Coding"
description: "Context engineering, providing extensive information, examples, and constraints to AI coding assistants up front and best structured through Rasmus's PRP framework, is what separates production-ready builds from vibe coding, demonstrated by one-shotting a non-trivial MCP server."
youtube_id: Mk87sFlUG28
url: https://www.youtube.com/watch?v=Mk87sFlUG28
slug: context-engineering-101-the-simple-strategy-to-100x-ai-coding
published: 2025-07-16
duration: "0:37:46"
recency_rank: 80
raw: "../raw/context-engineering-101-the-simple-strategy-to-100x-ai-coding.md"
tags: [context-engineering, prp, agentic-coding]
created: 2026-07-21
updated: 2026-07-21
---

# Context Engineering 101 - The Simple Strategy to 100x AI Coding

Cole argues that context engineering is the emerging discipline that finally systematizes what separates real AI-coding results from vibe coding and shallow prompt engineering. He frames context engineering as a superset of prompt engineering: instead of tweaking individual phrases, you invest time up front to give the AI all the information, examples, best practices, and constraints it needs to plausibly ship production code on the first pass. The concrete methodology he keeps returning to is the PRP framework from guest Rasmus, and Cole showcases a specialized template that applies PRP specifically to building Cloudflare/TypeScript MCP servers.

Rasmus explains that a PRP (Product Requirement Prompt) is a PRD plus curated codebase intelligence plus an agent runbook, the minimum viable packet an AI needs to ship production-ready code in one pass. The workflow has three steps: describe what you want in an initial.md, run a create/generate slash command that researches and pulls in all needed context on top of a pre-built base template, then run an execute command that builds the code with validation gates (linting, unit tests, iteration). Crucially, the human must validate the generated PRP, reading it, removing risky steps such as editing secrets, and confirming it follows the intended business logic, rather than blindly generating and executing. Rasmus also distinguishes CLAUDE.md (constant rules true forever) from the PRP (per-feature specific context) and slash commands (generic, reusable planning/execution workflows that only become specific via the plan you pass in).

The payoff is demonstrated live: using the MCP-specific PRP template, Cole builds a PRP Taskmaster MCP server with 18 working tools in essentially two shots. Rasmus notes that better models dramatically raised reliability, where Claude 3.7 could run a roughly 100-line PRP reliably, Claude 4 can run 500-line prompts reliably and even 1500-line prompts semi-reliably, and that PRP is purpose-built for existing codebases because a good scaffold gives the AI patterns to follow. Cole closes by announcing plans to build a community repository of reusable PRP templates across languages and project types.

## Concepts covered

- [Context Engineering](../concepts/context-engineering.md)
- [PRP Framework](../concepts/prp-framework.md)
- [PRD-First Development](../concepts/prd-first-development.md)
- [Vibe Coding](../concepts/vibe-coding.md)
- [Validation](../concepts/validation.md)
- [Human in the Loop](../concepts/human-in-the-loop.md)
- [Global Rules](../concepts/global-rules.md)
- [Slash Commands](../concepts/slash-commands.md)
- [Planning with AI](../concepts/planning-with-ai.md)
- [Context Reset](../concepts/context-reset.md)
- [Provider Independence](../concepts/provider-independence.md)
- [Parallel Agentic Coding](../concepts/parallel-agentic-coding.md)
- [Model Selection](../concepts/model-selection.md)
- [End-to-End Validation](../concepts/end-to-end-validation.md)

## Entities

- [Cole Medin](../entities/people/cole-medin.md)
- [Rasmus](../entities/people/rasmus.md)
- [MCP (Model Context Protocol)](../entities/tools/mcp.md)
- [Claude Code](../entities/tools/claude-code.md)
- [Postgres](../entities/tools/postgres-pgvector.md)
- [Dynamous](../entities/organizations/dynamous.md)
- [Aider](../entities/tools/aider.md)
- [Cline](../entities/tools/cline.md)
- [Lindy](../entities/tools/lindy.md)
- [Anthropic](../entities/organizations/anthropic.md)
- [Archon](../entities/tools/archon.md)

## Key moments

- **[0:00:00]** Opening: context engineering is the new big thing because it puts context up front, separating real results from vibe coding
- **[0:00:54]** Defines context engineering as a superset of prompt engineering - all info, examples, best practices, constraints up front
- **[0:01:13]** Introduces the PRP framework from Rasmus and the MCP-specific template built on Cole's Cloudflare MCP repo
- **[0:03:35]** Three-step workflow: fill initial.md, generate PRP via slash command, validate, then execute
- **[0:04:51]** Live demo of the PRP Taskmaster MCP built in two shots with 18 working tools
- **[0:07:20]** Emphasizes validating every tool and having the AI write tests
- **[0:11:36]** Rasmus defines PRP: PRD + curated codebase intelligence + agent runbook = minimum viable packet to ship on first pass
- **[0:15:08]** Rasmus walks the workflow: initial.md plan -> create command pulls context -> base template already pre-engineered
- **[0:18:00]** Read through your PRPs before executing; avoid tangled parallel worktree runs
- **[0:19:31]** CLAUDE.md vs PRP: global rules hold constants that rarely change; PRP holds per-feature context
- **[0:22:05]** Rasmus on existing codebases and model improvements: Claude 3.7 ~100-line PRP vs Claude 4 running 1500-line prompts
- **[0:29:11]** Runs /prp-mcp-create with initial.md, then generates and validates the PRP
- **[0:32:08]** Validation catch: removing a step that wanted to edit .dev.vars secrets
- **[0:33:32]** Clear context, run /prp-mcp-execute; execute implements validation gates (lint, unit tests, iterate)
- **[0:34:35]** After ~25 min the MCP server is fully implemented with green checks; verified 18 tools in Claude Desktop

## Transcript

[Raw transcript](../raw/context-engineering-101-the-simple-strategy-to-100x-ai-coding.md)

## Sources

- [Context Engineering 101 - The Simple Strategy to 100x AI Coding](./context-engineering-101-the-simple-strategy-to-100x-ai-coding.md) - "[0:11:36] Rasmus defines PRP: PRD + curated codebase intelligence + agent runbook = minimum viable packet to ship on first pass"
