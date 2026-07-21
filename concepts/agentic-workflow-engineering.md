---
type: concept
title: "Agentic Workflow Engineering"
description: "Designing repeatable AI workflows as engineered systems with defined steps, orchestration, and background execution rather than ad-hoc prompting."
tags: [workflows, orchestration, automation, agentic-coding, harness]
videos: [i-turned-claude-code-into-a-complete-video-generation-system-with-archon, the-best-ai-coding-setup-isnt-the-most-autonomous-one-heres-why, the-creators-of-claude-code-and-openclaw-dont-prompt-their-agents-anymore, omnigent-the-new-meta-harness-for-every-coding-agent-claude-code-codex-pi-more, claude-plans-gemini-designs-the-workflow-to-build-beautiful-frontends, harness-engineering-what-separates-top-agentic-engineers-right-now, pi-coding-agent-archon-build-any-ai-coding-workflow-no-claude-code-bloat, im-building-an-ai-dark-factory-that-ships-its-own-code-public-experiment, the-next-evolution-of-ai-coding-is-harnesses-heres-how-to-build-them, everything-you-thought-about-building-ai-agents-is-wrong, youre-hardly-using-what-claude-code-has-to-offer-its-insane, stripes-coding-agents-ship-1300-prs-every-week-heres-how-they-do-it, turn-claude-code-into-your-full-engineering-team-with-subagents, github-is-the-future-of-ai-coding-heres-why, should-i-build-my-ai-agents-with-n8n-or-python, the-official-archon-guide-10x-your-ai-coding-workflow, the-true-power-of-ai-coding-build-your-own-workflows-full-guide, i-built-my-claude-code-subagents-dream-team-to-create-any-ai-agent, archon-beta-launch-livestream-what-you-missed, google-anthropic-and-openais-guides-to-ai-agents-all-in-18-minutes, the-best-tool-for-ai-agent-workflows-langgraph-full-guide, this-is-hands-down-the-best-way-to-build-ai-agents]
created: 2026-07-21
updated: 2026-07-21
---

# Agentic Workflow Engineering

Agentic workflow engineering is the practice of packaging a development process into repeatable, orchestrated workflows instead of steering agents by hand each time. As Cole frames it, "the main idea with Archon is you can encode your development process as a workflow, no matter what it is," so that you "define once, run forever, reusable across projects." The payoff is scale: "It allows you to take your entire agentic engineering process, no matter what it is, and package it up into reusable workflows that you can execute in parallel to handle all of your AI coding tasks at scale."

The defining shift is away from prompting toward orchestration. Cole reports that the people who built these tools "don't prompt their agents anymore": "We want to have some main orchestrator agent that we talk to. We do minimal prompting, just telling it what we want at a high level, and it figures out how to set up the loop and the entire system." A typical engineered pipeline chains specialist stages, "it starts with a planning agent... And then we send that into the code generation agent... and then the validation layer to review that pull request... And then of course we have the deployment system," bound together by "the orchestration layer... that higher level agent to take the spec and split it into tasks to manage the handoffs between the different agents."

This is where custom beats off-the-shelf. Cole is blunt: "I really believe that if you build your own optimized workflow, it's going to be way better than anything that's off the shelf," which is why he advocates "scrapping the notion of existing frameworks like PRP and BMAD" to build your own. Every orchestrator, in his decomposition, "comprises of three parts. We have the configuration and then we have all the skills... and then we have the agents that it can call upon." Workflows also run unattended: recurring prompts via `/loop`, quality-gate agents running alongside, and cron jobs "outside of any specific cloud code session," all managed "under the hood just with natural language."

## Builds on

- [AI Coding Harness](./ai-coding-harness.md) - the engineered system that agentic workflows package and run.
- [Context Engineering](./context-engineering.md) - the discipline harness engineering directly evolves from.

## Part of

- [Agents vs. Workflows](./agents-vs-workflows.md) - workflows fix the graph of steps; agents choose steps at runtime.

## Related

- [Deterministic Workflows](./deterministic-workflows.md) - fixing known steps in code and reserving the LLM for fuzzy decisions.
- [Subagents Pattern](./subagents-pattern.md) and [Agent Teams](./agent-teams.md) - the specialists an orchestrator calls upon.
- [Parallel Agentic Coding](./parallel-agentic-coding.md) - running packaged workflows concurrently.
- [Commandify Everything](./commandify-everything.md) - turning steps into reusable, invocable commands.
- [Human in the Loop](./human-in-the-loop.md) - where the engineer still steers the orchestrator.
- [MCP](./mcp.md), [Tool Calling](./tool-use.md), [RAG](./rag.md) - the capabilities a workflow wires together.
- [Chat Interfaces](./chat-interfaces.md) - the natural-language surface for driving the system.

## Tools

- [Archon](../entities/tools/archon.md) - encodes a development process as a runnable, parallelizable workflow.
- [Claude Code](../entities/tools/claude-code.md) - drives orchestration, subagents, `/loop`, and cron jobs.
- [Pi](../entities/tools/pi-coding-agent.md) - a lightweight agent for building workflows without harness bloat.
- [LangGraph](../entities/tools/langgraph.md) - a nodes-and-edges framework for structuring agent interactions.
- [GitHub](../entities/tools/github.md) - the orchestration layer for task management and handoffs.

## Sources

