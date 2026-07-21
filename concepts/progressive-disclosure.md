---
type: concept
title: "Progressive Disclosure"
description: "Loading context, skills, and tools on demand only when a task needs them instead of front-loading everything into the context window."
tags: [progressive-disclosure, context-engineering, skills, on-demand-context]
videos: [pydantic-ai-20-the-new-best-way-to-build-ai-agents-is-composing-capabilities, finally-an-open-standard-for-the-karpathy-llm-wiki-is-here, google-just-dropped-a-masterclass-on-agentic-engineering-its-so-good, anthropic-just-dropped-a-masterclass-on-building-agent-harnesses-for-large-codebases, the-next-evolution-of-ai-coding-is-harnesses-heres-how-to-build-them, i-built-self-evolving-claude-code-memory-w-karpathys-llm-knowledge-bases, ive-used-claude-code-for-2000-hours-heres-how-i-build-anything-with-it, build-beautiful-diagrams-with-claude-code-full-workflow, my-complete-agentic-coding-workflow-to-build-anything-no-fluff-or-overengineering, turn-claude-code-into-your-full-engineering-team-with-subagents, claude-skills-arent-just-for-claude-heres-how-to-build-them-for-any-agent, i-built-my-second-brain-with-claude-code-obsidian-skills-heres-how, your-ai-coding-workflow-needs-this-new-agent-browser-cli, the-5-techniques-separating-top-agentic-engineers-right-now, ai-exploded-in-2025-heres-everything-that-happened, the-way-we-use-ai-will-completely-change-in-2026-hot-takes, the-big-problem-with-mcp-servers-and-the-solution]
created: 2026-07-21
updated: 2026-07-21
---

# Progressive Disclosure

Progressive disclosure is the practice of giving an agent a short description of a capability up front and letting it load the full context, skill, or tool only when a task actually requires it, instead of front-loading everything into the context window. Cole describes the mechanic directly: "the beautifully simple power of skills is the idea of progressive disclosure. Instead of giving all the tools up front to our agent like MCP servers, we are allowing our agent to discover the capabilities over time as it actually needs them" [0:04:12]. The payoff is scale without overwhelm: "we can give it dozens, maybe even hundreds of capabilities and not overwhelm the LLM because it only has to really dig into and leverage the ones that it needs based on the user's current prompt" [0:10:45].

The governing heuristic is "just in time, not just in case": "Load your context just in time, not just in case. And what I mean by that is if you're not 100% confident that a piece of information is important to your coding agent right now, then you shouldn't bother loading it" [0:15:35]. This directly attacks context rot, since a bloated window degrades reasoning. It is layered. A skill exposes a one-line description first, a fuller `SKILL.md` second, and referenced files third: "within the skill itself, we even have other files. This is the third layer of progressive disclosure" [0:10:45]. The same pattern recurs across the stack. On-demand rules load only for the part of the codebase in play: "if you are working on the front end then you can read this file... this is essentially progressive disclosure. We have different layers of context that the agent can discover over time" [0:16:56]. An LLM wiki works the same way through its index: "the index tells it the knowledge it has and then it can read the full document if it's appropriate" [0:04:58]. It is also the answer to MCP tool bloat, replacing dumped tool definitions with a searchable folder: "It's a folder that the agent can search through in real time, discovering the capabilities as it needs" [0:04:37]. Cole calls this "very scalable" [0:16:23] and expects it to define how agents are built into 2026.

## Part of

- [Context Engineering](./context-engineering.md) - progressive disclosure is a core context-engineering tactic for keeping the window lean while capabilities grow.

## Contrasts with

- [The Problems With MCP Servers](./mcp-problems.md) - dumping many tool definitions up front is the anti-pattern progressive disclosure replaces.
- [Model Context Protocol (MCP)](./mcp.md) - classic MCP loads all tool definitions eagerly; progressive disclosure loads them on demand instead.

## Implemented by

- [Skills](./skills.md) - the canonical mechanism: a short description surfaces first, the full workflow loads only when needed.
- [Capabilities Over Tools](./capabilities-over-tools.md) - Pydantic AI capabilities apply progressive disclosure so an agent can hold hundreds of them.
- [The LLM Wiki](./the-llm-wiki.md) - the wiki index is a progressive-disclosure entry point into a large knowledge base.
- [Code Execution](./code-execution.md) - loading tool definitions as executable code the agent calls on demand is a progressive-disclosure alternative to eager tool schemas.

## Tools

- [Claude Code](../entities/tools/claude-code.md) - Claude Code skills are Cole's reference implementation of progressive disclosure.

## Related

- [Global Rules](./global-rules.md) - a reference section in global rules points to on-demand context loaded per task type.
- [Agentic Search](./agentic-search.md) - the agent searches a folder in real time to discover capabilities as it needs them.
- [Commandify Everything](./commandify-everything.md) - commands and skills both keep the base context small until invoked.
- [Prime Command](./prime-command.md) - priming loads a lean high-level overview first, deferring detail until needed.
- [The AI Layer](./the-ai-layer.md) - progressive disclosure is a structural principle of the reusable AI layer Cole builds on top of a codebase.

