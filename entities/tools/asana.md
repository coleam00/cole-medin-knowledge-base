---
type: entity
subtype: tool
title: "Asana"
description: "Task-management platform the agent integrates with; the chatbot creates real Asana tasks with due dates from natural-language requests."
resource: "https://asana.com/"
tags: [task-management, productivity, integration, crud, ai-agents]
videos: [qwen-just-casually-started-the-local-ai-revolution, llama-32-is-insane-but-does-it-beat-gpt-as-an-ai-agent, openais-o1-is-barely-usable-but-i-fixed-it, complete-guide-to-langserve-make-your-ai-agent-actually-useful, i-found-the-limits-of-the-most-popular-llms, youre-wasting-time-coding-your-ai-agents, the-best-tool-for-ai-agent-workflows-langgraph-full-guide, this-ai-agent-with-rag-manages-my-life, ai-is-too-expensive-if-you-dont-do-this, ai-agents-the-future-of-ai-or-a-passing-fad, new-llama-3-model-beats-gpt-and-claude-with-function-calling, i-finally-built-an-ai-agent-to-organize-my-life-ai-agents-masterclass-4, function-calling-with-any-llm-for-local-ai-agents-feat-langchain-huggingface-and-llama-3, ai-agents-just-got-sexy-ai-agents-masterclass-3, the-secret-sauce-for-simple-powerful-ai-apps-ai-agents-masterclass-2, developers-this-is-how-you-stay-relevant-with-ai-ai-agents-masterclass-1]
created: 2026-07-21
updated: 2026-07-21
---

# Asana

Asana is a project- and task-management platform, and across Cole's catalog it is *the* external service he reaches for when he wants to prove an LLM is actually an agent rather than a chatbot. As he frames it, "the platform that I'm going to use for this is called asana it's a really nice platform to manage projects and tasks it's something external that I'm going to be using with AI." It became the running example of the AI Agents Masterclass series: "this hooks into Asana which is my favorite task management platform and it can do literally anything that I need to do in Asana." The point is not Asana's feature set but that talking to a real, stateful third-party API is what turns a language model into a tool-using agent.

## How Cole uses it

The agent wraps Asana's REST API in a small set of deliberately **simple functions**, "create tasks ... create projects ... get tasks in a certain project," plus deleting tasks and marking them complete. Cole is explicit that the tools are thin CRUD wrappers, "basically just a bunch of crud operations for tasks and projects," and that he sets up the Tasks API specifically because "there are a bunch of different apis in asana." This is the practical face of [Tool Calling](../../concepts/tool-use.md) and [Tool Design](../../concepts/tool-design.md): give the model a handful of well-named functions and let the [agent loop](../../concepts/agent-loop.md) map a natural-language request onto them. In demo after demo the agent turns plain English into a real, dated task, "I need to uh bake cookies by Friday," "I need to go on a run by Tuesday," and the task shows up in Asana with the correct due date.

Because the wiring stays constant, Asana doubles as Cole's **function-calling benchmark harness**. Every time a new model lands (o1, Llama 3 and 3.2, Qwen, GPT-4o), he points the same Asana agent at it to see whether it can pick the right tool, populate arguments, and chain project and task operations, which is how he compares models as agents rather than as chatbots (see [Model Selection](../../concepts/model-selection.md)). The same tools are reused when he demonstrates orchestration frameworks (LangGraph, LangServe) and cost-cutting techniques, making Asana the stable backbone of his [agentic workflow engineering](../../concepts/agentic-workflow-engineering.md) teaching. One recurring gotcha he flags: an Asana SDK version bump changed task deletion, "you need to upgrade Asana from what we had in the last video otherwise the deletion of tasks will not work."

## Realizes

- [Tool Calling](../../concepts/tool-use.md) - Letting an LLM invoke external functions and APIs so it can take actions and fetch data beyond its parametric knowledge.
- [Tool Design](../../concepts/tool-design.md) - Designing agent tools to be few, single-purpose, and well-described (often via docstrings) so the model uses them reliably.
- [The Agent Loop (Reason-Act-Observe)](../../concepts/agent-loop.md) - The core agentic cycle where the LLM reasons, calls a tool, observes the result, and loops an unknown number of times until it decides to respond.

## Works with

- [n8n](./n8n.md) - A no-code AI automation platform for building agents and workflows that integrate with 500+ applications.
- [Zapier](./zapier.md) - Automation platform whose MCP server connects agents to 8,000+ apps (video sponsor).

## Related

