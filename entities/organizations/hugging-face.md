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

## Related

- [RAG](../../concepts/rag.md), [Agentic RAG](../../concepts/agentic-rag.md), and [Chunking](../../concepts/chunking.md): the retrieval pipelines its models power.
- [Vector Embeddings](../../concepts/vector-embeddings.md) and [Semantic Search](../../concepts/semantic-search.md): open embedding models pulled from the Hub.
- [Reranking](../../concepts/reranking.md): cross-encoder models downloaded for relevance scoring.
- [Local AI](../../concepts/local-ai.md) and [Model Quantization](../../concepts/model-quantization.md): serverless endpoints or fully local pipelines, quantized weights.
- Hosts [Meta AI](./meta.md) Llama and [DeepSeek](./deepseek.md) weights; the open-source counterpart to [OpenAI](./openai.md) embeddings; partners with [Scrimba](./scrimba.md) on its AI engineering path.

## Sources

- [Are You Building REAL AI Agents or Just Using LLMs?](../../sources/are-you-building-real-ai-agents-or-just-using-llms.md) - "[0:01:27] AI agents are programs where llm outputs control the workflow."
- [All the BEST RAG Strategies in ONE MCP for AI Coding Assistants](../../sources/all-the-best-rag-strategies-in-one-mcp-for-ai-coding-assistants.md) - "[0:17:08] we have this cross encoder that we're just downloading from HuggingFace. So we're pulling an open source model using that to do our reranking."
- [You HAVE to Try Agentic RAG with DeepSeek R1 (Insane Results)](../../sources/you-have-to-try-agentic-rag-with-deepseek-r1-insane-results.md) - "[0:10:08] we create this embedding model from hugging face so we're going to just be running this locally on our machine."
- [Function Calling with ANY LLM for Local AI Agents (Feat. LangChain, HuggingFace, and Llama 3)](../../sources/function-calling-with-any-llm-for-local-ai-agents-feat-langchain-huggingface-and-llama-3.md) - "[0:04:02] you can swap it out for this code right here huggingface pipeline. from model ID and then you will actually have the model running locally on your laptop."
- [The Most Value Packed RAG Guide on YouTube (Feat. Llama 3.1 405B!)](../../sources/the-most-value-packed-rag-guide-on-youtube-feat-llama-31-405b.md) - "[0:03:39] we got hugging face for our access to llama 3.1 405b."
- [DeepSeek R1 Just Revolutionized AI Forever](../../sources/deepseek-r1-just-revolutionized-ai-forever.md) - "[0:09:41] what I can do is click on quantizations there's 43 models available here."
- [This AI Agent with RAG Manages MY LIFE](../../sources/this-ai-agent-with-rag-manages-my-life.md) - "[0:04:25] creating the embedding function using an open source hugging face embedding model."