- [The Next Evolution of AI Coding Is Harnesses - Here's How to Build Them](../sources/the-next-evolution-of-ai-coding-is-harnesses-heres-how-to-build-them.md) - "[0:06:20] now your entire process, you can bundle as an Archon workflow. Define once, run forever, reusable across projects."
- [Pi Coding Agent + Archon: Build ANY AI Coding Workflow](../sources/pi-coding-agent-archon-build-any-ai-coding-workflow-no-claude-code-bloat.md) - "[0:00:52] package it up into reusable workflows that you can execute in parallel to handle all of your AI coding tasks at scale."
- [The Creators of Claude Code and OpenClaw don't Prompt Their Agents Anymore?!](../sources/the-creators-of-claude-code-and-openclaw-dont-prompt-their-agents-anymore.md) - "[0:03:28] We want to have some main orchestrator agent that we talk to. We do minimal prompting... and it figures out how to set up the loop and the entire system."
- [The Best AI Coding Setup Isn't the Most Autonomous One (Here's Why)](../sources/the-best-ai-coding-setup-isnt-the-most-autonomous-one-heres-why.md) - "[0:18:35] we need the orchestration layer... that higher level agent to take the spec and split it into tasks to manage the handoffs between the different agents."
- [Harness Engineering: What Separates Top Agentic Engineers Right Now](../sources/harness-engineering-what-separates-top-agentic-engineers-right-now.md) - "[0:14:13] The real power with harness engineering here is we can automate all of this... hooks together all these coding agent sessions with the handoff documents and creating the poll requests."
- [The True Power of AI Coding - Build Your OWN Workflows](../sources/the-true-power-of-ai-coding-build-your-own-workflows-full-guide.md) - "[0:25:24] that becomes your process that you can reuse for anything."
- [Turn Claude Code into Your Full Engineering Team with Subagents](../sources/turn-claude-code-into-your-full-engineering-team-with-subagents.md) - "[0:19:01] I really believe that if you build your own optimized workflow, it's going to be way better than anything that's off the shelf."
- [Omnigent: The New Meta-Harness for EVERY Coding Agent](../sources/omnigent-the-new-meta-harness-for-every-coding-agent-claude-code-codex-pi-more.md) - "[0:08:13] every single orchestrator comprises of three parts. We have the configuration and then we have all the skills... and then we have the agents that it can call upon."
- [I'm Building an AI Dark Factory That Ships Its Own Code](../sources/im-building-an-ai-dark-factory-that-ships-its-own-code-public-experiment.md) - "[0:15:28] you take your AI coding process, no matter what it is, and you can package it up into deterministic and repeatable AI coding workflows."
- [Stripe's Coding Agents Ship 1,300 PRs EVERY Week](../sources/stripes-coding-agents-ship-1300-prs-every-week-heres-how-they-do-it.md) - "[0:05:40] A workflow is an LLM system that operates via a fixed graph of steps... versus having the system be the agent."
- [You're Hardly Using What Claude Code Has to Offer](../sources/youre-hardly-using-what-claude-code-has-to-offer-its-insane.md) - "[0:13:33] we can also set up what are called cron jobs... we manage all of these tasks under the hood just with natural language."
- [I Turned Claude Code Into a Complete Video Generation System (with Archon)](../sources/i-turned-claude-code-into-a-complete-video-generation-system-with-archon.md) - "[0:00:18] It allows you to create these larger systems where you're connecting many coding agents together to work on longer tasks autonomously."
- [Everything You Thought About Building AI Agents is Wrong](../sources/everything-you-thought-about-building-ai-agents-is-wrong.md) - "[0:03:27] There is a lot of glue code to create the agent infrastructure ourself. There is a lot of complexity there."
- [GitHub is the Future of AI Coding (Here's Why)](../sources/github-is-the-future-of-ai-coding-heres-why.md) - "[0:00:16] we are always going to have a need for what I like to call the orchestration layer... task management, track changes... even make a different assignments to different coding agents."
- [The OFFICIAL Archon Guide - 10x Your AI Coding Workflow](../sources/the-official-archon-guide-10x-your-ai-coding-workflow.md) - "[0:14:03] it's up to you to define your own AI coding workflow and how you want to incorporate Archon. There's a lot of flexibility here."
- [I Built My Claude Code Subagents DREAM TEAM to Create Any AI Agent](../sources/i-built-my-claude-code-subagents-dream-team-to-create-any-ai-agent.md) - "[0:00:29] We become the project manager of our agents. And that my friend is the future of agentic coding."
- [Google, Anthropic, and OpenAI's Guides to AI Agents ALL in 18 Minutes](../sources/google-anthropic-and-openais-guides-to-ai-agents-all-in-18-minutes.md) - "[0:09:36] we have the orchestrator and worker flow where we have one primary agent that is managing many other agents taking the task and splitting it up."
- [THE BEST Tool for AI Agent Workflows - LangGraph FULL Guide](../sources/the-best-tool-for-ai-agent-workflows-langgraph-full-guide.md) - "[0:00:31] using LangGraph which makes even your most complicated agentic workflows clear concise and bug-free."
- [Claude Plans, Gemini Designs: The Workflow to Build BEAUTIFUL Frontends](../sources/claude-plans-gemini-designs-the-workflow-to-build-beautiful-frontends.md) - "[0:05:32] I can try in just a couple minutes, I can swap exploration to use Gemini with Pi as well... find the best mix of providers."
- [Should I Build My AI Agents with n8n or Python?](../sources/should-i-build-my-ai-agents-with-n8n-or-python.md) - "[0:06:15] what I mean by the integration box is we are boxed in to the integrations that n8n supplies us."
- [Archon Beta Launch Livestream - What You Missed!](../sources/archon-beta-launch-livestream-what-you-missed.md) - "[0:04:00] It is the operating system for AI coding. And so what that means is it's the command center."
- [This is Hands Down the BEST Way to Build AI Agents](../sources/this-is-hands-down-the-best-way-to-build-ai-agents.md) - "[0:03:19] it is an orchestrator it is a way to take AI agents that you've built with something like Pydantic AI and combine them together in a workflow."
