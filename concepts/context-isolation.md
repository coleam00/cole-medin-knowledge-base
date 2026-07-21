---
type: concept
title: "Context Isolation"
description: "Giving each agent or subagent its own clean context window so unrelated tokens never dilute the task at hand."
tags: [context-isolation, subagents-pattern, context-engineering, agent-teams]
videos: [the-subagent-era-is-officially-here-learn-this-now, ive-used-claude-code-for-2000-hours-heres-how-i-build-anything-with-it, turn-claude-code-into-your-full-engineering-team-with-subagents, my-complete-agentic-coding-workflow-to-build-anything-no-fluff-or-overengineering, anthropic-just-dropped-a-masterclass-on-building-agent-harnesses-for-large-codebases, full-guide-to-becoming-a-principled-agentic-engineer-build-anything-with-ai, parallel-claude-code-git-worktrees-this-setup-will-change-how-you-ship, the-next-evolution-of-ai-coding-is-harnesses-heres-how-to-build-them, harness-engineering-what-separates-top-agentic-engineers-right-now, i-built-my-claude-code-subagents-dream-team-to-create-any-ai-agent, claude-codes-agent-teams-are-insane-multiple-ai-agents-coding-together-in-real-time, the-creators-of-claude-code-and-openclaw-dont-prompt-their-agents-anymore, stripes-coding-agents-ship-1300-prs-every-week-heres-how-they-do-it, a-complete-guide-to-claude-code-here-are-all-the-best-strategies]
created: 2026-07-21
updated: 2026-07-21
---

# Context Isolation

Context isolation is giving each agent or subagent its own clean context window so the work of one never pollutes another. Cole states the purpose plainly: "We're using subagents for context isolation. So we're not bloating the main context window for our primary orchestrator here." The main win is that a subagent can burn enormous tokens exploring and hand back only a distilled result: "We can use subagents to perform tens or even hundreds of thousands of tokens of research... and then just giving the needed summary to our main claude code context window," compressing "tens of thousands of tokens of research" down to "only something like 500 tokens."

Because a subagent "runs with its own context window. It does all the analysis it needs to and then it returns a summary back," isolation makes research and exploration the ideal delegation target: "usually all we need is that summary back." The counterpart caution is that isolation breaks continuity, so implementation is a poor fit: "I don't recommend using subagents for implementation because with implementation we usually care about all of the context of the files that we've been editing." Isolated agents also do not share history, which means "we have to make sure that we're passing in all the context the subagent needs."

Isolation applies beyond subagents to whole sessions and infrastructure. Multi-step harness workflows run "every step is a separate coding agent session," communicating only "by passing off handoff documents." Parallel work needs environment isolation too, "worktrees... so they're not stepping on each other's toes, not just with code changes, but also database changes." Stripe pushes this furthest: every run happens "in an isolated AWS EC2 instance... they call it cattle, not pets." A special case is review: the validator must never see the writer's chat, "start a fresh context window. The reviewer should never see the writer's chat" (see [Separate Reviewer](./separate-reviewer.md)).

## Part of

- [Subagents Pattern](./subagents-pattern.md) - subagents are the primary mechanism for isolation.
- [Context Engineering](./context-engineering.md) - isolation is one of its core protection strategies.
- [AI Coding Harness](./ai-coding-harness.md) - session-level isolation is a harness building block.

## Contrasts with

- [Context Reset](./context-reset.md) - reset clears one agent's window over time; isolation runs separate windows in parallel.

## Related

- [Context Rot](./context-rot.md) - the degradation isolation prevents by keeping windows small.
- [Separate Reviewer](./separate-reviewer.md) and [Code Review](./code-review.md) - the reviewer gets a fresh, isolated window to remove bias.
- [Parallel Agentic Coding](./parallel-agentic-coding.md) - worktrees give each parallel agent an isolated workspace.
- [Agent Teams](./agent-teams.md) and [Agentic Workflow Engineering](./agentic-workflow-engineering.md) - orchestrating many focused, isolated sessions.
- [The PIV Loop](./the-piv-loop.md) and [The WHISK Framework](./the-whisk-framework.md) - workflows that lean on isolated sessions.

## Tools

- [Claude Code](../entities/tools/claude-code.md) - subagents and agent teams each get their own context window.

## Sources

- [The Subagent Era Is Officially Here - Learn this Now](../sources/the-subagent-era-is-officially-here-learn-this-now.md) - "[0:10:39] I want to use subagents because I need that context isolation."
- [Turn Claude Code into Your Full Engineering Team with Subagents](../sources/turn-claude-code-into-your-full-engineering-team-with-subagents.md) - "[0:09:51] We're using subagents for context isolation. So we're not bloating the main context window for our primary orchestrator here."
- [I've Used Claude Code for 2,000+ Hours - Here's How I Build Anything With It](../sources/ive-used-claude-code-for-2000-hours-heres-how-i-build-anything-with-it.md) - "[0:11:57] instead of loading in tens of thousands of tokens of research into our main context window, it is now only something like 500 tokens."
- [My COMPLETE Agentic Coding Workflow to Build Anything](../sources/my-complete-agentic-coding-workflow-to-build-anything-no-fluff-or-overengineering.md) - "[0:09:35] I don't recommend using subagents for implementation because with implementation we usually care about all of the context of the files that we've been editing."
- [Anthropic Just Dropped a Masterclass on Building Agent Harnesses](../sources/anthropic-just-dropped-a-masterclass-on-building-agent-harnesses-for-large-codebases.md) - "[0:22:30] It runs with its own context window. It does all the analysis it needs to and then it returns a summary back to our primary Claude Code session."
- [Parallel Claude Code + Git Worktrees](../sources/parallel-claude-code-git-worktrees-this-setup-will-change-how-you-ship.md) - "[0:10:28] start a fresh context window. The reviewer should never see the writer's chat."
- [I Built My Claude Code Subagents DREAM TEAM to Create Any AI Agent](../sources/i-built-my-claude-code-subagents-dream-team-to-create-any-ai-agent.md) - "[0:06:10] these subagents do not share the conversation history with our primary claude code agent. So, we have to make sure that we're passing in all the context the subagent needs."
- [Claude Code's Agent Teams Are Insane](../sources/claude-codes-agent-teams-are-insane-multiple-ai-agents-coding-together-in-real-time.md) - "[0:10:39] our primary agent knows generally what happened, but it doesn't have to be polluted by the context of the entire task."
- [Stripe's Coding Agents Ship 1,300 PRs EVERY Week](../sources/stripes-coding-agents-ship-1300-prs-every-week-heres-how-they-do-it.md) - "[0:11:31] they call it cattle, not pets, as in these instances are not important. We can spin them up and tear them down willy-nilly."
- [The Creators of Claude Code and OpenClaw don't Prompt Their Agents Anymore?!](../sources/the-creators-of-claude-code-and-openclaw-dont-prompt-their-agents-anymore.md) - "[0:14:03] if we're having many different agents handling tasks in a loop, we need to make sure they're running in isolation so they're not stepping on each other's toes."
- [The Next Evolution of AI Coding Is Harnesses](../sources/the-next-evolution-of-ai-coding-is-harnesses-heres-how-to-build-them.md) - "[0:07:21] You always want to do your planning and implementation in different coding sessions to remove bias."
- [A Complete Guide to Claude Code](../sources/a-complete-guide-to-claude-code-here-are-all-the-best-strategies.md) - "[0:26:23] The subagent has its own context window. So, we're not bringing in the entire conversation history into each subagent."
