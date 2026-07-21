---
type: concept
title: "One Feature Per Prompt"
description: "Scoping each AI coding prompt to a single feature so the model stays focused and produces smaller, reviewable, higher-quality changes."
tags: [prompting, agentic-coding, scoping, focus]
videos: [code-100x-faster-with-ai-heres-how-no-hype-full-process]
created: 2026-07-21
updated: 2026-07-21
---

# One Feature Per Prompt

One feature per prompt is the discipline of scoping each request to a coding agent to a single feature or change, rather than bundling many requirements into one instruction. Cole calls it a rule: "the important thing that it covers here is that golden rule to only ask for one change at a time." Kept narrow, the agent stays focused and returns a smaller, more reviewable diff, which is easier to verify and correct than a sprawling multi-feature change.

The payoff is quality. From experience across hundreds of builds: "I usually find that it's best to just ask it to do one new feature or implement one new thing per prompt that I give it. Much better results." The mechanism is the same one behind context discipline generally, a model asked to juggle several loosely related requirements tends to confuse itself and hallucinate, whereas a single crisp objective keeps every token of the response pointed at one target. Smaller changes also keep a human meaningfully in the loop, since each unit of work is small enough to actually read.

This is the scoping-side statement of the same idea that [Iterative Prompting](./iterative-prompting.md) expresses as a sequence and that [Phases of Work](./phases-of-work.md) expresses at the level of a whole build: never let the agent do too much at once. It is a foundational habit of [Agentic Coding](./agentic-coding.md) and a direct application of [Context Engineering](./context-engineering.md), where protecting the context window from overload is the whole game.

## Part of

- [Agentic Coding](./agentic-coding.md) - one of the core working habits of building with coding agents.

## Related

- [Context Engineering](./context-engineering.md) - narrow scope keeps the context window lean and focused, the underlying reason this works.
- [Iterative Prompting](./iterative-prompting.md) - the same "one change at a time" rule applied across a whole build sequence.
- [Phases of Work](./phases-of-work.md) - the same principle scaled up: one coherent chunk per agent session.
- [Granular Task Management](./granular-task-management.md) - Breaking a large request into small focused tasks on a shared, persistent task board the agent works through one at a time, so its plan stays visible and steerable.

## Sources

- [Code 100x Faster with AI, Here's How (No Hype, FULL Process)](../sources/code-100x-faster-with-ai-heres-how-no-hype-full-process.md) - "[0:03:10] I usually find that it's best to just ask it to do one new feature or implement one new thing per prompt that I give it. Much better results."
- [Code 100x Faster with AI, Here's How (No Hype, FULL Process)](../sources/code-100x-faster-with-ai-heres-how-no-hype-full-process.md) - "[0:25:34] the important thing that it covers here is that golden rule to only ask for one change at a time."
