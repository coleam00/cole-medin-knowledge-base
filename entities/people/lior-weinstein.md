---
type: entity
subtype: person
title: "Lior Weinstein"
description: "Co-host of Cole's AI Transformation Workshop and founder of CTOX; source of the CX-OS 'agent-managed operations' framing."
tags: [ai-transformation, operations, workshop]
videos: [full-guide-to-becoming-a-principled-agentic-engineer-build-anything-with-ai, ive-used-claude-code-for-2000-hours-heres-how-i-build-anything-with-it]
created: 2026-07-21
updated: 2026-07-21
---

# Lior Weinstein

Lior Weinstein is the collaborator Cole co-hosted the free AI Transformation Workshop with, and the source of an operations framing Cole reuses when explaining what agentic systems are for. Cole introduces him plainly: "I hosted the AI transformation workshop with Lior Weinstein. He's a big name in the AI space" ([0:00:00]), and names his company: "I am hosting a free AI transformation workshop live on my YouTube channel along with Lior Weinstein, the founder of CTOX" ([0:22:06]).

His durable contribution here is the CX-OS idea, where an agent shoulders the repetitive operational load so humans stay on judgment. Cole borrows it directly to illustrate his own setups: "It's kind of like the whole COXOS that Lior was showing you guys where you have the agent managing all of the grunt work" ([0:30:53]). That framing maps onto the practices Cole teaches around it: [Context Engineering](../../concepts/context-engineering.md) to feed the agent the right operating context, [Planning with AI](../../concepts/planning-with-ai.md) before execution, and the mechanics of keeping long-running agents coherent, [Git as Long-Term Memory](../../concepts/git-as-long-term-memory.md), [Context Reset](../../concepts/context-reset.md), and [Context Isolation](../../concepts/context-isolation.md). It also connects to delegating grunt work to a [Subagents Pattern](../../concepts/subagents-pattern.md), the concrete way "the agent managing all of the grunt work" gets built.

## Related

- [Context Engineering](../../concepts/context-engineering.md) - The deliberate practice of curating exactly what goes into an LLM's limited context window - system messages, schemas, chat history, and dynamic variables - to avoid overload and keep outputs sharp.
- [Planning with AI](../../concepts/planning-with-ai.md) - Using the AI to produce a detailed plan before implementation so execution follows a reviewed blueprint instead of improvising.
- [Subagents Pattern](../../concepts/subagents-pattern.md) - Delegating scoped tasks to isolated subagents to parallelize work and protect the main agent's context window.
- [Git as Long-Term Memory](../../concepts/git-as-long-term-memory.md) - Treating the git history and versioned files as durable, inspectable memory for agents instead of opaque model state.
- [Context Reset](../../concepts/context-reset.md) - Clearing or compacting an agent's context window between phases of work to avoid context rot and keep reasoning sharp.
- [Context Isolation](../../concepts/context-isolation.md) - Giving each agent or subagent its own clean context window so unrelated tokens never dilute the task at hand.
- [Cole Medin](./cole-medin.md) - AI engineer and educator whose YouTube channel and Dynamous community teach agentic coding; creator of Archon and the source of this entire knowledge base.

## Sources

- [FULL Guide to Becoming a Principled Agentic Engineer (Build Anything with AI)](../../sources/full-guide-to-becoming-a-principled-agentic-engineer-build-anything-with-ai.md) - "[0:30:53] It's kind of like the whole COXOS that Lior was showing you guys where you have the agent managing all of the grunt work."
- [I've Used Claude Code for 2,000+ Hours - Here's How I Build Anything With It](../../sources/ive-used-claude-code-for-2000-hours-heres-how-i-build-anything-with-it.md) - "[0:22:06] I am hosting a free AI transformation workshop live on my YouTube channel along with Lior Weinstein, the founder of CTOX."
