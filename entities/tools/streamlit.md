---
type: entity
subtype: tool
title: "Streamlit"
description: "Used to build the travel-planner's chat UI, where users set preferences and watch the streamed synthesizer output."
resource: "https://streamlit.io"
tags: [python-ui, chat-interface, rapid-prototyping]
videos: [googles-agents-cli-the-cli-skills-combination-to-ship-ai-agents-easily, why-is-everyone-missing-this-with-ai-agents-memory-tools-that-scale, the-3-must-have-mcp-servers-for-any-ai-coding-and-how-to-use-them, turn-any-website-into-llm-knowledge-in-seconds-evolved, 10x-your-ai-agents-with-this-one-agent-architecture, openais-brand-new-agents-sdk-crash-course, build-ai-agents-that-evolve-over-time, this-is-hands-down-the-best-way-to-build-ai-agents, the-future-of-rag-is-agentic-learn-this-strategy-now, turn-any-website-into-llm-knowledge-in-seconds, revealing-my-complete-ai-agent-blueprint, weve-been-building-ai-agents-wrong-until-now, claude-computer-use-boltnew-the-ultimate-ai-coding-combo, qwen-just-casually-started-the-local-ai-revolution, build-a-full-stack-app-for-your-n8n-ai-agent-in-20-minutes, llama-32-is-insane-but-does-it-beat-gpt-as-an-ai-agent, dont-sleep-on-the-ultimate-ai-agent-combo-n8n-langchain-python, openais-o1-is-barely-usable-but-i-fixed-it, complete-guide-to-langserve-make-your-ai-agent-actually-useful, i-found-the-limits-of-the-most-popular-llms, youre-wasting-time-coding-your-ai-agents, the-best-tool-for-ai-agent-workflows-langgraph-full-guide, this-ai-agent-with-rag-manages-my-life, ai-is-too-expensive-if-you-dont-do-this, the-most-value-packed-rag-guide-on-youtube-feat-llama-31-405b, new-llama-3-model-beats-gpt-and-claude-with-function-calling, build-a-hilarious-ai-game-from-scratch-in-10-minutes, i-finally-built-an-ai-agent-to-organize-my-life-ai-agents-masterclass-4, function-calling-with-any-llm-for-local-ai-agents-feat-langchain-huggingface-and-llama-3, ai-agents-just-got-sexy-ai-agents-masterclass-3, i-made-a-custom-ai-chatbot-site-in-47-lines-of-code]
created: 2026-07-21
updated: 2026-07-21
---

# Streamlit

Streamlit is Cole's default Python UI library, and it is the front end that appears in more of his agent videos than any other. He calls it "a fantastic and really easy to use Python UI library... it's made for interacting with llms" ([0:08:42](../../sources/revealing-my-complete-ai-agent-blueprint.md)), and the reason he reaches for it every time is speed: "it just makes it so easy to build something beautiful really fast so I love using Streamlit in my videos" ([0:19:01](../../sources/weve-been-building-ai-agents-wrong-until-now.md)). With no JavaScript required, "it's a python package that makes it super easy to build websites no need for JavaScript at all" ([0:01:18](../../sources/build-a-full-stack-app-for-your-n8n-ai-agent-in-20-minutes.md)), it lets him put a usable [chat interface](../../concepts/chat-interfaces.md) in front of any agent in a few lines, which is why it is his go-to for [rapid prototyping](../../concepts/rapid-prototyping.md) and demos.

The idioms recur across the catalog. Everything is built by calling `st.` components, and the app runs with a single `streamlit run <script>` command that opens in the browser with hot reloading, so "any changes you make to your code will automatically be reflected in your site without having to rerun anything" ([0:14:03](../../sources/ai-agents-just-got-sexy-ai-agents-masterclass-3.md)). Because Streamlit re-executes the whole script on every interaction, Cole leans hard on its caching decorators (`st.cache_resource`) to avoid re-instantiating models each rerun, a pattern he repeats in his RAG and function-calling builds. He also uses its streaming support to deliver [streaming responses](../../concepts/streaming-responses.md): "I actually stream this out so instead of it being just like boom here's all the text at once it streams it out in typewriter style" ([0:42:33](../../sources/the-future-of-rag-is-agentic-learn-this-strategy-now.md)).

