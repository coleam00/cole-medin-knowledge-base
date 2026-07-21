---
type: entity
subtype: tool
title: "OpenAI o3-mini"
description: "OpenAI's small reasoning model, used as Archon's reasoner to write the scope document before the coder agent builds, and the head-to-head rival to DeepSeek R1 for coding."
resource: "https://openai.com"
tags: [llm, model, reasoning-model, openai]
videos: [lets-settle-the-o3-mini-vs-r1-debate-for-coding-once-and-for-all, this-is-hands-down-the-best-way-to-build-ai-agents, you-have-to-try-agentic-rag-with-deepseek-r1-insane-results]
created: 2026-07-21
updated: 2026-07-21
---

# OpenAI o3-mini

o3-mini is OpenAI's small, fast [reasoning model](../../concepts/reasoning-models.md), released as a direct answer to DeepSeek: "open AI almost immediately fired back releasing 03 mini which is their next generation of their Advanced reasoning models" [0:00:00]. It arrived mid-production on Cole's channel, so it shows up twice over: once as the drop-in reasoner in his agent architectures, and once as the challenger in a head-to-head coding bake-off.

## The reasoner role

Cole's most durable use of o3-mini is structural rather than conversational. In [Archon](./archon.md) V2 he puts a reasoning model at the front of the graph: "using a reasoning llm at the start of the workflow something like deep seek R1 or open aai 03 mini and this guy is going to take the requirements from the user like the agent that they want to build and create a full scope document outlining everything that needs to be" built [0:19:46]. The scope document is then injected into the coder agent's [dynamic system prompt](../../concepts/dynamic-system-prompt.md), so a slow deliberate model does the [planning](../../concepts/planning-with-ai.md) once and a cheaper coder executes against it. o3-mini is the default there ("we're just going to be defaulting to 03 mini if nothing is specified"), swappable for a local reasoner. Same idea in his [agentic RAG](../../concepts/agentic-rag.md) build, where the reasoner slot takes whichever model you point it at: "grab the ID for our reasoning model like R1 or you could go use o03 mini cuz apparently that was just released I found out in the middle of recording this video" [0:07:02]. That interchangeability is the point: this is [reasoning model as a tool](../../concepts/reasoning-model-as-a-tool.md), not a hard dependency.

## Against DeepSeek R1

Cole ran o3-mini and [DeepSeek R1](./deepseek-r1.md) through identical builds in [bolt.diy](./bolt-diy.md) and scored them. The verdict splits cleanly: "03 is better for Speed and then raw functionality then R1 is better for UI" [0:18:28]. He frames the underlying difference architecturally, o3-mini being a dense Transformer against R1's [mixture of experts](../../concepts/mixture-of-experts.md), and warns the test is not an end-all comparison: o3-mini tends to be stronger on directed agent-style tasks, R1 on free-thinking logic and research. The practical read is a [model selection](../../concepts/model-selection.md) call, not a winner.

## Realizes

- [Reasoning Models](../../concepts/reasoning-models.md) - Models that produce explicit reasoning before answering, and when that extra thinking helps versus hurts.
- [Reasoning Model as a Tool](../../concepts/reasoning-model-as-a-tool.md) - A fast model drives the flow and calls a slow reasoning model on just the hard step.

## Contrasts with

- [DeepSeek R1](./deepseek-r1.md) - Open-source MIT-licensed reasoning LLM; the head-to-head rival that wins on UI while o3-mini wins on speed and raw functionality.
- [OpenAI o1](./o1.md) - The previous generation of OpenAI's reasoning models, which o3-mini supersedes on speed and price.

## Works with

- [Archon](./archon.md) - Cole's open-source AI command center, where o3-mini is the default reasoner that writes the scope document for the coder agent.
- [bolt.diy](./bolt-diy.md) - Open-source AI coding assistant used as the neutral test harness for the o3-mini versus R1 comparison.
- [Pydantic AI](./pydantic-ai.md) - The framework the reasoner agent is defined in, with the model read from an environment variable.
- [LangGraph](./langgraph.md) - Orchestrates the reasoner node, coder node, and shared state that carries the scope forward.
- [OpenRouter](./openrouter.md) - Gateway used to reach the rival model while o3-mini is called directly through the OpenAI API.

## Related

- [Model Selection](../../concepts/model-selection.md) - Choosing the right LLM per task by trading off quality, speed, and cost.
- [Mixture of Experts](../../concepts/mixture-of-experts.md) - The architecture difference that explains why two similar-looking reasoning LLMs behave differently.
- [Planning with AI](../../concepts/planning-with-ai.md) - Producing a reviewed blueprint before implementation, which the scope document realizes.
- [Agentic RAG](../../concepts/agentic-rag.md) - Retrieval as a tool, with a reasoning model deciding what to look up and why.
- [Agents That Build Agents](../../concepts/agents-that-build-agents.md) - The meta-agent pattern Archon implements on top of this reasoner-plus-coder split.
- [Graph-Based Agent Workflows](../../concepts/langgraph-nodes-edges-state.md) - Nodes, edges, and shared state, the structure the reasoner output flows through.

## Sources

- [Let's Settle the o3-mini Vs. R1 Debate for Coding ONCE and for ALL](../../sources/lets-settle-the-o3-mini-vs-r1-debate-for-coding-once-and-for-all.md) - "[0:00:00] open AI almost immediately fired back releasing 03 mini which is their next generation of their Advanced reasoning models"
- [Let's Settle the o3-mini Vs. R1 Debate for Coding ONCE and for ALL](../../sources/lets-settle-the-o3-mini-vs-r1-debate-for-coding-once-and-for-all.md) - "[0:18:28] 03 is better for Speed and then raw functionality then R1 is better for UI"
- [This is Hands Down the BEST Way to Build AI Agents](../../sources/this-is-hands-down-the-best-way-to-build-ai-agents.md) - "[0:19:46] using a reasoning llm at the start of the workflow something like deep seek R1 or open aai 03 mini and this guy is going to take the requirements from the user like the agent that they want to build and create a full scope document"
- [You HAVE to Try Agentic RAG with DeepSeek R1 (Insane Results)](../../sources/you-have-to-try-agentic-rag-with-deepseek-r1-insane-results.md) - "[0:07:02] grab the ID for our reasoning model like R1 or you could go use o03 mini cuz apparently that was just released I found out in the middle of recording this video"
