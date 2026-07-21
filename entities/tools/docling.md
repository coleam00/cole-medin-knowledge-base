---
type: entity
subtype: tool
title: "Docling"
description: "The open-source Python data-extraction/chunking tool that is the subject of the video summarized and integrated into Archon during the workflow demo."
resource: "https://github.com/docling-project/docling"
tags: [rag, chunking, data-extraction, open-source]
videos: [the-simplest-rag-stack-that-actually-works-complete-guide, the-only-ai-tech-stack-you-need-in-2026, every-rag-strategy-explained-in-13-minutes-no-fluff, super-special-livestream-this-weekend-live-ai-agent-build, should-i-build-my-ai-agents-with-n8n-or-python, docker-just-made-using-mcp-servers-100x-easier-one-click-installs, turn-any-file-into-llm-knowledge-in-seconds]
created: 2026-07-21
updated: 2026-07-21
---

# Docling

Docling is the open-source Python library Cole reaches for whenever the [RAG](../../concepts/rag.md) source is a file rather than a website. As he describes it, "Dockling makes it really easy to extract text from PDFs, Word documents, markdown documents, even audio files" ([0:03:34]). It is "a free and open-source tool... to work with all these complex data types so you can properly curate your data no matter how complex it is" ([0:01:10]), and it pairs directly with [Crawl4AI](./crawl4ai.md) in his stack under a simple rule: "If you are working with files, use dockling. If you are working with websites, use crawl for AAI" ([0:13:06]).

## How Cole uses it

Docling's value is that it collapses two hard problems, extraction and [chunking](../../concepts/chunking.md), into a few lines of code. On the extraction side it is format-aware: "under the hood, it recognizes the file extension and it knows what to do to work with those different file types without us having to do that much more in our code" ([0:06:19]), which makes it "helpful to have something out of the box like dockling" for "more complex documents specifically like PDFs with diagrams Excel files" ([0:12:12]).

The feature Cole most consistently praises is its hybrid chunking. "chunking is not an easy problem to solve, but we're able to do this very easily just using what Dockling has for us out of the box" ([0:04:30]). He treats hybrid chunking as a form of [context-aware chunking](../../concepts/context-aware-chunking.md): "dockling is a library that I use in Python that makes it very easy to implement hybrid chunking, which is a form of contextaware chunking" ([0:08:09]), and it is "especially useful for the hybrid chunking that they have available" ([0:03:48]). Cleanly chunked text is what makes downstream [vector embeddings](../../concepts/vector-embeddings.md) retrieve well.

Docling sits alongside the rest of Cole's data tooling, "graffiti for knowledge graphs, dockling for rag" ([0:13:13]), and he has demonstrated integrating it into [Archon](./archon.md) during a workflow build. Because it runs entirely in Python without a hosted service, it fits his [local AI](../../concepts/local-ai.md) preference: "a tool to help with data extraction and chunking for rag" ([0:05:25]) that you own end to end.

## Related

- [RAG](../../concepts/rag.md) and [Agentic RAG](../../concepts/agentic-rag.md) - Docling prepares the documents these pipelines retrieve over.
- [Chunking](../../concepts/chunking.md) and [Context-Aware Chunking](../../concepts/context-aware-chunking.md) - its hybrid chunking is the headline feature.
- [Vector Embeddings](../../concepts/vector-embeddings.md) - cleanly chunked output embeds and retrieves better.
- [Local & Self-Hosted AI](../../concepts/local-ai.md) - a pure-Python library you run yourself.
- Sibling tools: [Crawl4AI](./crawl4ai.md) (the website-side counterpart), [Chroma](./chroma.md), [Graphiti](./graphiti.md), [Archon](./archon.md).

## Sources

- [Turn ANY File into LLM Knowledge in SECONDS](../../sources/turn-any-file-into-llm-knowledge-in-seconds.md) - "[0:01:10] It is a free and open-source tool I'm going to show you how to use today to work with all these complex data types so you can properly curate your data no matter how complex it is."
- [The Simplest RAG Stack That Actually Works (Complete Guide)](../../sources/the-simplest-rag-stack-that-actually-works-complete-guide.md) - "[0:04:30] chunking is not an easy problem to solve, but we're able to do this very easily just using what Dockling has for us out of the box."
- [Every RAG Strategy Explained in 13 Minutes (No Fluff)](../../sources/every-rag-strategy-explained-in-13-minutes-no-fluff.md) - "[0:08:09] dockling is a library that I use in Python that makes it very easy to implement hybrid chunking, which is a form of contextaware chunking."
- [The ONLY AI Tech Stack You Need in 2026](../../sources/the-only-ai-tech-stack-you-need-in-2026.md) - "[0:13:06] If you are working with files, use dockling. If you are working with websites, use crawl for AAI."
- [Turn ANY File into LLM Knowledge in SECONDS](../../sources/turn-any-file-into-llm-knowledge-in-seconds.md) - "[0:06:19] under the hood, it recognizes the file extension and it knows what to do to work with those different file types without us having to do that much more in our code."
- [Super Special Livestream this Weekend! (LIVE AI Agent Build)](../../sources/super-special-livestream-this-weekend-live-ai-agent-build.md) - "[0:03:48] a tool for rag called Dockling. And this is especially useful for the hybrid chunking that they have available."
- [Docker Just Made Using MCP Servers 100x Easier (One Click Installs!)](../../sources/docker-just-made-using-mcp-servers-100x-easier-one-click-installs.md) - "[0:05:25] one of the latest videos on my channel where I cover Dockling, which is a tool to help with data extraction and chunking for rag."
- [Should I Build My AI Agents with n8n or Python?](../../sources/should-i-build-my-ai-agents-with-n8n-or-python.md) - "[0:13:13] graffiti for knowledge graphs, dockling for rag. We have crawl for AI for crawling websites."
