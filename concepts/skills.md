---
type: concept
title: "Skills"
description: "Reusable, model-invoked capability packages that load specialized instructions and tools on demand to extend an agent."
tags: [skills, capabilities, reuse]
videos: [this-completely-changes-the-way-we-build-production-ai-agents-vercel-eve, i-turned-claude-code-into-a-complete-video-generation-system-with-archon, google-just-dropped-a-masterclass-on-agentic-engineering-its-so-good, omnigent-the-new-meta-harness-for-every-coding-agent-claude-code-codex-pi-more, googles-agents-cli-the-cli-skills-combination-to-ship-ai-agents-easily, claude-plans-gemini-designs-the-workflow-to-build-beautiful-frontends, anthropic-just-dropped-a-masterclass-on-building-agent-harnesses-for-large-codebases, build-render-entire-videos-with-claude-code-full-workflow, ai-youtube-is-only-claude-hype-now, full-guide-to-becoming-a-principled-agentic-engineer-build-anything-with-ai, pi-coding-agent-archon-build-any-ai-coding-workflow-no-claude-code-bloat, full-guide-build-your-own-ai-second-brain-with-claude-code, everything-you-thought-about-building-ai-agents-is-wrong, ive-used-claude-code-for-2000-hours-heres-how-i-build-anything-with-it, build-beautiful-diagrams-with-claude-code-full-workflow, this-one-command-makes-coding-agents-find-all-their-mistakes-use-it-now, how-to-properly-use-claude-code-agent-teams-full-live-build, i-built-a-safer-openclaw-alternative-using-claude-code, claude-codes-agent-teams-are-insane-multiple-ai-agents-coding-together-in-real-time, claude-skills-arent-just-for-claude-heres-how-to-build-them-for-any-agent, i-built-my-second-brain-with-claude-code-obsidian-skills-heres-how, your-ai-coding-workflow-needs-this-new-agent-browser-cli, ai-exploded-in-2025-heres-everything-that-happened, the-way-we-use-ai-will-completely-change-in-2026-hot-takes, the-big-problem-with-mcp-servers-and-the-solution, how-to-dominate-with-ai-in-2025]
created: 2026-07-21
updated: 2026-07-21
---

# Skills

A skill is a reusable, model-invoked capability package: a `skill.md` file of specialized instructions (optionally pointing to scripts and reference docs) that an agent loads on demand. The definition Cole endorses from Google's masterclass captures why they matter: "rather than embedding every piece of specialized knowledge into the agent system prompt, skills allow the agent to remain a lightweight generalist that flexes into specialist roles on demand through progressive disclosure." The mechanic is deliberately simple: "as long as you dump a skill.md file in a folder within skills, Claude code magically understands it and you can now invoke that skill." Cole's shorthand across videos is blunt: "your skills. These are your reusable workflows."

The load happens in stages, which is the whole point. "When we define a skill we have the name and the description. The description is what is given to the coding agent right away," and only "if the agent decides it wants to use this skill, then it'll load the full skill.md which can also point to other scripts or reference documents." That [progressive disclosure](./progressive-disclosure.md) is why skills are so much cheaper than always-on tooling: the initial cost is "very very token efficient like 2 to 3% of the token usage compared to MCP at the start of a conversation," which is why "it's becoming a replacement in a lot of ways for MCP cuz it's a lot more context optimized" (see [The Problems With MCP Servers](./mcp-problems.md)). A skill can flip its behavior too: you can disable model invocation so it only fires on an explicit call, blurring the line with [slash commands](./slash-commands.md).

Skills are how a single generalist agent becomes many specialists. "we really only need one agent for everything and then we can make it specialized with our skills," so "claude code can essentially specialize itself in each session depending on what I want it to do." They also travel: they are just files, so "we can literally use a skill as a prompt, even if you're using a coding agent that doesn't support skills in the same way," and the pattern "is going to work no matter what tool you end up using." Increasingly every platform ships one, since "every single platform that you integrate is going to have some skill that you can bring into your coding agent so it knows how to best leverage the SDK." Most powerfully, skills compose recursively: "one of the skills I have in my second brain is a skill on how to create more skills," making capability growth a conversation.

## Builds on

- [Progressive Disclosure](./progressive-disclosure.md) - the description-then-body loading model that makes skills token-efficient.
- [The AI Layer](./the-ai-layer.md) - skills are one of the core owned components of the layer.

## Contrasts with

- [The Problems With MCP Servers](./mcp-problems.md) - skills are the context-optimized alternative to always-loaded MCP tool schemas.

