---
type: entity
subtype: tool
title: "Telegram"
description: "The messaging app Cole integrates Codex into via the Telegraf library, letting him trigger remote coding jobs from his phone."
resource: "https://telegram.org"
tags: [messaging, chat, integration, remote-access]
videos: [claude-code-web-just-dropped-but-i-already-built-something-better-with-codex, claude-codes-real-purpose-its-bigger-than-you-think]
created: 2026-07-21
updated: 2026-07-21
---

# Telegram

Telegram is a cross-platform messaging app, and in Cole's videos it becomes the phone-friendly remote control for a coding agent. Instead of sitting at a terminal, he wires a coding assistant into a Telegram bot so he can kick off and steer jobs from anywhere: "I have integrated OpenAI's codeex as the coding assistant directly into Telegram." The chat thread is the whole interface, messages in become coding tasks, and the agent's replies come back as messages. On the implementation side it is deliberately ordinary plumbing: "we're using the Telegraph [Telegraf] library in Typescript for our Telegram integration."

## How Cole uses it

The headline build is a **Telegram-driven remote [coding harness](../../concepts/ai-coding-harness.md)**, positioned as a homegrown answer to Claude Code's web/mobile experience. Cole runs [Codex](./codex.md) in a container and fronts it with a Telegram bot, so he can trigger [agentic coding](../../concepts/agentic-coding.md) runs from his phone, review progress, and reply with follow-ups, the mobile equivalent of leaving an agent working while he steps away. Because the agent's state and repo access live server-side, Telegram is purely the thin, always-with-you [chat interface](../../concepts/chat-interfaces.md) and a lightweight [observability](../../concepts/agent-observability.md) window into what the run is doing.

The deeper point Cole makes is that the messaging surface is **interchangeable by design**: "I want to show you how easy it is to build cla code into any application we want. Like I'm picking Telegram here, but this could be Slack, it could be GitHub, it could be email, whatever you want." That is a [provider-independence](../../concepts/provider-independence.md) argument applied to the front end, once the agent is reachable over a simple API, the choice of Telegram versus [Slack](./slack.md) or email is a preference, not an architecture. It is the same "meet me where I already am" instinct behind his [second brain](../../concepts/second-brain.md), and the kind of small integration that lets a personal system keep [evolving](../../concepts/system-evolution.md) toward however the builder actually works.

## Related

- [AI Coding Harness](../../concepts/ai-coding-harness.md) - Telegram fronts a remote coding harness
- [Agentic Coding](../../concepts/agentic-coding.md) - jobs triggered from the phone
- [Chat Interfaces](../../concepts/chat-interfaces.md) - the message thread is the whole UI
- [Provider Independence](../../concepts/provider-independence.md) - the messaging surface is swappable
- [Agent Observability](../../concepts/agent-observability.md) - watching a run over chat
- [Second Brain](../../concepts/second-brain.md)
- [System Evolution](../../concepts/system-evolution.md)
- [Codex](./codex.md) - the coding assistant wired into the bot
- [Slack](./slack.md) - the interchangeable messaging surface

## Sources

- [Claude Code Web JUST Dropped but I Already Built Something BETTER (with Codex!)](../../sources/claude-code-web-just-dropped-but-i-already-built-something-better-with-codex.md) - "[0:01:05] I have integrated OpenAI's codeex as the coding assistant directly into Telegram"
- [Claude Code's Real Purpose (It's Bigger Than You Think)](../../sources/claude-codes-real-purpose-its-bigger-than-you-think.md) - "[0:14:55] I'm picking Telegram here, but this could be Slack, it could be GitHub, it could be email, whatever you want."
