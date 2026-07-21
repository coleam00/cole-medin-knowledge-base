---
type: source
title: "COMPLETE Guide to LangServe - Make Your AI Agent Actually Useful"
description: "Any agent built with LangChain/LangGraph can be turned into a scalable, always-on cloud API in minutes by wrapping it with LangServe and deploying it to a cheap DigitalOcean droplet."
youtube_id: qgH_KFSFMUE
url: https://www.youtube.com/watch?v=qgH_KFSFMUE
slug: complete-guide-to-langserve-make-your-ai-agent-actually-useful
published: 2024-09-01
duration: "0:17:18"
recency_rank: 169
raw: "../raw/complete-guide-to-langserve-make-your-ai-agent-actually-useful.md"
tags: [agent-deployment, langserve, api, langgraph]
created: 2026-07-21
updated: 2026-07-21
---

# COMPLETE Guide to LangServe - Make Your AI Agent Actually Useful

Cole walks through taking a LangGraph agent (from his AI agents masterclass) off his local machine and deploying it to the cloud as a production API endpoint. The magic tool is LangServe, which wraps any LangChain chain or LangGraph runnable in a FastAPI app with a single `add_routes` call. He shows the three-file structure: `runnable.py` (the LangGraph app with a tool-bound model, agent node, tool node, and a conditional router), `langserve_endpoints.py` (FastAPI plus LangServe plus uvicorn), and the Streamlit `chatbot.py` front end.

The headline claim is that only three lines of code change in the front end: import `RemoteRunnable` from LangServe, read the endpoint URL from an environment variable, and instantiate a `RemoteRunnable` pointed at that URL instead of calling the local runnable directly. This lets the same Streamlit UI talk to a remote agent transparently.

The bulk of the video is a step-by-step DigitalOcean deployment: spin up a $7 a month Ubuntu droplet, clone the repo, install pyenv and create a virtualenv, `pip install --no-cache-dir` the requirements (memory-constrained 1GB droplet), populate the `.env` with API keys, open port 8000 with `ufw`, run the endpoint, verify via the auto-generated `/docs` page, and finally point the front end's endpoint env var at the droplet's IPv4 (over plain HTTP, no SSL or auth in this basic version). He tests with an Asana query and confirms the agent's tool calls execute in the cloud.

## Concepts covered

- [Agent Deployment](../concepts/agent-deployment.md)
- [Agent as an API Endpoint](../concepts/agent-as-api-endpoint.md)
- [Agent Protocols](../concepts/agent-protocols.md)
- [Tool Calling](../concepts/tool-use.md)
- [Graph-Based Agent Workflows](../concepts/langgraph-nodes-edges-state.md)
- [Model Selection](../concepts/model-selection.md)
- [Firewall Configuration](../concepts/firewall-configuration.md)

## Entities

- [LangServe](../entities/tools/langserve.md)
- [LangGraph](../entities/tools/langgraph.md)
- [LangChain](../entities/tools/langchain.md)
- [FastAPI](../entities/tools/fastapi.md)
- [Uvicorn](../entities/tools/uvicorn.md)
- [DigitalOcean](../entities/organizations/digital-ocean.md)
- [Streamlit](../entities/tools/streamlit.md)
- [Asana](../entities/tools/asana.md)
- [OpenAI](../entities/organizations/openai.md)
- [Anthropic](../entities/organizations/anthropic.md)
- [Groq](../entities/organizations/groq.md)
- [Cole Medin](../entities/people/cole-medin.md)

## Key moments

- **[0:00:00]** Pitch: put a custom-coded AI agent behind a single scalable cloud API running 24/7
- **[0:01:02]** Roadmap: FastAPI plus LangServe endpoint, 3-line front-end change, DigitalOcean deploy, test
- **[0:02:54]** Overview of the LangGraph agent: OpenAI/Anthropic/Groq model plus Asana CRUD tools
- **[0:03:39]** Graph structure: agent node, tool node, conditional router edge, memory checkpointer
- **[0:04:31]** Defining LangServe endpoints: FastAPI app plus CORS middleware plus add_routes
- **[0:06:15]** The three lines: import RemoteRunnable, read URL env var, instantiate RemoteRunnable
- **[0:07:26]** Create a $7 a month premium AMD Ubuntu droplet on DigitalOcean
- **[0:09:31]** Clone repo, install pyenv, create and activate virtualenv
- **[0:11:07]** pip install -r requirements.txt --no-cache-dir on the memory-limited droplet
- **[0:12:34]** Open port 8000 via ufw enable, allow, reload
- **[0:13:49]** Verify the running endpoint via the /docs page in the browser
- **[0:15:44]** Test: "what projects do I have in Asana" returns real projects from the cloud agent

## Transcript

[Raw transcript](../raw/complete-guide-to-langserve-make-your-ai-agent-actually-useful.md)
