---
type: source
title: "Code 100x Faster with AI, Here's How (No Hype, FULL Process)"
description: "A repeatable, tool-agnostic process (golden rules, planning/task markdown docs, global rules, MCP servers, and disciplined one-feature-at-a-time prompting) is what turns AI coding assistants from erratic to consistently high-output."
youtube_id: SS5DYx6mPw8
url: https://www.youtube.com/watch?v=SS5DYx6mPw8
slug: code-100x-faster-with-ai-heres-how-no-hype-full-process
published: 2025-03-30
duration: "0:32:10"
recency_rank: 105
raw: "../raw/code-100x-faster-with-ai-heres-how-no-hype-full-process.md"
tags: [agentic-coding, planning-with-ai, global-rules, mcp, workflow]
created: 2026-07-21
updated: 2026-07-21
---

Cole walks through his full end-to-end workflow for coding with AI, arguing that the difference between great and terrible results is not the model or the IDE but having a refined, deliberate process. He opens with "golden rules": use higher-level markdown documents (planning, tasks, installation, docs) to feed the LLM context; do not overwhelm the model (keep files under 500 lines, start fresh conversations often, ask for only one feature per prompt); always have the AI write tests after each feature; be specific about technologies and libraries; write docs and comments continuously; and never trust the LLM with environment variables, API keys, or database security (illustrated by a cautionary tale of a vibe-coded SaaS that got hacked two days after launch).

He then executes the workflow to build a Supabase MCP server. The phases: (1) plan first in a chatbot like Claude Desktop, generating planning.md (vision, architecture, tech stack) and task.md (trackable tasks), optionally using multiple LLMs to plan; (2) set up global/workspace rules that act as a persistent system prompt so prompts can stay short; (3) configure his core three MCP servers, filesystem, Brave web search, and Git; (4) give a detailed initial prompt that supplies documentation and a GitHub example. Windsurf one-shots a roughly 300-line working server by reading the docs and the planning/task files.

He finishes by covering the disciplined iteration loop: commit to Git at every good state so you can revert when the AI breaks things, add the tests and README the model skipped (one change at a time), and deploy via a Docker file the LLM writes. The recurring theme is that the human stays the project manager, dictating scope, verifying security, and using markdown docs plus Git as durable context and safety nets.

## Concepts covered

- [Agentic Coding](../concepts/agentic-coding.md)
- [Planning with AI](../concepts/planning-with-ai.md)
- [Two-Layer Planning](../concepts/two-layer-planning.md)
- [Context Engineering](../concepts/context-engineering.md)
- [Context Reset](../concepts/context-reset.md)
- [Global Rules](../concepts/global-rules.md)
- [Reduce Assumptions](../concepts/reduce-assumptions.md)
- [Validation](../concepts/validation.md)
- [One Feature Per Prompt](../concepts/one-feature-per-prompt.md)
- [Git as Long-Term Memory](../concepts/git-as-long-term-memory.md)
- [Vibe Coding](../concepts/vibe-coding.md)
- [Agent Security](../concepts/agent-security.md)
- [Learn by Building](../concepts/learn-by-building.md)
- [Human in the Loop](../concepts/human-in-the-loop.md)
- [Tool Design](../concepts/tool-design.md)
- [Model Context Protocol (MCP)](../concepts/mcp.md)

## Entities

- [Cole Medin](../entities/people/cole-medin.md)
- [Windsurf](../entities/tools/windsurf.md)
- [Cursor](../entities/tools/cursor.md)
- [Claude Code](../entities/tools/claude-code.md)
- [Supabase](../entities/tools/supabase.md)
- [MCP (Model Context Protocol)](../entities/tools/mcp.md)
- [Brave Search API](../entities/tools/brave-search.md)
- [GitHub](../entities/tools/github.md)
- [Docker](../entities/tools/docker.md)
- [Archon](../entities/tools/archon.md)
- [Dynamous](../entities/organizations/dynamous.md)
- [Qdrant](../entities/tools/qdrant.md)

## Key moments

- **[0:02:33]** Golden rules introduced: use markdown context docs, don't overwhelm the LLM, keep files under 500 lines, fresh conversations, one feature per prompt
- **[0:04:38]** Security rule: implement environment variables yourself; cautionary tale of a vibe-coded SaaS hacked two days after launch
- **[0:05:45]** Planning phase: create planning.md (vision/architecture) and task.md before writing any code
- **[0:09:11]** Tip: use multiple LLMs to plan and combine results
- **[0:10:35]** Global rules = persistent system prompt so prompts stay simple (e.g. always read planning file at start)
- **[0:13:30]** MCP configuration: the core three servers, filesystem, Brave web search, Git
- **[0:16:55]** Initial prompt: be specific, supply documentation and a GitHub example three ways
- **[0:19:55]** Windsurf reads docs + planning/task files and one-shots a ~300-line Supabase MCP server
- **[0:23:53]** Commit to Git at a good state so you can revert when the AI breaks things later
- **[0:25:34]** Iterate one change at a time, add the README and tests the model skipped
- **[0:29:28]** Deployment: LLM writes a Docker file to package and ship the project

## Transcript

[Raw transcript](../raw/code-100x-faster-with-ai-heres-how-no-hype-full-process.md)
