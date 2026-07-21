---
type: concept
title: "Tool Calling"
description: "Letting an LLM invoke external functions and APIs so it can take actions and fetch data beyond its parametric knowledge."
tags: [tools, function-calling, actions, apis, arguments]
videos: [build-your-first-voice-ai-agent-in-20-minutes-with-livekit-open-source, give-me-28-minutes-and-ill-completely-change-the-way-you-build-ai-agents, openais-brand-new-agents-sdk-crash-course, are-you-building-real-ai-agents-or-just-using-llms, pydantic-ai-deepseek-v3-the-best-ai-agent-combo, weve-been-building-ai-agents-wrong-until-now, flowise-n8n-the-best-no-code-local-ai-agent-combo, the-king-of-no-code-ai-agent-builders, ollama-openais-swarm-easily-run-ai-agents-locally, openais-swarm-a-game-changer-for-ai-agents, this-slack-ai-personal-assistant-is-better-than-a-real-person, llama-32-is-insane-but-does-it-beat-gpt-as-an-ai-agent, bubble-is-my-biggest-regret-for-no-code-ai-apps-what-i-use-instead, openais-o1-is-barely-usable-but-i-fixed-it, complete-guide-to-langserve-make-your-ai-agent-actually-useful, i-found-the-limits-of-the-most-popular-llms, the-most-profitable-ai-niche-no-one-is-talking-about, youre-wasting-time-coding-your-ai-agents, ai-is-too-expensive-if-you-dont-do-this, new-llama-3-model-beats-gpt-and-claude-with-function-calling, i-finally-built-an-ai-agent-to-organize-my-life-ai-agents-masterclass-4, function-calling-with-any-llm-for-local-ai-agents-feat-langchain-huggingface-and-llama-3, ai-agents-just-got-sexy-ai-agents-masterclass-3, the-secret-sauce-for-simple-powerful-ai-apps-ai-agents-masterclass-2, the-only-ai-developer-roadmap-you-need-in-2024, developers-this-is-how-you-stay-relevant-with-ai-ai-agents-masterclass-1, chatgpt-is-the-gift-that-keeps-on-giving-introducing-auto-gpt]
created: 2026-07-21
updated: 2026-07-21
---

# Tool Calling

Tool calling, also known as function calling, is the mechanism that lets a language model invoke code to act on the world instead of only emitting text. As Cole frames it, "tools are how AI agents are given the ability to interact with the outside world to do things like search for flights Reserve hotels or get weather information" [0:11:39], and more concretely they are "the functions we give it to do things like explore the web hit some API like the weather API in this example or to perform rag over your knowledge base or use a calculator" [0:05:28]. This capability is what elevates a plain LLM into something useful: "function calling is one of the most powerful pieces of the latest and greatest large language models like GPT and Claw it's what allows them to seamlessly interact with external services on your behalf" [0:00:00].

The loop is deliberately narrow. The model never runs your code directly; it decides *which* function to call and *what arguments* to pass, and your program executes it and hands the result back. "The important thing to keep in mind for tools is that the llm determines the parameters and then whatever string we return is given back to the llm so it then reasons about the result" [0:13:19]. In modern SDKs the wiring is trivial: "all you have to do is Define a regular python function ... but you add this decorator at the top ... and that instantly turns this function into one of the tools available to the large language model" [0:09:00]. Under the hood, frameworks bind a name-to-function mapping into the chat object so a returned tool name resolves to real code: "we bind all of the functions that we're defining in all these different tool files together into the single dictionary and then we map that we bind that into the chat object" [0:05:59].

Tool calling is also the dividing line between an agent and a chatbot: "the tools part of the agent node is just dangling here there's nothing given to it for it to interact with the environment so it's just a regular chatbot" [0:11:14]. It depends on model support, which historically excluded most local models: "if you have a model that doesn't support tool calling it's not going to be able to actually act as an agent and invoke the tools that you have set up" [0:17:11]. When it works, agents chain calls, using "the context from previous tool calls to make the next one" [0:09:02]; when the model supplies wrong arguments or a bad ID, the action fails, which is why error feedback matters.

## Builds on

- [What Is an AI Agent](./what-is-an-ai-agent.md) - an agent is an LLM plus tools; tool calling is the ability that defines the category.
- [Tool Design](./tool-design.md) - how you shape and describe tools determines whether the model calls them correctly.

## Contrasts with

- [Structured Outputs](./structured-outputs.md) - both constrain the model to a schema, but structured outputs shape the final answer while tool calling triggers an external action mid-run.
- [Agents vs. Workflows](./agents-vs-workflows.md) - in a workflow the calls are hardcoded; tool calling lets the model itself decide when to act.