- [Model Selection](../../concepts/model-selection.md) - Choosing the right LLM per task by trading off quality, speed, and cost, often routing easy requests to cheap models and hard ones to expensive models.
- [Retrieval-Augmented Generation (RAG)](../../concepts/rag.md) - Grounding an LLM's answers by retrieving relevant documents from an external knowledge base and injecting them into the prompt at query time.
- [Agentic Workflow Engineering](../../concepts/agentic-workflow-engineering.md) - Designing repeatable AI workflows as engineered systems with defined steps, orchestration, and background execution rather than ad-hoc prompting.

## Sources

- [I FINALLY Built an AI Agent to Organize my Life - AI Agents Masterclass #4](../../sources/i-finally-built-an-ai-agent-to-organize-my-life-ai-agents-masterclass-4.md) - "[0:00:26] this hooks into Asana which is my favorite task management platform and it can do literally anything that I need to do in Asana"
- [Developers, THIS is How you Stay Relevant with AI - AI Agents Masterclass #1](../../sources/developers-this-is-how-you-stay-relevant-with-ai-ai-agents-masterclass-1.md) - "[0:01:49] the platform that I'm going to use for this is called asana it's a really nice platform to manage projects and tasks it's something external that I'm going to be using with AI"
- [The Secret Sauce for SIMPLE + POWERFUL AI Apps - AI Agents Masterclass #2](../../sources/the-secret-sauce-for-simple-powerful-ai-apps-ai-agents-masterclass-2.md) - "[0:04:55] creating a list of tools where in this case we only have one tool create an Asana task"
- [AI Agents Just Got Sexy - AI Agents Masterclass #3](../../sources/ai-agents-just-got-sexy-ai-agents-masterclass-3.md) - "[0:08:37] let's try to actually create a task now on Asana so I'll say I need to go on a run by Tuesday ... created a task going to run by Tuesday July 9th"
- [Function Calling with ANY LLM for Local AI Agents (Feat. LangChain, HuggingFace, and Llama 3)](../../sources/function-calling-with-any-llm-for-local-ai-agents-feat-langchain-huggingface-and-llama-3.md) - "[0:02:27] Asana is a task management platform and because we need this AI agent to interact with an external service to really be an AI agent I chose to use Asana"
- [Llama 3.2 is INSANE - But Does it Beat GPT as an AI Agent?](../../sources/llama-32-is-insane-but-does-it-beat-gpt-as-an-ai-agent.md) - "[0:05:41] for Asana we have SIMPLE functions here to create tasks to create projects to get tasks in a certain project"
- [OpenAI's o1 is Barely Usable, but I Fixed it...](../../sources/openais-o1-is-barely-usable-but-i-fixed-it.md) - "[0:03:27] Asana is my favorite task management platform that I use every single day and so this agent is going to help me manage all my projects and tasks"
- [You're WASTING TIME Coding Your AI Agents](../../sources/youre-wasting-time-coding-your-ai-agents.md) - "[0:10:18] I need to uh bake cookies by Friday so we'll see if it'll make a task for me"
- [This AI Agent with RAG Manages MY LIFE](../../sources/this-ai-agent-with-rag-manages-my-life.md) - "[0:05:07] what we have right here is the Asana agent that we've already been building ... I have all my tools here for interacting with Asana doing things like creating projects and updating tasks"
- [COMPLETE Guide to LangServe - Make Your AI Agent Actually Useful](../../sources/complete-guide-to-langserve-make-your-ai-agent-actually-useful.md) - "[0:03:21] it's basically just a bunch of crud operations for tasks and projects"
- [THE BEST Tool for AI Agent Workflows - LangGraph FULL Guide](../../sources/the-best-tool-for-ai-agent-workflows-langgraph-full-guide.md) - "[0:22:17] it should go out to Asana and find the projects for me and then list them out"
- [Qwen Just Casually Started the Local AI Revolution](../../sources/qwen-just-casually-started-the-local-ai-revolution.md) - "[0:11:44] it's going to call the get as projects tool gets the Json result from the Asana API and then it tells me our projects"
- [New Llama 3 Model BEATS GPT and Claude with Function Calling!?](../../sources/new-llama-3-model-beats-gpt-and-claude-with-function-calling.md) - "[0:03:18] this agent it helps me manage my tasks in Asana which is my favorite task management software"
- [I Found the Limits of the Most Popular LLMs](../../sources/i-found-the-limits-of-the-most-popular-llms.md) - "[0:08:12] creating projects managing tasks deleting tasks marketing those as complete all that good stuff"
- [AI is TOO EXPENSIVE if You Don't Do This](../../sources/ai-is-too-expensive-if-you-dont-do-this.md) - "[0:03:15] we have a bunch of tools to interact with Asana things like creating projects for us deleting tasks for us marking them as complete"
- [AI Agents: The Future of AI or a Passing Fad?](../../sources/ai-agents-the-future-of-ai-or-a-passing-fad.md) - "[0:04:12] when a user requests something that would need to create a task in Asana or use the stripe API"
