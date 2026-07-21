---
type: entity
subtype: tool
title: "bolt.new"
description: "StackBlitz's commercial AI coding platform that generates entire full-stack applications; the stable product bolt.DIY forks from."
resource: "https://bolt.new"
tags: [ai-coding, app-builder]
videos: [my-top-20-lessons-from-building-100s-of-ai-agents-super-actionable, insane-new-strategy-for-building-ai-agent-apps, breaking-news-ottodev-is-now-the-official-open-source-boltnew, our-boltnew-forks-most-requested-feature-is-finally-here, im-addicted-to-windsurf-send-help, claude-computer-use-boltnew-the-ultimate-ai-coding-combo, ottodev-is-becoming-the-best-open-source-ai-coding-assistant, turn-any-ai-agent-into-a-live-person-voice-chat-setup-in-minutes, qwen-just-casually-started-the-local-ai-revolution, how-to-use-boltnew-for-free-with-local-llms-and-no-rate-limits, were-taking-this-ai-coding-assistant-to-the-moon-plus-installation-instructions, this-boltnew-fork-is-exploding-dont-miss-out-on-whats-happening, stop-paying-for-gpt-claude-other-llms-get-them-all-in-one-place, im-building-the-best-open-source-ai-coding-assistant-with-your-help, i-forked-boltnew-and-made-it-way-better]
created: 2026-07-21
updated: 2026-07-21
---

# bolt.new

bolt.new is StackBlitz's commercial, browser-based AI coding platform. Cole's one-line definition: "bolt.new generates entire full stack applications and it's a lot different than you know GitHub copilot in 2022." Everything runs inside a StackBlitz web container in the browser, with a one-click deploy to Netlify, and it is "the stable product for you to go and very easily build anything."

The catch that shaped much of Cole's work is that "bolt.new itself only supports using one LLM, Claude 3.5 Sonnet." Its system prompt was heavily tuned and "prompted for Sonnet," which delivers strong results but locks users to a single provider. That single-[model](../../concepts/model-selection.md) limitation, plus the inability to run [local models](../../concepts/local-ai.md), is exactly what pushed Cole to fork it, first as bolt.new-any-llm, then [oTToDev/autodev](./ottodev.md), and finally the [community-driven](../../concepts/community-driven-development.md) [bolt.diy](./bolt-diy.md), an exercise in [provider independence](../../concepts/provider-independence.md) and [open-source AI coding](../../concepts/open-source-ai-coding.md).

Cole uses bolt.new (and his forks) mainly to generate polished initial front-ends, noting it "pairs very well with Windsurf" for follow-on work, a [human-in-the-loop](../../concepts/human-in-the-loop.md) handoff between the generator and an IDE agent. He benchmarks it against [Lovable](./lovable.md): "honestly lovable and bolt.new are pretty comparable, they do better at certain things though," with bolt stronger at landing pages. Known limits include difficulty loading in existing projects and a web container that blocks requests to localhost agents (breaking embedded iframes and local-agent chat).

## Contrasts with

- [Lovable](./lovable.md) - AI app builder optimized for Claude 3.5 Sonnet; Cole's earlier lovable build is the comparison baseline for the R1 build.
- [bolt.diy](./bolt-diy.md) - Front-end build tools cited as examples of domains that already have strong built-in self-correction, so the knowledge-graph MCP isn't needed there.

## Works with

- [Windsurf](./windsurf.md) - AI coding IDE Cole used to build the Python AG-UI backend and consume the protocol docs.

## Related

