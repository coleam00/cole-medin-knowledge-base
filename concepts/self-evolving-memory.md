---
type: concept
title: "Self-Evolving Memory"
description: "A memory system that reflects on and rewrites its own notes over time, promoting and pruning what it stores."
tags: [memory, reflection, self-improving]
videos: [i-love-the-karpathy-llm-wiki-but-it-doesnt-scale-heres-what-does, anthropic-just-dropped-a-masterclass-on-building-agent-harnesses-for-large-codebases, i-built-self-evolving-claude-code-memory-w-karpathys-llm-knowledge-bases, full-guide-build-your-own-ai-second-brain-with-claude-code, youre-hardly-using-what-claude-code-has-to-offer-its-insane, i-forced-claude-to-code-for-24-hours-nonstop-heres-what-happened, build-ai-agents-that-evolve-over-time, introducing-archon-an-ai-agent-that-builds-ai-agents]
created: 2026-07-21
updated: 2026-07-21
---

# Self-Evolving Memory

Self-evolving memory is a memory system that reflects on its own history and rewrites its notes over time, promoting what matters and pruning what does not, instead of just appending. Cole builds it as a promotion process: a reflection pass reads the long raw log and "extracts things like key decisions, lessons learned, important facts. This is one of the most important parts... that allows our agent to evolve over time" - ["Full Guide - Build Your Own AI Second Brain with Claude Code"](../sources/full-guide-build-your-own-ai-second-brain-with-claude-code.md) [0:12:07]. The distilled result lands in an always-loaded file: "you're extracting key findings and things you tell it to remember into that promoted memory like that memory.md file that's always given to the agent." - ["I Love the Karpathy LLM Wiki but it Doesn't Scale"](../sources/i-love-the-karpathy-llm-wiki-but-it-doesnt-scale-heres-what-does.md) [0:15:16].

## Learning from your own work, not external data

What makes this distinct from a knowledge base is the source: the agent learns from its own conversations and decisions rather than ingested documents. The goal is "giving claude code a memory that evolves with your codebase. So basing the whole LLM knowledge base on our conversations with our coding agent or second brain instead of bringing in external data" - ["I Built Self-Evolving Claude Code Memory w/ Karpathy's LLM Knowledge Bases"](../sources/i-built-self-evolving-claude-code-memory-w-karpathys-llm-knowledge-bases.md) [0:01:31], so the "coding agent... is going to get smarter and smarter over time because it remembers the decisions you've made and how you've evolved your project" [0:09:01]. The broader ambition is agents "that learn as we interact with them" - ["Build AI Agents that EVOLVE Over Time"](../sources/build-ai-agents-that-evolve-over-time.md) [0:00:34].

## Hooks that keep rules from going stale

A key mechanism is a stop hook that reflects at the end of a session while context is fresh. "A stop hook can reflect on what happened during a session and propose CLAUDE.md updates while the context is fresh." - ["Anthropic Just Dropped a Masterclass on Building Agent Harnesses"](../sources/anthropic-just-dropped-a-masterclass-on-building-agent-harnesses-for-large-codebases.md) [0:11:08], running "a separate Claude session in headless mode to look at these changes, look at the global rules and propose if anything needs to be tweaked." [0:13:40]. This matters because "As you're evolving your codebase you need to make sure that your rules are evolving as well. It's really really bad when your CLAUDE.md goes stale." [0:13:10].

> **Contradiction:** There are two postures on how much autonomy to grant the memory. Claude's automemory "can curate memories for itself. So it accumulates knowledge across sessions to learn from its mistakes" but "it's a bit more nondeterministic than the CLAUDE.md because we're not managing it" - ["You're Hardly Using What Claude Code Has to Offer"](../sources/youre-hardly-using-what-claude-code-has-to-offer-its-insane.md) [0:07:40], [0:08:15], 2026-07-21. Cole's recommendation reconciles them: rely on both a hand-managed rules file and autonomous automemory together rather than choosing one.

## Builds on

- [Memory Systems](./memory-systems.md) - the durable memory this concept adds a reflection-and-rewrite loop on top of.

## Related

