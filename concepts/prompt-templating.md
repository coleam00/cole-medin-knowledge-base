---
type: concept
title: "Prompt Variable Templating"
description: "Defining named variables (e.g. {{prompt}}, {{context}}) inside a node's prompt to create typed inputs the workflow can wire data into."
tags: [no-code, prompts]
videos: [turn-any-ai-agent-into-a-live-person-voice-chat-setup-in-minutes]
created: 2026-07-21
updated: 2026-07-21
---

# Prompt Variable Templating

Prompt variable templating is the practice of writing placeholder variables directly inside a node's prompt so the surrounding workflow can wire live data into them. In a [Visual Workflow Builder](./visual-workflow-builder.md), a prompt is not a static string; it is a template with named slots. As Cole demonstrates in Vector Shift, "you can Define parameters within these boxes here that give multiple different inputs available in this node" [0:04:54]. Each variable you declare becomes an actual input port on the node that upstream data can be dragged into.

The syntax is deliberately simple. "I'll use their syntax here which is with squiggly brackets so two s brackets and then prompt and then closing it out and then there we go we now have an input called prompt where I can drag the text into it" [0:05:11]. Typing `{{prompt}}` inside the text box materializes a `prompt` input on the node; the workflow author then connects a trigger's output, a retrieval result, or another node's response into that slot. The double-brace convention is shared across most no-code builders, so the mental model transfers between platforms.

Why it matters: templating is what turns a one-off prompt into a reusable, composable node. It separates the fixed instruction (the template text) from the variable payload (whatever the user said, whatever a knowledge base returned), which is the same separation that makes prompts maintainable in code. It is the no-code expression of [Effective Prompting](./effective-prompting.md): the template holds your carefully written instructions while the variables carry context in at runtime. When one of those variables is populated from retrieved documents, templating becomes the injection point for [Retrieval-Augmented Generation (RAG)](./rag.md), the retrieved chunks land in a `{{context}}` slot that the prompt wraps with instructions.

## Builds on

- [Effective Prompting](./effective-prompting.md) - the template text is where prompting discipline lives; variables just carry the payload.

## Related

- [Visual Workflow Builder](./visual-workflow-builder.md) - templated variables become the input ports you wire nodes together with.
- [Reusable Components and Variables](./reusable-components.md) - stored conversation variables are a common source for what gets dragged into a prompt slot.
- [Retrieval-Augmented Generation (RAG)](./rag.md) - a `{{context}}` variable is the standard injection point for retrieved knowledge.
- [No-Code AI Agents](./no-code-agents.md) - templating is a core mechanic of building agents without writing code.

## Tools

- [Vector Shift](../entities/tools/vector-shift.md) - the platform where Cole demonstrates the `{{ }}` variable syntax.

## Sources

- [Turn ANY AI Agent into a Live Person - Voice Chat Setup in Minutes](../sources/turn-any-ai-agent-into-a-live-person-voice-chat-setup-in-minutes.md) - "[0:05:11] I'll use their syntax here which is with squiggly brackets so two s brackets and then prompt and then closing it out and then there we go we now have an input called prompt where I can drag the text into it"
