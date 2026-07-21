---
type: entity
subtype: tool
title: "Slack"
description: "Messaging platform used as an alerting destination for error workflows and scheduled report notifications, and as the chat surface for talking to agents."
resource: "https://slack.com"
tags: [messaging, chat, notifications, alerting, integration]
videos: [this-completely-changes-the-way-we-build-production-ai-agents-vercel-eve, stripes-coding-agents-ship-1300-prs-every-week-heres-how-they-do-it, i-built-a-safer-openclaw-alternative-using-claude-code, turn-claude-code-into-your-full-engineering-team-with-subagents, docker-just-made-using-mcp-servers-100x-easier-one-click-installs, flowise-n8n-the-best-no-code-local-ai-agent-combo, 10-n8n-tips-in-10-minutes-to-10x-your-ai-automations, the-king-of-no-code-ai-agent-builders, this-slack-ai-personal-assistant-is-better-than-a-real-person, dont-sleep-on-the-ultimate-ai-agent-combo-n8n-langchain-python]
created: 2026-07-21
updated: 2026-07-21
---

# Slack

Slack is a team messaging platform, and across Cole's videos it serves as the everyday human interface to agents and automations: the place agents post to, get told to act from, and report back in. Its appeal is that it is already open on everyone's screen, so it needs no new UI. As Cole puts it about his own second brain, "I really like talking to my second brain in Slack ... I can talk to it in Slack from anywhere. It's super cool. And that's really all I need." That framing, Slack as the [chat interface](../../concepts/chat-interfaces.md) and notification channel rather than a bespoke app, is why it recurs as an integration in nearly every workflow-building demo.

## How Cole uses it

Three patterns recur. First, **Slack as the alerting destination** in [agentic workflow engineering](../../concepts/agentic-workflow-engineering.md). In the n8n tips video he wires an error branch to Slack: "send a slack message with the error details so that you know to go and handle whatever went wrong within your workflow," and elsewhere has workflows summarize findings or a conversation and post the result. Sending a Slack message is the canonical "now do something in the real world" [tool call](../../concepts/tool-use.md) at the end of a flow.

Second, **Slack as the way to talk to and supervise agents**, a [human-in-the-loop](../../concepts/human-in-the-loop.md) surface. Cole highlights that at Stripe "they use Slack as the way to talk to their minions pretty often," and in his own subagents run he keeps humans informed the same way: "We're providing updates in Slack ... I just have it message me after the first and second sessions." The Vercel demo goes further, putting approval controls in the message itself, "we have the integration right in Slack where we have the buttons that are open here. So I will click allow, and then it'll run the query." His second brain, backed by [memory systems](../../concepts/memory-systems.md) and [RAG](../../concepts/rag.md), lives in Slack for exactly this reason.

Third, **Slack as a stock connector to set up.** He repeatedly walks through the auth: Docker's one-click MCP install still needs you to "create a Slack app and hook in the bot token here," and n8n's Slack credentials are "a little bit trickier ... you actually want to go to ooth and permissions." However it is wired, Slack is the reliable output/notification channel of these builds. Cole notes the same slot could be filled by [Telegram](./telegram.md).

## Realizes

- [Chat Interfaces](../../concepts/chat-interfaces.md) - Wrapping agents in chat surfaces (websites, DMs, platforms) with adapters, a shared message format, and durable history.

## Works with

- [n8n](./n8n.md) - A no-code AI automation platform for building agents and workflows that integrate with 500+ applications.
- [Docker](./docker.md) - Containerization prerequisite; a single docker compose command spins up Archon's four containers (agents, MCP server, UI, API server).
- [Zapier](./zapier.md) - Automation platform whose MCP server connects agents to 8,000+ apps (video sponsor).
- [Confluence](./confluence.md) - Atlassian's team documentation wiki, connected via API key as the ingested knowledge-base source that grounds a RAG assistant's answers.

## Contrasts with

- [Telegram](./telegram.md) - The messaging app Cole integrates Codex into via the Telegraf library, letting him trigger remote coding jobs from his phone.

## Related

- [Human in the Loop](../../concepts/human-in-the-loop.md) - Keeping a human as the approver and steerer of agentic work rather than fully automating, so AI augments engineers instead of replacing them.
- [Agentic Workflow Engineering](../../concepts/agentic-workflow-engineering.md) - Designing repeatable AI workflows as engineered systems with defined steps, orchestration, and background execution rather than ad-hoc prompting.
- [Tool Calling](../../concepts/tool-use.md) - Letting an LLM invoke external functions and APIs so it can take actions and fetch data beyond its parametric knowledge.
- [Memory Systems](../../concepts/memory-systems.md) - Giving agents durable short- and long-term memory so conversations, user context, and facts persist across sessions and users.
- [Retrieval-Augmented Generation (RAG)](../../concepts/rag.md) - Grounding an LLM's answers by retrieving relevant documents from an external knowledge base and injecting them into the prompt at query time.

## Sources

- [I Built a Safer OpenClaw Alternative Using Claude Code](../../sources/i-built-a-safer-openclaw-alternative-using-claude-code.md) - "[0:11:34] I really like talking to my second brain in Slack ... I can talk to it in Slack from anywhere. It's super cool. And that's really all I need."
- [Stripe's Coding Agents Ship 1,300 PRs EVERY Week - Here's How They Do It](../../sources/stripes-coding-agents-ship-1300-prs-every-week-heres-how-they-do-it.md) - "[0:02:44] in Stripe, they use Slack as the way to talk to their minions pretty often."
- [This Completely Changes the Way We Build Production AI Agents (Vercel Eve)](../../sources/this-completely-changes-the-way-we-build-production-ai-agents-vercel-eve.md) - "[0:14:34] we have the integration right in Slack where we have the buttons that are open here. So I will click allow, and then it'll run the query."
- [Turn Claude Code into Your Full Engineering Team with Subagents](../../sources/turn-claude-code-into-your-full-engineering-team-with-subagents.md) - "[0:04:48] We're providing updates in Slack ... I just have it message me after the first and second sessions."
- [10 n8n Tips in 10 Minutes to 10x Your AI Automations](../../sources/10-n8n-tips-in-10-minutes-to-10x-your-ai-automations.md) - "[0:08:25] send a slack message with the error details so that you know to go and handle whatever went wrong within your workflow"
- [Docker Just Made Using MCP Servers 100x Easier (One Click Installs!)](../../sources/docker-just-made-using-mcp-servers-100x-easier-one-click-installs.md) - "[0:09:00] you just have to create a Slack app and hook in the bot token here."
- [Don't Sleep on the ULTIMATE AI Agent Combo (n8n, LangChain, Python)](../../sources/dont-sleep-on-the-ultimate-ai-agent-combo-n8n-langchain-python.md) - "[0:06:43] setting up the slack credentials is a little bit trickier in n8n ... you actually want to go to ooth and permissions"
- [Flowise + n8n - The BEST No Code + Local AI Agent Combo](../../sources/flowise-n8n-the-best-no-code-local-ai-agent-combo.md) - "[0:27:50] let's have it send a slack message with this link and the summary of its findings"
- [The KING of No Code AI Agent Builders?!](../../sources/the-king-of-no-code-ai-agent-builders.md) - "[0:14:30] if we go into my slack Channel there we go it sent test message so everything is working good for the connection"
- [This Slack AI Personal Assistant is Better than a Real Person](../../sources/this-slack-ai-personal-assistant-is-better-than-a-real-person.md) - "[0:08:02] I want to do is invite run bear into this channel"
