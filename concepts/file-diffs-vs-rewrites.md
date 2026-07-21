---
type: concept
title: "File Diffs Instead of Full Rewrites"
description: "Applying targeted diffs (file walking) rather than rewriting whole files makes an AI coding tool faster, cheaper, and less destructive on edits."
tags: [ai-coding, diffs]
videos: [boltdiy-the-future-of-open-source-ai-coding-whats-next]
created: 2026-07-21
updated: 2026-07-21
---

# File Diffs Instead of Full Rewrites

File diffs instead of full rewrites is the editing strategy where a coding tool walks to the exact region it needs to change and applies a targeted patch, rather than regenerating an entire file from scratch every time it touches one line. On the [bolt.diy](../entities/tools/bolt-diy.md) roadmap Cole names it as a headline gap against the commercial product: the priority is "having file walking and diffs like commercial bolt. new especially to make it so that bolt. DIY doesn't have to rewrite files as often" [0:04:46].

The reason it is a headline item and not a micro-optimization is that full rewrites are expensive on three axes at once. Every rewrite pays output tokens for code that never changed, which is pure waste against any [cost budget](./llm-cost-optimization.md); it is slow, since the user watches a whole file stream back to see a two-line fix; and it is destructive, because a model regenerating a long file has a fresh chance to drop an import, mangle an unrelated function, or quietly lose formatting. A diff constrains the blast radius to the lines the model actually intended to touch. Large files make all three effects worse, so the pain scales exactly with codebase maturity - the failure mode is far more visible in [brownfield work](./greenfield-vs-brownfield.md) than in a fresh scaffold.

Diffs also change the review surface. A patch is legible: you can read what moved without diffing the file yourself, which is the same ergonomic argument behind [code streaming and other assistant UX patterns](./ai-coding-ux.md). That legibility is what makes fast human [code review](./code-review.md) of agent output practical at all.

Because it is largely a harness-level implementation detail rather than a model capability, diff-based editing is one of the clearest places where open-source tools visibly trail their commercial counterparts and then catch up - which is why it sat on the [open-source AI coding](./open-source-ai-coding.md) roadmap alongside one-click deploys and a plugin system.

## Builds on

- [AI Coding Assistant](./ai-coding-assistant.md) - the tool layer that decides how edits are applied.

## Tools

- [bolt.diy](../entities/tools/bolt-diy.md) - shipped file walking and diffs to stop rewriting whole files.
- [bolt.new](../entities/tools/bolt-new.md) - the commercial reference implementation Cole benchmarks against.

## Related

- [AI Coding Assistant UX Patterns](./ai-coding-ux.md) - how edits are surfaced to the user.
- [LLM Cost Optimization](./llm-cost-optimization.md) - rewrites burn output tokens for unchanged code.
- [Context Window Limits](./context-window-limits.md) - whole-file rewrites consume budget that diffs preserve.
- [Browser-Based AI Coding Tools](./browser-based-ai-coding.md), [Open-Source & Local AI Coding](./open-source-ai-coding.md) - where this gap showed up first.
- [Code Review](./code-review.md) - a patch is reviewable in a way a regenerated file is not.

## Sources

- [bolt.diy: The Future of Open Source AI Coding - What's Next?](../sources/boltdiy-the-future-of-open-source-ai-coding-whats-next.md) - "[0:04:46] having file walking and diffs like commercial bolt. new especially to make it so that bolt. DIY doesn't have to rewrite files as often"
