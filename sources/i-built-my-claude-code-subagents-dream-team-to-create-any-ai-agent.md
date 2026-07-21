---
type: source
title: "I Built My Claude Code Subagents DREAM TEAM to Create Any AI Agent"
description: "Claude Code subagents plus Archon can be composed into a reusable agent factory where a primary agent plans, splits, and validates work across specialized subagents that communicate through markdown files."
youtube_id: HJ9VvIG3Rps
url: https://www.youtube.com/watch?v=HJ9VvIG3Rps
slug: i-built-my-claude-code-subagents-dream-team-to-create-any-ai-agent
published: 2025-08-27
duration: "0:26:36"
recency_rank: 73
raw: "../raw/i-built-my-claude-code-subagents-dream-team-to-create-any-ai-agent.md"
tags: [subagents, agentic-coding, archon]
created: 2026-07-21
updated: 2026-07-21
---

# I Built My Claude Code Subagents DREAM TEAM to Create Any AI Agent

Cole walks through an open-source subagent agent factory template that turns a single high-level request into a fully built Pydantic AI agent. A primary Claude Code agent (not itself a subagent) gathers requirements via clarifying questions, sets up tasks in Archon distributed across specialized subagents, then runs an orchestrated workflow: a Pydantic AI planner produces an initial.md plan, three parallel subagents plan the system prompt, tools, and dependencies, the primary agent does the actual implementation, and a validator subagent writes and iterates on unit tests before delivering the final agent. The whole workflow is defined in global rules (CLAUDE.md), which could equivalently be packaged as a slash command.

The core technique is context isolation. Subagents each have their own context window and do not share conversation history with the primary agent, so they communicate exclusively through markdown files (initial.md, prompts.md, and so on) placed in a per-build planning folder. This keeps web research and Archon MCP knowledge lookups from polluting the primary conversation, which avoids early auto-compaction and hallucination. Subagents also allow per-agent model selection (Opus, Sonnet, Haiku) to save tokens, fine-tuned system prompts, scoped tool permissions, and reusability across builds.

Cole shows two ways to author subagents: the interactive /agents command, where Claude generates the markdown and you hand-iterate to tighten it, or feeding the Claude Code subagent docs into an Archon knowledge base so Claude can generate all subagents and the CLAUDE.md orchestration at once. He demonstrates a live end-to-end build of a hybrid-search RAG agent, noting that the planner is where you could integrate a heavier context-engineering strategy like PRP or BMAD, and that the whole pattern generalizes beyond AI agents to any software, such as splitting a frontend into components, CSS, and dependencies.

## Concepts covered

- [Subagents Pattern](../concepts/subagents-pattern.md)
- [Context Isolation](../concepts/context-isolation.md)
- [Context Engineering](../concepts/context-engineering.md)
- [Agentic Workflow Engineering](../concepts/agentic-workflow-engineering.md)
- [Parallel Agentic Coding](../concepts/parallel-agentic-coding.md)
- [Global Rules](../concepts/global-rules.md)
- [Slash Commands](../concepts/slash-commands.md)
- [Model Selection](../concepts/model-selection.md)
- [Clarifying Questions](../concepts/clarifying-questions.md)
- [Validation](../concepts/validation.md)
- [Planning with AI](../concepts/planning-with-ai.md)
- [Knowledge Bases](../concepts/knowledge-bases.md)
- [Git as Long-Term Memory](../concepts/git-as-long-term-memory.md)

## Entities

- [Claude Code](../entities/tools/claude-code.md)
- [Archon](../entities/tools/archon.md)
- [Pydantic AI](../entities/tools/pydantic-ai.md)
- [MCP (Model Context Protocol)](../entities/tools/mcp.md)
- [GitHub](../entities/tools/github.md)
- [Anthropic](../entities/organizations/anthropic.md)
- [Lindy](../entities/tools/lindy.md)
- [Cole Medin](../entities/people/cole-medin.md)

## Key moments

- **[0:00:00]** Intro: Claude Code subagents + Archon = an AI agent factory from one high-level description
- **[0:01:01]** Walkthrough of the README workflow diagram: subagents in .claude/agents, orchestrated by CLAUDE.md global rules
- **[0:01:44]** Phase flow: primary agent asks clarifying questions, sets up Archon tasks, invokes the Pydantic AI planner
- **[0:02:49]** Three parallel subagents plan system prompt, tools, and dependencies
- **[0:03:22]** Implementation done by the primary Claude Code agent, then the validator subagent writes/iterates tests
- **[0:05:43]** Deep dive on subagent benefits: specialized expertise, reusability, flexible permissions/model, context preservation
- **[0:07:13]** Creating a subagent with the /agents command and iterating on the generated markdown
- **[0:09:58]** Second approach: add Claude Code subagent docs to Archon so Claude generates all subagents + CLAUDE.md at once
- **[0:13:10]** How markdown files (initial.md, prompts.md) pass context between subagents that share no context
- **[0:15:24]** Live demo begins: building a hybrid-search RAG agent
- **[0:21:09]** Planner subagent runs (~1 min, ~30k tokens of research), marks Archon task done
- **[0:22:10]** Three parallel agents fire simultaneously, each reads initial.md and outputs its own markdown
- **[0:24:16]** Validator runs and iterates on unit tests; final hybrid-search RAG agent delivered and demoed

## Transcript

[Raw transcript](../raw/i-built-my-claude-code-subagents-dream-team-to-create-any-ai-agent.md)

## Sources

- [I Built My Claude Code Subagents DREAM TEAM to Create Any AI Agent](./i-built-my-claude-code-subagents-dream-team-to-create-any-ai-agent.md) - "[0:13:10] How markdown files (initial.md, prompts.md) pass context between subagents that share no context"
