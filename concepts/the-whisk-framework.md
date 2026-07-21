---
type: concept
title: "The WHISK Framework"
description: "Cole's mnemonic framework for structuring the context you feed an agent to reliably build anything with it."
tags: [the-whisk-framework, context-engineering, agentic-coding, subagents-pattern]
videos: [the-subagent-era-is-officially-here-learn-this-now, ive-used-claude-code-for-2000-hours-heres-how-i-build-anything-with-it]
created: 2026-07-21
updated: 2026-07-21
---

# The WHISK Framework

The WHISK framework is Cole's mnemonic for the distinct ways to manage the context you feed a coding agent so it can reliably build anything. He spells out the acronym: "So W stands for write, I for isolate, S for select and C for compress" [0:05:16]. Each letter names a concrete tactic. *Write* is externalizing context out of the window into durable files (PRDs, notes, git). *Isolate* is keeping separate concerns in separate contexts, for example dispatching subagents so their work never pollutes the main thread. *Select* is pulling in only the context a task actually needs, the just-in-time discipline behind progressive disclosure. *Compress* is condensing what is already in the window so the agent stays sharp as a conversation grows.

WHISK exists specifically as a toolbox for fighting context rot, the degradation that sets in as an agent's window fills with stale or irrelevant tokens. Cole positions it exactly that way when pointing back to it in a later video: "There's a lot of solutions to context rod. I actually covered it in my last video that I'll link to right here with the whisk framework" [0:03:32]. Rather than a single fix, WHISK is a checklist of complementary levers: when an agent starts to drift, you ask which of write, isolate, select, or compress the situation calls for. Cole presents it as a level-up for any agentic workflow: "So that is the whisk framework. I hope that you can use this to take you to the next level of cloud code or really any AI coding assistant" [0:21:35].

## Part of

- [Context Engineering](./context-engineering.md) - WHISK is a practical mnemonic for the core moves of context engineering.

## Contrasts with

- [Context Rot](./context-rot.md) - WHISK is the toolbox assembled specifically to counter context rot.

## Related

- [Context Isolation](./context-isolation.md) - the "I" in WHISK: keep separate concerns in separate contexts.
- [Context Reset](./context-reset.md) - resetting the window complements WHISK's compress and select moves when a conversation degrades.
- [Global Rules](./global-rules.md) - global rules are one place written, selected context lives.

## Sources

- [I've Used Claude Code for 2,000+ Hours](../sources/ive-used-claude-code-for-2000-hours-heres-how-i-build-anything-with-it.md) - "[0:05:16] So W stands for write, I for isolate, S for select and C for compress."
- [I've Used Claude Code for 2,000+ Hours](../sources/ive-used-claude-code-for-2000-hours-heres-how-i-build-anything-with-it.md) - "[0:21:35] So that is the whisk framework. I hope that you can use this to take you to the next level of cloud code or really any AI coding assistant."
- [The Subagent Era Is Officially Here](../sources/the-subagent-era-is-officially-here-learn-this-now.md) - "[0:03:32] There's a lot of solutions to context rod. I actually covered it in my last video that I'll link to right here with the whisk framework."
