---
type: concept
title: "The Evolving Role of the Software Engineer"
description: "The argument that software engineering is not dying but shifting: as agents absorb the typing, the human owns requirements, architecture, orchestration, and review."
tags: [software-engineering, commentary, ai-coding, workflow]
videos: [is-software-engineering-finally-dead, the-way-we-use-ai-will-completely-change-in-2026-hot-takes]
created: 2026-07-21
updated: 2026-07-21
---

# The Evolving Role of the Software Engineer

The role of the software engineer is not disappearing, it is moving up a layer: the agent absorbs the typing, and the human keeps everything that surrounds the typing. Cole states the thesis plainly - "software engineering is going to evolve significantly over the next couple of years, but it is not going away. Maybe we will need less engineers, but the role is still going to be very important" [0:05:21]. What remains is the part that was always the hard part: "Someone has to prompt the clouds. Talk to the customers. This is very important. Coordinate with other teams. Decide what to build next. Engineering is changing and great engineers are more important than ever." [0:03:44]

The positive name for the new role is systems architect. "we are finally going to get to the point where we are not the coders. We delegate that entirely to our coding agents and we are the system architects." [0:04:50] That job decomposes into three duties: "We define our objectives and the system that our agents will operate under. And then we orchestrate by delegating the coding to our agents. And then we validate the outputs" [0:05:24] - define, orchestrate, validate. It is the same shape as [The PIV Loop](./the-piv-loop.md), with the human holding the planning and validation ends of the sandwich while implementation is handed off.

The skill ladder tracks that shift. [Prompt Engineering](./prompt-engineering.md) is wording a single request well; [Context Engineering](./context-engineering.md) builds the whole system of context an agent needs to plausibly succeed; [Intent Engineering](./intent-engineering.md) adds explicit success criteria and self-validation. Each rung looks more like classical software engineering, not less, which is exactly the point: everything except the code becomes the human's responsibility.

The caution attached to this is agency. Cole's advice is to never vibe anything into production, to keep technical craft sharp, and to use the coding agent as an educator so you never lose your understanding of the codebase - because the engineers who hand over judgment entirely have no fallback when the agent is wrong. The endgame he predicts (shipping code you have never read, trusting your validation system) is earned by building that system first, not assumed.

## Builds on

- [The Evolution of AI Coding](./the-evolution-of-ai-coding.md) - the landscape shift that forces the role change.
- [Context Engineering](./context-engineering.md) and [Intent Engineering](./intent-engineering.md) - the skills that replace hand-coding.

## Contrasts with

- [Vibe Coding](./vibe-coding.md) - abdicating the role rather than evolving it.

## Related

- [The PIV Loop](./the-piv-loop.md) - the human keeps plan and validate, delegates implement.
- [The Five Levels of AI Coding Autonomy](./five-levels-of-ai-coding-autonomy.md) - how far up the delegation ladder to climb.
- [Human in the Loop](./human-in-the-loop.md), [Validation](./validation.md), [Code Review](./code-review.md) - the duties that stay human.
- [Parallel Agentic Coding](./parallel-agentic-coding.md) - orchestration as the day-to-day surface of the new role.
- [Agentic Coding](./agentic-coding.md), [The AI Layer](./the-ai-layer.md) - the practice and the system the architect designs.
- [Cole Medin](../entities/people/cole-medin.md) - his own arc from AI-refusing hand-coder to delegating all implementation.
- [Dario Amodei](../entities/people/dario-amodei.md) - CEO of Anthropic, cited as the highest-profile source of the 'AI will write 90% of code' and 'software engineers go extinct in 2026' predictions Cole pushes back on.

## Sources

- [Is Software Engineering Finally Dead?](../sources/is-software-engineering-finally-dead.md) - "[0:03:44] Someone has to prompt the clouds. Talk to the customers. This is very important. Coordinate with other teams. Decide what to build next. Engineering is changing and great engineers are more important than ever."
- [Is Software Engineering Finally Dead?](../sources/is-software-engineering-finally-dead.md) - "[0:05:21] software engineering is going to evolve significantly over the next couple of years, but it is not going away. Maybe we will need less engineers, but the role is still going to be very important"
- [The Way We Use AI Will Completely Change in 2026 (Hot Takes)](../sources/the-way-we-use-ai-will-completely-change-in-2026-hot-takes.md) - "[0:04:50] we are finally going to get to the point where we are not the coders. We delegate that entirely to our coding agents and we are the system architects."
- [The Way We Use AI Will Completely Change in 2026 (Hot Takes)](../sources/the-way-we-use-ai-will-completely-change-in-2026-hot-takes.md) - "[0:05:24] We define our objectives and the system that our agents will operate under. And then we orchestrate by delegating the coding to our agents. And then we validate the outputs"
