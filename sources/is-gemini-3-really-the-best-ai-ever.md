---
type: source
title: "Is Gemini 3 Really the Best AI Ever?"
description: "Gemini 3 is a genuinely powerful model, but LLM benchmarks are unreliable marketing-like signals, and the real gains developers see come as much from the tools and systems built on top of models as from the models themselves, so the industry needs real-task evals like Cline's Kleinbench."
youtube_id: YyoqKHpH1EU
url: https://www.youtube.com/watch?v=YyoqKHpH1EU
slug: is-gemini-3-really-the-best-ai-ever
published: 2025-11-24
duration: "0:12:20"
recency_rank: 52
raw: "../raw/is-gemini-3-really-the-best-ai-ever.md"
tags: [benchmarks, model-evaluation, gemini]
created: 2026-07-21
updated: 2026-07-21
---

# Is Gemini 3 Really the Best AI Ever?

Cole reacts to Google's Gemini 3 release by pushing back on the reflex to crown every new model "the best AI ever" based on benchmark jumps. He argues benchmarks increasingly resemble marketing material because models are trained specifically to ace these tests, and they do not resemble how people actually use LLMs in the wild. For coding, benchmarks are LeetCode-style puzzles like reversing a linked list, not the messy real work engineers do. The only current way to know whether a model is truly better is to try it yourself and wait for a slow-forming community consensus, which is itself neither trustworthy nor immediate.

His central point is that developer productivity has stayed roughly flat even as benchmark capability appears to explode, citing a study of top open-source contributors. He reflects that his own large productivity gains over the past year may owe more to his tooling and AI coding system than to the underlying model, noting that even four-generations-old Claude Sonnet 3.5 was crushing it for him. He demonstrates this with Google's new Anti-Gravity IDE, whose built-in Chrome integration lets Gemini 3 autonomously open a browser, navigate a site, wait for rendering, and visually verify frontends. That capability is layered on top of the model, and it makes the whole experience feel dramatically better at design work even though the model alone is only part of the story.

The proposed solution is to move evals off synthetic benchmarks and onto real engineering tasks. He highlights Cline's Kleinbench, which leverages the fact that public GitHub repos already record how real engineers change code over time. An opt-in, privacy-first, open-source-only system captures three pieces per task, the starting repo snapshot, the prompt and process, and the committed end state, to build reliable real-world evals, document system gaps, and generate training data. He stresses that Cline may not become the standard; the point is the direction, evaluating LLMs on real tasks rather than puzzles.

## Concepts covered

- [Agent Evaluation](../concepts/agent-evaluation.md)
- [Real-World Coding Benchmarks](../concepts/coding-benchmarks.md)
- [AI Coding Harness](../concepts/ai-coding-harness.md)
- [End-to-End Validation](../concepts/end-to-end-validation.md)
- [Model Selection](../concepts/model-selection.md)

## Entities

- [Cline](../entities/tools/cline.md)
- [GitHub](../entities/tools/github.md)
- [Claude Code](../entities/tools/claude-code.md)
- [Windsurf](../entities/tools/windsurf.md)
- [Google](../entities/organizations/google.md)
- [Cole Medin](../entities/people/cole-medin.md)

## Key moments

- **[0:00:00]** Framing: Google released Gemini 3, but declaring it 'the best AI ever' from benchmarks is not that simple
- **[0:00:26]** Core problem: benchmarks look like marketing material; models are trained to ace these tests
- **[0:01:45]** The benchmark-vs-productivity gap: capability curve explodes while developer productivity is a flat line
- **[0:02:46]** Personal anecdote: Sonnet 3.5 (4 generations old) still crushed it; gains may be the tooling not the model
- **[0:04:09]** Anti-Gravity demo: Google's new AI IDE with Gemini 3 and autonomous Chrome browser verification
- **[0:07:20]** Gemini 3 is legit (huge ARC-AGI-2 abstract-reasoning jump), but tools on top blur how powerful it really is
- **[0:08:13]** Solution: Kleinbench uses public GitHub repos as real-engineering-task evals
- **[0:09:33]** Three pieces needed per task: starting snapshot, prompt/process, committed end state
- **[0:11:35]** Cline may not be the standard; the point is moving evals to real tasks, not puzzles

## Transcript

[Raw transcript](../raw/is-gemini-3-really-the-best-ai-ever.md)
