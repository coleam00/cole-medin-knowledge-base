---
type: concept
title: "Adversarial Agents"
description: "Pitting a generator against an adversarial critic so an agent's output is stress-tested before it's accepted."
tags: [adversarial, critic, validation]
videos: [omnigent-the-new-meta-harness-for-every-coding-agent-claude-code-codex-pi-more, build-render-entire-videos-with-claude-code-full-workflow, parallel-claude-code-git-worktrees-this-setup-will-change-how-you-ship, coding-agent-reliability-explodes-when-they-argue-new-adversarial-dev-technique, google-anthropic-and-openais-guides-to-ai-agents-all-in-18-minutes, 3-most-important-prompt-engineering-techniques-you-need-to-know]
created: 2026-07-21
updated: 2026-07-21
---

# Adversarial Agents

Adversarial agents pit a generator against a separate critic whose only job is to attack its work, so the output is stress-tested before anyone accepts it. As Cole frames the pattern: "I'm talking a totally separate coding agent with its own contact session where its sole job is to rip apart the main agents implementation. I call it adversarial dev." [0:01:04] The critic runs in an isolated context, uninvested in the original solution, which is exactly what lets it find the flaws the author's own context is biased to miss.

The lineage is explicitly generative adversarial networks: "they've been taking a lot of inspiration from generative adversarial networks... one model generate images and then another model is the discriminator." [0:02:56] In coding, that maps to a builder agent and a discriminator agent. A concrete instance is running a review with a different vendor's model, for example `/codex adversarial review`, which "review[s] this current branch as it relates to the changes from main" and, in Cole's run, "ripped apart my code. It says I need attention for this one." [0:12:42] The point of using a *different* agent (Codex reviewing Claude Code) is genuine independence of judgment.

Some harnesses formalize this as a debate. Omnigent "pits two coding agents against each other to argue on a question or a topic and then come to a conclusion together" [0:11:58], letting Claude take one perspective and GPT take the other. This is where the pattern shades into an evaluator loop: "an LLM produce some output and then we have another LLM evaluate it [and] have a loop of selfcorrection if necessary." [0:09:36]

At the lightest weight, the adversary is the same model turned on itself: "have the AI criticize itself" then "write a better tweet based off of its feedback" [0:02:36]. Cole's rule is that this "always give[s] you something better." Video pipelines add domain-specific critics too, such as "an anti-fabrication gate... So it's not just hallucinating everything." [0:08:11]

## Builds on

- [Self-Criticism Prompting](./self-criticism-prompting.md)
- [Role Prompting](./role-prompting.md)
- [Prompt Engineering](./prompt-engineering.md)

## Contrasts with

- [Sycophancy](./sycophancy.md) - the failure mode adversarial critics exist to counter, when an agent flatters instead of finding fault.

## Related

- [Self-Correcting Agents](./self-correction.md)
- [Separate Reviewer](./separate-reviewer.md)
- [Code Review](./code-review.md)
- [End-to-End Validation](./end-to-end-validation.md)
- [Guardrails](./guardrails.md)
- [Agent Evaluation](./agent-evaluation.md)
- [Agentic Workflow Engineering](./agentic-workflow-engineering.md)
- [AI Coding Harness](./ai-coding-harness.md)

## Tools

- [Claude Code](../entities/tools/claude-code.md)
- [Codex](../entities/tools/codex.md)
- [Claude](../entities/tools/claude.md)
- [GPT-4](../entities/tools/gpt-4.md)

## Sources

- [Coding Agent Reliability EXPLODES When They Argue (New Adversarial Dev Technique)](../sources/coding-agent-reliability-explodes-when-they-argue-new-adversarial-dev-technique.md) - "[0:01:04] I'm talking a totally separate coding agent with its own contact session where its sole job is to rip apart the main agents implementation. I call it adversarial dev."
- [Coding Agent Reliability EXPLODES When They Argue (New Adversarial Dev Technique)](../sources/coding-agent-reliability-explodes-when-they-argue-new-adversarial-dev-technique.md) - "[0:02:56] they've been taking a lot of inspiration from generative adversarial networks... one model generate images and then another model is the discriminator."
- [Parallel Claude Code + Git Worktrees: This Setup Will Change How You Ship](../sources/parallel-claude-code-git-worktrees-this-setup-will-change-how-you-ship.md) - "[0:12:42] And it ripped apart my code. It says I need attention for this one."
- [Omnigent: The New Meta-Harness for EVERY Coding Agent - Claude Code, Codex, Pi, More](../sources/omnigent-the-new-meta-harness-for-every-coding-agent-claude-code-codex-pi-more.md) - "[0:11:58] this is an orchestrator that pits two coding agents against each other to argue on a question or a topic and then come to a conclusion together with Debbie orchestrating everything."
- [Google, Anthropic, and OpenAI's Guides to AI Agents ALL in 18 Minutes](../sources/google-anthropic-and-openais-guides-to-ai-agents-all-in-18-minutes.md) - "[0:09:36] We have evaluator loops where we have an LLM produce some output and then we have another LLM evaluate it have a loop of selfcorrection if necessary."
- [3 MOST Important Prompt Engineering Techniques you NEED to know!](../sources/3-most-important-prompt-engineering-techniques-you-need-to-know.md) - "[0:09:32] you always want to ask the AI to critique itself when it doesn't quite give you the answer that you want because it'll always give you something better"
- [Build + Render ENTIRE Videos with Claude Code (Full Workflow)](../sources/build-render-entire-videos-with-claude-code-full-workflow.md) - "[0:08:11] We have an anti-fabrication gate as well. So it's not just hallucinating everything"
