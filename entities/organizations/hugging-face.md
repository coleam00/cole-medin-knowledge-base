---
type: entity
subtype: organization
title: "Hugging Face"
description: "AI platform whose blog post and AI Agents course provide the starting definition: programs where LLM outputs control the workflow to achieve a goal."
resource: "https://huggingface.co"
tags: [open-source, models, embeddings, hub]
videos: [all-the-best-rag-strategies-in-one-mcp-for-ai-coding-assistants, are-you-building-real-ai-agents-or-just-using-llms, you-have-to-try-agentic-rag-with-deepseek-r1-insane-results, deepseek-r1-just-revolutionized-ai-forever, this-ai-agent-with-rag-manages-my-life, the-most-value-packed-rag-guide-on-youtube-feat-llama-31-405b, function-calling-with-any-llm-for-local-ai-agents-feat-langchain-huggingface-and-llama-3]
created: 2026-07-21
updated: 2026-07-21
---

# Hugging Face

Hugging Face is the open-model hub and platform Cole treats as the on-ramp to open-source AI: the place he pulls embedding models, cross-encoders, and open LLM weights, and the source of the definition he uses to open his "real agents" video. He starts "right here with this blog post by hugging face they have this really nice single sentence definition of what an agent is" ([0:01:27]), namely that "AI agents are programs where llm outputs control the workflow" ([0:01:27]). That framing anchors much of his agent teaching, and the platform underneath it shows up in nearly every [RAG](../../concepts/rag.md) build he ships.

In practice Hugging Face is Cole's default supplier of open models for retrieval and local inference. For [Reranking](../../concepts/reranking.md) he notes "we have this cross encoder that we're just downloading from HuggingFace... pulling an open source model" ([0:17:08]). For [Vector Embeddings](../../concepts/vector-embeddings.md) he repeatedly reaches for it, "creating the embedding function using an open source hugging face embedding model" ([0:04:25]) and "we create this embedding model from hugging face so we're going to just be running this locally on our machine" ([0:10:08]), a concrete path into [Local AI](../../concepts/local-ai.md). Its serverless API gives quick access to hosted weights, "hugging face endpoint is how you use their serverless API to use these models quickly" ([0:03:45]), while the same code swaps to fully local execution: "you can swap it out for this code right here huggingface pipeline... you will actually have the model running locally on your laptop" ([0:04:02]). It is also his gateway to large and trending open models, "we got hugging face for our access to llama 3.1 405b" ([0:03:39]), and a distribution channel for [DeepSeek](./deepseek.md) R1 where "you can also install through hugging face as well... click on quantizations there's 43 models available here" ([0:09:41]), tying it to [Model Quantization](../../concepts/model-quantization.md).

## Works with

- [Meta AI](./meta.md) - Cited as an example of a model trained with ~10x fewer parameters than GPT, pointing toward faster/cheaper training.
- [DeepSeek](./deepseek.md) - Chinese startup whose R1 open-source model was tied to Nvidia's $600B one-day drop; later shipped DeepSeek 3.2.

## Contrasts with

- [OpenAI](./openai.md) - Maker of GPT-4o mini (affordable-but-strong chat model) and text-embedding-3-small (recommended RAG embedding model).

## Related

- [Retrieval-Augmented Generation (RAG)](../../concepts/rag.md) - Grounding an LLM's answers by retrieving relevant documents from an external knowledge base and injecting them into the prompt at query time.
- [Agentic RAG](../../concepts/agentic-rag.md) - Giving an agent retrieval as a tool so it decides when and how to search a knowledge base, picking strategies and issuing follow-up queries instead of a single static lookup.
- [Chunking](../../concepts/chunking.md) - Splitting source documents into appropriately sized, embeddable segments, the foundational preprocessing step that determines RAG retrieval quality.
- [Vector Embeddings](../../concepts/vector-embeddings.md) - Numeric representations of text that enable semantic similarity search, stored and managed in a vector database for retrieval.
- [Semantic Search](../../concepts/semantic-search.md) - Retrieving content by embedding-based similarity so results match on meaning rather than exact keywords.
- [Reranking](../../concepts/reranking.md) - Applying a second, more precise model to reorder an initial candidate set so the most relevant chunks land at the top of the context.
- [Local & Self-Hosted AI](../../concepts/local-ai.md) - Running open-weight models on your own hardware or cloud for privacy, cost control, and independence from API providers.
- [Model Quantization](../../concepts/model-quantization.md) - Compressing model weights to lower precision so large models fit and run on limited local hardware.
- [Scrimba](./scrimba.md) - Interactive coding-education platform where tutorials become pair-programming sessions you can edit in real time; a recurring sponsor of Cole's videos.

## Sources

- [Are You Building REAL AI Agents or Just Using LLMs?](../../sources/are-you-building-real-ai-agents-or-just-using-llms.md) - "[0:01:27] AI agents are programs where llm outputs control the workflow."
- [All the BEST RAG Strategies in ONE MCP for AI Coding Assistants](../../sources/all-the-best-rag-strategies-in-one-mcp-for-ai-coding-assistants.md) - "[0:17:08] we have this cross encoder that we're just downloading from HuggingFace. So we're pulling an open source model using that to do our reranking."
- [You HAVE to Try Agentic RAG with DeepSeek R1 (Insane Results)](../../sources/you-have-to-try-agentic-rag-with-deepseek-r1-insane-results.md) - "[0:10:08] we create this embedding model from hugging face so we're going to just be running this locally on our machine."
- [Function Calling with ANY LLM for Local AI Agents (Feat. LangChain, HuggingFace, and Llama 3)](../../sources/function-calling-with-any-llm-for-local-ai-agents-feat-langchain-huggingface-and-llama-3.md) - "[0:04:02] you can swap it out for this code right here huggingface pipeline. from model ID and then you will actually have the model running locally on your laptop."
- [The Most Value Packed RAG Guide on YouTube (Feat. Llama 3.1 405B!)](../../sources/the-most-value-packed-rag-guide-on-youtube-feat-llama-31-405b.md) - "[0:03:39] we got hugging face for our access to llama 3.1 405b."
- [DeepSeek R1 Just Revolutionized AI Forever](../../sources/deepseek-r1-just-revolutionized-ai-forever.md) - "[0:09:41] what I can do is click on quantizations there's 43 models available here."
- [This AI Agent with RAG Manages MY LIFE](../../sources/this-ai-agent-with-rag-manages-my-life.md) - "[0:04:25] creating the embedding function using an open source hugging face embedding model."
