---
type: source
title: "This Slack AI Personal Assistant is Better than a Real Person"
description: "Building an AI personal assistant inside a chat platform like Slack is a classic, high-value use case that no longer needs to be built from scratch. A no-code platform like RunBear delivers RAG, web search, tool calling, and conversation summarization out of the box."
youtube_id: oMwipO6cmPQ
url: https://www.youtube.com/watch?v=oMwipO6cmPQ
slug: this-slack-ai-personal-assistant-is-better-than-a-real-person
published: 2024-10-04
duration: "0:12:24"
recency_rank: 157
raw: "../raw/this-slack-ai-personal-assistant-is-better-than-a-real-person.md"
tags: [no-code, slack, rag, chat-assistant]
created: 2026-07-21
updated: 2026-07-21
---

# This Slack AI Personal Assistant is Better than a Real Person

Cole frames the Slack AI assistant as one of the most classic and enduring AI use cases: a bot living in a team's chat platform that can answer FAQs, search a knowledge base, and boost productivity. He notes that three years earlier people doubted whether this kind of RAG-powered FAQ assistant was even possible, yet it is now a standard business use case that almost anyone would benefit from. Rather than build it himself, he argues against reinventing the wheel and demos RunBear, a no-code platform that spins up chat assistants for Slack (and Discord or Teams).

The walkthrough covers RunBear's two core tabs, Integrations (connecting Slack plus a knowledge base via Confluence, Google Drive, or Notion) and Assistants (creating the bot with a name, behavioral instructions, model choice, and an external knowledge source). He highlights baked-in actions (image interpretation/generation, current date, web search, URL fetching/scraping, Slack conversation search) and the ability to add fully custom functions using OpenAI's function-calling JSON spec. A key extensibility point: you can plug in your own LangChain/LangServe agent through RunBear's Python SDK instead of just a base model.

In Slack he demonstrates three tools live: a RAG question answered from an ingested Confluence document, a web-search follow-up that pulls real pricing for tools like Groq, Pinecone, and Supabase, and a summarize-conversation action that condenses a busy channel into a concise digest. He points out that each Slack thread acts as its own separate chat memory (analogous to a ChatGPT conversation), and that the assistant carries conversation history across turns. The through-line: even a technical builder should lean on a robust platform for a classic use case because there is real work in wiring up all the tools and integrations reliably.

## Concepts covered

- [Chat Interfaces](../concepts/chat-interfaces.md)
- [Retrieval-Augmented Generation (RAG)](../concepts/rag.md)
- [Buy vs. Build](../concepts/buy-vs-build.md)
- [Knowledge Bases](../concepts/knowledge-bases.md)
- [Tool Calling](../concepts/tool-use.md)
- [Context Window Limits](../concepts/context-window-limits.md)
- [Memory Systems](../concepts/memory-systems.md)

## Entities

- [Slack](../entities/tools/slack.md)
- [Google Drive](../entities/tools/google-drive.md)
- [LangChain](../entities/tools/langchain.md)
- [OpenAI](../entities/organizations/openai.md)
- [Cole Medin](../entities/people/cole-medin.md)

## Key moments

- **[0:00:29]** Cole recalls a Slack community wanting an AI FAQ assistant years ago, now a classic RAG use case
- **[0:01:04]** Argues against reinventing the wheel; introduces RunBear as an easy platform
- **[0:02:46]** Tour of the RunBear dashboard: Integrations and Assistants tabs
- **[0:03:13]** Knowledge base options: Confluence, Google Drive, Notion
- **[0:04:08]** Extensibility: plug in a custom LangChain/LangServe agent via Python SDK, not just a base model
- **[0:05:38]** Built-in actions: image gen, current date, web search, URL fetch, Slack search
- **[0:06:22]** Add custom functions using OpenAI function-calling spec
- **[0:07:36]** Trigger configuration: respond only on mention, keyword, or emoji
- **[0:08:30]** Live RAG demo answering from the Confluence document
- **[0:09:04]** Live web-search demo pulling real pricing for Groq, Pinecone, Supabase
- **[0:10:32]** Live conversation-summarization demo, then 'make it more concise'

## Transcript

[Raw transcript](../raw/this-slack-ai-personal-assistant-is-better-than-a-real-person.md)
