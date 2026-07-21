---
type: concept
title: "Chunking"
description: "Splitting source documents into appropriately sized, embeddable segments, the foundational preprocessing step that determines RAG retrieval quality."
tags: [rag, chunking, embeddings, preprocessing]
videos: [why-the-best-ai-coding-tools-abandoned-rag-and-what-they-use-instead, the-simplest-rag-stack-that-actually-works-complete-guide, every-rag-strategy-explained-in-13-minutes-no-fluff, super-special-livestream-this-weekend-live-ai-agent-build, turn-any-file-into-llm-knowledge-in-seconds, knowledge-graphs-in-n8n-are-finally-here, your-ultimate-n8n-rag-ai-agent-template-just-got-a-massive-upgrade, introducing-rag-20-agentic-rag-knowledge-graphs-free-template, all-the-best-rag-strategies-in-one-mcp-for-ai-coding-assistants, the-easiest-possible-strategy-for-accurate-rag-step-by-step-guide, i-built-the-ultimate-rag-mcp-server-for-ai-coding-better-than-context7, turn-any-website-into-llm-knowledge-in-seconds-evolved, this-mcp-server-for-ai-coding-assistants-will-10x-your-productivity, the-proven-solution-for-unbelievable-rag-performance-lightrag-guide, the-ultimate-n8n-rag-ai-agent-template-local-ai-edition, i-built-the-ultimate-n8n-rag-ai-agent-template, you-have-to-try-agentic-rag-with-deepseek-r1-insane-results, n8n-crawl4ai-scrape-any-website-in-minutes-with-no-code, the-future-of-rag-is-agentic-learn-this-strategy-now, effortless-rag-in-n8n-use-all-your-files-pdfs-excel-and-more, i-built-a-full-rag-ai-agent-with-no-code-in-4-minutes-with-vectorshift, run-all-your-ai-locally-in-minutes-llms-rag-and-more, this-rag-ai-agent-with-n8n-supabase-is-the-real-deal, no-code-rag-agents-you-have-to-check-out-n8n-langchain, this-ai-agent-with-rag-manages-my-life, the-most-value-packed-rag-guide-on-youtube-feat-llama-31-405b]
created: 2026-07-21
updated: 2026-07-21
---

# Chunking

Chunking is the preprocessing step that splits large source documents into small, self-contained segments before they are embedded and stored for retrieval. As Cole puts it, "When we are chunking our documents, we're splitting them up into bite-sized pieces of information. So when we retrieve a chunk, we have just a little bit of information that ideally has exactly what our agent needs" [0:11:16]. It is the first, most consequential decision in any [RAG](./rag.md) pipeline: retrieval can only ever be as good as the chunks it draws from.

## Why it matters

Chunking exists to solve two problems at once, accuracy and cost. Storing an entire document as a single record poisons retrieval: "we can't just store every single document as a single record here because that's way too much to pull into the large language model and it's going to make the embeddings really inaccurate" [0:05:24]. A 50,000-word page embedded as one vector produces a blurry, averaged representation that matches nothing well. Splitting fixes both the embedding precision and the amount of context handed to the model, so the agent "can retrieve the specific knowledge it needs from a piece of documentation without pulling in the entire thing" [0:12:04]. The cost side is just as sharp: pulling small chunks instead of whole documents is "about a hundred times cheaper for these really large knowledge bases" [0:11:53].

## How it works

The naive baseline is a fixed-size character split, often a recursive character text splitter with a chunk size around 400 to 1,000 characters, sometimes with overlap. Cole repeatedly notes this is a reasonable default that depends heavily on the use case: smaller chunk sizes keep prompts short for weaker or local models, larger sizes preserve more context per record. The key failure mode of a blind split is cutting through the middle of an idea, so "we definitely want to make sure that we don't split in the middle of paragraphs and bullet point lists" [0:11:16]. That failure is exactly what smarter strategies are built to avoid.

## Contrasts with

- [Structured vs Unstructured Data](./structured-vs-unstructured-data.md) - chunking is for prose; tabular data is better kept queryable as SQL rather than shredded into chunks.

## Builds on

