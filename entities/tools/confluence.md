---
type: entity
subtype: tool
title: "Confluence"
description: "Atlassian's team documentation wiki, connected via API key as the ingested knowledge-base source that grounds a RAG assistant's answers."
resource: "https://www.atlassian.com/software/confluence"
tags: [integration, productivity, rag]
videos: [this-slack-ai-personal-assistant-is-better-than-a-real-person]
created: 2026-07-21
updated: 2026-07-21
---

# Confluence

Confluence is Atlassian's team documentation wiki, the place where a company's runbooks, specs, onboarding guides, and policies already live. In Cole's Slack assistant build it is not a feature of the demo so much as the *substrate* of it: the [knowledge base](../../concepts/knowledge-bases.md) the assistant retrieves from. RunBear offers three connectors for this role (Confluence, [Google Drive](./google-drive.md), and Notion), and the setup is deliberately unglamorous: "for confluence there's even documentation that gives you on how to create an API key put it in here to get that connection set up" [0:03:28].

That mundanity is the point. Cole demos the assistant answering a live question in Slack straight out of an ingested Confluence page [0:08:30], and the reason the answer is good has little to do with the retrieval algorithm. A documentation wiki is the highest-value [RAG](../../concepts/rag.md) corpus available to most teams because it is already curated, already deduplicated, and already maintained by humans who are accountable for it. The hard part of a company FAQ bot was never the vector search; it was getting a durable, permissioned pipe to the system of record, which an API key and a connector solve.

Confluence therefore anchors his [buy vs. build](../../concepts/buy-vs-build.md) argument. He notes that three years earlier people doubted a RAG-powered FAQ assistant was even possible, and now it is a standard business use case, which means the differentiated work has moved elsewhere and a technical builder should lean on a platform rather than rewire Confluence auth by hand. Inside the Atlassian pair, Confluence is also the natural counterpart to [Jira](./jira.md): Jira supplies the scoped ticket that says what to do, Confluence supplies the written context that says how this system actually works, which is the same split that makes [docs as agent context](../../concepts/docs-as-agent-context.md) work for coding agents.

## Realizes

- [Knowledge Bases](../../concepts/knowledge-bases.md) - Curated bodies of knowledge an agent can retrieve from, distinct from raw model weights, that ground responses in trusted source material.
- [Retrieval-Augmented Generation (RAG)](../../concepts/rag.md) - Grounding an LLM's answers by retrieving relevant documents from an external knowledge base and injecting them into the prompt at query time.

## Works with

- [Slack](./slack.md) - The chat surface where the assistant lives and answers from the ingested Confluence content.
- [Jira](./jira.md) - Atlassian's issue tracker whose scoped tickets pair with Confluence's written context.
- [Google Drive](./google-drive.md) - Alternative knowledge-base connector for the same assistant, used elsewhere as a RAG ingestion source.
- [n8n](./n8n.md) - No-code automation platform used elsewhere to build the same kind of ingestion pipeline yourself.

## Related

- [Buy vs. Build](../../concepts/buy-vs-build.md) - For a classic, well-solved use case, leaning on a robust existing platform beats building it yourself.
- [Chat Interfaces](../../concepts/chat-interfaces.md) - Wrapping agents in chat surfaces (websites, DMs, platforms) with adapters, a shared message format, and durable history.
- [Agentic RAG](../../concepts/agentic-rag.md) - Giving an agent retrieval as a tool so it decides when and how to search a knowledge base instead of doing a single static lookup.
- [Docs and Templates as Coding-Assistant Context](../../concepts/docs-as-agent-context.md) - Feeding real docs and proven reference templates to an assistant so it builds from context instead of hallucinating.
- [Memory Systems](../../concepts/memory-systems.md) - Giving agents durable short- and long-term memory so conversations and context persist across sessions.

## Sources

- [This Slack AI Personal Assistant is Better than a Real Person](../../sources/this-slack-ai-personal-assistant-is-better-than-a-real-person.md) - "[0:03:28] for confluence there's even documentation that gives you on how to create an API key put it in here to get that connection set up"
