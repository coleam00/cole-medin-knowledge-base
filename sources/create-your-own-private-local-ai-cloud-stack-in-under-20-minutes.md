---
type: source
title: "Create Your Own Private Local AI Cloud Stack in Under 20 Minutes"
description: "You can deploy the bundled Local AI Package to your own private cloud instance in under 20 minutes and keep it fully self-managed (still 'local'), gaining always-on access, more hardware, and team sharing without hogging your own machine."
youtube_id: hKrl5Gr7hM0
url: https://www.youtube.com/watch?v=hKrl5Gr7hM0
slug: create-your-own-private-local-ai-cloud-stack-in-under-20-minutes
published: 2025-03-12
duration: "0:16:51"
recency_rank: 110
raw: "../raw/create-your-own-private-local-ai-cloud-stack-in-under-20-minutes.md"
tags: [local-ai, local-ai-package, deployment, docker, self-hosting]
created: 2026-07-21
updated: 2026-07-21
---

Cole walks through taking the Local AI Package (a Docker-Compose bundle of n8n, Supabase, Ollama, Open WebUI, Flowise, Qdrant, SearXNG, Redis, and Caddy) and deploying it to a private cloud instance rather than running it on a personal computer. The motivation: you may want the stack running 24/7, accessible by an internal team, or on hardware you do not own, and hosting it on a cloud instance you personally manage still counts as a private, local setup. The guide is provider-agnostic and works on any Linux (Ubuntu) machine, though he demos on DigitalOcean because of its strong CPU-instance options.

The end-to-end process covers cloud-provider and hardware selection (CPU instances are cheaper and sufficient unless you run LLMs larger than 7-8B parameters, which require a dedicated GPU; many people instead host Ollama elsewhere or use an API like OpenRouter while keeping the rest of the stack local), spinning up an Ubuntu-with-Docker droplet, then the cloud-specific extra steps: opening firewall ports (UFW) for each exposed service and creating DNS A records that point subdomains (e.g. yt-nn.yourdomain.com) at the droplet's IP. Ollama and SearXNG are deliberately left un-exposed because they are not password protected.

The base install is: git clone the repo, copy .env.example to .env and fill in secrets (n8n key, Supabase Postgres password / JWT / anon / service-role keys, pool ID) plus the Caddy config where you uncomment and set each subdomain and a Let's Encrypt email. Running the Python start script brings up Supabase then the rest of the containers on a single shared Docker network so they communicate over localhost, with Caddy providing managed HTTPS/TLS. Finally he verifies each service resolves at its secure subdomain and shows docker ps and docker logs -f for managing the stack.

## Concepts covered

- [Local & Self-Hosted AI](../concepts/local-ai.md)
- [Agent Deployment](../concepts/agent-deployment.md)
- [Agent Security](../concepts/agent-security.md)

## Entities

- [Local AI Package](../entities/tools/local-ai-package.md)
- [n8n](../entities/tools/n8n.md)
- [Supabase](../entities/tools/supabase.md)
- [Ollama](../entities/tools/ollama.md)
- [Open Web UI](../entities/tools/open-web-ui.md)
- [Flowise](../entities/tools/flowise.md)
- [Qdrant](../entities/tools/qdrant.md)
- [SearXNG](../entities/tools/searxng.md)
- [Caddy](../entities/tools/caddy.md)
- [DigitalOcean](../entities/organizations/digital-ocean.md)
- [Docker](../entities/tools/docker.md)
- [Redis](../entities/tools/redis.md)
- [OpenRouter](../entities/tools/openrouter.md)
- [Cole Medin](../entities/people/cole-medin.md)

## Key moments

- **[0:00:00]** Intro, the Local AI Package is the easiest way to get LLMs, DBs, automation, web search, and UI running locally for free
- **[0:00:52]** Key framing: a cloud instance you manage yourself is still considered "local"
- **[0:01:42]** Tour of the bundled services in the Local AI Package repo
- **[0:02:31]** Caddy added for managed HTTPS/TLS so services get secure subdomain endpoints
- **[0:03:18]** Provider selection, demos DigitalOcean (unsponsored) for best CPU instances; barrage of GPU options
- **[0:04:20]** Platforms that don't work well: TensorDock (can't open ports), RunPod/Novita (container-in-container)
- **[0:05:04]** Creating the droplet, $42/mo CPU instance, 8GB RAM, Ubuntu + Docker image
- **[0:05:38]** GPU needed only for LLMs larger than 7-8B params; else use CPU + external Ollama or OpenRouter
- **[0:07:16]** Cloud-only extra steps: open firewall ports (UFW) per service
- **[0:08:16]** Set up DNS A records mapping subdomains to the droplet IP
- **[0:09:35]** Base install: git clone, copy .env.example to .env, edit secrets
- **[0:11:37]** Caddy config, uncomment subdomains, set Let's Encrypt email
- **[0:12:55]** Run the Python start script, pulls Supabase then rest of stack on a single Docker network
- **[0:14:55]** Manage the stack with docker ps and docker logs -f
- **[0:15:22]** Verify each service resolves securely at its subdomain from an external browser

## Transcript

[Raw transcript](../raw/create-your-own-private-local-ai-cloud-stack-in-under-20-minutes.md)
