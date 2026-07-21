---
type: source
title: "A Complete Guide to Claude Code - Here are ALL the Best Strategies"
description: "A start-to-finish tour of Claude Code's core features (global rules, permissions, slash commands, MCP, sub-agents, hooks, GitHub CLI, YOLO dev containers, and parallel git worktrees) and how to combine them into reusable agentic coding workflows."
youtube_id: amEUIuBKwvg
url: https://www.youtube.com/watch?v=amEUIuBKwvg
slug: a-complete-guide-to-claude-code-here-are-all-the-best-strategies
published: 2025-08-06
duration: "0:50:18"
recency_rank: 77
raw: "../raw/a-complete-guide-to-claude-code-here-are-all-the-best-strategies.md"
tags: [claude-code, agentic-coding, workflows]
created: 2026-07-21
updated: 2026-07-21
---

# A Complete Guide to Claude Code - Here are ALL the Best Strategies

Cole walks through every major lever for getting the most out of Claude Code, starting with global rules in CLAUDE.md as the crafted system prompt (best set up sparingly, referencing external pattern and business docs so they are easy to share across teammates and swap between AI coding assistants). He covers permission management via settings.local.json (explicitly allowlist safe commands, never allow bash * or rm, always approve deletes) and building reusable agentic workflows as custom slash commands with $ARGUMENTS parameters, such as a primer command that catches Claude up on a fresh codebase.

He then layers in enhancements: MCP servers (highlighting Serena for semantic code search and editing, and teasing the Archon v2 knowledge-and-task backbone), context engineering with the three-step PRP framework (initial.md, generate PRP, execute PRP, with validation loops baked in), sub-agents that each carry their own context window, specialized system prompt, restricted tools, and even a model choice (demoed with Rasmus's validation-gates agent), and Claude Code hooks that fire deterministic custom commands at lifecycle points defined in JSON.

The back half shows Claude Code operating beyond the local machine: the GitHub CLI integration for end-to-end issue-to-PR workflows (a /fix-github-issue command that reads an issue, fixes it, tests, branches, and opens a PR), YOLO mode via Anthropic's dev containers so --dangerously-skip-permissions runs safely in an isolated, firewalled environment, and parallel agent execution with git worktrees, automated by prep-parallel and execute-parallel slash commands that spin up N isolated branches all implementing the same feature so you can pick the best result. Throughout, Cole stresses that nearly every artifact (rules, commands, sub-agents) is really just a prompt, so the same patterns transfer to other coding assistants.

## Concepts covered

- [Global Rules](../concepts/global-rules.md)
- [Prime Command](../concepts/prime-command.md)
- [Slash Commands](../concepts/slash-commands.md)
- [Commandify Everything](../concepts/commandify-everything.md)
- [The PIV Loop](../concepts/the-piv-loop.md)
- [Validation](../concepts/validation.md)
- [Subagents Pattern](../concepts/subagents-pattern.md)
- [Context Isolation](../concepts/context-isolation.md)
- [Claude Code Hooks](../concepts/claude-code-hooks.md)
- [Agent Security](../concepts/agent-security.md)
- [Vibe Coding](../concepts/vibe-coding.md)
- [Parallel Agentic Coding](../concepts/parallel-agentic-coding.md)
- [Provider Independence](../concepts/provider-independence.md)
- [The Issue Is the Spec](../concepts/issue-is-the-spec.md)

## Entities

- [Claude Code](../entities/tools/claude-code.md)
- [Archon](../entities/tools/archon.md)
- [MCP (Model Context Protocol)](../entities/tools/mcp.md)
- [GitHub](../entities/tools/github.md)
- [Git Worktrees](../entities/tools/git-worktree.md)
- [Pydantic AI](../entities/tools/pydantic-ai.md)
- [Anthropic](../entities/organizations/anthropic.md)
- [Dynamous](../entities/organizations/dynamous.md)
- [Cole Medin](../entities/people/cole-medin.md)

## Key moments

- **[0:04:53]** Global rules: CLAUDE.md as the crafted system prompt, /init vs hand-authoring, multi-level and reference-based rules
- **[0:09:20]** Permission management via settings.local.json; never allow bash * or rm
- **[0:11:17]** Custom slash commands as reusable agentic workflows, with a primer example and $ARGUMENTS parameters
- **[0:14:26]** MCP servers, Serena for semantic code retrieval/editing, allowlisting mcp__serena tools
- **[0:16:20]** Archon v2 teaser: MCP knowledge + task-management backbone, beta launch
- **[0:18:36]** Context engineering with the PRP framework: initial.md -> generate -> execute with validation loops
- **[0:25:50]** Sub-agents: own context window, specialized prompt, restricted tools, model selection, validation-gates demo
- **[0:30:17]** Claude Code hooks: deterministic custom commands at lifecycle events defined in JSON
- **[0:33:00]** GitHub CLI integration and a /fix-github-issue command that goes issue -> fix -> tests -> branch -> PR
- **[0:37:13]** YOLO mode with dev containers: --dangerously-skip-permissions safely in an isolated, firewalled environment
- **[0:41:16]** Parallel agent execution with git worktrees, automated via prep-parallel and execute-parallel commands

## Transcript

[Raw transcript](../raw/a-complete-guide-to-claude-code-here-are-all-the-best-strategies.md)

## Sources

- [A Complete Guide to Claude Code - Here are ALL the Best Strategies](./a-complete-guide-to-claude-code-here-are-all-the-best-strategies.md) - "[0:04:53] Global rules: CLAUDE.md as the crafted system prompt, /init vs hand-authoring, multi-level and reference-based rules"
