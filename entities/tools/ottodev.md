---
type: entity
subtype: tool
title: "oTToDev (autod Dev)"
description: "Community fork of bolt.new that adds support for any LLM, including local models via Ollama; the tool this video is built around."
resource: "https://github.com/coleam00/bolt.new-any-llm"
tags: [ai-coding, open-source, app-builder]
videos: [ottodev-is-becoming-the-best-open-source-ai-coding-assistant, how-to-use-boltnew-for-free-with-local-llms-and-no-rate-limits]
created: 2026-07-21
updated: 2026-07-21
---

# oTToDev (autod Dev)

oTToDev (transcribed in Cole's videos as "autod Dev") is the community fork of [bolt.new](./bolt-new.md) that started life as "bolt.new-any-llm." Cole defines its founding purpose directly: "we as a community started autod Dev, a fork of bolt. new, that aims to implement a bunch of much needed features including being able to use any large language model like local ones with olama." The shared goal, repeated across the videos, is to build "the best open-source AI coding assistant."

Its headline capability is [provider independence](../../concepts/provider-independence.md): unlike the single-LLM commercial product, oTToDev lets you plug in any [model](../../concepts/model-selection.md), cloud or [local](../../concepts/local-ai.md) via Ollama, and Cole regularly stress-tests brand-new models (DeepSeek R1, Qwen, o3-mini) through it. That flexibility surfaces real [context-window](../../concepts/context-window-limits.md) and [iterative-prompting](../../concepts/iterative-prompting.md) tradeoffs between models. Setup is documented in the repo README, and Cole covers running it "both with Docker and without Docker."

oTToDev is a stage in a single evolving [open-source](../../concepts/open-source-ai-coding.md) project, not a separate tool: bolt.new -> bolt.new-any-llm -> oTToDev / [autodev](./autodev.md) -> [bolt.diy](./bolt-diy.md). After the StackBlitz partnership made it the official open-source bolt.new, it was renamed to bolt.diy, so this page and its siblings describe the same lineage under the names Cole used at each point in time.

## Related

- [Open-Source & Local AI Coding](../../concepts/open-source-ai-coding.md)
- [Local & Self-Hosted AI](../../concepts/local-ai.md)
- [Model Selection](../../concepts/model-selection.md)
- [Provider Independence](../../concepts/provider-independence.md)
- [Context Window Limits](../../concepts/context-window-limits.md)
- [Iterative Prompting](../../concepts/iterative-prompting.md)
- [bolt.new](./bolt-new.md)
- [bolt.diy](./bolt-diy.md)
- [autodev (bolt.new fork)](./autodev.md)

## Sources

- [oTToDev is Becoming the BEST Open Source AI Coding Assistant](../../sources/ottodev-is-becoming-the-best-open-source-ai-coding-assistant.md) - "[0:00:00] we are building to be the best open- source AI coding assistant"
- [How to Use Bolt.new for FREE with Local LLMs (And NO Rate Limits)](../../sources/how-to-use-boltnew-for-free-with-local-llms-and-no-rate-limits.md) - "[0:00:00] we as a community started autod Dev a for bolt. new that aims to implement a bunch of much needed features including being able to use any large language model like local ones with olama"
