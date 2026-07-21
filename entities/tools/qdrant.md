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

Qdrant is the vector database Cole reaches for when speed is the priority and the workload is pure similarity search. As he puts it plainly, "quadron is just a vector database I can only store embeddings and so if I wanted to use quadrant in my solution I could only use it for basic Rag" ([0:38:18]). That focus is also its selling point: "quadrant is a lot faster so if I wanted to optimize for Speed here I actually would have all my knowledge embeddings stored in quadrant" ([0:38:49]). It is a core [RAG](../../concepts/rag.md) building block in his stacks, storing [vector embeddings](../../concepts/vector-embeddings.md) for fast [semantic search](../../concepts/semantic-search.md).

## How Cole uses it

The feature Cole highlights most is Qdrant's MCP server, which lets an agent do retrieval without any custom plumbing. "you've got quadrant for example for rag you don't even have to implement custom rag tools you can just use this quadrant mCP" ([0:11:09]), and he points to "the Quadrant MCP server" as the way to "have more like long-term memory, implement rag within your AI IDE" ([0:15:44]). This makes Qdrant a clean way to bolt [tool use](../../concepts/tool-use.md) and retrieval onto a coding assistant through [MCP](../../concepts/mcp.md).

Qdrant is a fixture of Cole's [local AI](../../concepts/local-ai.md) cloud stacks, listed alongside "n8n superbase olama open web UI flow wise quadrant" ([0:02:12]). He notes it overlaps with [Supabase](./supabase.md) as a vector store but keeps it for throughput: "quadrant is also kind of similar because you can use it as a vector store just like you can use superbase but I'm keeping quadrant in there... just because it's faster than superbase" ([0:03:02]). Running fully local, "including quadrant this can be whatever you want" ([0:13:24]), and it ships a dashboard at its default port: "you can actually go to this URL Right Here Local Host um port 6333 dashboard and you'll see your collection here" ([0:14:44]). The same port carries over to deployment: "for the URL is just going to be quadrant HTTP quadrant and then the port is 6333" ([0:19:26]) once containerized for [agent deployment](../../concepts/agent-deployment.md).

## Related

- [RAG](../../concepts/rag.md) and [Semantic Search](../../concepts/semantic-search.md) - Qdrant stores embeddings for fast retrieval.
- [Vector Embeddings](../../concepts/vector-embeddings.md) - the data it holds.
- [Model Context Protocol (MCP)](../../concepts/mcp.md) and [Tool Use](../../concepts/tool-use.md) - its MCP server gives agents RAG with no custom tools.
- [Local & Self-Hosted AI](../../concepts/local-ai.md) and [Agent Deployment](../../concepts/agent-deployment.md) - a staple of his local and cloud stacks.
- Sibling tools: [Supabase](./supabase.md) (overlapping vector store), [Pinecone](./pinecone.md), [Chroma](./chroma.md), [n8n](./n8n.md), [Ollama](./ollama.md), [Local AI Package](./local-ai-package.md).

## Sources

- [The Future of RAG is Agentic - Learn this Strategy NOW](../../sources/the-future-of-rag-is-agentic-learn-this-strategy-now.md) - "[0:38:18] quadron is just a vector database I can only store embeddings and so if I wanted to use quadrant in my solution I could only use it for basic Rag."
- [Claude MCP has Changed AI Forever - Here's What You NEED to Know](../../sources/claude-mcp-has-changed-ai-forever-heres-what-you-need-to-know.md) - "[0:11:09] you've got quadrant for example for rag you don't even have to implement custom rag tools you can just use this quadrant mCP."
- [Code 100x Faster with AI, Here's How (No Hype, FULL Process)](../../sources/code-100x-faster-with-ai-heres-how-no-hype-full-process.md) - "[0:15:44] if you want to have more like long-term memory, implement rag within your AI IDE... For example, the Quadrant MCP server."
- [Run Supabase 100% LOCALLY for Your AI Agents](../../sources/run-supabase-100-locally-for-your-ai-agents.md) - "[0:03:02] quadrant is also kind of similar because you can use it as a vector store just like you can use superbase but I'm keeping quadrant in there... just because it's faster than superbase."
- [Run ALL Your AI Locally in Minutes (LLMs, RAG, and more)](../../sources/run-all-your-ai-locally-in-minutes-llms-rag-and-more.md) - "[0:11:30] if you go to local hostport 6333 ... it's going to take you to your very own self-hosted quadrant dashboard where you can see all your collections your knowledge base."
- [Use Open WebUI with Your N8N AI Agents - Voice Chat Included!](../../sources/use-open-webui-with-your-n8n-ai-agents-voice-chat-included.md) - "[0:14:44] you can actually go to this URL Right Here Local Host um port 6333 dashboard and you'll see your collection here."
- [Deploy ANY AI App to the Cloud FAST](../../sources/deploy-any-ai-app-to-the-cloud-fast.md) - "[0:19:26] right here for the URL is just going to be quadrant HTTP quadrant and then the port is 6333 go ahead and click save this connection is good as well."
- [Create Your Own Private Local AI Cloud Stack in Under 20 Minutes](../../sources/create-your-own-private-local-ai-cloud-stack-in-under-20-minutes.md) - "[0:02:12] we've got n8n superbase olama open web UI flow wise quadrant."
- [Local vs. Cloud LLMs/RAG - Let's FINALLY End this Debate](../../sources/local-vs-cloud-llmsrag-lets-finally-end-this-debate.md) - "[0:01:59] next up we've got quadrant for the vector database."
