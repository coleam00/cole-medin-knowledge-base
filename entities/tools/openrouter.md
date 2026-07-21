---
type: entity
subtype: tool
title: "OpenRouter"
description: "Unified API gateway to many LLMs; here it hosts Quasar Alpha, its first stealth/cloaked pre-release Foundation model, free to use."
resource: "https://openrouter.ai"
tags: [llm, model-gateway]
videos: [claude-plans-gemini-designs-the-workflow-to-build-beautiful-frontends, claude-skills-arent-just-for-claude-heres-how-to-build-them-for-any-agent, i-was-wrong-about-ralph-wiggum, learn-90-of-building-ai-agents-in-30-minutes, the-ultimate-guide-to-local-ai-and-ai-agents-the-future-is-here, brand-new-stealth-llm-released-on-openrouter-its-a-beast, openais-brand-new-agents-sdk-crash-course, create-your-own-private-local-ai-cloud-stack-in-under-20-minutes, lets-settle-the-o3-mini-vs-r1-debate-for-coding-once-and-for-all, deepseek-r1-just-revolutionized-ai-forever, the-glow-up-every-ai-agent-needs, pydantic-ai-deepseek-v3-the-best-ai-agent-combo, ottodev-is-becoming-the-best-open-source-ai-coding-assistant, the-king-of-no-code-ai-agent-builders, how-to-use-boltnew-for-free-with-local-llms-and-no-rate-limits, were-taking-this-ai-coding-assistant-to-the-moon-plus-installation-instructions, this-boltnew-fork-is-exploding-dont-miss-out-on-whats-happening, im-building-the-best-open-source-ai-coding-assistant-with-your-help]
created: 2026-07-21
updated: 2026-07-21
---

# OpenRouter

OpenRouter is a single API gateway that fronts nearly every large language model, and it is Cole's default recommendation whenever a project needs model access without committing to one provider. As he puts it in his agent-building crash course, "I would highly recommend using a platform called Open Router because it gives you access to pretty much any large language model you could possibly want." One API key, one base URL, and the entire market of frontier and open models becomes swappable, which is exactly why it recurs across dozens of his builds.

The mechanism is deliberately simple: because OpenRouter speaks the OpenAI-compatible API, you point an existing client at it by "overriding the base URL and API key to use open router so instead of going to open AI it'll go to open router." That one-line swap is how Cole runs DeepSeek V3 inside Pydantic AI, Gemini inside a frontend workflow ("I just used open router as my way to work with Gemini"), and Claude Haiku 4.5 as the cheap coach in his Ralph Wiggum loop. It is the concrete tool that makes [Provider Independence](../../concepts/provider-independence.md) real: agents he ships "you can use Open Router, O Lama, or OpenAI, easy to extend it for others as well."

OpenRouter is also where new models debut. It was the launch venue for the Quasar Alpha stealth model: "for the first time ever open router is giving us a stealth model which they're calling quazar Alpha it's the pre-release of an upcoming long context Foundation model," free to try by creating a key. Cole leans on it for reliability and price too, using "the Nitro version" of DeepSeek R1 to dodge first-party API outages and noting that models routed through it are often "super super cheap," sometimes even cheaper than [GPT-4o mini](./gpt-4o-mini.md). In his local-AI work it is the pragmatic escape hatch: when a fully-private stack is impractical, teams "just use an API like open router because at least the rest of their stack is still private and local." Bolt.new forks and no-code builders integrate it precisely because it auto-fetches "all the models that are available in open router" with live pricing.

## Related

- [Provider Independence](../../concepts/provider-independence.md) - one gateway that makes swapping model providers a base-URL change.
- [Model Selection](../../concepts/model-selection.md) - a live catalog of models with pricing to choose from.
- [Local & Self-Hosted AI](../../concepts/local-ai.md) - the cloud escape hatch when full local hosting is impractical.
- [Memory Systems](../../concepts/memory-systems.md) - supplies the models behind memory-augmented agents.
- [Agent Deployment](../../concepts/agent-deployment.md) - the model access layer for deployed agents.
- [Vibe Coding](../../concepts/vibe-coding.md) - powers no-code and browser builders that pull its model list.
- [Ollama](./ollama.md) - the local-hosting alternative Cole names alongside it.
- [DeepSeek V3](./deepseek-v3.md) and [DeepSeek R1](./deepseek-r1.md) - models he routes through it to avoid first-party outages.
- [Gemini](./gemini.md) - accessed via OpenRouter in his frontend workflow.
- [Pydantic AI](./pydantic-ai.md) and [Bolt.diy](./bolt-diy.md) - frameworks/tools wired to it by overriding the base URL.

## Sources

