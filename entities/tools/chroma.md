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

## Related

- [RAG](../../concepts/rag.md), [Agentic RAG](../../concepts/agentic-rag.md), [Traditional RAG](../../concepts/traditional-rag.md) - Chroma is the local vector store in these pipelines.
- [Vector Embeddings](../../concepts/vector-embeddings.md), [Semantic Search](../../concepts/semantic-search.md), [Chunking](../../concepts/chunking.md) - what it stores and searches.
- [Context Rot](../../concepts/context-rot.md) - Chroma's technical report is Cole's go-to source on it.
- [Local & Self-Hosted AI](../../concepts/local-ai.md) - it runs fully local, in-memory or on disk.
- Sibling tools: [Qdrant](./qdrant.md), [Pinecone](./pinecone.md), [Crawl4AI](./crawl4ai.md), [LightRAG](./lightrag.md).

## Sources

- [Turn ANY Website into LLM Knowledge in Seconds - EVOLVED](../../sources/turn-any-website-into-llm-knowledge-in-seconds-evolved.md) - "[0:11:44] I just wanted something really simple and that you can run locally. So that's why I chose Chroma DB."
- [The Most Value Packed RAG Guide on YouTube (Feat. Llama 3.1 405B!)](../../sources/the-most-value-packed-rag-guide-on-youtube-feat-llama-31-405b.md) - "[0:05:29] I'm using chroma for a local Vector database that's just going to run in memory you can also use chroma and save it to dis to have more persistent Vector DB storage."
- [I've Used Claude Code for 2,000+ Hours - Here's How I Build Anything With It](../../sources/ive-used-claude-code-for-2000-hours-heres-how-i-build-anything-with-it.md) - "[0:02:52] my favorite, this is the most practical and probably most popular as well, is the Chroma technical report covering how increasing input tokens impacts LLM performance."
- [The PROVEN Solution for Unbelievable RAG Performance (LightRAG Guide)](../../sources/the-proven-solution-for-unbelievable-rag-performance-lightrag-guide.md) - "[0:11:19] because Chromb only has to search the vector database and not the knowledge graph as well, it is going to give us a faster response."
- [You HAVE to Try Agentic RAG with DeepSeek R1 (Insane Results)](../../sources/you-have-to-try-agentic-rag-with-deepseek-r1-insane-results.md) - "[0:14:24] I still want to show you my process here for getting our local knowledge based set up with chroma DB."
- [Qwen Just Casually Started the Local AI Revolution](../../sources/qwen-just-casually-started-the-local-ai-revolution.md) - "[0:10:28] for rag I am integrating with chroma for a local Vector database."
- [Llama 3.2 is INSANE - But Does it Beat GPT as an AI Agent?](../../sources/llama-32-is-insane-but-does-it-beat-gpt-as-an-ai-agent.md) - "[0:05:41] the vector database tools that we have for Rag and that's just using a local chroma instance because I don't need anything fancy to test llms with Rag."
- [This AI Agent with RAG Manages MY LIFE](../../sources/this-ai-agent-with-rag-manages-my-life.md) - "[0:04:40] you're going to have a chroma DB folder that has a SQL light file as well as a folder with a lot of other stuff in it."
