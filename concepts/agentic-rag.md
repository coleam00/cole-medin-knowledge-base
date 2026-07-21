---
type: concept
title: "Agentic RAG"
description: "Giving an agent retrieval as a tool so it decides when and how to search a knowledge base, picking strategies and issuing follow-up queries instead of a single static lookup."
tags: [rag, agents, tool-calling, retrieval, knowledge-base]
videos: [pydantic-ai-20-the-new-best-way-to-build-ai-agents-is-composing-capabilities, im-building-an-ai-dark-factory-that-ships-its-own-code-public-experiment, everything-you-thought-about-building-ai-agents-is-wrong, the-subagent-era-is-officially-here-learn-this-now, why-the-best-ai-coding-tools-abandoned-rag-and-what-they-use-instead, the-simplest-rag-stack-that-actually-works-complete-guide, the-only-ai-tech-stack-you-need-in-2026, every-rag-strategy-explained-in-13-minutes-no-fluff, super-special-livestream-this-weekend-live-ai-agent-build, turn-any-file-into-llm-knowledge-in-seconds, knowledge-graphs-in-n8n-are-finally-here, your-ultimate-n8n-rag-ai-agent-template-just-got-a-massive-upgrade, archon-beta-launch-livestream-what-you-missed, introducing-archon-the-revolutionary-operating-system-for-ai-coding, introducing-rag-20-agentic-rag-knowledge-graphs-free-template, all-the-best-rag-strategies-in-one-mcp-for-ai-coding-assistants, make-rag-100x-better-with-real-time-knowledge-graphs, the-3-must-have-mcp-servers-for-any-ai-coding-and-how-to-use-them, i-built-the-ultimate-rag-mcp-server-for-ai-coding-better-than-context7, the-proven-solution-for-unbelievable-rag-performance-lightrag-guide, the-ultimate-n8n-rag-ai-agent-template-local-ai-edition, i-built-the-ultimate-n8n-rag-ai-agent-template, this-is-hands-down-the-best-way-to-build-ai-agents, you-have-to-try-agentic-rag-with-deepseek-r1-insane-results, n8n-crawl4ai-scrape-any-website-in-minutes-with-no-code, the-future-of-rag-is-agentic-learn-this-strategy-now, i-created-the-best-ai-agent-platform-in-just-2-months, claude-computer-use-boltnew-the-ultimate-ai-coding-combo, qwen-just-casually-started-the-local-ai-revolution, run-all-your-ai-locally-in-minutes-llms-rag-and-more, this-rag-ai-agent-with-n8n-supabase-is-the-real-deal, this-ai-agent-with-rag-manages-my-life, the-most-value-packed-rag-guide-on-youtube-feat-llama-31-405b]
created: 2026-07-21
updated: 2026-07-21
---

# Agentic RAG

"all agentic rag is is giving agents the ability to reason about how they explore the knowledge base instead of just giving it a single tool" [0:03:14]. Agentic RAG turns retrieval from a fixed pre-processing step into a set of tools the agent calls on its own judgment. Rather than force-feeding context into the prompt before the model ever runs, the agent comes first and decides whether to search, what to search for, and which strategy fits the question. As Cole frames it: "instead of just having rag be a oneshot here's some context from the vector database we actually create rag as tools for the agent to interact with."

## How it works

The core move is exposing one or more retrieval capabilities as agent tools. The agent reads the user question, decides if it even needs to search (a plain "hi" should not trigger a lookup), and then chooses a strategy: a plain [semantic search](./semantic-search.md), a [keyword search](./keyword-search.md), a [hybrid search](./hybrid-search.md), or a hop into a [knowledge graph](./knowledge-graphs.md) when the question is relational ("if we're asking about how two companies work together, now that would be a good example to go and search the knowledge graph"). A common pattern is several vector stores or knowledge bases behind separate tools so the agent picks the right corpus per question. Because the agent can observe that a first lookup failed and try again with a better query or a different tool, retrieval becomes iterative and self-correcting.

The tradeoff is flexibility bought with predictability: "this makes rag very flexible but it is going to be less predictable as well." What the agent searches, and where, is driven largely by the system prompt and tool descriptions.

## Builds on

- [Retrieval-Augmented Generation (RAG)](./rag.md) - agentic RAG is still RAG; it changes control flow, not the underlying grounding idea.

## Contrasts with

- [Traditional RAG](./traditional-rag.md) - the naive one-shot pipeline that always retrieves before the LLM, assuming every prompt is a question about the documents.

## Related

