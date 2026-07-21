---
type: entity
subtype: tool
title: "Vercel Agent Browser CLI"
description: "Browser-automation skill used for the final smoke test so the agent verifies the deployed site as a user would."
resource: "https://vercel.com"
tags: [browser-automation, testing, skill, vercel]
videos: [claude-plans-gemini-designs-the-workflow-to-build-beautiful-frontends, full-guide-to-becoming-a-principled-agentic-engineer-build-anything-with-ai, pi-coding-agent-archon-build-any-ai-coding-workflow-no-claude-code-bloat, ive-used-claude-code-for-2000-hours-heres-how-i-build-anything-with-it, this-one-command-makes-coding-agents-find-all-their-mistakes-use-it-now, my-complete-agentic-coding-workflow-to-build-anything-no-fluff-or-overengineering, how-to-properly-use-claude-code-agent-teams-full-live-build, i-was-wrong-about-ralph-wiggum, your-ai-coding-workflow-needs-this-new-agent-browser-cli]
created: 2026-07-21
updated: 2026-07-21
---

# Vercel Agent Browser CLI

The Vercel Agent Browser CLI is a browser-automation tool that lets a coding agent drive a real browser and exercise a running application exactly as a person would. Cole describes the core idea directly: "using the agent browser skill... It's browser automation, so the agent can verify the website testing it as a user actually would" ([0:17:11]). It is the tool he reaches for at the end of a build to close the loop on [End-to-End Validation](../../concepts/end-to-end-validation.md), and he wraps it as one of his reusable [Skills](../../concepts/skills.md) so any agent can call it: "I have my agent browser skill. This is what I use for my browser automation for all my endto-end testing" ([0:17:23]).

## How Cole uses it / why it matters

Agent Browser is Cole's default final smoke test. After an agent spins up the backend and frontend and runs migrations, it navigates the live site to confirm the real user path works: "it's going to use a mix of the agent browser CLI to navigate the website and database queries to make sure that things are looking good in the back end" ([0:06:20]). This makes it the enforcement mechanism behind [Human in the Loop](../../concepts/human-in-the-loop.md) verification and a natural fit after a [Context Reset](../../concepts/context-reset.md), when a fresh agent must prove the work rather than trust its own prior claims. Cole rates it unusually reliable: "for the Vercel agent browser CLI, it's 95%... pretty much going to be 100% if you allow the agent to retry even just once" ([0:02:41]). He is explicit that he prefers it over the alternatives, calling it "a big upgrade over other tools I've used in the past like the Playwright or Puppeteer MCP servers" ([0:15:02]), though he notes [Playwright](./playwright.md) MCP remains a valid substitute. It pairs with [Planning with AI](../../concepts/planning-with-ai.md) up front and often runs as a dedicated validation step within a [Subagents Pattern](../../concepts/subagents-pattern.md) pipeline, and it installs automatically in some of his workflows.

## Realizes

- [End-to-End Validation](../../concepts/end-to-end-validation.md) - validating the whole system through its real interface so the agent proves the feature actually works.
- [Skills](../../concepts/skills.md) - reusable, model-invoked capability packages that load specialized instructions and tools on demand.

## Contrasts with

- [Playwright](./playwright.md) - Cole's deterministic multi-browser automation tool whose MCP server is the alternative Agent Browser upgrades over.

## Works with

- [Claude Code](./claude-code.md) - Anthropic's terminal-based agentic coding assistant.
- [Pi](./pi-coding-agent.md) - a coding agent Cole drives the browser smoke test from.
- [Archon](./archon.md) - Cole's free open-source AI agent that builds other agents.
- [Gemini](./gemini.md) - Google's LLM line used in his frontend builds.
- [Clerk](./clerk.md) - Drop-in authentication and user-management provider for web apps; Cole seeds a Clerk test account so an autonomous agent can sign in and self-validate the real running app.

## Related

- [Human in the Loop](../../concepts/human-in-the-loop.md) - a fresh agent proves the site works rather than trusting its own prior claims.
- [Context Reset](../../concepts/context-reset.md) - clearing an agent's context between phases so a fresh agent must prove the work.
- [Planning with AI](../../concepts/planning-with-ai.md) - producing a detailed plan before implementation so execution follows a reviewed blueprint.
- [Subagents Pattern](../../concepts/subagents-pattern.md) - delegating scoped tasks to isolated subagents; the browser test often runs as a dedicated validation step.

## Sources

- [Claude Plans, Gemini Designs: The Workflow to Build BEAUTIFUL Frontends](../../sources/claude-plans-gemini-designs-the-workflow-to-build-beautiful-frontends.md) - "[0:17:11] using the agent browser skill, I use this all of the time. It's browser automation, so the agent can verify the website testing it as a user actually would."
- [Your AI Coding Workflow NEEDS This New Agent Browser CLI](../../sources/your-ai-coding-workflow-needs-this-new-agent-browser-cli.md) - "[0:02:41] for the Vercel agent browser CLI, it's 95%. It's insanely good because this isn't even considering that it's pretty much going to be 100% if you allow the agent to retry even just once."
- [How to Properly Use Claude Code Agent Teams (FULL LIVE BUILD)](../../sources/how-to-properly-use-claude-code-agent-teams-full-live-build.md) - "[0:15:02] it's a big upgrade over other tools I've used in the past like the Playwright or Puppeteer MCP servers."
- [I've Used Claude Code for 2,000+ Hours - Here's How I Build Anything With It](../../sources/ive-used-claude-code-for-2000-hours-heres-how-i-build-anything-with-it.md) - "[0:17:23] I have my agent browser skill. This is what I use for my browser automation for all my endto-end testing."
- [This One Command Makes Coding Agents Find All Their Mistakes (Use it Now)](../../sources/this-one-command-makes-coding-agents-find-all-their-mistakes-use-it-now.md) - "[0:06:20] it's going to use a mix of the agent browser CLI to navigate the website and database queries to make sure that things are looking good in the back end."
- [Pi Coding Agent + Archon: Build ANY AI Coding Workflow (No Claude Code Bloat)](../../sources/pi-coding-agent-archon-build-any-ai-coding-workflow-no-claude-code-bloat.md) - "[0:15:31] I also want to do browser automation testing with the agent browser CLI. I love using this as a tool to navigate through website just as a user would."
- [FULL Guide to Becoming a Principled Agentic Engineer (Build Anything with AI)](../../sources/full-guide-to-becoming-a-principled-agentic-engineer-build-anything-with-ai.md) - "[0:53:11] if we wanted to use browser automation tools with the agent browser CLI for example... that's actually one of the skills that I have for you guys here"
- [My COMPLETE Agentic Coding Workflow to Build Anything (No Fluff or Overengineering)](../../sources/my-complete-agentic-coding-workflow-to-build-anything-no-fluff-or-overengineering.md) - "[0:29:01] I am actually using the Vercel agent browser CLI skill, which I made a video on... we're going to build in full browser automation."
- [I Was Wrong About Ralph Wiggum](../../sources/i-was-wrong-about-ralph-wiggum.md) - "[0:04:31] I'm also using the Vercel agent browser CLI for browser automation ... You could use something like the Playwright MCP as well. This is just my preferred tool"
