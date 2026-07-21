---
type: source
title: "Our Bolt.new Fork's Most Requested Feature is FINALLY Here"
description: "oTToDev, the community-built open-source fork of Bolt.new, ships its most-requested feature (importing existing local projects) alongside a wave of contributor-driven improvements that push it toward a mature, best-in-class open-source AI coding assistant."
youtube_id: nkqQfABopyc
url: https://www.youtube.com/watch?v=nkqQfABopyc
slug: our-boltnew-forks-most-requested-feature-is-finally-here
published: 2024-12-01
duration: "0:15:25"
recency_rank: 137
raw: "../raw/our-boltnew-forks-most-requested-feature-is-finally-here.md"
tags: [bolt-diy, open-source, browser-coding, community]
created: 2026-07-21
updated: 2026-07-21
---

# Our Bolt.new Fork's Most Requested Feature is FINALLY Here

This is a community update video on oTToDev (the open-source [bolt.new](../entities/tools/bolt-new.md) fork, later [bolt.diy](../entities/tools/bolt-diy.md)) that Cole Medin is stewarding. The headline feature is the ability to import an existing local project folder into the [browser-based coding](../concepts/browser-based-ai-coding.md) platform so you can keep building on code you already wrote elsewhere; Cole demos uploading 13 files and shows the AI immediately understanding and extending them as if the code had been written in the same conversation. He flags a practical constraint of the WebContainer-based architecture: keep imports under roughly 100 files and exclude node_modules, because every file must be pulled into the front end before it can be filtered, and huge imports crash the site.

The rest of the video is a roadmap and contributor tour, a study in [community-driven development](../concepts/community-driven-development.md). Cole walks the high-priority roadmap items (loading local projects done, GitHub repo import in progress, attaching images to prompts almost done) and credits specific community contributors for changes like [reverting code to earlier versions and forking chats](../concepts/conversation-checkpointing.md), [Cohere](../entities/organizations/cohere.md) integration, dynamic per-model max-token limits (a [model-selection](../concepts/model-selection.md) concern), [prompt caching](../concepts/prompt-caching.md), linting/testing/CI cleanup, and an auto-generated documentation page compiled from the repo's markdown.

He gives a live demo of the in-progress image-to-prompt feature by checking out the PR branch via GitHub Desktop, reinstalling with pnpm, and uploading a screenshot for a vision-capable model ([Anthropic](../entities/organizations/anthropic.md)'s Claude, [OpenAI](../entities/organizations/openai.md)'s GPT-4o) to describe and attempt to replicate as HTML, illustrating [prompting techniques for AI coding](../concepts/ai-coding-prompting.md). Vision-only models are required here, so [Ollama](../entities/tools/ollama.md)-hosted Qwen/Llama will not work. Cole closes by teasing a strategic partnership that will bring open-source expertise, financial incentives to reward contributors, and visibility to transition oTToDev from a hobbyist project into "the real deal." The throughline is open-source, contributor-driven development turning a month-and-a-half-old fork into a mature project.

## Concepts covered

- [Browser-Based AI Coding Tools](../concepts/browser-based-ai-coding.md)
- [Reverting and Forking Conversations](../concepts/conversation-checkpointing.md)
- [Prompting Techniques for AI Coding](../concepts/ai-coding-prompting.md)
- [Model Selection](../concepts/model-selection.md)
- [Prompt Caching](../concepts/prompt-caching.md)
- [Community-Driven Development](../concepts/community-driven-development.md)

## Entities

- [bolt.diy](../entities/tools/bolt-diy.md)
- [bolt.new](../entities/tools/bolt-new.md)
- [Cole Medin](../entities/people/cole-medin.md)
- [Anthropic](../entities/organizations/anthropic.md)
- [OpenAI](../entities/organizations/openai.md)
- [Ollama](../entities/tools/ollama.md)
- [Cohere](../entities/organizations/cohere.md)
- [GitHub](../entities/tools/github.md)

## Key moments

- **[0:00:16]** Announces the most-requested feature: loading existing local projects into oTToDev
- **[0:02:38]** Demo: importing a 13-file local project folder; AI understands all files
- **[0:03:06]** Constraint: keep imports under ~100 files, exclude node_modules (front-end must load all files before filtering)
- **[0:04:01]** Conversation controls: revert to a specific message and fork the chat
- **[0:05:39]** Roadmap: local projects done, GitHub import in progress, image attachments almost done
- **[0:06:48]** Contributor changelog: revert code, Cohere integration, dynamic max tokens, prompt caching
- **[0:10:23]** Live demo of in-progress image-to-prompt: checkout PR branch via GitHub Desktop, pnpm install, run
- **[0:11:24]** Vision-only: image upload works only with multimodal models (Claude, GPT-4o), not Qwen/Llama
- **[0:13:11]** Teases strategic partnership: open-source expertise, financial incentives, visibility

## Transcript

[Raw transcript](../raw/our-boltnew-forks-most-requested-feature-is-finally-here.md)
