---
type: entity
subtype: tool
title: "Visual Studio Code"
description: "Microsoft's editor where Cole drops LLM-generated Python, fills in placeholders, and runs the app from the integrated terminal."
resource: "https://code.visualstudio.com"
tags: [ai-coding, coding-agent]
videos: [build-a-full-stack-app-for-your-n8n-ai-agent-in-20-minutes]
created: 2026-07-21
updated: 2026-07-21
---

# Visual Studio Code

Visual Studio Code is Microsoft's general-purpose code editor, and in Cole's catalog it plays a deliberately unglamorous role: it is the plain editor where LLM-written code lands and runs. The moment that defines it comes at the seam between the no-code half and the code half of a build: "we now have everything that we need to just dump our python code from Claude into Visual Studio code" [0:08:18]. VS Code is not the agent here. It is the surface where the agent's output becomes a running program.

The workflow around that line is instructive. The [n8n](./n8n.md) RAG agent is already built and exposed over a webhook, [Claude](./claude.md) has written the Python client, and VS Code is where Cole creates a new file, pastes the generated script, and touches "literally nothing besides the placeholders" (the webhook URL and the bearer token). He installs dependencies from a requirements file and launches the front end with `streamlit run` from the integrated terminal, which pops a working chat widget in the browser. That is a [full-stack AI application](../../concepts/full-stack-ai-application.md) assembled in minutes, and it is the concrete shape of the [hybrid no-code plus code architecture](../../concepts/hybrid-no-code-and-code.md): orchestration stays in n8n, the interface and the glue live in [Python](./python.md) files in the editor.

VS Code is also the baseline the rest of this bundle's editors are measured against. [Cursor](./cursor.md) and [Windsurf](./windsurf.md) are the AI-native forks of it, [Zed](./zed.md) is introduced as "a code editor just like VS Code and its forks," and Cole expects VS Code to eventually pick up the [Agent Client Protocol](../../concepts/agent-client-protocol.md) as well. Reading it as the null hypothesis clarifies what the agentic editors actually add: everything a driver like [Claude Code](./claude-code.md) does around the file, VS Code leaves to you.

## Realizes

- [Full-Stack AI Application](../../concepts/full-stack-ai-application.md) - Combining an AI agent with a real front end, database, and API integrations, with the agent acting as the brain connecting the UI to back-end services.
- [Hybrid No-Code + Code Architecture](../../concepts/hybrid-no-code-and-code.md) - Reject the either/or: use n8n for orchestration, entry points, and integrations while offloading heavy processing (agents, RAG chunking, large files) to Python microservices deployed on the same instance.

## Works with

- [Python](./python.md) - Language Auto-GPT is built in; requires Python 3.8+ to run.
- [Streamlit](./streamlit.md) - Used to build the travel-planner's chat UI, where users set preferences and watch the streamed synthesizer output.
- [Claude](./claude.md) - Named as an example of a large language model that can be turned into an agent.
- [n8n](./n8n.md) - A no-code AI automation platform for building agents and workflows that integrate with 500+ applications.

## Contrasts with

- [Cursor](./cursor.md) - AI coding assistant that can consume AG-UI's llms.txt docs to help build with the protocol.
- [Windsurf](./windsurf.md) - AI coding IDE Cole used to build the Python AG-UI backend and consume the protocol docs.
- [Zed](./zed.md) - A free, open-source code editor from the team that created the Agent Client Protocol, shipping the first beta ACP implementation with native Gemini CLI and adapter-based Claude Code support.
- [Claude Code](./claude-code.md) - Anthropic's terminal-based agentic coding assistant that is the subject of this complete-guide walkthrough.
- [iTerm2](./iterm2.md) - macOS terminal application with split-pane support; one of only two terminals Claude Code can drive to display agent teams live.

## Related

- [AI Coding Assistant](../../concepts/ai-coding-assistant.md) - A tool that generates or completes code from short prompts, applying targeted edits and offloading low-leverage software work.
- [No-Code vs. Code](../../concepts/no-code-vs-code.md) - The use-case-by-use-case decision to build agents visually or in code, often starting no-code for speed then migrating to Python when hitting a feature ceiling.
- [Agent Client Protocol (ACP)](../../concepts/agent-client-protocol.md) - An open standard for connecting any coding agent to any code editor, the agent-to-editor analog of MCP.
- [The Evolution of AI Coding](../../concepts/the-evolution-of-ai-coding.md) - How AI coding assistants moved from novelty to daily driver, and where the landscape, adoption, and commentary are heading.
- [Chat Interfaces](../../concepts/chat-interfaces.md) - Wrapping agents in chat surfaces (websites, DMs, platforms) with adapters, a shared message format, and durable history.

## Sources

- [Build a FULL Stack App for your n8n AI Agent in 20 Minutes](../../sources/build-a-full-stack-app-for-your-n8n-ai-agent-in-20-minutes.md) - "[0:08:18] we now have everything that we need to just dump our python code from Claude into Visual Studio code"
