---
type: entity
subtype: tool
title: "bolt.diy"
description: "Front-end build tools cited as examples of domains that already have strong built-in self-correction, so the knowledge-graph MCP isn't needed there."
resource: "https://bolt.diy"
tags: [ai-coding, open-source, app-builder]
videos: [ai-code-that-fixes-itself-an-mcp-you-can-try-now, brand-new-stealth-llm-released-on-openrouter-its-a-beast, lets-settle-the-o3-mini-vs-r1-debate-for-coding-once-and-for-all, deploying-billions-of-ai-agents-is-easier-than-you-think, deepseek-r1-just-revolutionized-ai-forever, insane-new-strategy-for-building-ai-agent-apps, the-glow-up-every-ai-agent-needs, pydantic-ai-deepseek-v3-the-best-ai-agent-combo, how-to-dominate-with-ai-in-2025, boltdiy-the-future-of-open-source-ai-coding-whats-next, i-created-the-best-ai-agent-platform-in-just-2-months, breaking-news-ottodev-is-now-the-official-open-source-boltnew, our-boltnew-forks-most-requested-feature-is-finally-here]
created: 2026-07-21
updated: 2026-07-21
---

# bolt.diy

bolt.diy is the community-driven, open-source version of [bolt.new](./bolt-new.md), and after Cole's platform partnered with StackBlitz, it became the official one: "my platform automator is partnering with stack Blitz to make bolt.diy the official open-source bolt.new." Cole frames it as a shared mission: "bolt.diy which we as a community are building to be the best open-source AI coding assistant." The "DIY" is the whole point, "do-it-yourself really speaks well to being able to run this yourself, test with your own local llms."

Its defining feature versus the commercial product is total [model](../../concepts/model-selection.md) freedom: you can use "basically any large language model that you could dream of," many of them free, including [local models](../../concepts/local-ai.md) via Ollama. New models on OpenRouter work instantly, "without me even having to update bolt.diy we instantly have access to... free to build out our front ends." Cole uses it to build "beautiful front ends," often as the second step of a [vibe-coding](../../concepts/vibe-coding.md) flow, for example starting an app in Lovable then moving it "into bolt.diy to do a bunch of improvements with Gemini for free."

He also cites front-end builders like bolt.diy as a domain that already has strong built-in [self-correction](../../concepts/agentic-coding.md), the reason his knowledge-graph MCP is less necessary there. It shares bolt.new's web-container constraints (localhost agent requests are blocked) and its browser-first [security](../../concepts/agent-security.md) model. Lineage: bolt.new -> bolt.new-any-llm -> [oTToDev/autodev](./ottodev.md) -> bolt.diy.

## Realizes

- [Community-Driven Development](../../concepts/community-driven-development.md) - Building products and open source in public with a community, using a public roadmap and shared learning.
- [Local & Self-Hosted AI](../../concepts/local-ai.md) - Running open-weight models on your own hardware or cloud for privacy, cost control, and independence from API providers.
- [File Diffs Instead of Full Rewrites](../../concepts/file-diffs-vs-rewrites.md) - Applying targeted diffs (file walking) rather than rewriting whole files makes an AI coding tool faster, cheaper, and less destructive on edits.

## Contrasts with

- [bolt.new](./bolt-new.md) - StackBlitz's commercial AI coding platform that generates entire full-stack applications; the stable product bolt.DIY forks from.
- [Lovable](./lovable.md) - AI app builder optimized for Claude 3.5 Sonnet; Cole's earlier lovable build is the comparison baseline for the R1 build.

## Related

