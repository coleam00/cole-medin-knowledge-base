---
type: entity
subtype: tool
title: "Claude Agent SDK"
description: "The engine that powers Claude Code, exposed as a library so you can invoke Claude Code programmatically and build custom agents on top of the same harness."
resource: "https://docs.anthropic.com/en/docs/claude-code/sdk"
tags: [coding-agent, sdk, anthropic, harness, headless]
videos: [pydantic-ai-20-the-new-best-way-to-build-ai-agents-is-composing-capabilities, i-love-the-karpathy-llm-wiki-but-it-doesnt-scale-heres-what-does, googles-agents-cli-the-cli-skills-combination-to-ship-ai-agents-easily, the-next-evolution-of-ai-coding-is-harnesses-heres-how-to-build-them, i-built-self-evolving-claude-code-memory-w-karpathys-llm-knowledge-bases, full-guide-build-your-own-ai-second-brain-with-claude-code, coding-agent-reliability-explodes-when-they-argue-new-adversarial-dev-technique, everything-you-thought-about-building-ai-agents-is-wrong, i-built-a-safer-openclaw-alternative-using-claude-code, turn-claude-code-into-your-full-engineering-team-with-subagents, i-forced-claude-to-code-for-24-hours-nonstop-heres-what-happened, claude-code-web-just-dropped-but-i-already-built-something-better-with-codex, claude-codes-real-purpose-its-bigger-than-you-think, claude-sonnet-45-the-new-coding-king-sonnet-45-vs-gpt-5-codex, archon-beta-launch-livestream-what-you-missed]
created: 2026-07-21
updated: 2026-07-21
---

# Claude Agent SDK

The Claude Agent SDK is Anthropic's library for invoking Claude Code programmatically, the same harness that powers the Claude Code CLI exposed so you can build your own agents on it. Cole treats it as more than a coding tool: "A couple weeks ago, they renamed the Cloud Code SDK to the Cloud Agent SDK because it really is this engine that can power any of our AI agents we want to build" [0:02:19]. Instead of prompting the CLI by hand, you drive it from code, "we're using the Agent SDK because we're invoking Claude Code programmatically. I'm not prompting it myself" [0:18:08], defining everything in code rather than a `.claude` folder, "When we create our agent, we're using the cloud agents SDK. So we're defining everything in code. We're not using our cloud folder like you would with cloud code" [0:14:22].

Its power is that you inherit a full [AI coding harness](../../concepts/ai-coding-harness.md) for free, "these really powerful harnesses that give us a ton of capability right out of the gate, the same capabilities used in these AI coding assistants" [0:08:01]. The tradeoff is speed and cost: "It's a lot less token efficient to use these SDKs, and you're going to get slower responses" [0:08:36], which is why for scalable production agents Cole still reaches for a framework, while the SDK shines for personal and coding-heavy agents. He uses it as the backbone of his own systems, "I'm using the Claude agent SDK for the whole heartbeat system that I built for my own [second brain](../../concepts/second-brain.md)" [0:05:48], for self-evolving memory, and as the engine behind Archon, "we'll use the cloud code SDK that they offer so that we can build our own application that is invoking cloud code and we can manage the different instances" [0:09:00]. In TypeScript that is as simple as "import query from cloud code" [0:33:00].

A recurring, important caveat Cole repeats is licensing: local use on your Anthropic subscription is fine, "We are allowed to use our Anthropic subscription as long as it's an application running locally using the Claude Agent SDK" [0:12:22], but "if you're building a business on top of the Asian SDK, as in other people would be using your subscription, then it's against the terms of service and you should use your API key" [0:14:25]. He frequently pairs and contrasts it with OpenAI's Codex SDK as the near-identical TypeScript alternative.

## Related

- [AI Coding Harness](../../concepts/ai-coding-harness.md) - the SDK hands you Claude Code's full harness out of the gate.
- [SDK vs. Framework Decision](../../concepts/sdk-vs-framework-decision.md) - when to pick this SDK over a from-scratch framework.
- [Provider Independence](../../concepts/provider-independence.md) - the SDK ties you to Anthropic, a key tradeoff versus a framework.
- [Second Brain](../../concepts/second-brain.md) - Cole's heartbeat and second-brain systems run on the SDK.
- [Model Selection](../../concepts/model-selection.md) - the Claude model the SDK bundles by default.
- [Validation](../../concepts/validation.md) and [PRD-First Development](../../concepts/prd-first-development.md) - practices layered on agents built with the SDK.
- [Claude Code](./claude-code.md) - the CLI whose engine this SDK exposes.
- [Codex](./codex.md) - OpenAI's near-identical coding-agent SDK Cole contrasts it with.
- [Archon](./archon.md) - built on the Claude Agent SDK to manage many Claude Code instances.
- [Pydantic AI](./pydantic-ai.md) and [LangGraph](./langgraph.md) - the frameworks he still prefers for fast, scalable production agents.

## Sources

- [Claude Code's Real Purpose (It's Bigger Than You Think)](../../sources/claude-codes-real-purpose-its-bigger-than-you-think.md) - "[0:02:19] A couple weeks ago, they renamed the Cloud Code SDK to the Cloud Agent SDK because it really is this engine that can power any of our AI agents we want to build."
- [Everything You Thought About Building AI Agents is Wrong](../../sources/everything-you-thought-about-building-ai-agents-is-wrong.md) - "[0:05:48] I'm using the Claude agent SDK for the whole heartbeat system that I built for my own second brain"
- [Google's Agents CLI: The CLI + Skills Combination to Ship AI Agents EASILY](../../sources/googles-agents-cli-the-cli-skills-combination-to-ship-ai-agents-easily.md) - "[0:08:36] It's a lot less token efficient to use these SDKs, and you're going to get slower responses."
- [The Next Evolution of AI Coding Is Harnesses - Here's How to Build Them](../../sources/the-next-evolution-of-ai-coding-is-harnesses-heres-how-to-build-them.md) - "[0:12:22] We are allowed to use our Anthropic subscription as long as it's an application running locally using the Claude Agent SDK. And that is the case for Archon."
- [Coding Agent Reliability EXPLODES When They Argue (New Adversarial Dev Technique)](../../sources/coding-agent-reliability-explodes-when-they-argue-new-adversarial-dev-technique.md) - "[0:14:25] if you're building a business on top of the Asian SDK, as in other people would be using your script subscription, then it's against the terms of service and you should use your API key."
- [I Forced Claude to Code for 24 Hours NONSTOP, Here's What Happened](../../sources/i-forced-claude-to-code-for-24-hours-nonstop-heres-what-happened.md) - "[0:07:39] We are using the Claude agent SDK to create our Claude code client and interact with it directly in Python code."
- [Turn Claude Code into Your Full Engineering Team with Subagents](../../sources/turn-claude-code-into-your-full-engineering-team-with-subagents.md) - "[0:14:22] When we create our agent, we're using the cloud agents SDK. So we're defining everything in code. We're not using our cloud folder like you would with cloud code."
