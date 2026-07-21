---
type: entity
subtype: tool
title: "Archon"
description: "Cole's free, open-source AI command center and harness builder for AI coding; started as an AI agent that builds other AI agents."
resource: "https://github.com/coleam00/Archon"
tags: [coding-agent, open-source, harness, mcp, rag]
videos: [i-turned-claude-code-into-a-complete-video-generation-system-with-archon, the-best-ai-coding-setup-isnt-the-most-autonomous-one-heres-why, the-creators-of-claude-code-and-openclaw-dont-prompt-their-agents-anymore, omnigent-the-new-meta-harness-for-every-coding-agent-claude-code-codex-pi-more, harness-engineering-what-separates-top-agentic-engineers-right-now, the-next-evolution-of-ai-coding-is-harnesses-heres-how-to-build-them, pi-coding-agent-archon-build-any-ai-coding-workflow-no-claude-code-bloat, im-building-an-ai-dark-factory-that-ships-its-own-code-public-experiment, the-official-archon-guide-10x-your-ai-coding-workflow, introducing-archon-the-revolutionary-operating-system-for-ai-coding, introducing-archon-an-ai-agent-that-builds-ai-agents, build-an-army-of-ai-agents-on-autopilot-with-archon-heres-how, the-big-problem-with-mcp-servers-and-the-solution, why-the-best-ai-coding-tools-abandoned-rag-and-what-they-use-instead]
created: 2026-07-21
updated: 2026-07-21
---

# Archon

Archon is Cole's flagship free, open-source project: an AI command center for coding that has grown into "the first open-source harness builder for AI coding" ([0:00:00]). Cole frames it as the layer between a developer and their coding agents: "Archon is my harness builder. Allows us to build workflows that orchestrate many coding agent sessions to handle larger tasks" ([0:08:57]). Rather than being a single agent, it wraps and coordinates the others: "it wraps above Claude code and Codex. So the old Archon was more of a tool built into coding agents" ([0:05:48]).

## The evolution (narrated, not contradictory)

Archon's identity has deliberately shifted over time. It launched as "an open-source AI agent that literally builds other AI agents" ([0:00:00]), powered by "a combination of my two favorite Frameworks Pydantic AI and LangGraph" ([0:06:22]), linking it to [Pydantic AI](./pydantic-ai.md) and [LangGraph](./langgraph.md). It then became a knowledge-and-task backbone exposed over [MCP](./mcp.md): "you instantly give it access through the MCP to search all of the documentation that you've curated and manage the same projects and tasks in this Kanban board" ([0:00:18]), an application of [RAG](../../concepts/rag.md) and [Context Engineering](../../concepts/context-engineering.md) for coding assistants. Cole later cooled on naive [RAG](../../concepts/rag.md) for codebases ("the chunks... just kind of confuses the LLM more than it helps," [0:09:29]) and pivoted Archon toward harness building. Today it centers on [Agentic Workflow Engineering](../../concepts/agentic-workflow-engineering.md): "This is a workflow that takes all of these skills, and it combines it together into a single execution" ([0:03:54]), with a workflow builder he calls "the n8n for AI coding," inviting comparison to [n8n](./n8n.md).

## How Cole uses it / why it matters

Archon is the orchestration backbone across Cole's builds. It ships default workflows ("Let's take a look at fix GitHub issue for example," [0:09:42]), supports [Git Worktrees](./git-worktree.md) and [Context Isolation](../../concepts/context-isolation.md) for [Parallel Agentic Coding](../../concepts/parallel-agentic-coding.md) "at extreme scale" ([0:02:24]), and mixes deterministic and agentic nodes so a workflow can enforce [Validation](../../concepts/validation.md) and [Human in the Loop](../../concepts/human-in-the-loop.md) gates. As of the Pi release, "we've officially added it as the third coding agent supported in Archon" ([0:00:34]), a nod to [Model Selection](../../concepts/model-selection.md) and provider flexibility across [Claude Code](./claude-code.md), [Codex](./codex.md), and [Pi](./pi-coding-agent.md). It is the chosen backbone for Cole's Dark Factory experiment because "I define the process" ([0:15:45]).

