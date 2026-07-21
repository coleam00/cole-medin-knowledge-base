---
type: source
title: "Use ChatGPT in Two Clicks on ANY website with a Custom Chrome Extension"
description: "You can build a simple Chrome extension backed by a small Express API that lets you invoke ChatGPT on any website via a right-click, replacing highlighted or in-box text with the model's response."
youtube_id: 3kI14Jpzj_E
url: https://www.youtube.com/watch?v=3kI14Jpzj_E
slug: use-chatgpt-in-two-clicks-on-any-website-with-a-custom-chrome-extension
published: 2023-05-09
duration: "0:21:56"
recency_rank: 195
raw: "../raw/use-chatgpt-in-two-clicks-on-any-website-with-a-custom-chrome-extension.md"
tags: [chrome-extension, chat-interfaces, api-security, tutorial]
created: 2026-07-21
updated: 2026-07-21
---

# Use ChatGPT in Two Clicks on ANY website with a Custom Chrome Extension

This 2023 tutorial walks through building a Chrome extension ("Chrome GPT") that removes the friction of leaving your current page to use ChatGPT. Instead of navigating to the OpenAI UI, signing in, selecting a model, prompting, copying, and pasting back, you right-click inside any text box (or highlight specific text), click the extension's context-menu option, and it replaces your text with GPT's response in place. Cole demonstrates it on Twitter, a YouTube comment box, and an online code editor.

The extension's anatomy is three parts. manifest.json is the metadata backbone declaring the manifest version, name, permissions, icons, a background service worker, and content scripts. background.js registers a right-click context-menu item and, on click, sends a message to content.js. content.js does the real work: it reads the active element's text (or the highlighted selection), shows a loading cursor, POSTs the prompt to a local API, then writes GPT's reply back into the text box (handling both textarea/input elements and contentEditable via ranges).

The browser can't safely hold an OpenAI key, so Cole stands up a minimal Express.js server (server.js) that reads the API key and org from a .env file, calls OpenAI's chat completion with gpt-3.5-turbo, trims leading whitespace, and returns the reply. He loads the unpacked extension via chrome://extensions, notes you must refresh pages to pick up a reloaded extension, and closes by outlining how to productionize it: host the API publicly, add auth (e.g. Firebase), and add Stripe for payments, plus richer prompt engineering for use cases like tweet replies or YouTube video summarization.

## Concepts covered

- [Chat Interfaces](../concepts/chat-interfaces.md)
- [Securing Agent APIs](../concepts/api-security.md)
- [Tool Design](../concepts/tool-design.md)
- [Agent Deployment](../concepts/agent-deployment.md)

## Entities

- [Cole Medin](../entities/people/cole-medin.md)
- [OpenAI](../entities/organizations/openai.md)
- [GitHub](../entities/tools/github.md)
- [Firebase](../entities/tools/firebase.md)
- [Stripe](../entities/organizations/stripe.md)

## Key moments

- **[0:00:00]** The friction problem: constantly switching to the ChatGPT UI to copy answers back to where you're working
- **[0:01:02]** Demo goal: a Chrome extension to interact with GPT on any website via right-click
- **[0:01:15]** Live demos on Twitter, a YouTube comment box, and an online code editor (highlighting a selection)
- **[0:04:32]** Chrome extensions are just HTML/CSS/JS, starting with manifest.json as the backbone
- **[0:06:07]** Manifest references a background service worker and content scripts
- **[0:07:00]** background.js registers the right-click context menu and messages content.js
- **[0:09:15]** content.js reads the active/highlighted text, calls the API, and writes the reply back
- **[0:13:02]** contentEditable elements must be handled differently using a range
- **[0:14:35]** Building a minimal Express.js API with a .env holding the OpenAI key
- **[0:16:12]** Server calls OpenAI chat completion with gpt-3.5-turbo on port 3000
- **[0:18:28]** Loading the unpacked extension via chrome://extensions and refreshing to reload it
- **[0:20:31]** Productionizing: public API, Firebase auth, Stripe payments, richer prompting like YouTube summarization

## Transcript

[Raw transcript](../raw/use-chatgpt-in-two-clicks-on-any-website-with-a-custom-chrome-extension.md)
