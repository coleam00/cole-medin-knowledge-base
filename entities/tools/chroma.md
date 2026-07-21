---
type: entity
subtype: tool
title: "Chroma"
description: "Publisher of the technical report on context rot that Cole cites as the most practical treatment of how input tokens degrade LLM performance."
resource: "https://www.trychroma.com"
tags: [vector-database, rag, local-ai]
videos: [ive-used-claude-code-for-2000-hours-heres-how-i-build-anything-with-it, turn-any-website-into-llm-knowledge-in-seconds-evolved, the-proven-solution-for-unbelievable-rag-performance-lightrag-guide, you-have-to-try-agentic-rag-with-deepseek-r1-insane-results, qwen-just-casually-started-the-local-ai-revolution, llama-32-is-insane-but-does-it-beat-gpt-as-an-ai-agent, this-ai-agent-with-rag-manages-my-life, the-most-value-packed-rag-guide-on-youtube-feat-llama-31-405b]
created: 2026-07-21
updated: 2026-07-21
---

# Chroma

Chroma (ChromaDB) is the lightweight, local-first vector database Cole reaches for whenever he wants [RAG](../../concepts/rag.md) without any infrastructure overhead. His reasoning is consistently about simplicity: "I just wanted something really simple and that you can run locally. So that's why I chose Chroma DB" ([0:11:44]). It stores [vector embeddings](../../concepts/vector-embeddings.md) and serves [semantic search](../../concepts/semantic-search.md), and because it runs in-process it is the default choice across his tutorials, especially when testing models with retrieval.

## How Cole uses it

Chroma is Cole's standard local vector store for demos and experiments. "I'm using chroma for a local Vector database that's just going to run in memory you can also use chroma and save it to dis to have more persistent Vector DB storage" ([0:05:29]), and the retrieval call is a one-liner: "we're going to use the chroma similarity search function on our Vector database given the question and then we want the five most related pieces of knowledge" ([0:06:40]). When he benchmarks new models he keeps the retrieval layer deliberately plain, "just using a local chroma instance because I don't need anything fancy to test llms with Rag" ([0:05:41]), the same reason it appears in his DeepSeek R1, Qwen, and Llama 3.2 agentic-RAG builds. On disk it is unmistakable: "you're going to have a chroma DB folder that has a SQL light file as well as a folder with a lot of other stuff in it" ([0:04:40]).

Speed is the other reason Cole likes it. Paired with [Crawl4AI](./crawl4ai.md), the bottleneck is never Chroma: "basically the insert into Chroma DB takes longer than the scraping itself. That is how blazing fast crawl for AAI is" ([0:13:05]). And because it only touches the vector index, it beats graph-augmented retrieval on latency: "because Chromb only has to search the vector database and not the knowledge graph as well, it is going to give us a faster response" ([0:11:19]) - the [traditional RAG](../../concepts/traditional-rag.md) fast path he contrasts against knowledge-graph strategies. Its in-memory, local nature makes it a natural fit for his [local AI](../../concepts/local-ai.md) work.

Notably, Cole also cites the **company** Chroma as a research publisher. His single most-recommended reading on [context rot](../../concepts/context-rot.md) is theirs: "my favorite, this is the most practical and probably most popular as well, is the Chroma technical report covering how increasing input tokens impacts LLM performance" ([0:02:52]) - the empirical grounding for why he keeps retrieved context tight.

## Realizes

- [Retrieval-Augmented Generation (RAG)](../../concepts/rag.md) - Grounding an LLM's answers by retrieving relevant documents from an external knowledge base and injecting them into the prompt at query time.
- [Vector Embeddings](../../concepts/vector-embeddings.md) - Numeric representations of text that enable semantic similarity search, stored and managed in a vector database for retrieval.
- [Semantic Search](../../concepts/semantic-search.md) - Retrieving content by embedding-based similarity so results match on meaning rather than exact keywords.

