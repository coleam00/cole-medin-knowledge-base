---
type: concept
title: "Agents That Build Agents"
description: "A meta-agent whose specialty is generating, iterating on, and eventually running other AI agents on demand, so the agents it produces become reusable sub-agents themselves."
tags: [agentic-coding, meta-agent, archon]
videos: [introducing-archon-an-ai-agent-that-builds-ai-agents]
created: 2026-07-21
updated: 2026-07-21
---

# Agents That Build Agents

An agent that builds agents is a meta-agent: its domain is not code in general but the production of other agents. "Today it is my pleasure to officially introduce to you Archon, an open-source AI agent that literally builds other AI agents." [0:00:00] The framing Cole reaches for is a familiar one from the app-generation world: "you can think of it like bolt but for agents instead of front ends and a lot more" [0:01:42].

The bet is specialization over generality. Generalist coding assistants can write agent code, but they are tuned for everything, so they never get one framework quite right. A meta-agent narrows the target: targeted instructions plus [RAG](./rag.md) over framework documentation means it emits correct [Pydantic AI](../entities/tools/pydantic-ai.md) and [LangGraph](../entities/tools/langgraph.md) code, complete with file structure, an environment example, and a README. It can run standalone or plug into an AI IDE over [MCP](./mcp.md), which turns the meta-agent into a sub-agent the IDE calls whenever it needs agent-building intelligence.

What makes the pattern more than a code generator is the second and third verb: "what about an AI coding assistant that creates other AI agents, runs them and iterates on them" [0:01:24]. Generation alone leaves a human in the validation loop. A meta-agent that can spin up an isolated sandbox with a database, vector store, and web search can execute what it wrote, observe the failure, and revise, closing a self-feedback loop instead of handing back a guess. That is the same move [self-correcting](./self-correction.md) coding systems make, applied to agent construction.

The end state Cole sketches is compounding. Agents the meta-agent produces are registered as reusable sub-agents in a marketplace, so each build enlarges the library the next build draws from. Framework learning becomes autonomous: good agents and tools it generates are folded back into its own examples, tool library, and even its own system prompt. A grounded tool library also fixes the most wasteful failure mode, hallucinating a tool that has already been written a thousand times. Built in versioned increments, the system doubles as a public teaching artifact, each version introducing a harder concept while staying simple enough to follow.

## Builds on

- [Agentic Coding](./agentic-coding.md) - the meta-agent is a coding agent with a narrowed domain.
- [Agent Development Lifecycle](./agent-development-lifecycle.md) - the build, run, evaluate loop it is automating.
- [Embedding a Coding Agent in Your Application](./embedding-a-coding-agent.md) - Using a coding agent's SDK to programmatically define and embed the same agent harness inside your own apps and workflows, including non-coding work like note-taking, research, and knowledge management.

## Related

- [Subagents Pattern](./subagents-pattern.md) - the produced agents become callable sub-agents.
- [Meta-Harness](./meta-harness.md) - the same abstraction move applied to harnesses rather than agents.
- [Dark Factory](./dark-factory.md) - the fully autonomous end state of a system that ships its own code.
- [System Evolution](./system-evolution.md) - versioned, incremental growth of the meta-agent itself.
- [Self-Evolving Memory](./self-evolving-memory.md) - feeding its own output back into its knowledge base.
- [Self-Correction](./self-correction.md) - running the generated agent to find and fix its own errors.
- [Build Your Own MCP Server](./build-your-own-mcp-server.md) - how the meta-agent exposes itself to an IDE.
- [Abstraction Distraction](./abstraction-distraction.md) - why it targets a small set of frameworks deliberately.
- [Tool Design](./tool-design.md) - the pre-built tool library that stops redundant generation.
- [Handoff Documents](./handoff-documents.md) - Because isolated agents share no conversation history, they communicate by writing and reading markdown handoff files (initial.md, prompts.md) in a shared planning folder, passing only the distilled context each next step needs.

## Tools

- [Archon](../entities/tools/archon.md) - the open-source implementation of the pattern.
- [Pydantic AI](../entities/tools/pydantic-ai.md) - a primary generation target.
- [LangGraph](../entities/tools/langgraph.md) - the other generation target and the meta-agent's own workflow engine.
- [MCP (Model Context Protocol)](../entities/tools/mcp.md) - how an IDE invokes the meta-agent as a sub-agent.
- [Docker](../entities/tools/docker.md) - the isolated environment where generated agents are run.
- [Local AI Package](../entities/tools/local-ai-package.md) - supplies the sandbox services generated agents need.
- [Google Agents CLI](../entities/tools/google-agents-cli.md) - Google's free open-source CLI and skill collection that instructs a coding agent to build, evaluate, deploy, and monitor agents on the ADK.
- [OpenAI o3-mini](../entities/tools/o3-mini.md) - OpenAI's small reasoning model, used as Archon's reasoner to write the scope document before the coder agent builds, and the head-to-head rival to DeepSeek R1 for coding.

## Sources

- [Introducing Archon - an AI Agent that BUILDS AI Agents](../sources/introducing-archon-an-ai-agent-that-builds-ai-agents.md) - "[0:00:00] today it is my pleasure to officially introduce to you archon an open- Source AI agent that literally builds other AI agents"
- [Introducing Archon - an AI Agent that BUILDS AI Agents](../sources/introducing-archon-an-ai-agent-that-builds-ai-agents.md) - "[0:01:24] what about an AI coding assistant that creates other AI agents runs them and iterates on them"
- [Introducing Archon - an AI Agent that BUILDS AI Agents](../sources/introducing-archon-an-ai-agent-that-builds-ai-agents.md) - "[0:01:42] you can think of it like bolt but for agents instead of front ends and a lot more"
