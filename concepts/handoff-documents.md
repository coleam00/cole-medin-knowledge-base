---
type: concept
title: "Handoff Documents"
description: "Because isolated agents share no conversation history, they communicate by writing and reading markdown handoff files (initial.md, prompts.md) in a shared planning folder, passing only the distilled context each next step needs."
tags: [context-engineering, subagents, memory]
videos: [i-built-my-claude-code-subagents-dream-team-to-create-any-ai-agent]
created: 2026-07-21
updated: 2026-07-21
---

# Handoff Documents

A handoff document is a markdown file one agent writes so the next agent can read it. Subagents run in isolated context windows, so they cannot talk: nothing said inside one appears inside another. The file system becomes the bus. As Cole puts it, "we use these markdown files to allow these sub aents to communicate with each other and with our primary cloud code agent."

The pattern is a chain of named artifacts in a shared planning folder, each step consuming the previous file and emitting the next: "we have the prompt come into our engineer agent from the primary cloud code instance and we're telling it to look in initial MD... the last thing that it does is it outputs a prompts.mmd." Requirements land in `initial.md`, the engineer agent turns them into `prompts.md`, and the next specialist reads only that. Each hop is a deliberate narrowing, since the handoff carries the **distilled** conclusion rather than the transcript that produced it.

That narrowing is the real payoff. The orchestrator never absorbs each subagent's full working context, so a long multi-agent run does not degrade the primary window. It also makes the pipeline inspectable and resumable: the intermediate files are human-readable, editable before the next step runs, and committed alongside the code, so a failed stage can be re-run from its input instead of from the top. Naming the files as a fixed convention is what makes the handoff reliable, since each agent's instructions can point at an exact path instead of hoping the right context was passed along.

## Prerequisites

- [Context Isolation](./context-isolation.md) - separate windows are precisely why agents cannot speak directly.
- [Context Engineering](./context-engineering.md) - deciding what to carry forward is the design work in every handoff.

## Part of

- [Subagents Pattern](./subagents-pattern.md) - handoff files are the wiring between the specialists.
- [Agent Teams](./agent-teams.md) - a team only coheres if its members share written artifacts.

## Contrasts with

- [Context Rot](./context-rot.md) - the alternative, piling every step's reasoning into one thread, is what handoffs exist to prevent.

## Related

- [File-System-Based Agents](./file-system-based-agents.md) - the general principle: state lives on disk, not in a conversation.
- [Git as Long-Term Memory](./git-as-long-term-memory.md) - committed handoff files give the pipeline a durable history.
- [Memory Systems](./memory-systems.md) - handoffs are short-term working memory between steps.
- [Context Reset](./context-reset.md) - a fresh session can pick the work back up by reading the last file written.
- [Progressive Disclosure](./progressive-disclosure.md) - each agent reads only the document its step needs.
- [Phases of Work](./phases-of-work.md) and [Synthesizer Agent](./synthesizer-agent.md) - the stage boundaries and the merge step that handoffs formalize.
- [PRD-First Development](./prd-first-development.md) and [PRP Framework](./prp-framework.md) - the plan document is the largest handoff in the chain.
- [Agents That Build Agents](./agents-that-build-agents.md) - the dream-team pipeline this pattern came from.
- [Human in the Loop](./human-in-the-loop.md) - a readable intermediate file is a natural approval gate.
- [Long-Running Agents](./long-running-agents.md) - Coding agents that run autonomously for hours or days as background tasks, chaining dozens of fresh-context sessions through shared artifact files to produce a working proof of concept before a human takes over.

## Tools

- [Claude Code](../entities/tools/claude-code.md) - the primary agent that dispatches subagents and owns the planning folder.
- [Archon](../entities/tools/archon.md) - runs multi-step workflows whose nodes pass artifacts the same way.
- [Gemini 3.5 Flash](../entities/tools/gemini-3-5-flash.md) - Google's cheap, fast LLM that builds unusually beautiful, handcrafted-looking frontends; the design half of Cole's provider-mixing workflow, paired with Opus 4.8 for planning and integrations.

## Sources

- [I Built My Claude Code Subagents DREAM TEAM to Create Any AI Agent](../sources/i-built-my-claude-code-subagents-dream-team-to-create-any-ai-agent.md) - "[0:02:30] we use these markdown files to allow these sub aents to communicate with each other and with our primary cloud code agent."
- [I Built My Claude Code Subagents DREAM TEAM to Create Any AI Agent](../sources/i-built-my-claude-code-subagents-dream-team-to-create-any-ai-agent.md) - "[0:14:11] we have the prompt come into our engineer agent from the primary cloud code instance and we're telling it to look in initial MD... the last thing that it does is it outputs a prompts.mmd"
