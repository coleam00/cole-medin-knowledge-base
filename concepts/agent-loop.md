---
type: concept
title: "The Agent Loop (Reason-Act-Observe)"
description: "The core agentic cycle where the LLM reasons, calls a tool, observes the result, and loops an unknown number of times until it decides to respond."
tags: [react, reasoning-loop, tool-calling, recursion]
videos: [google-anthropic-and-openais-guides-to-ai-agents-all-in-18-minutes, are-you-building-real-ai-agents-or-just-using-llms, llama-32-is-insane-but-does-it-beat-gpt-as-an-ai-agent, dont-sleep-on-the-ultimate-ai-agent-combo-n8n-langchain-python, openais-o1-is-barely-usable-but-i-fixed-it, i-found-the-limits-of-the-most-popular-llms, the-best-tool-for-ai-agent-workflows-langgraph-full-guide, prompt-engineering-is-a-bunch-of-bs-heres-the-5-of-it-to-learn, the-secret-sauce-for-simple-powerful-ai-apps-ai-agents-masterclass-2, developers-this-is-how-you-stay-relevant-with-ai-ai-agents-masterclass-1, introducing-trainers-ally-nvidia-ai-agents-competition-submission]
created: 2026-07-21
updated: 2026-07-21
---

# The Agent Loop (Reason-Act-Observe)

The agent loop is the engine at the center of every agent. The pattern is ReAct: "first we have react. This is reason, then act, then observe. This is the main one that we'll focus on." [0:06:35] The model reasons about what to do, acts by calling a tool, observes the result, and then loops, feeding the observation back in so it can decide the next move. Cole describes the observe step concretely: "the agent observes what happens when it invokes these tools in the environment like it sees what happened when I queried the database what did I get back what do I need to do next." [0:04:55]

What makes it a *loop* rather than a straight line is that the number of iterations is not fixed: "we don't know how many actions the agent is going to take. Sometimes it might take zero actions and just answer our question right away. Other times it'll take two. Sometimes it'll take five." [0:01:49] The agent decides for itself when it is done, and only then "the final results after it decides that it's performed everything it needs to do to achieve the goal it sends that back to the user." [0:06:14] This self-directed termination is exactly what separates an agent from a fixed [workflow](./agents-vs-workflows.md).

Mechanically, the loop is a router plus recursion. A router node checks the model's last message for tool calls: "this router here is going to determine do we need to make any tool calls did the llm ask to do so if it did then we'll route to the tool node." [0:04:12] The tool runs, and its result is appended to the conversation as a tool message "because that way AI has context around what actually happened when it decided to invoke this n8n workflow." [0:19:53] Then the model is called again: "we're going to recursively call Prompt AI again to get a response from the llm now that it has made the tool call so it might choose to make another tool call or maybe now it's going to actually produce the final response." [0:20:10] That cycle repeats "until the AI agent has done everything that the user asked it to do." [0:04:40]

## Prerequisites

- [Tool Use](./tool-use.md) - the "act" step; the loop is built around invoking tools.
- [Chain-of-Thought Prompting](./chain-of-thought.md) - the "reason" step that decides each action.

## Part of

- [The Core Components of an Agent](./agent-core-components.md) - the loop is what animates the LLM, tools, prompt, and memory at runtime.

## Contrasts with

- [Agents vs. Workflows](./agents-vs-workflows.md) - the loop's unknown iteration count is precisely what a deterministic workflow lacks.
- [Deterministic Workflows](./deterministic-workflows.md) - a fixed step sequence with no self-directed looping.

## Related

- [Self-Correcting Agents](./self-correction.md) - observing a bad result and retrying is a loop behavior.
- [Agentic Workflow Engineering](./agentic-workflow-engineering.md) - engineering the loop into reliable systems.
- [Agent Graphs](./agent-graphs.md) - modeling the loop as router nodes and edges.
- [Chat Interfaces](./chat-interfaces.md) - where the loop's final response is delivered.
- [Human in the Loop](./human-in-the-loop.md) - pausing the loop for approval.
- [Memory Systems](./memory-systems.md) - the growing message history the loop reads and appends to.
- [Prompt Engineering](./prompt-engineering.md) - ReAct prompting drives the reasoning step.
- [Provider Independence](./provider-independence.md) - the loop pattern is the same across model providers.

## Tools

