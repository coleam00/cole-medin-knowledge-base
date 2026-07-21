---
type: concept
title: "Reverse Proxy"
description: "A server (Nginx or Caddy) that receives requests at a public URL and routes them behind the scenes to internal services by port or subdomain, keeping backend services private and centralizing HTTPS."
tags: [deployment, networking, nginx, caddy, reverse-proxy, security]
videos: [the-ultimate-guide-to-local-ai-and-ai-agents-the-future-is-here, deploy-any-ai-app-to-the-cloud-fast]
created: 2026-07-21
updated: 2026-07-21
---

# Reverse Proxy

A reverse proxy is a single front-door server that accepts requests at a public URL and forwards them, behind the scenes, to whichever internal service should handle them, routing by port or by subdomain. As Cole describes Nginx in a deploy walkthrough: "Nginx is a reverse proxy and that is what's going to make it possible for... it to set it up so that there is a URL that a user visits and then behind the scenes it routes that request to n8n that is running on the Local Host here on Port 5678." [0:09:12] The user only ever sees the clean URL; the port-bound process stays on localhost.

The routing is trivially reusable across whatever you happen to be running: "you can see how if you have a nextjs app on Port 3000 or a Streamlit app on Port 5601 whatever it is you would just set that here and that's how you can reverse proxy to get your url to point to this." [0:11:25] One proxy config maps many public paths or hostnames onto many private ports.

Beyond routing, the pattern is a security boundary. In the local AI package, Caddy is the tool that "is going to allow us to set up subdomains for all of our services... this is called a reverse proxy" [1:29:00], and it becomes the single controlled ingress: "any of the services that you access from outside of the droplet, it has to go through caddy. So we use the reverse proxy as the only entry point." [1:40:00] Because everything funnels through one entry point, you decide precisely what is exposed and what stays internal. Cole's rule of thumb is to leave sensitive services unmapped entirely: "The two that I would generally recommend not uncommenting ever is Ollama and CRXNG. We don't really want to expose them through a subdomain." [1:37:00] A service with no proxy route simply has no public surface. Centralizing ingress this way also gives you one place to terminate TLS, which is why the reverse proxy is where HTTPS certificates live.

## Builds on

- [Agent Deployment](./agent-deployment.md)
- [Containerization & Docker Networking](./containerization.md)

## Related

- [Custom Domain via DNS A Record](./custom-domain-dns.md)
- [HTTPS via Certbot / Let's Encrypt](./ssl-tls.md)
- [Firewall Configuration](./firewall-configuration.md)
- [Full-Stack AI Application](./full-stack-ai-application.md)

## Tools

- [Caddy](../entities/tools/caddy.md)
- [Local AI Package](../entities/tools/local-ai-package.md)
- [Docker](../entities/tools/docker.md)

## Sources

- [Deploy ANY AI App to the Cloud FAST](../sources/deploy-any-ai-app-to-the-cloud-fast.md) - "[0:09:12] Nginx is a reverse proxy and that is what's going to make it possible for set it to set it up so that there is a URL that a user visits and then behind the scenes it routes that request to n8n that is running on the Local Host here on Port 5678"
- [Deploy ANY AI App to the Cloud FAST](../sources/deploy-any-ai-app-to-the-cloud-fast.md) - "[0:11:25] you can see how if you have a nextjs app on Port 3000 or a Streamlit app on Port 5601 whatever it is you would just set that here and that's how you can reverse proxy to get your url to point to this"
- [The Ultimate Guide to Local AI and AI Agents (The Future is Here)](../sources/the-ultimate-guide-to-local-ai-and-ai-agents-the-future-is-here.md) - "[1:40:00] any of the services that you access from outside of the droplet, it has to go through caddy. So we use the reverse proxy as the only entry point"
- [The Ultimate Guide to Local AI and AI Agents (The Future is Here)](../sources/the-ultimate-guide-to-local-ai-and-ai-agents-the-future-is-here.md) - "[1:37:00] The two that I would generally recommend not uncommenting ever is Ollama and CRXNG. We don't really want to expose them through a subdomain"
