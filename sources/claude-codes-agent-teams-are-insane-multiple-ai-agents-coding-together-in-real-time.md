---
type: source
title: "Claude Code's Agent Teams Are Insane - Multiple AI Agents Coding Together in Real Time"
description: "Claude Code's new experimental Agent Teams feature lets multiple collaborating agents share one task list and coordinate peer-to-peer, making it far better than isolated sub-agents for implementation work if you guide it with the right instructions."
youtube_id: -1K_ZWDKpU0
url: https://www.youtube.com/watch?v=-1K_ZWDKpU0
slug: claude-codes-agent-teams-are-insane-multiple-ai-agents-coding-together-in-real-time
published: 2026-02-09
duration: "0:20:17"
recency_rank: 36
raw: "../raw/claude-codes-agent-teams-are-insane-multiple-ai-agents-coding-together-in-real-time.md"
tags: [agent-teams, claude-code, parallel-coding]
created: 2026-07-21
updated: 2026-07-21
---
# Claude Code's Agent Teams Are Insane - Multiple AI Agents Coding Together in Real Time

Cole introduces Claude Code's new experimental Agent Teams feature, which spins up multiple Claude Code instances (in tmux or iTerm2 split panes) that collaborate on the same shared task list rather than working in isolation. The key novelty over sub-agents is peer-to-peer coordination: the lead agent decides what team to form based on the request, and the spawned agents actually talk to each other ("I changed this API, update the front-end component"), preventing the kind of silent conflicts that plagued parallel sub-agent implementation. He demos a four-agent code review (security, code quality, documentation) and cites Anthropic's example of 16 agents building a C compiler from scratch for ~$20K in API costs.

The core teaching is the distinction between sub-agents and agent teams. Sub-agents provide context isolation: dispatch a heavy task, get back only a summary, keeping the main agent's precious context clean, but with zero coordination and a black-box process, which makes them best for research over implementation. Agent teams sacrifice token efficiency (often 2-4x the token usage) for true collaboration and a shared task list, which is what implementation needs. Cole's rule of thumb: use sub-agents for research, feed that into a plan, then hand the plan to an agent team to implement.

He's honest about the feature's rough edges: it's experimental and must be explicitly enabled (env var or settings.json), Claude Code isn't actually good at using it out of the box, you must be very specific or it hallucinates weird teams, and agents can't always truly run in parallel (a backend agent built against an incorrect schema before the database agent finished). His solution is a custom skill/command (/build-with-agent-team) that adds reliable team formation, terminal management, and "contract-first spawning": laying groundwork (like the database schema contract) up front, then parallelizing the rest, which he found dramatically more reliable than raw prompting.

## Concepts covered

- [Agent Teams](../concepts/agent-teams.md)
- [Subagents Pattern](../concepts/subagents-pattern.md)
- [Context Isolation](../concepts/context-isolation.md)
- [Contract-First Development](../concepts/contract-first.md)
- [Parallel Agentic Coding](../concepts/parallel-agentic-coding.md)
- [Planning with AI](../concepts/planning-with-ai.md)
- [Skills](../concepts/skills.md)
- [Validation](../concepts/validation.md)

## Entities

- [Claude Code](../entities/tools/claude-code.md)
- [Anthropic](../entities/organizations/anthropic.md)
- [Cole Medin](../entities/people/cole-medin.md)
- [Sonar (Sonar Summit)](../entities/organizations/sonar.md)

## Key moments

- **[0:00:00]** Demo: four Claude Code instances collaborating on a code review via the new Agent Teams feature
- **[0:02:09]** Anthropic used 16 agents with agent teams to build a C compiler for ~$20K in API costs
- **[0:03:11]** How to enable agent teams: env var or settings.json, plus tmux or iTerm2 for split-pane mode
- **[0:05:22]** Live demo: spinning up a 3-agent review team (security, code quality, documentation)
- **[0:08:15]** Sonar Summit sponsor break: AI validation pyramid framework
- **[0:10:23]** Sub-agents = context isolation (research); no coordination, black box
- **[0:11:46]** Agent teams = peer-to-peer coordination and shared task list (implementation)
- **[0:13:09]** Token cost: agent teams often 2-4x more tokens than sub-agents or solo Claude Code
- **[0:14:14]** Two problems: must be very specific or it hallucinates teams; agents can't always truly parallelize
- **[0:16:30]** Contract-first spawning: set the stage (e.g. DB schema) before kicking off parallel agents
- **[0:17:01]** The /build-with-agent-team skill/command: point it at a plan, set or auto-decide team size

## Transcript

[Raw transcript](../raw/claude-codes-agent-teams-are-insane-multiple-ai-agents-coding-together-in-real-time.md)

