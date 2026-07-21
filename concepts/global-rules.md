---
type: concept
title: "Global Rules"
description: "Persistent project- or user-level rule files that inject standing context and conventions into every agent run."
tags: [rules, context, conventions]
videos: [ive-used-claude-code-for-2000-hours-heres-how-i-build-anything-with-it, my-complete-agentic-coding-workflow-to-build-anything-no-fluff-or-overengineering, the-5-techniques-separating-top-agentic-engineers-right-now, anthropic-just-dropped-a-masterclass-on-building-agent-harnesses-for-large-codebases, full-guide-to-becoming-a-principled-agentic-engineer-build-anything-with-ai, context-engineering-101-the-simple-strategy-to-100x-ai-coding, context-engineering-is-the-new-vibe-coding-learn-this-now, youre-hardly-using-what-claude-code-has-to-offer-its-insane, a-complete-guide-to-claude-code-here-are-all-the-best-strategies, code-100x-faster-with-ai-heres-how-no-hype-full-process, the-official-archon-guide-10x-your-ai-coding-workflow, i-built-my-second-brain-with-claude-code-obsidian-skills-heres-how, claude-skills-arent-just-for-claude-heres-how-to-build-them-for-any-agent, the-kiro-ai-coding-hackathon-has-officially-started-build-anything-win-big-prizes, i-built-self-evolving-claude-code-memory-w-karpathys-llm-knowledge-bases]
created: 2026-07-21
updated: 2026-07-21
---

# Global Rules

