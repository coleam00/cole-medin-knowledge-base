---
type: entity
subtype: organization
title: "Anthropic"
description: "Maker of Claude and Claude Code, creator of MCP, and Cole's pick for the best coding LLM and the lab whose research most shapes his practice."
resource: "https://www.anthropic.com"
tags: [ai-lab, claude, claude-code, mcp, coding]
videos: [10-n8n-tips-in-10-minutes-to-10x-your-ai-automations, google-anthropic-and-openais-guides-to-ai-agents-all-in-18-minutes, anthropic-just-dropped-a-masterclass-on-building-agent-harnesses-for-large-codebases, the-next-evolution-of-ai-coding-is-harnesses-heres-how-to-build-them, i-forced-claude-to-code-for-24-hours-nonstop-heres-what-happened, coding-agent-reliability-explodes-when-they-argue-new-adversarial-dev-technique, the-easiest-possible-strategy-for-accurate-rag-step-by-step-guide, the-big-problem-with-mcp-servers-and-the-solution, the-ultimate-guide-to-building-your-own-mcp-servers-free-template, claude-mcp-has-changed-ai-forever-heres-what-you-need-to-know, claude-sonnet-45-the-new-coding-king-sonnet-45-vs-gpt-5-codex, learn-90-of-building-ai-agents-in-30-minutes, how-to-dominate-with-ai-in-2025, is-software-engineering-finally-dead, ai-exploded-in-2025-heres-everything-that-happened]
created: 2026-07-21
updated: 2026-07-21
---

# Anthropic

Anthropic is, more than any other organization, the lab Cole's practice is built on top of. It makes [Claude](../tools/claude.md) and [Claude Code](../tools/claude-code.md), the models and tool he reaches for by default, and when the question is raw quality he is unambiguous: "if you want the absolute best large language model right now I would choose anthropic and go with Claude 3.5 Sonnet" ([0:02:02]), a verdict he later carries forward to Sonnet 4.5 as "generally the best all-around right now" ([0:09:22]). Its definitions ground his teaching too, "within the anthropic article, an agent is a system where the LLM dynamically directs their own processes and tool usage" ([0:02:18]), and "the best guide to dive into for all these patterns is definitely the one from anthropic on building effective agents" ([0:10:08]), the anchor for [Agentic Workflow Engineering](../../concepts/agentic-workflow-engineering.md).

Anthropic's research is a recurring engine for whole videos. It authored [Contextual Retrieval](../../concepts/contextual-retrieval.md), "contextual retrieval, which is something that Anthropic has done a lot of research on. They have some very enticing statistics for how much it helps" ([0:05:37]), and it invented [MCP](../../concepts/mcp.md): "It was November of last year that MCP was first released by Anthropic." Cole treats its open-sourced work as a template, building his own harness on top of Anthropic's long-running-agent harness and running it for 24 hours straight. He also tracks the business, noting its jump "from a $61.5 billion valuation to a whopping $380 billion in less than a year" ([0:04:18]) and its focus on coding: "Anthropic is definitely continuing to push themselves as the enterprise LLM provider especially for coding."

He is a fan without being captured. Despite recommending Claude constantly, he preaches [Provider Independence](../../concepts/provider-independence.md), keeping a [Human in the Loop](../../concepts/human-in-the-loop.md), and picking models by task under [Model Selection](../../concepts/model-selection.md), which for him means Anthropic sits beside [OpenAI](./openai.md) and [Google](./google.md), not above the decision.

## Realizes

- [Model Context Protocol (MCP)](../../concepts/mcp.md) - An open protocol for packaging tools, data, and RAG capabilities as servers that any AI coding assistant or agent can connect to and call with a standard interface.
- [Contextual Retrieval](../../concepts/contextual-retrieval.md) - Prepending LLM-generated context to each chunk before embedding so retrieval understands where the chunk sits in the larger document.
- [Agentic Workflow Engineering](../../concepts/agentic-workflow-engineering.md) - Designing repeatable AI workflows as engineered systems with defined steps, orchestration, and background execution rather than ad-hoc prompting.
- [Context Engineering](../../concepts/context-engineering.md) - The deliberate practice of curating exactly what goes into an LLM's limited context window - system messages, schemas, chat history, and dynamic variables - to avoid overload and keep outputs sharp.

## Contrasts with

- [OpenAI](./openai.md) - Maker of GPT-4o mini (affordable-but-strong chat model) and text-embedding-3-small (recommended RAG embedding model).
- [Google](./google.md) - Author of the A2UI generative-UI specification used in the demo.

## Related

