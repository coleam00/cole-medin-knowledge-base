---
type: entity
subtype: tool
title: "GPT-3.5 Turbo"
description: "OpenAI's ChatGPT-era chat-completion model called by the proxy server to generate the text that replaces the user's selection in place."
tags: [llm, model, api, security, backend, openai]
videos: [use-chatgpt-in-two-clicks-on-any-website-with-a-custom-chrome-extension]
created: 2026-07-21
updated: 2026-07-21
---

# GPT-3.5 Turbo

GPT-3.5 Turbo is the chat-completion model behind the original [ChatGPT](./chatgpt.md), and in Cole's 2023 Chrome-extension build it is the engine that rewrites whatever text you highlight. The configuration is a single line in the server: "[0:16:12] from the model we want to use GPT 3.5 which is chat GPT and then the port that we're going to host this on is 3000." Nothing about the model is special in the build; what matters is the plumbing that lets a browser extension reach it safely.

That plumbing is the lesson the page carries forward. A browser cannot hold an API key, so the extension never talks to OpenAI at all: "[0:14:35] the only thing we have to do before we actually use this is create that API for making the requests to GPT." The key lives server-side in an environment file, not in shipped JavaScript: "[0:14:52] you do have to have a DOT EnV file here the same directory as server.js where you would give your openai API key and openai organization." The small [Express.js](./express.md) proxy that results is the earliest appearance in Cole's catalog of a pattern he keeps reusing, a thin backend whose whole job is to hold credentials and forward requests.

Historically the model is a marker. GPT-3.5 Turbo was the first version of ChatGPT most developers could call from code, and it defined the chat-completion request shape (messages, roles, temperature) that later models inherited. Cole's productionization notes at the end of the video (host the API publicly, add auth, add payments) describe turning that proxy into a product, which is the same arc as any modern agent moving from local script to deployed service.

## Realizes

- [Securing Agent APIs](../../concepts/api-security.md) - Keeping the model key out of the client and behind a small backend proxy so it cannot be lifted from shipped code.
- [Chat Interfaces](../../concepts/chat-interfaces.md) - Wrapping a model in a surface people already use, here a right-click menu on any web page instead of a chat window.
- [Agent Deployment](../../concepts/agent-deployment.md) - Moving from a locally hosted endpoint on port 3000 to a public, authenticated, billable service.
- [Prompt Engineering](../../concepts/prompt-engineering.md) - Shaping the request text so a general chat model produces a usable in-place replacement for the selection.
- [Tool Design](../../concepts/tool-design.md) - Giving the model one narrow, well-specified job rather than a general assistant surface.

## Contrasts with

- [GPT-4](./gpt-4.md) - The stronger successor Cole cites as reasoning step by step without being told to, capability this model lacked.

## Works with

- [Express.js](./express.md) - Minimal JavaScript web framework used to stand up the backend API that holds the OpenAI key and proxies chat-completion requests for the browser client.
- [Node.js](./nodejs.md) - The runtime the proxy server runs on, started locally alongside the unpacked extension.
- [ChatGPT](./chatgpt.md) - The product this model powers, and the interface the extension exists to avoid switching to.
- [Firebase](./firebase.md) - The auth layer Cole names when outlining how to productionize the proxy.

## Related

- [GPT-4o](./gpt-4o.md) - The later flagship in the same chat-completion lineage, used where quality matters more than price.
- [GPT-4o mini](./gpt-4o-mini.md) - The modern equivalent of this model's role, the cheap default for high-volume, low-reasoning calls.
- [Model Selection](../../concepts/model-selection.md) - Trading quality against speed and cost, the choice this build makes implicitly by taking the cheapest chat model available.
- [The Evolution of AI Coding](../../concepts/the-evolution-of-ai-coding.md) - The arc from copy-paste-from-a-chat-window to agents that act in place, which this extension was an early attempt at collapsing.

## Sources

- [Use ChatGPT in Two Clicks on ANY website with a Custom Chrome Extension](../../sources/use-chatgpt-in-two-clicks-on-any-website-with-a-custom-chrome-extension.md) - "[0:14:35] the only thing we have to do before we actually use this is create that API for making the requests to GPT"
- [Use ChatGPT in Two Clicks on ANY website with a Custom Chrome Extension](../../sources/use-chatgpt-in-two-clicks-on-any-website-with-a-custom-chrome-extension.md) - "[0:14:52] you do have to have a DOT EnV file here the same directory as server.js where you would give your openai API key and openai organization"
- [Use ChatGPT in Two Clicks on ANY website with a Custom Chrome Extension](../../sources/use-chatgpt-in-two-clicks-on-any-website-with-a-custom-chrome-extension.md) - "[0:16:12] from the model we want to use GPT 3.5 which is chat GPT and then the port that we're going to host this on is 3000"
