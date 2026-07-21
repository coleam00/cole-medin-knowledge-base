---
type: concept
title: "The LLM Wiki"
description: "An LLM-maintained knowledge base of plain markdown pages that compiles sources into a navigable, self-referential wiki."
tags: [wiki, knowledge, markdown]
videos: [i-love-the-karpathy-llm-wiki-but-it-doesnt-scale-heres-what-does, finally-an-open-standard-for-the-karpathy-llm-wiki-is-here, i-built-self-evolving-claude-code-memory-w-karpathys-llm-knowledge-bases, chatgpt-teaches-the-secrets-to-financial-freedom]
created: 2026-07-21
updated: 2026-07-21
---

# The LLM Wiki

The LLM wiki is a knowledge base built and maintained by a language model as a set of plain markdown pages: index documents, entity documents, and concept documents, densely cross-linked and organized so an agent can navigate it directly. The pattern originated with Andrej Karpathy. As Cole frames it, "everyone is focused on LLM knowledge bases, which originated from this tweet from Andre Karpathy" [0:00:00], the idea of "using LLM to build personal knowledge bases for various topics of research interest. So taking external information bringing it into our own system and organizing it in the best way for agents to query" [0:00:29]. A typical instance has "your index documents with your tagging and categorization and all of your entities" [0:00:14].

The clearest mental model for how it works is compilation. "That brings us to the compiler analogy. This is the simplest way to explain everything that he's built... the way that we're handling knowledge is very similar to how we take source code all the way into a final application" [0:02:22]. Raw sources are the source code; the synthesized, linked wiki is the compiled artifact an agent queries. Because it is just markdown and links, the wiki itself IS the search index: no embeddings, no vector database, just an index page and relative links an agent follows on demand. This is why the pattern pairs so naturally with progressive disclosure and clean context.

The unsolved problem was interoperability: everyone built wikis their own way, so none could be shared. Google's Open Knowledge Format (OKF) is the answer. "We need a standard so that everyone's building wikis in the same way so that we can share them freely. And so that is what Google has released here with their open knowledge format" [0:02:06]. OKF standardizes two things: "The first is how we are organizing information like our entity documents and our concepts. And then the second standardization is the exact fields that we're going to have in our metadata" [0:03:10]. It is deliberately minimal, "the bare minimum layer that we need on top so that we can produce and consume these wikis in exactly the same way across everyone's agents that lean into OKF" [0:18:37]. The structure the wiki provides is also what tools like context retrievers add on top of a store: "that's one of the big things that context retriever does on top of Redis is it provides that structure. It's kind of like the metadata in a Karpathy LLM wiki" [0:08:48].

## Builds on

- [Knowledge Bases](./knowledge-bases.md) - the LLM wiki is one concrete way to organize a knowledge base for agents.
- [Progressive Disclosure](./progressive-disclosure.md) - an agent reads the index, then follows only the links a question needs, instead of loading everything.

## Contrasts with

- [Fine-Tuning](./fine-tuning.md) - an alternative way to give a model durable knowledge; the wiki keeps knowledge external, editable, and inspectable rather than baked into weights.
- [When RAG Is Dead](./when-rag-is-dead.md) - the navigational, index-plus-links model sidesteps embedding-based retrieval entirely.

## Implemented by

- [Google](../entities/organizations/google.md) - published the Open Knowledge Format (OKF), the open standard for producing and consuming these wikis.
- [Redis](../entities/tools/redis.md) - a store that context-retriever layers wiki-like metadata and structure on top of.
- [Claude Code](../entities/tools/claude-code.md) - the harness used to build a self-evolving memory system on top of the LLM knowledge-base pattern.

## Related

- [Andrej Karpathy](../entities/people/andrej-karpathy.md) - originated the LLM wiki idea that this pattern is named for.
- [Second Brain](./second-brain.md) - a personal knowledge system the LLM wiki naturally powers.
- [Self-Evolving Memory](./self-evolving-memory.md) - the wiki as a living store an agent updates over time.
- [Memory Systems](./memory-systems.md) - the broader family of ways agents persist and recall knowledge.
- [Knowledge Graphs](./knowledge-graphs.md) - an alternative structured representation of the same external knowledge.
- [Context Engineering](./context-engineering.md) - the wiki exists to feed an agent exactly the right context.
- [Model Context Protocol (MCP)](./mcp.md) - a common way agents actually reach into a knowledge base at query time.
- [Validation](./validation.md) - conformance checks (like OKF linting) keep the wiki's links and metadata honest.

## Sources

- [I Built Self-Evolving Claude Code Memory w/ Karpathy's LLM Knowledge Bases](../sources/i-built-self-evolving-claude-code-memory-w-karpathys-llm-knowledge-bases.md) - "[0:00:29] using LLM to build personal knowledge bases for various topics of research interest. So taking external information bringing it into our own system and organizing it in the best way for agents to query"
- [I Built Self-Evolving Claude Code Memory w/ Karpathy's LLM Knowledge Bases](../sources/i-built-self-evolving-claude-code-memory-w-karpathys-llm-knowledge-bases.md) - "[0:02:22] That brings us to the compiler analogy. This is the simplest way to explain everything that he's built... the way that we're handling knowledge is very similar to how we take source code all the way into a final application"
- [Finally, an Open Standard for the Karpathy LLM Wiki is HERE](../sources/finally-an-open-standard-for-the-karpathy-llm-wiki-is-here.md) - "[0:02:06] We need a standard so that everyone's building wikis in the same way so that we can share them freely. And so that is what Google has released here with their open knowledge format."
- [Finally, an Open Standard for the Karpathy LLM Wiki is HERE](../sources/finally-an-open-standard-for-the-karpathy-llm-wiki-is-here.md) - "[0:03:10] There are two things that they're standardizing here. The first is how we are organizing information like our entity documents and our concepts. And then the second standardization is the exact fields that we're going to have in our metadata."
- [I Love the Karpathy LLM Wiki but it Doesn't Scale. Here's What Does.](../sources/i-love-the-karpathy-llm-wiki-but-it-doesnt-scale-heres-what-does.md) - "[0:00:14] typically you'll have something like a Karpathy LLM Wiki for your organization. You have your index documents with your tagging and categorization and all of your entities."
- [I Love the Karpathy LLM Wiki but it Doesn't Scale. Here's What Does.](../sources/i-love-the-karpathy-llm-wiki-but-it-doesnt-scale-heres-what-does.md) - "[0:08:48] that's one of the big things that context retriever does on top of Redis is it provides that structure. It's kind of like the metadata in a Karpathy LLM wiki."
- [ChatGPT Teaches the Secrets to Financial Freedom!?](../sources/chatgpt-teaches-the-secrets-to-financial-freedom.md) - "[0:00:23] you can take a book all of the advice in that book and you can turn it into a mentor for you giving it your unique circumstances"
