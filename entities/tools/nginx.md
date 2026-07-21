---
type: entity
subtype: tool
title: "Nginx"
description: "Open-source web server used as the reverse proxy that maps a public URL and domain to a local app's port, with configs symlinked from sites-available to sites-enabled and validated with nginx -t."
resource: "https://nginx.org"
tags: [deployment, infrastructure]
videos: [deploy-any-ai-app-to-the-cloud-fast]
created: 2026-07-21
updated: 2026-07-21
---

# Nginx

Nginx is the open-source web server Cole installs on a fresh Ubuntu box to turn "an app running on some port on localhost" into "a URL people can type." It is the single load-bearing piece of his cloud-deployment recipe, and he flags it as the one step that demands attention: "let me do pseudo app install engine X ... this is where it gets a little technical with engine X we have to set up all of the reverse proxy configuration" ([0:09:24](../../sources/deploy-any-ai-app-to-the-cloud-fast.md)).

The configuration itself is short. You write a site file that listens on port 80 for your domain (his example is `nn.dynamous.ai`) and proxies every request to `localhost:5678`, where [n8n](./n8n.md) happens to be running. Swap that port and the exact same file deploys a Streamlit dashboard, a [Next.js](./nextjs.md) app, an [Ollama](./ollama.md) endpoint, or any custom agent API. The mechanics that trip people up are the conventions, not the syntax: the file lives in `sites-available` and is activated by symlinking it into `sites-enabled`, then `nginx -t` validates the config before a reload applies it. Testing before reloading matters, because a syntax error takes the whole server down rather than just the one site.

Order of operations is what makes the recipe work. The [firewall](../../concepts/firewall-configuration.md) opens 80 and 443 first, Nginx goes up second, the [DNS A record](../../concepts/custom-domain-dns.md) points the subdomain at the droplet's IP third, and [Certbot](./certbot.md) comes last, rewriting this same site config in place to add the 443 listener and an HTTP-to-HTTPS redirect. Only then does the app itself come up with `docker compose up -d`. The app never learns about TLS or domains at all, which is the real value of the proxy: the backend stays private on localhost while the edge owns naming, encryption, and routing. Because none of it is provider-specific, the sequence carries over to any Ubuntu machine from any host.

## Prerequisites

- [Firewall Configuration](../../concepts/firewall-configuration.md) - Ports 80 and 443 must be open before anything the proxy serves is reachable from outside.
- [Custom Domain via DNS A Record](../../concepts/custom-domain-dns.md) - The subdomain in the site config has to actually resolve to the server's IP.

## Realizes

- [Reverse Proxy](../../concepts/reverse-proxy.md) - A server that receives requests at a public URL and routes them behind the scenes to internal services by port or subdomain, keeping backends private and centralizing HTTPS.

## Contrasts with

- [Caddy](./caddy.md) - The same job with managed HTTPS built in, so there is no separate certificate tool or manual 443 listener.

## Works with

- [Certbot](./certbot.md) - Edits this server's site config to install the Let's Encrypt certificate and add the HTTPS redirect.
- [Docker](./docker.md) - The containerized app stack that keeps running on localhost behind the proxy.
- [n8n](./n8n.md) - The self-hosted service proxied at a real subdomain in the worked example.
- [n8n Self-Hosted AI Starter Kit](./n8n-self-hosted-ai-starter-kit.md) - The localhost stack being taken to the cloud in this walkthrough.

## Related

- [HTTPS via Certbot / Let's Encrypt](../../concepts/ssl-tls.md) - The TLS step that lands directly on top of the Nginx site config.
- [Agent Deployment](../../concepts/agent-deployment.md) - Getting agents to production: containerize, network, reverse-proxy, secure, and pick a cost-predictable host.
- [Containerization & Docker Networking](../../concepts/containerization.md) - Why containers behind the proxy address each other by service name instead of localhost.
- [Securing Agent APIs](../../concepts/api-security.md) - What still has to be protected once an agent endpoint is publicly reachable.

## Sources

- [Deploy ANY AI App to the Cloud FAST](../../sources/deploy-any-ai-app-to-the-cloud-fast.md) - "[0:09:24] let me do pseudo app install engine X ... this is where it gets a little technical with engine X we have to set up all of the reverse proxy configuration"
