---
type: concept
title: "Tool Design"
description: "Designing agent tools to be few, single-purpose, and well-described (often via docstrings) so the model uses them reliably."
tags: [tools, design, docstrings, agents, mcp, tool-calling]
videos: [your-ai-coding-workflow-needs-this-new-agent-browser-cli, learn-90-of-building-ai-agents-in-30-minutes, my-top-20-lessons-from-building-100s-of-ai-agents-super-actionable, build-and-ship-any-mcp-server-in-minutes-full-guide, google-anthropic-and-openais-guides-to-ai-agents-all-in-18-minutes, the-ultimate-guide-to-building-your-own-mcp-servers-free-template, code-100x-faster-with-ai-heres-how-no-hype-full-process, introducing-archon-an-ai-agent-that-builds-ai-agents, coding-subagents-the-next-evolution-of-ai-ides, you-have-to-try-agentic-rag-with-deepseek-r1-insane-results, openais-swarm-a-game-changer-for-ai-agents, llama-32-is-insane-but-does-it-beat-gpt-as-an-ai-agent, dont-sleep-on-the-ultimate-ai-agent-combo-n8n-langchain-python, openais-o1-is-barely-usable-but-i-fixed-it, this-ai-agent-with-rag-manages-my-life, function-calling-with-any-llm-for-local-ai-agents-feat-langchain-huggingface-and-llama-3, ai-agents-just-got-sexy-ai-agents-masterclass-3, the-secret-sauce-for-simple-powerful-ai-apps-ai-agents-masterclass-2, developers-this-is-how-you-stay-relevant-with-ai-ai-agents-masterclass-1, use-chatgpt-in-two-clicks-on-any-website-with-a-custom-chrome-extension]
created: 2026-07-21
updated: 2026-07-21
---

# Tool Design

Tool design is the craft of shaping the functions you give an agent so the model reaches for the right one and calls it correctly. Three rules recur across Cole's builds: keep the set small, keep each tool single-purpose, and describe each one well. On count and distinctness: "you should keep your tools to under 10 for your AI agents, at least when starting out. And you definitely want to make sure that each tool's purpose is very distinct" [0:12:21], because "if your tools have overlapping functionality or if you have too many, then your large language model starts to get overwhelmed" [0:12:47]. The same principle drives MCP servers: "we want modular singlepurpose tools so the LLM doesn't get confused when it's using our MCP server and descriptions are very important for that" [0:15:10].

Descriptions are the load-bearing part, and in Python the docstring is where they live. "The descriptions that you give to your tools are key because everything that you give as a part of the tool description is indeed included in the prompt to the LLM to tell it when and how to use a tool" [0:41:34]. This is a cross-framework constant: "just like with LangChain and Pydantic AI and other Frameworks we use this dock string right here this comment at the start of the function to tell the llm when and how to use this tool specifically" [0:10:54]. A good docstring gives a description, an example call, and every argument in detail, including format constraints that will otherwise break the call: the date format "is really really important if you give a bad date format then Asana won't be able to create the task" [0:09:12]. A nice property is that this is documentation you would write anyway: "everything here you'd have anyway because you want to have doc strings in your python code for good documentation anyway" [0:04:24].

Two further design choices matter. First, return only what the model needs: "you want to make sure that what you return is just the information that you care about giving back to the LLM" [0:45:47], and fail gracefully so a bad call does not crash the app but tells the agent "exactly what went wrong" [0:44:13]. Second, sometimes the best design is fewer, more powerful tools. Giving an agent one flexible tool to write its own SQL against a schema hit "a 100% success rate" [0:05:42] by getting "out of the way of the agent to make it as flexible as possible" [0:06:07]. Prebuilt tool libraries extend this: reusing a proven tool means "we don't have to worry about hallucinating the creation of tools" [0:13:10].

## Prerequisites

- [Tool Calling](./tool-use.md) - tool design only matters because the model must choose and invoke these functions itself.

## Builds on

- [What Is an AI Agent](./what-is-an-ai-agent.md) - well-designed tools are what make the agent capable rather than confused.

## Contrasts with

- [Structured Outputs](./structured-outputs.md) - both lean on schemas, but tool design governs the interface the agent acts through, not the shape of its final reply.

## Related