- [Vector Embeddings](./vector-embeddings.md) - each chunk is embedded into a vector for similarity search.
- [RAG](./rag.md) - chunking is the ingestion-side foundation of the retrieval pipeline.
- [Document Extraction](./document-extraction.md) - Pulling clean raw text out of source files (PDFs, Excel, HTML, JSON) is the real bottleneck in RAG ingestion, solved by branching on each file's MIME type to a format-specific extractor rather than one universal node.

## Related

- [Context-Aware Chunking](./context-aware-chunking.md) - splitting along semantic and structural boundaries instead of blind character counts.
- [Late Chunking](./late-chunking.md) - embedding first and splitting after, so chunks keep whole-document context.
- [Contextual Retrieval](./contextual-retrieval.md) - enriching each chunk with document-level context before embedding.
- [Knowledge Bases](./knowledge-bases.md) - where the finished chunks live.
- [Web Crawling & Ingestion](./web-crawling.md) - the crawl step that produces the documents you then chunk.
- [Context Engineering](./context-engineering.md) - chunking as an upstream lever on what fills the context window.
- [Semantic Search](./semantic-search.md) - the retrieval this preprocessing enables.
- [Delete-Before-Insert Re-Ingestion](./delete-before-insert-reingestion.md) - Because most vector stores insert rather than upsert, you must delete a document's existing chunks (matched by file ID metadata) before re-inserting an updated version, or stale chunks linger forever.
- [Metadata Filtering](./metadata-filtering.md) - Tagging every embedded chunk with source metadata so retrieval can be scoped to one document set and answers can cite which document they came from.
- [llms.txt](./llms-txt.md) - An emerging convention where a project publishes all of its documentation as a single LLM-formatted page (llms.txt / llms-full.txt), so one fetch yields complete, chunk-ready knowledge for an agent.

## Tools

- [Docling](../entities/tools/docling.md) - Cole's preferred chunking library, used for its hybrid chunking strategy.
- [LangChain](../entities/tools/langchain.md) - provides the recursive character text splitter used as a simple default.
- [Crawl4AI](../entities/tools/crawl4ai.md) - returns clean markdown that makes structure-aware splitting easy.
- [LightRAG](../entities/tools/lightrag.md) - abstracts chunking away, auto-chunking on `rag.insert`.
- [OpenAI Whisper](../entities/tools/whisper.md) - OpenAI's open-source speech-to-text model; Whisper Turbo runs fully locally as Docling's ASR pipeline to transcribe audio and video into timestamped text.

## Sources

