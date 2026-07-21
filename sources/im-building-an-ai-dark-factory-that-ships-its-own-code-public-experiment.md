---
type: source
title: "I'm Building an AI Dark Factory That Ships Its Own Code (Public Experiment)"
description: "A 'dark factory' hands a codebase entirely over to AI to triage, plan, implement, validate and merge to production with no human review, and its reliability depends almost entirely on the governance and validation system you build around it."
youtube_id: 6woc6ii-zoE
url: https://www.youtube.com/watch?v=6woc6ii-zoE
slug: im-building-an-ai-dark-factory-that-ships-its-own-code-public-experiment
published: 2026-04-15
duration: "0:25:13"
recency_rank: 19
raw: "../raw/im-building-an-ai-dark-factory-that-ships-its-own-code-public-experiment.md"
tags: [dark-factory, autonomous, workflow, validation]
created: 2026-07-21
updated: 2026-07-21
---

# I'm Building an AI Dark Factory That Ships Its Own Code (Public Experiment)

Cole announces a public experiment to build a 'dark factory': a system where a coding agent owns the full lifecycle of a codebase (planning, implementing, opening PRs, and merging to production) with no human in the loop. Borrowing Dan Shapiro's self-driving-car analogy, he walks through the levels of AI-assisted coding, from level-0 'spicy autocomplete' up through the level-3 human-in-the-loop stage he recommends for production today, level-4 unattended harnesses (Ralph, GSD) where you still review the final PR, and finally level-5 the dark factory where code ships without any review. He frames this as not-yet-practical for production but a glimpse of where AI coding is headed, and notes prior art from StrongDM and Spotify while positioning his own as the first fully open, public version you can submit issues to.

The architecture has three parts. A governance layer of three files loaded into every workflow (mission.md defining what is in and out of scope, factory-rules.md defining triage/implementation/merge operations and quality gates, and CLAUDE.md holding global tech-stack rules) keeps the agent aligned to Cole's mission. Archon is the harness/workflow engine that packages his process into deterministic, repeatable workflows; Claude Code is the coding agent, but routed via environment variables to MiniMax M2.7 rather than Anthropic models for pure cost and throughput reasons. The loop starts from a GitHub issue, runs a scheduled triage workflow (a bash fetch, an agent classify step against the governance files, and a deterministic apply of labels/decisions), then kicks off parallel implementation workflows using Archon's git-worktree isolation.

Validation is deliberately a separate Archon workflow to enforce StrongDM's 'hold-out pattern': one agent implements, a different agent validates, receiving only the user journey and the code diffs but none of the development context, specifically to avoid sycophancy and self-bias where agents declare success or lazily rewrite tests to match their own code. Validation leans on end-to-end browser automation to test real user journeys rather than trusting stored unit tests, after which the change can merge straight to main. The whole thing runs on a cron loop (triage, implement, validate, repeat), with a planned weekly regression pass that documents every user journey and files its own GitHub issues for anything imperfect. The underlying app being built is an agentic RAG 'AI tutor' over Cole's YouTube content.

## Concepts covered

- [Dark Factory](../concepts/dark-factory.md)
- [The Evolution of AI Coding](../concepts/the-evolution-of-ai-coding.md)
- [Human in the Loop](../concepts/human-in-the-loop.md)
- [AI Coding Harness](../concepts/ai-coding-harness.md)
- [Agentic Workflow Engineering](../concepts/agentic-workflow-engineering.md)
- [Deterministic Workflows](../concepts/deterministic-workflows.md)
- [Global Rules](../concepts/global-rules.md)
- [The Issue Is the Spec](../concepts/issue-is-the-spec.md)
- [Separate Reviewer](../concepts/separate-reviewer.md)
- [Sycophancy](../concepts/sycophancy.md)
- [End-to-End Validation](../concepts/end-to-end-validation.md)
- [Parallel Agentic Coding](../concepts/parallel-agentic-coding.md)
- [Provider Independence](../concepts/provider-independence.md)
- [Model Selection](../concepts/model-selection.md)
- [System Evolution](../concepts/system-evolution.md)
- [Agentic RAG](../concepts/agentic-rag.md)

## Entities

- [Archon](../entities/tools/archon.md)
- [Claude Code](../entities/tools/claude-code.md)
- [GitHub](../entities/tools/github.md)
- [Git Worktrees](../entities/tools/git-worktree.md)
- [StrongDM](../entities/organizations/strongdm.md)
- [Dan Shapiro](../entities/people/dan-shapiro.md)
- [Anthropic](../entities/organizations/anthropic.md)
- [Cole Medin](../entities/people/cole-medin.md)

## Key moments

- **[0:00:00]** Announces the public dark-factory experiment: hand a codebase entirely to AI, no human in the loop
- **[0:02:03]** Origin of 'dark factory' term: lights-out manufacturing, later applied to code by Dan Shapiro
- **[0:03:11]** Levels 0-5 of AI coding mapped to self-driving-car autonomy levels
- **[0:04:46]** Level 3 (human-in-the-loop reviewing every plan and diff) recommended for reliable production code today
- **[0:05:34]** Level 4 harnesses (Ralph, GSD) run unattended but you still review the final PR
- **[0:06:33]** Level 5 dark factory: code ships to production with no review at all
- **[0:07:37]** StrongDM and Spotify prior art; Cole's is the first open public version
- **[0:09:53]** Governance layer: mission.md, factory-rules.md, CLAUDE.md loaded into every workflow
- **[0:15:28]** Archon as the harness/workflow engine driving the whole factory
- **[0:16:05]** Claude Code routed to MiniMax M2.7 for cost and throughput
- **[0:17:16]** The factory loop: GitHub issue -> triage -> implement -> validate
- **[0:18:45]** Triage workflow: bash fetch, agent classify, deterministic apply of labels
- **[0:21:32]** Validation as a separate workflow implementing StrongDM's hold-out pattern
- **[0:21:45]** Sycophancy: why implementer and validator must be separate agents
- **[0:23:24]** After validation, merge straight to main; runs on an hourly cron loop
- **[0:23:54]** Planned weekly regression pass that files its own GitHub issues

## Transcript

[Raw transcript](../raw/im-building-an-ai-dark-factory-that-ships-its-own-code-public-experiment.md)
