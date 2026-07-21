---
type: entity
subtype: person
title: "Geoffrey Huntley"
description: "Creator of the Ralph Wiggum long-running agent loop, who frames it as a planning-heavy philosophy rather than a shiny framework or the Anthropic plugin."
resource: "https://ghuntley.com"
tags: [ralph-loop, harness-engineering, autonomous-agents]
videos: [harness-engineering-what-separates-top-agentic-engineers-right-now, i-was-wrong-about-ralph-wiggum]
created: 2026-07-21
updated: 2026-07-21
---

# Geoffrey Huntley

Geoffrey Huntley is the creator of Ralph Wiggum, the long-running agent loop, and the person Cole credits with first showing that agent sessions could be chained into an unattended system at all: "Jeffrey Huntley, the creator of Ralph, he really is one of the pioneers here. This is one of the first examples showing in a very basic sense how we can automate stringing together many instances of cloud code, codecs" ([0:14:42], transcript spelling). [The Ralph Loop](../../concepts/the-ralph-loop.md) in its plainest form is a bash script: take a large PRD, split it into tasks, run a coding-agent session per iteration, and keep looping until a done indicator says every spec item is complete and validated.

Huntley matters here for a second reason, which is that he corrected Cole in public and changed his mind. Cole had dismissed Ralph based on the wrong artifact: "Jeffrey Huntley, the creator of Ralph Wiggum, he commented and he shared some resources, some videos on his channel" ([0:00:30]). The point Huntley made is that the Anthropic plugin Cole had fixated on is not the real Ralph Wiggum. The real thing is a philosophy with extensive planning built into it, not a shiny framework you install. That distinction is the whole argument: a loop is only as good as the spec and the exit condition you hand it.

Cole's revised position, after rebuilding the template himself, is that Ralph is not a way to autonomously ship production code but a way to validate an idea. With a structured PRD produced up front, a persistent activity log as cross-loop memory, a sandboxed settings file so an unattended agent cannot go haywire, and browser-driven self-validation, the loop builds a complete proof of concept overnight while you keep your hands off the keyboard. In the larger picture Huntley's loop is one example harness among many, which is where it connects to [AI Coding Harness](../../concepts/ai-coding-harness.md) and to purpose-built orchestrators like [Archon](../tools/archon.md).

## Implemented by

- [The Ralph Loop](../../concepts/the-ralph-loop.md) - Re-running an agent against the same prompt/state in a tight loop, letting each pass fix errors and compound reliability.
- [Claude Code](../tools/claude-code.md) - Anthropic's terminal-based agentic coding assistant, the session the loop re-invokes each iteration.
- [Archon](../tools/archon.md) - Cole's free, open-source AI command center and harness builder for AI coding.

## Contrasts with

- [Vibe Coding](../../concepts/vibe-coding.md) - Building software by conversationally prompting an AI without closely reading the code. Ralph is the opposite bet: the planning is front-loaded so the agent can run unattended.

## Related

- [AI Coding Harness](../../concepts/ai-coding-harness.md) - The surrounding scaffolding (prompts, tools, rules, validation) that turns a raw model into a reliable coding system.
- [Agentic Workflow Engineering](../../concepts/agentic-workflow-engineering.md) - Designing repeatable AI workflows as engineered systems with defined steps, orchestration, and background execution.
- [PRD-First Development](../../concepts/prd-first-development.md) - Starting every build from a written product requirements document that becomes the contract the agent implements against.
- [Planning with AI](../../concepts/planning-with-ai.md) - Using the AI to produce a detailed plan before implementation so execution follows a reviewed blueprint.
- [End-to-End Validation](../../concepts/end-to-end-validation.md) - Validating the whole system through its real interface so the agent proves the feature actually works.
- [Rapid Prototyping](../../concepts/rapid-prototyping.md) - Building a fast proof of concept first, then hardening only what proves out.
- [Loop Engineering](../../concepts/loop-engineering.md) - Designing self-prompting loops so coding agents pick up and run work autonomously.
- [Peter Steinberger](./peter-steinberger.md) - Creator of OpenClaw and a proponent of writing loops instead of prompting agents.
- [Cole Medin](./cole-medin.md) - AI engineer and educator whose YouTube channel and Dynamous community teach agentic coding.

## Sources

- [Harness Engineering: What Separates Top Agentic Engineers Right Now](../../sources/harness-engineering-what-separates-top-agentic-engineers-right-now.md) - "[0:14:42] Jeffrey Huntley, the creator of Ralph, he really is one of the pioneers here. This is one of the first examples showing in a very basic sense how we can automate stringing together many instances of cloud code, codecs."
- [I Was Wrong About Ralph Wiggum](../../sources/i-was-wrong-about-ralph-wiggum.md) - "[0:00:30] Jeffrey Huntley, the creator of Ralph Wiggum, he commented and he shared some resources, some videos on his channel."
