---
type: entity
subtype: tool
title: "GPT-4o"
description: "Cited as the more expensive, more powerful model to route complicated requests to in a cost-routing setup."
tags: [llm, openai]
videos: [ai-agents-the-future-of-ai-or-a-passing-fad, i-made-a-custom-ai-chatbot-site-in-47-lines-of-code]
created: 2026-07-21
updated: 2026-07-21
---

# GPT-4o

GPT-4o is OpenAI's flagship multimodal model from the pre-reasoning-model era, and in Cole's videos it plays two recurring roles: the default "most powerful" choice for a general chatbot, and the expensive endpoint you route hard requests to. In the 47-lines-of-code chatbot build he notes the app "defaults to GPT-4o because that really is uh the most powerful model at the time of this recording except for maybe Claude 3.5," positioning it as the sensible baseline when you just want strong general-purpose output.

Its more instructive appearance is as the top tier in a cost-routing pattern. Rather than paying flagship prices for every call, Cole describes classifying incoming requests and only escalating the difficult ones: "If it's something that's more complicated then you go to the more expensive model like GPT-4o in my example here." That makes GPT-4o less a fixed dependency than a knob in [Model Selection](../../concepts/model-selection.md), the lever you reach for when a task's difficulty justifies the spend. Cheap requests stay on a smaller sibling; only the ones that need the horsepower hit GPT-4o.

Because it is a closed, hosted model, GPT-4o also sits on the opposite side of Cole's local-AI work from tools like [Ollama](./ollama.md). When he wants privacy or zero marginal cost he runs open models locally; when he wants raw capability for a customer-facing [chat interface](../../concepts/chat-interfaces.md) or a [generative UI](../../concepts/generative-ui.md), GPT-4o is the reach-for default. It is the same model his [GPT-4o mini](./gpt-4o-mini.md) references as the cheaper, faster cousin, and it accessible through aggregators like [OpenRouter](./openrouter.md) alongside every other provider.

## Realizes

- [Model Selection](../../concepts/model-selection.md) - Choosing the right LLM per task by trading off quality, speed, and cost, often routing easy requests to cheap models and hard ones to expensive models.
- [Chat Interfaces](../../concepts/chat-interfaces.md) - Wrapping agents in chat surfaces (websites, DMs, platforms) with adapters, a shared message format, and durable history.
- [Generative UI](../../concepts/generative-ui.md) - Interfaces the agent generates or drives at runtime, streaming tool activity and reasoning into a live, stateful UI.
- [Agentic Workflow Engineering](../../concepts/agentic-workflow-engineering.md) - Designing repeatable AI workflows as engineered systems with defined steps, orchestration, and background execution rather than ad-hoc prompting.
- [System Prompt Engineering](../../concepts/system-prompt-engineering.md) - Crafting an agent's system prompt (persona, rules, output shape, routing logic, reusable templates) to steer its behavior consistently across turns.
- [Memory Systems](../../concepts/memory-systems.md) - Giving agents durable short- and long-term memory so conversations, user context, and facts persist across sessions and users.

## Contrasts with

- [Claude](./claude.md) - Named as an example of a large language model that can be turned into an agent, the "Claude 3.5" contemporary Cole flags as the one rival to GPT-4o.
- [Claude 3.5 Sonnet](./claude-3-5-sonnet.md) - Anthropic's mid-2024 flagship model and the only LLM Cole could not break in his agentic stress test, making it his clear winner for multi-step tool-using workflows.
- [Berkeley Function Calling Leaderboard](./berkeley-function-calling-leaderboard.md) - A public benchmark that ranks LLMs on function-calling accuracy using tasks meant to represent real agent and enterprise workflows.

## Related

- [GPT-4o mini](./gpt-4o-mini.md) - A fast, cheap OpenAI model cited as a speed benchmark; the cheaper, faster sibling for simple requests.
- [OpenRouter](./openrouter.md) - Unified API gateway to many LLMs through which GPT-4o and rivals can all be reached.

## Sources

- [AI Agents: The Future of AI or a Passing Fad?](../../sources/ai-agents-the-future-of-ai-or-a-passing-fad.md) - "[0:08:16] If it's something that's more complicated then you go to the more expensive model like GPT-4o in my example here"
- [I Made a Custom AI Chatbot Site in 47 Lines of Code](../../sources/i-made-a-custom-ai-chatbot-site-in-47-lines-of-code.md) - "[0:02:03] defaults to GPT-4o because that really is uh the most powerful model at the time of this recording except for maybe Claude 3.5"
