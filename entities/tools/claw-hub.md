---
type: entity
subtype: tool
title: "Claw Hub"
description: "OpenClaw's public skills marketplace, where research found hundreds of malicious packages stealing API keys and SSH credentials, the canonical example of untrusted third-party agent capabilities."
tags: [ai-coding, coding-agent, agent-security]
videos: [i-built-a-safer-openclaw-alternative-using-claude-code]
created: 2026-07-21
updated: 2026-07-21
---

# Claw Hub

Claw Hub is the public marketplace where anyone can publish [skills](../../concepts/skills.md) for [OpenClaw](./openclaw.md), and it is the sharpest illustration in Cole's catalog of why third-party agent capabilities are a security surface, not a convenience feature. He describes it plainly: "we also have the issue with Claw Hub. This is a marketplace that is publicly available where people are publishing skills... But research found that there are hundreds of malicious packages" [0:03:06]. Those packages were caught stealing API keys and SSH credentials.

The reason a skills registry is more dangerous than a normal package registry is what a skill *is*. A skill is instructions plus code that an agent loads on demand and then executes with the full privileges of the assistant that installed it, which for a personal assistant means your inbox, your calendar, your shell, and your stored OAuth tokens. Installing one is closer to handing over a session than to adding a dependency. Cole stacks this on top of OpenClaw's other problems (a one-click remote-code-execution path and plaintext credential storage) and then names the deeper issue: a huge, poorly-understood codebase is being handed enormous agent power.

His response is not to harden Claw Hub but to remove the registry from the architecture entirely. Rebuilding OpenClaw's four magical components himself, he keeps the skills idea and drops the marketplace: skills are built into [Claude Code](./claude-code.md) and the [Claude Agent SDK](./claude-agent-sdk.md), he has a skill whose job is creating more skills, and because nothing is pulled from a public registry the capability set stays auditable as it grows [0:12:12]. Claw Hub is therefore best read as the negative example that motivates the [learn by building](../../concepts/learn-by-building.md) approach: treat the popular project as a reference implementation, take the design, leave the trust assumptions.

## Realizes

- [Skills](../../concepts/skills.md) - Reusable, model-invoked capability packages that load specialized instructions and tools on demand to extend an agent.

## Contrasts with

- [Claude Code](./claude-code.md) - Anthropic's terminal-based agentic coding assistant, whose locally-authored built-in skills replace the public registry in Cole's rebuild.

## Works with

- [OpenClaw](./openclaw.md) - The explosively popular open-source personal AI assistant the marketplace serves, and the codebase Cole treats as a reference implementation rather than something to run.
- [Claude Agent SDK](./claude-agent-sdk.md) - The engine that powers Claude Code, exposed as a library; it supplies the skill mechanism in the safer rebuild.

## Related

- [Agent Security](../../concepts/agent-security.md) - Sandboxing agents, scoping permissions, and keeping secrets out of the model to limit blast radius and prevent abuse.
- [Permission Management](../../concepts/permission-management.md) - Allowlisting the specific safe commands an agent may run unattended, and using an isolated firewalled container when you do skip permissions entirely.
- [Disposable Agent Sandboxes](../../concepts/disposable-agent-sandboxes.md) - Running each agent in an ephemeral, preloaded cloud dev box so unattended agents run with scoped permissions.
- [Learn by Building](../../concepts/learn-by-building.md) - Learning AI engineering by building real projects, forking open source, and rebuilding from docs rather than passive study.
- [Second Brain](../../concepts/second-brain.md) - A personal, always-on AI system that captures, recalls, and acts on your knowledge and daily context.

## Sources

- [I Built a Safer OpenClaw Alternative Using Claude Code](../../sources/i-built-a-safer-openclaw-alternative-using-claude-code.md) - "[0:03:06] we also have the issue with Claw Hub. This is a marketplace that is publicly available where people are publishing skills... But research found that there are hundreds of malicious packages."