## Related

- [Slash Commands](./slash-commands.md) and [Commandify Everything](./commandify-everything.md) - the lighter, user-invoked cousins; a skill with model-invocation off behaves like a command.
- [Global Rules](./global-rules.md) - always-on conventions that teach the agent when to reach for skills.
- [Context Engineering](./context-engineering.md) and [Code Execution](./code-execution.md) - skills curate context and often hand the agent scripts to run.
- [System Evolution](./system-evolution.md) - a skill that writes skills is how capabilities compound.
- [Second Brain](./second-brain.md) and [Agent Teams](./agent-teams.md) - skills give a personal assistant its arms and give teammates shared capabilities.
- [AI Coding Harness](./ai-coding-harness.md) - skills are a harness building block.
- [Dynamic System Prompt](./dynamic-system-prompt.md) - Assembling an agent's system prompt at runtime by scanning a skills/context directory and injecting each file's front-matter description and path onto the static base instructions, which is what makes skills portable to any framework.

## Tools

- [Claude Code](../entities/tools/claude-code.md) - native skills from the `skills/` folder; [Claude Desktop](../entities/tools/claude-desktop.md) ships a skill creator.
- [Pydantic AI](../entities/tools/pydantic-ai.md) - Cole added his own skills support via a dynamic system prompt loaded from a skills directory.
- [Archon](../entities/tools/archon.md) - wraps skills in workflows for parallel execution and durability.
- [Agent Browser](../entities/tools/agent-browser.md) and [Remotion](../entities/tools/remotion.md) - example integrations that ship a `skill.md`; [Pi Coding Agent](../entities/tools/pi-coding-agent.md) supports skills out of the box.
- [Claw Hub](../entities/tools/claw-hub.md) - OpenClaw's public skills marketplace, where research found hundreds of malicious packages stealing API keys and SSH credentials, the canonical example of untrusted third-party agent capabilities.
- [Excalidraw](../entities/tools/excalidraw.md) - Free, open-source hand-drawn-style diagramming tool whose JSON format coding agents can generate directly, rendered at excalidraw.com or through the Obsidian Excalidraw plugin.

## Sources

