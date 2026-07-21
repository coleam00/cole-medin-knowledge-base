---
type: concept
title: "Self-Reflective RAG"
description: "A RAG pattern where the agent evaluates its own retrieved context and re-queries or researches further until it has what it needs to answer well."
tags: [rag, agents, self-reflection, retrieval]
videos: [every-rag-strategy-explained-in-13-minutes-no-fluff, you-have-to-try-agentic-rag-with-deepseek-r1-insane-results, claude-computer-use-boltnew-the-ultimate-ai-coding-combo, ai-agents-the-future-of-ai-or-a-passing-fad]
created: 2026-07-21
updated: 2026-07-21
---

# Self-Reflective RAG

Self-reflective RAG adds a grading loop to retrieval: after fetching context, the agent judges whether that context is actually good enough to answer, and if not, it searches again with a better query. Cole spells out the mechanism: "we call upon a large language model given the chunks and the question to produce some kind of grade like maybe on a 1 through five scale and if it's less than three for example then we're going to call the rag tool again with a refined search" (every-rag-strategy, 0:10:14). Instead of trusting the first retrieval blindly, the system inspects it and decides whether to accept, retry, or dig deeper.

## How it works

The pattern layers a critic over the retrieval loop. A grading model scores the retrieved chunks against the question; a low score triggers another pass. The refined query is not a blind retry, the reflection produces a better search: "we can actually return back to our primary llm a better query for it to go through this Loop because we have that with small agents to then try again with a better query for rag" (deepseek-r1, 0:11:54). Pushed further, the agent researches to assist itself, "having AI even researching to assist itself" (computer-use-boltnew, 0:00:00), for example having one model "research the web on library documentation, craft a beautiful prompt to then feed it into another LLM" (computer-use-boltnew, 0:09:37).

The grading step is a specific instance of a general evaluator pattern Cole describes for agent outputs: "instead of sending it right back to the user it sends it to a second model with a separate prompt for AI evaluation so you define the rules here of what makes the response good or bad" (ai-agents-fad, 0:06:12), and on a fail it "will go back to the first model to regenerate the response probably providing feedback as well" (ai-agents-fad, 0:06:44). Self-reflective RAG applies that evaluate-and-retry loop specifically to retrieved context.

## Builds on

- [Retrieval-Augmented Generation (RAG)](./rag.md) is the base pipeline the reflection loop wraps.
- [Agentic RAG](./agentic-rag.md) is the broader family; self-reflective RAG is the variant where the agent's reasoning is turned on its own retrieved context.

## Related

- [Separate Reviewer](./separate-reviewer.md) is the general architecture behind the grading step: a second model with its own prompt judges the first model's work.
- [What Is an AI Agent](./what-is-an-ai-agent.md) grounds why this is agentic; the loop, tool use, and self-directed retries are what make it more than a one-shot lookup.
- [Computer Use](./computer-use.md) extends the same idea to letting the model research the open web to fill its own gaps.

## Sources

- [Every RAG Strategy Explained in 13 Minutes (No Fluff)](../sources/every-rag-strategy-explained-in-13-minutes-no-fluff.md) - "[0:10:14] we call upon a large language model given the chunks and the question to produce some kind of grade like maybe on a 1 through five scale and if it's less than three for example then we're going to call the rag tool again with a refined search"
- [You HAVE to Try Agentic RAG with DeepSeek R1 (Insane Results)](../sources/you-have-to-try-agentic-rag-with-deepseek-r1-insane-results.md) - "[0:11:54] we can actually return back to our primary llm a better query for it to go through this Loop because we have that with small agents to then try again with a better query for rag"
- [AI Agents: The Future of AI or a Passing Fad?](../sources/ai-agents-the-future-of-ai-or-a-passing-fad.md) - "[0:06:12] instead of sending it right back to the user it sends it to a second model with a separate prompt for AI evaluation so you define the rules here of what makes the response good or bad"
- [Claude Computer Use + Bolt.new - The ULTIMATE AI Coding Combo?!](../sources/claude-computer-use-boltnew-the-ultimate-ai-coding-combo.md) - "[0:00:00] we're going to be able to be hands off the wheel having AI even researching to assist itself which is kind of what we're seeing here so a glimpse into the future"
