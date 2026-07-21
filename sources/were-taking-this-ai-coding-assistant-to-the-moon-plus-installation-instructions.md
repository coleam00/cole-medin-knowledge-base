---
type: source
title: "We're Taking this AI Coding Assistant to the MOON [Plus Installation Instructions!]"
description: "Cole's rapidly-growing fork of bolt.new (being renamed 'autoDev') is becoming a community-driven, LLM-agnostic open-source AI coding assistant, and this video announces project updates while giving a step-by-step Docker installation guide."
youtube_id: 31ivQdydmGg
url: https://www.youtube.com/watch?v=31ivQdydmGg
slug: were-taking-this-ai-coding-assistant-to-the-moon-plus-installation-instructions
published: 2024-11-03
duration: "0:13:10"
recency_rank: 146
raw: "../raw/were-taking-this-ai-coding-assistant-to-the-moon-plus-installation-instructions.md"
tags: [open-source, docker, installation, community, provider-independence]
created: 2026-07-21
updated: 2026-07-21
---

This is a project-update and onboarding video for [Cole Medin](../entities/people/cole-medin.md)'s fork of [bolt.new](../entities/tools/bolt-new.md), originally called "bolt.new any LLM" and being renamed [autoDev](../entities/tools/autodev.md). In just three weeks the fork exploded into a large community; the goal is to build the best open-source AI coding assistant, one that lets people use many different LLMs, cloud and local via [Ollama](../entities/tools/ollama.md). Cole covers announcements: a launch live stream, 36 applications to become core contributors, a Discourse community, and the rename.

The bulk of the video is a beginner-friendly installation guide. Prerequisites are [Git](../entities/tools/git.md) and Node.js; you clone the [GitHub](../entities/tools/github.md) repo, then configure API keys by editing the .env.example file (adding keys only for the providers you want, for example [OpenAI](../entities/organizations/openai.md) or [OpenRouter](../entities/tools/openrouter.md)) and renaming it to .env. Cole strongly recommends running with [Docker](../entities/tools/docker.md) rather than natively, because Docker gives an isolated, reproducible environment that eliminates the "works on my machine" class of errors (missing modules, access violations, header and API-key errors) that come from every system being slightly different.

The Docker workflow uses npm helper scripts that wrap Docker commands: `npm run docker:build` to build the container image, then Docker Compose with profiles to spin it up for the development environment. The npm scripts are optional convenience wrappers, so you can run the underlying Docker commands directly and skip installing Node entirely. Once running, you visit localhost:5173, and Cole notes a browser gotcha: bolt.new does not work in standard Google Chrome, so you must use Chrome Canary or Firefox.

## Concepts covered

- [Provider Independence](../concepts/provider-independence.md)
- [Open-Source & Local AI Coding](../concepts/open-source-ai-coding.md)
- [Agent Deployment](../concepts/agent-deployment.md)
- [Agent Security](../concepts/agent-security.md)
- [Community-Driven Development](../concepts/community-driven-development.md)

## Entities

- [bolt.new](../entities/tools/bolt-new.md)
- [autodev (bolt.new fork)](../entities/tools/autodev.md)
- [Docker](../entities/tools/docker.md)
- [GitHub](../entities/tools/github.md)
- [Git](../entities/tools/git.md)
- [Ollama](../entities/tools/ollama.md)
- [OpenRouter](../entities/tools/openrouter.md)
- [OpenAI](../entities/organizations/openai.md)
- [Cole Medin](../entities/people/cole-medin.md)

## Key moments

- **[0:00:00]** Cole introduces the bolt.new fork he started 3 weeks ago and how fast the community/project has grown
- **[0:01:31]** Announces renaming "bolt.new any LLM" to "autoDev" and teases merging into the main bolt.new repo later
- **[0:02:04]** Announces a Discourse community launch and a live stream to showcase updates
- **[0:03:00]** Transition into the step-by-step Docker installation guide
- **[0:04:11]** Prerequisites: install Git and Node.js, then clone the GitHub repo
- **[0:05:44]** Configure API keys by editing .env.example and renaming it to .env; only set keys for providers you use
- **[0:08:18]** Why Docker: isolated environment guarantees the same setup and avoids machine-specific errors
- **[0:09:02]** Run `npm run docker:build` to build the container image
- **[0:10:16]** Use Docker Compose with profiles to run the container; npm scripts are optional wrappers around Docker commands
- **[0:11:14]** Visit localhost:5173; browser gotcha, use Chrome Canary or Firefox, not standard Chrome

## Transcript

[Raw transcript](../raw/were-taking-this-ai-coding-assistant-to-the-moon-plus-installation-instructions.md)
