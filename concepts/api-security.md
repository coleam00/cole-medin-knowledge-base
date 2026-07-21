---
type: concept
title: "Securing Agent APIs"
description: "Protecting agent endpoints and secrets: bearer-token header auth stops strangers from calling a public agent webhook and draining LLM credits, while a small backend proxy holds the secret API key so a browser client never has to."
tags: [api, security, auth, bearer-token, proxy, backend]
videos: [build-a-chatgpt-style-app-for-your-n8n-ai-agents-in-minutes, use-chatgpt-in-two-clicks-on-any-website-with-a-custom-chrome-extension]
created: 2026-07-21
updated: 2026-07-21
---

# Securing Agent APIs

The moment an agent becomes an [API endpoint](./agent-as-api-endpoint.md) on the public internet, anyone who finds the URL can call it, and every call spends your money. As Cole puts it, "when we have a public URL to communicate with our workflow that means anybody could just theoretically call into this and spend our LLM credits. And so we want to protect this endpoint with header authentication as well." [0:12:21] Securing an agent API is about two distinct problems: keeping strangers out, and keeping your secret keys off the client.

The first is solved with **bearer-token header auth**. You set a shared secret and require every request to carry it in a header: "the value is going to be bearer and then space whatever token you want to set... you're going to go back into open web UI and you're going to add that right here." [0:13:08] The endpoint rejects any request without the matching token, so a public URL stops being an open door. This is the minimum bar for any agent webhook exposed to the internet.

The second problem is that a raw API key must never live in browser-side code, where anyone can read it. The fix is a small backend that holds the secret and proxies requests to the model provider. In the Chrome-extension build, "the only thing we have to do before we actually use this is create that API for making the requests to GPT" [0:14:35], and the key stays server-side: "you do have to have a DOT EnV file here the same directory as server.js where you would give your openai API key and openai organization." [0:14:52] The client talks only to your proxy, never directly to OpenAI, so the credential is never shipped to the user. That proxy is just another small service, hosting "the model we want to use GPT 3.5... and then the port that we're going to host this on is 3000." [0:16:12]

## Prerequisites

- [Agent as an API Endpoint](./agent-as-api-endpoint.md)

## Part of

- [Agent Deployment](./agent-deployment.md)

## Related

- [Agent Security](./agent-security.md)
- [Reverse Proxy](./reverse-proxy.md)
- [Webhook Tool Pattern](./webhook-tool-pattern.md)
- [Chat Interfaces](./chat-interfaces.md)
- [Local & Self-Hosted AI](./local-ai.md)
- [MCP Authentication with OAuth](./mcp-oauth.md) - Putting an OAuth provider (e.g. GitHub) in front of an MCP server as an authentication gateway so only authorized users can reach its tools.

## Tools

- [n8n](../entities/tools/n8n.md) - where header auth is added to protect a public webhook.
- [Open Web UI](../entities/tools/open-web-ui.md) - the client that supplies the bearer token on each call.
- [OpenAI](../entities/organizations/openai.md) - the model provider whose key the backend proxy keeps hidden.
- [Google Cloud Functions](../entities/tools/google-cloud-functions.md) - Google's serverless function platform, used as the HTTP endpoint that receives the GoHighLevel webhook and hosts the agent's request-handling backend.
- [GPT-3.5 Turbo](../entities/tools/gpt-3-5-turbo.md) - OpenAI's ChatGPT-era chat-completion model called by the proxy server to generate the text that replaces the user's selection in place.

## Sources

- [Build a ChatGPT Style App for Your n8n AI Agents in MINUTES](../sources/build-a-chatgpt-style-app-for-your-n8n-ai-agents-in-minutes.md) - "[0:12:21] when we have a public URL to communicate with our workflow that means anybody could just theoretically call into this and spend our LLM credits. And so we want to protect this endpoint with header authentication as well."
- [Use ChatGPT in Two Clicks on ANY website with a Custom Chrome Extension](../sources/use-chatgpt-in-two-clicks-on-any-website-with-a-custom-chrome-extension.md) - "[0:14:52] you do have to have a DOT EnV file here the same directory as server.js where you would give your openai API key and openai organization"
