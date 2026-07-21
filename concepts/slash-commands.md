---
type: concept
title: "Slash Commands"
description: "User-defined command files that package a prompt and arguments into a callable shortcut inside the coding agent."
tags: [commands, prompts, reuse]
videos: [full-guide-to-becoming-a-principled-agentic-engineer-build-anything-with-ai, ive-used-claude-code-for-2000-hours-heres-how-i-build-anything-with-it, your-ai-coding-workflow-needs-this-new-agent-browser-cli, the-5-techniques-separating-top-agentic-engineers-right-now, the-kiro-ai-coding-hackathon-has-officially-started-build-anything-win-big-prizes, ai-fixes-my-code-better-than-me-now-heres-how, the-official-archon-guide-10x-your-ai-coding-workflow, the-true-power-of-ai-coding-build-your-own-workflows-full-guide, i-built-my-claude-code-subagents-dream-team-to-create-any-ai-agent, a-complete-guide-to-claude-code-here-are-all-the-best-strategies, build-any-ai-agent-with-this-context-engineering-blueprint, context-engineering-101-the-simple-strategy-to-100x-ai-coding, context-engineering-is-the-new-vibe-coding-learn-this-now]
created: 2026-07-21
updated: 2026-07-21
---

# Slash Commands

A slash command is a user-defined markdown file that packages a prompt into a callable, reusable shortcut inside the coding agent. The one-line definition Cole returns to over and over is that "commands are just prompts that we're having the coding agent run through," or as he puts it elsewhere, "Slash commands are simply prompts that you want to turn into reusable workflows." The mechanism is deliberately dumb: "In the cloud folder, if you have a folder called commands, any of the markdown files that you have here can be executed as custom commands," so a repeatable procedure you would otherwise retype every session becomes a single `/name` invocation.

What makes them workflows rather than snippets is argument templating. "commands and skills support arguments. So that's how we can make things dynamic," and "most of my procedures have arguments." A generic planning command "becomes specific because you pass in your specific plan," e.g. `/generate PRP <feature>` where "the argument that I want to pass in here... it's going to replace the arguments placeholder." This is the payoff of [Commandify Everything](./commandify-everything.md): a small library of parameterized commands covers most of the day, from `/commit` (which carries "the standardization for how I document any work that I did") to intense multi-phase [validation](./validation.md) runs that "understand the codebase, spin up the front end, and then go through the ringer."

Crucially, slash commands are portable because they are just files. Cole stresses this against tool lock-in: "you can use these commands for any AI coding assistant, not just Claude Code. They're really just prompts that define these workflows." If your tool lacks the feature, "it's okay if you don't have slash commands in your AI coding assistant" - you "just say go and read and then give it the path to this command," pointing the agent at the markdown as its prompt. That portability is why slash commands sit next to [Global Rules](./global-rules.md) and [Skills](./skills.md) as core, transferable pieces of the harness.

## Builds on

- [Commandify Everything](./commandify-everything.md) - the principle that every repeatable procedure should become a command.

## Related

- [Skills](./skills.md) - a heavier, model-invoked capability package; commands are the lighter, user-invoked prompt. Both take arguments.
- [Global Rules](./global-rules.md) - always-on conventions; commands are the on-demand workflows those rules point to.
- [The Prime Command](./prime-command.md) - a canonical command that loads codebase context at session start.
- [Agentic Workflow Engineering](./agentic-workflow-engineering.md), [Planning with AI](./planning-with-ai.md), [PRD-First Development](./prd-first-development.md), [The PRP Framework](./prp-framework.md) - the planning and execution procedures most often packaged as commands.
- [Agentic Coding](./agentic-coding.md), [Git as Long-Term Memory](./git-as-long-term-memory.md), [Memory Systems](./memory-systems.md) - where a standardized `/commit` and context commands pay off.

## Tools

- [Claude Code](../entities/tools/claude-code.md) - native `/command` support reading the `.claude/commands/` folder.
- [Codex](../entities/tools/codex.md), [Cursor](../entities/tools/cursor.md), [Gemini CLI](../entities/tools/gemini-cli.md), [Windsurf](../entities/tools/windsurf.md) - either support commands directly or run the same markdown as a pasted prompt.
- [Archon](../entities/tools/archon.md) - packages the same reusable planning workflows into portable command files.

## Sources

- [FULL Guide to Becoming a Principled Agentic Engineer](../sources/full-guide-to-becoming-a-principled-agentic-engineer-build-anything-with-ai.md) - "[0:26:04] commands are just prompts that we're having the coding agent run through"
- [The True Power of AI Coding - Build Your OWN Workflows](../sources/the-true-power-of-ai-coding-build-your-own-workflows-full-guide.md) - "[0:10:28] Slash commands are simply prompts that you want to turn into reusable workflows"
- [Context Engineering is the New Vibe Coding](../sources/context-engineering-is-the-new-vibe-coding-learn-this-now.md) - "[0:13:35] In thecloud folder, if you have a folder called commands, any of the markdown files that you have here can be executed as custom commands for Claude Code."
- [Context Engineering 101 - The Simple Strategy to 100x AI Coding](../sources/context-engineering-101-the-simple-strategy-to-100x-ai-coding.md) - "[0:21:03] It becomes specific because you pass in your specific plan. And the same goes with execute."
- [I've Used Claude Code for 2,000+ Hours](../sources/ive-used-claude-code-for-2000-hours-heres-how-i-build-anything-with-it.md) - "[0:07:50] if I just run / commit. That's all I have to do. It's running this command that has the standardization for how I document any work that I did."
- [The 5 Techniques Separating Top Agentic Engineers Right Now](../sources/the-5-techniques-separating-top-agentic-engineers-right-now.md) - "[0:02:38] you can use these commands for any AI coding assistant, not just Claude Code. They're really just prompts that define these workflows."
- [AI Fixes My Code Better than Me Now?!](../sources/ai-fixes-my-code-better-than-me-now-heres-how.md) - "[0:02:40] if you are using a coding assistant that doesn't support slash commands like cursor for example you can just say go and read and then give it the path to this command"
- [Build ANY AI Agent with this Context Engineering Blueprint](../sources/build-any-ai-agent-with-this-context-engineering-blueprint.md) - "[0:06:49] If you're not using Claude Code, you can still use these slash commands... tell it to use the command as the prompt."
- [The OFFICIAL Archon Guide](../sources/the-official-archon-guide-10x-your-ai-coding-workflow.md) - "[0:22:26] slash commands are just prompts and so no matter your AI coding assistant you can tell it to look at this markdown document and execute this operation"
- [Your AI Coding Workflow NEEDS This New Agent Browser CLI](../sources/your-ai-coding-workflow-needs-this-new-agent-browser-cli.md) - "[0:11:49] I created different Claude Code slashcomands to build the same validation workflow for the different tools."
- [The Kiro AI Coding Hackathon has Officially Started](../sources/the-kiro-ai-coding-hackathon-has-officially-started-build-anything-win-big-prizes.md) - "[0:04:33] You have your prompts or commands. These are the workflows that you define in markdown."
- [A Complete Guide to Claude Code](../sources/a-complete-guide-to-claude-code-here-are-all-the-best-strategies.md) - "[0:12:44] the nice part about having this as a slash command though is that it's just very reusable"
- [I Built My Claude Code Subagents DREAM TEAM](../sources/i-built-my-claude-code-subagents-dream-team-to-create-any-ai-agent.md) - "[0:04:21] Slash commands are your way to have packaged up workflows in Claude Code."