- [LangGraph](../entities/tools/langgraph.md) - models the loop explicitly as an agent node, a tool node, and a router edge.
- [LangChain](../entities/tools/langchain.md) - provides the tool-calling primitives the loop recurses over.
- [n8n](../entities/tools/n8n.md) - runs the loop inside a no-code agent node.
- [Pydantic AI](../entities/tools/pydantic-ai.md) - handles the reason-act-observe cycle for you.
- [Auto-GPT](../entities/tools/auto-gpt.md) - Open-source experiment that wraps GPT-4 in an autonomous goal-decomposition-and-execution loop with tool use and optional vector-database memory; the first widely known autonomous agent.
- [Claude 3.5 Sonnet](../entities/tools/claude-3-5-sonnet.md) - Anthropic's mid-2024 flagship model and the only LLM Cole could not break in his agentic stress test, making it his clear winner for multi-step tool-using workflows.

## Sources

- [Google, Anthropic, and OpenAI's Guides to AI Agents ALL in 18 Minutes](../sources/google-anthropic-and-openais-guides-to-ai-agents-all-in-18-minutes.md) - "[0:01:49] we don't know how many actions the agent is going to take. Sometimes it might take zero actions and just answer our question right away. Other times it'll take two. Sometimes it'll take five."
- [Are You Building REAL AI Agents or Just Using LLMs?](../sources/are-you-building-real-ai-agents-or-just-using-llms.md) - "[0:04:55] the agent observes what happens when it invokes these tools in the environment like it sees what happened when I queried the database what did I get back what do I need to do next"
- [Don't Sleep on the ULTIMATE AI Agent Combo (n8n, LangChain, Python)](../sources/dont-sleep-on-the-ultimate-ai-agent-combo-n8n-langchain-python.md) - "[0:20:10] what we're going to do is recursively call Prompt AI again to get a response from the llm now that it has made the tool call so it might choose to make another tool call or maybe now it's going to actually produce the final response"
- [THE BEST Tool for AI Agent Workflows - LangGraph FULL Guide](../sources/the-best-tool-for-ai-agent-workflows-langgraph-full-guide.md) - "[0:05:30] a lot of times when agents interact with tools it goes in a loop and the reason for that is you have an agent that decides it wants to invoke a tool"
- ["Prompt Engineering" is a Bunch of BS - Here's the 5% of it to Learn](../sources/prompt-engineering-is-a-bunch-of-bs-heres-the-5-of-it-to-learn.md) - "[0:02:26] the reason plus act framework like I just said that's like the core of AI agents to reason about oh I need to invoke this tool now I need to take the response and tell it to the user"
- [The Secret Sauce for SIMPLE + POWERFUL AI Apps - AI Agents Masterclass #2](../sources/the-secret-sauce-for-simple-powerful-ai-apps-ai-agents-masterclass-2.md) - "[0:06:21] we're going to Loop through every single tool call ... extract the name of the tool ... map the tool name to the actual function ... and invoke the tool with the arguments"
- [Developers, THIS is How you Stay Relevant with AI - AI Agents Masterclass #1](../sources/developers-this-is-how-you-stay-relevant-with-ai-ai-agents-masterclass-1.md) - "[0:13:35] we need to actually query the AI again and tell it hey you asked to call this function we did it here's the response now write a message back out to the user"
- [Llama 3.2 is INSANE - But Does it Beat GPT as an AI Agent?](../sources/llama-32-is-insane-but-does-it-beat-gpt-as-an-ai-agent.md) - "[0:04:40] it can handle invoking a bunch of different Tools in a loop until the AI agent has done everything that the user asked it to do"
- [I Found the Limits of the Most Popular LLMs](../sources/i-found-the-limits-of-the-most-popular-llms.md) - "[0:07:27] go through that cycle of making tool calls until it decides it doesn't need to anymore"
- [OpenAI's o1 is Barely Usable, but I Fixed it...](../sources/openais-o1-is-barely-usable-but-i-fixed-it.md) - "[0:15:23] at the end of this function here we're just going to recursively call Prompt AI... to either make the next tool call that might be necessary or produce that final response for the user"
- [Introducing Trainer's Ally - Nvidia AI Agents Competition Submission](../sources/introducing-trainers-ally-nvidia-ai-agents-competition-submission.md) - "[0:01:18] and that's the last day so it will go to the end for me so here are the final workouts"
