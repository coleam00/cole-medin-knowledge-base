---
type: concept
title: "Abstraction Distraction"
description: "The trap of reaching for heavy frameworks and abstractions that get in the way instead of writing simple, direct code."
tags: [abstraction, simplicity, frameworks]
videos: [the-only-ai-tech-stack-you-need-in-2026, openais-brand-new-agents-sdk-crash-course, introducing-archon-an-ai-agent-that-builds-ai-agents]
created: 2026-07-21
updated: 2026-07-21
---

# Abstraction Distraction

An abstraction distraction is a framework or library that promises to do so much for you that it ends up costing you the flexibility, control, and understanding you actually need. Cole coined the phrase for exactly this failure mode: "a lot of these frameworks are what I like to call an abstraction distraction. You end up fighting the framework more than it's actually helping you because it's hard to really customize things." The distraction is subtle because the framework feels productive at first, "it's really easy to use those frameworks because they take care of so much for you, but then in the end you don't really understand what's going on."

The core problem is a hidden trade: convenience now for opacity and rigidity later. When a framework owns the internals of your agent loop, tool calls, and prompt assembly, you inherit its opinions and lose the ability to tune the parts that matter. Cole names LangChain and CrewAI as the usual offenders, tools that "try to do too much for you," and he even puts the OpenAI Agents SDK partway down that same slope: "for the agent SDK I find it leads a bit more towards that CrewAI and LangChain level of abstraction." The tell is when you spend more time reverse-engineering the framework than solving your actual problem.

The antidote is staying close to raw LLM calls while adopting just enough structure to stay productive. The goal is a stack thin enough that "I still feel like I have all the flexibility and control that I need as if I was doing raw LLM calls." This is why Cole reaches for lighter-weight tooling and why he built [Archon](../entities/tools/archon.md) as an iteration on the idea rather than another do-everything framework, warning that heavier alternatives make you "lose a lot of that customizability and control." Abstraction is not the enemy; the wrong abstraction, one that hides the machinery you need to reach, is.

## Contrasts with

- [Capabilities Over Tools](./capabilities-over-tools.md) - focusing on what you can accomplish and the durable skills underneath, rather than mastering (or fighting) any one framework.

## Related

- [Provider Independence](./provider-independence.md) - staying thin and close to raw calls also keeps you free to swap models and providers.
- [Agentic Workflow Engineering](./agentic-workflow-engineering.md) - building your own optimized workflow instead of inheriting a heavy framework's opinions.

## Tools

- [LangChain](../entities/tools/langchain.md) - Cole's recurring example of an abstraction that implements too much for you.
- [CrewAI](../entities/tools/crewai.md) - grouped with LangChain as trying to do too much.
- [OpenAI Agents SDK](../entities/tools/openai-agents-sdk.md) - lands "a bit more" toward the CrewAI and LangChain level of abstraction.
- [Pydantic AI](../entities/tools/pydantic-ai.md) - a lighter-weight alternative that preserves raw-call flexibility.

## Sources

- [The ONLY AI Tech Stack You Need in 2026](../sources/the-only-ai-tech-stack-you-need-in-2026.md) - "[0:06:56] a lot of these frameworks are what I like to call an abstraction distraction. You end up fighting the framework more than it's actually helping you because it's hard to really customize things"
- [OpenAI's BRAND NEW Agents SDK (Crash Course)](../sources/openais-brand-new-agents-sdk-crash-course.md) - "[0:27:35] there are other frameworks like LangChain and CrewAI that try to do too much for you... it's really easy to use those frameworks because they take care of so much for you but then in the end you don't really understand what's going on"
- [Introducing Archon - an AI Agent that BUILDS AI Agents](../sources/introducing-archon-an-ai-agent-that-builds-ai-agents.md) - "[0:07:29] a lot of the other frameworks out there like LangChain... they are what's called an abstraction distraction... they try to implement so much for you that you lose a lot of that customizability and control"
