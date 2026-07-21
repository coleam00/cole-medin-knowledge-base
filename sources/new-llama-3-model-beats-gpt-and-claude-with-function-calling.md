---
type: source
title: "New Llama 3 Model BEATS GPT and Claude with Function Calling!?"
description: "Groq's fine-tuned Llama 3 models top the Berkeley Function Calling Leaderboard, so an open-source model you can run locally is now competitive with GPT and Claude for driving AI agents."
youtube_id: RtEzpBhQWIc
url: https://www.youtube.com/watch?v=RtEzpBhQWIc
slug: new-llama-3-model-beats-gpt-and-claude-with-function-calling
published: 2024-07-21
duration: "0:14:06"
recency_rank: 181
raw: "../raw/new-llama-3-model-beats-gpt-and-claude-with-function-calling.md"
tags: [local-ai, tool-use, model-selection, agent-evaluation]
created: 2026-07-21
updated: 2026-07-21
---

# New Llama 3 Model BEATS GPT and Claude with Function Calling!?

Cole reacts to Groq's release of Llama 3 models specifically tuned for function calling, which claimed the top spots on the Berkeley Function Calling Leaderboard. The 70B version is ranked #1 at roughly 90% accuracy and the 8B version is #3, beating every GPT model and every Claude model except 3.5 Sonnet. Cole frames this as a historic first: the best function-calling model is now open source rather than proprietary, which matters because function calling is what lets a model act as a real agent.

To test the claim beyond the benchmark, he runs the same task-management AI agent (built in LangChain with a Streamlit UI, controlling Asana) under two models: GPT-4o first, then Groq's Llama 3 70B. GPT-4o handles a complex multi-tool request flawlessly, researching 10 steps, creating an Asana project, adding each step as a task due Friday, then completing, deleting, and adding tasks. Swapping to Groq requires only importing ChatGroq from LangChain and changing the model instantiation; everything else stays the same, which underscores how LangChain makes agents model-agnostic.

Groq's Llama 3 completes the same workflow but with more friction. It is dramatically faster per response, yet it asks the user to resolve the actual date for "Friday," fails to look up task IDs on its own, and occasionally updates the wrong task. Cole concludes it is "almost as good" as GPT, attributing the gap mostly to GPT's better handling of many tokens, and calls near-parity from a local open-source model a big win for accessible, transparent AI.

## Concepts covered

- [Local & Self-Hosted AI](../concepts/local-ai.md)
- [Tool Calling](../concepts/tool-use.md)
- [Model Selection](../concepts/model-selection.md)
- [Agent Evaluation](../concepts/agent-evaluation.md)
- [What Is an AI Agent](../concepts/what-is-an-ai-agent.md)

## Entities

- [Groq](../entities/organizations/groq.md)
- [Llama](../entities/tools/llama.md)
- [LangChain](../entities/tools/langchain.md)
- [OpenAI](../entities/organizations/openai.md)
- [Anthropic](../entities/organizations/anthropic.md)
- [Asana](../entities/tools/asana.md)
- [Streamlit](../entities/tools/streamlit.md)
- [Cole Medin](../entities/people/cole-medin.md)

## Key moments

- **[0:00:00]** Claim: for the first time the best function-calling LLM is an open-source model you can run locally
- **[0:01:02]** Groq's 70B Llama 3 is #1 (~90%) and 8B is #3 on the Berkeley Function Calling Leaderboard
- **[0:02:31]** Sets up a head-to-head test using his Asana task-management agent, GPT-4o first
- **[0:06:21]** GPT-4o completes the complex multi-tool Asana workflow flawlessly
- **[0:08:19]** Shows the code change to switch to Groq: import ChatGroq, swap the model
- **[0:09:41]** Groq Llama 3 is much faster but asks the user to confirm the date for Friday
- **[0:11:07]** Groq model fails to look up task IDs itself and updates the wrong task
- **[0:13:00]** Verdict: almost as good as GPT, a huge victory for open-source / local models

## Transcript

[Raw transcript](../raw/new-llama-3-model-beats-gpt-and-claude-with-function-calling.md)
