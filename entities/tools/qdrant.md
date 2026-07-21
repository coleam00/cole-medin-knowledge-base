---
type: entity
subtype: tool
title: "Qdrant"
description: "Vector database with an MCP server that lets agents do RAG without implementing custom retrieval tools."
resource: "https://qdrant.tech"
tags: [vector-database, rag, mcp, local-ai]
videos: [code-100x-faster-with-ai-heres-how-no-hype-full-process, claude-mcp-has-changed-ai-forever-heres-what-you-need-to-know, create-your-own-private-local-ai-cloud-stack-in-under-20-minutes, run-supabase-100-locally-for-your-ai-agents, the-future-of-rag-is-agentic-learn-this-strategy-now, use-open-webui-with-your-n8n-ai-agents-voice-chat-included, deploy-any-ai-app-to-the-cloud-fast, run-all-your-ai-locally-in-minutes-llms-rag-and-more, local-vs-cloud-llmsrag-lets-finally-end-this-debate]
created: 2026-07-21
updated: 2026-07-21
---

# Qdrant

Qdrant is the vector database Cole reaches for when speed is the priority and the workload is pure similarity search. As he puts it plainly, "Qdrant is just a vector database I can only store embeddings and so if I wanted to use Qdrant in my solution I could only use it for basic Rag" ([0:38:18]). That focus is also its selling point: "Qdrant is a lot faster so if I wanted to optimize for Speed here I actually would have all my knowledge embeddings stored in Qdrant" ([0:38:49]). It is a core [RAG](../../concepts/rag.md) building block in his stacks, storing [vector embeddings](../../concepts/vector-embeddings.md) for fast [semantic search](../../concepts/semantic-search.md).

## How Cole uses it

The feature Cole highlights most is Qdrant's MCP server, which lets an agent do retrieval without any custom plumbing. "you've got Qdrant for example for rag you don't even have to implement custom rag tools you can just use this Qdrant mCP" ([0:11:09]), and he points to "the Qdrant MCP server" as the way to "have more like long-term memory, implement rag within your AI IDE" ([0:15:44]). This makes Qdrant a clean way to bolt [tool use](../../concepts/tool-use.md) and retrieval onto a coding assistant through [MCP](../../concepts/mcp.md).

Qdrant is a fixture of Cole's [local AI](../../concepts/local-ai.md) cloud stacks, listed alongside "n8n Supabase Ollama open web UI Flowise Qdrant" ([0:02:12]). He notes it overlaps with [Supabase](./supabase.md) as a vector store but keeps it for throughput: "Qdrant is also kind of similar because you can use it as a vector store just like you can use Supabase but I'm keeping Qdrant in there... just because it's faster than Supabase" ([0:03:02]). Running fully local, "including Qdrant this can be whatever you want" ([0:13:24]), and it ships a dashboard at its default port: "you can actually go to this URL Right Here Local Host um port 6333 dashboard and you'll see your collection here" ([0:14:44]). The same port carries over to deployment: "for the URL is just going to be Qdrant HTTP Qdrant and then the port is 6333" ([0:19:26]) once containerized for [agent deployment](../../concepts/agent-deployment.md).

## Realizes

- [Retrieval-Augmented Generation (RAG)](../../concepts/rag.md) - grounding an LLM's answers by retrieving relevant documents from an external knowledge base and injecting them into the prompt at query time.
- [Semantic Search](../../concepts/semantic-search.md) - retrieving content by embedding-based similarity so results match on meaning rather than exact keywords.
- [Vector Embeddings](../../concepts/vector-embeddings.md) - numeric representations of text that enable semantic similarity search, stored and managed in a vector database for retrieval.

## Contrasts with

- [Supabase](./supabase.md) - a single platform providing Postgres for scalable chat memory plus the pgvector store for RAG embeddings; an overlapping vector store Cole keeps Qdrant alongside for speed.
- [Pinecone](./pinecone.md) - vector database used optionally by Auto-GPT to provide long-term memory.
- [Chroma](./chroma.md) - publisher of the technical report on context rot that Cole cites as the most practical treatment of how input tokens degrade LLM performance.

