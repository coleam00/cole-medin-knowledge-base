---
type: entity
subtype: tool
title: "Docker"
description: "Containerization prerequisite; a single docker compose command spins up Archon's four containers (agents, MCP server, UI, API server)."
resource: "https://www.docker.com"
tags: [containerization, deployment, local-ai]
videos: [omnigent-the-new-meta-harness-for-every-coding-agent-claude-code-codex-pi-more, learn-90-of-building-ai-agents-in-30-minutes, the-official-archon-guide-10x-your-ai-coding-workflow, docker-just-made-using-mcp-servers-100x-easier-one-click-installs, build-your-first-voice-ai-agent-in-20-minutes-with-livekit-open-source, the-true-power-of-ai-coding-build-your-own-workflows-full-guide, knowledge-graphs-in-n8n-are-finally-here, archon-beta-launch-livestream-what-you-missed, the-ultimate-guide-to-local-ai-and-ai-agents-the-future-is-here, how-id-learn-ai-agents-fast-if-i-had-to-start-over-full-roadmap, i-built-the-ultimate-rag-mcp-server-for-ai-coding-better-than-context7, the-ultimate-guide-to-building-your-own-mcp-servers-free-template, code-100x-faster-with-ai-heres-how-no-hype-full-process, claude-mcp-has-changed-ai-forever-heres-what-you-need-to-know, create-your-own-private-local-ai-cloud-stack-in-under-20-minutes, introducing-archon-an-ai-agent-that-builds-ai-agents, run-supabase-100-locally-for-your-ai-agents, deploying-billions-of-ai-agents-is-easier-than-you-think, n8n-crawl4ai-scrape-any-website-in-minutes-with-no-code, im-hosting-a-huge-ai-hackathon-competition, revealing-my-complete-ai-agent-blueprint, flowise-n8n-the-best-no-code-local-ai-agent-combo, claude-computer-use-boltnew-the-ultimate-ai-coding-combo, were-taking-this-ai-coding-assistant-to-the-moon-plus-installation-instructions, this-boltnew-fork-is-exploding-dont-miss-out-on-whats-happening, use-open-webui-with-your-n8n-ai-agents-voice-chat-included, deploy-any-ai-app-to-the-cloud-fast, run-all-your-ai-locally-in-minutes-llms-rag-and-more, local-vs-cloud-llmsrag-lets-finally-end-this-debate]
created: 2026-07-21
updated: 2026-07-21
---

# Docker

Docker is the containerization platform Cole treats as the near-universal prerequisite for shipping AI software, and it is the single most-recurring tool across his catalog. He frames it in one line: "Docker is my method for packaging up any application especially AI agents that I want to deploy to the cloud" ([0:26:35](../../sources/learn-90-of-building-ai-agents-in-30-minutes.md)). A container bundles code plus its full environment into one reproducible image, so the same thing runs identically on his laptop, a VPS, or a GPU host. That reproducibility is why Docker underpins both of his major workflows: local self-hosted stacks and cloud [agent deployment](../../concepts/agent-deployment.md).

The dominant pattern in his videos is `docker compose`, a single command that pulls and wires many services together. For [Archon](./archon.md) he pastes one line and "it's going to build all of our archon containers at the same time. We got one for our user interface, one for the MCP server, and one for all of the API endpoints" ([0:08:30](../../sources/the-official-archon-guide-10x-your-ai-coding-workflow.md)). His local AI stack works the same way: "all of these local AI services that I've curated for you, they all run as individual Docker containers that are all combined together in a stack" ([0:44:00](../../sources/the-ultimate-guide-to-local-ai-and-ai-agents-the-future-is-here.md)), each tool ([Supabase](./supabase.md), [Ollama](./ollama.md), [n8n](./n8n.md), [Crawl4AI](./crawl4ai.md), [Open WebUI](../../sources/use-open-webui-with-your-n8n-ai-agents-voice-chat-included.md)) defined in one compose file.

Docker is also his default recommendation for running [MCP](../../concepts/mcp.md) servers, both via Docker Desktop's MCP toolkit ("the only thing you have to do is install Docker Desktop") and the Docker MCP gateway that his [LiveKit](../../sources/build-your-first-voice-ai-agent-in-20-minutes-with-livekit-open-source.md) voice agent connects to over streamable HTTP. For production, he recommends containerizing every agent because it makes deployment identical and scalable: "it's all running the same Docker container that is the beauty of Docker and what makes it so scalable and so easy to deploy" ([0:09:29](../../sources/deploying-billions-of-ai-agents-is-easier-than-you-think.md)). He adds a coding-workflow reason too: LLMs write Docker configs well "just because it's been around for so long. There's so many examples of it on the internet."

