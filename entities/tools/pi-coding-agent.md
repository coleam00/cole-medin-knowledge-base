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

Pi is Cole's preferred driver for orchestrated workflows. He runs it against non-Anthropic models to keep his stack provider-flexible: "I'm driving everything with Pi. So I'm actually using my Kimi subscription with Kimi K 2.7 to drive all of these workflows" ([0:19:04]), a direct expression of deliberate [Model Selection](../../concepts/model-selection.md). Because Pi exposes an API layer, it slots into larger systems: "It'll connect to the backend with the API that I have running with PI" ([0:22:05]). In [Archon](./archon.md) it became "the third coding agent supported," giving Cole a lean alternative to the bigger agents when doing [Agentic Workflow Engineering](../../concepts/agentic-workflow-engineering.md). Pi is also a recurring member of the "you name the millions of coding agents out there" list ([0:01:56]) alongside [Claude Code](./claude-code.md) and [Codex](./codex.md), and it can be pointed at a local model through meta-harnesses: "if I even wanted to use PI with Olama for some local development, I can even do that" ([0:05:23]) via [Ollama](./ollama.md). Cole has flagged the Pi Agent SDK as a coding assistant he wants to wire into his own harnesses next.

## Related

- [AI Coding Harness](../../concepts/ai-coding-harness.md) - Pi is a minimal, self-modifying harness core.
- [Model Selection](../../concepts/model-selection.md) - Pi is driven by Kimi K2.7 to stay off Anthropic.
- [Agentic Workflow Engineering](../../concepts/agentic-workflow-engineering.md) - Pi drives multi-step orchestrated workflows.
- [Parallel Agentic Coding](../../concepts/parallel-agentic-coding.md) and [Context Isolation](../../concepts/context-isolation.md) - how Pi sessions are run without stepping on each other.
- [Human in the Loop](../../concepts/human-in-the-loop.md) - the oversight posture around Pi-driven builds.
- Sibling agents: [Claude Code](./claude-code.md), [Codex](./codex.md), [Archon](./archon.md), [Ollama](./ollama.md).

## Sources

- [Pi Coding Agent + Archon: Build ANY AI Coding Workflow (No Claude Code Bloat)](../../sources/pi-coding-agent-archon-build-any-ai-coding-workflow-no-claude-code-bloat.md) - "[0:00:00] Pi is a minimalistic open-source coding agent, and minimalistic is really important here because Pi is fighting the bloat that we see with so many other coding agents right now."
- [The Creators of Claude Code and OpenClaw don't Prompt Their Agents Anymore?!](../../sources/the-creators-of-claude-code-and-openclaw-dont-prompt-their-agents-anymore.md) - "[0:19:04] I'm driving everything with Pi. So I'm actually using my Kimi subscription with Kimi K 2.7 to drive all of these workflows."
- [Omnigent: The New Meta-Harness for EVERY Coding Agent - Claude Code, Codex, Pi, More](../../sources/omnigent-the-new-meta-harness-for-every-coding-agent-claude-code-codex-pi-more.md) - "[0:05:23] if I even wanted to use PI with Olama for some local development, I can even do that with Omni Agent."
- [Harness Engineering: What Separates Top Agentic Engineers Right Now](../../sources/harness-engineering-what-separates-top-agentic-engineers-right-now.md) - "[0:01:56] Claude Code, Codeex, Pi, you name the millions of coding agents out there."
- [The Next Evolution of AI Coding Is Harnesses - Here's How to Build Them](../../sources/the-next-evolution-of-ai-coding-is-harnesses-heres-how-to-build-them.md) - "[0:12:08] we want to add in other coding assistants later, like the Pi Agent SDK and Open Code."