- [Claude](../tools/claude.md) - Named as an example of a large language model that can be turned into an agent.
- [Claude Code](../tools/claude-code.md) - Anthropic's terminal-based agentic coding assistant that is the subject of this complete-guide walkthrough.
- [Claude Agent SDK](../tools/claude-agent-sdk.md) - The engine that powers Claude Code, exposed as a library so you can invoke Claude Code programmatically and build custom agents on top of the same harness.
- [Model Selection](../../concepts/model-selection.md) - Choosing the right LLM per task by trading off quality, speed, and cost, often routing easy requests to cheap models and hard ones to expensive models.
- [Provider Independence](../../concepts/provider-independence.md) - Architecting agents so the underlying model, framework, or client can be swapped without a rewrite, avoiding lock-in through low-level abstractions.
- [Human in the Loop](../../concepts/human-in-the-loop.md) - Keeping a human as the approver and steerer of agentic work rather than fully automating, so AI augments engineers instead of replacing them.
- [Retrieval-Augmented Generation (RAG)](../../concepts/rag.md) - Grounding an LLM's answers by retrieving relevant documents from an external knowledge base and injecting them into the prompt at query time.
- [Cole Medin](../people/cole-medin.md) - AI engineer and educator whose YouTube channel and Dynamous community teach agentic coding; creator of Archon and the source of this entire knowledge base.

## Sources

- [10 n8n Tips in 10 Minutes to 10x Your AI Automations](../../sources/10-n8n-tips-in-10-minutes-to-10x-your-ai-automations.md) - "[0:02:02] if you want the absolute best large language model right now I would choose anthropic and go with Claude 3.5 Sonnet."
- [Google, Anthropic, and OpenAI's Guides to AI Agents ALL in 18 Minutes](../../sources/google-anthropic-and-openais-guides-to-ai-agents-all-in-18-minutes.md) - "[0:10:08] the best guide to dive into for all these patterns is definitely the one from anthropic on building effective agents."
- [Anthropic Just Dropped a Masterclass on Building Agent Harnesses (for Large Codebases)](../../sources/anthropic-just-dropped-a-masterclass-on-building-agent-harnesses-for-large-codebases.md) - "[0:00:33] Anthropic put out this article just a few days ago, how to use cloud code to work in large code bases."
- [The Next Evolution of AI Coding Is Harnesses - Here's How to Build Them](../../sources/the-next-evolution-of-ai-coding-is-harnesses-heres-how-to-build-them.md) - "[0:05:32] with the Claude code source code leak, we found that even Anthropic is leaning a lot more into harnesses... 40% of their code base is just code for harnesses right now."
- [I Forced Claude to Code for 24 Hours NONSTOP, Here's What Happened](../../sources/i-forced-claude-to-code-for-24-hours-nonstop-heres-what-happened.md) - "[0:00:00] A few days ago, Anthropic released this article where they have open sourced their harness for building longunning agents."
- [The BIG Problem with MCP Servers (and the Solution!)](../../sources/the-big-problem-with-mcp-servers-and-the-solution.md) - "[0:00:00] Anthropic admitted to this problem themselves, and they literally built the protocol. So they published this blog post recently covering the main issue with MCP."
- [The EASIEST Possible Strategy for Accurate RAG (Step by Step Guide)](../../sources/the-easiest-possible-strategy-for-accurate-rag-step-by-step-guide.md) - "[0:00:00] it's all based around the idea of contextual retrieval introduced to us by the anthropic team."
- [Claude MCP has Changed AI Forever - Here's What You NEED to Know](../../sources/claude-mcp-has-changed-ai-forever-heres-what-you-need-to-know.md) - "[0:22:24] it's still really important for us to dive into this protocol because anthropic is doing a great job with this."
- [Claude Sonnet 4.5 - The New Coding King? (Sonnet 4.5 vs. GPT 5 Codex)](../../sources/claude-sonnet-45-the-new-coding-king-sonnet-45-vs-gpt-5-codex.md) - "[0:00:00] Anthropic just released Claude Sonnet 4.5 and it is looking really, really good."
- [Learn 90% of Building AI Agents in 30 Minutes](../../sources/learn-90-of-building-ai-agents-in-30-minutes.md) - "[0:09:22] Claude Sonnet 4.5 is generally the best all-around right now."
- [How to DOMINATE with AI in 2025](../../sources/how-to-dominate-with-ai-in-2025.md) - "[0:08:19] anthropic is an incredible company with the amount of research and development they're doing within AI even more than most other companies like open AI at least in my eyes."
- [Is Software Engineering Finally Dead?](../../sources/is-software-engineering-finally-dead.md) - "[0:04:18] if we look at Anthropic here, they went from a $61.5 billion valuation to a whopping $380 billion in less than a year."
- [AI Exploded in 2025 - Here's Everything That Happened](../../sources/ai-exploded-in-2025-heres-everything-that-happened.md) - "[0:10:52] Anthropic is definitely continuing to push themselves as the enterprise LLM provider especially for coding."
- [The ULTIMATE Guide to Building Your Own MCP Servers (Free Template)](../../sources/the-ultimate-guide-to-building-your-own-mcp-servers-free-template.md) - "[0:00:00] Everyone is starting to realize how big of a deal Anthropic's model context protocol is."
- [Coding Agent Reliability EXPLODES When They Argue (New Adversarial Dev Technique)](../../sources/coding-agent-reliability-explodes-when-they-argue-new-adversarial-dev-technique.md) - "[0:01:37] We're going to take a lot of inspiration from Anthropic, and so I'll cover this new blog post from them."