- [QwQ](./qwq.md) - Alibaba's open reasoning model, cited as the kind of model that could draft a plan or README before any code is generated.
- [oTToDev (autod Dev)](./ottodev.md) - Community fork of bolt.new that adds support for any LLM, including local models via Ollama; the tool this video is built around.
- [LM Studio](./lm-studio.md) - Desktop app for downloading and running open-weight LLMs locally, the main alternative to Ollama and a requested provider integration for the bolt.new fork.
- [autodev (bolt.new fork)](./autodev.md) - Cole's community-built fork of bolt.new, used to generate the front-end wrapper (vanilla JS/HTML) that embeds the Voiceflow chat widget.
- [Model Selection](../../concepts/model-selection.md) - Choosing the right LLM per task by trading off quality, speed, and cost, often routing easy requests to cheap models and hard ones to expensive models.
- [Vibe Coding](../../concepts/vibe-coding.md) - Building software by conversationally prompting an AI without closely reading the code, useful for prototypes but risky for production.
- [Agentic Coding](../../concepts/agentic-coding.md) - Letting an AI agent drive software development end-to-end, from planning through implementation and validation, with human steering.
- [Agent Security](../../concepts/agent-security.md) - Sandboxing agents, scoping permissions, and keeping secrets out of the model to limit blast radius and prevent abuse.
- [Eric Simons](../people/eric-simons.md) - CEO and co-founder of StackBlitz (maker of bolt.new) who announces the partnership making the community fork the official open-source bolt.DIY and frames it as a real-world benchmark frontier labs test models against.
- [Mistral](../organizations/mistral.md) - French AI lab and LLM provider whose models were added to the bolt.new fork as a first-class API integration by popular community request.

## Sources

- [AI Code That Fixes Itself (An MCP You Can Try Now)](../../sources/ai-code-that-fixes-itself-an-mcp-you-can-try-now.md) - "[0:07:13] building front-end applications is a really good example because we have tools like our very own open source bolt.diy. We've got Bolt.new and Lovable."
- [BRAND NEW \"Stealth\" LLM Released on OpenRouter (It's a BEAST)](../../sources/brand-new-stealth-llm-released-on-openrouter-its-a-beast.md) - "[0:10:13] without me even having to update bolt.diy we instantly have access to quazar Alpha for free to build out our front ends"
- [Let's Settle the o3-mini Vs. R1 Debate for Coding ONCE and for ALL](../../sources/lets-settle-the-o3-mini-vs-r1-debate-for-coding-once-and-for-all.md)
- [Deploying Billions of AI Agents is Easier than You Think](../../sources/deploying-billions-of-ai-agents-is-easier-than-you-think.md) - "[0:15:38] moved it into bolt.diy to do a bunch of improvements with Gemini for free"
- [DeepSeek R1 Just Revolutionized AI Forever](../../sources/deepseek-r1-just-revolutionized-ai-forever.md)
- [INSANE New Strategy for Building AI Agent Apps](../../sources/insane-new-strategy-for-building-ai-agent-apps.md) - "[0:00:33] bolt.diy which we as a community are building to be the best open- source AI coding assistant"
- [The GLOW-UP Every AI Agent Needs](../../sources/the-glow-up-every-ai-agent-needs.md)
- [Pydantic AI + DeepSeek V3 - The BEST AI Agent Combo](../../sources/pydantic-ai-deepseek-v3-the-best-ai-agent-combo.md)
- [How to DOMINATE with AI in 2025](../../sources/how-to-dominate-with-ai-in-2025.md)
- [bolt.diy: The Future of Open Source AI Coding - What's Next?](../../sources/boltdiy-the-future-of-open-source-ai-coding-whats-next.md) - "[0:00:00] my platform automator is partnering with stack Blitz to make bolt.diy the official open- Source bolt.new"
- [I Created the BEST AI Agent Platform in Just 2 MONTHS!](../../sources/i-created-the-best-ai-agent-platform-in-just-2-months.md)
- [BREAKING NEWS: oTToDev is Now the OFFICIAL Open Source Bolt.new](../../sources/breaking-news-ottodev-is-now-the-official-open-source-boltnew.md) - "[0:10:45] DIY which stands for do-it-yourself really speaks well to being able to run this yourself test with your own local llms"
- [Our Bolt.new Fork's Most Requested Feature is FINALLY Here](../../sources/our-boltnew-forks-most-requested-feature-is-finally-here.md)
