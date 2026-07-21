---
type: concept
title: "Code Execution"
description: "Giving agents a sandbox to write and run code as a general-purpose tool rather than exposing many narrow tools."
tags: [code, sandbox, tools]
videos: [the-way-we-use-ai-will-completely-change-in-2026-hot-takes, the-big-problem-with-mcp-servers-and-the-solution, this-completely-changes-the-way-we-build-production-ai-agents-vercel-eve, pydantic-ai-20-the-new-best-way-to-build-ai-agents-is-composing-capabilities, googles-agents-cli-the-cli-skills-combination-to-ship-ai-agents-easily, claude-skills-arent-just-for-claude-heres-how-to-build-them-for-any-agent, i-built-my-second-brain-with-claude-code-obsidian-skills-heres-how, claude-code-web-just-dropped-but-i-already-built-something-better-with-codex, the-best-tool-for-ai-agent-workflows-langgraph-full-guide]
created: 2026-07-21
updated: 2026-07-21
---

# Code Execution

Code execution gives an agent a single, general-purpose capability, writing and running code, instead of forcing it through dozens of narrow, predefined tools. The pitch is that "code execution is starting to replace tool calling because the problem we have with tool calling right now is that all the capabilities that we give our agent, they have to take context upfront." When the agent can write code at runtime, it generates its own capabilities on demand: "you are giving the agent the ability to generate its own capabilities at runtime by writing the code to interact with the API." The result is "a massive token reduction. It's also faster and more flexible."

This is Cole's proposed answer to [The Problems With MCP Servers](./mcp-problems.md), where loading many tools burns context before the agent does anything. Instead: "What if we just allowed the agent to write the code directly to interact with the Archon API endpoints instead of having the MCP server as the middleman that is loading dozens of tools up front." The agent decides how to call the API rather than being boxed into fixed tools, "the LLMs these days are really good at writing code and developers should take advantage of this." It pairs naturally with [Progressive Disclosure](./progressive-disclosure.md) and [Skills](./skills.md): a Second Brain build "using code execution to edit and create our PowerPoint slides" reaches MCP servers "through our Python script" rather than wiring them straight into the model.

The non-negotiable cost is isolation. Letting an agent run arbitrary code is only safe in a sandbox, and doing that reliably in production is hard. Providers offer "isolated sandboxing for code execution. So, your agent can write and execute code, but do it in a secure way," and Cole singles it out as "one of the things that you have to do in isolation... a bit of a challenge to really make that reliable when you have an agent deployed to production." Pydantic is building a lightweight open-source sandbox, Monty, for exactly this. In graph-based workflows the generated code becomes a self-correcting step, "if it fails then it's going to go back and try to basically just redo it."

## Builds on

- [Capabilities Over Tools](./capabilities-over-tools.md) - code execution as the ultimate general capability instead of many fixed tools.
- [Tool Calling](./tool-use.md) - the mechanism code execution is starting to replace for token-heavy tool sets.

## Contrasts with

- [The Problems With MCP Servers](./mcp-problems.md) - the upfront-context problem that writing code to hit APIs directly avoids.

## Related

- [Skills](./skills.md) and [Progressive Disclosure](./progressive-disclosure.md) - loading capabilities and instructions on demand, executed via code.
- [Model Context Protocol (MCP)](./mcp.md) - the tool-standard code execution competes with and can call through a script.
- [Agentic Workflow Engineering](./agentic-workflow-engineering.md) and [The Agent Loop (Reason-Act-Observe)](./agent-loop.md) - where generate-run-retry becomes a self-correcting step.
- [AI Coding Harness](./ai-coding-harness.md) and [Agentic Coding](./agentic-coding.md) - systems that lean on runtime code as a first-class action.
- [Context Engineering](./context-engineering.md) - code execution as a major token/context saver.
- [Human in the Loop](./human-in-the-loop.md) and [Memory Systems](./memory-systems.md) - guardrails and state around what an agent runs.

## Tools

- [Pydantic AI](../entities/tools/pydantic-ai.md) - ships "code mode" and is building the open-source Monty sandbox for secure execution.
- [Archon](../entities/tools/archon.md) - the API endpoints an agent hits by writing code instead of via MCP middleman tools.
- [Claude](../entities/tools/claude.md) - Skills-driven agents that run code to manipulate files like PowerPoint slides.
- [Codex](../entities/tools/codex.md) - run inside an authenticated container so code executes in an isolated environment.
- [LangGraph](../entities/tools/langgraph.md) - graph workflows where generated code is imported, run, and retried on failure.

## Sources

- [The Way We Use AI Will Completely Change in 2026 (Hot Takes)](../sources/the-way-we-use-ai-will-completely-change-in-2026-hot-takes.md) - "[0:08:10] code execution is a massive token reduction. It's also faster and more flexible because essentially... you are giving the agent the ability to generate its own capabilities at runtime by writing the code to interact with the API"
- [The BIG Problem with MCP Servers (and the Solution!)](../sources/the-big-problem-with-mcp-servers-and-the-solution.md) - "[0:03:47] What if we just allowed the agent to write the code directly to interact with the Archon API endpoints instead of having the MCP server as the middleman that is loading dozens of tools up front."
- [This Completely Changes the Way We Build Production AI Agents (Vercel Eve)](../sources/this-completely-changes-the-way-we-build-production-ai-agents-vercel-eve.md) - "[0:04:11] They also offer isolated sandboxing for code execution. So, your agent can write and execute code, but do it in a secure way."
- [Google's Agents CLI: The CLI + Skills Combination to Ship AI Agents EASILY](../sources/googles-agents-cli-the-cli-skills-combination-to-ship-ai-agents-easily.md) - "[0:06:00] I'm specifically choosing code execution here because this is one of the things that you have to do in isolation. It's actually a bit of a challenge to really make that reliable when you have an agent deployed to production."
- [Pydantic AI 2.0: The New Best Way to Build AI Agents is Composing Capabilities](../sources/pydantic-ai-20-the-new-best-way-to-build-ai-agents-is-composing-capabilities.md) - "[0:13:39] Pydantic AI or the Pydantic company, the parent company is working on their own lightweight sandbox called Monty, which is open source as well."
- [I Built My Second Brain with Claude Code + Obsidian + Skills (Here's How)](../sources/i-built-my-second-brain-with-claude-code-obsidian-skills-heres-how.md) - "[0:11:14] We're actually using code execution to edit and create our PowerPoint slides, which makes it very powerful and flexible"
- [Claude Skills Aren't Just for Claude - Here's How to Build Them for ANY Agent](../sources/claude-skills-arent-just-for-claude-heres-how-to-build-them-for-any-agent.md) - "[0:07:47] we just need a simple tool. Typically, this load skill tool is going to take a path to the skill.md"
- [Claude Code Web JUST Dropped but I Already Built Something BETTER (with Codex!)](../sources/claude-code-web-just-dropped-but-i-already-built-something-better-with-codex.md) - "[0:13:33] we are running everything within a container. So we don't have the luxury of just using our already authenticated codex because we're running things in an isolated environment"
- [THE BEST Tool for AI Agent Workflows - LangGraph FULL Guide](../sources/the-best-tool-for-ai-agent-workflows-langgraph-full-guide.md) - "[0:04:31] it's going to generate the Preamble Imports and code and so it'll try to then import the code as another step and if it fails then it's going to go back and try to basically just redo it"
