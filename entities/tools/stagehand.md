---
type: entity
subtype: tool
title: "Stagehand"
description: "Browserbase's open-source browser-automation framework, exposed as an MCP server so a coding agent can navigate a deployed site and validate its own work."
resource: "https://www.stagehand.dev"
tags: [observability, validation]
videos: [claude-code-web-just-dropped-but-i-already-built-something-better-with-codex]
created: 2026-07-21
updated: 2026-07-21
---

# Stagehand

Stagehand is [Browserbase](./browserbase.md)'s open-source browser-automation framework, and the way Cole uses it is as the steering layer between an agent and a live browser: "the stage handm is our way to very easily direct our agent to navigate this website" [0:08:17]. Browserbase supplies the remote browser session; Stagehand is the instruction set an LLM can actually drive. Wrapped as an [MCP](./mcp.md) server it becomes a tool any coding agent can call, which turns "go check that the change actually works" into a single natural-language request instead of a hand-written test script.

## How Cole uses it

In his remote agentic coding setup, a [Telegram](./telegram.md) message kicks off [Codex](./codex.md) in a container that clones the repo, branches, and deploys to a staging environment on [Render](./render.md). He then asks the agent to validate the changes in staging, and Stagehand does the looking: "going in the container logs, we can see the different MCP calls to the stage hand MCP. It's creating a remote browser session, visiting our staging URL, making sure all the changes look good, and then reporting that back to us" [0:07:31]. Because the session is remote and recorded, he can open the replay and watch exactly what the agent saw before approving the push from staging to production, which keeps a human in the loop without making the human do the clicking.

He is careful to mark it as optional in the setup, the whole Stagehand MCP layer can be dropped if you would rather open the staging URL yourself. That is the honest framing of what it buys you: not a new capability so much as [end-to-end validation](../../concepts/end-to-end-validation.md) that the agent performs on its own work, through the real interface, with an artifact you can audit afterward.

## Realizes

- [End-to-End Validation](../../concepts/end-to-end-validation.md) - Validating the whole system through its real interface (not just unit-level checks) so the agent proves the feature actually works.
- [Self-Correcting Agents](../../concepts/self-correction.md) - Feeding tool errors and results back to the model so it can reason about mistakes, avoid repeating calls, and retry until it gets the action right.
- [Computer Use](../../concepts/computer-use.md) - Giving an agent control of a computer (mouse, keyboard, screen) so it can operate real software the way a person would.
- [Human in the Loop](../../concepts/human-in-the-loop.md) - Keeping a human as the approver and steerer of agentic work rather than fully automating, so AI augments engineers instead of replacing them.

## Contrasts with

- [Playwright](./playwright.md) - Cole's deterministic multi-browser web automation tool, whose MCP server lets coding assistants visually validate frontend changes.
- [Puppeteer](./puppeteer.md) - Browser-automation MCP server that lets a coding agent load pages, click, and screenshot to visually validate that a feature actually works before marking it passed.
- [Vercel Agent Browser CLI](./agent-browser.md) - Browser-automation skill used for the final smoke test so the agent verifies the deployed site as a user would.
- [QA Tech](./qa-tech.md) - AI testing platform whose agents crawl your deployed site and generate/evolve regression test cases as the codebase grows (has a free tier).

## Works with

- [Browserbase](./browserbase.md) - Browser-automation company Cole partnered with; its Stagehand framework and Director platform bring self-correcting web automation on top of Playwright.
- [MCP (Model Context Protocol)](./mcp.md) - The protocol used to connect Claude Code to external tools and servers.
- [Codex](./codex.md) - OpenAI's cloud-based software-engineering agent integrated with GitHub, plus a Codex CLI.
- [Render](./render.md) - The cloud deployment platform (used on its free tier) that auto-builds and deploys staging on push and production on commit to main.
- [Telegram](./telegram.md) - The messaging app Cole integrates Codex into via the Telegraf library, letting him trigger remote coding jobs from his phone.

## Related

- [Remote Agentic Coding](../../concepts/remote-agentic-coding.md) - Kicking off a coding request from anywhere (phone, chat app) to an agent that runs entirely remotely in an isolated container, cloning the GitHub repo, branching, and deploying on its own.
- [Validation](../../concepts/validation.md) - Building explicit checks into agentic workflows so the AI verifies its own output against real success criteria before moving on.
- [Visual Self-Validation Loop](../../concepts/visual-self-validation.md) - Giving an agent the ability to render its own visual output to an image, look at the screenshot, spot imperfections, and edit the source in place over several iterations.
- [The AI Layer](../../concepts/the-ai-layer.md) - The layer of rules, commands, skills, and context you own on top of a codebase that makes AI coding effective and portable.
- [Agent Observability](../../concepts/agent-observability.md) - Instrumenting agents with tracing, logging, and cost/token metrics so you can see and debug what they actually did.

## Sources

- [Claude Code Web JUST Dropped but I Already Built Something BETTER (with Codex!)](../../sources/claude-code-web-just-dropped-but-i-already-built-something-better-with-codex.md) - "[0:08:17] the stage handm is our way to very easily direct our agent to navigate this website"
- [Claude Code Web JUST Dropped but I Already Built Something BETTER (with Codex!)](../../sources/claude-code-web-just-dropped-but-i-already-built-something-better-with-codex.md) - "[0:07:31] going in the container logs, we can see the different MCP calls to the stage hand MCP. It's creating a remote browser session, visiting our staging URL"
