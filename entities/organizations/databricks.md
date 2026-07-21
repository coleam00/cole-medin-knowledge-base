---
type: entity
subtype: organization
title: "Databricks"
description: "Data and AI company that open-sourced Omnigent (driven by its CTO and dogfooded internally); also the acquirer of Neon."
resource: "https://www.databricks.com"
tags: [organization, open-source, meta-harness, ai-coding]
videos: [omnigent-the-new-meta-harness-for-every-coding-agent-claude-code-codex-pi-more]
created: 2026-07-21
updated: 2026-07-21
---

# Databricks

Databricks is the data and AI company that released [Omnigent](../tools/omnigent.md), the open-source [meta-harness](../../concepts/meta-harness.md) that sits above individual coding agents and orchestrates them together. Cole's credibility case for the project is entirely about who is behind it and how it is used: "Omni agent is open source from the company data bricks... this is a project driven by their CTO. They're already using this very extensively internally" ([0:03:52]). CTO sponsorship plus real internal dogfooding is what separates it from a weekend framework release, and it is the reason he treats meta-harnesses as the next serious layer of AI coding rather than a curiosity.

What Databricks actually shipped is a portable [AI Layer](../../concepts/the-ai-layer.md). Omnigent packages system prompts, [skills](../../concepts/skills.md), MCP servers, policies, [guardrails](../../concepts/guardrails.md), and sandboxing once at the server level, then applies that configuration to whichever agent is running underneath, whether that is [Claude Code](../tools/claude-code.md), [Codex](../tools/codex.md), or [Pi](../tools/pi-coding-agent.md), reachable from a native app, REST API, terminal, or web UI. Example orchestrators show the payoff: one delegates implementation to Claude Code and review to Codex, a working [Separate Reviewer](../../concepts/separate-reviewer.md) split, and another pits two agents against each other to debate a question, an [Adversarial Agents](../../concepts/adversarial-agents.md) pattern. Cole's own demo adds a Python-defined policy requiring human approval before any force git push, showing [Human in the Loop](../../concepts/human-in-the-loop.md) enforcement that survives a change of underlying agent. That is [Provider Independence](../../concepts/provider-independence.md) at the workflow level, not just the model level.

Databricks shows up a second way in Cole's stack: it acquired [Neon](../tools/neon.md), the serverless Postgres platform he favors and the one that makes [Database Branching](../../concepts/database-branching.md) per git worktree practical. So the company sits behind both halves of a parallel agentic setup, the orchestration layer above the agents and the isolated database underneath them.

## Tools

- [Omnigent](../tools/omnigent.md) - Databricks' open-source meta-harness that orchestrates Claude Code, Codex, and Pi from one customizable AI layer.
- [Neon](../tools/neon.md) - Serverless Postgres platform Cole favors, acquired by Databricks in 2025.

## Works with

- [Claude Code](../tools/claude-code.md) - Anthropic's terminal-based agentic coding assistant, one of the executors Omnigent delegates to.
- [Codex](../tools/codex.md) - OpenAI's software-engineering agent, used as the reviewer half of the mixed-model orchestrator.
- [Pi](../tools/pi-coding-agent.md) - A minimalistic, open-source coding agent, another executor Omnigent can drive.

## Related

- [Meta-Harness](../../concepts/meta-harness.md) - A layer above individual AI coding assistants that orchestrates many of them on larger tasks.
- [The AI Layer](../../concepts/the-ai-layer.md) - The rules, commands, skills, and context you own on top of a codebase, made portable across agents.
- [Provider Independence](../../concepts/provider-independence.md) - Architecting so the model, framework, or client can be swapped without a rewrite.
- [AI Coding Harness](../../concepts/ai-coding-harness.md) - The surrounding scaffolding that turns a raw model into a reliable coding system.
- [Separate Reviewer](../../concepts/separate-reviewer.md) - Splitting authoring and grading across different agents so the reviewer is not biased.
- [Adversarial Agents](../../concepts/adversarial-agents.md) - Setting agents against each other to surface weaknesses a single agent would miss.
- [Guardrails](../../concepts/guardrails.md) - Constraints and checks that keep agents from going off the rails.
- [Skills](../../concepts/skills.md) - Reusable, model-invoked capability packages that load specialized instructions on demand.
- [Database Branching](../../concepts/database-branching.md) - Giving each git worktree its own isolated database copy so parallel agents do not collide.
- [Open-Source & Local AI Coding](../../concepts/open-source-ai-coding.md) - Community-maintained, self-hostable AI coding tools.

## Sources

- [Omnigent: The New Meta-Harness for EVERY Coding Agent - Claude Code, Codex, Pi, More](../../sources/omnigent-the-new-meta-harness-for-every-coding-agent-claude-code-codex-pi-more.md) - "[0:03:52] Omni agent is open source from the company data bricks... this is a project driven by their CTO. They're already using this very extensively internally."