Functionally, Streamlit is the demonstration surface for nearly every agent architecture Cole teaches. It fronts his travel-planner ([10x Your AI Agents](../../sources/10x-your-ai-agents-with-this-one-agent-architecture.md)), his RAG assistants, his [Pydantic AI](./pydantic-ai.md) and [LangGraph](./langgraph.md) agents, his local-LLM tests, and his life-organizing task agents. It is deliberately a thin presentation layer: it lets viewers see and interact with the agent so the real subject (the [model](../../concepts/model-selection.md), the [tools](../../concepts/tool-use.md), the [workflow](../../concepts/agentic-workflow-engineering.md)) is what gets attention. When he needs a production API instead of a demo UI, he swaps Streamlit out for [FastAPI](./fastapi.md) plus [Uvicorn](./uvicorn.md).

## Realizes

- [Chat Interfaces](../../concepts/chat-interfaces.md) - Wrapping agents in chat surfaces (websites, DMs, platforms) with adapters, a shared message format, and durable history.
- [Rapid Prototyping](../../concepts/rapid-prototyping.md) - Building a fast proof of concept with managed services first, then hardening only what proves out, instead of over-engineering up front.
- [Streaming Responses](../../concepts/streaming-responses.md) - Streaming tokens and intermediate agent output to the user in real time instead of waiting for the full response.
- [Human in the Loop](../../concepts/human-in-the-loop.md) - Keeping a human as the approver and steerer of agentic work rather than fully automating, so AI augments engineers instead of replacing them.

## Contrasts with

- [FastAPI](./fastapi.md) - Python web framework used to serve the swapped-in Python agent endpoint that streams AG-UI events.
- [Uvicorn](./uvicorn.md) - The ASGI server used to host the FastAPI app, running on 0.0.0.0:8000.

## Works with

- [Pydantic AI](./pydantic-ai.md) - Cole's framework for the individual agents, structured around three parts: dependencies, the agent definition, and tools.
- [LangGraph](./langgraph.md) - The orchestration framework wiring agents into a stateful graph of nodes and edges, used here to run agents in parallel and add human-in-the-loop.
- [LangServe](./langserve.md) - LangChain's library that wraps any chain or LangGraph runnable in a FastAPI web server via a single add_routes call, plus a RemoteRunnable client.
- [n8n](./n8n.md) - A no-code AI automation platform for building agents and workflows that integrate with 500+ applications.

## Related

- [Full-Stack AI Application](../../concepts/full-stack-ai-application.md) - Combining an AI agent with a real front end, database, and API integrations, with the agent acting as the brain connecting the UI to back-end services.
- [Tool Use](../../concepts/tool-use.md) - Letting an LLM invoke external functions and APIs so it can take actions and fetch data beyond its parametric knowledge.
- [Model Selection](../../concepts/model-selection.md) - Choosing the right LLM per task by trading off quality, speed, and cost, often routing easy requests to cheap models and hard ones to expensive models.
- [Retrieval-Augmented Generation (RAG)](../../concepts/rag.md) - Grounding an LLM's answers by retrieving relevant documents from an external knowledge base and injecting them into the prompt at query time.
- [Agentic Workflow Engineering](../../concepts/agentic-workflow-engineering.md) - Designing repeatable AI workflows as engineered systems with defined steps, orchestration, and background execution rather than ad-hoc prompting.

## Sources