- [Why the Best AI Coding Tools Abandoned RAG (And What They Use Instead)](../sources/why-the-best-ai-coding-tools-abandoned-rag-and-what-they-use-instead.md) - "[0:11:16] When we are chunking our documents, we're splitting them up into bite-sized pieces of information. So when we retrieve a chunk, we have just a little bit of information that ideally has exactly what our agent needs."
- [Every RAG Strategy Explained in 13 Minutes (No Fluff)](../sources/every-rag-strategy-explained-in-13-minutes-no-fluff.md) - "[0:07:45] If we don't split our documents into bite-sized pieces of information, then our embeddings are inaccurate and our agents are pulling way too much information."
- [The Future of RAG is Agentic - Learn this Strategy NOW](../sources/the-future-of-rag-is-agentic-learn-this-strategy-now.md) - "[0:11:32] we don't want to store a massive page just in one record for the llm to retrieve because if we have a documentation page that's like 50,000 words and we give that all to an llm at the same time that is going to overwhelm The Prompt"
- [The Most Value Packed RAG Guide on YouTube (Feat. Llama 3.1 405B!)](../sources/the-most-value-packed-rag-guide-on-youtube-feat-llama-31-405b.md) - "[0:01:46] we're going to split up every document into nice and concise chunks of a 100 characters a thousand characters you can play around with this and turn each one of these into vectors"
- [The EASIEST Possible Strategy for Accurate RAG (Step by Step Guide)](../sources/the-easiest-possible-strategy-for-accurate-rag-step-by-step-guide.md) - "[0:10:22] we're just splitting the document every 400 characters with no overlap. And you could adjust these parameters yourself, build out your own chunking strategy"
- [The Simplest RAG Stack That Actually Works (Complete Guide)](../sources/the-simplest-rag-stack-that-actually-works-complete-guide.md) - "[0:04:02] out of all of the chunking strategies, hybrid is by far my favorite... we have really nice starts and ends to all of our chunks thanks to our hybrid chunking strategy"
- [Turn ANY File into LLM Knowledge in SECONDS](../sources/turn-any-file-into-llm-knowledge-in-seconds.md) - "[0:11:16] We definitely want to make sure that we don't split in the middle of paragraphs and bullet point lists for example."
- [I Built the Ultimate RAG MCP Server for AI Coding (Better than Context7)](../sources/i-built-the-ultimate-rag-mcp-server-for-ai-coding-better-than-context7.md) - "[0:16:08] After we crawl we have to chunk everything for Supabase. I have a decent strategy where I try to keep all of the paragraphs and sentences together as much as I can."
- [Run ALL Your AI Locally in Minutes (LLMs, RAG, and more)](../sources/run-all-your-ai-locally-in-minutes-llms-rag-and-more.md) - "[0:16:51] I want to keep it small just because I'm running llama 3.1 locally... so I want my prompts to be small so I'm keeping my context lower by having smaller chunk sizes"
- [Super Special Livestream this Weekend! (LIVE AI Agent Build)](../sources/super-special-livestream-this-weekend-live-ai-agent-build.md)
- [Knowledge Graphs in n8n are FINALLY Here!](../sources/knowledge-graphs-in-n8n-are-finally-here.md)
- [Your ULTIMATE n8n RAG AI Agent Template just got a Massive Upgrade](../sources/your-ultimate-n8n-rag-ai-agent-template-just-got-a-massive-upgrade.md)
- [Introducing RAG 2.0: Agentic RAG + Knowledge Graphs (FREE Template)](../sources/introducing-rag-20-agentic-rag-knowledge-graphs-free-template.md)
- [All the BEST RAG Strategies in ONE MCP for AI Coding Assistants](../sources/all-the-best-rag-strategies-in-one-mcp-for-ai-coding-assistants.md)
- [Turn ANY Website into LLM Knowledge in Seconds - EVOLVED](../sources/turn-any-website-into-llm-knowledge-in-seconds-evolved.md)
- [This MCP Server for AI Coding Assistants Will 10x Your Productivity](../sources/this-mcp-server-for-ai-coding-assistants-will-10x-your-productivity.md)
- [The PROVEN Solution for Unbelievable RAG Performance (LightRAG Guide)](../sources/the-proven-solution-for-unbelievable-rag-performance-lightrag-guide.md)
- [The ULTIMATE n8n RAG AI Agent Template - Local AI Edition](../sources/the-ultimate-n8n-rag-ai-agent-template-local-ai-edition.md)
- [I Built the ULTIMATE n8n RAG AI Agent Template](../sources/i-built-the-ultimate-n8n-rag-ai-agent-template.md)
- [You HAVE to Try Agentic RAG with DeepSeek R1 (Insane Results)](../sources/you-have-to-try-agentic-rag-with-deepseek-r1-insane-results.md)
- [n8n + Crawl4AI - Scrape ANY Website in Minutes with NO Code](../sources/n8n-crawl4ai-scrape-any-website-in-minutes-with-no-code.md)
- [Effortless RAG in n8n - Use ALL Your Files (PDFs, Excel, and More)](../sources/effortless-rag-in-n8n-use-all-your-files-pdfs-excel-and-more.md)
- [I Built a FULL RAG AI Agent with No Code in 4 Minutes with VectorShift](../sources/i-built-a-full-rag-ai-agent-with-no-code-in-4-minutes-with-vectorshift.md)
- [This RAG AI Agent with n8n + Supabase is the Real Deal](../sources/this-rag-ai-agent-with-n8n-supabase-is-the-real-deal.md)
- [No Code RAG Agents? You HAVE to Check out n8n + LangChain](../sources/no-code-rag-agents-you-have-to-check-out-n8n-langchain.md)
- [This AI Agent with RAG Manages MY LIFE](../sources/this-ai-agent-with-rag-manages-my-life.md)
