---
type: entity
subtype: tool
title: "Lovable"
description: "AI app builder optimized for Claude 3.5 Sonnet; Cole's earlier lovable build is the comparison baseline for the R1 build."
resource: "https://lovable.dev"
tags: [ai-coding, app-builder]
videos: [google-is-quietly-revolutionizing-ai-agents-this-is-huge, deploying-billions-of-ai-agents-is-easier-than-you-think, deepseek-r1-just-revolutionized-ai-forever, insane-new-strategy-for-building-ai-agent-apps, revealing-my-complete-ai-agent-blueprint]
created: 2026-07-21
updated: 2026-07-21
---

# Lovable

Lovable is an AI app builder that Cole relies on as his default for front-end work: "we have Lovable. This is my solution to build out almost all of my front-end applications for everything that I'm doing with AI." Like [bolt.new](./bolt-new.md), it is optimized around Claude 3.5 Sonnet and typically outputs a Vite + React project, "this is built with vite and react, that's typically what lovable and bolt will spit out for you."

Cole's most common pattern is to use Lovable as the starting point of a build and then hand off: "we just started with lovable, built our app there, and then moved it into bolt DIY to do a bunch of improvements." He also treats an earlier Lovable build as the comparison baseline when evaluating new [models](../../concepts/model-selection.md), for instance judging a DeepSeek R1 front-end against it, and used Lovable to build the first version of the Dynamous community landing page, so it recurs as his [rapid-prototyping](../../concepts/rapid-prototyping.md) benchmark.

Against [bolt.new](./bolt-new.md) and [bolt.diy](./bolt-diy.md), Cole finds the tools "pretty comparable" but with distinct strengths: Lovable "does a bit better" on certain app-style builds, while bolt is stronger at landing pages. One concrete [deployment](../../concepts/agent-deployment.md) advantage: chatting with a local agent "will not work within bolt. new or bolt. DIY because the web container actually blocks requests to the localhost agents, so lovable is a bit better in this way." He notes its output does not always "look the best" out of the box, a reminder that generated front-ends still need iteration.

## Related

- [Model Selection](../../concepts/model-selection.md)
- [Agent Deployment](../../concepts/agent-deployment.md)
- [Agent Security](../../concepts/agent-security.md)
- [Agent Protocols](../../concepts/agent-protocols.md)
- [Agent Development Lifecycle](../../concepts/agent-development-lifecycle.md)
- [Rapid Prototyping](../../concepts/rapid-prototyping.md)
- [bolt.new](./bolt-new.md)
- [bolt.diy](./bolt-diy.md)

## Sources

- [Google is Quietly Revolutionizing AI Agents (This is HUGE)](../../sources/google-is-quietly-revolutionizing-ai-agents-this-is-huge.md) - "[0:12:35] we have Lovable. This is my solution to build out almost all of my front-end applications for everything that I'm doing with AI."
- [Deploying Billions of AI Agents is Easier than You Think](../../sources/deploying-billions-of-ai-agents-is-easier-than-you-think.md) - "[0:15:23] we just started with lovable built our app there and then moved it into bolt DIY to do a bunch of improvements"
- [DeepSeek R1 Just Revolutionized AI Forever](../../sources/deepseek-r1-just-revolutionized-ai-forever.md) - "[0:12:17] I actually built something very similar in one of the previous videos on my channel using lovable"
- [INSANE New Strategy for Building AI Agent Apps](../../sources/insane-new-strategy-for-building-ai-agent-apps.md) - "[0:20:14] chatting with the agent will not work within bolt. new or bolt. DIY because the web container actually blocks requests to the Local Host agents here so lovable is a bit better in this way"
- [Revealing my COMPLETE AI Agent Blueprint](../../sources/revealing-my-complete-ai-agent-blueprint.md)
