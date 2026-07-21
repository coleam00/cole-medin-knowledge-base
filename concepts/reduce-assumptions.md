---
type: concept
title: "Reduce Assumptions"
description: "Write explicit, unambiguous, non-contradictory prompts so the LLM has to guess as little as possible, which is the single biggest driver of accurate and predictable output."
tags: [prompting, clarity, specificity, ai-agents, agentic-coding]
videos: [claude-plans-gemini-designs-the-workflow-to-build-beautiful-frontends, full-guide-to-becoming-a-principled-agentic-engineer-build-anything-with-ai, my-complete-agentic-coding-workflow-to-build-anything-no-fluff-or-overengineering, how-to-properly-use-claude-code-agent-teams-full-live-build, my-top-20-lessons-from-building-100s-of-ai-agents-super-actionable, archon-beta-launch-livestream-what-you-missed, build-any-ai-agent-with-this-context-engineering-blueprint, the-3-must-have-mcp-servers-for-any-ai-coding-and-how-to-use-them, code-100x-faster-with-ai-heres-how-no-hype-full-process, pydantic-ai-deepseek-v3-the-best-ai-agent-combo, im-addicted-to-windsurf-send-help, build-a-full-stack-app-for-your-n8n-ai-agent-in-20-minutes]
created: 2026-07-21
updated: 2026-07-21
---

# Reduce Assumptions

Reducing assumptions is Cole's north-star principle for prompting a coding agent: the fewer things the model has to guess, the better and more predictable the result. "Your number one goal for any kind of planning with coding agents is to reduce the number of assumptions that your coding agent is making" [0:07:29], and "the most important part when you're first planning work with a coding agent is to reduce the number of assumptions that it is making" [0:09:29]. The reason it matters so much is that agent failures are rarely broken syntax, they are misalignment: "most of the time when a coding agent does a bad job, it's not like the code is just broken. It's that it's not aligned with what you are actually looking to build" [0:09:35].

## Why it matters

The cost of a vague instruction compounds. "one line of bad code is just one line of bad code. One line of a bad plan is maybe a 100 lines of bad code ... one bad line in a PRD, that could be a thousand bad lines of code because you have misalignment" [0:07:46]. So specificity is leverage. Be concrete about the stack, libraries, and desired output: "don't just describe what you want to build at a high level, but get into the details of the technologies that you want it to use, the different libraries, what you want the output to look like" [0:03:58]. Otherwise the agent fills the gaps itself: "it's important to give it all these details otherwise it's not really a co-pilot it's just kind of doing its own thing because you barely told it what you want" [0:14:05].

Three specific tactics recur. First, examples beat description: "Examples are so so powerful for AI coding assistance ... even better than just looking at the documentation" [0:13:19], especially since agents "love to hallucinate the way that we use these specific APIs when they don't have access to this documentation" [0:18:04]. Second, preempt known failure modes explicitly, like forcing both a login and a signup tab [0:11:00] or naming deprecated features to avoid [0:11:59]. Third, eliminate contradictions, since a self-conflicting prompt makes the model "randomly pick between one of these" [0:26:07]; Cole's own example was telling an agent to be rigid about tools while telling it to be accommodating to the user [0:27:45]. The same clarity discipline also curbs over-engineering: an unconstrained planner "created 123 to-dos ... completely overengineered" [0:27:00] when the goal was 10 to 20 tasks kept simple [0:27:45].

## Part of

- [Planning with AI](./planning-with-ai.md) and [Context Engineering](./context-engineering.md): reducing assumptions is the number-one goal of the planning phase.

## Contrasts with

- [Vibe Coding](./vibe-coding.md): loose, vibes-first prompting is the opposite posture from deliberately eliminating ambiguity.

## Related

- [Clarifying Questions](./clarifying-questions.md), [PRD-First Development](./prd-first-development.md), and [Prototype as a Coding Blueprint](./prototype-as-blueprint.md) are ways to surface and lock down assumptions before code.
- [Avoid Negative Instructions](./avoid-negative-instructions.md), [Global Rules](./global-rules.md), [Prompt Versioning](./prompt-versioning.md), [Self-Correcting Agents](./self-correction.md), [Agentic Coding](./agentic-coding.md), and [Provider Independence](./provider-independence.md).

