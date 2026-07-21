---
type: source
title: "You're Hardly Using What Claude Code Has to Offer, it's Insane"
description: "In the last couple of months Claude Code has added roughly a dozen features (1M context, agent teams, git worktrees, new slash commands, remote control, automemory, and scheduling) that turn it into a multi-agent orchestration platform, and knowing when NOT to lean on each one matters as much as knowing they exist."
youtube_id: uegyRTOrXSU
url: https://www.youtube.com/watch?v=uegyRTOrXSU
slug: youre-hardly-using-what-claude-code-has-to-offer-its-insane
published: 2026-03-23
duration: "0:14:43"
recency_rank: 25
raw: "../raw/youre-hardly-using-what-claude-code-has-to-offer-its-insane.md"
tags: [claude-code, subagents, orchestration, features]
created: 2026-07-21
updated: 2026-07-21
---

# You're Hardly Using What Claude Code Has to Offer, it's Insane

Cole walks through about a dozen features Anthropic shipped to Claude Code in the prior couple of months, framing the tool's evolution from autocomplete to autonomous agents to a full multi-agent orchestration platform. For each feature he pairs the capability with a practical judgment call about when it actually helps. The headline additions include the now-generally-available 1 million token context window (caveat: hallucinations spike past 250-300k tokens, so compact or hand off before then), agent teams that can communicate in parallel (great for fast proof-of-concepts, not production yet), and native git worktree support (his most-used new feature, enabling parallel work on multiple codebase copies without manual setup).

He then covers new built-in slash commands Anthropic dogfooded internally: /simplify (de-overengineers code after an implementation) and /batch (orchestrates large parallel refactors like swapping every console.log for a structured logger). Remote control (/remote-control) hands off a session to the Claude phone app for cross-device work. On the sub-agent side, sub-agents now get persistent memory and their own granular hooks, and the new automemory lets Claude curate its own memory folder across sessions to learn from mistakes, complementing (not replacing) the human-curated CLAUDE.md.

Two small commands round it out: /btw for a tool-less sidecar conversation that keeps trivial questions out of your primary context, and /loop for scheduling a recurring prompt (deployment polling, a test quality-gate, website watching). He also notes native /voice support (though external tools like Aqua Voice or Whispering still edge it out), adjustable model effort levels (low/medium/high, plus Opus max) to balance reasoning against 5-hour and weekly token limits, and scheduled tasks / cron jobs managed entirely through natural language.

## Concepts covered

- [Context Rot](../concepts/context-rot.md)
- [Agent Teams](../concepts/agent-teams.md)
- [Parallel Agentic Coding](../concepts/parallel-agentic-coding.md)
- [Commandify Everything](../concepts/commandify-everything.md)
- [Subagents Pattern](../concepts/subagents-pattern.md)
- [Claude Code Hooks](../concepts/claude-code-hooks.md)
- [Self-Evolving Memory](../concepts/self-evolving-memory.md)
- [Global Rules](../concepts/global-rules.md)
- [Context Isolation](../concepts/context-isolation.md)
- [Agentic Workflow Engineering](../concepts/agentic-workflow-engineering.md)
- [Model Selection](../concepts/model-selection.md)
- [The Evolution of AI Coding](../concepts/the-evolution-of-ai-coding.md)

## Entities

- [Claude Code](../entities/tools/claude-code.md)
- [Anthropic](../entities/organizations/anthropic.md)
- [Git Worktrees](../entities/tools/git-worktree.md)
- [Aqua Voice](../entities/tools/aqua-voice.md)
- [Cole Medin](../entities/people/cole-medin.md)

## Key moments

- **[0:00:36]** Framing: a dozen new Claude Code features from the last couple months, positioning it as a multi-agent orchestration platform
- **[0:01:31]** 1 million token context window now GA for Sonnet and Opus; ~750k words
- **[0:01:49]** Key caveat: hallucinations spike past 250-300k tokens; use /context to monitor, then compact or hand off
- **[0:02:21]** Agent teams, parallel agents that communicate with each other (e.g., security/performance/test-coverage review)
- **[0:03:47]** Native git worktree support, Cole's most-used new feature for parallel work on codebase copies
- **[0:04:37]** Built-in /simplify (de-overengineer) and /batch (parallel large refactor) commands
- **[0:06:10]** Remote control, hand a session to the Claude phone app for cross-device coding
- **[0:07:11]** Sub-agents gain persistent memory and per-agent granular hooks
- **[0:07:40]** Automemory, Claude curates its own memory folder across sessions, complementing CLAUDE.md
- **[0:08:46]** /btw sidecar (tool-less) and /loop recurring-prompt commands
- **[0:11:00]** Native /voice support; still recommends external speech-to-text like Aqua Voice / Whispering
- **[0:12:04]** Adjustable model effort levels (low/medium/high, Opus max) to manage token limits
- **[0:13:03]** Scheduled tasks and cron jobs managed entirely through natural language

## Transcript

[Raw transcript](../raw/youre-hardly-using-what-claude-code-has-to-offer-its-insane.md)
