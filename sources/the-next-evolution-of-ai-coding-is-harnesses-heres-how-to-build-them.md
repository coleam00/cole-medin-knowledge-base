---
type: source
title: "The Next Evolution of AI Coding Is Harnesses - Here's How to Build Them"
description: "AI coding has evolved from prompt engineering to context engineering to harness engineering, and the new Archon lets anyone build custom harnesses that orchestrate coding-agent sessions into deterministic, repeatable, reusable workflows."
youtube_id: qMnClynCAmM
url: https://www.youtube.com/watch?v=qMnClynCAmM
slug: the-next-evolution-of-ai-coding-is-harnesses-heres-how-to-build-them
published: 2026-04-08
duration: "0:30:49"
recency_rank: 20
raw: "../raw/the-next-evolution-of-ai-coding-is-harnesses-heres-how-to-build-them.md"
tags: [harness-engineering, archon, workflow]
created: 2026-07-21
updated: 2026-07-21
---

# The Next Evolution of AI Coding Is Harnesses - Here's How to Build Them

Cole unveils the completely rebuilt Archon, repositioning it as the first open-source harness builder for AI coding. Where the old Archon was a tool built into coding agents (RAG, task management), the new Archon sits above coding agents like Claude Code and Codex and orchestrates them. He frames this through an evolution: prompt engineering (2022-2024, best single output) to context engineering (curating the perfect context for a single agent) to harness engineering (chaining many coding-agent sessions together). A harness is the tooling, prompting, and orchestration that elevates a single model beyond its raw capability, and Cole cites a study showing raw-model PR acceptance around 6.7 percent versus near 70 percent with a well-built harness, plus Stripe's Minion (1,300 AI-only PRs weekly) and Anthropic's leaked codebase (40 percent harness code) as proof the industry is leaning this way.

In Archon, a workflow is a set of nodes, where each node is either a prompt sent into a coding-agent session or a deterministic command (bash, context creation, validation) you do not want to leave to the agent's memory. This 'hybrid secret' - mixing deterministic enforcement with agent-driven prompts - is what makes workflows reliable. Workflows are plain YAML with a description (used like a skill's trigger so Claude knows when to invoke it), a provider, a default model, and a list of nodes with branches, decisions, loops, and human approval gates. You control per-node context injection (a skill only during validation, an MCP server only during planning), whether to continue or start a fresh session between nodes for token/context management, and which model runs each node (Haiku for classification, Sonnet by default) for cost efficiency.

The video is also a setup guide: clone the repo, open Claude Code, say 'set up Archon,' and an included skill walks you through prerequisites (Bun), registering a target project, choosing platforms (CLI, GitHub, Telegram, Slack), a separate-terminal credential wizard (so API keys never go into the coding agent), database choice (SQLite default or Postgres), and assistant/auth (Anthropic subscription via the Claude Agent SDK). Once installed you copy the Archon skill into any repo and say things like 'use Archon to fix issue number one,' or dispatch many issues in parallel as background processes, monitored via the CLI or web UI. Archon ships many default workflows (fix GitHub issue, idea-to-PR, PR review, interactive PRD with human-in-the-loop, the Ralph loop, adversarial dev harness) and even a workflow-builder workflow to author your own - demonstrated by building a workflow that incorporates the 'beads' persistent-memory idea.

## Concepts covered

- [AI Coding Harness](../concepts/ai-coding-harness.md)
- [The Evolution of AI Coding](../concepts/the-evolution-of-ai-coding.md)
- [Agentic Workflow Engineering](../concepts/agentic-workflow-engineering.md)
- [Deterministic Workflows](../concepts/deterministic-workflows.md)
- [Local & Self-Hosted AI](../concepts/local-ai.md)
- [Context Isolation](../concepts/context-isolation.md)
- [Model Selection](../concepts/model-selection.md)
- [Human in the Loop](../concepts/human-in-the-loop.md)
- [Parallel Agentic Coding](../concepts/parallel-agentic-coding.md)
- [The PIV Loop](../concepts/the-piv-loop.md)
- [Commandify Everything](../concepts/commandify-everything.md)
- [Progressive Disclosure](../concepts/progressive-disclosure.md)

## Entities

- [Archon](../entities/tools/archon.md)
- [Claude Code](../entities/tools/claude-code.md)
- [Codex](../entities/tools/codex.md)
- [Stripe](../entities/organizations/stripe.md)
- [Anthropic](../entities/organizations/anthropic.md)
- [Claude Agent SDK](../entities/tools/claude-agent-sdk.md)
- [GitHub](../entities/tools/github.md)
- [Pi](../entities/tools/pi-coding-agent.md)
- [Cole Medin](../entities/people/cole-medin.md)

## Key moments

- **[0:00:00]** Unveils the rebuilt Archon as the first open-source harness builder for AI coding
- **[0:03:06]** The evolution: prompt engineering to context engineering to harness engineering
- **[0:04:42]** Study cited: 6.7% raw PR acceptance vs ~70% with a harness; Stripe Minion and Anthropic's 40% harness codebase
- **[0:05:48]** New Archon sits above Claude Code and Codex and orchestrates them, unlike the old tool-based Archon
- **[0:07:51]** The hybrid secret: deterministic nodes for context/validation, prompt nodes for agent-driven work
- **[0:08:33]** Setup guide begins: clone repo, open Claude, say 'set up Archon'
- **[0:15:32]** Using Archon to fix a GitHub issue with a single command, monitored as a background process
- **[0:18:41]** Workflows are YAML: description, provider, default model, list of nodes with branches
- **[0:20:31]** Per-node model selection (Haiku for classification, Sonnet default) for token efficiency
- **[0:25:52]** Dispatching six GitHub-issue-fix workflows in parallel as background processes
- **[0:28:09]** Building a custom workflow using the meta workflow-builder workflow, incorporating 'beads'

## Transcript

[Raw transcript](../raw/the-next-evolution-of-ai-coding-is-harnesses-heres-how-to-build-them.md)
