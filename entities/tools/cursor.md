---
type: entity
subtype: tool
title: "Cursor"
description: "AI coding assistant that can consume AG-UI's llms.txt docs to help build with the protocol."
resource: "https://cursor.com"
tags: [coding-agent, ai-ide]
videos: [ai-exploded-in-2025-heres-everything-that-happened, the-way-we-use-ai-will-completely-change-in-2026-hot-takes, github-is-the-future-of-ai-coding-heres-why, ag-ui-just-released-the-new-wave-of-ai-agent-apps, i-built-the-ultimate-rag-mcp-server-for-ai-coding-better-than-context7, this-mcp-server-for-ai-coding-assistants-will-10x-your-productivity, code-100x-faster-with-ai-heres-how-no-hype-full-process, introducing-archon-an-ai-agent-that-builds-ai-agents, coding-subagents-the-next-evolution-of-ai-ides, insane-new-strategy-for-building-ai-agent-apps, revealing-my-complete-ai-agent-blueprint, claude-computer-use-boltnew-the-ultimate-ai-coding-combo, stop-paying-for-gpt-claude-other-llms-get-them-all-in-one-place]
created: 2026-07-21
updated: 2026-07-21
---

# Cursor

[Cursor](./cursor.md) is the AI-coding IDE that, for a stretch, defined the category. "Cursor reached $500 million in annually recurring revenue," Cole recalls. "At this point, it was very clear that Cursor was the fastest growing platform." It is one of the tools he reaches for interchangeably in tutorials: single-command Archon and skills installs work "in a coding agent like Claude Code or Cursor," and setup instructions cover "cursor and Cline as well."

Cole treats Cursor as a full [agentic coding](../../concepts/agentic-coding.md) environment with strong [context engineering](../../concepts/context-engineering.md) hooks. It ships a built-in docs feature and [MCP](../../concepts/mcp.md) support, though he finds its retrieval weaker than a dedicated server: "In cursor you can even add custom docs. But the performance for this compared to something like Context7 is not that impressive," and its baked-in [RAG](../../concepts/rag.md) is "provably less powerful than Context7." He also uses its `llms.txt` docs ingestion when building against a new protocol.

Beyond the IDE, "we install the cursor CLI ourself. And then we invoke the cursor agent in headless mode... a one-off request with the -p flag," which slots Cursor into scripted, [human-in-the-loop](../../concepts/human-in-the-loop.md) or fully headless pipelines. With the 2.0 update it gained parallel-orchestration features similar to the other frontier tools. Across videos Cursor sits alongside [Windsurf](./windsurf.md) as one of Cole's original go-to AI IDEs, and remains a valid substitute anywhere he demonstrates a workflow, whatever the underlying [model](../../concepts/model-selection.md).

## Realizes

- [Agentic Coding](../../concepts/agentic-coding.md) - Letting an AI agent drive software development end-to-end, from planning through implementation and validation, with human steering.
- [Context Engineering](../../concepts/context-engineering.md) - The deliberate practice of curating exactly what goes into an LLM's limited context window to avoid overload and keep outputs sharp.
- [Model Context Protocol (MCP)](../../concepts/mcp.md) - An open protocol for packaging tools, data, and RAG capabilities as servers that any AI coding assistant or agent can connect to and call with a standard interface.
- [Retrieval-Augmented Generation (RAG)](../../concepts/rag.md) - Grounding an LLM's answers by retrieving relevant documents from an external knowledge base and injecting them into the prompt at query time.
- [Human in the Loop](../../concepts/human-in-the-loop.md) - Keeping a human as the approver and steerer of agentic work rather than fully automating, so AI augments engineers instead of replacing them.
- [Model Selection](../../concepts/model-selection.md) - Choosing the right LLM per task by trading off quality, speed, and cost, often routing easy requests to cheap models and hard ones to expensive models.

## Contrasts with

- [Windsurf](./windsurf.md) - AI coding IDE Cole used to build the Python AG-UI backend and consume the protocol docs; his other original go-to AI IDE alongside Cursor.
- [Claude Code](./claude-code.md) - Anthropic's terminal-based agentic coding assistant.
- [Codex](./codex.md) - OpenAI's cloud-based software-engineering agent integrated with GitHub, plus a Codex CLI.
- [Cline](./cline.md) - An early AI coding driver alongside Aider; PRP was inspired by the Cline community's memory-prompting framework.
- [Kiro](./kiro.md) - Amazon's AI coding assistant, drawing growing enterprise interest after re:Invent.
- [Codeium](../organizations/codeium.md) - The company behind Windsurf, which coined and marketed the 'AI flows' / flow-state framing for AI IDEs.

## Related

- [Context7](./context7.md) - A hosted MCP RAG server for 8,000+ library docs; Cole finds Cursor's built-in docs retrieval provably less powerful than it.

## Sources

- [AI Exploded in 2025 - Here's Everything That Happened](../../sources/ai-exploded-in-2025-heres-everything-that-happened.md) - "[0:06:15] Cursor reached $500 million in annually recurring revenue. At this point, it was very clear that Cursor was the fastest growing platform"
- [The Way We Use AI Will Completely Change in 2026 (Hot Takes)](../../sources/the-way-we-use-ai-will-completely-change-in-2026-hot-takes.md) - "[0:01:20] cursor with their new 2.0 update, they also have something like this."
- [GitHub is the Future of AI Coding (Here's Why)](../../sources/github-is-the-future-of-ai-coding-heres-why.md) - "[0:13:59] we install the cursor CLI ourself. And then we invoke the cursor agent in headless mode... you can just do like a one-off request with the -p flag."
- [AG-UI Just Released: The NEW WAVE of AI Agent Apps](../../sources/ag-ui-just-released-the-new-wave-of-ai-agent-apps.md) - "[0:19:15] developing with cursor, they have this llm's-fold.ext... cursor has their built-in docs feature"
- [I Built the Ultimate RAG MCP Server for AI Coding (Better than Context7)](../../sources/i-built-the-ultimate-rag-mcp-server-for-ai-coding-better-than-context7.md)
- [This MCP Server for AI Coding Assistants Will 10x Your Productivity](../../sources/this-mcp-server-for-ai-coding-assistants-will-10x-your-productivity.md) - "[0:03:24] There are AI coding assistants like Cursor that already have something similar baked into the platform... But this is provably less powerful than Context7."
- [Code 100x Faster with AI, Here's How (No Hype, FULL Process)](../../sources/code-100x-faster-with-ai-heres-how-no-hype-full-process.md)
- [Introducing Archon - an AI Agent that BUILDS AI Agents](../../sources/introducing-archon-an-ai-agent-that-builds-ai-agents.md)
- [Coding Subagents - The Next Evolution of AI IDEs](../../sources/coding-subagents-the-next-evolution-of-ai-ides.md)
- [INSANE New Strategy for Building AI Agent Apps](../../sources/insane-new-strategy-for-building-ai-agent-apps.md)
- [Revealing my COMPLETE AI Agent Blueprint](../../sources/revealing-my-complete-ai-agent-blueprint.md)
- [Claude Computer Use + Bolt.new - The ULTIMATE AI Coding Combo?!](../../sources/claude-computer-use-boltnew-the-ultimate-ai-coding-combo.md)
- [STOP Paying for GPT, Claude, & Other LLMs - Get them ALL in One Place](../../sources/stop-paying-for-gpt-claude-other-llms-get-them-all-in-one-place.md)
