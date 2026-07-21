---
type: source
title: "BRAND NEW \"Stealth\" LLM Released on OpenRouter (It's a BEAST)"
description: "OpenRouter's first stealth Foundation model, Quasar Alpha, is a fast, coding-optimized, million-token LLM that matches Claude 3.7 Sonnet's quality at roughly 4x the speed, hinting that the usual speed-vs-power tradeoff may be closing."
youtube_id: nCzDnpWSiro
url: https://www.youtube.com/watch?v=nCzDnpWSiro
slug: brand-new-stealth-llm-released-on-openrouter-its-a-beast
published: 2025-04-03
duration: "0:14:42"
recency_rank: 103
raw: "../raw/brand-new-stealth-llm-released-on-openrouter-its-a-beast.md"
tags: [model-selection, openrouter, agentic-coding, benchmarks, mcp]
created: 2026-07-21
updated: 2026-07-21
---

Cole tests Quasar Alpha, the first "cloaked" or stealth model OpenRouter has offered: a pre-release, long-context (1M token) Foundation model from an undisclosed lab (possibly OpenAI, Anthropic, or Google), free to use through the OpenRouter API. He walks through where to find it, how to grab an API key, and frames the whole video as speculative early testing since preliminary benchmarks on a day-old model deserve a grain of salt. On general benchmarks it sits near QwQ, o3-mini, and DeepSeek R1 and slightly above Claude 3.7 Sonnet; on coding-specific Python and Bash tests it shines while being dramatically faster, suggesting it is a smaller, non-reasoning model.

He puts it through three real tests. First, raw chat speed in the OpenRouter chat room (lightning fast, not a reasoning model), though a long-context test fails with a 400 error, so he cannot verify needle-in-a-haystack recall. Second, agentic coding with Archon, his open-source agent builder: Quasar Alpha builds an MCP-connected "agent army" about 4x faster than Claude 3.7 Sonnet with comparable code quality (both needed a couple of iterations to get MCP config right), then runs as the LLM powering the agents themselves, searching the web via Brave, writing to Airtable, and posting to Slack in one multi-tool request, faster than even GPT-4o mini. Third, front-end generation in bolt.diy, where it near-perfectly replicates a landing-page screenshot and spins up a themed chat app in about ten seconds.

Cole's takeaway: Quasar Alpha probably will not revolutionize AI, but its combination of solid power and standout speed could be a game changer for use cases that normally force you to sacrifice speed for capability (like R1 or o3). He invites viewers to guess the provider and the eventual pricing.

## Concepts covered

- [Model Selection](../concepts/model-selection.md)
- [Agentic Coding](../concepts/agentic-coding.md)
- [Context Window Limits](../concepts/context-window-limits.md)
- [Model Context Protocol (MCP)](../concepts/mcp.md)
- [Vibe Coding](../concepts/vibe-coding.md)

## Entities

- [OpenRouter](../entities/tools/openrouter.md)
- [Archon](../entities/tools/archon.md)
- [bolt.diy](../entities/tools/bolt-diy.md)
- [MCP (Model Context Protocol)](../entities/tools/mcp.md)
- [GPT-4o mini](../entities/tools/gpt-4o-mini.md)
- [Cole Medin](../entities/people/cole-medin.md)
- [Dynamous](../entities/organizations/dynamous.md)

## Key moments

- **[0:00:00]** Announces Quasar Alpha, OpenRouter's first stealth pre-release Foundation model, 1M context, coding-optimized, free
- **[0:01:08]** How to access it: OpenRouter chat room or create an API key to use in Python/agents
- **[0:01:53]** Preliminary benchmarks: near QwQ/o3-mini/DeepSeek R1, slightly above Claude 3.7 Sonnet; shines on coding tests
- **[0:03:44]** Long-context test fails, 400 error on longer prompts, can't run needle-in-a-haystack
- **[0:04:59]** Builds an MCP agent army in Archon ~4x faster than Claude 3.7 Sonnet, comparable code quality
- **[0:08:02]** Runs the agent with Quasar Alpha as the LLM: Brave web search + Airtable write + Slack message in one request
- **[0:10:13]** bolt.diy front-end tests: replicates a landing-page screenshot and builds a chat app in ~10 seconds
- **[0:13:39]** Verdict: speed is the headline; may close the usual speed-vs-power tradeoff

## Transcript

[Raw transcript](../raw/brand-new-stealth-llm-released-on-openrouter-its-a-beast.md)
