---
type: concept
title: "Clarifying Questions"
description: "Having the agent ask targeted questions up front to infer intent and reduce assumptions before it plans or builds."
tags: [clarify, intent, planning, agentic-coding, prompting]
videos: [full-guide-to-becoming-a-principled-agentic-engineer-build-anything-with-ai, pi-coding-agent-archon-build-any-ai-coding-workflow-no-claude-code-bloat, my-complete-agentic-coding-workflow-to-build-anything-no-fluff-or-overengineering, how-to-properly-use-claude-code-agent-teams-full-live-build, build-your-first-voice-ai-agent-in-20-minutes-with-livekit-open-source, i-built-my-claude-code-subagents-dream-team-to-create-any-ai-agent, build-any-ai-agent-with-this-context-engineering-blueprint, lets-settle-the-o3-mini-vs-r1-debate-for-coding-once-and-for-all, the-king-of-no-code-ai-agent-builders, chatgpt-teaches-the-secrets-to-financial-freedom]
created: 2026-07-21
updated: 2026-07-21
---

# Clarifying Questions

Clarifying questions is the technique of forcing the agent to interrogate you before it writes anything, so it can infer intent instead of guessing. Cole calls it the highest-leverage move in the whole workflow: "the most powerful strategy here... is to have the coding agent ask you questions. Like we will specifically ask it to ask us questions." Concretely, the instruction is: "before you write anything ask me clarifying questions one at a time using the ask user question tool."

The mechanism is assumption removal. Each answered question collapses an unknown the agent would otherwise have filled in blindly: "Every single question that we answer here is removing an assumption from the coding agent. And because it's multiple choice and usually one of the options it presents here is good. We can blitz through this really quickly." The volume matters, Cole deliberately sets a high bar: "I'm not happy unless it's asking me at least 10 questions here." The surprising value is in the questions you did not know to ask: "a lot of times it'll ask questions that I didn't even really think I needed to. Like, it's making some other kind of assumption that I didn't even realize I had to specify."

In an engineered workflow, this becomes a dedicated stage. Cole opens the PIV loop with "a clarification phase... we just want to have the coding agent ask us a few questions, make sure it understands our request going into this piv loop." A related trick is to ask the agent to score its own certainty and then close the gap: "what would it take to get to a 10 out of 10 confidence score?", after which "it'll ask me a couple of follow-up questions to then adjust the PRP further." The same pattern shows up in production agents, which withhold a tool call until every required value is gathered from the user: "the agent will have that conversation with the user getting all those values and only continuing when it has every single one of these required entities."

## Prerequisites

- [Human in the Loop](./human-in-the-loop.md) - clarifying questions is the front-loaded human checkpoint.

## Part of

- [The PIV Loop](./the-piv-loop.md) - clarification is the opening phase before Plan, Implement, Validate.
- [Planning with AI](./planning-with-ai.md) and [PRD-First Development](./prd-first-development.md) - clarification feeds the plan or PRD.

## Related

- [Reduce Assumptions](./reduce-assumptions.md) - the underlying goal; each answer removes one assumption.
- [Intents and Entities](./intents-and-entities.md) - production agents clarify until every required entity is filled.
- [Reasoning Models](./reasoning-models.md) - stronger reasoning infers unstated needs from a simple prompt.
- [Prompt Engineering](./prompt-engineering.md) - the instruction that triggers the questioning behavior.
- [Rapid Prototyping](./rapid-prototyping.md) - clarify early to avoid rebuilding on wrong assumptions.
- [Tool Calling](./tool-use.md) - the "ask user question" tool that renders questions as multiple choice.

## Tools

- [Claude Code](../entities/tools/claude-code.md) - ships a built-in "ask user question" tool for fast multiple-choice clarification.
- [Archon](../entities/tools/archon.md) - opens builds with a clarification phase before setting up tasks.
- [Pi](../entities/tools/pi-coding-agent.md) - runs the clarification step at the start of the PIV loop.

## Sources

- [FULL Guide to Becoming a Principled Agentic Engineer](../sources/full-guide-to-becoming-a-principled-agentic-engineer-build-anything-with-ai.md) - "[0:17:13] before you write anything ask me clarifying questions one at a time using the ask user question tool."
- [How to Properly Use Claude Code Agent Teams (FULL LIVE BUILD)](../sources/how-to-properly-use-claude-code-agent-teams-full-live-build.md) - "[0:12:57] a lot of times it'll ask questions that I didn't even really think I needed to. Like, it's making some other kind of assumption that I didn't even realize I had to specify."
- [My COMPLETE Agentic Coding Workflow to Build Anything](../sources/my-complete-agentic-coding-workflow-to-build-anything-no-fluff-or-overengineering.md) - "[0:10:19] Every single question that we answer here is removing an assumption from the coding agent... We can blitz through this really quickly."
- [Pi Coding Agent + Archon: Build ANY AI Coding Workflow](../sources/pi-coding-agent-archon-build-any-ai-coding-workflow-no-claude-code-bloat.md) - "[0:11:57] I start with a clarification phase... make sure it understands our request going into this piv loop here."
- [Build ANY AI Agent with this Context Engineering Blueprint](../sources/build-any-ai-agent-with-this-context-engineering-blueprint.md) - "[0:19:45] What I can do is literally say, what would it take to get to a 10 out of 10 confidence score?"
- [I Built My Claude Code Subagents DREAM TEAM to Create Any AI Agent](../sources/i-built-my-claude-code-subagents-dream-team-to-create-any-ai-agent.md) - "[0:01:44] that's going to ask some clarifying questions understand our requirements and then set up all the tasks in archon."
- [The KING of No Code AI Agent Builders?!](../sources/the-king-of-no-code-ai-agent-builders.md) - "[0:10:28] the agent will have that conversation with the user getting all those values and only continuing when it has every single one of these required entities."
- [Build Your First Voice AI Agent in 20 Minutes with LiveKit](../sources/build-your-first-voice-ai-agent-in-20-minutes-with-livekit-open-source.md) - "[0:08:38] if any of these arguments it doesn't actually know yet from our conversation, then it will clarify with us."
- [Let's Settle the o3-mini Vs. R1 Debate for Coding](../sources/lets-settle-the-o3-mini-vs-r1-debate-for-coding-once-and-for-all.md) - "[0:07:32] it took this simple prompt and reasoned better about what I would actually need."
- [ChatGPT Teaches the Secrets to Financial Freedom!?](../sources/chatgpt-teaches-the-secrets-to-financial-freedom.md) - "[0:12:07] you can even drill down on certain things tell me more about the real estate investing part."
