---
type: entity
subtype: tool
title: "Local AI Package"
description: "Cole's bundled collection of self-hosted AI services (database, n8n, Ollama, Open Web UI) that installs the whole stack together for free."
resource: "https://github.com/coleam00/local-ai-packaged"
tags: [local-ai, self-hosted, cole-project]
videos: [the-ultimate-guide-to-local-ai-and-ai-agents-the-future-is-here, ive-been-holding-back-on-youtube-but-not-anymore, build-a-chatgpt-style-app-for-your-n8n-ai-agents-in-minutes, create-your-own-private-local-ai-cloud-stack-in-under-20-minutes, introducing-archon-an-ai-agent-that-builds-ai-agents]
created: 2026-07-21
updated: 2026-07-21
---

# Local AI Package

The Local AI Package is Cole's own curated bundle of self-hosted AI services that installs an entire private stack in a few steps, so you never have to wire the pieces together yourself. He frames it as the assembly of a whole ecosystem: "the local AI package is the solution to bring all of that together curated for you to install in just a few steps." Originally seeded by the n8n team, Cole extended it into the collection he leans on daily: "I've extended to include all of these services so we've got n8n superbase olama open web UI flow wise quadrant and then recently I added CRX NG."

What makes it matter is that it turns the abstract goal of [Local & Self-Hosted AI](../../concepts/local-ai.md) into one command. Each component he covers separately elsewhere ships pre-integrated here: [Ollama](./ollama.md) for the models, [Open Web UI](./open-web-ui.md) for the chat frontend, [n8n](./n8n.md) for agent workflows, [Supabase](./supabase.md) for the database and vector store, [Flowise](./flowise.md) for no-code agents, and Qdrant plus SearXNG for retrieval and search. As Cole puts it, "everything I'm covering in this video can be done with the services included in the local AI package. So, honestly, this is probably the most convenient way to get everything up and running from scratch." That is the payoff: a fully private, free, self-hosted platform for models, [RAG](../../concepts/rag.md), [memory systems](../../concepts/memory-systems.md), and [agent deployment](../../concepts/agent-deployment.md), with none of the data leaving your infrastructure.

The package is also load-bearing for Cole's broader work. He calls it the foundation of his local-AI practice ("This local AI package is the core of everything that I do with local AI") and reuses it as scaffolding elsewhere: an early Archon design "would use the local AI package ... to spin up an isolated environment with the database." It is the practical embodiment of running your own AI cloud rather than renting one, and the same privacy-and-control argument that runs through his self-hosting videos.

## Related

- [Local & Self-Hosted AI](../../concepts/local-ai.md) - the package is the one-command realization of a fully local stack.
- [Model Selection](../../concepts/model-selection.md) - ships Ollama so any local model can be swapped in.
- [Agent Deployment](../../concepts/agent-deployment.md) - a private, self-hosted platform for deploying agents.
- [Memory Systems](../../concepts/memory-systems.md) - bundles the database and vector store agent memory needs.
- [Provider Independence](../../concepts/provider-independence.md) - keeps the whole stack off any single cloud provider.
- [Agent Security](../../concepts/agent-security.md) - privacy by default since nothing leaves your infrastructure.
- [Ollama](./ollama.md), [Open Web UI](./open-web-ui.md), [n8n](./n8n.md), [Supabase](./supabase.md), [Flowise](./flowise.md) - the services it packages together.
- [Archon](./archon.md) - reuses the package to spin up isolated environments.

## Sources

- [The Ultimate Guide to Local AI and AI Agents (The Future is Here)](../../sources/the-ultimate-guide-to-local-ai-and-ai-agents-the-future-is-here.md) - "[0:53:00] the local AI package is the solution to bring all of that together curated for you to install in just a few steps"
- [Create Your Own Private Local AI Cloud Stack in Under 20 Minutes](../../sources/create-your-own-private-local-ai-cloud-stack-in-under-20-minutes.md) - "[0:02:12] this package which was originally created by the n8n team I've extended to include all of these services so we've got n8n superbase olama open web UI flow wise quadrant and then recently I added CRX NG"
- [Build a ChatGPT Style App for Your n8n AI Agents in MINUTES](../../sources/build-a-chatgpt-style-app-for-your-n8n-ai-agents-in-minutes.md) - "[0:05:56] everything I'm covering in this video can be done with the services included in the local AI package. So, honestly, this is probably the most convenient way to get everything up and running from scratch."
- [Introducing Archon - an AI Agent that BUILDS AI Agents](../../sources/introducing-archon-an-ai-agent-that-builds-ai-agents.md) - "[0:15:58] then it would use the local AI package I've covered this on my channel a lot to spin up an isolate an environment with the database"
- [I've Been Holding Back on YouTube... But Not Anymore](../../sources/ive-been-holding-back-on-youtube-but-not-anymore.md) - "[0:07:26] I'm kicking it off actually this Wednesday with a local AI master class which I cannot wait for."
