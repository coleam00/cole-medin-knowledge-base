---
type: source
title: "Harness Engineering: What Separates Top Agentic Engineers Right Now"
description: "Harness engineering, building and continually evolving the AI layer around a coding agent, and orchestrating multiple focused agent sessions into automated workflows, is the 2026 evolution of context engineering and what separates top agentic engineers."
youtube_id: ulNsa0sD8N0
url: https://www.youtube.com/watch?v=ulNsa0sD8N0
slug: harness-engineering-what-separates-top-agentic-engineers-right-now
published: 2026-05-27
duration: "0:17:10"
recency_rank: 12
raw: "../raw/harness-engineering-what-separates-top-agentic-engineers-right-now.md"
tags: [harness-engineering, ai-layer, workflow]
created: 2026-07-21
updated: 2026-07-21
---

# Harness Engineering: What Separates Top Agentic Engineers Right Now

Cole defines harness engineering as building the wrapper around the model: an agent is the underlying LLM plus the harness that gives it context and defines its processes. There are two layers. The first is the harness inside a single coding-agent session, which is largely a direct evolution of context engineering. Every coding tool (Claude Code, Codex, Pi) is itself a company-built harness around a model, and choosing the tool is your first harness decision. Above that sits the AI layer you actually build, global rules, skills, MCP servers, codebase-search capabilities (LSP, knowledge graphs), hooks, and subagents. These roughly six components are the levers through which you inject your rules and processes.

The key reframe distinguishing harness engineering from context engineering is control and the 'skill issue' mindset: when an agent does something dumb, don't blame the model and wait for the next version, treat every mistake as an opportunity to improve your harness. Cole calls this system evolution: add the missing convention to your rules, add a hook to block a destructive command, sharpen a skill. You steer the system with feed-forward principles and feedback sensors (hooks, review agents, self-correcting skills). He recommends splitting plan, implement, and validate into separate, token-efficient coding-agent sessions that hand off markdown artifacts, the foundational PIV loop, and highlights security pre-tool-use hooks, a stop-validation hook that deterministically runs tests/lint/type-checks, and a post-edit lint.

The peak evolution is orchestrating many coding-agent sessions into an automated workflow rather than dumping a massive PRD into one session that will be overwhelmed. Each agent gets a focused task: explore, plan, implement, then multiple parallel code-review agents (security, correctness, simplicity) before opening a pull request. The Ralph loop (Jeffrey Huntley) is one example harness, a simple script that takes a large PRD, splits it into tasks, and runs coding-agent sessions one at a time in a while loop until a done indicator (done.txt) signals all spec items are complete and validated. Archon is Cole's open-source harness builder for creating custom harnesses like this.

## Concepts covered

- [AI Coding Harness](../concepts/ai-coding-harness.md)
- [The AI Layer](../concepts/the-ai-layer.md)
- [Context Engineering](../concepts/context-engineering.md)
- [System Evolution](../concepts/system-evolution.md)
- [The PIV Loop](../concepts/the-piv-loop.md)
- [Context Isolation](../concepts/context-isolation.md)
- [Claude Code Hooks](../concepts/claude-code-hooks.md)
- [Agentic Workflow Engineering](../concepts/agentic-workflow-engineering.md)
- [Code Review](../concepts/code-review.md)
- [The Ralph Loop](../concepts/the-ralph-loop.md)
- [Model Selection](../concepts/model-selection.md)

## Entities

- [Cole Medin](../entities/people/cole-medin.md)
- [Archon](../entities/tools/archon.md)
- [Claude Code](../entities/tools/claude-code.md)
- [Codex](../entities/tools/codex.md)
- [Pi](../entities/tools/pi-coding-agent.md)
- [MCP (Model Context Protocol)](../entities/tools/mcp.md)

## Key moments

- **[0:00:46]** Definition: harness engineering is building the wrapper around the model; two parts, single-session and multi-session orchestration
- **[0:01:56]** Diagram walkthrough: LLM -> tool harness (Claude Code/Codex/Pi) -> the AI layer you build
- **[0:02:46]** The six AI-layer components: global rules, skills, MCP servers, codebase search (LSP/knowledge graphs), hooks, subagents
- **[0:04:32]** The elephant in the room: isn't this just context engineering? Two distinctions follow
- **[0:05:26]** Skill-issue reframe / system evolution: every mistake becomes a rule to improve the harness
- **[0:07:33]** Google Cloud agent CLI sponsor segment, skills to build/deploy/monitor agents
- **[0:10:14]** AI layer foundation: rules, skills as plan/implement/validate workflows outputting handoff artifacts
- **[0:11:15]** Hooks: pre-tool-use security, stop-validation running tests/lint/type-check, post-edit lint
- **[0:12:43]** Peak evolution: orchestrating many focused coding-agent sessions instead of one overwhelmed session
- **[0:14:27]** The Ralph loop (Jeffrey Huntley), automated script splits a PRD into tasks, loops until done.txt
- **[0:16:35]** Archon as an open-source harness builder for custom workflows

## Transcript

[Raw transcript](../raw/harness-engineering-what-separates-top-agentic-engineers-right-now.md)
