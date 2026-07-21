---
type: source
title: "My Top 20 Lessons from Building 100s of AI Agents (Super Actionable)"
description: "The hardest problem in building AI agents is non-determinism and hallucination, so nearly every practical lesson is really a strategy for reducing or catching hallucinations."
youtube_id: OFfwN23hR8U
url: https://www.youtube.com/watch?v=OFfwN23hR8U
slug: my-top-20-lessons-from-building-100s-of-ai-agents-super-actionable
published: 2025-08-20
duration: "1:03:34"
recency_rank: 74
raw: "../raw/my-top-20-lessons-from-building-100s-of-ai-agents-super-actionable.md"
tags: [ai-agents, hallucination, best-practices]
created: 2026-07-21
updated: 2026-07-21
---

# My Top 20 Lessons from Building 100s of AI Agents (Super Actionable)

In a Dynamous community live event, Cole Medin condenses lessons from building hundreds of AI agents into 20 actionable tips, organized around the four components of an agent: the agent program and system prompt, the LLM, the tools, and the memory system. He frames the central challenge as hallucination and non-determinism. Unlike traditional software, the same input can yield a different output, and an agent that works 50 times can botch the 51st. The through-line of the talk is that most good practices exist to reduce or catch those hallucinations.

At the high level he argues you should use AI to save time rather than replace yourself entirely (draft emails instead of auto-sending), invest heavily in planning and prototyping before implementation, and beware the hallucination explosion, where chaining agents that each succeed 95 percent of the time compounds down to roughly 86 percent system reliability. His hallucination-reduction toolkit includes input and output guardrails (lightweight LLM checks before and after the agent), specialized agents behind an orchestrator, and concrete examples in prompts. For system prompts specifically: avoid negative instructions (LLMs drop the "do not"), avoid contradictions, and version your prompts like code. For LLMs: swapping models is risky even when the new model is better, your favorite model is not always best for every task, and watch context length, since the system prompt is first to fall off.

On memory, he notes that short-term memory tends to repeat earlier hallucinations (a reason to start fresh conversations often), that long-term memory is just another RAG so RAG strategies like query expansion and reranking apply, and that you should store tool calls and their responses in conversation history so the agent can re-reference retrieved data. He closes with the anatomy of a good tool: descriptive, framework-agnostic tool descriptions, examples for complex parameters, wrapping tools in try/except and returning the error to the agent, and returning only the data the LLM needs (well-formatted, ideally markdown) rather than raw API metadata.

## Concepts covered

- [Human in the Loop](../concepts/human-in-the-loop.md)
- [Deterministic Workflows](../concepts/deterministic-workflows.md)
- [Planning with AI](../concepts/planning-with-ai.md)
- [Guardrails](../concepts/guardrails.md)
- [Subagents Pattern](../concepts/subagents-pattern.md)
- [Few-Shot Prompting](../concepts/few-shot-prompting.md)
- [Avoid Negative Instructions](../concepts/avoid-negative-instructions.md)
- [Reduce Assumptions](../concepts/reduce-assumptions.md)
- [Prompt Versioning](../concepts/prompt-versioning.md)
- [Model Selection](../concepts/model-selection.md)
- [Context Window Limits](../concepts/context-window-limits.md)
- [Memory Systems](../concepts/memory-systems.md)
- [Tool Design](../concepts/tool-design.md)

## Entities

- [Cole Medin](../entities/people/cole-medin.md)
- [Dynamous](../entities/organizations/dynamous.md)
- [Windsurf](../entities/tools/windsurf.md)
- [n8n](../entities/tools/n8n.md)
- [Pydantic AI](../entities/tools/pydantic-ai.md)
- [Langfuse](../entities/tools/langfuse.md)
- [Supabase](../entities/tools/supabase.md)
- [MCP (Model Context Protocol)](../entities/tools/mcp.md)
- [Claude](../entities/tools/claude.md)
- [Google Gemini 2.0 Flash](../entities/tools/gemini.md)
- [bolt.new](../entities/tools/bolt-new.md)

## Key moments

- **[0:02:15]** Definition of an AI agent and its four components: agent program, LLM, tools, memory
- **[0:05:40]** Hallucinations framed as the core challenge; non-determinism explained
- **[0:08:16]** Lesson 1: use AI to save time, not replace you (draft emails, don't auto-send)
- **[0:09:57]** Lesson 2: don't skimp on planning and prototyping
- **[0:12:00]** Lesson 3: the hallucination explosion / compounding non-determinism (95% x 95% x 95% = 86%)
- **[0:15:55]** Lesson 4: AI agent guardrails (input and output) with the travel-planner example
- **[0:19:17]** Lesson 5: specialized agents behind an orchestrator
- **[0:21:20]** Lesson 6: examples, examples, examples in the system prompt
- **[0:23:29]** System prompt lesson: avoid negatives (LLMs drop the 'do not')
- **[0:25:20]** System prompt lesson: avoid contradictions (calendar accommodating vs rigid example)
- **[0:28:44]** System prompt lesson: version your prompts (Langfuse / git)
- **[0:30:10]** LLM lesson: swapping models is dangerous even when the new model is better
- **[0:33:26]** LLM lesson: watch context length; system prompt is first to fall off
- **[0:35:38]** Memory lesson: previous hallucinations get repeated in the same conversation
- **[0:37:36]** Memory lesson: long-term memory is just another RAG
- **[0:38:58]** Memory lesson: include tool calls and responses in conversation history
- **[0:41:20]** Tools: the anatomy of a good tool begins (descriptions, examples, error handling, minimal output)

## Transcript

[Raw transcript](../raw/my-top-20-lessons-from-building-100s-of-ai-agents-super-actionable.md)

## Sources

- [My Top 20 Lessons from Building 100s of AI Agents (Super Actionable)](./my-top-20-lessons-from-building-100s-of-ai-agents-super-actionable.md) - "[0:12:00] Lesson 3: the hallucination explosion / compounding non-determinism (95% x 95% x 95% = 86%)"