- [Second Brain](./second-brain.md) - daily reflection is the second brain's self-evolution mechanism.
- [Git as Long-Term Memory](./git-as-long-term-memory.md) - the commit ledger the reflection pass reads alongside notes.
- [Knowledge Bases](./knowledge-bases.md) - self-evolving memory is a knowledge base sourced from your own conversations.
- [The LLM Wiki](./the-llm-wiki.md) - the Karpathy pattern of an LLM auto-maintaining its own knowledge files.
- [Claude Code Hooks](./claude-code-hooks.md) - the stop hook that triggers reflection when a session ends.
- [Global Rules](./global-rules.md) - the CLAUDE.md rules a self-evolving system keeps current.
- [Context Isolation](./context-isolation.md) - the fresh headless session that reviews changes without polluting the working context.
- [System Evolution](./system-evolution.md) - the same self-improvement idea applied to a whole codebase or agent.
- [Tool Design](./tool-design.md) - Archon promoting its own good tools and examples back into its library.

## Tools

- [Claude Code](../entities/tools/claude-code.md) - CLAUDE.md plus automemory as complementary self-evolving memory.
- [Claude Agent SDK](../entities/tools/claude-agent-sdk.md) - runs the promotion/reflection pass under the hood.
- [Archon](../entities/tools/archon.md) - an agent that promotes proven agents, tools, and even its own system prompt over time: "adjusting its own system prompt as well as it iterates over time and realizes what makes the agents work the best" - ["Introducing Archon - an AI Agent that BUILDS AI Agents"](../sources/introducing-archon-an-ai-agent-that-builds-ai-agents.md) [0:17:29].

## Sources

- [Full Guide - Build Your Own AI Second Brain with Claude Code](../sources/full-guide-build-your-own-ai-second-brain-with-claude-code.md) - "[0:12:07] it extracts things like key decisions, lessons learned, important facts. This is one of the most important parts... that allows our agent to evolve over time"
- [I Love the Karpathy LLM Wiki but it Doesn't Scale. Here's What Does.](../sources/i-love-the-karpathy-llm-wiki-but-it-doesnt-scale-heres-what-does.md) - "[0:15:16] you're extracting key findings and things you tell it to remember into that promoted memory like that memory.md file that's always given to the agent."
- [I Built Self-Evolving Claude Code Memory w/ Karpathy's LLM Knowledge Bases](../sources/i-built-self-evolving-claude-code-memory-w-karpathys-llm-knowledge-bases.md) - "[0:01:31] giving claude code a memory that evolves with your codebase. So basing the whole LLM knowledge base on our conversations with our coding agent or second brain instead of bringing in external data"
- [Anthropic Just Dropped a Masterclass on Building Agent Harnesses (for Large Codebases)](../sources/anthropic-just-dropped-a-masterclass-on-building-agent-harnesses-for-large-codebases.md) - "[0:11:08] A stop hook can reflect on what happened during a session and propose CLAUDE.md updates while the context is fresh."
- [You're Hardly Using What Claude Code Has to Offer, it's Insane](../sources/youre-hardly-using-what-claude-code-has-to-offer-its-insane.md) - "[0:07:40] now with automemory, Claude has another way where it can curate memories for itself. So it accumulates knowledge across sessions to learn from its mistakes"
- [Build AI Agents that EVOLVE Over Time](../sources/build-ai-agents-that-evolve-over-time.md) - "[0:00:34] What about giving our AI agents the ability to not just learn through documents we give it, but also through our conversations? We want AI agents that learn as we interact with them"
- [I Forced Claude to Code for 24 Hours NONSTOP, Here's What Happened](../sources/i-forced-claude-to-code-for-24-hours-nonstop-heres-what-happened.md) - "[0:05:02] The last core artifact here is our claude progress. This is the file that is updated at the end of every session, giving a summary of what was just done."
- [Introducing Archon - an AI Agent that BUILDS AI Agents](../sources/introducing-archon-an-ai-agent-that-builds-ai-agents.md) - "[0:17:11] whenever archon creates a good Agent or defines good tools and it iterates and tests and confirms it I wanted to add that to its examples and to the tool Library so that it can continuously give itself better examples"
