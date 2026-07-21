---
type: concept
title: "Iterative Prompting"
description: "Build complex software by prompting for a minimal baseline first and adding one change at a time to minimize hallucination."
tags: [ai-coding, prompting, iteration, workflow]
videos: [insane-new-strategy-for-building-ai-agent-apps, how-to-use-boltnew-for-free-with-local-llms-and-no-rate-limits, v0-claude-a-game-changer-for-building-ai-apps]
created: 2026-07-21
updated: 2026-07-21
---

# Iterative Prompting

Iterative prompting is the practice of building complex software incrementally, prompting for a minimal working baseline first and then layering on one change per prompt. The core advice is blunt: "the main thing that I want to give as a piece of advice here is just request it to add one thing at a time that makes it so much easier for the llm to just understand what you're doing and implement it correctly." The premise is that an LLM handed a small, well-scoped delta against a working codebase will implement it correctly far more often than one asked to produce a large, feature-rich application in a single shot.

The method is a sequence, not a single big prompt. You "start with a very basic example and then we'll build on this with prompts as we go to make it the fully robust application with authentication that I described at the start," then progressively "get a little more complicated with the requests" to improve the UI and add features like auth. Starting simple is a hallucination-control strategy: "start really simple and iteratively get more complicated to avoid the most amount of hallucinations possible and make sure that you don't have something that's broken right out the gate." Each accepted step becomes a known-good foundation, so a broken change is easy to spot and revert instead of hiding inside a large tangled diff.

Cole stresses this holds regardless of model strength. It is not a crutch for weak local models: "even with larger models like if you're using Cloud 3.5 Sonet on the commercial bolt.new this is still a good strategy to develop very complex applications by starting really simple." The technique is model-agnostic and pairs naturally with browser-based and no-code coding tools where each prompt visibly extends a running app.

## Builds on

- [Prompting Techniques for AI Coding](./ai-coding-prompting.md) - iterative prompting is one of the concrete tactics in that broader toolkit.

## Related

- [One Feature Per Prompt](./one-feature-per-prompt.md) - the same "one change at a time" rule stated as a scoping principle.
- [Planning with AI](./planning-with-ai.md) - iteration executes best against a plan that sequences the increments up front.
- [Open-Source & Local AI Coding](./open-source-ai-coding.md) - where this strategy matters most, since smaller local models hallucinate faster on large asks.

## Sources

- [INSANE New Strategy for Building AI Agent Apps](../sources/insane-new-strategy-for-building-ai-agent-apps.md) - "[0:21:11] the main thing that I want to give as a piece of advice here is just request it to add one thing at a time that makes it so much easier for the llm to just understand what you're doing and implement it correctly"
- [How to Use Bolt.new for FREE with Local LLMs (And NO Rate Limits)](../sources/how-to-use-boltnew-for-free-with-local-llms-and-no-rate-limits.md) - "[0:10:35] start really simple and iteratively get more complicated to avoid the most amount of hallucinations possible and make sure that you don't have something that's broken right out the gate"
- [V0 + Claude: A GAME CHANGER for Building AI Apps](../sources/v0-claude-a-game-changer-for-building-ai-apps.md) - "[0:02:33] so I'm going to start with a very basic example and then we'll build on this with prompts as we go to make it the fully robust application with authentication that I described at the start"