## Sources

- [Claude Skills Aren't Just for Claude](../sources/claude-skills-arent-just-for-claude-heres-how-to-build-them-for-any-agent.md) - "[0:04:12] the beautifully simple power of skills is the idea of progressive disclosure. Instead of giving all the tools up front to our agent like MCP servers, we are allowing our agent to discover the capabilities over time as it actually needs them."
- [I've Used Claude Code for 2,000+ Hours](../sources/ive-used-claude-code-for-2000-hours-heres-how-i-build-anything-with-it.md) - "[0:15:35] Load your context just in time, not just in case. And what I mean by that is if you're not 100% confident that a piece of information is important to your coding agent right now, then you shouldn't bother loading it."
- [Pydantic AI 2.0: Composing Capabilities](../sources/pydantic-ai-20-the-new-best-way-to-build-ai-agents-is-composing-capabilities.md) - "[0:10:45] we can give it dozens, maybe even hundreds of capabilities and not overwhelm the LLM because it only has to really dig into and leverage the ones that it needs based on the user's current prompt"
- [Finally, an Open Standard for the Karpathy LLM Wiki is HERE](../sources/finally-an-open-standard-for-the-karpathy-llm-wiki-is-here.md) - "[0:04:58] This is like progressive disclosure like skills where the index tells it the knowledge it has and then it can read the full document if it's appropriate."
- [Google Just Dropped a Masterclass on Agentic Engineering](../sources/google-just-dropped-a-masterclass-on-agentic-engineering-its-so-good.md) - "[0:17:10] skills allow the agent to remain a lightweight generalist that flexes into specialist roles on demand through progressive disclosure."
- [Anthropic's Masterclass on Building Agent Harnesses](../sources/anthropic-just-dropped-a-masterclass-on-building-agent-harnesses-for-large-codebases.md) - "[0:16:02] Skill solve this through progressive disclosure. So we're offloading specialized workflows and domain knowledge and we load it when we actually need it."
- [The Next Evolution of AI Coding Is Harnesses](../sources/the-next-evolution-of-ai-coding-is-harnesses-heres-how-to-build-them.md) - "[0:19:26] We don't want to load the entire workflow into context for the coding agent. That's way too much."
- [I Built Self-Evolving Claude Code Memory](../sources/i-built-self-evolving-claude-code-memory-w-karpathys-llm-knowledge-bases.md) - "[0:05:32] we have the index. So this file describes to the agent here are all the different folders and resources that you have access to. So it uses this as a starting point"
- [My COMPLETE Agentic Coding Workflow to Build Anything](../sources/my-complete-agentic-coding-workflow-to-build-anything-no-fluff-or-overengineering.md) - "[0:16:56] this is essentially progressive disclosure. We have different layers of context that the agent can discover over time"
- [Turn Claude Code into Your Full Engineering Team with Subagents](../sources/turn-claude-code-into-your-full-engineering-team-with-subagents.md) - "[0:06:51] it's not like we're just dumping 91 tool definitions directly into our coding agent. That would not be contexts efficient."
- [I Built My Second Brain with Claude Code + Obsidian + Skills](../sources/i-built-my-second-brain-with-claude-code-obsidian-skills-heres-how.md) - "[0:10:45] within the skill itself, we even have other files. This is the third layer of progressive disclosure"
- [The BIG Problem with MCP Servers (and the Solution!)](../sources/the-big-problem-with-mcp-servers-and-the-solution.md) - "[0:04:37] It's a folder that the agent can search through in real time, discovering the capabilities as it needs."
- [The 5 Techniques Separating Top Agentic Engineers Right Now](../sources/the-5-techniques-separating-top-agentic-engineers-right-now.md) - "[0:07:12] whatever it takes to make sure that you have access to all the context you need, but not all up front"
- [AI Exploded in 2025](../sources/ai-exploded-in-2025-heres-everything-that-happened.md) - "[0:15:09] it's this idea of progressive disclosure where we only give capabilities to our agents when it actually needs them. So we save a lot of context up front."
- [The Way We Use AI Will Completely Change in 2026](../sources/the-way-we-use-ai-will-completely-change-in-2026-hot-takes.md) - "[0:08:44] we have a lot of capabilities for an agent, but we don't actually give all of them to the agent upfront. Instead, we allow the agent to discover the capabilities and then leverage them in a more flexible way."
- [Build BEAUTIFUL Diagrams with Claude Code](../sources/build-beautiful-diagrams-with-claude-code-full-workflow.md) - "[0:08:48] one of the files that I referenced in the reference folder of the skill... is the color palette."
- [Your AI Coding Workflow NEEDS This New Agent Browser CLI](../sources/your-ai-coding-workflow-needs-this-new-agent-browser-cli.md) - "[0:10:38] it just loaded the skill so it understands how to use the agent browser CLI. So we got our progressive disclosure going on there."
