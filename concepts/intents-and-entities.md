---
type: concept
title: "Intents and Entities"
description: "The no-code tool-definition mechanism where an intent (name, description, and example utterances) tells the agent when to fire a tool, and entities are the required input variables it must collect first."
tags: [no-code, tool-calling]
videos: [the-king-of-no-code-ai-agent-builders]
created: 2026-07-21
updated: 2026-07-21
---

# Intents and Entities

Intents and entities are the no-code builder's mechanism for defining tools and telling an agent when to use them. In Cole's walkthrough, "we get to intents and entities and this is where we get to really Define the tools for our agent and telling our agent when to invoke these specific tools" ([0:08:07]). It is the visual-canvas equivalent of a coded tool definition plus its trigger condition.

An **intent** is the instruction that decides *when* a tool fires. "I'm going to create an intent right here and that is basically the instructions to the AI agent to understand when to use a tool" ([0:08:22]). In practice an intent carries a name, a description of what the tool is for, and example utterances that show the phrasings that should trigger it. The agent matches an incoming message against those intents to route to the right tool, which is the no-code framing of tool selection.

An **entity** is a required input the tool needs before it can run. "Whenever we want to invoke a tool ... there's typically input variables ... so that is what an entity is it is essentially an input variable" ([0:09:40]). Because the tool cannot execute without its entities, the pattern implies the agent should gather missing values first, which is where clarifying questions come in: if a user's message triggers an intent but leaves an entity unfilled, the agent asks for it rather than calling the tool with a hole in its arguments.

## Part of

- [No-Code AI Agents](./no-code-agents.md) - the broader no-code agent-building context this tool-definition model lives inside.

## Related

- [Tool Use](./tool-use.md) - the general capability that intents and entities express in a no-code form.
- [Clarifying Questions](./clarifying-questions.md) - how an agent collects an entity it is missing before firing the tool.

## Tools

- [Voiceflow](../entities/tools/voiceflow.md) - the no-code builder whose intent/entity model this describes.

## Sources

- [The KING of No Code AI Agent Builders?!](../sources/the-king-of-no-code-ai-agent-builders.md) - "[0:08:07] we get to intents and entities and this is where we get to really Define the tools for our agent and telling our agent when to invoke these specific tools"
- [The KING of No Code AI Agent Builders?!](../sources/the-king-of-no-code-ai-agent-builders.md) - "[0:09:40] whenever we want to invoke a tool ... there's typically input variables ... so that is what an entity is it is essentially an input variable"
