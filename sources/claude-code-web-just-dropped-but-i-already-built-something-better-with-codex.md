---
type: source
title: "Claude Code Web JUST Dropped but I Already Built Something BETTER (with Codex!)"
description: "Instead of using locked-down cloud coding tools like Claude Code for the web, you can use the Codex SDK to build your own remote agentic coding assistant that carries your full AI layer and integrates with any app like Telegram."
youtube_id: injqJTy5Tus
url: https://www.youtube.com/watch?v=injqJTy5Tus
slug: claude-code-web-just-dropped-but-i-already-built-something-better-with-codex
published: 2025-10-22
duration: "0:18:01"
recency_rank: 60
raw: "../raw/claude-code-web-just-dropped-but-i-already-built-something-better-with-codex.md"
tags: [ai-coding-harness, codex, provider-independence]
created: 2026-07-21
updated: 2026-07-21
---

# Claude Code Web JUST Dropped but I Already Built Something BETTER (with Codex!)

Cole reacts to Anthropic's release of Claude Code for the web (and similar remote agentic coding tools like Jules and Codex Cloud) by arguing they lack the flexibility he wants. You cannot define your own commands and prompts, wire in your own MCP servers, or keep your AI layer where you send requests. His answer is a custom solution built on OpenAI's Codex SDK, integrated directly into Telegram, so he can kick off a fully remote coding job from his phone with his own workflow powering the bot.

The bulk of the video is a live end-to-end demo. From Telegram he asks Codex to update his coach.dynamous.ai website copy. A container clones the repo, creates a feature branch, pushes to a staging environment (deployed via Render's free tier), and reports back staging URLs. A workflow defined entirely in an agents.md file governs these steps. For validation he uses a Stagehand MCP server on Browserbase so the agent visits the deployed staging site itself and produces a session replay he can watch, keeping a human in the loop before he authorizes the final push from staging to production.

Under the hood he explains the Codex SDK, a TypeScript library mirroring the Claude Agent SDK: import it, start a thread, run it with the latest prompt, and it auto-loads your slash commands and agents.md AI layer. He streams events for real-time tool-call visibility in Telegram, resumes threads by thread ID for persistent per-user conversations, and handles auth by copying Codex and GitHub credentials into container environment variables. His broader thesis: the future of AI coding is using SDKs to build your own coding assistants that integrate with any application, not relying on any single vendor's cloud UI.

## Concepts covered

- [AI Coding Harness](../concepts/ai-coding-harness.md)
- [Provider Independence](../concepts/provider-independence.md)
- [The AI Layer](../concepts/the-ai-layer.md)
- [Human in the Loop](../concepts/human-in-the-loop.md)
- [End-to-End Validation](../concepts/end-to-end-validation.md)
- [Agentic Coding](../concepts/agentic-coding.md)
- [Code Execution](../concepts/code-execution.md)
- [Memory Systems](../concepts/memory-systems.md)

## Entities

- [Codex](../entities/tools/codex.md)
- [Claude Code](../entities/tools/claude-code.md)
- [Claude Agent SDK](../entities/tools/claude-agent-sdk.md)
- [Telegram](../entities/tools/telegram.md)
- [Browserbase](../entities/tools/browserbase.md)
- [Render](../entities/tools/render.md)
- [GitHub](../entities/tools/github.md)
- [OpenAI](../entities/organizations/openai.md)
- [Anthropic](../entities/organizations/anthropic.md)
- [Cole Medin](../entities/people/cole-medin.md)

## Key moments

- **[0:00:00]** Frames Anthropic's Claude Code for the web + other remote coding tools (Jules, Codex Cloud), and why they lack flexibility/control
- **[0:01:05]** Reveals his alternative: Codex integrated directly into Telegram with his own workflow
- **[0:03:14]** Demo setup: update coach.dynamous.ai from his phone via Telegram, deploy to staging first
- **[0:04:35]** Container clones repo, creates branch, follows a workflow defined in agents.md, pushes to staging
- **[0:06:44]** Human-in-the-loop validation via Stagehand MCP + Browserbase browser session with a replay
- **[0:08:49]** After validation, approves push from staging to production, Render auto-deploys on commit to main
- **[0:10:30]** Explains the Codex SDK: TypeScript library, threads, run/run-stream, auto-loading the AI layer
- **[0:13:03]** Authentication: copy Codex auth.json + GitHub token into container env vars

## Transcript

[Raw transcript](../raw/claude-code-web-just-dropped-but-i-already-built-something-better-with-codex.md)
