---
type: source
title: "AI is TOO EXPENSIVE if You Don't Do This"
description: "Instead of paying for one expensive LLM to handle every request, put a cheap router model in front that classifies each request's complexity and dispatches simple requests to a cheap model and only the rare complex ones to the expensive model, cutting AI costs by 90% or more."
youtube_id: ZzRCrhA3JUQ
url: https://www.youtube.com/watch?v=ZzRCrhA3JUQ
slug: ai-is-too-expensive-if-you-dont-do-this
published: 2024-07-31
duration: "0:11:26"
recency_rank: 178
raw: "../raw/ai-is-too-expensive-if-you-dont-do-this.md"
tags: [model-selection, ai-router, cost-optimization, groq, llama]
created: 2026-07-21
updated: 2026-07-21
---

Production AI applications get very expensive because most teams pick a single model powerful (and costly) enough to handle their hardest requests, even though those complex requests are only 5-10% of traffic. Paying premium prices for the 90-95% of requests that a cheap model could handle just fine is the core waste.

The fix is an AI router: a first-step LLM call that outputs a simple yes/no complexity judgment. Simple requests route to a cheap model, complex ones route to the expensive model, so both get a good answer but the bill is a fraction of what it would be. The router itself can run on a cheap model, and even paying for that extra classification step is pennies compared to sending everything to the premium model. The hardest part is writing the router prompt with specific, agent-tailored rules for what counts as complicated.

He demonstrates by enhancing a GPT-4o-powered Asana task-management agent to also use Llama 3 70B via Groq (roughly 11% of GPT-4o's input cost and 5% of its output cost). A helper pulls recent chat history into the router prompt for context, a decide-model function returns "cheap" or "expensive," and the prompt-AI function instantiates ChatGroq or ChatOpenAI accordingly. Live tests show greetings and single lookups going to the cheap model, while multi-task creation requests escalate to the expensive one; when routing is off, you just refine the router prompt.

## Concepts covered

- [Model Selection](../concepts/model-selection.md)
- [Agent Observability](../concepts/agent-observability.md)
- [System Prompt Engineering](../concepts/system-prompt-engineering.md)
- [Context Engineering](../concepts/context-engineering.md)
- [Tool Calling](../concepts/tool-use.md)

## Entities

- [Cole Medin](../entities/people/cole-medin.md)
- [OpenAI](../entities/organizations/openai.md)
- [Groq](../entities/organizations/groq.md)
- [Llama](../entities/tools/llama.md)
- [Asana](../entities/tools/asana.md)
- [Streamlit](../entities/tools/streamlit.md)

## Key moments

- **[0:00:16]** Promise: save 90% or more on AI costs by not using a single model for everything
- **[0:00:31]** Only 5-10% of agent requests are truly complex; the rest are simple
- **[0:01:32]** Introduces the AI router pattern via a diagram from a prior video
- **[0:01:48]** Router outputs yes/no complexity using custom prompt rules, then routes to cheap or expensive model
- **[0:02:47]** Code walkthrough begins on a GPT-4o Asana task agent from the AI Agents Master Class
- **[0:04:13]** Adds Llama 3 70B via Groq (~11% input / ~5% output cost of GPT-4o), function-calling fine-tune
- **[0:04:27]** Helper pulls recent chat history to give the router context for its decision
- **[0:05:14]** Groq/Llama 3 70B used as the router itself because it's so cheap
- **[0:06:15]** prompt-AI gains a cheap/expensive parameter selecting ChatGroq vs ChatOpenAI
- **[0:08:09]** Live tests: greetings and single lookups go cheap, multi-task creation escalates to expensive
- **[0:10:33]** Wrap-up: the hardest part is a good router prompt; the rest of the code is easy

## Transcript

[Raw transcript](../raw/ai-is-too-expensive-if-you-dont-do-this.md)
