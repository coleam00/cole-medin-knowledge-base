---
type: source
title: "I've Used Claude Code for 2,000+ Hours - Here's How I Build Anything With It"
description: "After 2,000+ hours in Claude Code, the single highest-leverage skill is context engineering, captured in the WHISK framework (Write, Isolate, Select, Compress) that keeps the context window as lean as possible while still giving the agent everything it needs."
youtube_id: nxHKBq5ZU9U
url: https://www.youtube.com/watch?v=nxHKBq5ZU9U
slug: ive-used-claude-code-for-2000-hours-heres-how-i-build-anything-with-it
published: 2026-03-16
duration: "0:22:49"
recency_rank: 27
raw: "../raw/ive-used-claude-code-for-2000-hours-heres-how-i-build-anything-with-it.md"
tags: [context-engineering, whisk, claude-code, context-rot]
created: 2026-07-21
updated: 2026-07-21
---

# I've Used Claude Code for 2,000+ Hours - Here's How I Build Anything With It

Cole argues that roughly 80% of the time an AI coding agent fails, it is because context was managed poorly, not because the model is incapable. The core enemy is context rot: as the context window fills, the LLM struggles with the needle-in-the-haystack problem and gets confused by 'distractors' (similar-but-wrong information), which is especially punishing on large, repetitive codebases. Even Claude Code's new 1M-token window doesn't fix this, so context must be treated as the most precious, deliberately engineered resource.

He packages his battle-tested strategies into the WHISK framework, demonstrated live on the new Archon codebase. Write (externalize agent memory): use the git log as long-term memory via a standardized /commit command, always start a fresh context window when moving from planning to writing code, and use progress/handoff/decision-log files to bridge sessions. Isolate (use sub-agents): spin up parallel sub-agents for codebase and web research so tens or hundreds of thousands of tokens of exploration collapse into a ~500-token summary in the main window (Anthropic reports ~90% improvement), plus the 'scout pattern' where a sub-agent decides whether a doc is worth loading before you commit it.

Select (load context just-in-time, not just-in-case) uses a four-layer approach: concise global rules (500-700 lines), on-demand rules loaded only for the relevant part of the codebase, skills with progressive disclosure (description first, full SKILL.md and scripts only when needed), and prime commands that spend tokens up front to explore the live codebase before planning. Compress is the last resort and least-needed section if the other layers are done well: the /handoff command and Claude Code's /compact (optionally with focus instructions) manage a bloated window, but the best compression strategy is not needing compression at all.

## Concepts covered

- [The WHISK Framework](../concepts/the-whisk-framework.md)
- [Context Engineering](../concepts/context-engineering.md)
- [Context Rot](../concepts/context-rot.md)
- [Git as Long-Term Memory](../concepts/git-as-long-term-memory.md)
- [Context Reset](../concepts/context-reset.md)
- [Planning with AI](../concepts/planning-with-ai.md)
- [Memory Systems](../concepts/memory-systems.md)
- [Context Isolation](../concepts/context-isolation.md)
- [Subagents Pattern](../concepts/subagents-pattern.md)
- [Progressive Disclosure](../concepts/progressive-disclosure.md)
- [Global Rules](../concepts/global-rules.md)
- [Skills](../concepts/skills.md)
- [Prime Command](../concepts/prime-command.md)
- [Slash Commands](../concepts/slash-commands.md)
- [Commandify Everything](../concepts/commandify-everything.md)
- [End-to-End Validation](../concepts/end-to-end-validation.md)
- [Context Window Limits](../concepts/context-window-limits.md)

## Entities

- [Claude Code](../entities/tools/claude-code.md)
- [Archon](../entities/tools/archon.md)
- [Vercel Agent Browser CLI](../entities/tools/agent-browser.md)
- [Anthropic](../entities/organizations/anthropic.md)
- [Chroma](../entities/tools/chroma.md)
- [GitHub](../entities/tools/github.md)
- [Cole Medin](../entities/people/cole-medin.md)
- [Lior Weinstein](../entities/people/lior-weinstein.md)
- [CTO.ai](../entities/organizations/cto-ai.md)

## Key moments

- **[0:00:00]** Cole frames the video: 2,000+ hours in Claude Code, sharing power-user strategies as the WHISK framework
- **[0:02:19]** Claims ~80% of agent failures are context-management failures; introduces context rot as the core problem
- **[0:02:52]** Cites the Chroma technical report on how increasing input tokens degrades LLM performance
- **[0:03:26]** Explains needle-in-the-haystack and distractors as the mechanism of context rot
- **[0:05:16]** WHISK defined: Write, Isolate, Select, Compress
- **[0:05:33]** Write strategy 1: git log as long-term memory via a standardized /commit command
- **[0:08:42]** Write strategy 2: always start a fresh context window when going from planning to implementation
- **[0:09:56]** Write strategy 3: progress files, decision logs, and the /handoff command between sessions
- **[0:11:41]** Isolate: use sub-agents for research to keep the main context clean (~90% token improvement)
- **[0:14:09]** The scout pattern: a sub-agent decides whether documentation is worth loading before committing it
- **[0:15:35]** Select: load context just-in-time, not just-in-case, via a four-layer approach
- **[0:17:52]** Prime commands explore the live codebase at the start of planning
- **[0:19:26]** Compress: /handoff and /compact as last resorts; best compression is not needing compression
- **[0:22:06]** Promo: free AI transformation workshop April 2 with Lior Weinstein of CTO.ai

## Transcript

[Raw transcript](../raw/ive-used-claude-code-for-2000-hours-heres-how-i-build-anything-with-it.md)
