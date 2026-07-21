---
type: concept
title: "The Scout Pattern"
description: "Send a sub-agent ahead to explore docs or code and decide whether a piece of context is worth loading into the main window before you commit it."
tags: [subagents, context-isolation, context-engineering]
videos: [ive-used-claude-code-for-2000-hours-heres-how-i-build-anything-with-it]
created: 2026-07-21
updated: 2026-07-21
---

# The Scout Pattern

The scout pattern is using a subagent as a disposable reconnaissance run: it goes and looks at documentation or code, reports back whether that material is actually relevant, and only then do you spend main-window tokens on it. Cole names the metaphor directly: "We want to send scouts ahead before you commit your main context. There might be parts of your codebase or documentation that you want sub agents to explore to see if it is relevant to load into your main cloud code session" [0:14:09].

The key move is that the scout answers a *routing* question, not the task question. It burns whatever tokens it needs inside its own window, then hands back a short verdict, and the human or orchestrator makes the load decision: "It found all of our documentation recommended loading one and then I said, 'Yep, go ahead and load it.'" [0:15:06]. The expensive exploration is paid for in a window you are about to throw away; the main session only ever sees the winning file.

This is why the pattern pairs so naturally with [Context Isolation](./context-isolation.md). A scout is worth dispatching exactly when you cannot tell in advance which of several candidate files matters - a large docs folder, an unfamiliar module, a set of similarly-named services. It fails when you already know what you need, in which case the extra hop is pure latency, and it fails when the scout's summary is too lossy to make a real decision, which is why the return format should be a recommendation plus pointers rather than a rewritten version of the source.

Scouting is a load-time complement to [Progressive Disclosure](./progressive-disclosure.md): disclosure keeps context shallow until it is needed, scouting decides whether the deeper level is worth opening at all.

## Part of

- [Subagents Pattern](./subagents-pattern.md) - the scout is a subagent whose only job is reconnaissance.
- [Context Engineering](./context-engineering.md) - deciding what enters the window is the whole discipline.

## Builds on

- [Context Isolation](./context-isolation.md) - the scout explores in its own window so exploration never pollutes the main one.
- [Agentic Search](./agentic-search.md) - the scout finds relevant material by searching live rather than querying a prebuilt index.

## Contrasts with

- [Codebase Indexing](./codebase-indexing.md) - indexing decides relevance ahead of time and offline; a scout decides it live, per task.

## Related

- [Context Rot](./context-rot.md) - the degradation you avoid by refusing to load material a scout says is irrelevant.
- [Progressive Disclosure](./progressive-disclosure.md) - the same "load only on demand" instinct, applied to layered files.
- [Docs and Templates as Coding-Assistant Context](./docs-as-agent-context.md) - documentation is the most common thing a scout is sent to evaluate.
- [Handoff Documents](./handoff-documents.md) - the scout's report is a small handoff artifact between sessions.
- [Stacking Context-Engineering Strategies](./strategy-stacking.md) - scouting stacks with reset, isolation, and disclosure.
- [The PIV Loop](./the-piv-loop.md) - scouting is a planning-phase move, run before implementation begins.

## Tools

- [Claude Code](../entities/tools/claude-code.md) - subagents dispatched from the main session are Cole's scouts.
- [Kimi K2](../entities/tools/kimi-k2.md) - Moonshot's Kimi model (K2.7), used as a cheap driver and exploration model in Cole's harness via a Kimi subscription to control per-token cost.

## Sources

- [I've Used Claude Code for 2,000+ Hours - Here's How I Build Anything With It](../sources/ive-used-claude-code-for-2000-hours-heres-how-i-build-anything-with-it.md) - "[0:14:09] We want to send scouts ahead before you commit your main context. There might be parts of your codebase or documentation that you want sub agents to explore to see if it is relevant to load into your main cloud code session."
- [I've Used Claude Code for 2,000+ Hours - Here's How I Build Anything With It](../sources/ive-used-claude-code-for-2000-hours-heres-how-i-build-anything-with-it.md) - "[0:15:06] It found all of our documentation recommended loading one and then I said, 'Yep, go ahead and load it.'"