## Related

- [The Agent Loop (Reason-Act-Observe)](./agent-loop.md) - tool calls are the "act" step whose results feed the next reasoning pass.
- [Model Context Protocol (MCP)](./mcp.md) - a standard way to expose prepackaged tools to any agent.
- [Model Selection](./model-selection.md) - picking a model that reliably supports function calling.
- [Provider Independence](./provider-independence.md) - most providers converge on the same OpenAI-style calling format.
- [Agent Graphs](./agent-graphs.md) - tool nodes are where graph-based agents perform actions.
- [Context Window Limits](./context-window-limits.md) - every tool result consumes context and can bloat the conversation.

## Implemented by

- [Pydantic AI](../entities/tools/pydantic-ai.md), [LangChain](../entities/tools/langchain.md), [LangGraph](../entities/tools/langgraph.md), and [LangServe](../entities/tools/langserve.md) - Python frameworks that bind decorated functions as agent tools.
- [OpenAI Agents SDK](../entities/tools/openai-agents-sdk.md) and [OpenAI Swarm](../entities/tools/openai-swarm.md) - SDKs where a docstringed function becomes a callable tool.
- [n8n](../entities/tools/n8n.md), [Flowise](../entities/tools/flowise.md), and [Voiceflow](../entities/tools/voiceflow.md) - no-code builders that attach workflows and API endpoints as tools.
- [Ollama](../entities/tools/ollama.md) and [Llama](../entities/tools/llama.md) - local runtimes; only tool-labeled models can call functions.
- [Asana](../entities/tools/asana.md), [Brave Search API](../entities/tools/brave-search.md), and [GoHighLevel](../entities/tools/gohighlevel.md) - external services frequently wrapped as agent tools.

## Sources

- [OpenAI's BRAND NEW Agents SDK (Crash Course)](../sources/openais-brand-new-agents-sdk-crash-course.md) - "tools are how AI agents are given the ability to interact with the outside world to do things like search for flights Reserve hotels or get weather information" [0:11:39]
- [Are You Building REAL AI Agents or Just Using LLMs?](../sources/are-you-building-real-ai-agents-or-just-using-llms.md) - "the tools part of the agent node is just dangling here there's nothing given to it for it to interact with the environment so it's just a regular chatbot" [0:11:14]
- [Function Calling with ANY LLM for Local AI Agents (Feat. LangChain, HuggingFace, and Llama 3)](../sources/function-calling-with-any-llm-for-local-ai-agents-feat-langchain-huggingface-and-llama-3.md) - "function calling is one of the most powerful pieces of the latest and greatest large language models like GPT and Claw it's what allows them to seamlessly interact with external services on your behalf" [0:00:00]
- [Pydantic AI + DeepSeek V3 - The BEST AI Agent Combo](../sources/pydantic-ai-deepseek-v3-the-best-ai-agent-combo.md) - "all you have to do is Define a regular python function ... but you add this decorator at the top ... and that instantly turns this function into one of the tools available to the large language model" [0:09:00]
- [Ollama + OpenAI's Swarm - EASILY Run AI Agents Locally](../sources/ollama-openais-swarm-easily-run-ai-agents-locally.md) - "if you have a model that doesn't support tool calling it's not going to be able to actually act as an agent and invoke the tools that you have set up in your swarm code so you need specifically a model that has the tool label" [0:17:11]
- [Llama 3.2 is INSANE - But Does it Beat GPT as an AI Agent?](../sources/llama-32-is-insane-but-does-it-beat-gpt-as-an-ai-agent.md) - "local llms have generally not been good as AI agents because they don't do well with function calling otherwise known as tool calling and this is what enables llms to actually do things for you besides just generating text" [0:00:37]
- [Developers, THIS is How you Stay Relevant with AI - AI Agents Masterclass #1](../sources/developers-this-is-how-you-stay-relevant-with-ai-ai-agents-masterclass-1.md) - "the agent intelligently decides when it needs to actually run that function make that tool call based on the conversation" [0:15:08]
- [I Found the Limits of the Most Popular LLMs](../sources/i-found-the-limits-of-the-most-popular-llms.md) - "really what happened is it gave incorrect arguments to marking a task as complete" [0:18:23]
- [ChatGPT is the GIFT that keeps on GIVING - Introducing Auto-GPT](../sources/chatgpt-is-the-gift-that-keeps-on-giving-introducing-auto-gpt.md) - "this is a really powerful thing that GPT cannot do on its own you need something like this that actually provides an infrastructure for GPT to browse the internet to get this kind of stuff" [0:09:58]
