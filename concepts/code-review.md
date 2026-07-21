---
type: concept
title: "Code Review"
description: "Using AI to review diffs for bugs and quality as a gate before merging, ideally with a reviewer separate from the author."
tags: [review, quality, bugs]
videos: [harness-engineering-what-separates-top-agentic-engineers-right-now, full-guide-to-becoming-a-principled-agentic-engineer-build-anything-with-ai, parallel-claude-code-git-worktrees-this-setup-will-change-how-you-ship, the-subagent-era-is-officially-here-learn-this-now, this-one-command-makes-coding-agents-find-all-their-mistakes-use-it-now, the-way-we-use-ai-will-completely-change-in-2026-hot-takes, github-is-the-future-of-ai-coding-heres-why, the-true-power-of-ai-coding-build-your-own-workflows-full-guide]
created: 2026-07-21
updated: 2026-07-21
---

# Code Review

Code review is the gate where an AI agent (and then a human) reads the actual code changes for logic errors, security holes, and needless complexity before anything merges. It is the second half of the build loop: the agent implements, and then a fresh pass tears the implementation apart. As Cole puts it, "the other one is doing the code review part of our validation. So this sub agent is going to find things like logic errors that we have in our code" ([This One Command Makes Coding Agents Find All Their Mistakes](../sources/this-one-command-makes-coding-agents-find-all-their-mistakes-use-it-now.md), 0:05:07). He nicknames it "the bunk hunting code analysis."

The discipline is non-negotiable in Cole's workflow: never merge without a review, and never let a review substitute for your own eyes. "The last step here is our own review. You definitely want to perform a code review on everything that was outputed by your coding assistant. Otherwise, you're still just reverting back to Vive coding" ([The True Power of AI Coding](../sources/the-true-power-of-ai-coding-build-your-own-workflows-full-guide.md), 0:23:53). The point is comprehension, not just approval: "we want to be a part of this process as well. Performing a code review because we don't want to vibe code. We want to actually look at and understand the code that is being produced" (0:19:05).

Code review parallelizes cleanly. Different reviewer agents can specialize, each in its own context: "We could have many code review agents running in parallel. This one focuses on security. This one correctness of the implementation. And this one making sure it's as simple as it can be. And then if everything passes, you create the pull request" ([Harness Engineering](../sources/harness-engineering-what-separates-top-agentic-engineers-right-now.md), 0:13:58). Reviews also apply to the tooling itself, not just product code: "you can even create pull requests to update commands just like you create pull requests to update your codebase. So you can do code reviews" ([Principled Agentic Engineer](../sources/full-guide-to-becoming-a-principled-agentic-engineer-build-anything-with-ai.md), 0:59:38).

Cole sees the review medium shifting from line-by-line diffs toward artifacts: "my next prediction is artifact reviews instead of diff reviews... instead of us having to review things line by line, we can look at browser recordings they send us... full working demos of a backend API" ([The Way We Use AI Will Change in 2026](../sources/the-way-we-use-ai-will-completely-change-in-2026-hot-takes.md), 0:13:15). That prediction leans on strong [end-to-end validation](./end-to-end-validation.md) to prove the artifact actually works.

## Part of

- [Validation](./validation.md) - code review is one layer of the broader validation strategy, alongside tests and end-to-end checks.

## Builds on

- [Separate Reviewer](./separate-reviewer.md) - the strongest reviews happen outside the author's context, so bias doesn't leak in.

## Related

- [End-to-End Validation](./end-to-end-validation.md) - proving the feature works through its real interface, the counterpart to reading the diff.
- [Adversarial Agents](./adversarial-agents.md) - a reviewer whose sole job is to attack the implementation.
- [Subagents Pattern](./subagents-pattern.md) - running reviews in isolated sub-agent contexts.
- [Agent Teams](./agent-teams.md) - parallel specialist reviewers coordinated together.
- [Parallel Agentic Coding](./parallel-agentic-coding.md) - running many review agents at once.
- [Human in the Loop](./human-in-the-loop.md) - your own review after the agent's, before merge.
- [Agentic Workflow Engineering](./agentic-workflow-engineering.md) - where the review step is codified into a repeatable command.
- [System Evolution](./system-evolution.md) - reviewing PRs against the harness and its commands, not just the app.

## Tools

- [Claude Code](../entities/tools/claude-code.md) - runs `@claude-review` on PRs and hosts parallel review sub-agents.
- [Codex](../entities/tools/codex.md) - often preferred as the reviewing agent when Claude implements.
- [CodeRabbit](../entities/tools/code-rabbit.md) - a dedicated review agent whose recommendations Cole feeds back to Claude Code.
- [GitHub](../entities/tools/github.md) - where PR reviews live; agents review each other's pull requests.

## Sources

- [This One Command Makes Coding Agents Find All Their Mistakes](../sources/this-one-command-makes-coding-agents-find-all-their-mistakes-use-it-now.md) - "[0:05:07] the other one is doing the code review part of our validation. So... this sub aent is going to find things like logic errors that we have in our code."
- [Harness Engineering: What Separates Top Agentic Engineers Right Now](../sources/harness-engineering-what-separates-top-agentic-engineers-right-now.md) - "[0:13:58] We could have many code review agents running in parallel. This one focuses on security. This one correctness of the implementation. And this one making sure it's as simple as it can be. And then if everything passes, you create the pull request."
- [The True Power of AI Coding - Build Your OWN Workflows](../sources/the-true-power-of-ai-coding-build-your-own-workflows-full-guide.md) - "[0:23:53] the last step here is our own review. You definitely want to perform a code review on everything that was outputed by your coding assistant. Otherwise, you're still just reverting back to Vive coding."
- [FULL Guide to Becoming a Principled Agentic Engineer](../sources/full-guide-to-becoming-a-principled-agentic-engineer-build-anything-with-ai.md) - "[0:55:50] we'll wait for it to write the code, do all of its own validation, and then we'll also step in and we'll do a code review"
- [Parallel Claude Code + Git Worktrees](../sources/parallel-claude-code-git-worktrees-this-setup-will-change-how-you-ship.md) - "[0:11:43] Always important to do the review with the coding agent and then yourself after before you're merging any pull requests into production."
- [The Subagent Era Is Officially Here](../sources/the-subagent-era-is-officially-here-learn-this-now.md) - "[0:13:28] Running code reviews as well is another really good use of sub agents. There's so many times where I'm just relying on sub agents very very deeply."
- [The Way We Use AI Will Completely Change in 2026](../sources/the-way-we-use-ai-will-completely-change-in-2026-hot-takes.md) - "[0:13:15] my next prediction is artifact reviews instead of diff reviews."
- [GitHub is the Future of AI Coding](../sources/github-is-the-future-of-ai-coding-heres-why.md) - "[0:23:07] you never want to merge a pull request without a review as well... I'm going to go ahead and have the coding assistants review each other."