Global rules are the persistent rule file (Claude's `CLAUDE.md`, Cursor rules, Windsurf rules, an `AGENTS.md`) that injects standing conventions into every agent run. Cole defines them as "our constraints and conventions that we always want our coding agent to be aware of," containing "things like the commands to run our application, our testing strategy, our logging strategy." They function as a durable system prompt: "This is essentially system prompts for your AI coding assistant... you do in the global rules so you don't have to type it out explicitly every time," so best practices are followed "without me doing anything in the prompt related to it."

Because this file loads into context every single conversation, it is [static context](./context-engineering.md) and therefore expensive, which makes leanness the cardinal rule. "the reason we don't want to just dump this all into our agents.md is this is loaded into the context of the coding agent every single conversation. And remember context is precious. So we want to keep this really concise." Cole targets "usually between 500 and 700 lines," and Anthropic warns bloat actively hurts: "Create these global rule files that are thousands of lines long. That is not a good idea. There are actually studies out there that prove that that can hurt your coding agent performance."

The scaling answer is layering, not a longer file. Sub-directory rule files scope conventions to where they matter: "you can actually have claude.md files in subdirectories," so "we're not overwhelming our coding agent with context it doesn't care about." Task-specific rules split out and get referenced on demand: "take these different rules for different task types, split them out into different markdown documents, and have your primary global rules reference these" (see [Progressive Disclosure](./progressive-disclosure.md)). Beyond conventions, global rules are where you document MCP gotchas, teach the agent how to invoke [Skills](./skills.md) and [Subagents](./subagents-pattern.md), and wire in tools like [Archon](../entities/tools/archon.md): "copy the recommended global rules... Your coding assistant now understands how to use archon for the knowledge and task management."

> **Contradiction:** On skills vs. rules for control, Cole says "In fact, a lot of my instructions here is just telling the agent how to use skills" ([Claude Skills Aren't Just for Claude](../sources/claude-skills-arent-just-for-claude-heres-how-to-build-them-for-any-agent.md), 0:14:49), yet also "if you want absolutely the most control possible, I would recommend just sticking to the claude.md" ([You're Hardly Using What Claude Code Has to Offer](../sources/youre-hardly-using-what-claude-code-has-to-offer-its-insane.md), 0:08:15). The tension is deliberate: rules give maximal control, skills give scalable capability, and the global rules file is where you bridge them.

## Part of

- [Context Engineering](./context-engineering.md) - global rules are the static-context layer of a curated window.

## Related

- [Progressive Disclosure](./progressive-disclosure.md) - keep rules lean, reference detail loaded on demand.
- [Agentic Coding](./agentic-coding.md) and [Agentic Workflow Engineering](./agentic-workflow-engineering.md) - rules steer the whole workflow.
- [Skills](./skills.md), [Slash Commands](./slash-commands.md), [Commandify Everything](./commandify-everything.md) - capabilities the global rules teach the agent to invoke.
- [Claude Code Hooks](./claude-code-hooks.md) - the deterministic lifecycle actions rules sit alongside.
- [MCP](./mcp.md) - global rules document server gotchas and usage.
- [Planning with AI](./planning-with-ai.md) - rules point the agent at planning and task files.
- [The AI Layer](./the-ai-layer.md) and [Provider Independence](./provider-independence.md) - `AGENTS.md` as a portable, cross-assistant rules standard.

## Tools

- [Claude Code](../entities/tools/claude-code.md) - `CLAUDE.md`, layerable in subdirectories.
- [Cursor](../entities/tools/cursor.md) and [Windsurf](../entities/tools/windsurf.md) - their rules files are the same concept.
- [Kiro](../entities/tools/kiro.md) - calls them "steering documents."
- [Archon](../entities/tools/archon.md) - ships recommended global rules so the assistant learns to use its knowledge and tasks.

## Sources

- [I've Used Claude Code for 2,000+ Hours](../sources/ive-used-claude-code-for-2000-hours-heres-how-i-build-anything-with-it.md) - "[0:15:39] we start with our global rules. These are our constraints and conventions that we always want our coding agent to be aware of... Usually between 500 and 700 lines long is what I go for."
- [My COMPLETE Agentic Coding Workflow to Build Anything](../sources/my-complete-agentic-coding-workflow-to-build-anything-no-fluff-or-overengineering.md) - "[0:16:42] this is loaded into the context of the coding agent every single conversation. And remember context is precious. So we want to keep this really concise."
- [The 5 Techniques Separating Top Agentic Engineers Right Now](../sources/the-5-techniques-separating-top-agentic-engineers-right-now.md) - "[0:04:57] take these different rules for different task types, split them out into different markdown documents, and have your primary global rules reference these."
- [Anthropic Just Dropped a Masterclass on Building Agent Harnesses](../sources/anthropic-just-dropped-a-masterclass-on-building-agent-harnesses-for-large-codebases.md) - "[0:05:11] Create these global rule files that are thousands of lines long. That is not a good idea. There are actually studies out there that prove that that can hurt your coding agent performance."
- [FULL Guide to Becoming a Principled Agentic Engineer](../sources/full-guide-to-becoming-a-principled-agentic-engineer-build-anything-with-ai.md) - "[0:11:26] your global rules, these are the conventions, the rules that you always want your coding agent to follow."
- [Code 100x Faster with AI](../sources/code-100x-faster-with-ai-heres-how-no-hype-full-process.md) - "[0:10:35] all the high-level instructions that you want to give to the AI coding assistant, you do in the global rules so you don't have to type it out explicitly every time."
- [Context Engineering is the New Vibe Coding](../sources/context-engineering-is-the-new-vibe-coding-learn-this-now.md) - "[0:09:59] The first file that I want to cover is our claude.md. These are the global rules for our AI coding assistant. similar to Windsurf rules or cursor rules."
- [The OFFICIAL Archon Guide](../sources/the-official-archon-guide-10x-your-ai-coding-workflow.md) - "[0:10:55] copy the recommended global rules that we have for your coding assistant. So you got one for Claude Code and then one that applies to any other AI coding assistant."
- [I Built My Second Brain with Claude Code + Obsidian + Skills](../sources/i-built-my-second-brain-with-claude-code-obsidian-skills-heres-how.md) - "[0:18:35] ask Claude specifically to go through all the tools and document any gotchas in the global rules like for Claude Code our claude.md."
- [Claude Skills Aren't Just for Claude](../sources/claude-skills-arent-just-for-claude-heres-how-to-build-them-for-any-agent.md) - "[0:04:12] the only thing we're giving to the agent right away in the system prompt or you can think of it like the global rules is the description of the capability or the skill."
- [The Kiro AI Coding Hackathon has Officially Started](../sources/the-kiro-ai-coding-hackathon-has-officially-started-build-anything-win-big-prizes.md) - "[0:04:33] your steering documents. These are global rules. That's what Kiro calls global rules."
- [I Built Self-Evolving Claude Code Memory w/ Karpathy's LLM Knowledge Bases](../sources/i-built-self-evolving-claude-code-memory-w-karpathys-llm-knowledge-bases.md) - "[0:07:07] the agents.md. So this is like global rules for your coding agent."
