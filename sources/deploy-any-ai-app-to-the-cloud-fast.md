---
type: source
title: "Deploy ANY AI App to the Cloud FAST"
description: "Any application that runs on localhost with a port can be taken to production by putting it on a cloud VPS behind an Nginx reverse proxy with a custom domain and SSL, shown step by step using the n8n self-hosted local AI starter kit."
youtube_id: 259KgP3GbdE
url: https://www.youtube.com/watch?v=259KgP3GbdE
slug: deploy-any-ai-app-to-the-cloud-fast
published: 2024-10-06
duration: "0:21:20"
recency_rank: 156
raw: "../raw/deploy-any-ai-app-to-the-cloud-fast.md"
tags: [deployment, devops, reverse-proxy, self-hosting]
created: 2026-07-21
updated: 2026-07-21
---

# Deploy ANY AI App to the Cloud FAST

Cole walks through deploying an AI application to the cloud end-to-end, using the n8n self-hosted local AI starter kit (Ollama + Qdrant + Postgres + n8n) as a concrete example while stressing that the same steps deploy anything that runs on localhost with a port: a Streamlit app, a Next.js app, Ollama, or any Dockerized service. He spins up a basic Docker-on-Ubuntu droplet on DigitalOcean (recommending RunPod instead only when you need a beefy GPU machine for large models), clones the starter kit, edits its .env (Postgres creds, n8n encryption secrets) and docker-compose.yml (adding a nomic-embed-text pull for RAG embeddings).

The core deployment pattern is a reverse proxy: enable the UFW firewall and open ports 80 and 443, install Nginx, and write a site config that listens on port 80 for the chosen domain (nn.dynamous.ai) and proxies requests to localhost:5678 where n8n runs. He symlinks the config from sites-available to sites-enabled, tests with nginx -t, and reloads. He then adds a DNS A record at the domain registrar (Namecheap) pointing the subdomain at the droplet's IPv4, and installs Certbot to obtain a Let's Encrypt SSL certificate so the site is served over HTTPS. Only after this infrastructure is in place does he run the stack with docker compose up -d (detached).

A bonus section covers Docker Compose service networking: because every service shares one compose file, containers reference each other by service name rather than localhost. Inside n8n he wires Ollama at http://ollama:11434, Postgres at host "postgres", and Qdrant at http://qdrant:6333 (the API key can be anything since it runs locally), then verifies a chat with llama 3.1 8B works. The takeaway is that the reverse-proxy-plus-domain-plus-SSL recipe is cloud-provider-agnostic and applies to any localhost app.

## Concepts covered

- [Agent Deployment](../concepts/agent-deployment.md)
- [Reverse Proxy](../concepts/reverse-proxy.md)
- [Custom Domain via DNS A Record](../concepts/custom-domain-dns.md)
- [HTTPS via Certbot / Let's Encrypt](../concepts/ssl-tls.md)
- [Firewall Configuration](../concepts/firewall-configuration.md)
- [Retrieval-Augmented Generation (RAG)](../concepts/rag.md)
- [Model Selection](../concepts/model-selection.md)

## Entities

- [Cole Medin](../entities/people/cole-medin.md)
- [n8n](../entities/tools/n8n.md)
- [Ollama](../entities/tools/ollama.md)
- [Qdrant](../entities/tools/qdrant.md)
- [Postgres](../entities/tools/postgres-pgvector.md)
- [DigitalOcean](../entities/organizations/digital-ocean.md)
- [RunPod](../entities/tools/runpod.md)
- [Docker](../entities/tools/docker.md)
- [nomic-embed-text](../entities/tools/nomic-embed-text.md)

## Key moments

- **[0:00:00]** Intro: most-requested follow-up is deploying AI apps to the cloud; will deploy the n8n local AI starter kit
- **[0:01:19]** Framing: these steps deploy anything that runs on localhost with a port (Streamlit, Next.js, Ollama, Docker)
- **[0:01:49]** Overview of the local AI starter kit: Ollama (LLMs), Qdrant (vectors), Postgres (SQL/chat memory), n8n (workflows)
- **[0:02:42]** The goal: a URL like nn.yourdomain.com that redirects to n8n on port 5678
- **[0:02:57]** Chose DigitalOcean; recommends RunPod instead for powerful GPU machines to run large models
- **[0:04:03]** Create a basic Docker-on-Ubuntu droplet; steps are cloud-provider agnostic for any Ubuntu machine
- **[0:06:03]** Clone the starter kit repo, edit .env (Postgres creds plus n8n encryption secrets)
- **[0:07:23]** Edit docker-compose to also pull nomic-embed-text so RAG embeddings are available
- **[0:08:10]** Enable UFW firewall and open ports 80 and 443 (needed for SSL later)
- **[0:09:12]** Install Nginx as a reverse proxy that routes a URL to localhost:5678
- **[0:11:07]** Nginx config listens on port 80 for the domain, proxies to localhost:5678; swap the port for any app
- **[0:11:57]** Symlink sites-available to sites-enabled, test with nginx -t, reload
- **[0:12:43]** Add a DNS A record at the registrar (Namecheap) pointing the subdomain to the droplet IP
- **[0:13:59]** Install Certbot and obtain a Let's Encrypt SSL certificate for HTTPS
- **[0:15:14]** Run the stack with docker compose up -d (detached); containers pull images and start
- **[0:17:53]** Bonus: for non-n8n apps you are already done; n8n credential wiring is starter-kit specific
- **[0:18:08]** Docker Compose service networking: reference containers by service name (ollama:11434, postgres, qdrant:6333)
- **[0:19:43]** Verify with a chat to llama 3.1 8B; connection to Postgres and Ollama works

## Transcript

[Raw transcript](../raw/deploy-any-ai-app-to-the-cloud-fast.md)
