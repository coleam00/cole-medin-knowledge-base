---
type: entity
subtype: tool
title: "Auto-GPT"
description: "Open-source experiment that wraps GPT-4 in an autonomous goal-decomposition-and-execution loop with tool use and optional vector-database memory; the first widely known autonomous agent."
resource: "https://github.com/Significant-Gravitas/AutoGPT"
tags: [agent-framework, sdk]
videos: [chatgpt-is-the-gift-that-keeps-on-giving-introducing-auto-gpt]
created: 2026-07-21
updated: 2026-07-21
---

# Auto-GPT

Auto-GPT is the project that first made "autonomous agent" a mainstream idea. Cole's 2023 definition is the cleanest one in the catalog: "what Auto GPT is is it is an experiment a program that somebody has created and a lot of people have contributed to where it operates autonomously" [0:00:37] - the "auto" being short for autonomous. You give it a role and a handful of goals; it generates its own steps, executes them, observes the result, and continues without being re-prompted. That is [the agent loop](../../concepts/agent-loop.md) in its earliest popular packaging, and it is why the video frames it as the "sparks of AGI."

It is community software, not a product: "all of the code for auto GPT is stored in this GitHub repository right here it's open source" [0:02:11]. Setup is Python 3.8+, an OpenAI API key for [GPT-4](./gpt-4.md), a git clone, and renaming the .env template. Two optional add-ons are architecturally interesting because they prefigure standard agent components - a [Pinecone](./pinecone.md) key gives it long-term memory through a vector database, and an [ElevenLabs](./elevenlabs.md) key lets it speak its reasoning aloud.

The behavior Cole demonstrates is the whole modern agent stack in embryo. The agent prints thoughts, reasoning, and a plan, then **self-criticizes** before acting. It browses the web, falls back to search when a page yields nothing (routing around the model's September 2021 [training cutoff](../../concepts/training-cutoff.md)), writes and refactors code, and finally writes a file of results. It also exposes the failure modes that still matter: it loops, it stays too general, and continuous mode is dangerous - so you run it step by step and approve each action, "so this way you can kind of oversee it and make sure it's not doing anything stupid." Human approval was a safety valve then and is a design principle now.

Cole's verdict is calibrated: experimental and imperfect, but "the start of something big." Read against the rest of the catalog, Auto-GPT is the origin point for everything from [Manus](./manus.md) to today's coding harnesses.

## Realizes

- [The Agent Loop (Reason-Act-Observe)](../../concepts/agent-loop.md) - decompose, act, observe, repeat, with no human turn in between.
- [What Is an AI Agent](../../concepts/what-is-an-ai-agent.md) - the first widely seen answer to the question.
- [The Core Components of an Agent](../../concepts/agent-core-components.md) - model, tools, memory, and a loop, all present in 2023.
- [Tool Calling](../../concepts/tool-use.md) - browsing, searching, file writes, and code execution as agent actions.
- [Memory Systems](../../concepts/memory-systems.md) - optional vector-database memory so goals survive across steps.
- [Self-Criticism Prompting](../../concepts/self-criticism-prompting.md) - the agent critiques its own plan before executing it.
- [Human in the Loop](../../concepts/human-in-the-loop.md) - step-by-step authorization instead of continuous mode.

## Works with

- [ChatGPT](./chatgpt.md) - the model family Auto-GPT drives, paid through the API rather than the chat UI.
- [GPT-4](./gpt-4.md) - the reasoning engine behind each step.
- [Pinecone](./pinecone.md) - optional vector database supplying long-term memory.
- [ElevenLabs](./elevenlabs.md) - optional voice output for the agent's thoughts.
- [Python](./python.md) and [Git](./git.md) - the entire installation prerequisite list.

## Contrasts with

- [Manus](./manus.md) - the same autonomous-agent premise, delivered years later as a polished hosted product.
- [Archon](./archon.md) - autonomy re-framed around a shared knowledge base and managed tasks rather than an open-ended goal list.
- [The Ralph Loop](../../concepts/the-ralph-loop.md) - modern unattended looping, deliberately scoped and validated where Auto-GPT ran open-ended.

## Related

- [Agentic Coding](../../concepts/agentic-coding.md) - the discipline that grew out of this experiment.
- [The Evolution of AI Coding](../../concepts/the-evolution-of-ai-coding.md) - Auto-GPT is the early waypoint on that arc.
- [Long-Running Agents](../../concepts/long-running-agents.md) - the looping-forever problem it surfaced first.
- [Effective Prompting](../../concepts/effective-prompting.md) - garbage in, garbage out, even when the agent writes its own prompts.

## Sources

- [ChatGPT is the GIFT that keeps on GIVING - Introducing Auto-GPT](../../sources/chatgpt-is-the-gift-that-keeps-on-giving-introducing-auto-gpt.md) - "[0:00:37] what Auto GPT is is it is an experiment a program that somebody has created and a lot of people have contributed to where it operates autonomously"
- [ChatGPT is the GIFT that keeps on GIVING - Introducing Auto-GPT](../../sources/chatgpt-is-the-gift-that-keeps-on-giving-introducing-auto-gpt.md) - "[0:02:11] all of the code for auto GPT is stored in this GitHub repository right here it's open source"
