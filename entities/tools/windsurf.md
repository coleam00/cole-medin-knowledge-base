---
type: entity
subtype: tool
title: "Windsurf"
description: "AI coding IDE Cole used to build the Python AG-UI backend and consume the protocol docs."
resource: "https://windsurf.com"
tags: [coding-agent, ai-ide]
videos: [is-software-engineering-finally-dead, is-gemini-3-really-the-best-ai-ever, my-top-20-lessons-from-building-100s-of-ai-agents-super-actionable, build-any-ai-agent-with-this-context-engineering-blueprint, ai-code-that-fixes-itself-an-mcp-you-can-try-now, all-the-best-rag-strategies-in-one-mcp-for-ai-coding-assistants, ag-ui-just-released-the-new-wave-of-ai-agent-apps, the-3-must-have-mcp-servers-for-any-ai-coding-and-how-to-use-them, i-built-the-ultimate-rag-mcp-server-for-ai-coding-better-than-context7, turn-any-website-into-llm-knowledge-in-seconds-evolved, this-mcp-server-for-ai-coding-assistants-will-10x-your-productivity, the-ultimate-guide-to-building-your-own-mcp-servers-free-template, code-100x-faster-with-ai-heres-how-no-hype-full-process, introducing-archon-an-ai-agent-that-builds-ai-agents, are-you-building-real-ai-agents-or-just-using-llms, coding-subagents-the-next-evolution-of-ai-ides, deploying-billions-of-ai-agents-is-easier-than-you-think, insane-new-strategy-for-building-ai-agent-apps, pydantic-ai-deepseek-v3-the-best-ai-agent-combo, how-to-dominate-with-ai-in-2025, revealing-my-complete-ai-agent-blueprint, im-addicted-to-windsurf-send-help, claude-computer-use-boltnew-the-ultimate-ai-coding-combo]
created: 2026-07-21
updated: 2026-07-21
---

# Windsurf

[Windsurf](./windsurf.md) holds a special place in Cole's story: it was his entry point into AI coding. "November of 2024 is when I installed Windsurf. That was my first AI coding assistant. And man was my brain blown." At the time he was pairing it "with Claude Sonnet 3.5 which is like four generations old at this point," and for a while he was smitten: "it is not even a competition right now Windsurf is hands down the best AI IDE," a "pair programmer with an AI agent."

In practice Windsurf is the IDE where much of his early [agentic coding](../../concepts/agentic-coding.md) happened. He built Pydantic AI agents, Dockerfiles, Streamlit UIs, and "the full Supabase MCP server for us in a single prompt... almost 300 lines of code." Its Cascade mode and one-click [MCP](../../concepts/mcp.md) configuration recur in his MCP tutorials: "click on the hammer icon for MCP servers and then click on configure," and "type at MCP and then hit tab. And now it's going to use [RAG](../../concepts/rag.md) to search the MCP docs for me." That docs-ingestion habit ties directly into his [context engineering](../../concepts/context-engineering.md) message.

Cole is candid that Windsurf is where he learned the failure modes too, an early demo caught a hallucinated method: "This is hallucinated windsurf with Claude 3.7 Sonnet," reinforcing [human-in-the-loop](../../concepts/human-in-the-loop.md) review regardless of [model](../../concepts/model-selection.md). Over time [Claude Code](./claude-code.md) became his primary driver, but Windsurf remains his stand-in for "any AI IDE like Windsurf or Cursor," and it appears throughout as an interchangeable surface next to [Cursor](./cursor.md).

## Realizes

- [Agentic Coding](../../concepts/agentic-coding.md) - Letting an AI agent drive software development end-to-end, from planning through implementation and validation, with human steering.

## Contrasts with

- [Cursor](./cursor.md) - AI coding assistant that can consume AG-UI's llms.txt docs to help build with the protocol.
- [Claude Code](./claude-code.md) - Anthropic's terminal-based agentic coding assistant that is the subject of this complete-guide walkthrough.
- [Cline](./cline.md) - An early AI coding driver alongside Aider; PRP was inspired by the Cline community's memory-prompting framework.
- [Kiro](./kiro.md) - Amazon's AI coding assistant, drawing growing enterprise interest after re:Invent.

## Works with

- [Model Context Protocol (MCP)](../../concepts/mcp.md) - An open protocol for packaging tools, data, and RAG capabilities as servers that any AI coding assistant or agent can connect to and call with a standard interface.
- [Archon](./archon.md) - Cole's free, open-source AI command center and harness builder for AI coding; started as an AI agent that builds other AI agents.

## Related