## Realizes

- [Agents That Build Agents](../../concepts/agents-that-build-agents.md) - A meta-agent whose specialty is generating, iterating on, and eventually running other AI agents on demand, so the agents it produces become reusable sub-agents themselves.
- [Agentic Workflow Engineering](../../concepts/agentic-workflow-engineering.md) - Designing repeatable AI workflows as engineered systems with defined steps, orchestration, and background execution rather than ad-hoc prompting.
- [AI Coding Harness](../../concepts/ai-coding-harness.md) - The surrounding scaffolding (prompts, tools, rules, validation) that turns a raw model into a reliable coding system.

## Works with

- [Claude Code](./claude-code.md) - Anthropic's terminal-based agentic coding assistant that is the subject of this complete-guide walkthrough.
- [Codex](./codex.md) - OpenAI's cloud-based software-engineering agent integrated with GitHub, plus a Codex CLI.
- [Pi](./pi-coding-agent.md) - A minimalistic, open-source coding agent cited as another example of a company-built harness around a model.
- [Roast](./roast.md) - Shopify's open-source structured AI workflow engine that combines deterministic and agentic nodes, Cole's recommended starting point for building your own harness.
- [Git Worktrees](./git-worktree.md) - Git feature that duplicates the codebase across isolated branches so multiple coding agents can run in parallel without collisions.
- [MCP (Model Context Protocol)](./mcp.md) - The protocol used to connect Claude Code to external tools and servers.
- [Pydantic AI](./pydantic-ai.md) - Cole's framework for the individual agents, structured around three parts: dependencies, the agent definition, and tools.
- [LangGraph](./langgraph.md) - The orchestration framework wiring agents into a stateful graph of nodes and edges, used here to run agents in parallel and add human-in-the-loop.
- [Airtable](./airtable.md) - Spreadsheet-database platform wired to an agent via its MCP server, backing the 'AI research base' where the agent army writes and reads structured records.
- [BMAD Method](./bmad-method.md) - An open-source context-engineering framework (installed via npx bmad-method install) that ships expert sub-agent personas (analyst, PM, architect, scrum master, dev, QA) as markdown prompts driving separate greenfield and brownfield planning and development workflows.
- [Higgsfield](./higgsfield.md) - A video-generation platform with a CLI used to create marketing videos and UGC-style ads from prompts and branded reference images, driven from inside the coding agent's terminal.
- [HyperFrames](./hyperframes.md) - An HTML-based video rendering tool with a built-in preview editor that lets AI agents generate and mold animated scenes, positioned as a more reliable step up from Remotion.
- [Kokoro](./kokoro.md) - A free, open-source text-to-speech model that lets you run the entire AI video-generation workflow at no cost.

## Related

- [Retrieval-Augmented Generation (RAG)](../../concepts/rag.md) - Grounding an LLM's answers by retrieving relevant documents from an external knowledge base and injecting them into the prompt at query time.
- [Context Engineering](../../concepts/context-engineering.md) - The deliberate practice of curating exactly what goes into an LLM's limited context window - system messages, schemas, chat history, and dynamic variables - to avoid overload and keep outputs sharp.
- [Validation](../../concepts/validation.md) - Building explicit checks into agentic workflows so the AI verifies its own output against real success criteria before moving on.
- [Human in the Loop](../../concepts/human-in-the-loop.md) - Keeping a human as the approver and steerer of agentic work rather than fully automating, so AI augments engineers instead of replacing them.
- [Model Selection](../../concepts/model-selection.md) - Choosing the right LLM per task by trading off quality, speed, and cost, often routing easy requests to cheap models and hard ones to expensive models.
- [Parallel Agentic Coding](../../concepts/parallel-agentic-coding.md) - Dispatching agents to background tasks in isolated git worktrees, each fed repo context and returning a reviewable PR.
- [Context Isolation](../../concepts/context-isolation.md) - Giving each agent or subagent its own clean context window so unrelated tokens never dilute the task at hand.
- [n8n](./n8n.md) - A no-code AI automation platform for building agents and workflows that integrate with 500+ applications.
- [Geoffrey Huntley](../people/geoffrey-huntley.md) - Creator of the Ralph Wiggum long-running agent loop, who frames it as a planning-heavy philosophy rather than a shiny framework or the Anthropic plugin.