- [Model Context Protocol (MCP)](./mcp.md) - "MCP servers are a great way to find preackaged sets of tools you can bring into your an agent" [0:12:47].
- [The Problems With MCP Servers](./mcp-problems.md) - overloading an agent with too many MCP tools is the failure mode tool design guards against.
- [Context Engineering](./context-engineering.md) - every tool and its description spends the context budget, so fewer, sharper tools pay off.
- [Agent Core Components](./agent-core-components.md) - tools are one of the core components, alongside the model and instructions.
- [Few-Shot Prompting](./few-shot-prompting.md) - example calls inside a docstring are few-shot guidance for tool use.
- [Agentic RAG](./agentic-rag.md) and [Retrieval-Augmented Generation (RAG)](./rag.md) - retrieval is often exposed to the agent as a single, well-described tool.
- [Streaming Responses](./streaming-responses.md) - tool-calling adds a second model call, which complicates streaming the response.
- [Chat Interfaces](./chat-interfaces.md) - the surface where tool results ultimately reach the user.

## Tools

- [Archon](../entities/tools/archon.md) - pulls tools from a prebuilt library so it does not hallucinate them "from scratch" [0:12:56].
- [Pydantic AI](../entities/tools/pydantic-ai.md), [LangChain](../entities/tools/langchain.md), and [OpenAI Swarm](../entities/tools/openai-swarm.md) - frameworks that read the function docstring as the tool description.
- [n8n](../entities/tools/n8n.md) - where "it takes more space to write the doc string than it actually does to create any of these tools" [0:15:05].
- [Vercel Agent Browser CLI](../entities/tools/agent-browser.md) and [Brave Search API](../entities/tools/brave-search.md) - examples of the few-flexible-tools approach.

## Sources

- [Learn 90% of Building AI Agents in 30 Minutes](../sources/learn-90-of-building-ai-agents-in-30-minutes.md) - "you should keep your tools to under 10 for your AI agents, at least when starting out. And you definitely want to make sure that each tool's purpose is very distinct" [0:12:21]
- [My Top 20 Lessons from Building 100s of AI Agents (Super Actionable)](../sources/my-top-20-lessons-from-building-100s-of-ai-agents-super-actionable.md) - "the descriptions that you give to your tools are key because everything that you give as a part of the tool description is indeed included in the prompt to the LLM to tell it when and how to use a tool." [0:41:34]
- [Build and Ship Any MCP Server in MINUTES (Full Guide)](../sources/build-and-ship-any-mcp-server-in-minutes-full-guide.md) - "We want modular singlepurpose tools so the LLM doesn't get confused when it's using our MCP server and descriptions are very important for that." [0:15:10]
- [The ULTIMATE Guide to Building Your Own MCP Servers (Free Template)](../sources/the-ultimate-guide-to-building-your-own-mcp-servers-free-template.md) - "this dock string ... is actually crucial because whatever we write right here is the description for the tool that's given to the LLM." [0:18:29]
- [Your AI Coding Workflow NEEDS This New Agent Browser CLI](../sources/your-ai-coding-workflow-needs-this-new-agent-browser-cli.md) - "what if we just give it two tools? Primarily a tool to write whatever SQL the agent wants given the schema... when they did this, they got to a 100% success rate." [0:05:42]
- [You HAVE to Try Agentic RAG with DeepSeek R1 (Insane Results)](../sources/you-have-to-try-agentic-rag-with-deepseek-r1-insane-results.md) - "just like with LangChain and Pydantic AI and other Frameworks we use this dock string right here this comment at the start of the function to tell the llm when and how to use this tool specifically" [0:10:54]
- [Introducing Archon - an AI Agent that BUILDS AI Agents](../sources/introducing-archon-an-ai-agent-that-builds-ai-agents.md) - "we don't have to worry about hallucinating the creation of tools when that's a tool that's already been built a thousand times" [0:13:10]
- [Google, Anthropic, and OpenAI's Guides to AI Agents ALL in 18 Minutes](../sources/google-anthropic-and-openais-guides-to-ai-agents-all-in-18-minutes.md) - "You also want clear instructions. This is both for your system prompt and then also for the descriptions that you give the agent for your tools so it knows how to leverage those effectively" [0:13:42]
- [The Secret Sauce for SIMPLE + POWERFUL AI Apps - AI Agents Masterclass #2](../sources/the-secret-sauce-for-simple-powerful-ai-apps-ai-agents-masterclass-2.md) - "everything here you'd have anyway because you want to have doc strings in your python code for good documentation anyway" [0:04:24]
