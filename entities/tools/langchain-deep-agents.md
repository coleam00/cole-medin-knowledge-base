---
type: entity
subtype: tool
title: "LangChain Deep Agents"
description: "LangChain's harness implementation for long-running (not just coding) agents that manages context by offloading to file-system tools."
resource: "https://www.langchain.com"
tags: [agent-framework, sdk]
videos: [are-agent-harnesses-bringing-back-vibe-coding]
created: 2026-07-21
updated: 2026-07-21
---

# LangChain Deep Agents

Deep Agents is [LangChain](./langchain.md)'s implementation of the agent harness: the wrapper that connects many agent sessions together so a task can run far longer than any single context window survives. Cole names it while establishing that harnesses are already shipping product rather than theory, "Langchain has built deep agents" [0:03:41], and the detail he pulls out is the one that matters architecturally: "with lane chains deep agents for example, this is not just for coding. They have context management using file system tools" [0:14:19].

Two claims sit inside that sentence. The first is scope. Most harness prior art is coding-shaped (an initializer agent writes a feature list, a task agent loops through it), but Deep Agents generalizes the same machinery to research, operations, and any other work that outlives one session. That is what makes the harness a pattern rather than a coding-tool feature, and it is why [long-running agents](../../concepts/long-running-agents.md) are the unit of design instead of prompts.

The second claim is the mechanism. Context management happens through file-system tools: the agent writes state, findings, and progress out to files and reads back only what the current step needs, instead of dragging an ever-growing transcript forward. That is [context engineering](../../concepts/context-engineering.md) done with the disk as the buffer, the same instinct behind [git as long-term memory](../../concepts/git-as-long-term-memory.md) and [file-system-based agents](../../concepts/file-system-based-agents.md), and it is the standard partial answer to [context rot](../../concepts/context-rot.md): clear the window between sessions and let the file system be the memory.

Cole cites Deep Agents alongside Anthropic's open-sourced harness and [Manus](./manus.md) as evidence the field converged on the same shape independently, and his caution applies equally here. Summarized handoffs still drop the one observation that mattered ten steps later, and [compounding error rates](../../concepts/compounding-error-rates.md) mean a 95 percent reliable step run twenty times is only about 36 percent reliable end to end. File-system context management pushes the ceiling up. It does not remove the need for checkpoints and [human-in-the-loop](../../concepts/human-in-the-loop.md) injection points.

## Realizes

- [AI Coding Harness](../../concepts/ai-coding-harness.md) - The surrounding scaffolding (prompts, tools, rules, validation) that turns a raw model into a reliable coding system.
- [Long-Running Agents](../../concepts/long-running-agents.md) - Agents that run autonomously for hours or days, chaining fresh-context sessions through shared artifact files.
- [File-System-Based Agents](../../concepts/file-system-based-agents.md) - An architecture where agent state and primitives live as files on disk rather than hand-wired framework code.
- [Context Engineering](../../concepts/context-engineering.md) - Deliberately curating exactly what goes into the model's limited context window so outputs stay sharp.
- [Context Reset](../../concepts/context-reset.md) - Clearing or compacting the context window between phases of work to avoid context rot.
- [Context Isolation](../../concepts/context-isolation.md) - Giving each agent or subagent a clean context window so unrelated tokens never dilute the task.

## Works with

- [LangChain](./langchain.md) - The parent framework whose message objects, chains, and integrations Deep Agents is built on.
- [LangGraph](./langgraph.md) - LangChain's stateful graph orchestration layer, the natural substrate for a looped harness.

## Contrasts with

- [Claude Agent SDK](./claude-agent-sdk.md) - Anthropic's harness exposed as a library, the coding-agent route to the same long-task problem.
- [Archon](./archon.md) - Cole's open-source command center and harness builder, which packages a process into deterministic workflows instead of a library.
- [Eve (Vercel)](./eve.md) - Vercel's file-system-first agent framework, which compiles a folder of primitives into a deployable production agent.
- [Manus](./manus.md) - First-of-its-kind general AI agent that pioneered the same context-engineering strategies, cited as parallel prior art.
- [Claude Code](./claude-code.md) - Anthropic's terminal coding agent, the single-session harness Deep Agents generalizes past.

## Related

- [Meta-Harness](../../concepts/meta-harness.md) - A layer above individual coding assistants that orchestrates many of them on larger tasks.
- [Memory Systems](../../concepts/memory-systems.md) - Durable short- and long-term memory so context persists across sessions.
- [Git as Long-Term Memory](../../concepts/git-as-long-term-memory.md) - Treating git history and versioned files as inspectable agent memory.
- [Context Rot](../../concepts/context-rot.md) - Output quality degrading as the window fills with stale accumulated information.
- [Compounding Error Rates](../../concepts/compounding-error-rates.md) - Per-step error rates multiplying across a long chain into low end-to-end reliability.
- [Human in the Loop](../../concepts/human-in-the-loop.md) - Keeping a human as approver and steerer rather than fully automating.
- [Subagents Pattern](../../concepts/subagents-pattern.md) - Delegating scoped tasks to isolated subagents to parallelize work and protect context.
- [Vibe Coding](../../concepts/vibe-coding.md) - Conversationally prompting an AI without reading the code, which harnesses may make viable again in disciplined form.
- [SDK vs. Framework Decision](../../concepts/sdk-vs-framework-decision.md) - Choosing between a batteries-included coding-agent SDK and a from-scratch agent framework.
- [The Evolution of AI Coding](../../concepts/the-evolution-of-ai-coding.md) - Prompt engineering to context engineering to harnesses, the timeline Deep Agents sits at the end of.

## Sources

- [Are Agent Harnesses Bringing Back Vibe Coding?](../../sources/are-agent-harnesses-bringing-back-vibe-coding.md) - "[0:03:41] Langchain has built deep agents."
- [Are Agent Harnesses Bringing Back Vibe Coding?](../../sources/are-agent-harnesses-bringing-back-vibe-coding.md) - "[0:14:19] with lane chains deep agents for example, this is not just for coding. They have context management using file system tools."
