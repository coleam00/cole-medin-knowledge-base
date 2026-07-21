---
type: concept
title: "Knowledge Bases"
description: "Curated bodies of knowledge an agent can retrieve from, distinct from raw model weights, that ground responses in trusted source material."
tags: [knowledge, rag, curation]
videos: [this-completely-changes-the-way-we-build-production-ai-agents-vercel-eve, finally-an-open-standard-for-the-karpathy-llm-wiki-is-here, why-the-best-ai-coding-tools-abandoned-rag-and-what-they-use-instead, the-official-archon-guide-10x-your-ai-coding-workflow, turn-any-file-into-llm-knowledge-in-seconds, your-ultimate-n8n-rag-ai-agent-template-just-got-a-massive-upgrade, i-built-my-claude-code-subagents-dream-team-to-create-any-ai-agent, archon-beta-launch-livestream-what-you-missed, introducing-archon-the-revolutionary-operating-system-for-ai-coding, all-the-best-rag-strategies-in-one-mcp-for-ai-coding-assistants, the-3-must-have-mcp-servers-for-any-ai-coding-and-how-to-use-them, i-built-the-ultimate-rag-mcp-server-for-ai-coding-better-than-context7, turn-any-website-into-llm-knowledge-in-seconds-evolved, build-ai-agents-that-evolve-over-time, i-built-the-ultimate-n8n-rag-ai-agent-template, n8n-crawl4ai-scrape-any-website-in-minutes-with-no-code, the-future-of-rag-is-agentic-learn-this-strategy-now, turn-any-website-into-llm-knowledge-in-seconds, turn-any-ai-agent-into-a-live-person-voice-chat-setup-in-minutes, get-qualified-leads-while-you-sleep-with-ai, effortless-rag-in-n8n-use-all-your-files-pdfs-excel-and-more, this-slack-ai-personal-assistant-is-better-than-a-real-person, i-built-a-full-rag-ai-agent-with-no-code-in-4-minutes-with-vectorshift, run-all-your-ai-locally-in-minutes-llms-rag-and-more, this-rag-ai-agent-with-n8n-supabase-is-the-real-deal, no-code-rag-agents-you-have-to-check-out-n8n-langchain, build-a-chatbot-for-your-website-in-4-minutes-no-code, the-most-value-packed-rag-guide-on-youtube-feat-llama-31-405b]
created: 2026-07-21
updated: 2026-07-21
---

# Knowledge Bases

A knowledge base is a curated, private store of source material an agent retrieves from at query time, separate from the model's frozen weights. It exists because "one of the biggest challenges we face with large language models right now is their knowledge is too General and it's very limited for new things because of its training cut off" - ["Turn ANY Website into LLM Knowledge in SECONDS"](../sources/turn-any-website-into-llm-knowledge-in-seconds.md) [0:00:00]. Ground the model in the right corpus and the gap closes: "if I take all of the framework documentation for pantic AI and put it in a knowledge base for the llm... the answer that I get is spot on" [0:00:17]. Crucially it is a distinct architectural layer, not part of the agent: "the knowledge base is a separate thing." - ["This Completely Changes the Way We Build Production AI Agents (Vercel Eve)"](../sources/this-completely-changes-the-way-we-build-production-ai-agents-vercel-eve.md) [0:06:25].

## Why curation is the hard part

The value of a knowledge base is set upstream, at ingestion, long before any search runs. "the data curation step is the most important part of Rag because it sets the foundation for everything" - ["Turn ANY File into LLM Knowledge in SECONDS"](../sources/turn-any-file-into-llm-knowledge-in-seconds.md) [0:01:52]. Curation and search are co-dependent: "If you're not very strategic about how you are chunking and curating the knowledge for your knowledge base, it doesn't matter how effective your agentic search strategies are, your agent will fall apart." - ["Your ULTIMATE n8n RAG AI Agent Template just got a Massive Upgrade"](../sources/your-ultimate-n8n-rag-ai-agent-template-just-got-a-massive-upgrade.md) [0:01:52]. Ingestion is format-aware, since "the way that you take content from a PDF or a spreadsheet or a Google doc those are all different" - ["I Built the ULTIMATE n8n RAG AI Agent Template"](../sources/i-built-the-ultimate-n8n-rag-ai-agent-template.md) [0:20:16], and it must stay clean: "you don't want different versions of your file existing at the same time in your knowledge base that will confuse the heck out of your llm" - ["Run ALL Your AI Locally in Minutes"](../sources/run-all-your-ai-locally-in-minutes-llms-rag-and-more.md) [0:15:36].

## Private and owned

The recurring theme is ownership: a knowledge base you control, scoped to your stack. [Archon](../entities/tools/archon.md) is Cole's canonical build here: "this is your own private knowledge base. You get to manage the strategies for Rag and the way that we're extracting code examples" - ["Introducing Archon - The Revolutionary Operating System for AI Coding"](../sources/introducing-archon-the-revolutionary-operating-system-for-ai-coding.md) [0:06:05]. Sources range from crawled sites and sitemaps to uploaded documents, and once ingested a coding assistant reaches them over [MCP](./mcp.md): "our coding assistant through MCP will immediately be able to search through everything that we brought into our own private knowledge base." - ["The OFFICIAL Archon Guide"](../sources/the-official-archon-guide-10x-your-ai-coding-workflow.md) [0:16:34].

## Builds on

- [Retrieval-Augmented Generation (RAG)](./rag.md) - the retrieval pattern a knowledge base feeds.
- [Chunking](./chunking.md) - how documents are split before they enter the base.
- [Vector Embeddings](./vector-embeddings.md) - the representation that makes semantic lookup possible.

