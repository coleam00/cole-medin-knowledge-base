---
type: entity
subtype: tool
title: "Uvicorn"
description: "The ASGI server used to host the FastAPI app, running on 0.0.0.0:8000."
resource: "https://www.uvicorn.org/"
tags: [asgi-server, api, deployment]
videos: [the-glow-up-every-ai-agent-needs, complete-guide-to-langserve-make-your-ai-agent-actually-useful]
created: 2026-07-21
updated: 2026-07-21
---

# Uvicorn

Uvicorn is the ASGI server Cole uses to actually run his Python agent APIs. When he wraps an agent as a web service, Uvicorn is the process that binds the app to a port and serves requests: "the last line of code here is just using uvicorn to run this app and I'm going to just have it hosted on 00000000 with Port 8000" ([0:05:44](../../sources/complete-guide-to-langserve-make-your-ai-agent-actually-useful.md)). Binding to `0.0.0.0` makes the endpoint reachable on all network interfaces, which is exactly what you want once the service leaves localhost for a container or cloud host. He describes the same role again while upgrading an agent: "we're using this python package called UV corn which is going to serve our endpoint on our Local Host" ([0:16:40](../../sources/the-glow-up-every-ai-agent-needs.md)).

Uvicorn is the runtime layer beneath [FastAPI](./fastapi.md): FastAPI defines the routes and the [request/response schema](../../concepts/request-response-schema.md), and Uvicorn is the ASGI server that runs that app and handles the actual connections. This pairing is how Cole turns an agent into an [agent-as-an-API-endpoint](../../concepts/agent-as-api-endpoint.md), the step that makes an agent [frontend-agnostic](../../concepts/frontend-agnostic-agent.md) so any client (a [Streamlit](./streamlit.md) UI, a mobile app, another service) can call it over HTTP. It is a small, invisible piece, but it is the one that makes the endpoint real.

Because it sits at the boundary between code and network, Uvicorn is also part of Cole's [agent deployment](../../concepts/agent-deployment.md) story: the container built with [Docker](./docker.md) typically starts Uvicorn as its entrypoint, serving the FastAPI app on port 8000 so a platform like [Render](./render.md) can route traffic to it.

## Related

- [Agent as an API Endpoint](../../concepts/agent-as-api-endpoint.md) - Uvicorn is what serves that endpoint
- [Frontend-Agnostic Agents](../../concepts/frontend-agnostic-agent.md) - an HTTP-served agent decouples from any single UI
- [Agent Request/Response Schema](../../concepts/request-response-schema.md) - the contract FastAPI defines and Uvicorn serves
- [Agent Deployment](../../concepts/agent-deployment.md) - Uvicorn is the container entrypoint that runs the API
- [Memory Systems](../../concepts/memory-systems.md), [Context Engineering](../../concepts/context-engineering.md) - surrounding topics in the source videos
- Sibling tools: [FastAPI](./fastapi.md), [LangServe](./langserve.md), [Docker](./docker.md), [Render](./render.md), [Streamlit](./streamlit.md)

## Sources

- [COMPLETE Guide to LangServe - Make Your AI Agent Actually Useful](../../sources/complete-guide-to-langserve-make-your-ai-agent-actually-useful.md) - "[0:05:44] the last line of code here is just using uvicorn to run this app and I'm going to just have it hosted on 00000000 with Port 8000"
- [The GLOW-UP Every AI Agent Needs](../../sources/the-glow-up-every-ai-agent-needs.md) - "[0:16:40] we're using this python package called UV corn which is going to serve our endpoint on our Local Host using Port 801"
