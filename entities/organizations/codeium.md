---
type: entity
subtype: organization
title: "Codeium"
description: "The company behind Windsurf, which coined and marketed the 'AI flows' / flow-state framing for AI IDEs."
resource: "https://codeium.com"
tags: [organization, ai-coding, ide, positioning]
videos: [im-addicted-to-windsurf-send-help]
created: 2026-07-21
updated: 2026-07-21
---

# Codeium

Codeium is the company that built [Windsurf](../tools/windsurf.md), and in Cole's coverage it is as much a positioning story as an engineering one: "codium the creators of wind surf have done a very good job marketing the platform and really framing what makes it revolutionary" ([0:01:47]). The framing they coined is flows, the claim that the previous generation split developers between two disconnected modes, writing code yourself and consulting an agent, and that the IDE should collapse them into one shared timeline where the agent sees every change you make and you see every change it makes.

That framing is Codeium's contribution to [The Evolution of AI Coding](../../concepts/the-evolution-of-ai-coding.md): manual coding, then co-pilots doing autocomplete in 2022, then agents in 2024 that were powerful but came with long waits, inconsistent results, and a disjointed editor experience, and then flows. What made it land is that the naming pointed at a real [AI Coding Assistant UX](../../concepts/ai-coding-ux.md) problem rather than a benchmark. Windsurf's granular accept and reject of changes across files, @-references for scoping context, and function-level Refactor and Explain buttons are all expressions of it, and they keep a tight [Human in the Loop](../../concepts/human-in-the-loop.md) instead of trading control for autonomy.

Cole is candid that the marketing outruns the output: the tool does not produce production-ready code on its own, and the habits that make it pay off are ordinary [Context Engineering](../../concepts/context-engineering.md) discipline, starting fresh conversations when [context rot](../../concepts/context-rot.md) sets in, sending one request at a time, defining the tech stack up front, and switching to a [reasoning model](../../concepts/reasoning-models.md) like [o1](../tools/o1.md) when the default model gets stuck. Codeium matters here as the vendor that named the experience the whole category then chased, making it a useful marker for how [AI Coding Assistant](../../concepts/ai-coding-assistant.md) products compete on interaction design rather than model quality.

## Tools

- [Windsurf](../tools/windsurf.md) - Codeium's AI coding IDE, built around the flow-state experience that fuses co-pilot and agent into one surface.

## Contrasts with

- [Cursor](../tools/cursor.md) - The other leading AI IDE of the same era, competing on the same in-codebase editing ground.
- [GitHub Copilot](../tools/github-copilot.md) - The autocomplete-era co-pilot that flows was explicitly positioned against.

## Related

- [AI Coding Assistant UX Patterns](../../concepts/ai-coding-ux.md) - Interaction patterns of coding assistants: streamed output, inline versus manual suggestions, and scoped context.
- [The Evolution of AI Coding](../../concepts/the-evolution-of-ai-coding.md) - How AI coding assistants moved from novelty to daily driver.
- [AI Coding Assistant](../../concepts/ai-coding-assistant.md) - A tool that generates or completes code from short prompts and applies targeted edits.
- [AI Coding Harness](../../concepts/ai-coding-harness.md) - The surrounding scaffolding that turns a raw model into a reliable coding system.
- [Human in the Loop](../../concepts/human-in-the-loop.md) - Keeping a human as the approver and steerer of agentic work.
- [Context Engineering](../../concepts/context-engineering.md) - Deliberately curating exactly what goes into an LLM's limited context window.
- [Context Rot](../../concepts/context-rot.md) - Output quality degrading as the context window fills with stale, accumulated information.
- [Model Selection](../../concepts/model-selection.md) - Choosing the right LLM per task by trading off quality, speed, and cost.
- [Agentic Coding](../../concepts/agentic-coding.md) - Letting an AI agent drive development end-to-end with human steering.

## Sources

- [I'm Addicted to Windsurf, Send Help](../../sources/im-addicted-to-windsurf-send-help.md) - "[0:01:47] codium the creators of wind surf have done a very good job marketing the platform and really framing what makes it revolutionary"
