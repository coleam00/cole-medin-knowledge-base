---
type: entity
subtype: tool
title: "Berkeley Function Calling Leaderboard"
description: "A public benchmark that ranks LLMs on function-calling accuracy using tasks meant to represent real agent and enterprise workflows."
tags: [observability, validation, function-calling, agents, tools]
videos: [new-llama-3-model-beats-gpt-and-claude-with-function-calling]
created: 2026-07-21
updated: 2026-07-21
---

# Berkeley Function Calling Leaderboard

The Berkeley Function Calling Leaderboard is a public benchmark that scores models on one narrow but decisive capability: how reliably they pick the right function, with the right arguments, from a set of tool definitions. It is the scoreboard Cole reaches for when a model claims agent-grade tool use - "The way that they're benchmarking this is with the Berkeley function calling leaderboard" [0:00:48]. Function calling is the hinge between a chatbot and an agent, so a leaderboard measuring it is effectively a leaderboard of who can *act*.

Its moment in the catalog is Groq's function-calling fine-tunes of [Llama](./llama.md) 3 taking the top spots: the 70B at roughly 90% accuracy at number one, the 8B at number three, ahead of every GPT model and every Claude model except [Claude 3.5 Sonnet](./claude-3-5-sonnet.md). Cole opens on the significance: "for the very first time ever the best large language model for function calling is an open source model that you can run locally" [0:00:00]. That is the leaderboard doing its job - flagging that the frontier for this specific capability had moved to open weights.

What he does next is the more instructive part. Rather than accept the ranking, he re-tests it against a real agent: a [LangChain](./langchain.md) app driving [Asana](./asana.md) through a tool layer, where "we have a section that defines all the tools that we're giving the agent to interact with a SAA on my behalf to manage projects and to manage tasks" [0:03:44]. [GPT-4o](./gpt-4o.md) runs the multi-step workflow cleanly; the top-ranked open model completes it but asks the user to resolve what date "Friday" is, fails to look up task IDs on its own, and sometimes updates the wrong task. His conclusion is "almost as good," with the gap attributed to handling many tokens rather than to picking functions.

That is the honest read on this benchmark: it measures function selection well, not the surrounding competence an agent needs. Treat a leaderboard position as a shortlist signal, then validate on your own tool surface.

## Realizes

- [Agent Evaluation](../../concepts/agent-evaluation.md) - a standardized, comparable measure of the capability agents live or die on.
- [Tool Calling](../../concepts/tool-use.md) - the exact behavior being scored.
- [Model Selection](../../concepts/model-selection.md) - the shortlist input when choosing which model drives an agent.

## Contrasts with

- [Real-World Coding Benchmarks](../../concepts/coding-benchmarks.md) - Cole's preferred check is running your own workload, which is exactly what he does after reading the leaderboard.
- [Validation](../../concepts/validation.md) - a rank is a claim; validation is proving it on your tools.

## Works with

- [Llama](./llama.md) - the open model whose fine-tunes topped the board.
- [GPT-4o](./gpt-4o.md) - the proprietary baseline he benchmarks against by hand.
- [Claude](./claude.md) - the other proprietary family the board ranks.
- [LangChain](./langchain.md) - the framework that makes swapping the ranked models a one-line change.
- [Asana](./asana.md) - the real tool surface used for the follow-up test.

## Related

- [Local LLMs as Agents](../../concepts/local-llms-as-agents.md) - the payoff if an open model really is top of the board.
- [Local & Self-Hosted AI](../../concepts/local-ai.md) - why open-weight parity on function calling matters beyond bragging rights.
- [Open-Source & Local AI Coding](../../concepts/open-source-ai-coding.md) - the broader closing-the-gap story.
- [Tool Design](../../concepts/tool-design.md) - clean tool definitions raise every model's score before any swap does.
- [Docstrings as Tool Descriptions](../../concepts/docstrings-as-tool-descriptions.md) - the practical lever on function-calling accuracy in your own code.
- [Structured Outputs](../../concepts/structured-outputs.md) - the adjacent capability of emitting well-formed arguments.
- [Fine-Tuning](../../concepts/fine-tuning.md) - how Groq bought the top rank in the first place.

## Sources

- [New Llama 3 Model BEATS GPT and Claude with Function Calling!?](../../sources/new-llama-3-model-beats-gpt-and-claude-with-function-calling.md) - "[0:00:48] The way that they're benchmarking this is with the Berkeley function calling leaderboard"
- [New Llama 3 Model BEATS GPT and Claude with Function Calling!?](../../sources/new-llama-3-model-beats-gpt-and-claude-with-function-calling.md) - "[0:00:00] for the very first time ever the best large language model for function calling is an open source model that you can run locally"
- [New Llama 3 Model BEATS GPT and Claude with Function Calling!?](../../sources/new-llama-3-model-beats-gpt-and-claude-with-function-calling.md) - "[0:03:44] we have a section that defines all the tools that we're giving the agent to interact with a SAA on my behalf to manage projects and to manage tasks"