> **Contradiction:** In most videos the goal is to *supply* detail so the agent assumes nothing. But when combining a strong planner and a strong designer, Cole deliberately withholds detail: "I specifically don't want Opus though to describe the structure of the site in any way ... because I want to rely on the strength of Gemini to do that" [0:13:28], since over-specifying "steamrolled Gemini and told it how to design the site and it did look significantly worse" [0:13:41] ([Claude Plans, Gemini Designs](../sources/claude-plans-gemini-designs-the-workflow-to-build-beautiful-frontends.md), and [My COMPLETE Agentic Coding Workflow](../sources/my-complete-agentic-coding-workflow-to-build-anything-no-fluff-or-overengineering.md)). Reconciled: reduce *ambiguity about intent*, but do not over-prescribe the parts a more capable model should own.

## Sources

- [My COMPLETE Agentic Coding Workflow to Build Anything (No Fluff or Overengineering)](../sources/my-complete-agentic-coding-workflow-to-build-anything-no-fluff-or-overengineering.md) - "[0:07:29] Your number one goal for any kind of planning with coding agents is to reduce the number of assumptions that your coding agent is making."
- [FULL Guide to Becoming a Principled Agentic Engineer (Build Anything with AI)](../sources/full-guide-to-becoming-a-principled-agentic-engineer-build-anything-with-ai.md) - "[0:09:35] most of the time when a coding agent does a bad job, it's not like the code is just broken. It's that it's not aligned with what you are actually looking to build."
- [How to Properly Use Claude Code Agent Teams (FULL LIVE BUILD)](../sources/how-to-properly-use-claude-code-agent-teams-full-live-build.md) - "[0:11:28] the number one goal of planning is to reduce the number of assumptions the coding agent is making"
- [Code 100x Faster with AI, Here's How (No Hype, FULL Process)](../sources/code-100x-faster-with-ai-heres-how-no-hype-full-process.md) - "[0:03:58] You want to be very specific with what you're looking for ... get into the details of the technologies that you want it to use, the different libraries, what you want the output to look like."
- [My Top 20 Lessons from Building 100s of AI Agents (Super Actionable)](../sources/my-top-20-lessons-from-building-100s-of-ai-agents-super-actionable.md) - "[0:26:07] This is a contradiction. The LLM is going to take these two pieces of instruction, try to balance what it wants to do, and it's going to usually just kind of randomly pick between one of these."
- [Build ANY AI Agent with this Context Engineering Blueprint](../sources/build-any-ai-agent-with-this-context-engineering-blueprint.md) - "[0:13:19] Examples are so so powerful for AI coding assistance. is even better than just looking at the documentation or doing web research."
- [The 3 MUST Have MCP Servers for Any AI Coding (and How to Use Them)](../sources/the-3-must-have-mcp-servers-for-any-ai-coding-and-how-to-use-them.md) - "[0:11:04] one really powerful thing for using AI coding assistants in general is to give examples whenever you can."
- [Claude Plans, Gemini Designs: The Workflow to Build BEAUTIFUL Frontends](../sources/claude-plans-gemini-designs-the-workflow-to-build-beautiful-frontends.md) - "[0:13:28] I specifically don't want Opus though to describe the structure of the site in any way ... because I want to rely on the strength of Gemini to do that."
- [Archon Beta Launch Livestream - What You Missed!](../sources/archon-beta-launch-livestream-what-you-missed.md) - "[0:27:45] We don't want 123 tasks. We want like 10 to 20 ... I'm telling it to not overengineer and just keep things simple"
- [I'm Addicted to Windsurf, Send Help](../sources/im-addicted-to-windsurf-send-help.md) - "[0:14:05] it's important to give it all these details otherwise it's not really a co-pilot it's just kind of doing its own thing because you barely told it what you want"
- [Build a FULL Stack App for your n8n AI Agent in 20 Minutes](../sources/build-a-full-stack-app-for-your-n8n-ai-agent-in-20-minutes.md) - "[0:11:59] sometimes Claude likes to hallucinate and use features that are deprecated so I just specified this at the very end"
- [Pydantic AI + DeepSeek V3 - The BEST AI Agent Combo](../sources/pydantic-ai-deepseek-v3-the-best-ai-agent-combo.md) - "[0:12:47] the first thing we want to do is Define the system prompt for our agent and that I am taking directly from our n8n prototype ... word for word no reason to reinvent the wheel"
