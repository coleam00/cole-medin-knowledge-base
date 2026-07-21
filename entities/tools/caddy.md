---
type: entity
subtype: tool
title: "Caddy"
description: "Reverse proxy providing managed HTTPS/TLS via Let's Encrypt so each service gets a secure subdomain endpoint."
resource: "https://caddyserver.com"
tags: [reverse-proxy, https, local-ai]
videos: [the-ultimate-guide-to-local-ai-and-ai-agents-the-future-is-here, create-your-own-private-local-ai-cloud-stack-in-under-20-minutes]
created: 2026-07-21
updated: 2026-07-21
---

# Caddy

Caddy is the web server Cole runs as a [reverse proxy](../../concepts/reverse-proxy.md) in front of his self-hosted AI stack, and its defining job is automatic HTTPS. In his words, adding it "makes it so that we can get HTTPS so we can have secure endpoints set up automatically and it manages that encryption for us" ([1:29:30](../../sources/the-ultimate-guide-to-local-ai-and-ai-agents-the-future-is-here.md)). Rather than hand-configuring TLS certificates for every service, Caddy provisions and renews them automatically through Let's Encrypt, so each container in the stack is reachable at its own secure subdomain.

Cole treats Caddy as the networking layer that turns a private box full of [Docker](./docker.md) containers into a set of production-grade, publicly-reachable endpoints. In his private local AI cloud build he explains: "I included caddy now which is managed https and TLS so this is how we can have secure endpoints for all of our services" ([0:02:31](../../sources/create-your-own-private-local-ai-cloud-stack-in-under-20-minutes.md)). This matters for [local and self-hosted AI](../../concepts/local-ai.md) because self-hosting only becomes usable once the services behind it (an [n8n](./n8n.md) instance, a [Supabase](./supabase.md) dashboard, an [Ollama](./ollama.md) endpoint) can be accessed over encrypted connections instead of raw internal ports. Caddy sits at the edge of the stack, routing inbound requests to the right container while presenting a single trusted TLS surface to the outside world.

Where [Docker](./docker.md) gives Cole reproducible packaging, Caddy gives him secure exposure. The two compose together: the same `docker compose` file that defines his services also runs Caddy, which reads its routing rules and issues certificates on startup. This keeps the whole self-hosted deployment declarative and repeatable, which is the point of running a personal AI cloud that behaves like a real one.

## Realizes

- [Reverse Proxy](../../concepts/reverse-proxy.md) - A server (Nginx or Caddy) that receives requests at a public URL and routes them behind the scenes to internal services by port or subdomain, keeping backend services private and centralizing HTTPS.

## Works with

- [Docker](./docker.md) - Containerization prerequisite; the same docker compose file that defines the services also runs Caddy at the edge.
- [n8n](./n8n.md) - A no-code AI automation platform for building agents and workflows that integrate with 500+ applications.
- [Supabase](./supabase.md) - A single platform providing Postgres for scalable chat memory plus the pgvector store for RAG embeddings, recommended over in-memory alternatives.
- [Ollama](./ollama.md) - Local LLM runtime; one of the self-hosted services Caddy exposes over an encrypted endpoint.

## Related

- [Local & Self-Hosted AI](../../concepts/local-ai.md) - Running open-weight models on your own hardware or cloud for privacy, cost control, and independence from API providers.
- [Provider Independence](../../concepts/provider-independence.md) - Architecting agents so the underlying model, framework, or client can be swapped without a rewrite, avoiding lock-in through low-level abstractions.
- [Model Quantization](../../concepts/model-quantization.md) - Compressing model weights to lower precision so large models fit and run on limited local hardware.
- [Model Selection](../../concepts/model-selection.md) - Choosing the right LLM per task by trading off quality, speed, and cost.
- [Fine-Tuning](../../concepts/fine-tuning.md) - Adapting a base model to a task or domain via additional training, weighed against just prompting a stronger general model.
- [Context Window Limits](../../concepts/context-window-limits.md) - Managing finite context by summarizing, compacting, and sizing what you load so the model stays sharp on long tasks.
- [Certbot](./certbot.md) - EFF tool that obtains and installs free Let's Encrypt SSL certificates and rewrites the web-server config so a deployed site is served over HTTPS.

## Sources

- [The Ultimate Guide to Local AI and AI Agents (The Future is Here)](../../sources/the-ultimate-guide-to-local-ai-and-ai-agents-the-future-is-here.md) - "[1:29:30] it also makes it so that we can get HTTPS so we can have secure endpoints set up automatically and it manages that encryption for us"
- [Create Your Own Private Local AI Cloud Stack in Under 20 Minutes](../../sources/create-your-own-private-local-ai-cloud-stack-in-under-20-minutes.md) - "[0:02:31] I included caddy now which is managed https and TLS so this is how we can have secure endpoints for all of our services"
