---
type: source
title: "The BIG Problem with MCP Servers (and the Solution!)"
description: "MCP servers bloat an agent's context by loading every tool definition up front, and the fix is code execution via skills that load capabilities on demand, trading MCP's control for far greater token efficiency and flexibility."
youtube_id: 1_z3h2r93OY
url: https://www.youtube.com/watch?v=1_z3h2r93OY
slug: the-big-problem-with-mcp-servers-and-the-solution
published: 2025-11-09
duration: "0:10:22"
recency_rank: 55
raw: "../raw/the-big-problem-with-mcp-servers-and-the-solution.md"
tags: [mcp, context-engineering, skills]
created: 2026-07-21
updated: 2026-07-21
---

# The BIG Problem with MCP Servers (and the Solution!)

Cole breaks down the central flaw with MCP that Anthropic itself admitted to: MCP servers are token-inefficient and rigid because every tool definition and every tool call fills the context window before the first message is even sent. He demonstrates with five standard AI-coding MCP servers connected in Claude Code, where /context shows MCP tools alone consuming 97,000 tokens, about 48% of Claude Sonnet 4.5's window. Even multi-million-token models are overwhelmed by loading all capabilities up front.

The proposed solution is real-time discovery and code execution. Rather than loading dozens of tool definitions eagerly, the agent searches a folder of capabilities, loads only the relevant instruction set and code when a user query calls for it (for example Google Drive), and can generate and reuse scripts to hit API endpoints directly. Since most MCP servers are just API wrappers, letting the agent write its own code to call the API is both far cheaper and more flexible. Anthropic's Agent Skills embody this pattern: only a short skill description sits in context at the start, roughly 2-3% of MCP's token cost, with the full instructions and code loaded on demand. Cole converted the Archon MCP server into a skill and proved it retains all functionality at a couple hundred tokens up front.

He closes by asking whether this is the end of MCP and answers no. MCP's strength is "what you see is what you get." The server author defines exactly which tools are exposed, giving control, predictability, credential and env-var management, and less risk of missed capabilities. Code execution is flexible and efficient but risky and complicated, with sandboxing and security to manage. The real tension is control versus flexibility, and Cole bets flexibility wins over time as LLMs get more capable and trustworthy with code.

## Concepts covered

- [The Problems With MCP Servers](../concepts/mcp-problems.md)
- [Context Rot](../concepts/context-rot.md)
- [Code Execution](../concepts/code-execution.md)
- [Progressive Disclosure](../concepts/progressive-disclosure.md)
- [Skills](../concepts/skills.md)
- [Model Context Protocol (MCP)](../concepts/mcp.md)

## Entities

- [MCP (Model Context Protocol)](../entities/tools/mcp.md)
- [Anthropic](../entities/organizations/anthropic.md)
- [Claude Code](../entities/tools/claude-code.md)
- [Archon](../entities/tools/archon.md)
- [Dynamous](../entities/organizations/dynamous.md)
- [Cole Medin](../entities/people/cole-medin.md)

## Key moments

- **[0:00:00]** Framing: MCP's major flaw is token consumption and context rot, and Anthropic (the protocol's creator) admitted it in a blog post
- **[0:00:58]** The problem stated: MCP servers are token-inefficient and rigid because tool definitions and calls both fill the context window
- **[0:02:23]** Live demo: /context in Claude Code shows MCP tools consuming 97,000 tokens = 48% of Sonnet 4.5's window
- **[0:02:53]** The solution: real-time discovery, load a capability's context only when needed, or generate it on the fly (code execution)
- **[0:03:47]** Insight that most MCP servers are just API wrappers; let the agent write code to hit the API directly instead of a tool middleman
- **[0:05:24]** Agent Skills as the embodiment of the solution: only the short skill description sits in context up front
- **[0:07:11]** Cole converted the Archon MCP server into a skill, same functionality, hundreds of tokens instead of 90k up front
- **[0:08:02]** Is this the end of MCP? No, the control vs flexibility trade-off, with Cole betting flexibility wins over time

## Transcript

[Raw transcript](../raw/the-big-problem-with-mcp-servers-and-the-solution.md)