- [Agentic Search](./agentic-search.md) - the same reason-then-retrieve loop applied to codebases and the web without a vector index.
- [Hybrid Search](./hybrid-search.md), [Keyword Search](./keyword-search.md), [Semantic Search](./semantic-search.md) - strategies the agent chooses among.
- [Knowledge Graphs](./knowledge-graphs.md), [Knowledge Bases](./knowledge-bases.md), [Vector Embeddings](./vector-embeddings.md) - the stores retrieval tools sit on top of.
- [Reranking](./reranking.md), [Query Expansion](./query-expansion.md), [Multi-Query RAG](./multi-query-rag.md), [Hierarchical RAG](./hierarchical-rag.md), [Contextual Retrieval](./contextual-retrieval.md) - complementary accuracy strategies stacked underneath agentic tools.
- [Model Context Protocol (MCP)](./mcp.md) - a common way to ship a RAG knowledge base as a tool to a coding assistant.
- [Structured vs. Unstructured Data](./structured-vs-unstructured-data.md), [Human in the Loop](./human-in-the-loop.md).
- [Production-Ready RAG](./production-ready-rag.md) - Building RAG that survives a growing knowledge base, updated documents, and unexpected user questions, unlike toy 'chat with your PDF' demos.
- [Reasoning Model as a Tool](./reasoning-model-as-a-tool.md) - Architecture where a fast, lightweight model drives the conversation and calls a slow, powerful reasoning model as just another tool, keeping the flow nimble while still getting reasoning-grade answers on the hard step.
- [Metadata Filtering](./metadata-filtering.md) - Tagging every embedded chunk with source metadata so retrieval can be scoped to one document set and answers can cite which document they came from.

## Tools

- [Archon](../entities/tools/archon.md) - bundles several agentic RAG functions (keyword, semantic, code-example search) over a crawled knowledge base.
- [Pydantic AI](../entities/tools/pydantic-ai.md) - Cole's Python framework for wiring retrieval as agent tools.
- [n8n](../entities/tools/n8n.md), [Supabase](../entities/tools/supabase.md), [Chroma](../entities/tools/chroma.md), [Qdrant](../entities/tools/qdrant.md) - no-code and vector-store building blocks for agentic RAG agents.
- [LightRAG](../entities/tools/lightrag.md) - combines vector retrieval and knowledge-graph search behind one agent-facing interface.
- [OpenAI o3-mini](../entities/tools/o3-mini.md) - OpenAI's small reasoning model, used as Archon's reasoner to write the scope document before the coder agent builds, and the head-to-head rival to DeepSeek R1 for coding.

## Sources

