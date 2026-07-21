---
type: concept
title: "Intent Engineering"
description: "Shifting the engineer's job from writing code to precisely expressing intent that an AI agent implements."
tags: [intent-engineering, context-engineering, spec-driven-development, agentic-coding]
videos: [is-software-engineering-finally-dead]
created: 2026-07-21
updated: 2026-07-21
---

# Intent Engineering

Intent engineering reframes the software engineer's job: instead of writing the code yourself, you precisely express *what* you want built and *how you will know it is correct*, then let an AI agent produce the implementation. As Cole frames it, "the new term intent engineering showing up on the internet recently. It's really just a lot of software engineering principles put into a package to apply to AI" [0:02:46]. The skill is not new. It is the discipline of specification, decomposition, and acceptance criteria, relocated from the code editor to the prompt.

Because the agent, not the human, types the code, the leverage moves entirely to the clarity of the intent handed off. A vague request produces plausible but wrong output; a sharp one, with explicit success criteria the agent can check itself against, produces something closer to shippable on the first pass. Cole stresses aligning on the target before any code is written: "we also want to be very clear on things like the success criteria, how the agent can validate its own work, making sure we're super aligned on what we're building" [0:09:43]. Intent engineering is therefore inseparable from validation: the definition of "done" is part of the intent, not an afterthought.

## Builds on

- [Context Engineering](./context-engineering.md) - intent engineering is the human-facing half of context engineering: you package requirements, constraints, and success criteria so the agent has everything it needs.

## Related

- [Clarifying Questions](./clarifying-questions.md) - surfacing hidden assumptions is how you sharpen intent before the agent commits to an implementation.
- [Validation](./validation.md) - the success criteria that let an agent check its own work are a core part of the intent you express.
- [The Evolution of AI Coding](./the-evolution-of-ai-coding.md) - intent engineering is the latest stage in the shift from writing code to directing agents.

## Sources

- [Is Software Engineering Finally Dead?](../sources/is-software-engineering-finally-dead.md) - "[0:02:46] the new term intent engineering showing up on the internet recently. It's really just a lot of software engineering principles put into a package to apply to AI"
- [Is Software Engineering Finally Dead?](../sources/is-software-engineering-finally-dead.md) - "[0:09:43] we also want to be very clear on things like the success criteria, how the agent can validate its own work, making sure we're super aligned on what we're building"
