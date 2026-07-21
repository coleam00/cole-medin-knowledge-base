---
type: entity
subtype: tool
title: "Perplexity"
description: "AI-powered deep research search engine Cole uses daily to research new LLMs, frameworks, and AI tech."
resource: "https://www.perplexity.ai"
tags: [search, retrieval]
videos: [how-id-learn-ai-agents-fast-if-i-had-to-start-over-full-roadmap]
created: 2026-07-21
updated: 2026-07-21
---

# Perplexity

Perplexity is an AI-native search engine that answers a question by running the searches itself, reading what comes back, and returning a synthesized, cited briefing instead of a page of links. Cole names it exactly that way while walking through the handful of off-the-shelf tools he opens every day: "The last one that I'll show right now is Perplexity. This is a deep research tool that I'll use all the time" [0:04:17]. The job it does for him is narrow and constant, which is keeping current. When new AI tech ships, a new model or a new framework he wants to understand before committing to it, Perplexity is the first surface he points at the problem.

That makes it the human-facing counterpart to the retrieval machinery he builds for agents. It is [Retrieval-Augmented Generation (RAG)](../../concepts/rag.md) as a product: the model is not answering from weights alone, it is grounding an answer in freshly fetched sources, and the multi-step query-read-refine behavior behind "deep research" is [Agentic Search](../../concepts/agentic-search.md) running on Cole's behalf rather than inside a system he wrote. Understanding the pattern from the consumer side is part of why he recommends the tool while learning: you feel what good retrieval produces before you try to engineer it.

Perplexity sits in the phase-one toolkit of the [AI Agent Learning Roadmap](../../concepts/ai-agent-learning-roadmap.md), alongside [Claude Desktop](./claude-desktop.md) for quick LLM conversations, [Aqua Voice](./aqua-voice.md) for voice input, and a notes app for capture. Cole is deliberate that the list is illustrative, not prescriptive. The lesson attached to that whole tool tour is [Capabilities Over Tools](../../concepts/capabilities-over-tools.md): learn the capability of researching a new technology quickly, because the specific product providing it may be irrelevant next month.

## Realizes

- [Agentic Search](../../concepts/agentic-search.md) - the iterative search-read-refine loop, run as a product for a human instead of as a tool inside an agent.
- [Retrieval-Augmented Generation (RAG)](../../concepts/rag.md) - answers grounded in retrieved live sources rather than model weights alone.

## Contrasts with

- [Brave Search API](./brave-search.md) - the web-search capability Cole wires into agents as a tool; Perplexity is the one he drives himself, deeper but slower.
- [ChatGPT](./chatgpt.md) - a general chat assistant, where Perplexity is search-first and citation-first.
- [Claude Desktop](./claude-desktop.md) - his go-to for bouncing ideas off an LLM, while Perplexity is for researching things the model has not seen.

## Related

- [AI Agent Learning Roadmap](../../concepts/ai-agent-learning-roadmap.md) - the phase-one stage where these daily-driver tools appear.
- [Capabilities Over Tools](../../concepts/capabilities-over-tools.md) - the explicit lesson Cole attaches to this exact tool list.
- [Semantic Search](../../concepts/semantic-search.md) - the retrieval primitive underneath AI-native search products.
- [Model Selection](../../concepts/model-selection.md) - staying current on new models is the research task Perplexity most often serves.
- [Context Engineering](../../concepts/context-engineering.md) - a research briefing is a compressed, high-signal input for whatever you build next.
- [Aqua Voice](./aqua-voice.md) - the voice-to-text layer Cole uses to drive tools like this quickly.

## Sources

- [How I'd Learn AI Agents FAST if I Had to Start Over (Full Roadmap)](../../sources/how-id-learn-ai-agents-fast-if-i-had-to-start-over-full-roadmap.md) - "[0:04:17] The last one that I'll show right now is Perplexity. This is a deep research tool that I'll use all the time."
