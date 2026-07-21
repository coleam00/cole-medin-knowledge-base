---
type: concept
title: "Permission Management"
description: "Allowlisting the specific safe commands an agent may run unattended, and using an isolated firewalled container when you do skip permissions entirely."
tags: [claude-code, agentic-coding, agent-security, permissions]
videos: [a-complete-guide-to-claude-code-here-are-all-the-best-strategies]
created: 2026-07-21
updated: 2026-07-21
---

# Permission Management

Permission management is the practice of curating exactly which commands a coding agent may execute without asking, so that routine work flows uninterrupted while destructive actions still hit a human gate. The allowlist is built by exception, not by wildcard: "something that I never add to this list is I never add the rm the remove command because I always want to approve before it deletes any files" [0:10:35]. Cole is blunt about the tempting shortcut: "never just to give it bash star because this means that it can run any command without asking for your approval ... That is way too dangerous" [0:10:51].

The tension it resolves is real. Approval prompts are the main thing that breaks agent flow, and an agent stalled on a confirmation dialog is an agent not working. But blanket bypass hands an unsupervised process the ability to delete files, rewrite git history, or exfiltrate credentials. The resolution is granularity: allow `npm test`, `git status`, the project's linter and type-checker, the read-only commands the agent runs dozens of times per session, and leave everything irreversible behind a prompt. This is the same instinct as [guardrails](./guardrails.md) around a production agent, applied to the developer's own machine.

When you genuinely want zero interruptions, you change the blast radius instead of the allowlist: "if you want to have a safe environment, but also have claude never have to ask you for permission ... that's when we want to enable yolo mode with dev containers" [0:38:03]. Inside a [container](./containerization.md) with a restrictive [firewall](./firewall-configuration.md), full autonomy is acceptable because the worst case is a discarded sandbox rather than a damaged host. That is what makes [long-running agents](./long-running-agents.md), [the Ralph loop](./the-ralph-loop.md), and [parallel agentic coding](./parallel-agentic-coding.md) practical - the isolation carries the safety burden the permission prompt used to carry. Where you sit on this dial is essentially your position on [the five levels of AI coding autonomy](./five-levels-of-ai-coding-autonomy.md).

## Prerequisites

- [Agentic Coding](./agentic-coding.md) - permissions only become a question once an agent is executing commands on your behalf.

## Part of

- [Agent Security](./agent-security.md) - allowlisting is the developer-machine face of agent security.

## Contrasts with

- [Human in the Loop](./human-in-the-loop.md) - the approval prompt is human-in-the-loop by default; a curated allowlist trades review for throughput on commands proven safe.
- [Disposable Agent Sandboxes](./disposable-agent-sandboxes.md) - the alternative safety model, where isolation replaces approval entirely.

## Implemented by

- [Claude Code Hooks](./claude-code-hooks.md) - hooks intercept tool calls programmatically, enforcing policy that a static allowlist cannot express.
- [Containerization & Docker Networking](./containerization.md) - dev containers are what make full permission bypass defensible.
- [Firewall Configuration](./firewall-configuration.md) - restricting outbound network access closes the exfiltration path a fully permitted agent would otherwise have.

## Related

- [The Lethal Trifecta](./lethal-trifecta.md) - private data, untrusted content, and outbound communication together are what an over-broad allowlist enables.
- [Long-Running Agents](./long-running-agents.md), [The Ralph Loop](./the-ralph-loop.md), [Parallel Agentic Coding](./parallel-agentic-coding.md) - unattended patterns that require settling the permission question first.
- [The Five Levels of AI Coding Autonomy](./five-levels-of-ai-coding-autonomy.md) - permission posture is the practical expression of how much autonomy you have granted.
- [Guardrails](./guardrails.md) - the same containment idea applied to deployed agents.
- [Agent Authorization](./agent-authorization.md) - Letting an agent obtain scoped OAuth access to each user's own accounts, requested just in time when a tool is first needed, instead of hardcoding one set of credentials.

## Tools

- [Claude Code](../entities/tools/claude-code.md) - the allowlist, the dangerous bypass flag, and dev-container mode all live here.
- [Docker](../entities/tools/docker.md) - the isolation layer behind the safe version of skipping permissions.

## Sources

- [A Complete Guide to Claude Code - Here are ALL the Best Strategies](../sources/a-complete-guide-to-claude-code-here-are-all-the-best-strategies.md) - "[0:10:35] something that I never add to this list is I never add the rm the remove command because I always want to approve before it deletes any files"
- [A Complete Guide to Claude Code - Here are ALL the Best Strategies](../sources/a-complete-guide-to-claude-code-here-are-all-the-best-strategies.md) - "[0:10:51] never just to give it bash star because this means that it can run any command without asking for your approval ... That is way too dangerous."
- [A Complete Guide to Claude Code - Here are ALL the Best Strategies](../sources/a-complete-guide-to-claude-code-here-are-all-the-best-strategies.md) - "[0:38:03] if you want to have a safe environment, but also have claude never have to ask you for permission ... that's when we want to enable yolo mode with dev containers."
