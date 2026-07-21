---
type: source
title: "Omnigent: The New Meta-Harness for EVERY Coding Agent - Claude Code, Codex, Pi, More"
description: "Omnigent is an open-source meta-harness from Databricks that orchestrates multiple AI coding agents (Claude Code, Codex, Pi) from a single layer, making it trivial to run mixed-model workflows like Claude-implements/Codex-reviews."
youtube_id: oGE_Dwz-rMk
url: https://www.youtube.com/watch?v=oGE_Dwz-rMk
slug: omnigent-the-new-meta-harness-for-every-coding-agent-claude-code-codex-pi-more
published: 2026-06-15
duration: "0:14:51"
recency_rank: 9
raw: "../raw/omnigent-the-new-meta-harness-for-every-coding-agent-claude-code-codex-pi-more.md"
tags: [meta-harness, provider-independence, archon]
created: 2026-07-21
updated: 2026-07-21
---

Cole introduces Omnigent, an open-source "meta-harness" released by Databricks that sits above individual AI coding assistants and orchestrates them together. The core argument is that top engineers no longer rely on a single model or harness: they mix assistants to lean on each tool's strengths and to isolate context across separate sessions for token optimization. Because the LLMs themselves can't be relied on to keep getting better (he cites the recent Fable 5 ban), reliability must come from the harness and, increasingly, the layer above it that coordinates many harnesses.

Omnigent packages the customizable "AI layer" (system prompts, skills, MCP servers, policies, guardrails, sandboxing) once at the server level so it applies to any connected coding agent, accessible via native app, REST API, terminal, or web UI. It ships with example orchestrators Poly (delegates implementation to Claude Code and review to Codex) and Debbie (pits two agents against each other to debate a question and synthesizes a conclusion). Every orchestrator is built from three primitives: configuration (executor, system prompt, sandboxing, guardrails, tools), skills (repeatable workflows), and the agents it can delegate to. Setup is a single command or handing the repo to your coding assistant, and it reuses the CLI credentials you're already signed into.

Cole demonstrates building a custom guarded agent whose Python-defined policy requires human approval before any force git push, showing Omnigent's human-in-the-loop guardrails apply regardless of which agent is running. He also highlights session sharing and cross-device collaboration (phone plus desktop on the same network or hosted over the internet). His takeaway: meta-harnesses are the next big thing in AI coding, and you don't want to be locked to one model or provider for an entire workflow.

## Concepts covered

- [AI Coding Harness](../concepts/ai-coding-harness.md)
- [Provider Independence](../concepts/provider-independence.md)
- [Separate Reviewer](../concepts/separate-reviewer.md)
- [Model Selection](../concepts/model-selection.md)
- [Context Isolation](../concepts/context-isolation.md)
- [The AI Layer](../concepts/the-ai-layer.md)
- [Adversarial Agents](../concepts/adversarial-agents.md)
- [Human in the Loop](../concepts/human-in-the-loop.md)
- [Agentic Workflow Engineering](../concepts/agentic-workflow-engineering.md)
- [Skills](../concepts/skills.md)
- [Parallel Agentic Coding](../concepts/parallel-agentic-coding.md)

## Entities

- [Claude Code](../entities/tools/claude-code.md)
- [Codex](../entities/tools/codex.md)
- [Pi](../entities/tools/pi-coding-agent.md)
- [Archon](../entities/tools/archon.md)
- [Git Worktrees](../entities/tools/git-worktree.md)
- [Docker](../entities/tools/docker.md)
- [Cole Medin](../entities/people/cole-medin.md)

## Key moments

- **[0:00:00]** Introduces Omnigent as a new free open-source meta-harness released over the weekend
- **[0:01:19]** Why meta-harnesses matter: the harness matters as much as the model, reinforced by the Fable 5 ban
- **[0:02:10]** Defines the meta-harness as the layer above that orchestrates many coding assistants
- **[0:03:52]** Omnigent is open source from Databricks, driven by their CTO, used internally (dogfooding)
- **[0:04:42]** The customizable AI layer lives in the server and applies to any coding assistant; multiple access surfaces (app, REST, terminal, web UI)
- **[0:05:52]** Walks the Poly orchestrator: delegate implementation to Claude Code, review to Codex
- **[0:06:56]** Argues for doing code review in a separate agent session from implementation to avoid bias
- **[0:08:13]** Three primitives of an orchestrator: configuration, skills, and agents it can call upon
- **[0:10:02]** Builds a custom guarded agent with a Python policy requiring approval before force git push
- **[0:11:58]** Debbie orchestrator pits Claude vs GPT to debate a topic and synthesizes a conclusion
- **[0:13:03]** Collaboration: same session across phone and computer, local network or hosted over the internet

## Transcript

[Raw transcript](../raw/omnigent-the-new-meta-harness-for-every-coding-agent-claude-code-codex-pi-more.md)
