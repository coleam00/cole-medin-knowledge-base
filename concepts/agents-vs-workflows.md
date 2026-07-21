---
type: concept
title: "Agents vs. Workflows"
description: "An agent lets the LLM non-deterministically control which tools run and how often to reach a goal, whereas a workflow chains a fixed sequence of steps."
tags: [workflows, non-determinism, when-to-build, automation]
videos: [how-id-learn-ai-agents-fast-if-i-had-to-start-over-full-roadmap, google-anthropic-and-openais-guides-to-ai-agents-all-in-18-minutes, are-you-building-real-ai-agents-or-just-using-llms]
created: 2026-07-21
updated: 2026-07-21
---

# Agents vs. Workflows

The line between an agent and a workflow is who is in control of the flow. A workflow is a fixed chain of steps you author; an agent hands that control to the model. "There's workflows which is where you have a few llm calls chained together and really what we think an agent is is where you're letting the llm decide sort of how many times to run." [0:03:04] The distinguishing property is non-determinism: "the key word that I apply to this is nondeterministic and what I mean by that is we don't actually know exactly what is going to happen in a workflow when an agent is controlling it." [0:01:44] That freedom is what the [agent loop](./agent-loop.md) provides, and it is exactly what a workflow gives up in exchange for predictability.

This is a genuine paradigm shift, not a spectrum quibble: "learning AI agents versus traditional automations. It's a whole paradigm shift when we add this extra reasoning into our automations." [0:01:42] But the extra reasoning is a trade, not a free upgrade: "there's a lot more power but also unpredictability that comes with this." [0:02:01] The important subtlety is that putting an LLM inside a flow does not make it an agent, "there is a big difference between actual AI agents and a workflow that just happens to have an llm inside of it." [0:00:17] If the model cannot choose which tools run or how many times to loop, it is still a workflow.

Choosing between them is a design decision, and defaulting to "agent" is often over-engineering. Build an agent "when you need that complex decision-m around the tools... you also want to build agents when brittle logic is present." [0:04:29] Otherwise stay with a workflow: "if your automations are very predictable and stable logic is enough, like just regular code or regular workflow automation, then you don't want to overengineer for an agent." [0:05:04]

## Contrasts with

- [The Agent Loop (Reason-Act-Observe)](./agent-loop.md) - the non-deterministic loop is the agent side of this contrast.
- [Deterministic Workflows](./deterministic-workflows.md) - the fixed-sequence side, chosen when logic is predictable and stable.
- [The Seven Node Blueprint](./seven-node-blueprint.md) - Cole's mental model that decomposes any AI agent into seven reusable node types (LLM, tool, control, memory, guardrail, fallback, user input) you build individually and combine like Lego bricks.

## Related

- [Tool Use](./tool-use.md) - an agent is defined by controlling which tools run and how often.
- [Workflow as a Tool](./workflow-as-a-tool.md) - Packaging an arbitrary multi-step automation workflow as a single callable agent tool, so the agent inherits the automation platform's hundreds of integrations as capabilities.
- [Human in the Loop](./human-in-the-loop.md) - a checkpoint that reintroduces control into an otherwise autonomous agent.
- [Validation](./validation.md) - non-determinism raises the bar for testing agent behavior.

## Tools

- [n8n](../entities/tools/n8n.md) - supports both plain workflow automations and agent nodes, making the trade-off explicit.
- [LangGraph](../entities/tools/langgraph.md) - lets you draw the line yourself, from fixed edges to model-routed loops.

## Sources

- [Are You Building REAL AI Agents or Just Using LLMs?](../sources/are-you-building-real-ai-agents-or-just-using-llms.md) - "[0:01:44] the key word that I apply to this is nondeterministic and what I mean by that is we don't actually know exactly what is going to happen in a workflow when an agent is controlling it"
- [Google, Anthropic, and OpenAI's Guides to AI Agents ALL in 18 Minutes](../sources/google-anthropic-and-openais-guides-to-ai-agents-all-in-18-minutes.md) - "[0:05:04] if your automations are very predictable and stable logic is enough, like just regular code or regular workflow automation, then you don't want to overengineer for an agent"
- [How I'd Learn AI Agents FAST if I Had to Start Over (Full Roadmap)](../sources/how-id-learn-ai-agents-fast-if-i-had-to-start-over-full-roadmap.md) - "[0:01:42] learning AI agents versus traditional automations. It's a whole paradigm shift when we add this extra reasoning into our automations"
