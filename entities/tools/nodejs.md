---
type: entity
subtype: tool
title: "Node.js"
description: "JavaScript runtime used as an install prerequisite, whose npm scripts act as optional convenience wrappers around the underlying Docker build and run commands."
resource: "https://nodejs.org"
tags: [agent-framework, sdk]
videos: [were-taking-this-ai-coding-assistant-to-the-moon-plus-installation-instructions]
created: 2026-07-21
updated: 2026-07-21
---

# Node.js

Node.js is the JavaScript runtime that executes JS outside a browser, and in Cole's install guides it shows up in the least glamorous role possible: a prerequisite you download and forget about. Walking beginners through setting up his [bolt.new](./bolt-new.md) fork, he keeps it to one line: "the other prerequisite that we need is node.js and so you can just go to nodejs.org and then download uh just from their homepage" ([0:04:41](../../sources/were-taking-this-ai-coding-assistant-to-the-moon-plus-installation-instructions.md)). Alongside [Git](./git.md), that is the entire local toolchain before the repo is cloned.

The interesting part is how little of the install actually depends on it. Cole recommends running [oTToDev](./ottodev.md) with [Docker](./docker.md) rather than natively, because a container gives everyone an identical environment and eliminates the missing-module and access-violation errors that come from every machine being slightly different. The repo ships `npm run docker:build` and friends, which look like Node is doing the work, but he is explicit that they are not: "these npm scripts are just kind of also a wrapper around Docker command so you can use these Docker commands directly to build the container if you want" ([0:09:45](../../sources/were-taking-this-ai-coding-assistant-to-the-moon-plus-installation-instructions.md)). Run the underlying `docker build` and `docker compose` commands and you can skip installing Node entirely.

That distinction is worth internalizing beyond this one project. A package script is a bookmark for a command, not a dependency of it, and treating the two as the same thing is how people end up debugging a runtime they never needed. The [containerized](../../concepts/containerization.md) path is the one Cole actually endorses for [open-source AI coding tools](../../concepts/open-source-ai-coding.md), because reproducibility is the whole reason a community fork with hundreds of contributors can give the same install instructions to everybody. Node.js remains the runtime the app itself is written for, and the ecosystem behind most of the browser-based coding assistants and agent SDKs Cole covers, but as an installation step it is convenience rather than requirement.

## Contrasts with

- [Python](./python.md) - The other runtime Cole's agent and tooling builds land in, chosen per project rather than per preference.

## Works with

- [Docker](./docker.md) - Does the real work behind the npm scripts, and is the install path Cole recommends over running natively.
- [oTToDev (autod Dev)](./ottodev.md) - The community fork whose npm scripts wrap its Docker build and compose commands.
- [bolt.new](./bolt-new.md) - The upstream project the fork is built from.
- [bolt.diy](./bolt-diy.md) - The eventual name of the same open-source browser-based coding assistant.
- [Git](./git.md) - The other install prerequisite; clone the repo, then build.
- [Express.js](./express.md) - A minimal Node web framework Cole uses to stand up small backend APIs that hold secrets for browser clients.
- [TypeScript](./typescript.md) - The go-to language for building MCP servers, especially remote ones deployed to Cloudflare.

## Related

- [Containerization & Docker Networking](../../concepts/containerization.md) - Running each service as a container so the environment is identical everywhere and the runtime install stops mattering.
- [Open-Source & Local AI Coding](../../concepts/open-source-ai-coding.md) - Community-maintained, self-hostable AI coding tools and local models that dodge API costs and rate limits.
- [Provider Independence](../../concepts/provider-independence.md) - Architecting so the underlying model, framework, or client can be swapped without a rewrite.
- [Agent Deployment](../../concepts/agent-deployment.md) - Getting agents to production: containerize, network, reverse-proxy, secure, and pick a cost-predictable host.

## Sources

- [We're Taking this AI Coding Assistant to the MOON [Plus Installation Instructions!]](../../sources/were-taking-this-ai-coding-assistant-to-the-moon-plus-installation-instructions.md) - "[0:04:41] the other prerequisite that we need is node.js and so you can just go to nodejs.org and then download uh just from their homepage"
- [We're Taking this AI Coding Assistant to the MOON [Plus Installation Instructions!]](../../sources/were-taking-this-ai-coding-assistant-to-the-moon-plus-installation-instructions.md) - "[0:09:45] these npm scripts are just kind of also a wrapper around Docker command so you can use these Docker commands directly to build the container if you want"
