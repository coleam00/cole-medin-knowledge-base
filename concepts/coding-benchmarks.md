---
type: concept
title: "Real-World Coding Benchmarks"
description: "Evaluating coding models on real engineering tasks, and the gap between exploding benchmark scores and flat developer productivity."
tags: [ai-coding, benchmarks, evals, model-selection, productivity]
videos: [is-gemini-3-really-the-best-ai-ever, breaking-news-ottodev-is-now-the-official-open-source-boltnew]
created: 2026-07-21
updated: 2026-07-21
---

# Real-World Coding Benchmarks

A real-world coding benchmark evaluates a model on actual engineering work rather than a synthetic puzzle: "instead of relying on these synthetic benchmarks, we are now working on real engineering tasks" [0:09:06]. The push comes from a credibility gap. Leaderboard numbers keep climbing while the day-to-day experience of shipping code does not move nearly as fast, so Cole argues the measurement itself has to change: "The point is not the individual company or tool, just that we have to move to real tasks for evaluating our LLMs for things like AI coding."

## How it works

The recipe for a real-task benchmark is deliberately simple. "There's just three pieces of information that we need for any real engineering task. We need the starting snapshot of the repository, their prompt, and then also the end state." Give the model a real repo at a known commit, hand it the same prompt a developer got, and compare what it produces against the human's actual resulting diff. That construction is closer to [agent evaluation](./agent-evaluation.md) on end-to-end tasks than to a multiple-choice exam, and it uses [git](./git-as-long-term-memory.md) snapshots as the ground truth.

## Why it matters

Synthetic benchmarks saturate and stop discriminating. Cole and guests note that providers have started reaching for whatever real workload is handy just to find signal: "can it run Bolt" became a de-facto test "because there's not a lot of other things to test it out against." The blunter critique is that the classic evals "are not actually representative of like real world applications," so a model can top a benchmark and still stumble on the messy, stateful work of a live codebase. For anyone doing [model selection](./model-selection.md), that means a headline score is a starting hypothesis, not a verdict, and the only trustworthy benchmark is your own repository under your own prompts.

## Related

- [Agent Evaluation](./agent-evaluation.md) - the broader discipline of scoring agents on end-to-end tasks.
- [Model Selection](./model-selection.md) - where benchmark skepticism turns into a real decision.
- [Git as Long-Term Memory](./git-as-long-term-memory.md) - repo snapshots and diffs are the ground truth for a real-task benchmark.
- [AI Coding Harness](./ai-coding-harness.md), [Local & Self-Hosted AI Coding](./local-ai.md) - the surrounding setup whose value the benchmark is trying to measure.

## Sources

- [Is Gemini 3 Really the Best AI Ever?](../sources/is-gemini-3-really-the-best-ai-ever.md) - "[0:09:06] instead of relying on these synthetic benchmarks, we are now working on real engineering tasks."
- [Is Gemini 3 Really the Best AI Ever?](../sources/is-gemini-3-really-the-best-ai-ever.md) - "[0:10:00] There's just three pieces of information that we need for any real engineering task. We need the starting snapshot of the repository, their prompt, and then also the end state"
- [BREAKING NEWS: oTToDev is Now the OFFICIAL Open Source Bolt.new](../sources/breaking-news-ottodev-is-now-the-official-open-source-boltnew.md) - "[0:02:28] The evals and benchmarks that they're testing these things against are... not actually representative of like real world applications"
