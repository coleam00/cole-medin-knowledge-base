---
type: concept
title: "System Prompt Engineering"
description: "Crafting an agent's system prompt (persona, rules, output shape, routing logic, reusable templates) to steer its behavior consistently across turns."
tags: [prompting, system-prompt, ai-agents, output-shaping, routing]
videos: [learn-90-of-building-ai-agents-in-30-minutes, stop-paying-for-gpt-claude-other-llms-get-them-all-in-one-place, ai-is-too-expensive-if-you-dont-do-this, i-finally-built-an-ai-agent-to-organize-my-life-ai-agents-masterclass-4, i-made-a-custom-ai-chatbot-site-in-47-lines-of-code, developers-this-is-how-you-stay-relevant-with-ai-ai-agents-masterclass-1]
created: 2026-07-21
updated: 2026-07-21
---

# System Prompt Engineering

System prompt engineering is the craft of writing the standing instructions that shape an agent's behavior across every turn, not just a single reply. The system message "kind of sets the context for the whole conversation with the chatbot" [0:02:48]. Cole works from a consistent skeleton: "I always have persona and goals, tool instructions and examples, output format, and miscellaneous instructions" [0:11:03]. Those four blocks cover who the agent is, how it uses its tools, what shape its answers take, and a catch-all for fixes: the miscellaneous block "is also the place to go to add in extra instructions to fix those little issues you see with your agent" [0:11:57].

## The building blocks

The persona sets the frame, "you are a personal assistant or you are a financial expert who does XYZ that's where you set that kind of thing here in the system message" [0:03:03], the same role-setting move as role prompting, made permanent. Output shaping directs the model toward the response you want, since without it "when you ask it for something like an answer where it should generate code ... it doesn't always do that" [0:07:56]. Two recurring, easily-missed details: inject the current date, because "AI doesn't always have the current date a lot of models are missing that" [0:03:17] and an agent needs it to set due dates correctly [0:04:53]; and give housekeeping rules like "you never give IDs to the user since those are just for you to keep track of" [0:11:38].

A specialized case is the router prompt, where the system prompt encodes decision logic. "the most important thing here for the AI router prompt is to be very specific in the way that you tell it how to determine if a request is complicated or not" [0:05:14], derived by thinking through "what your agent might be responsible for doing what kind of requests would come in and then you define the rules for the router based on that" [0:05:28]. Getting that prompt right was the hard part: "the hardest part there was getting a good prompt for the AI router the rest of the code was easy peasy" [0:10:33]. Cole's advice for beginners is to keep it lightweight at first: "what you shouldn't worry about at this point is setting up elaborate prompt evaluations or split testing your system prompts" [0:11:03].

## Part of

- [Context Engineering](./context-engineering.md) and [The Core Components of an Agent](./agent-core-components.md): the system prompt is a core, standing component of the agent's context.

## Related

- [Role Prompting](./role-prompting.md) is the persona block, made permanent.
- [Docstrings as Tool Descriptions](./docstrings-as-tool-descriptions.md) complements the tool-instructions block.
- [Prompt Versioning](./prompt-versioning.md) tracks changes to the system prompt over time.
- [Reduce Assumptions](./reduce-assumptions.md) and [Avoid Negative Instructions](./avoid-negative-instructions.md) are the clarity rules that keep a system prompt unambiguous.
- [Chat Interfaces](./chat-interfaces.md) and [Model Selection](./model-selection.md).
- [Model-Specific Prompts](./model-specific-prompts.md) - Different LLMs need different prompts, so a serious system keeps a library of model-tuned system prompts instead of reusing one prompt written for a single frontier model.
- [Dynamic System Prompt](./dynamic-system-prompt.md) - Assembling an agent's system prompt at runtime by scanning a skills/context directory and injecting each file's front-matter description and path onto the static base instructions, which is what makes skills portable to any framework.
- [Prompting Guide](../entities/tools/prompting-guide.md) - promptingguide.ai, the free resource Cole names as the single prompt-engineering guide worth studying end to end.

## Sources

- [Learn 90% of Building AI Agents in 30 Minutes](../sources/learn-90-of-building-ai-agents-in-30-minutes.md) - "[0:11:03] I always have persona and goals, tool instructions and examples, output format, and miscellaneous instructions"
- [AI is TOO EXPENSIVE if You Don't Do This](../sources/ai-is-too-expensive-if-you-dont-do-this.md) - "[0:05:14] the most important thing here for the AI router prompt is to be very specific in the way that you tell it how to determine if a request is complicated or not"
- [I Made a Custom AI Chatbot Site in 47 Lines of Code](../sources/i-made-a-custom-ai-chatbot-site-in-47-lines-of-code.md) - "[0:03:03] you are a personal assistant or you are a financial expert who does XYZ that's where you set that kind of thing here in the system message"
- [I FINALLY Built an AI Agent to Organize my Life - AI Agents Masterclass #4](../sources/i-finally-built-an-ai-agent-to-organize-my-life-ai-agents-masterclass-4.md) - "[0:11:38] one thing for example you never give IDs to the user since those are just for you to keep track of"
- [Developers, THIS is How you Stay Relevant with AI - AI Agents Masterclass #1](../sources/developers-this-is-how-you-stay-relevant-with-ai-ai-agents-masterclass-1.md) - "[0:04:53] I'm also giving the current date which is important because the AI needs to know the current date to then be able to know when to put the due dates on for tasks"
- [STOP Paying for GPT, Claude, & Other LLMs - Get them ALL in One Place](../sources/stop-paying-for-gpt-claude-other-llms-get-them-all-in-one-place.md) - "[0:07:56] you're basically directing the llm for what you are looking for ... when you ask it for something like an answer where it should generate code to get you the answer it doesn't always do that"
