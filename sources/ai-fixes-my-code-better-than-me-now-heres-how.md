---
type: source
title: "AI Fixes My Code Better than Me Now?! (Here's How)"
description: "A single reusable meta command can make any coding agent build a living, end-to-end validation command that tests your whole app like a real user would, catching bugs you'd never find yourself."
youtube_id: d40gE6bKxPk
url: https://www.youtube.com/watch?v=d40gE6bKxPk
slug: ai-fixes-my-code-better-than-me-now-heres-how
published: 2025-11-19
duration: "0:12:53"
recency_rank: 53
raw: "../raw/ai-fixes-my-code-better-than-me-now-heres-how.md"
tags: [validation, piv-loop, agentic-coding]
created: 2026-07-21
updated: 2026-07-21
---

# AI Fixes My Code Better than Me Now?! (Here's How)

Cole argues that validation is the most undervalued part of any AI coding workflow. Most people settle for a few unit tests, some linting, and maybe running the app, but that is not true end-to-end validation. As part of his PIV loop (Plan, Implement, Validate), he set out to push AI validation as far as possible and built a process where the coding agent creates a living, breathing system that validates an entire application end to end, effectively replacing the rigorous manual testing a developer would otherwise do across every user flow.

The centerpiece is a portable meta command. You drop it into any codebase and run it, and it does deep research on your project to figure out how to validate everything end to end, then generates a second command called validate.md that you run going forward. The key unlock was instructing the agent to act as a user and reach for real tools like Docker and the GitHub CLI rather than just unit-test frameworks, and telling it to generate a massive, comprehensive validate document rather than keeping it simple. Because commands are just prompts, the approach works with or without native slash-command support, whether in Claude Code or in Cursor by pasting the path.

Cole demonstrates this on his custom remote coding agent, a Claude-Code-for-the-web system integrating Telegram, GitHub, and multiple assistants. Its generated validate command spins up a throwaway GitHub repo and webhook, simulates Telegram via injected API endpoints, runs Docker and database checks, opens issues and pull requests that tag the agent, and even kicks off coding agents in parallel through the whole PIV loop. It has run consistently a dozen times, caught real bugs he might never have found manually, and lets him kick off a full test, go eat lunch, and return to green check marks. He is careful to note the validation is non-deterministic and he would not ship to production on its word alone, but "me plus the AI" beats "only me."

## Concepts covered

- [End-to-End Validation](../concepts/end-to-end-validation.md)
- [Validation](../concepts/validation.md)
- [The PIV Loop](../concepts/the-piv-loop.md)
- [Commandify Everything](../concepts/commandify-everything.md)
- [Slash Commands](../concepts/slash-commands.md)
- [Prime Command](../concepts/prime-command.md)
- [Human in the Loop](../concepts/human-in-the-loop.md)
- [Planning with AI](../concepts/planning-with-ai.md)

## Entities

- [Cole Medin](../entities/people/cole-medin.md)
- [Claude Code](../entities/tools/claude-code.md)
- [Codex](../entities/tools/codex.md)
- [GitHub](../entities/tools/github.md)
- [Dynamous](../entities/organizations/dynamous.md)

## Key moments

- **[0:00:00]** Cole admits he once refused AI coding assistants, trusting LLMs only for planning, not implementation or validation
- **[0:00:24]** Introduces the PIV loop and frames validation as the most undervalued part of any AI coding workflow
- **[0:01:49]** Reveals the portable meta command that researches a codebase and generates a validate.md command
- **[0:03:34]** Shows the real project: his custom remote coding agent (Claude Code for the web) with Telegram/GitHub integrations
- **[0:05:37]** The unlock: tell the agent to act as a user and use tools like the GitHub CLI for true end-to-end testing
- **[0:06:00]** Live recreation of the original messy prompt that seeded the meta command
- **[0:07:42]** Walks through the generated validate command: type-check, lint, throwaway GitHub repo + webhook, Telegram simulation, DB checks, PR validation
- **[0:10:20]** Non-deterministic but self-correcting; it found real bugs he wouldn't have caught manually
- **[0:10:44]** Shows validate autonomously creating its own issues and PRs (e.g. PR #13) through the full PIV loop

## Transcript

[Raw transcript](../raw/ai-fixes-my-code-better-than-me-now-heres-how.md)
