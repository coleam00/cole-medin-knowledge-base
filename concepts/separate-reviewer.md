---
type: concept
title: "Separate Reviewer"
description: "Splitting authoring and grading across different agents so the reviewer isn't biased by having written the code."
tags: [review, author-grader, bias]
videos: [the-best-ai-coding-setup-isnt-the-most-autonomous-one-heres-why, omnigent-the-new-meta-harness-for-every-coding-agent-claude-code-codex-pi-more, parallel-claude-code-git-worktrees-this-setup-will-change-how-you-ship, im-building-an-ai-dark-factory-that-ships-its-own-code-public-experiment, coding-agent-reliability-explodes-when-they-argue-new-adversarial-dev-technique, the-true-power-of-ai-coding-build-your-own-workflows-full-guide, 10x-your-ai-agents-with-this-one-agent-architecture, ai-agents-the-future-of-ai-or-a-passing-fad]
created: 2026-07-21
updated: 2026-07-21
---

# Separate Reviewer

A separate reviewer is a distinct agent, in its own context window, whose only job is to grade code it did not write. The whole point is to strip out the bias an author accumulates while implementing: "It's important to not do your code review in the same context window where you do the implementation because there's a lot of bias that's built up there" ([The Best AI Coding Setup Isn't the Most Autonomous One](../sources/the-best-ai-coding-setup-isnt-the-most-autonomous-one-heres-why.md), 0:18:21). An LLM that just spent a long conversation defending its own choices is the worst judge of them.

Cole treats this author-grader split as foundational: "it is very important, at least at a very fundamental level, to do your code review in a separate coding agent session from your implementation. Otherwise, the LLM builds up way too much bias" ([Omnigent](../sources/omnigent-the-new-meta-harness-for-every-coding-agent-claude-code-codex-pi-more.md), 0:06:56). The separation is often cross-model, because different tools have different strengths: "a lot of people feel like Codex is best at reviewing and Claude is best at implementing" (0:07:13). One agent builds, another tears it apart: "a totally separate coding agent with its own contact session where its sole job is to rip apart the main agents implementation" ([Coding Agent Reliability Explodes When They Argue](../sources/coding-agent-reliability-explodes-when-they-argue-new-adversarial-dev-technique.md), 0:01:04).

The most rigorous form is the hold-out pattern, where the reviewer is deliberately starved of the development narrative: "it is so important to have a key separation here. one agent to do the implementation, one to do the validation" ([AI Dark Factory](../sources/im-building-an-ai-dark-factory-that-ships-its-own-code-public-experiment.md), 0:21:45). "what the hold out pattern does is we give our validation agent the user journey that we either fixed or created and then the exact diffs for the code... but we give it no context into the development process" (0:22:01). By withholding the implementation's reasoning, the reviewer judges the result on its own merits. This also works around a core LLM weakness, that models "can't reason about their own output" ([AI Agents: Future or Fad](../sources/ai-agents-the-future-of-ai-or-a-passing-fad.md), 0:06:58), by making a fresh agent do the reasoning instead.

## Builds on

- [Context Isolation](./context-isolation.md) - the reviewer's fresh context is exactly what removes author bias.
- [Subagents Pattern](./subagents-pattern.md) - the separate reviewer is typically its own sub-agent session.

## Part of

- [Code Review](./code-review.md) - the separate reviewer is how a rigorous code review is staffed.

## Contrasts with

- [Sycophancy](./sycophancy.md) - an author reviewing itself tends to agree with itself; a separate grader resists that.

## Related

- [Adversarial Agents](./adversarial-agents.md) - a reviewer whose explicit mandate is to attack the implementation.
- [Validation](./validation.md) - separating author and grader is a validation-reliability technique.
- [End-to-End Validation](./end-to-end-validation.md) - the hold-out reviewer is handed the user journey to verify.
- [Model Selection](./model-selection.md) - pairing the best reviewer model with the best implementer model.
- [Dark Factory](./dark-factory.md) - the self-shipping pipeline that leans on the author-validator split.
- [Self-Reflective RAG](./self-reflective-rag.md) - the same self-critique idea applied to retrieval output.
- [What Is an AI Agent?](./what-is-an-ai-agent.md) - the self-reflection primitive that separate reviewers exploit.

## Tools

- [Claude Code](../entities/tools/claude-code.md) - often the implementer, with a separate session for review.
- [Codex](../entities/tools/codex.md) - frequently preferred as the reviewing agent against a Claude implementation.
- [CodeRabbit](../entities/tools/code-rabbit.md) - a dedicated external reviewer whose findings feed back to the implementer.

## Sources

- [The Best AI Coding Setup Isn't the Most Autonomous One](../sources/the-best-ai-coding-setup-isnt-the-most-autonomous-one-heres-why.md) - "[0:18:21] It's important to not do your code review in the same context window where you do the implementation because there's a lot of bias that's built up there."
- [Omnigent: The New Meta-Harness for EVERY Coding Agent](../sources/omnigent-the-new-meta-harness-for-every-coding-agent-claude-code-codex-pi-more.md) - "[0:06:56] it is very important, at least at a very fundamental level, to do your code review in a separate coding agent session from your implementation. Otherwise, the LLM builds up way too much bias."
- [I'm Building an AI Dark Factory](../sources/im-building-an-ai-dark-factory-that-ships-its-own-code-public-experiment.md) - "[0:22:01] what the hold out pattern does is we give our validation agent the user journey that we either fixed or created and then the exact diffs for the code... but we give it no context into the development process."
- [Coding Agent Reliability EXPLODES When They Argue](../sources/coding-agent-reliability-explodes-when-they-argue-new-adversarial-dev-technique.md) - "[0:01:04] a totally separate coding agent with its own contact session where its sole job is to rip apart the main agents implementation."
- [Parallel Claude Code + Git Worktrees](../sources/parallel-claude-code-git-worktrees-this-setup-will-change-how-you-ship.md) - "[0:10:28] there is a specialized command that I have created for this called review PR. So it automatically data mines the poll request associated with the current branch and it does a comprehensive review."
- [The True Power of AI Coding - Build Your OWN Workflows](../sources/the-true-power-of-ai-coding-build-your-own-workflows-full-guide.md) - "[0:19:32] There's another agent that I love using to review my work. You can think of it as another validation subagent and that is CodeRabbit."
- [10x Your AI Agents with this ONE Agent Architecture](../sources/10x-your-ai-agents-with-this-one-agent-architecture.md) - "[0:18:30] this is also a good opportunity to have an agent that could validate the different outputs from the other agents you can use a synthesizer as a validator as well"
- [AI Agents: The Future of AI or a Passing Fad?](../sources/ai-agents-the-future-of-ai-or-a-passing-fad.md) - "[0:06:58] this is really powerful because you're giving a large language model the ability to self-reflect because one huge problem with llms is they can't reason about their own output"
