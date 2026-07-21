---
type: concept
title: "Coding Agent as General Assistant"
description: "A coding agent is really five capabilities (file ops, search, terminal, web search, code intelligence) and removing code intelligence leaves exactly the general on-machine assistant a second brain needs."
tags: [claude-code, agentic-coding]
videos: [i-built-my-second-brain-with-claude-code-obsidian-skills-heres-how]
created: 2026-07-21
updated: 2026-07-21
---

# Coding Agent as General Assistant

This is the reframe that unlocks using a coding agent for work that has nothing to do with code. Decompose the tool and there is no "coding" primitive at the bottom of it: "it really comes down to these five categories. It needs to work with our files, search through them, run terminal commands, search the web, and then it needs access to code intelligence" [0:04:51]. Four of those five are generic. Only the last is domain-specific, and once you subtract it the remainder is the assistant everyone has been trying to build from scratch: "if we take this out of the picture, then all we have is just a very powerful general assistant that is running on our machine. And that's exactly what we need for a second brain" [0:05:16].

The practical consequence is that you should stop shopping for a personal-assistant product and start pointing the agent you already trust at a folder of markdown. File operations become note creation and editing, search becomes recall over your own writing, terminal access becomes scripting and automation over your life, and web search becomes research. The agent's maturity - permissioning, hooks, skills, subagents, long-session context handling - carries over wholesale, because none of that machinery was ever code-specific either.

It also explains why the vault, not the model, is the interesting design surface. If the harness is already general, the leverage moves to what you feed it and what you let it do: your files, your instructions, and the skills you install on top.

## Builds on

- [The Core Components of an Agent](./agent-core-components.md) - the general anatomy this five-capability breakdown specializes.
- [Capabilities Over Tools](./capabilities-over-tools.md) - reasoning about an agent by what it can do rather than by the product name on the box.
- [Embedding a Coding Agent in Your Application](./embedding-a-coding-agent.md) - Using a coding agent's SDK to programmatically define and embed the same agent harness inside your own apps and workflows, including non-coding work like note-taking, research, and knowledge management.

## Part of

- [Second Brain](./second-brain.md) - the system this repurposed agent is built to run.

## Contrasts with

- [AI Coding Assistant](./ai-coding-assistant.md) - the same harness with code intelligence left in, aimed at a codebase.

## Related

- [Skills](./skills.md) and [Slash Commands](./slash-commands.md) - how non-coding workflows get taught to a coding agent.
- [The AI Layer](./the-ai-layer.md) - the configuration layer that specializes a general agent for a domain.
- [Memory Systems](./memory-systems.md), [Self-Evolving Memory](./self-evolving-memory.md), [The LLM Wiki](./the-llm-wiki.md) - what the assistant reads and writes once the code intelligence is gone.
- [Heartbeat](./heartbeat.md) - giving the assistant a proactive schedule instead of only reacting to prompts.
- [Agentic Search](./agentic-search.md) - the search capability, applied to notes instead of source files.
- [Language Server Protocol](./language-server-protocol.md) and [Codebase Indexing](./codebase-indexing.md) - the code intelligence being subtracted.
- [Agentic Coding](./agentic-coding.md) - the original use case.

## Tools

- [Claude Code](../entities/tools/claude-code.md) - the coding agent Cole repurposes as the assistant.
- [Obsidian](../entities/tools/obsidian.md) - the markdown vault it operates on.
- [Claude Agent SDK](../entities/tools/claude-agent-sdk.md) - the same harness, embedded in scripts.
- [grep (command-line search)](../entities/tools/ripgrep.md) - the search primitive underneath.

## Sources

- [I Built My Second Brain with Claude Code + Obsidian + Skills (Here's How)](../sources/i-built-my-second-brain-with-claude-code-obsidian-skills-heres-how.md) - "[0:04:51] it really comes down to these five categories. It needs to work with our files, search through them, run terminal commands, search the web, and then it needs access to code intelligence"
- [I Built My Second Brain with Claude Code + Obsidian + Skills (Here's How)](../sources/i-built-my-second-brain-with-claude-code-obsidian-skills-heres-how.md) - "[0:05:16] if we take this out of the picture, then all we have is just a very powerful general assistant that is running on our machine. And that's exactly what we need for a second brain"
