---
type: concept
title: "Claude Code Hooks"
description: "Lifecycle hooks that run deterministic code at defined points in a Claude Code session to enforce behavior the model can't be trusted to."
tags: [hooks, automation, claude-code]
videos: [pydantic-ai-20-the-new-best-way-to-build-ai-agents-is-composing-capabilities, google-just-dropped-a-masterclass-on-agentic-engineering-its-so-good, harness-engineering-what-separates-top-agentic-engineers-right-now, anthropic-just-dropped-a-masterclass-on-building-agent-harnesses-for-large-codebases, i-built-self-evolving-claude-code-memory-w-karpathys-llm-knowledge-bases, full-guide-build-your-own-ai-second-brain-with-claude-code, youre-hardly-using-what-claude-code-has-to-offer-its-insane, ralph-wiggum-is-the-final-evolution-of-vibe-coding-heres-what-comes-next, build-a-rag-ai-agent-with-real-time-source-validation-copilotkit-pydantic-ai, a-complete-guide-to-claude-code-here-are-all-the-best-strategies]
created: 2026-07-21
updated: 2026-07-21
---

# Claude Code Hooks

Claude Code hooks are pieces of your own code that fire at defined points in a coding-agent session, giving you "a very powerful way to add deterministic control to Claude Code's behavior." Instead of hoping the model behaves, you attach a script to a lifecycle event: "before we use a tool, after we use a tool, after we use a sub agent, we can have our own custom command that runs." The value is that the action is deterministic, it happens by code, not by the model's discretion, which is exactly what you want "for the sake of security or guiding the agent properly."

The most familiar hook is the **pre-tool-use** hook, "a piece of code that's going to trigger before the coding agent executes any tool call... this is where we can build in security things like not reading files... or removing directories in a very destructive way." Its natural partner is a **stop / validation** hook: "when the coding agent says it's done... I want to deterministically run a set of tests like are the unit tests, the linting, the type checking, is all that really passing?" **Session-start** hooks load context automatically, "a start hook can load team specific contexts dynamically. So every dev gets the right setup without manual configuration", and in Cole's Second Brain that means the soul, user, and memory files are pulled "right into the context of our Claude Code up front through a session start hook." **Pre-compact** and **session-end** hooks catch the moment context is about to be lost and flush it somewhere durable: "whenever we're about to lose context... we want to send the latest messages from Claude Code into another large language model to process and create the summary." Hooks can now also be scoped per subagent rather than applying globally.

Cole's key reframe, echoing Anthropic, is that hooks are not just guardrails. "Most teams think of hooks as scripts that prevent Claude from doing something wrong... But their more valuable use is continuous improvement." Because a hook can run arbitrary code at the seams of a session, "you can use hooks to make your entire AI layer, your entire setup self-improving." Taken to its extreme, a single stop hook is what turns an agent into an autonomous loop: "we're going to detect when the agent is trying to stop running and we're going to force it to continue... take the output from the agent and feed it back into itself as the input for the next run."

## Part of

- [The AI Layer](./the-ai-layer.md) - hooks are one of its core deterministic components, alongside rules, commands, and skills.
- [AI Coding Harness](./ai-coding-harness.md) - hooks are the wiring that makes a harness enforce and improve itself.

## Implemented by

- [Claude Code](../entities/tools/claude-code.md) - exposes pre-tool-use, stop, session-start, pre-compact, and session-end hooks.
- [CopilotKit](../entities/tools/copilotkit.md) - its front-end `useAgent` hook exposes a securely backend-hosted agent to the UI.

## Related

- [Deterministic Workflows](./deterministic-workflows.md) - hooks are how you pin known steps into code instead of the model.
- [Validation](./validation.md) - the stop hook that deterministically runs tests, linting, and type checks.
- [Global Rules](./global-rules.md) - the standing instructions a session-start hook can load automatically.
- [Self-Evolving Memory](./self-evolving-memory.md) and [Memory Systems](./memory-systems.md) - pre-compact and session-end hooks flush context into durable memory.
- [System Evolution](./system-evolution.md) - hooks as the mechanism for a continuously self-improving setup.
- [Capabilities Over Tools](./capabilities-over-tools.md) - hooks are one layer a capability bundles.
- [Skills](./skills.md) - the other deterministic building block hooks sit beside.
- [Subagents Pattern](./subagents-pattern.md) - hooks can now be defined at the subagent level.
- [Agentic Experiences](./agentic-experiences.md) - hooks power richer, safer agent-driven UX.

## Sources

- [A Complete Guide to Claude Code - Here are ALL the Best Strategies](../sources/a-complete-guide-to-claude-code-here-are-all-the-best-strategies.md) - "[0:30:17] Claude hooks, which is a very powerful way to add deterministic control to Claude Code's behavior."
- [Harness Engineering: What Separates Top Agentic Engineers Right Now](../sources/harness-engineering-what-separates-top-agentic-engineers-right-now.md) - "[0:11:43] I also like having some kind of stop validation hook. So when the coding agent says it's done... I want to deterministically run a set of tests"
- [Anthropic Just Dropped a Masterclass on Building Agent Harnesses (for Large Codebases)](../sources/anthropic-just-dropped-a-masterclass-on-building-agent-harnesses-for-large-codebases.md) - "[0:11:08] Most teams think of hooks as scripts that prevent Claude from doing something wrong... But their more valuable use is continuous improvement."
- [I Built Self-Evolving Claude Code Memory w/ Karpathy's LLM Knowledge Bases](../sources/i-built-self-evolving-claude-code-memory-w-karpathys-llm-knowledge-bases.md) - "[0:12:13] this entire system is only driven by Claude Code hooks. That's the beautifully simple part about it."
- [Full Guide - Build Your Own AI Second Brain with Claude Code](../sources/full-guide-build-your-own-ai-second-brain-with-claude-code.md) - "[0:11:01] we're bringing them right into the context of our Claude Code up front through a session start hook. So, we automatically load the soul, user, and memory.mds"
- [Ralph Wiggum is the Final Evolution of Vibe Coding (Here's What Comes Next)](../sources/ralph-wiggum-is-the-final-evolution-of-vibe-coding-heres-what-comes-next.md) - "[0:01:22] we're going to detect when the agent is trying to stop running and we're going to force it to continue... take the output from the agent and feed it back into itself as the input for the next run."
- [Pydantic AI 2.0: The New Best Way to Build AI Agents is Composing Capabilities](../sources/pydantic-ai-20-the-new-best-way-to-build-ai-agents-is-composing-capabilities.md) - "[0:02:46] capabilities are a lot more than just the arm of the agent, aka the tools. It's also the instructions and the settings and the hooks and the guardrails"
- [You're Hardly Using What Claude Code Has to Offer, it's Insane](../sources/youre-hardly-using-what-claude-code-has-to-offer-its-insane.md) - "[0:07:11] We can also define hooks at the sub agent level. Before the last couple of months, when you built a hook, it had to be used by Claude Code all of the time."
- [Google Just Dropped a Masterclass on Agentic Engineering (It's SO Good)](../sources/google-just-dropped-a-masterclass-on-agentic-engineering-its-so-good.md) - "[0:08:07] It's your hooks like the deterministic actions you want in your life cycle your skills."
- [Build a RAG AI Agent with REAL-TIME Source Validation (CopilotKit + Pydantic AI)](../sources/build-a-rag-ai-agent-with-real-time-source-validation-copilotkit-pydantic-ai.md) - "[0:04:30] it gives us this agent object. And so we have direct access to the agent in our front end but the agent is still running securely in a backend API."
