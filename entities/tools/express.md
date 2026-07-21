---
type: entity
subtype: tool
title: "Express.js"
description: "Minimal JavaScript web framework used to stand up the small backend API that holds the OpenAI key and proxies chat-completion requests for the browser client."
resource: "https://expressjs.com"
tags: [agent-framework, sdk, javascript, api, backend]
videos: [use-chatgpt-in-two-clicks-on-any-website-with-a-custom-chrome-extension]
created: 2026-07-21
updated: 2026-07-21
---

# Express.js

Express.js is the minimal JavaScript web framework Cole reaches for when a browser client needs a backend of its own. Building a Chrome extension that calls GPT from any text box, he introduces it in one line: "for the API I'm just going to create a very simple express.js API... it's a really powerful JavaScript API framework" ([0:14:35](../../sources/use-chatgpt-in-two-clicks-on-any-website-with-a-custom-chrome-extension.md)). The whole server is a single `server.js`: it reads the OpenAI key and organization id out of a `.env`, exposes one POST route, forwards the prompt to a chat completion with [GPT-3.5 Turbo](./gpt-3-5-turbo.md), trims the leading whitespace off the reply, and returns the text that the extension's content script writes back into the page.

The framework is deliberately thin and extended by two middleware packages: "there's a few libraries that I need to import like I said I'm using Express I'm using body parse and cores which are extensions of Express" ([0:15:20](../../sources/use-chatgpt-in-two-clicks-on-any-website-with-a-custom-chrome-extension.md)). body-parser lets the route read the JSON body the extension POSTs, and CORS lets a script injected into an arbitrary website call `localhost:3000` at all. That is the entire backend.

Express is in this build because of a security constraint, not a feature list. A browser extension cannot safely hold a provider API key, so the secret moves one hop back onto a server the user controls and the client only ever talks to that proxy. Cole closes by naming the productionization path from this local server: host the API publicly, put auth in front of it with something like [Firebase](./firebase.md), and add payments if you want to charge for it ([0:20:31](../../sources/use-chatgpt-in-two-clicks-on-any-website-with-a-custom-chrome-extension.md)). The same shape scales to any agent behind an HTTP endpoint.

## Realizes

- [Securing Agent APIs](../../concepts/api-security.md) - A small backend proxy holds the secret API key so a browser client never has to, and bearer-token auth keeps strangers off the endpoint.
- [Agent as an API Endpoint](../../concepts/agent-as-api-endpoint.md) - Wrapping the model call in a web API turns it from a script into a deployable service any frontend or client can call remotely.

## Contrasts with

- [FastAPI](./fastapi.md) - The Python web framework Cole uses for the same job whenever the agent itself is written in Python.

## Works with

- [Node.js](./nodejs.md) - The JavaScript runtime the Express server runs on.
- [GPT-3.5 Turbo](./gpt-3-5-turbo.md) - The chat-completion model the single route calls to generate the replacement text.
- [ChatGPT](./chatgpt.md) - The product experience the extension compresses into a right-click.
- [Firebase](./firebase.md) - Suggested auth layer once the API is hosted publicly rather than on localhost.

## Related

- [Chat Interfaces](../../concepts/chat-interfaces.md) - Wrapping a model in a surface people already use, here the text box of whatever site they are on.
- [Agent Deployment](../../concepts/agent-deployment.md) - Getting the API off localhost and onto a real host with networking and secrets handled.
- [Full-Stack AI Application](../../concepts/full-stack-ai-application.md) - Combining a real front end, an API, and a model call into one shipped product.

## Sources

- [Use ChatGPT in Two Clicks on ANY website with a Custom Chrome Extension](../../sources/use-chatgpt-in-two-clicks-on-any-website-with-a-custom-chrome-extension.md) - "[0:14:35] for the API I'm just going to create a very simple express.js API... it's a really powerful JavaScript API framework"
- [Use ChatGPT in Two Clicks on ANY website with a Custom Chrome Extension](../../sources/use-chatgpt-in-two-clicks-on-any-website-with-a-custom-chrome-extension.md) - "[0:15:20] there's a few libraries that I need to import like I said I'm using Express I'm using body parse and cores which are extensions of Express"
