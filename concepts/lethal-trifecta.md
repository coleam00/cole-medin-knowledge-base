---
type: concept
title: "The Lethal Trifecta"
description: "The dangerous combination of private data access, untrusted content, and external communication that enables prompt-injection exfiltration."
tags: [security, prompt-injection, exfiltration]
videos: [full-guide-build-your-own-ai-second-brain-with-claude-code]
created: 2026-07-21
updated: 2026-07-21
---

# The Lethal Trifecta

The lethal trifecta is the dangerous combination of three capabilities in one agent, "private data access, untrusted content and an exfiltration vector" [0:03:42], that together open the door to prompt-injection attacks. Any one of these is harmless in isolation. Held at once, they let an attacker plant a malicious instruction inside untrusted content the agent reads, have the agent act on it against your private data, and then ship the results out through whatever external channel the agent can reach. The term originates with Simon Willison; Cole applies it directly to personal AI systems.

The reason it matters so much for a [Second Brain](./second-brain.md) is that these systems have every leg of the trifecta by construction. As Cole puts it: "all three of these are always going to apply to our second brains. They have all three by default. It's really hard to make a useful second brain without being exposed to the lethal trifecta." [0:05:40] A useful second brain reads your private notes and email (private data), ingests web pages, messages, and documents you did not write (untrusted content), and can send messages, post, or call external APIs (the exfiltration vector). You cannot simply drop one leg without gutting the assistant's usefulness.

Because you cannot eliminate the trifecta outright, the defense is to constrain each leg deliberately rather than assume the combination is safe. That is where this concept connects to broader [Agent Security](./agent-security.md) practice: starting from a zero-trust, read-only posture and adding write and send capabilities only when scoped and necessary, so that even if untrusted content carries a hidden instruction, the agent lacks the standing permission to exfiltrate anything sensitive. The lethal trifecta names the risk; agent-security discipline is how you shrink its blast radius.

## Part of

- [Agent Security](./agent-security.md) - the lethal trifecta is the specific attack pattern that agent-security controls (permission scoping, zero-trust, secret isolation) are designed to defuse.

## Related

- [Second Brain](./second-brain.md) - the system Cole shows carrying all three legs of the trifecta by default.

## Sources

- [Full Guide - Build Your Own AI Second Brain with Claude Code](../sources/full-guide-build-your-own-ai-second-brain-with-claude-code.md) - "[0:03:42] we have private data access, untrusted content and an exfiltration vector"
- [Full Guide - Build Your Own AI Second Brain with Claude Code](../sources/full-guide-build-your-own-ai-second-brain-with-claude-code.md) - "[0:05:40] all three of these are always going to apply to our second brains. They have all three by default. It's really hard to make a useful second brain without being exposed to the lethal trifecta"