- [Revealing my COMPLETE AI Agent Blueprint](../../sources/revealing-my-complete-ai-agent-blueprint.md) - "[0:08:42] Streamlit is a fantastic and really easy to use Python UI library... it's made for interacting with llms"
- [We've Been Building AI Agents WRONG Until Now](../../sources/weve-been-building-ai-agents-wrong-until-now.md) - "[0:19:01] it just makes it so easy to build something beautiful really fast so I love using Streamlit in my videos"
- [Build a FULL Stack App for your n8n AI Agent in 20 Minutes](../../sources/build-a-full-stack-app-for-your-n8n-ai-agent-in-20-minutes.md) - "[0:01:18] Streamlit it's a python package that makes it super easy to build websites no need for JavaScript at all"
- [AI Agents Just Got Sexy - AI Agents Masterclass #3](../../sources/ai-agents-just-got-sexy-ai-agents-masterclass-3.md) - "[0:14:03] streamlit automatically has hot reloading Incorporated so any changes you make to your code will automatically be reflected in your site without having to rerun anything"
- [The Future of RAG is Agentic - Learn this Strategy NOW](../../sources/the-future-of-rag-is-agentic-learn-this-strategy-now.md) - "[0:42:33] I actually stream this out so instead of it being just like boom here's all the text at once it streams it out in typewriter style"
- [10x Your AI Agents with this ONE Agent Architecture](../../sources/10x-your-ai-agents-with-this-one-agent-architecture.md) - "[0:04:25] we even have a Streamlit user interface built out for this travel planner assistant"
- [I Made a Custom AI Chatbot Site in 47 Lines of Code](../../sources/i-made-a-custom-ai-chatbot-site-in-47-lines-of-code.md) - "[0:07:31] there's a lot there to make this a robust UI right out the bat without having to do a ton of custom coding with react or vanilla JavaScript HTML and CSS"
- [Google's Agents CLI: The CLI + Skills Combination to Ship AI Agents EASILY](../../sources/googles-agents-cli-the-cli-skills-combination-to-ship-ai-agents-easily.md)
- [Why is Everyone Missing This with AI Agents?! (Memory + Tools that Scale)](../../sources/why-is-everyone-missing-this-with-ai-agents-memory-tools-that-scale.md)
- [The 3 MUST Have MCP Servers for Any AI Coding (and How to Use Them)](../../sources/the-3-must-have-mcp-servers-for-any-ai-coding-and-how-to-use-them.md)
- [Turn ANY Website into LLM Knowledge in Seconds - EVOLVED](../../sources/turn-any-website-into-llm-knowledge-in-seconds-evolved.md)
- [OpenAI's BRAND NEW Agents SDK (Crash Course)](../../sources/openais-brand-new-agents-sdk-crash-course.md)
- [Build AI Agents that EVOLVE Over Time](../../sources/build-ai-agents-that-evolve-over-time.md)
- [This is Hands Down the BEST Way to Build AI Agents](../../sources/this-is-hands-down-the-best-way-to-build-ai-agents.md)
- [Turn ANY Website into LLM Knowledge in SECONDS](../../sources/turn-any-website-into-llm-knowledge-in-seconds.md)
- [Claude Computer Use + Bolt.new - The ULTIMATE AI Coding Combo?!](../../sources/claude-computer-use-boltnew-the-ultimate-ai-coding-combo.md)
- [Qwen Just Casually Started the Local AI Revolution](../../sources/qwen-just-casually-started-the-local-ai-revolution.md)
- [Llama 3.2 is INSANE - But Does it Beat GPT as an AI Agent?](../../sources/llama-32-is-insane-but-does-it-beat-gpt-as-an-ai-agent.md)
- [Don't Sleep on the ULTIMATE AI Agent Combo (n8n, LangChain, Python)](../../sources/dont-sleep-on-the-ultimate-ai-agent-combo-n8n-langchain-python.md)
- [OpenAI's o1 is Barely Usable, but I Fixed it...](../../sources/openais-o1-is-barely-usable-but-i-fixed-it.md)
- [COMPLETE Guide to LangServe - Make Your AI Agent Actually Useful](../../sources/complete-guide-to-langserve-make-your-ai-agent-actually-useful.md)
- [I Found the Limits of the Most Popular LLMs](../../sources/i-found-the-limits-of-the-most-popular-llms.md)
- [You're WASTING TIME Coding Your AI Agents](../../sources/youre-wasting-time-coding-your-ai-agents.md)
- [THE BEST Tool for AI Agent Workflows - LangGraph FULL Guide](../../sources/the-best-tool-for-ai-agent-workflows-langgraph-full-guide.md)
- [This AI Agent with RAG Manages MY LIFE](../../sources/this-ai-agent-with-rag-manages-my-life.md)
- [AI is TOO EXPENSIVE if You Don't Do This](../../sources/ai-is-too-expensive-if-you-dont-do-this.md)
- [The Most Value Packed RAG Guide on YouTube (Feat. Llama 3.1 405B!)](../../sources/the-most-value-packed-rag-guide-on-youtube-feat-llama-31-405b.md)
- [New Llama 3 Model BEATS GPT and Claude with Function Calling!?](../../sources/new-llama-3-model-beats-gpt-and-claude-with-function-calling.md)
- [Build a Hilarious AI Game from SCRATCH in 10 Minutes](../../sources/build-a-hilarious-ai-game-from-scratch-in-10-minutes.md)
- [I FINALLY Built an AI Agent to Organize my Life - AI Agents Masterclass #4](../../sources/i-finally-built-an-ai-agent-to-organize-my-life-ai-agents-masterclass-4.md)
- [Function Calling with ANY LLM for Local AI Agents](../../sources/function-calling-with-any-llm-for-local-ai-agents-feat-langchain-huggingface-and-llama-3.md)