- [Google Just Dropped a Masterclass on Agentic Engineering](../sources/google-just-dropped-a-masterclass-on-agentic-engineering-its-so-good.md) - "[0:16:51] skills allow the agent to remain a lightweight generalist that flexes into specialist roles on demand through progressive disclosure."
- [This Completely Changes the Way We Build Production AI Agents (Vercel Eve)](../sources/this-completely-changes-the-way-we-build-production-ai-agents-vercel-eve.md) - "[0:03:22] as long as you dump a skill.md file in a folder within skills, Claude code magically understands it and you can now invoke that skill with a slash command."
- [Anthropic Just Dropped a Masterclass on Building Agent Harnesses](../sources/anthropic-just-dropped-a-masterclass-on-building-agent-harnesses-for-large-codebases.md) - "[0:16:33] When we define a skill we have the name and the description. The description is what is given to the coding agent right away."
- [I've Used Claude Code for 2,000+ Hours](../sources/ive-used-claude-code-for-2000-hours-heres-how-i-build-anything-with-it.md) - "[0:17:23] If the agent decides it wants to use this skill, then it'll load the full skill.md which can also point to other scripts or reference documents."
- [The BIG Problem with MCP Servers (and the Solution!)](../sources/the-big-problem-with-mcp-servers-and-the-solution.md) - "[0:06:46] this is very very token efficient like 2 to 3% of the token usage compared to MCP at the start of a conversation"
- [AI Exploded in 2025 - Here's Everything That Happened](../sources/ai-exploded-in-2025-heres-everything-that-happened.md) - "[0:14:52] Claude Skills... it's becoming a replacement in a lot of ways for MCP cuz it's a lot more context optimized"
- [Google Just Dropped a Masterclass on Agentic Engineering](../sources/google-just-dropped-a-masterclass-on-agentic-engineering-its-so-good.md) - "[0:17:10] we really only need one agent for everything and then we can make it specialized with our skills, i.e. our workflows."
- [Claude Plans, Gemini Designs](../sources/claude-plans-gemini-designs-the-workflow-to-build-beautiful-frontends.md) - "[0:15:34] we can literally use a skill as a prompt, even if you're using a coding agent that doesn't support skills in the same way."
- [Claude Skills Aren't Just for Claude](../sources/claude-skills-arent-just-for-claude-heres-how-to-build-them-for-any-agent.md) - "[0:00:00] It hasn't been that long since Anthropic released skills to the world and it is one of the most important advancements in AI recently."
- [I Built a Safer OpenClaw Alternative Using Claude Code](../sources/i-built-a-safer-openclaw-alternative-using-claude-code.md) - "[0:12:28] one of the skills I have in my second brain is a skill on how to create more skills and so it's very easy for me to evolve the capabilities of my second brain just by having a conversation with it."
- [This One Command Makes Coding Agents Find All Their Mistakes](../sources/this-one-command-makes-coding-agents-find-all-their-mistakes-use-it-now.md) - "[0:17:32] for the skill that I have linked in the GitHub repo, I've actually disabled model invocation. You can do this with all claude code skills."
- [How to Properly Use Claude Code Agent Teams](../sources/how-to-properly-use-claude-code-agent-teams-full-live-build.md) - "[0:34:18] every single platform that you integrate is going to have some skill that you can bring into your coding agent so it knows how to best leverage the SDK."
- [I Built My Second Brain with Claude Code + Obsidian + Skills](../sources/i-built-my-second-brain-with-claude-code-obsidian-skills-heres-how.md) - "[0:08:30] claude code can essentially specialize itself in each session depending on what I want it to do"
- [Everything You Thought About Building AI Agents is Wrong](../sources/everything-you-thought-about-building-ai-agents-is-wrong.md) - "[0:09:57] I created a Pydantic AI agent where I added in my own support for skills... Everything works the exact same as it would in in Claude Code"
- [Full Guide - Build Your Own AI Second Brain with Claude Code](../sources/full-guide-build-your-own-ai-second-brain-with-claude-code.md) - "[0:13:42] that is where skills come in. And Claude Code plus skills is all we need for our capabilities"
- [FULL Guide to Becoming a Principled Agentic Engineer](../sources/full-guide-to-becoming-a-principled-agentic-engineer-build-anything-with-ai.md) - "[0:11:41] your skills. These are your reusable workflows."
- [Build BEAUTIFUL Diagrams with Claude Code](../sources/build-beautiful-diagrams-with-claude-code-full-workflow.md) - "[0:00:35] I've taken my entire workflow and I've packaged it up into a skill so I can use Claude code or any coding agent"
- [Your AI Coding Workflow NEEDS This New Agent Browser CLI](../sources/your-ai-coding-workflow-needs-this-new-agent-browser-cli.md) - "[0:09:24] they have the skill.md. If you're using Claude code, you can add this into your skills directory."
- [Omnigent: The New Meta-Harness for EVERY Coding Agent](../sources/omnigent-the-new-meta-harness-for-every-coding-agent-claude-code-codex-pi-more.md) - "[0:09:32] skills... This is the workflow that it can walk itself through."
- [Google's Agents CLI: The CLI + Skills Combination](../sources/googles-agents-cli-the-cli-skills-combination-to-ship-ai-agents-easily.md) - "[0:04:07] every stage of building an agent that we have CLI capabilities for, we have a skill to go along with it."
- [Build + Render ENTIRE Videos with Claude Code](../sources/build-render-entire-videos-with-claude-code-full-workflow.md) - "[0:06:50] the entire workflow can be boiled down into this claude code skill that's wrapped in the archon workflow"
- [I Turned Claude Code Into a Complete Video Generation System](../sources/i-turned-claude-code-into-a-complete-video-generation-system-with-archon.md) - "[0:04:12] these are really just instructions for the agent on how to use the CLI effectively."
- [AI YouTube Is Only Claude Hype Now](../sources/ai-youtube-is-only-claude-hype-now.md) - "[0:03:22] Claude has an internal skill to search its own documentation."
- [The Way We Use AI Will Completely Change in 2026](../sources/the-way-we-use-ai-will-completely-change-in-2026-hot-takes.md) - "[0:09:31] take a look at Claude skills. It's kind of the first standard for composable skills or progressive disclosure."
- [Pi Coding Agent + Archon](../sources/pi-coding-agent-archon-build-any-ai-coding-workflow-no-claude-code-bloat.md) - "[0:08:13] It supports skills out of the box, global rules... So, it has that compatibility if you're coming over from Claude Code."
- [How to DOMINATE with AI in 2025](../sources/how-to-dominate-with-ai-in-2025.md) - "[0:02:53] focus on the bigger picture higher leverage skills instead of a bunch of disperate low leverage skills"