- [I Built the ULTIMATE n8n RAG AI Agent Template](../sources/i-built-the-ultimate-n8n-rag-ai-agent-template.md) - "[0:03:14] all agentic rag is is giving agents the ability to reason about how they explore the knowledge base instead of just giving it a single tool"
- [The Future of RAG is Agentic - Learn this Strategy NOW](../sources/the-future-of-rag-is-agentic-learn-this-strategy-now.md) - "[0:04:44] instead of just having rag be a oneshot here's some context from the vector database we actually create rag as tools for the agent to interact with"
- [Introducing RAG 2.0: Agentic RAG + Knowledge Graphs (FREE Template)](../sources/introducing-rag-20-agentic-rag-knowledge-graphs-free-template.md) - "[0:09:05] Agentic rag is all about giving the agent the ability to reason about how it explores the knowledge base instead of always force-feeding that context as kind of a pre-processing step."
- [Every RAG Strategy Explained in 13 Minutes (No Fluff)](../sources/every-rag-strategy-explained-in-13-minutes-no-fluff.md) - "[0:04:22] my agent can pick and choose where it searches based on the question. And so this makes rag very flexible but it is going to be less predictable as well."
- [Everything You Thought About Building AI Agents is Wrong](../sources/everything-you-thought-about-building-ai-agents-is-wrong.md) - "[0:14:15] now we've kind of gotten to a middle ground this year with agentic rag. We give our agent the ability to perform both semantic search and other kinds of searches like GP and keyword search"
- [Knowledge Graphs in n8n are FINALLY Here!](../sources/knowledge-graphs-in-n8n-are-finally-here.md) - "[0:03:11] if we're asking about a single company, well, we should probably just go to the vector database... But if we're asking about how two companies work together, now that would be a good example to go and search the knowledge graph"
- [The Simplest RAG Stack That Actually Works (Complete Guide)](../sources/the-simplest-rag-stack-that-actually-works-complete-guide.md) - "[0:11:14] I would actually consider hybrid search a form of agentic rag... it's just generally the idea of you give your agent the ability to choose how it explores your knowledge base"
- [This AI Agent with RAG Manages MY LIFE](../sources/this-ai-agent-with-rag-manages-my-life.md) - "[0:00:58] we want an AI agent that will intelligently determine if it needs to go out and search through the documents or if it can answer the user question right away"
- [You HAVE to Try Agentic RAG with DeepSeek R1 (Insane Results)](../sources/you-have-to-try-agentic-rag-with-deepseek-r1-insane-results.md) - "[0:21:10] if we didn't get the right answer R1 would have actually told Qwen to go back and use this tool again and I see that a lot in my testing too so it's very much agentic rag"
- [All the BEST RAG Strategies in ONE MCP for AI Coding Assistants](../sources/all-the-best-rag-strategies-in-one-mcp-for-ai-coding-assistants.md) - "[0:13:30] one really common pattern for agentic rag is to have multiple different vector databases that serve different purposes and then your agent has tools to access each one of them"
- [Make RAG 100x Better with Real-Time Knowledge Graphs](../sources/make-rag-100x-better-with-real-time-knowledge-graphs.md) - "[0:25:22] if the agent can reason like oh I didn't get what I needed when I searched the knowledge graph. Let me now look in the vector database or vice versa."
- [Introducing Archon - The Revolutionary Operating System for AI Coding](../sources/introducing-archon-the-revolutionary-operating-system-for-ai-coding.md) - "[0:11:48] There's a couple different functions that we give it for more agentic rag to search through our knowledge base in different ways. And there's a lot of strategies for rag that I have built into this"
- [Why the Best AI Coding Tools Abandoned RAG (And What They Use Instead)](../sources/why-the-best-ai-coding-tools-abandoned-rag-and-what-they-use-instead.md) - "[0:13:33] We can give our AI agent the ability to not just figure out what to search but also how based on the specific task."
- [The ULTIMATE n8n RAG AI Agent Template - Local AI Edition](../sources/the-ultimate-n8n-rag-ai-agent-template-local-ai-edition.md) - "[0:03:41] instead of there being a retrieval before we reach the llm with agentic RAG the agent comes first and then it has tools available for it to perform Rag"
- [Pydantic AI 2.0: The New Best Way to Build AI Agents is Composing Capabilities](../sources/pydantic-ai-20-the-new-best-way-to-build-ai-agents-is-composing-capabilities.md) - "[0:09:43] we just have a search knowledgebased function for our knowledgebased capability."
- [Turn ANY File into LLM Knowledge in SECONDS](../sources/turn-any-file-into-llm-knowledge-in-seconds.md) - "[0:18:36] We just have a query that the agent decides basically it's search for our knowledge base."
- [The PROVEN Solution for Unbelievable RAG Performance (LightRAG Guide)](../sources/the-proven-solution-for-unbelievable-rag-performance-lightrag-guide.md) - "[0:22:42] this isn't the only way to make rag more accurate... You also have agentic rag, query expansion, reranking."
- [I'm Building an AI Dark Factory That Ships Its Own Code (Public Experiment)](../sources/im-building-an-ai-dark-factory-that-ships-its-own-code-public-experiment.md) - "[0:11:57] It'll let you ask questions to an agent that can perform rag to search through my YouTube video."
- [The Subagent Era Is Officially Here - Learn this Now](../sources/the-subagent-era-is-officially-here-learn-this-now.md)
- [The ONLY AI Tech Stack You Need in 2026](../sources/the-only-ai-tech-stack-you-need-in-2026.md)
- [Super Special Livestream this Weekend! (LIVE AI Agent Build)](../sources/super-special-livestream-this-weekend-live-ai-agent-build.md)
- [Your ULTIMATE n8n RAG AI Agent Template just got a Massive Upgrade](../sources/your-ultimate-n8n-rag-ai-agent-template-just-got-a-massive-upgrade.md)
- [Archon Beta Launch Livestream - What You Missed!](../sources/archon-beta-launch-livestream-what-you-missed.md)
- [The 3 MUST Have MCP Servers for Any AI Coding (and How to Use Them)](../sources/the-3-must-have-mcp-servers-for-any-ai-coding-and-how-to-use-them.md)
- [I Built the Ultimate RAG MCP Server for AI Coding (Better than Context7)](../sources/i-built-the-ultimate-rag-mcp-server-for-ai-coding-better-than-context7.md)
- [This is Hands Down the BEST Way to Build AI Agents](../sources/this-is-hands-down-the-best-way-to-build-ai-agents.md)
- [n8n + Crawl4AI - Scrape ANY Website in Minutes with NO Code](../sources/n8n-crawl4ai-scrape-any-website-in-minutes-with-no-code.md)
- [I Created the BEST AI Agent Platform in Just 2 MONTHS!](../sources/i-created-the-best-ai-agent-platform-in-just-2-months.md)
- [Claude Computer Use + Bolt.new - The ULTIMATE AI Coding Combo?!](../sources/claude-computer-use-boltnew-the-ultimate-ai-coding-combo.md)
- [Qwen Just Casually Started the Local AI Revolution](../sources/qwen-just-casually-started-the-local-ai-revolution.md)
- [Run ALL Your AI Locally in Minutes (LLMs, RAG, and more)](../sources/run-all-your-ai-locally-in-minutes-llms-rag-and-more.md)
- [This RAG AI Agent with n8n + Supabase is the Real Deal](../sources/this-rag-ai-agent-with-n8n-supabase-is-the-real-deal.md)
- [The Most Value Packed RAG Guide on YouTube (Feat. Llama 3.1 405B!)](../sources/the-most-value-packed-rag-guide-on-youtube-feat-llama-31-405b.md)