- [oTToDev (autod Dev)](./ottodev.md) - Community fork of bolt.new that adds support for any LLM, including local models via Ollama; the tool this video is built around.
- [autodev (bolt.new fork)](./autodev.md) - Cole's community-built fork of bolt.new, used to generate the front-end wrapper (vanilla JS/HTML) that embeds the Voiceflow chat widget.
- [Model Selection](../../concepts/model-selection.md) - Choosing the right LLM per task by trading off quality, speed, and cost, often routing easy requests to cheap models and hard ones to expensive models.
- [Local & Self-Hosted AI](../../concepts/local-ai.md) - Running open-weight models on your own hardware or cloud for privacy, cost control, and independence from API providers.
- [Community-Driven Development](../../concepts/community-driven-development.md) - Building products and open source in public with a community, using a public roadmap and shared learning.
- [Provider Independence](../../concepts/provider-independence.md) - Architecting agents so the underlying model, framework, or client can be swapped without a rewrite, avoiding lock-in through low-level abstractions.
- [Open-Source & Local AI Coding](../../concepts/open-source-ai-coding.md) - Community-maintained, self-hostable AI coding tools and local models that dodge API costs and rate limits.
- [Human in the Loop](../../concepts/human-in-the-loop.md) - Keeping a human as the approver and steerer of agentic work rather than fully automating, so AI augments engineers instead of replacing them.

## Sources

- [My Top 20 Lessons from Building 100s of AI Agents (Super Actionable)](../../sources/my-top-20-lessons-from-building-100s-of-ai-agents-super-actionable.md)
- [INSANE New Strategy for Building AI Agent Apps](../../sources/insane-new-strategy-for-building-ai-agent-apps.md) - "[0:04:33] honestly lovable and bolt.new are pretty comparable they do better at certain things though"
- [BREAKING NEWS: oTToDev is Now the OFFICIAL Open Source Bolt.new](../../sources/breaking-news-ottodev-is-now-the-official-open-source-boltnew.md) - "[0:05:09] bolt.new generates entire full stack applications and it's a lot different than you know GitHub copilot in 2022"
- [Our Bolt.new Fork's Most Requested Feature is FINALLY Here](../../sources/our-boltnew-forks-most-requested-feature-is-finally-here.md)
- [I'm Addicted to Windsurf, Send Help](../../sources/im-addicted-to-windsurf-send-help.md) - "[0:00:48] I still prefer autod Dev or bolt.new to build my initial front ends which by the way they pair very well with wind surf"
- [Claude Computer Use + Bolt.new - The ULTIMATE AI Coding Combo?!](../../sources/claude-computer-use-boltnew-the-ultimate-ai-coding-combo.md)
- [oTToDev is Becoming the BEST Open Source AI Coding Assistant](../../sources/ottodev-is-becoming-the-best-open-source-ai-coding-assistant.md) - "[0:07:43] bolt.new was definitely made testing constantly with Sonnet prompted for Sonnet"
- [Turn ANY AI Agent into a Live Person - Voice Chat Setup in Minutes](../../sources/turn-any-ai-agent-into-a-live-person-voice-chat-setup-in-minutes.md)
- [Qwen Just Casually Started the Local AI Revolution](../../sources/qwen-just-casually-started-the-local-ai-revolution.md)
- [How to Use Bolt.new for FREE with Local LLMs (And NO Rate Limits)](../../sources/how-to-use-boltnew-for-free-with-local-llms-and-no-rate-limits.md) - "[0:00:00] bolt.new itself only supports using one llm Claude 3.5 Sonnet"
- [We're Taking this AI Coding Assistant to the MOON [Plus Installation Instructions!]](../../sources/were-taking-this-ai-coding-assistant-to-the-moon-plus-installation-instructions.md)
- [This Bolt.new Fork is EXPLODING - Don't Miss out on What's Happening!](../../sources/this-boltnew-fork-is-exploding-dont-miss-out-on-whats-happening.md)
- [STOP Paying for GPT, Claude, & Other LLMs - Get them ALL in One Place](../../sources/stop-paying-for-gpt-claude-other-llms-get-them-all-in-one-place.md)
- [I'm Building the BEST Open Source AI Coding Assistant with YOUR Help](../../sources/im-building-the-best-open-source-ai-coding-assistant-with-your-help.md)
- [I Forked Bolt.new and Made it WAY Better](../../sources/i-forked-boltnew-and-made-it-way-better.md) - "[0:01:14] I have fixed both of these problems by forking bolt.new running it locally on my computer and extending the platform"
