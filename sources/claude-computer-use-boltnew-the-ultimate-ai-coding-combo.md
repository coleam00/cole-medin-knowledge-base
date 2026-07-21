---
type: source
title: "Claude Computer Use + Bolt.new - The ULTIMATE AI Coding Combo?!"
description: "AI coding assistants fail on new or niche libraries because they lack external knowledge, and Claude's computer use API can bridge that gap by autonomously researching documentation and injecting it into a tool like Bolt.new before the build."
youtube_id: R6AYmqcOXaw
url: https://www.youtube.com/watch?v=R6AYmqcOXaw
slug: claude-computer-use-boltnew-the-ultimate-ai-coding-combo
published: 2024-11-24
duration: "0:10:31"
recency_rank: 139
raw: "../raw/claude-computer-use-boltnew-the-ultimate-ai-coding-combo.md"
tags: [computer-use, bolt-new, rag, ai-coding]
created: 2026-07-21
updated: 2026-07-21
---

# Claude Computer Use + Bolt.new - The ULTIMATE AI Coding Combo?!

Cole demonstrates a core limitation of browser and IDE AI coding assistants ([bolt.new](../entities/tools/bolt-new.md), [Cursor](../entities/tools/cursor.md), [Windsurf](../entities/tools/windsurf.md), Autodev): they have no external knowledge of newer or smaller libraries, so they botch any app built around documentation the underlying LLM never saw. This is a concrete case of [when RAG is (and is not) dead](../concepts/when-rag-is-dead.md). He proves the point by having Bolt build a frontend around the relatively new n8n Demo widget library, which Claude 3.5 Sonnet inside Bolt fails completely, even failing to install dependencies and self-fix.

He frames the fix as "[RAG](../concepts/rag.md) for an AI coding assistant": fetch the library's install and usage docs from the web and augment the coding prompt with that context, an [agentic RAG](../concepts/agentic-rag.md) and [self-reflective RAG](../concepts/self-reflective-rag.md) loop where the assistant researches to help itself. To achieve this today, he uses the [Anthropic](../entities/organizations/anthropic.md) [computer use](../concepts/computer-use.md) API, which lets Claude control a computer (a sandboxed virtual machine spun up via the Anthropic reference [Docker](../entities/tools/docker.md) implementation, an example of [context isolation](../concepts/context-isolation.md)) to type, click, and browse. With a bit of [handholding](../concepts/human-in-the-loop.md) (pointing Claude at the docs URL and supplying the workflow JSON), Claude researches the n8n Demo component, crafts a docs-augmented prompt, and drives Bolt to build the app hands-off.

The result works after one small correction (Claude initially included only one of the needed script tags): the app is deployed to [Netlify](../entities/tools/netlify.md) (iframes are blocked inside Bolt's web container) and the n8n workflow preview widget renders correctly. Cole positions this as an experimental glimpse of a near future where AI researches to assist itself, either through computer use or via direct doc-fetching integrations built into coding assistants, aided by documentation authored specifically for AI to scrape. It is another marker in [the evolution of AI coding](../concepts/the-evolution-of-ai-coding.md).

## Concepts covered

- [When RAG Is (and Isn't) Dead](../concepts/when-rag-is-dead.md)
- [Retrieval-Augmented Generation (RAG)](../concepts/rag.md)
- [Agentic RAG](../concepts/agentic-rag.md)
- [Computer Use](../concepts/computer-use.md)
- [Context Isolation](../concepts/context-isolation.md)
- [Human in the Loop](../concepts/human-in-the-loop.md)
- [Self-Reflective RAG](../concepts/self-reflective-rag.md)
- [The Evolution of AI Coding](../concepts/the-evolution-of-ai-coding.md)

## Entities

- [Cole Medin](../entities/people/cole-medin.md)
- [Claude Code](../entities/tools/claude-code.md)
- [Anthropic](../entities/organizations/anthropic.md)
- [bolt.new](../entities/tools/bolt-new.md)
- [Cursor](../entities/tools/cursor.md)
- [Windsurf](../entities/tools/windsurf.md)
- [Docker](../entities/tools/docker.md)
- [Netlify](../entities/tools/netlify.md)
- [Streamlit](../entities/tools/streamlit.md)

## Key moments

- **[0:00:29]** States the core flaw: AI coding assistants lack external knowledge like library documentation
- **[0:00:56]** Sets up a guaranteed-failure demo using the new/small n8n Demo library
- **[0:02:03]** Bolt completely fails to build the app, even failing dependency install and self-fix
- **[0:02:35]** Frames the solution as "RAG for an AI coding assistant"
- **[0:03:36]** Introduces the Claude computer use API as the mechanism
- **[0:04:04]** Shows Anthropic's reference implementation running via Docker in a sandboxed VM
- **[0:05:11]** Prompts Claude to research the n8n Demo component and inject findings into a Bolt prompt
- **[0:07:20]** Claude messes up research slightly (missing script tags); Cole hand-corrects
- **[0:08:09]** Deploys to Netlify to work around iframe blocking in the web container
- **[0:08:24]** Final app renders the n8n workflow preview widget successfully

## Transcript

[Raw transcript](../raw/claude-computer-use-boltnew-the-ultimate-ai-coding-combo.md)
