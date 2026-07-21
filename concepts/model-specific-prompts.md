---
type: concept
title: "Model-Specific Prompts"
description: "Different LLMs need different prompts, so a serious system keeps a library of model-tuned system prompts instead of reusing one prompt written for a single frontier model."
tags: [prompting, model-selection]
videos: [ottodev-is-becoming-the-best-open-source-ai-coding-assistant, boltdiy-the-future-of-open-source-ai-coding-whats-next]
created: 2026-07-21
updated: 2026-07-21
---

# Model-Specific Prompts

A model-specific prompt is a system prompt written and tuned for one model rather than shared across all of them. The insight comes from watching a multi-model coding tool degrade the moment you swap the model: "building in different prompts for different llms it's pretty obvious that if you just compare the performance of Sonet to other models that bolt. new was definitely made testing constantly with Sonet prompted for Sonet" [0:07:43]. The prompt was never neutral. It encoded the habits of the model it was developed against, so every other model inherited instructions written for someone else.

Once a product supports many providers, that becomes a first-class feature rather than a nicety: "having different prompts that work better for different llms especially local ones is going to be a really important feature" [0:08:00]. The emphasis on local models is the point. Smaller open-weight models tolerate far less ambiguity, need tighter output formatting, and lose tool calls when instructions sprawl, so the prompt that a frontier model glides through is the prompt that breaks them.

## What this changes in practice

Treating the prompt as model-dependent turns prompting into a small matrix instead of a single artifact. The prompt library becomes part of the system's configuration: one entry per supported model, each version-controlled and evaluated on the same tasks so a regression on one model does not get hidden by a win on another. It also reframes [model selection](./model-selection.md). You are not choosing a model, you are choosing a model-plus-prompt pair, and a weaker model with a prompt written for it can beat a stronger model running someone else's.

It is also the honest cost of [provider independence](./provider-independence.md). Swapping providers is easy at the API layer and hard at the prompt layer, and pretending otherwise is how "we support every model" quietly means "we work well with one."

## Builds on

- [Prompt Engineering](./prompt-engineering.md) - the base discipline this specializes.
- [System Prompt Engineering](./system-prompt-engineering.md) - the artifact that gets forked per model.

## Related

- [Model Selection](./model-selection.md) - pick the model and its prompt together, not separately.
- [Provider Independence](./provider-independence.md) - portability across providers is a prompt problem before it is an SDK problem.
- [Prompt Templating](./prompt-templating.md), [Prompt Versioning](./prompt-versioning.md) - how a per-model prompt library is stored and kept honest over time.
- [Local LLMs as Agents](./local-llms-as-agents.md), [Local AI](./local-ai.md) - the models that need bespoke prompting most.
- [Effective Prompting](./effective-prompting.md), [Avoid Negative Instructions](./avoid-negative-instructions.md) - techniques whose payoff varies sharply by model strength.
- [Open Source AI Coding](./open-source-ai-coding.md) - the multi-model tools where this surfaced first.

## Implemented by

- [oTToDev (autod Dev)](../entities/tools/ottodev.md) - the community fork that made per-LLM prompts a roadmap feature.
- [bolt.diy](../entities/tools/bolt-diy.md) - the multi-provider successor carrying the same requirement forward.
- [bolt.new](../entities/tools/bolt-new.md) - the original, whose single prompt was tuned against Sonnet.
- [Claude 3.5 Sonnet](../entities/tools/claude-3-5-sonnet.md) - the model that prompt was written for.
- [Ollama](../entities/tools/ollama.md) - the local runtime whose models most need their own prompts.

## Sources

- [oTToDev is Becoming the BEST Open Source AI Coding Assistant](../sources/ottodev-is-becoming-the-best-open-source-ai-coding-assistant.md) - "[0:07:43] building in different prompts for different llms it's pretty obvious that if you just compare the performance of Sonet to other models that bolt. new was definitely made testing constantly with Sonet prompted for Sonet"
- [oTToDev is Becoming the BEST Open Source AI Coding Assistant](../sources/ottodev-is-becoming-the-best-open-source-ai-coding-assistant.md) - "[0:08:00] having different prompts that work better for different llms especially local ones is going to be a really important feature"
