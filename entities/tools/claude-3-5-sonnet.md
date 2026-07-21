---
type: entity
subtype: tool
title: "Claude 3.5 Sonnet"
description: "Anthropic's mid-2024 flagship model and the only LLM Cole could not break in his agentic stress test, making it his clear winner for multi-step tool-using workflows."
tags: [llm, model]
videos: [i-found-the-limits-of-the-most-popular-llms]
created: 2026-07-21
updated: 2026-07-21
---

# Claude 3.5 Sonnet

Claude 3.5 Sonnet is Anthropic's mid-2024 flagship, and in Cole's work it earns a very specific title: the only model he could not break. He set out to find the ceiling of each popular LLM by wiring one agent to three tool groups (a vector knowledge base, Google Drive CRUD, and Asana task management), swapping the underlying model with a single environment variable, and escalating request difficulty until something failed. Claude 3.5 Sonnet did not fail: "Claud 3.5 son it handled the most complicated request that I really have at this point" ([0:22:39](../../sources/i-found-the-limits-of-the-most-popular-llms.md)), and the verdict at the end is unambiguous - "we have a clear winner for agentic workflows and that is Claude 3.5 Sonet" ([0:31:32](../../sources/i-found-the-limits-of-the-most-popular-llms.md)).

What it was actually being tested on is worth stating precisely, because it is not a coding benchmark. The hardest request forced the agent to chain three systems in one shot: pull a specific day's meeting notes out of Drive, ingest them into the knowledge base, then mark complete every task in an Asana project that the notes said was done. That demands correct tool arguments across many calls, holding intermediate results in working state, and knowing when it is finished. The failure modes of the rivals map exactly onto those demands. [GPT-4o mini](./gpt-4o-mini.md) handled a lot but passed bad arguments to the mark-complete tool. A Groq-hosted [Llama](./llama.md) 3 function-calling fine-tune broke almost immediately on due dates, search formats, and file IDs. [GPT-4o](./gpt-4o.md) got roughly 90% of the way and then silently skipped one task, which is worse than failing loudly.

That is the durable lesson: raw benchmark quality and agentic reliability are different axes, and the second one is only visible when you run a real multi-step task and check the output rather than the transcript. Claude 3.5 Sonnet's dominance here also explains its gravitational pull elsewhere in the ecosystem - the AI app builders Cole uses, [Lovable](./lovable.md) and [bolt.new](./bolt-new.md), were both tuned around it.

## Part of

- [Claude](./claude.md) - Anthropic's model family; 3.5 Sonnet is the mid-2024 generation of it.

## Realizes

- [Model Selection](../../concepts/model-selection.md) - Choosing the right LLM per task; this test is Cole's method for making that choice empirically rather than by vibes.
- [The Agent Loop (Reason-Act-Observe)](../../concepts/agent-loop.md) - The cycle the model has to sustain across an unknown number of tool calls before deciding it is done.
- [Tool Calling](../../concepts/tool-use.md) - Invoking external functions and APIs, where argument correctness is the thing that actually separated the models.
- [Agent Evaluation](../../concepts/agent-evaluation.md) - Scoring agent behavior systematically; Cole floats turning this break-the-LLM process into an automated scored test suite.

## Contrasts with

- [GPT-4o](./gpt-4o.md) - Reached about 90% of the hard request and then silently missed a task, a quieter and more dangerous failure.
- [GPT-4o mini](./gpt-4o-mini.md) - Kept up until the final multi-step request, then passed malformed tool arguments.
- [Llama](./llama.md) - The Groq function-calling fine-tune that broke fastest, on due dates, search format, and file IDs.

## Works with

- [LangGraph](./langgraph.md) - The graph runtime hosting the call-model / call-tools / route cycle every model was tested inside.
- [Lovable](./lovable.md) - AI app builder optimized around Claude 3.5 Sonnet.
- [bolt.new](./bolt-new.md) - The other prompt-to-app platform tuned to the same model.

## Related

- [Agentic Workflow Engineering](../../concepts/agentic-workflow-engineering.md) - Designing repeatable multi-step AI workflows rather than one-shot prompts.
- [Real-World Coding Benchmarks](../../concepts/coding-benchmarks.md) - Why leaderboard scores and practical reliability diverge.
- [Validation](../../concepts/validation.md) - The design trick that made the test honest: no direct Drive-read tool, so any answer is provably sourced from RAG.

## Sources

- [I Found the Limits of the Most Popular LLMs](../../sources/i-found-the-limits-of-the-most-popular-llms.md) - "[0:22:39] Claud 3.5 son it handled the most complicated request that I really have at this point"
- [I Found the Limits of the Most Popular LLMs](../../sources/i-found-the-limits-of-the-most-popular-llms.md) - "[0:31:32] we have a clear winner for agentic workflows and that is Claude 3.5 Sonet"
