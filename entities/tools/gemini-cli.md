---
type: entity
subtype: tool
title: "Gemini CLI"
description: "Google's coding CLI, where subagent support is experimental and which has a direct integration with the Agent Client Protocol."
resource: "https://github.com/google-gemini/gemini-cli"
tags: [coding-agent, google, cli]
videos: [the-subagent-era-is-officially-here-learn-this-now, this-new-protocol-will-change-ai-coding-forever-acp]
created: 2026-07-21
updated: 2026-07-21
---

# Gemini CLI

Gemini CLI is Google's terminal-based coding agent, the Gemini-model equivalent of [Claude Code](./claude-code.md) and [Codex](./codex.md). Cole treats it as one of the mainstream agentic coding front ends, notable for two things: early subagent support and native protocol integration. On subagents it is still catching up, and Cole is candid about the maturity gap: "This is where we can use GPT 5.4 mini and then it's experimental in the Gemini CLI" ([0:05:45]), placing Gemini CLI's take on the [Subagents Pattern](../../concepts/subagents-pattern.md) firmly in the experimental column at the time of recording.

## How Cole uses it / why it matters

The larger reason Gemini CLI shows up in Cole's videos is interoperability. It is one of the first coding assistants to speak the emerging Agent Client Protocol: "for coding assistance, Gemini CLI actually has a direct integration with ACP" ([0:02:33]). That matters for [Provider Independence](../../concepts/provider-independence.md) and [Parallel Agentic Coding](../../concepts/parallel-agentic-coding.md), because a protocol-native agent can be driven from a shared editor or harness without bespoke glue. Cole also uses the Gemini CLI announcement to track Google's model releases feeding it, noting alongside the CLI that "We also have Google that just released Gemini 3.1 Flash Light built for intelligence at scale" ([0:00:30]), a [Model Selection](../../concepts/model-selection.md) signal about cheap, fast models for high-volume subagent fan-out where [Context Isolation](../../concepts/context-isolation.md) keeps each worker's window clean and staves off [Context Rot](../../concepts/context-rot.md). Like every modern agent Cole favors, Gemini CLI leans on [Agentic Search](../../concepts/agentic-search.md) over the codebase rather than pre-indexed retrieval.

## Related

- [Subagents Pattern](../../concepts/subagents-pattern.md) - Gemini CLI's subagent support, still experimental.
- [Model Selection](../../concepts/model-selection.md) - Gemini 3.1 Flash Light as a cheap, high-throughput driver.
- [Parallel Agentic Coding](../../concepts/parallel-agentic-coding.md) and [Context Isolation](../../concepts/context-isolation.md) - fanning work out across isolated agent windows.
- [Context Rot](../../concepts/context-rot.md) - the failure mode isolation is meant to avoid.
- [Agentic Search](../../concepts/agentic-search.md) - how the CLI navigates a codebase.
- Sibling agents: [Gemini](./gemini.md), [Claude Code](./claude-code.md), [Codex](./codex.md), [Git Worktrees](./git-worktree.md), [Archon](./archon.md).

## Sources

- [The Subagent Era Is Officially Here - Learn this Now](../../sources/the-subagent-era-is-officially-here-learn-this-now.md) - "[0:05:45] This is where we can use GPT 5.4 mini and then it's experimental in the Gemini CLI."
- [The Subagent Era Is Officially Here - Learn this Now](../../sources/the-subagent-era-is-officially-here-learn-this-now.md) - "[0:00:30] We also have Google that just released Gemini 3.1 Flash Light built for intelligence at scale."
- [This New Protocol Will Change AI Coding Forever (ACP)](../../sources/this-new-protocol-will-change-ai-coding-forever-acp.md) - "[0:02:33] for coding assistance, Gemini CLI actually has a direct integration with ACP."
