---
type: concept
title: "Tree-of-Thought Prompting"
description: "Letting a model explore many possibilities and outcomes in parallel branches before committing to an answer, rather than a single linear chain of thought."
tags: [reasoning-pattern, chain-of-thought, tree-of-thought]
videos: [google-anthropic-and-openais-guides-to-ai-agents-all-in-18-minutes]
created: 2026-07-21
updated: 2026-07-21
---

# Tree-of-Thought Prompting

Tree-of-thought prompting has the model branch instead of march: rather than one linear reasoning path, it opens several candidate lines of reasoning, plays each one forward, and then picks. Cole introduces it directly against its predecessor - "the whole idea of tree of thought. Letting our AI agent explore many different possibilities and outcomes in parallel" [0:06:49] - immediately after describing the baseline it extends: "Then we have chain of thought. So, stepby-step logic. This is your classic telling an LLM to think through a problem step by step. And that generally does give us better results" [0:06:35].

The distinction is structural. Chain of thought commits to the first plausible next step and is therefore vulnerable to an early wrong turn that the rest of the reasoning faithfully compounds. Tree of thought keeps several next steps alive, evaluates their downstream consequences, and prunes. That makes it worth the extra tokens on problems where the branch points genuinely matter - architecture choices, search-like planning, anything where you would want a human to sketch two or three approaches before picking one - and wasteful on tasks with one obvious path.

Because these appear side by side in the major vendor agent guides, they are best read as a ladder of reasoning-shaping techniques rather than competing schools: [Zero-Shot Prompting](./zero-shot-prompting.md), then [Few-Shot Prompting](./few-shot-prompting.md), then [Chain-of-Thought Prompting](./chain-of-thought.md), then tree of thought. Each step trades more inference-time compute for more reliable reasoning. The same trade shows up architecturally in [Parallel Agent Execution](./parallel-agent-execution.md), where the branches are separate agents exploring different approaches concurrently and a synthesizer picks the winner, and in [Reasoning Models](./reasoning-models.md), which do a version of this branching and backtracking internally so the prompt does not have to ask for it.

## Builds on

- [Chain-of-Thought Prompting](./chain-of-thought.md) - tree of thought is chain of thought widened into parallel branches.
- [Prompt Engineering](./prompt-engineering.md) - it is one technique in the reasoning-shaping toolkit.

## Contrasts with

- [Reasoning Models](./reasoning-models.md) - these explore and backtrack natively, reducing the need to prompt the branching explicitly.

## Related

- [Agent Prompting Techniques](./agent-prompting.md) - the vendor-guide catalog this sits inside.
- [Parallel Agent Execution](./parallel-agent-execution.md) - the multi-agent analogue: branches as separate agents, then pick the best.
- [Planning with AI](./planning-with-ai.md) - branching before committing is what good planning passes do.
- [Self-Criticism Prompting](./self-criticism-prompting.md) - evaluating branches requires the model to judge its own candidates.
- [Zero-Shot Prompting](./zero-shot-prompting.md) and [Few-Shot Prompting](./few-shot-prompting.md) - the lower rungs of the same ladder.
- [Effective Prompting](./effective-prompting.md) - when the added reasoning cost is actually worth paying.

## Sources

- [Google, Anthropic, and OpenAI's Guides to AI Agents ALL in 18 Minutes](../sources/google-anthropic-and-openais-guides-to-ai-agents-all-in-18-minutes.md) - "[0:06:35] Then we have chain of thought. So, stepby-step logic. This is your classic telling an LLM to think through a problem step by step. And that generally does give us better results."
- [Google, Anthropic, and OpenAI's Guides to AI Agents ALL in 18 Minutes](../sources/google-anthropic-and-openais-guides-to-ai-agents-all-in-18-minutes.md) - "[0:06:49] the whole idea of tree of thought. Letting our AI agent explore many different possibilities and outcomes in parallel."
