---
type: entity
subtype: tool
title: "Pi"
description: "A minimalistic, open-source coding agent cited as another example of a company-built harness around a model."
resource: "https://github.com/earendil-works/pi"
tags: [coding-agent, open-source, harness]
videos: [the-creators-of-claude-code-and-openclaw-dont-prompt-their-agents-anymore, omnigent-the-new-meta-harness-for-every-coding-agent-claude-code-codex-pi-more, harness-engineering-what-separates-top-agentic-engineers-right-now, pi-coding-agent-archon-build-any-ai-coding-workflow-no-claude-code-bloat, the-next-evolution-of-ai-coding-is-harnesses-heres-how-to-build-them]
created: 2026-07-21
updated: 2026-07-21
---

# Pi

Pi is a minimalistic, open-source coding agent built to be the opposite of the heavyweight assistants that dominate the space. As Cole puts it, "Pi is a minimalistic open-source coding agent, and minimalistic is really important here because Pi is fighting the bloat that we see with so many other coding agents right now" ([0:00:00]). Its design philosophy is deliberately spare: "let's just strip away everything, build a minimal extensible core and make the agent modify itself" ([0:03:37]). That extensible core is what makes it interesting to Cole, who treats a coding agent as a stripped-down [AI Coding Harness](../../concepts/ai-coding-harness.md) you compose yourself rather than a finished product you accept as-is.

## How Cole uses it

Pi is Cole's preferred driver for orchestrated workflows. He runs it against non-Anthropic models to keep his stack provider-flexible: "I'm driving everything with Pi. So I'm actually using my Kimi subscription with Kimi K 2.7 to drive all of these workflows" ([0:19:04]), a direct expression of deliberate [Model Selection](../../concepts/model-selection.md). Because Pi exposes an API layer, it slots into larger systems: "It'll connect to the backend with the API that I have running with Pi" ([0:22:05]). In [Archon](./archon.md) it became "the third coding agent supported," giving Cole a lean alternative to the bigger agents when doing [Agentic Workflow Engineering](../../concepts/agentic-workflow-engineering.md). Pi is also a recurring member of the "you name the millions of coding agents out there" list ([0:01:56]) alongside [Claude Code](./claude-code.md) and [Codex](./codex.md), and it can be pointed at a local model through meta-harnesses: "if I even wanted to use Pi with Ollama for some local development, I can even do that" ([0:05:23]) via [Ollama](./ollama.md). Cole has flagged the Pi Agent SDK as a coding assistant he wants to wire into his own harnesses next.

## Realizes

- [AI Coding Harness](../../concepts/ai-coding-harness.md) - The surrounding scaffolding (prompts, tools, rules, validation) that turns a raw model into a reliable coding system.
- [Model Selection](../../concepts/model-selection.md) - Choosing the right LLM per task by trading off quality, speed, and cost, often routing easy requests to cheap models and hard ones to expensive models.
- [Agentic Workflow Engineering](../../concepts/agentic-workflow-engineering.md) - Designing repeatable AI workflows as engineered systems with defined steps, orchestration, and background execution rather than ad-hoc prompting.
- [Parallel Agentic Coding](../../concepts/parallel-agentic-coding.md) - Dispatching agents to background tasks in isolated git worktrees, each fed repo context and returning a reviewable PR.
- [Context Isolation](../../concepts/context-isolation.md) - Giving each agent or subagent its own clean context window so unrelated tokens never dilute the task at hand.
- [Human in the Loop](../../concepts/human-in-the-loop.md) - Keeping a human as the approver and steerer of agentic work rather than fully automating, so AI augments engineers instead of replacing them.
- [Coding-Agent Bloat](../../concepts/coding-agent-bloat.md) - The critique that feature-maxed coding tools accumulate bugs, heavy token usage, and an uncontrollable, constantly-shifting system prompt that degrades and obscures results, arguing for minimal, moldable foundations instead.

## Works with

- [Archon](./archon.md) - Cole's free, open-source AI command center and harness builder for AI coding; started as an AI agent that builds other AI agents.
- [Retool](./retool.md) - Internal-app platform that imports React code and connects to a database to deploy dashboards with a governed, permissioned, audit-trailed path to production.
- [Ollama](./ollama.md) - Local LLM runtime; works with a locally-run bolt.diy but can't be reached by a self-hosted (remote) instance.
- [Gemini 3.5 Flash](./gemini-3-5-flash.md) - Google's cheap, fast LLM that builds unusually beautiful, handcrafted-looking frontends; the design half of Cole's provider-mixing workflow, paired with Opus 4.8 for planning and integrations.
- [Kimi K2](./kimi-k2.md) - Moonshot's Kimi model (K2.7), used as a cheap driver and exploration model in Cole's harness via a Kimi subscription to control per-token cost.

## Contrasts with

- [Claude Code](./claude-code.md) - Anthropic's terminal-based agentic coding assistant that is the subject of this complete-guide walkthrough.
- [Codex](./codex.md) - OpenAI's cloud-based software-engineering agent integrated with GitHub, plus a Codex CLI.

## Sources

- [Pi Coding Agent + Archon: Build ANY AI Coding Workflow (No Claude Code Bloat)](../../sources/pi-coding-agent-archon-build-any-ai-coding-workflow-no-claude-code-bloat.md) - "[0:00:00] Pi is a minimalistic open-source coding agent, and minimalistic is really important here because Pi is fighting the bloat that we see with so many other coding agents right now."
- [The Creators of Claude Code and OpenClaw don't Prompt Their Agents Anymore?!](../../sources/the-creators-of-claude-code-and-openclaw-dont-prompt-their-agents-anymore.md) - "[0:19:04] I'm driving everything with Pi. So I'm actually using my Kimi subscription with Kimi K 2.7 to drive all of these workflows."
- [Omnigent: The New Meta-Harness for EVERY Coding Agent - Claude Code, Codex, Pi, More](../../sources/omnigent-the-new-meta-harness-for-every-coding-agent-claude-code-codex-pi-more.md) - "[0:05:23] if I even wanted to use Pi with Ollama for some local development, I can even do that with Omni Agent."
- [Harness Engineering: What Separates Top Agentic Engineers Right Now](../../sources/harness-engineering-what-separates-top-agentic-engineers-right-now.md) - "[0:01:56] Claude Code, Codex, Pi, you name the millions of coding agents out there."
- [The Next Evolution of AI Coding Is Harnesses - Here's How to Build Them](../../sources/the-next-evolution-of-ai-coding-is-harnesses-heres-how-to-build-them.md) - "[0:12:08] we want to add in other coding assistants later, like the Pi Agent SDK and Open Code."