- [Learn 90% of Building AI Agents in 30 Minutes](../../sources/learn-90-of-building-ai-agents-in-30-minutes.md) - "[0:03:05] I would highly recommend using a platform called Open Router because it gives you access to pretty much any large language model you could possibly want"
- [BRAND NEW "Stealth" LLM Released on OpenRouter (It's a BEAST)](../../sources/brand-new-stealth-llm-released-on-openrouter-its-a-beast.md) - "[0:00:00] for the first time ever open router is giving us a stealth model which they're calling quazar Alpha it's the pre-release of an upcoming long context Foundation model"
- [Pydantic AI + DeepSeek V3 - The BEST AI Agent Combo](../../sources/pydantic-ai-deepseek-v3-the-best-ai-agent-combo.md) - "[0:11:48] we are overriding the base URL and API key to use open router so instead of going to open AI it'll go to open router"
- [Claude Skills Aren't Just for Claude - Here's How to Build Them for ANY Agent](../../sources/claude-skills-arent-just-for-claude-heres-how-to-build-them-for-any-agent.md) - "[0:13:49] this agent you can use Open Router, O Lama, or OpenAI, easy to extend it for others as well."
- [The Ultimate Guide to Local AI and AI Agents (The Future is Here)](../../sources/the-ultimate-guide-to-local-ai-and-ai-agents-the-future-is-here.md) - "[0:23:00] You can use a platform like Open Router. You can just go to open router.ai, sign up, add in some API credits. You can try these open source LLM yourself"
- [DeepSeek R1 Just Revolutionized AI Forever](../../sources/deepseek-r1-just-revolutionized-ai-forever.md) - "[0:20:45] use them through platforms like open router and get access to all this power for super super cheap"
- [Create Your Own Private Local AI Cloud Stack in Under 20 Minutes](../../sources/create-your-own-private-local-ai-cloud-stack-in-under-20-minutes.md) - "[0:05:38] they'll just host AMA somewhere else or just use an API like open router because at least the rest of their stack is still private and local"
- [Claude Plans, Gemini Designs: The Workflow to Build BEAUTIFUL Frontends](../../sources/claude-plans-gemini-designs-the-workflow-to-build-beautiful-frontends.md) - "[0:03:38] I just used open router as my way to work with Gemini."
- [oTToDev is Becoming the BEST Open Source AI Coding Assistant](../../sources/ottodev-is-becoming-the-best-open-source-ai-coding-assistant.md) - "[0:04:03] it's automatically fetching all the models that are available in open router and it's sorted alphabetically they even have pricing for the models"
- [I Was Wrong About Ralph Wiggum](../../sources/i-was-wrong-about-ralph-wiggum.md) - "[0:12:24] I have an API key set up in open router ... going to be slowly exhausted as Ralph Wiggum runs the validation"
- [OpenAI's BRAND NEW Agents SDK (Crash Course)](../../sources/openais-brand-new-agents-sdk-crash-course.md) - "[0:05:18] for anything that is open AI compatible like open router or olama you can use those providers within the SDK as well"
- [Let's Settle the o3-mini Vs. R1 Debate for Coding ONCE and for ALL](../../sources/lets-settle-the-o3-mini-vs-r1-debate-for-coding-once-and-for-all.md) - "[0:04:38] deep seek R1 through open router so I'm going to be using the Nitro version cuz I've been getting some outages with the Deep seek API"
- [How to Use Bolt.new for FREE with Local LLMs (And NO Rate Limits)](../../sources/how-to-use-boltnew-for-free-with-local-llms-and-no-rate-limits.md) - "[0:09:11] if I look at the pricing here in open router it is actually cheaper than even GPT 40 Mini by a little bit"
- [The GLOW-UP Every AI Agent Needs](../../sources/the-glow-up-every-ai-agent-needs.md) - "[0:13:17] we covered our open router API key which you're going to need to access large language models you could set up something else through open AI or anthropic if you want"
- [The KING of No Code AI Agent Builders?!](../../sources/the-king-of-no-code-ai-agent-builders.md) - "[0:17:29] I'm doing this through open router so it's not totally free cuz it's not running locally with AMA but it's going to be less than a penny to create this entire application"
- [We're Taking this AI Coding Assistant to the MOON [Plus Installation Instructions!]](../../sources/were-taking-this-ai-coding-assistant-to-the-moon-plus-installation-instructions.md) - "[0:06:31] for open router you get your open your API key right here and then slap it in right here"
- [This Bolt.new Fork is EXPLODING - Don't Miss out on What's Happening!](../../sources/this-boltnew-fork-is-exploding-dont-miss-out-on-whats-happening.md) - "[0:05:19] you can use deep seek through open router as well for example"
- [I'm Building the BEST Open Source AI Coding Assistant with YOUR Help](../../sources/im-building-the-best-open-source-ai-coding-assistant-with-your-help.md) - "[0:04:34] the first big one that was requested ... is an integration with open router to use their huge range of models"
