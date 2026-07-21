---
type: entity
subtype: tool
title: "QwQ"
description: "Alibaba's open reasoning model, cited as the kind of model that could draft a plan or README before any code is generated."
resource: "https://qwenlm.github.io/blog/qwq-32b-preview/"
tags: [llm, model]
videos: [boltdiy-the-future-of-open-source-ai-coding-whats-next]
created: 2026-07-21
updated: 2026-07-21
---

# QwQ

QwQ is Alibaba's open-weight [reasoning model](../../concepts/reasoning-models.md), released by the Qwen team as a 32B-class model that thinks out loud before answering. In Cole's catalog it appears less as a chat model and more as a role in a pipeline: the thing that reasons first so that whatever writes the code has something to write against. Sketching a wanted feature for [bolt.diy](./bolt-diy.md), he describes it precisely: "it starts with a reasoning model like qwq it reasons about what it wants to produce based on your prompt" [0:06:41], and puts the output in a README or markdown file before any code generation begins.

That is [Reasoning Model as a Tool](../../concepts/reasoning-model-as-a-tool.md) in its cleanest form. The expensive, slow, deliberate model is not the one doing the typing; it is the one producing the plan, and a cheaper, faster coding model executes against that artifact. It is also the pre-planning step that separates [Vibe Planning](../../concepts/vibe-planning.md) from vibe coding: a written plan is a reviewable, editable contract, so a human can correct the direction before a single file is generated rather than after a broken app exists. Cole raises it as a plugin-shaped idea for bolt.diy, which makes the point that this is a harness pattern, not a property of any one model.

QwQ matters most because it is open. The same [Two-Layer Planning](../../concepts/two-layer-planning.md) split that closed reasoning models made popular becomes reproducible on your own hardware, so a fully [local](../../concepts/local-ai.md) stack can plan and then build without an API key. It shipped in the same wave as [DeepSeek R1](./deepseek-r1.md), which took most of the attention, but QwQ is the earlier proof that open-weight reasoning was viable, and it comes from the same [Qwen](./qwen.md) family Cole leans on for local coding work.

## Realizes

- [Reasoning Models](../../concepts/reasoning-models.md) - models that produce explicit reasoning before answering.
- [Reasoning Model as a Tool](../../concepts/reasoning-model-as-a-tool.md) - the reasoner drafts the plan, a cheaper model executes it.
- [Planning with AI](../../concepts/planning-with-ai.md) - generating the plan artifact before generating code.

## Works with

- [bolt.diy](./bolt-diy.md) - the open-source AI coding app where Cole proposes QwQ as the pre-planning step.
- [Ollama](./ollama.md) - the local runtime that makes running an open reasoning model on your own machine practical.
- [Qwen 2.5 Coder 32B](./qwen.md) - the sibling model from the same family, tuned for writing code rather than reasoning.

## Contrasts with

- [DeepSeek R1](./deepseek-r1.md) - the open reasoning model that arrived in the same wave and took the spotlight.
- [OpenAI o1](./o1.md) - the closed reasoning model QwQ is the open-weight answer to.

## Related

- [Local & Self-Hosted AI](../../concepts/local-ai.md) - open reasoning weights are what make a fully local plan-then-build loop possible.
- [Two-Layer Planning](../../concepts/two-layer-planning.md) - splitting planning and execution across different models.
- [Vibe Planning](../../concepts/vibe-planning.md) - planning carefully so the coding step can be loose.
- [Prototype as a Coding Blueprint](../../concepts/prototype-as-blueprint.md) - another way of producing the artifact the coder builds against.
- [Model Selection](../../concepts/model-selection.md) - choosing the reasoner and the coder separately, per task.

## Sources

- [bolt.diy: The Future of Open Source AI Coding - What's Next?](../../sources/boltdiy-the-future-of-open-source-ai-coding-whats-next.md) - "[0:06:41] it starts with a reasoning model like qwq it reasons about what it wants to produce based on your prompt"