## Realizes

- [Containerization & Docker Networking](../../concepts/containerization.md) - Running each service and your own agent as Docker containers in one stack so they communicate over a private network by service name, and exposing a tool as a Dockerized HTTP API when it can't be installed natively.

## Works with

- [Archon](./archon.md) - Cole's free, open-source AI command center and harness builder for AI coding; started as an AI agent that builds other AI agents.
- [Ask Gordon](./ask-gordon.md) - The AI agent built directly into Docker Desktop and wired to the MCP Toolkit by default, useful as a quick smoke test for MCP servers before connecting an external client (though its small model gets overwhelmed by large tool lists).
- [Supabase](./supabase.md) - A single platform providing Postgres for scalable chat memory plus the pgvector store for RAG embeddings, recommended over in-memory alternatives.
- [Ollama](./ollama.md) - Local LLM runtime; works with a locally-run bolt.diy but can't be reached by a self-hosted (remote) instance.
- [n8n](./n8n.md) - A no-code AI automation platform for building agents and workflows that integrate with 500+ applications.
- [Crawl4AI](./crawl4ai.md) - The open-source crawling library powering Cole's RAG MCP server, handling llms.txt, sitemaps, and recursive scraping.
- [Render](./render.md) - The cloud deployment platform (used on its free tier) that auto-builds and deploys staging on push and production on commit to main.
- [RunPod](./runpod.md) - GPU cloud recommended when you need a powerful high-VRAM machine to run large language models like Llama 3.2 90B.
- [Docker MCP Toolkit](./docker-mcp-toolkit.md) - Docker Desktop's MCP feature set: a curated catalog of hundreds of servers, a toolkit that runs each tool as an ephemeral container, and an open-source gateway for orchestrating them.

## Related

- [Agent Deployment](../../concepts/agent-deployment.md) - Getting agents to production, containerizing, networking, reverse-proxying, and choosing a provider-agnostic, cost-predictable host.
- [Local & Self-Hosted AI](../../concepts/local-ai.md) - Running open-weight models on your own hardware or cloud for privacy, cost control, and independence from API providers.
- [Model Context Protocol (MCP)](../../concepts/mcp.md) - An open protocol for packaging tools, data, and RAG capabilities as servers that any AI coding assistant or agent can connect to and call with a standard interface.
- [Provider Independence](../../concepts/provider-independence.md) - Architecting agents so the underlying model, framework, or client can be swapped without a rewrite, avoiding lock-in through low-level abstractions.
- [Retrieval-Augmented Generation (RAG)](../../concepts/rag.md) - Grounding an LLM's answers by retrieving relevant documents from an external knowledge base and injecting them into the prompt at query time.
- [Model Selection](../../concepts/model-selection.md) - Choosing the right LLM per task by trading off quality, speed, and cost, often routing easy requests to cheap models and hard ones to expensive models.

## Sources