- [Retrieval-Augmented Generation (RAG)](../../concepts/rag.md) - Grounding an LLM's answers by retrieving relevant documents from an external knowledge base and injecting them into the prompt at query time.
- [Context Engineering](../../concepts/context-engineering.md) - The deliberate practice of curating exactly what goes into an LLM's limited context window - system messages, schemas, chat history, and dynamic variables - to avoid overload and keep outputs sharp.
- [Human in the Loop](../../concepts/human-in-the-loop.md) - Keeping a human as the approver and steerer of agentic work rather than fully automating, so AI augments engineers instead of replacing them.
- [Model Selection](../../concepts/model-selection.md) - Choosing the right LLM per task by trading off quality, speed, and cost, often routing easy requests to cheap models and hard ones to expensive models.

## Sources

- [Is Software Engineering Finally Dead?](../../sources/is-software-engineering-finally-dead.md) - "[0:06:06] finally, November of 2024 is when I installed Windsurf. That was my first AI coding assistant. And man was my brain blown"
- [Is Gemini 3 Really the Best AI Ever?](../../sources/is-gemini-3-really-the-best-ai-ever.md) - "[0:02:46] I was using Windsurf way back in the day... within Windsurf um at this time I was using Claude Sonnet 3.5 which is like four generations old at this point."
- [My Top 20 Lessons from Building 100s of AI Agents (Super Actionable)](../../sources/my-top-20-lessons-from-building-100s-of-ai-agents-super-actionable.md) - "[0:14:25] the sponsor of today's video, which is Windsurf... it was my first ever AI coding assistant."
- [Build ANY AI Agent with this Context Engineering Blueprint](../../sources/build-any-ai-agent-with-this-context-engineering-blueprint.md)
- [AI Code That Fixes Itself (An MCP You Can Try Now)](../../sources/ai-code-that-fixes-itself-an-mcp-you-can-try-now.md)
- [All the BEST RAG Strategies in ONE MCP for AI Coding Assistants](../../sources/all-the-best-rag-strategies-in-one-mcp-for-ai-coding-assistants.md)
- [AG-UI Just Released: The NEW WAVE of AI Agent Apps](../../sources/ag-ui-just-released-the-new-wave-of-ai-agent-apps.md)
- [The 3 MUST Have MCP Servers for Any AI Coding (and How to Use Them)](../../sources/the-3-must-have-mcp-servers-for-any-ai-coding-and-how-to-use-them.md) - "[0:05:16] going into my own Windsurf here, I have the configuration set up."
- [I Built the Ultimate RAG MCP Server for AI Coding (Better than Context7)](../../sources/i-built-the-ultimate-rag-mcp-server-for-ai-coding-better-than-context7.md)
- [Turn ANY Website into LLM Knowledge in Seconds - EVOLVED](../../sources/turn-any-website-into-llm-knowledge-in-seconds-evolved.md)
- [This MCP Server for AI Coding Assistants Will 10x Your Productivity](../../sources/this-mcp-server-for-ai-coding-assistants-will-10x-your-productivity.md)
- [The ULTIMATE Guide to Building Your Own MCP Servers (Free Template)](../../sources/the-ultimate-guide-to-building-your-own-mcp-servers-free-template.md)
- [Code 100x Faster with AI, Here's How (No Hype, FULL Process)](../../sources/code-100x-faster-with-ai-heres-how-no-hype-full-process.md) - "[0:20:35] Windsurf created the full Supabase MCP server for us in a single prompt. And this is not a basic implementation. It's almost 300 lines of code."
- [Introducing Archon - an AI Agent that BUILDS AI Agents](../../sources/introducing-archon-an-ai-agent-that-builds-ai-agents.md)
- [Are You Building REAL AI Agents or Just Using LLMs?](../../sources/are-you-building-real-ai-agents-or-just-using-llms.md)
- [Coding Subagents - The Next Evolution of AI IDEs](../../sources/coding-subagents-the-next-evolution-of-ai-ides.md)
- [Deploying Billions of AI Agents is Easier than You Think](../../sources/deploying-billions-of-ai-agents-is-easier-than-you-think.md)
- [INSANE New Strategy for Building AI Agent Apps](../../sources/insane-new-strategy-for-building-ai-agent-apps.md)
- [Pydantic AI + DeepSeek V3 - The BEST AI Agent Combo](../../sources/pydantic-ai-deepseek-v3-the-best-ai-agent-combo.md)
- [How to DOMINATE with AI in 2025](../../sources/how-to-dominate-with-ai-in-2025.md)
- [Revealing my COMPLETE AI Agent Blueprint](../../sources/revealing-my-complete-ai-agent-blueprint.md)
- [I'm Addicted to Windsurf, Send Help](../../sources/im-addicted-to-windsurf-send-help.md) - "[0:00:00] it is not even a competition right now Windsurf is hands down the best AI IDE it combines The Best of Both Worlds"
- [Claude Computer Use + Bolt.new - The ULTIMATE AI Coding Combo?!](../../sources/claude-computer-use-boltnew-the-ultimate-ai-coding-combo.md)