## Contrasts with

- [The LLM Wiki](./the-llm-wiki.md) - the smarter, LLM-built alternative to dumping documents: "Instead of just dumping in a bunch of documents or indexing things for rag, we can have the LLM help us build something smarter." - ["Finally, an Open Standard for the Karpathy LLM Wiki is HERE"](../sources/finally-an-open-standard-for-the-karpathy-llm-wiki-is-here.md) [0:00:33]. Cole notes plain vector knowledge bases "don't necessarily scale, especially once you get to tens of thousands of documents" - [Vercel Eve](../sources/this-completely-changes-the-way-we-build-production-ai-agents-vercel-eve.md) [0:06:25].

## Related

- [Agentic RAG](./agentic-rag.md) - letting the agent reason about which knowledge store to query.
- [Knowledge Graphs](./knowledge-graphs.md) - a relational representation layered onto or beside a knowledge base.
- [Structured vs Unstructured Data](./structured-vs-unstructured-data.md) - the data-shape distinction that drives ingestion strategy.
- [Memory Systems](./memory-systems.md) - a user-specific knowledge base is effectively long-term memory.
- [Context Engineering](./context-engineering.md) - deciding what retrieved knowledge actually enters the prompt.
- [Agent Protocols](./agent-protocols.md) - OKF standardizes agent-to-knowledge-base communication the way MCP did agent-to-tool: "It's like what MCP did for agent-to-tool communication, this OKF is doing for agent to knowledgebased communication." - [Finally, an Open Standard](../sources/finally-an-open-standard-for-the-karpathy-llm-wiki-is-here.md) [0:09:36].
- [Chat Interfaces](./chat-interfaces.md) / [Embeddable Agent Widget](./embeddable-agent-widget.md) - front ends that surface a grounded knowledge base to users.

## Tools

- [Archon](../entities/tools/archon.md) - private, self-managed knowledge base for AI coding assistants.
- [Crawl4AI](../entities/tools/crawl4ai.md) / [Crawl4AI RAG MCP Server](../entities/tools/crawl4ai-rag-mcp.md) - crawl any website into a knowledge base.
- [Supabase](../entities/tools/supabase.md) - the private Postgres store behind many of these builds.
- [n8n](../entities/tools/n8n.md) - no-code ingestion workflows into a knowledge base.
- [Google Drive](../entities/tools/google-drive.md) - a common document source polled for new files.
- [Vector Shift](../entities/tools/vector-shift.md) - no-code knowledge-base ingestion.
- [Context7](../entities/tools/context7.md) - an out-of-the-box docs option contrasted with a private base.

## Sources

- [Turn ANY Website into LLM Knowledge in SECONDS](../sources/turn-any-website-into-llm-knowledge-in-seconds.md) - "[0:00:17] if I take all of the framework documentation for pantic AI and put it in a knowledge base for the llm and I ask it the exact same question the answer that I get is spot on"
- [This Completely Changes the Way We Build Production AI Agents (Vercel Eve)](../sources/this-completely-changes-the-way-we-build-production-ai-agents-vercel-eve.md) - "[0:06:25] I've said in the past that they don't necessarily scale, especially once you get to tens of thousands of documents. And so, yeah, the knowledge base is a separate thing."
- [Turn ANY File into LLM Knowledge in SECONDS](../sources/turn-any-file-into-llm-knowledge-in-seconds.md) - "[0:01:52] the data curation step is the most important part of Rag because it sets the foundation for everything"
- [Your ULTIMATE n8n RAG AI Agent Template just got a Massive Upgrade](../sources/your-ultimate-n8n-rag-ai-agent-template-just-got-a-massive-upgrade.md) - "[0:01:52] If you're not very strategic about how you are chunking and curating the knowledge for your knowledge base, it doesn't matter how effective your agentic search strategies are, your agent will fall apart."
- [Introducing Archon - The Revolutionary Operating System for AI Coding](../sources/introducing-archon-the-revolutionary-operating-system-for-ai-coding.md) - "[0:06:05] that's one of the things that makes Archon better than something like Context 7 because this is your own private knowledge base. You get to manage the strategies for Rag"
- [The OFFICIAL Archon Guide - 10x Your AI Coding Workflow](../sources/the-official-archon-guide-10x-your-ai-coding-workflow.md) - "[0:16:34] once this crawling is complete, our coding assistant through MCP will immediately be able to search through everything that we brought into our own private knowledge base."
- [Finally, an Open Standard for the Karpathy LLM Wiki is HERE](../sources/finally-an-open-standard-for-the-karpathy-llm-wiki-is-here.md) - "[0:09:36] It's like what MCP did for agent-to-tool communication, this OKF is doing for agent to knowledgebased communication."
- [Why the Best AI Coding Tools Abandoned RAG (And What They Use Instead)](../sources/why-the-best-ai-coding-tools-abandoned-rag-and-what-they-use-instead.md) - "[0:02:29] When we have massive knowledge bases of unstructured data, we need some way to find these synonyms and similar concepts that can be buried across thousands or even millions of documents."
- [I Built the ULTIMATE n8n RAG AI Agent Template](../sources/i-built-the-ultimate-n8n-rag-ai-agent-template.md) - "[0:20:16] based on the type of file there needs to be a different way for us to extract the content from it because the way that you take content from a PDF or a spreadsheet or a Google doc those are all different"
- [Run ALL Your AI Locally in Minutes (LLMs, RAG, and more)](../sources/run-all-your-ai-locally-in-minutes-llms-rag-and-more.md) - "[0:15:36] you don't want different versions of your file existing at the same time in your knowledge base that will confuse the heck out of your llm"
