---
type: source
title: "Pi Coding Agent + Archon: Build ANY AI Coding Workflow (No Claude Code Bloat)"
description: "Pi is a minimalistic, self-extending coding agent that fights coding-agent bloat by shipping a tiny foundational harness you extend yourself, and pairing it with Archon lets you build provider-mixing PIV-loop workflows for any AI coding task."
youtube_id: XSmI7OYd7iM
url: https://www.youtube.com/watch?v=XSmI7OYd7iM
slug: pi-coding-agent-archon-build-any-ai-coding-workflow-no-claude-code-bloat
published: 2026-04-20
duration: "0:17:48"
recency_rank: 18
raw: "../raw/pi-coding-agent-archon-build-any-ai-coding-workflow-no-claude-code-bloat.md"
tags: [pi, archon, harness, workflow]
created: 2026-07-21
updated: 2026-07-21
---

# Pi Coding Agent + Archon: Build ANY AI Coding Workflow (No Claude Code Bloat)

Cole introduces the Pi coding agent (by Mario Zechner) as a deliberately minimalistic, open-source alternative to increasingly bloated tools like Claude Code. He argues Claude Code deviated from its original simple, moldable philosophy: it now ships too many features and bugs, and its constantly-changing, uncontrollable system prompt means 'your context is not really your context.' Pi's answer is a minimal, unopinionated core plus a self-modifying design: for any missing feature (MCP, subagents, plan mode) you simply ask Pi to build it into itself, or install from a third-party extension marketplace with a single command. Because the codebase is small and Pi understands its own framework, extending it requires almost no context engineering. Pi is model- and provider-agnostic, working with virtually any LLM via subscription (/login) or API keys.

Cole then shows Pi as the third coding agent supported in Archon, his open-source harness builder that packages an agentic engineering process into reusable, parallel-executable workflows. He demonstrates a Plan-Implement-Validate (PIV) workflow built around Pi's 'planotator' extension, which renders a plan as a website where you leave inline comments and the agent revises automatically, keeping a human in the loop only during planning. The workflow mixes providers per node: Claude for a clarification phase, Pi (running Codex/GPT) for planotator planning, Claude again for implementation, and a final validation sweep like a PR review.

He builds the workflow simply by describing it in natural language to a coding agent using Archon's Claude Code skill, then runs it live to add a light/dark theme toggle to a demo GitHub issue-triager app: clarifying questions, planotator plan review (adding agent-browser CLI testing via inline comment), approval, then autonomous implementation and validation in a git worktree. The takeaway: start from a minimalistic foundation, add only the capabilities you need as extensions, and wrap everything in Archon workflows rather than piling features onto something already bloated.

## Concepts covered

- [AI Coding Harness](../concepts/ai-coding-harness.md)
- [The PIV Loop](../concepts/the-piv-loop.md)
- [Provider Independence](../concepts/provider-independence.md)
- [System Evolution](../concepts/system-evolution.md)
- [The Problems With MCP Servers](../concepts/mcp-problems.md)
- [Agentic Workflow Engineering](../concepts/agentic-workflow-engineering.md)
- [Human in the Loop](../concepts/human-in-the-loop.md)
- [Clarifying Questions](../concepts/clarifying-questions.md)
- [Skills](../concepts/skills.md)
- [Model Selection](../concepts/model-selection.md)
- [Context Engineering](../concepts/context-engineering.md)
- [Parallel Agentic Coding](../concepts/parallel-agentic-coding.md)

## Entities

- [Pi](../entities/tools/pi-coding-agent.md)
- [Archon](../entities/tools/archon.md)
- [Claude Code](../entities/tools/claude-code.md)
- [Codex](../entities/tools/codex.md)
- [Mario Zechner](../entities/people/mario-zechner.md)
- [OpenClaw](../entities/tools/openclaw.md)
- [Vercel Agent Browser CLI](../entities/tools/agent-browser.md)
- [Cole Medin](../entities/people/cole-medin.md)

## Key moments

- **[0:00:00]** Intro: Pi is a minimalistic open-source coding agent fighting the bloat of tools like Claude Code
- **[0:00:34]** Pi added as the third coding agent supported in Archon (after Claude and Codex)
- **[0:01:55]** Mario Zechner and his AI Engineer talk 'Building Pi in a world of slop'; why he built his own tool
- **[0:02:44]** Claude Code's bloat problem and uncontrollable, ever-changing system prompt
- **[0:04:00]** Pi's core idea: strip everything, minimal extensible core, make the agent modify itself
- **[0:04:44]** Things deliberately not built into Pi (MCP, subagents, plan mode) plus the extension marketplace
- **[0:05:16]** The planotator PIV workflow teased: inline web comments on a rendered plan
- **[0:06:05]** Installing Pi: single npm command, /login for subscriptions, /model to pick any LLM
- **[0:08:27]** Transition to using Archon and Pi together as favorite combo; harness builder recap
- **[0:09:35]** Building the planotator + Archon PIV workflow by just describing it in natural language
- **[0:11:32]** Walking through the workflow YAML: mixing providers per node (Claude clarify, Pi plan, Claude implement, validate)
- **[0:13:25]** Live demo: adding a light/dark theme toggle to the GitHub issue-triager demo app
- **[0:15:07]** Reviewing the rendered planotator plan and adding inline feedback (agent-browser CLI testing)
- **[0:16:19]** Approve -> autonomous implementation + validation in a worktree; theme toggle working

## Transcript

[Raw transcript](../raw/pi-coding-agent-archon-build-any-ai-coding-workflow-no-claude-code-bloat.md)