## Contrasts with

- [Qdrant](./qdrant.md) - Vector database with an MCP server that lets agents do RAG without implementing custom retrieval tools.
- [Pinecone](./pinecone.md) - Vector database used optionally by Auto-GPT to provide long-term memory.
- [LightRAG](./lightrag.md) - A knowledge-graph RAG solution Cole previously covered; suited to static document summarization but slower to build and query than Graphiti.

## Works with

- [Crawl4AI](./crawl4ai.md) - The open-source crawling library powering Cole's RAG MCP server, handling llms.txt, sitemaps, and recursive scraping.

## Related

- [Agentic RAG](../../concepts/agentic-rag.md) - Giving an agent retrieval as a tool so it decides when and how to search a knowledge base instead of a single static lookup.
- [Traditional RAG](../../concepts/traditional-rag.md) - The classic one-shot, static RAG pipeline that embeds a query, runs a single vector similarity search, and stuffs the top chunks into the prompt.
- [Chunking](../../concepts/chunking.md) - Splitting source documents into appropriately sized, embeddable segments, the foundational preprocessing step that determines RAG retrieval quality.
- [Context Rot](../../concepts/context-rot.md) - The degradation of an agent's output quality as its context window fills with stale, irrelevant, or accumulated information over a long session.
- [Local & Self-Hosted AI](../../concepts/local-ai.md) - Running open-weight models on your own hardware or cloud for privacy, cost control, and independence from API providers.
- [Model Selection](../../concepts/model-selection.md) - Choosing the right LLM per task by trading off quality, speed, and cost.

## Sources

- [Turn ANY Website into LLM Knowledge in Seconds - EVOLVED](../../sources/turn-any-website-into-llm-knowledge-in-seconds-evolved.md) - "[0:11:44] I just wanted something really simple and that you can run locally. So that's why I chose Chroma DB."
- [The Most Value Packed RAG Guide on YouTube (Feat. Llama 3.1 405B!)](../../sources/the-most-value-packed-rag-guide-on-youtube-feat-llama-31-405b.md) - "[0:05:29] I'm using chroma for a local Vector database that's just going to run in memory you can also use chroma and save it to dis to have more persistent Vector DB storage."
- [I've Used Claude Code for 2,000+ Hours - Here's How I Build Anything With It](../../sources/ive-used-claude-code-for-2000-hours-heres-how-i-build-anything-with-it.md) - "[0:02:52] my favorite, this is the most practical and probably most popular as well, is the Chroma technical report covering how increasing input tokens impacts LLM performance."
- [The PROVEN Solution for Unbelievable RAG Performance (LightRAG Guide)](../../sources/the-proven-solution-for-unbelievable-rag-performance-lightrag-guide.md) - "[0:11:19] because Chromb only has to search the vector database and not the knowledge graph as well, it is going to give us a faster response."
- [You HAVE to Try Agentic RAG with DeepSeek R1 (Insane Results)](../../sources/you-have-to-try-agentic-rag-with-deepseek-r1-insane-results.md) - "[0:14:24] I still want to show you my process here for getting our local knowledge based set up with chroma DB."
- [Qwen Just Casually Started the Local AI Revolution](../../sources/qwen-just-casually-started-the-local-ai-revolution.md) - "[0:10:28] for rag I am integrating with chroma for a local Vector database."
- [Llama 3.2 is INSANE - But Does it Beat GPT as an AI Agent?](../../sources/llama-32-is-insane-but-does-it-beat-gpt-as-an-ai-agent.md) - "[0:05:41] the vector database tools that we have for Rag and that's just using a local chroma instance because I don't need anything fancy to test llms with Rag."
- [This AI Agent with RAG Manages MY LIFE](../../sources/this-ai-agent-with-rag-manages-my-life.md) - "[0:04:40] you're going to have a chroma DB folder that has a SQL light file as well as a folder with a lot of other stuff in it."
