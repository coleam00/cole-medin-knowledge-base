---
type: source
title: "How to Properly Use Claude Code Agent Teams (FULL LIVE BUILD)"
description: "Claude Code's new agent teams let multiple agents work in parallel AND communicate with each other, and the way to use them reliably today is a contract-first plan produced through heavy clarifying questions plus end-to-end browser validation."
youtube_id: uvs1Igr4u6g
url: https://www.youtube.com/watch?v=uvs1Igr4u6g
slug: how-to-properly-use-claude-code-agent-teams-full-live-build
published: 2026-02-16
duration: "0:50:21"
recency_rank: 34
raw: "../raw/how-to-properly-use-claude-code-agent-teams-full-live-build.md"
tags: [agent-teams, claude-code, agentic-coding]
created: 2026-07-21
updated: 2026-07-21
---
# How to Properly Use Claude Code Agent Teams (FULL LIVE BUILD)

Cole does a live brownfield build, adding a ChargeBee token-purchase payment integration on top of an existing agentic chat app (Next.js + Supabase), to showcase Claude Code's experimental 'agent teams' feature released with Opus 4.6. The key distinction from subagents is communication: subagents run in parallel but only report back to the main agent, whereas agent-team teammates share a task list and message each other and the lead agent to coordinate who handles which task. The tradeoffs are non-determinism (the lead agent owns coordination) and heavy token overhead, though Cole finds the actual usage modest (16% of a session). He argues agent teams point at where agentic engineering is heading, even if they aren't yet production-reliable.

## Concepts covered

- [Agent Teams](../concepts/agent-teams.md)
- [Subagents Pattern](../concepts/subagents-pattern.md)
- [Contract-First Development](../concepts/contract-first.md)
- [Reduce Assumptions](../concepts/reduce-assumptions.md)
- [Clarifying Questions](../concepts/clarifying-questions.md)
- [Planning with AI](../concepts/planning-with-ai.md)
- [Prime Command](../concepts/prime-command.md)
- [Context Reset](../concepts/context-reset.md)
- [End-to-End Validation](../concepts/end-to-end-validation.md)
- [Commandify Everything](../concepts/commandify-everything.md)
- [Skills](../concepts/skills.md)
- [Human in the Loop](../concepts/human-in-the-loop.md)

## Entities

- [Claude Code](../entities/tools/claude-code.md)
- [Vercel Agent Browser CLI](../entities/tools/agent-browser.md)
- [Supabase](../entities/tools/supabase.md)
- [Anthropic](../entities/organizations/anthropic.md)
- [Cole Medin](../entities/people/cole-medin.md)

## Key moments

- **[0:01:19]** Agent teams released with Opus 4.6; experimental, non-deterministic, token-heavy but points at the future
- **[0:01:50]** Core distinction: agent teams share a task list and communicate with each other, unlike subagents
- **[0:07:31]** Brownfield planning begins with a /prime command to set codebase context
- **[0:11:28]** The number-one goal of planning: reduce the assumptions the coding agent is making
- **[0:17:37]** Formalizing the brain dump into a structured plan via a custom /plan command
- **[0:27:24]** After the plan, reset into a fresh context because the plan is the only context needed
- **[0:31:37]** The 'build with agent team' command uses a contract-first approach before spawning agents
- **[0:40:21]** Opus 4.6 skips the end-to-end testing; Cole forces it to run the agent browser CLI
- **[0:47:55]** End-to-end validation autonomously finds and fixes all issues; full purchase flow works

## Transcript

[Raw transcript](../raw/how-to-properly-use-claude-code-agent-teams-full-live-build.md)