## Works with

- [Model Context Protocol (MCP)](../../concepts/mcp.md) - an open protocol for packaging tools, data, and RAG capabilities as servers that any AI coding assistant or agent can connect to and call with a standard interface.
- [Tool Calling](../../concepts/tool-use.md) - letting an LLM invoke external functions and APIs so it can take actions and fetch data beyond its parametric knowledge.
- [Ollama](./ollama.md) - the local LLM runtime that rounds out the same self-hosted stack.
- [n8n](./n8n.md) - a no-code AI automation platform for building agents and workflows that integrate with 500+ applications.
- [Local AI Package](./local-ai-package.md) - Cole's bundled collection of self-hosted AI services that installs the whole stack together for free.

## Related

- [Local & Self-Hosted AI](../../concepts/local-ai.md) - running open-weight models on your own hardware or cloud for privacy, cost control, and independence from API providers.
- [Agent Deployment](../../concepts/agent-deployment.md) - getting agents to production, containerizing, networking, reverse-proxying, and choosing a provider-agnostic, cost-predictable host.
- [Agent Security](../../concepts/agent-security.md) - sandboxing agents, scoping permissions, and keeping secrets out of the model to limit blast radius.
- [Model Selection](../../concepts/model-selection.md) - choosing the right LLM per task by trading off quality, speed, and cost.

## Sources

- [The Future of RAG is Agentic - Learn this Strategy NOW](../../sources/the-future-of-rag-is-agentic-learn-this-strategy-now.md) - "[0:38:18] Qdrant is just a vector database I can only store embeddings and so if I wanted to use Qdrant in my solution I could only use it for basic Rag."
- [Claude MCP has Changed AI Forever - Here's What You NEED to Know](../../sources/claude-mcp-has-changed-ai-forever-heres-what-you-need-to-know.md) - "[0:11:09] you've got Qdrant for example for rag you don't even have to implement custom rag tools you can just use this Qdrant mCP."
- [Code 100x Faster with AI, Here's How (No Hype, FULL Process)](../../sources/code-100x-faster-with-ai-heres-how-no-hype-full-process.md) - "[0:15:44] if you want to have more like long-term memory, implement rag within your AI IDE... For example, the Qdrant MCP server."
- [Run Supabase 100% LOCALLY for Your AI Agents](../../sources/run-supabase-100-locally-for-your-ai-agents.md) - "[0:03:02] Qdrant is also kind of similar because you can use it as a vector store just like you can use Supabase but I'm keeping Qdrant in there... just because it's faster than Supabase."
- [Run ALL Your AI Locally in Minutes (LLMs, RAG, and more)](../../sources/run-all-your-ai-locally-in-minutes-llms-rag-and-more.md) - "[0:11:30] if you go to local hostport 6333 ... it's going to take you to your very own self-hosted Qdrant dashboard where you can see all your collections your knowledge base."
- [Use Open WebUI with Your N8N AI Agents - Voice Chat Included!](../../sources/use-open-webui-with-your-n8n-ai-agents-voice-chat-included.md) - "[0:14:44] you can actually go to this URL Right Here Local Host um port 6333 dashboard and you'll see your collection here."
- [Deploy ANY AI App to the Cloud FAST](../../sources/deploy-any-ai-app-to-the-cloud-fast.md) - "[0:19:26] right here for the URL is just going to be Qdrant HTTP Qdrant and then the port is 6333 go ahead and click save this connection is good as well."
- [Create Your Own Private Local AI Cloud Stack in Under 20 Minutes](../../sources/create-your-own-private-local-ai-cloud-stack-in-under-20-minutes.md) - "[0:02:12] we've got n8n Supabase Ollama open web UI Flowise Qdrant."
- [Local vs. Cloud LLMs/RAG - Let's FINALLY End this Debate](../../sources/local-vs-cloud-llmsrag-lets-finally-end-this-debate.md) - "[0:01:59] next up we've got Qdrant for the vector database."