## Sources

- [The Next Evolution of AI Coding Is Harnesses - Here's How to Build Them](../../sources/the-next-evolution-of-ai-coding-is-harnesses-heres-how-to-build-them.md) - "[0:00:00] I am unveiling the new Archon, a massive overhaul of the AI command center... It is now the first open-source harness builder for AI coding."
- [The Creators of Claude Code and OpenClaw don't Prompt Their Agents Anymore?!](../../sources/the-creators-of-claude-code-and-openclaw-dont-prompt-their-agents-anymore.md) - "[0:08:57] Archon is my harness builder. Allows us to build workflows that orchestrate many coding agent sessions to handle larger tasks."
- [Introducing Archon - an AI Agent that BUILDS AI Agents](../../sources/introducing-archon-an-ai-agent-that-builds-ai-agents.md) - "[0:06:22] archon uses a combination of my two favorite Frameworks Pydantic AI and LangGraph for this agentic workflow that can intelligently build agents"
- [The OFFICIAL Archon Guide - 10x Your AI Coding Workflow](../../sources/the-official-archon-guide-10x-your-ai-coding-workflow.md) - "[0:00:18] for the AI coding assistant, it is an MCP server... And then you instantly give it access through the MCP to search all of the documentation that you've curated and manage the same projects and tasks in this Kanban board."
- [Why the Best AI Coding Tools Abandoned RAG (And What They Use Instead)](../../sources/why-the-best-ai-coding-tools-abandoned-rag-and-what-they-use-instead.md) - "[0:09:29] I've seen it where the chunks that you get back from your knowledge base for your codebase, it just kind of confuses the LLM more than it helps."
- [Claude Plans, Gemini Designs: The Workflow to Build BEAUTIFUL Frontends](../../sources/claude-plans-gemini-designs-the-workflow-to-build-beautiful-frontends.md) - "[0:03:54] Archon is my open source harness builder. This is a workflow that takes all of these skills, and it combines it together into a single execution."
- [Pi Coding Agent + Archon: Build ANY AI Coding Workflow (No Claude Code Bloat)](../../sources/pi-coding-agent-archon-build-any-ai-coding-workflow-no-claude-code-bloat.md) - "[0:00:34] we've officially added it as the third coding agent supported in Archon."
- [Parallel Claude Code + Git Worktrees: This Setup Will Change How You Ship](../../sources/parallel-claude-code-git-worktrees-this-setup-will-change-how-you-ship.md) - "[0:02:24] I've built support for a lot of these things like isolation and workre. So, it's a system that ships ready for you to do parallel agentic development at extreme scale."
- [I'm Building an AI Dark Factory That Ships Its Own Code (Public Experiment)](../../sources/im-building-an-ai-dark-factory-that-ships-its-own-code-public-experiment.md) - "[0:15:45] It's the perfect fit to be the backbone for the dark factory because I define the process."
- [Introducing Archon - The Revolutionary Operating System for AI Coding](../../sources/introducing-archon-the-revolutionary-operating-system-for-ai-coding.md) - "[0:02:10] it's a command center for AI coding assistants... The UI is native to humans. MCP is native to the LLM. So we each have our way to collaborate on the same projects together."
- [Build an ARMY of AI Agents on Autopilot with Archon, Here's How](../../sources/build-an-army-of-ai-agents-on-autopilot-with-archon-heres-how.md) - "[0:00:00] archon is the first of its kind it's an open- source AI agent that builds other AI agents and I used it to create something pretty insane"
- [The BIG Problem with MCP Servers (and the Solution!)](../../sources/the-big-problem-with-mcp-servers-and-the-solution.md) - "[0:07:11] I took the Archon MCP server, transformed it into a skill to prove to myself and to you that we have all the same functionality, and now it is way more token efficient"
