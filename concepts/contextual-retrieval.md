---
type: concept
title: "Contextual Retrieval"
description: "Prepending LLM-generated context to each chunk before embedding so retrieval understands where the chunk sits in the larger document."
tags: [rag, chunking, contextual-embeddings, retrieval-quality]
videos: [every-rag-strategy-explained-in-13-minutes-no-fluff, turn-any-file-into-llm-knowledge-in-seconds, all-the-best-rag-strategies-in-one-mcp-for-ai-coding-assistants, the-easiest-possible-strategy-for-accurate-rag-step-by-step-guide, i-built-the-ultimate-rag-mcp-server-for-ai-coding-better-than-context7]
created: 2026-07-21
updated: 2026-07-21
---

# Contextual Retrieval

"we're using a large language model to enrich each chunk with information that we put at the start that describes how the chunk fits with the rest of the document" [0:05:37]. Contextual retrieval (also called contextual embeddings) fixes a core weakness of naive chunking: a chunk ripped out of a long document loses the surrounding context that gives it meaning. The fix is to run an LLM pass over every chunk that writes a short preface situating it, then embed the prefaced text so the vector captures both the chunk and its place in the whole. It is "a rag strategy that was introduced by the anthropic team."

## How it works

For each chunk you send the LLM the entire document plus that chunk and ask it "to give some more context around this chunk like where does it fit within the document?" The generated one-or-two-sentence preface is prepended, separated from the raw chunk (Cole uses a triple-dash delimiter), and the combined text is what gets embedded. The gains are outsized for the effort: "it's crazy how even just like one or two sentences that we add at the start of each chunk, it improves our results significantly," and per Anthropic's own tests it "does reduce failure rate for rag by up to 35%."

The obvious cost is running a prompt per chunk over the full document, which is expensive at scale. The mitigation is [prompt caching](./prompt-caching.md): "you can use prompt caching to make it so that it's not that expensive even though you have to put in the whole document." A lighter-weight variant simply folds in existing structure, "including things like the headings and subheadings that we have in the markdown," as cheap contextualization.

## Builds on

- [Chunking](./chunking.md) - contextual retrieval is a chunk-preparation strategy; it enriches chunks rather than replacing the split.
- [Vector Embeddings](./vector-embeddings.md) - the prefaced chunk is what gets embedded, so context flows into the vector itself.

## Contrasts with

- [Late Chunking](./late-chunking.md) - an alternative that preserves whole-document context by embedding first and chunking after, instead of prepending generated text.

## Related

- [Context-Aware Chunking](./context-aware-chunking.md) - a sibling technique for keeping chunks coherent with their surroundings.
- [Retrieval-Augmented Generation (RAG)](./rag.md), [Traditional RAG](./traditional-rag.md) - the pipeline this strategy plugs into to raise accuracy.
- [Agentic RAG](./agentic-rag.md) - often stacked together as complementary accuracy improvements.
- [Prompt Caching](./prompt-caching.md) - what makes the per-chunk LLM pass affordable.

## Tools

- [Anthropic](../entities/organizations/anthropic.md) - introduced contextual embeddings / contextual retrieval.
- [Archon](../entities/tools/archon.md) - implements contextual embeddings as one of its selectable RAG strategies.
- [GPT-4.1 Nano](../entities/tools/gpt-4-1-nano.md) - OpenAI's smallest, cheapest model in the GPT-4.1 line, used for the per-chunk context-generation call in contextual retrieval because the task needs almost no reasoning power.

## Sources

- [Every RAG Strategy Explained in 13 Minutes (No Fluff)](../sources/every-rag-strategy-explained-in-13-minutes-no-fluff.md) - "[0:05:37] we're using a large language model to enrich each chunk with information that we put at the start that describes how the chunk fits with the rest of the document"
- [The EASIEST Possible Strategy for Accurate RAG (Step by Step Guide)](../sources/the-easiest-possible-strategy-for-accurate-rag-step-by-step-guide.md) - "[0:22:27] contextual embedding which from anthropics tests does reduce failure rate for rag by up to 35%"
- [All the BEST RAG Strategies in ONE MCP for AI Coding Assistants](../sources/all-the-best-rag-strategies-in-one-mcp-for-ai-coding-assistants.md) - "[0:08:41] you're going to run a prompt for every single chunk... that prompt is going to preface your chunk with extra context that tells the LLM how this chunk fits in with the rest of the document"
- [Turn ANY File into LLM Knowledge in SECONDS](../sources/turn-any-file-into-llm-knowledge-in-seconds.md) - "[0:17:18] Contextualize basically just means we're also including things like the headings and subheadings that we have in the markdown as well."
- [I Built the Ultimate RAG MCP Server for AI Coding (Better than Context7)](../sources/i-built-the-ultimate-rag-mcp-server-for-ai-coding-better-than-context7.md) - "[0:15:52] We could implement things like contextual retrieval which was released recently by Anthropic or late chunking or agentic rag like I've covered on my channel."