- [Learn 90% of Building AI Agents in 30 Minutes](../../sources/learn-90-of-building-ai-agents-in-30-minutes.md) - "[0:26:35] Docker is my method for packaging up any application especially AI agents that I want to deploy to the cloud"
- [The OFFICIAL Archon Guide - 10x Your AI Coding Workflow](../../sources/the-official-archon-guide-10x-your-ai-coding-workflow.md) - "[0:08:30] Paste this in docker compose up build-d. This is going to build all of our archon containers at the same time. We got one for our user interface, one for the MCP server, and one for all of the API endpoints."
- [Deploying Billions of AI Agents is Easier than You Think](../../sources/deploying-billions-of-ai-agents-is-easier-than-you-think.md) - "[0:09:29] it's all running the same Docker container that is the beauty of Docker and what makes it so scalable and so easy to deploy"
- [The Ultimate Guide to Local AI and AI Agents (The Future is Here)](../../sources/the-ultimate-guide-to-local-ai-and-ai-agents-the-future-is-here.md) - "[0:44:00] all of these local AI services that I've curated for you, they all run as individual Docker containers that are all combined together in a stack"
- [Docker Just Made Using MCP Servers 100x Easier (One Click Installs!)](../../sources/docker-just-made-using-mcp-servers-100x-easier-one-click-installs.md) - "[0:02:02] the only thing you have to do is install Docker Desktop... I get to manage my MCP servers in the exact same place."
- [How I'd Learn AI Agents FAST if I Had to Start Over (Full Roadmap)](../../sources/how-id-learn-ai-agents-fast-if-i-had-to-start-over-full-roadmap.md) - "[0:12:36] the key for me for deploying my AI agents to production is to use a tool called Docker."
- [Code 100x Faster with AI, Here's How (No Hype, FULL Process)](../../sources/code-100x-faster-with-ai-heres-how-no-hype-full-process.md) - "[0:29:42] LLM are very good at working with Docker just because it's been around for so long. There's so many examples of it on the internet that's been used to train the LLMs."
- [Omnigent: The New Meta-Harness for EVERY Coding Agent](../../sources/omnigent-the-new-meta-harness-for-every-coding-agent-claude-code-codex-pi-more.md) - "[0:09:04] we can run unsandboxed or run in something like Docker or one of those more production platforms like E2B for example."
- [Build Your First Voice AI Agent in 20 Minutes with LiveKit](../../sources/build-your-first-voice-ai-agent-in-20-minutes-with-livekit-open-source.md) - "[0:10:34] I am running the MCP gateway from Docker so that I have this ready to be connected to from my LiveKit agent."
- [Archon Beta Launch Livestream - What You Missed!](../../sources/archon-beta-launch-livestream-what-you-missed.md) - "[0:06:30] you just run this docker compose command... and it'll spin up all the containers. And then you have everything running for archon."
- [Introducing Archon - an AI Agent that BUILDS AI Agents](../../sources/introducing-archon-an-ai-agent-that-builds-ai-agents.md) - "[0:07:58] you'll see the first option to install with Docker it is just three commands get up and running so stinking easy"
- [Run Supabase 100% LOCALLY for Your AI Agents](../../sources/run-supabase-100-locally-for-your-ai-agents.md) - "[0:05:19] our Docker compose do yaml so this file is responsible for defining all of the different Docker containers that we want to pull together"
- [Local vs. Cloud LLMs/RAG - Let's FINALLY End this Debate](../../sources/local-vs-cloud-llmsrag-lets-finally-end-this-debate.md) - "[0:01:41] I want to kick it off right away with Docker because this is a super important service you need Docker to guarantee that you have a sound infrastructure when you are self-hosting"
- [The True Power of AI Coding - Build Your OWN Workflows (Full Guide)](../../sources/the-true-power-of-ai-coding-build-your-own-workflows-full-guide.md) - "[0:03:39] I have my own AI agent that I have running in Docker on my computer and that is what Obsidian is connected to."
- [Knowledge Graphs in n8n are FINALLY Here!](../../sources/knowledge-graphs-in-n8n-are-finally-here.md)
- [The Ultimate Guide to Building Your Own MCP Servers (Free Template)](../../sources/the-ultimate-guide-to-building-your-own-mcp-servers-free-template.md)
- [I Built the Ultimate RAG MCP Server for AI Coding (Better than Context7)](../../sources/i-built-the-ultimate-rag-mcp-server-for-ai-coding-better-than-context7.md)
- [Claude MCP has Changed AI Forever](../../sources/claude-mcp-has-changed-ai-forever-heres-what-you-need-to-know.md)
- [Create Your Own Private Local AI Cloud Stack in Under 20 Minutes](../../sources/create-your-own-private-local-ai-cloud-stack-in-under-20-minutes.md)
- [n8n + Crawl4AI - Scrape ANY Website in Minutes with NO Code](../../sources/n8n-crawl4ai-scrape-any-website-in-minutes-with-no-code.md)
- [I'm Hosting a HUGE AI Hackathon Competition](../../sources/im-hosting-a-huge-ai-hackathon-competition.md)
- [Revealing my COMPLETE AI Agent Blueprint](../../sources/revealing-my-complete-ai-agent-blueprint.md)
- [Flowise + n8n - The BEST No Code + Local AI Agent Combo](../../sources/flowise-n8n-the-best-no-code-local-ai-agent-combo.md)
- [Claude Computer Use + Bolt.new - The ULTIMATE AI Coding Combo?!](../../sources/claude-computer-use-boltnew-the-ultimate-ai-coding-combo.md)
- [We're Taking this AI Coding Assistant to the MOON](../../sources/were-taking-this-ai-coding-assistant-to-the-moon-plus-installation-instructions.md)
- [This Bolt.new Fork is EXPLODING](../../sources/this-boltnew-fork-is-exploding-dont-miss-out-on-whats-happening.md)
- [Use Open WebUI with Your N8N AI Agents - Voice Chat Included!](../../sources/use-open-webui-with-your-n8n-ai-agents-voice-chat-included.md)
- [Deploy ANY AI App to the Cloud FAST](../../sources/deploy-any-ai-app-to-the-cloud-fast.md)
- [Run ALL Your AI Locally in Minutes (LLMs, RAG, and more)](../../sources/run-all-your-ai-locally-in-minutes-llms-rag-and-more.md)
