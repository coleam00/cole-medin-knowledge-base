---
type: concept
title: "Capabilities Over Tools"
description: "Framing skills as composable capabilities the model can combine, rather than a flat list of rigid tools."
tags: [capabilities, skills, composability]
videos: [pydantic-ai-20-the-new-best-way-to-build-ai-agents-is-composing-capabilities, the-only-ai-tech-stack-you-need-in-2026, ive-been-holding-back-on-youtube-but-not-anymore, how-id-learn-ai-agents-fast-if-i-had-to-start-over-full-roadmap, how-to-dominate-with-ai-in-2025]
created: 2026-07-21
updated: 2026-07-21
---

# Capabilities Over Tools

Capabilities over tools is Cole's central mantra for learning and building with AI: focus on what you can accomplish, not on the specific product you accomplish it with. "The mantra that I always have is capabilities over tools," and it is deliberately the highest-leverage idea he teaches: "no matter what you are building for yourself or your business, the most important thing is the capabilities that you are building not the underlying tools that you are using." The reason it matters is durability. Tools churn constantly, so "you don't want to get caught in the weeds spending hours and hours and hours mastering very specific tools that might become irrelevant next month." Capabilities, by contrast, "are the higher leverage skills that transcend any individual tool you could be using. Things like design patterns and architecture, the systems that go into building AI agents."

The phrase carries a second, more technical meaning that surfaces in the Pydantic AI 2.0 framing: a capability is a composable unit of agent behavior. "A capability bundles an agent's instructions, tools, life cycle hooks, and model settings into a single composable unit. So a whole extension can reach every layer of the agent through one concept." Under this lens an agent stops being a script and becomes an assembly: "now our AI agents can be thought of quite simply as just a set of these composable units, these capabilities. We're combining all of them together to give the agent all the responsibilities that we want for it." Because a capability spans every layer, it can be packaged once and reused, "we can package up in a single capability and then we can reuse it between our AI agents," for example a support capability that powers both a backend agent and a front-facing FAQ widget.

Both meanings point the same direction: don't obsess over the vendor, obsess over the reusable unit of problem-solving. The practical corollary is to "get right into solving the actual problem, building the actual software instead of worrying about the tools cuz in the end, problems come first," and once you find a stack that works, "find what works well for you and just stick with it." Learning specific tools still matters, but it is never the priority.

## Contrasts with

- [Abstraction Distraction](./abstraction-distraction.md) - the opposite failure: fixating on a heavy tool or framework instead of the capability you are actually building.

## Implemented by

- [Skills](./skills.md) - the concrete, reusable capability units a coding agent loads on demand.
- [MCP](./mcp.md) - a protocol for exposing capabilities to an agent without hardwiring a specific integration.

## Related

- [Progressive Disclosure](./progressive-disclosure.md) - how composable capabilities are surfaced to the model only when needed.
- [AI Coding Harness](./ai-coding-harness.md) - the system that composes capabilities into a working setup.
- [Agentic Workflow Engineering](./agentic-workflow-engineering.md) - engineering reusable workflows out of composed capabilities.
- [Provider Independence](./provider-independence.md) - capabilities thinking is what lets you swap the underlying tool or model.
- [Model Selection](./model-selection.md) - the model is one setting inside a capability, not the point of it.

## Tools

- [Pydantic AI](../entities/tools/pydantic-ai.md) - its 2.0 release formalizes capabilities as composable units bundling instructions, tools, hooks, and settings.

## Sources

- [The ONLY AI Tech Stack You Need in 2026](../sources/the-only-ai-tech-stack-you-need-in-2026.md) - "[0:00:54] The mantra that I always have is capabilities over tools."
- [I've Been Holding Back on YouTube... But Not Anymore](../sources/ive-been-holding-back-on-youtube-but-not-anymore.md) - "[0:05:01] no matter what you are building for yourself or your business, the most important thing is the capabilities that you are building not the underlying tools that you are using."
- [Pydantic AI 2.0: The New Best Way to Build AI Agents is Composing Capabilities](../sources/pydantic-ai-20-the-new-best-way-to-build-ai-agents-is-composing-capabilities.md) - "[0:01:23] a capability bundles an agent's instructions, tools, life cycle hooks, and model settings into a single composable unit. So a whole extension can reach every layer of the agent through one concept"
- [How I'd Learn AI Agents FAST if I Had to Start Over (Full Roadmap)](../sources/how-id-learn-ai-agents-fast-if-i-had-to-start-over-full-roadmap.md) - "[0:04:32] you always need to remember capabilities over tools... you want to focus on what you're able to accomplish instead of getting into the nitty-gritty details of mastering specific tools"
- [How to DOMINATE with AI in 2025](../sources/how-to-dominate-with-ai-in-2025.md) - "[0:02:36] it is the most important motto that you can get through your head right now and that is the idea of capabilities not tools"
