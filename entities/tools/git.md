---
type: entity
subtype: tool
title: "Git"
description: "Version control used as a core part of harness memory: commits and the git log let fresh sessions reconstruct progress, and enable automatic rollback."
resource: "https://git-scm.com"
tags: [version-control, harness, memory]
videos: [are-agent-harnesses-bringing-back-vibe-coding, were-taking-this-ai-coding-assistant-to-the-moon-plus-installation-instructions]
created: 2026-07-21
updated: 2026-07-21
---

# Git

Git is the version-control system Cole treats not just as a prerequisite for pulling repos but as an active memory mechanism inside AI coding harnesses. Its baseline role is table stakes: "the first one obviously being Git You need to be able to pull this GitHub repository so you have to install git on your machine" ([0:04:11](../../sources/were-taking-this-ai-coding-assistant-to-the-moon-plus-installation-instructions.md)). The more interesting claim is architectural. When he sets up a harness, initializing a repo is a deliberate design choice: it "initializes the git repo because we're going to be using git as a core part of our memory for all of our coding agents" ([0:16:43](../../sources/are-agent-harnesses-bringing-back-vibe-coding.md)).

The idea is that commits and the git log become durable, external memory that survives a [context reset](../../concepts/context-reset.md). A long agent run inevitably hits [context rot](../../concepts/context-rot.md), so instead of trying to hold all progress in a single conversation window, the harness commits work as it goes. A fresh session can then reconstruct exactly where things stand by reading the git history rather than the polluted context. This is the [git-as-long-term-memory](../../concepts/git-as-long-term-memory.md) pattern, and it is a concrete piece of [context engineering](../../concepts/context-engineering.md): the repo carries state so the model's window does not have to.

Git also gives the harness a safety net. Because every step is committed, "we can automatically roll back like when we have git integrated with a coding harness" ([0:22:33](../../sources/are-agent-harnesses-bringing-back-vibe-coding.md)). When an agent goes down a bad path, the harness reverts to the last good commit instead of leaving the codebase broken. This makes Git foundational to the [AI coding harness](../../concepts/ai-coding-harness.md) as Cole describes it, and part of why harnesses represent an evolution in how AI writes code: the version-control layer turns risky autonomous edits into checkpointed, reversible progress.

## Related

- [Git as Long-Term Memory](../../concepts/git-as-long-term-memory.md) - the pattern Git realizes inside a harness
- [AI Coding Harness](../../concepts/ai-coding-harness.md) - Git is a core component of the harness memory and rollback loop
- [Context Reset](../../concepts/context-reset.md) - the git log lets a fresh session rebuild state after a reset
- [Context Rot](../../concepts/context-rot.md) - committing progress keeps state out of the degrading window
- [Context Engineering](../../concepts/context-engineering.md), [The Evolution of AI Coding](../../concepts/the-evolution-of-ai-coding.md), [The AI Layer](../../concepts/the-ai-layer.md) - surrounding frames
- Sibling tools: [Claude Code](./claude-code.md), [Archon](./archon.md)

## Sources

- [Are Agent Harnesses Bringing Back Vibe Coding?](../../sources/are-agent-harnesses-bringing-back-vibe-coding.md) - "[0:16:43] initializes the git repo because we're going to be using git as a core part of our memory for all of our coding agents."
- [Are Agent Harnesses Bringing Back Vibe Coding?](../../sources/are-agent-harnesses-bringing-back-vibe-coding.md) - "[0:22:33] we can automatically roll back like when we have git integrated with a coding harness."
- [We're Taking this AI Coding Assistant to the MOON](../../sources/were-taking-this-ai-coding-assistant-to-the-moon-plus-installation-instructions.md) - "[0:04:11] the first one obviously being Git You need to be able to pull this GitHub repository so you have to install git on your machine"
