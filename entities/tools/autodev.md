---
type: entity
subtype: tool
title: "autodev (bolt.new fork)"
description: "Cole's community-built fork of bolt.new, used to generate the front-end wrapper (vanilla JS/HTML) that embeds the Voiceflow chat widget."
tags: [ai-coding, open-source, app-builder]
videos: [the-king-of-no-code-ai-agent-builders, were-taking-this-ai-coding-assistant-to-the-moon-plus-installation-instructions]
created: 2026-07-21
updated: 2026-07-21
---

# autodev (bolt.new fork)

autodev is Cole's community-built fork of [bolt.new](./bolt-new.md), the same project he elsewhere calls [oTToDev](./ottodev.md) (the "autod Dev" heard in his videos) and which was ultimately renamed [bolt.diy](./bolt-diy.md). He introduces it as a front-end generator: "go to autod Dev, this is my bolt. new fork... I'm going to use this to create a front end basically by telling it just to make a vanilla JS and HTML app with this embed."

In practice Cole uses autodev to spin up lightweight front-end wrappers for agents built elsewhere. The canonical example: after building a [Voiceflow](./voiceflow.md) agent, he uses autodev to generate a vanilla JS/HTML page that embeds the Voiceflow chat widget, turning a no-code agent into a deployable [full-stack app](../../concepts/full-stack-ai-application.md). This makes it a practical [deployment](../../concepts/agent-deployment.md) bridge for [no-code agents](../../concepts/no-code-agents.md) that expose [intents/entities](../../concepts/intents-and-entities.md) and [tool calling](../../concepts/tool-use.md).

The naming is a moment-in-time snapshot: "I'm actually planning on renaming bolt. new any llm to autod Dev... I am definitely down to merge this project into the main bolt. new repo at some point." Cole also shows how to "run autod Dev yourself really easily with Docker." Because it is one link in the bolt.new -> bolt.new-any-llm -> oTToDev/autodev -> bolt.diy chain, its open-source, any-LLM capabilities are documented most fully on the [bolt.diy](./bolt-diy.md) and [oTToDev](./ottodev.md) pages.

## Related

- [Agent Deployment](../../concepts/agent-deployment.md)
- [No-Code AI Agents](../../concepts/no-code-agents.md)
- [Full-Stack AI Application](../../concepts/full-stack-ai-application.md)
- [Intents and Entities](../../concepts/intents-and-entities.md)
- [Tool Calling](../../concepts/tool-use.md)
- [Clarifying Questions](../../concepts/clarifying-questions.md)
- [bolt.new](./bolt-new.md)
- [bolt.diy](./bolt-diy.md)
- [oTToDev (autod Dev)](./ottodev.md)
- [Voiceflow](./voiceflow.md)

## Sources

- [The KING of No Code AI Agent Builders?!](../../sources/the-king-of-no-code-ai-agent-builders.md) - "[0:17:15] go to autod Dev this is my bolt. new Fork ... I'm going to use this to create a front end basically by telling it just to make a vanilla JS and HTML app with this embed"
- [We're Taking this AI Coding Assistant to the MOON [Plus Installation Instructions!]](../../sources/were-taking-this-ai-coding-assistant-to-the-moon-plus-installation-instructions.md) - "[0:01:31] I'm actually planning on renaming bolt. new any llm to autod Dev why well I am definitely down to merge this project into the main bolt. new repo at some point"
