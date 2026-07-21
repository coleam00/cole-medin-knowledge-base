---
type: entity
subtype: tool
title: "Certbot"
description: "EFF tool that obtains and installs free Let's Encrypt SSL certificates and rewrites the web-server config so a deployed site is served over HTTPS."
resource: "https://certbot.eff.org"
tags: [deployment, infrastructure]
videos: [deploy-any-ai-app-to-the-cloud-fast]
created: 2026-07-21
updated: 2026-07-21
---

# Certbot

Certbot is the EFF's command-line client for Let's Encrypt: it proves you control a domain, fetches a free TLS certificate for it, installs the certificate into your web server's config, and renews it automatically before it expires. In Cole's cloud deployment walkthrough it is one short step near the end: "what we can do is install CTB that's what we're going to use for our SSL seert" ([0:14:14](../../sources/deploy-any-ai-app-to-the-cloud-fast.md)) - and that brevity is the point. The thing that used to be the scariest part of shipping a site is now two commands.

Its place in the sequence matters more than its flags. Certbot is the **last** infrastructure step, and it only works because of what came before it. The [firewall](../../concepts/firewall-configuration.md) has to be open on ports 80 and 443, since Let's Encrypt validates ownership by reaching your server over HTTP. The [DNS A record](../../concepts/custom-domain-dns.md) has to already point the subdomain at the droplet's IP, because the certificate is issued for a name, not an address. And [Nginx](./nginx.md) has to be installed and serving that name, because Certbot does not just hand you a `.pem` file - it edits the existing site config in place, adds the 443 listener with the certificate paths, and wires up an HTTP-to-HTTPS redirect. Get the order wrong and the challenge fails for reasons that look nothing like a certificate problem.

Everything downstream of that is unchanged: the app itself still runs on localhost behind the [reverse proxy](../../concepts/reverse-proxy.md), oblivious to TLS, and the [Docker](./docker.md) stack comes up afterward with `docker compose up -d`. That separation is what makes the recipe portable. The same firewall-proxy-DNS-Certbot sequence takes any localhost app to production, whether it is [n8n](./n8n.md), a Streamlit dashboard, or a custom agent API, on any Ubuntu box from any provider.

## Prerequisites

- [Custom Domain via DNS A Record](../../concepts/custom-domain-dns.md) - The subdomain must already resolve to the server's IP before a certificate can be issued for it.
- [Firewall Configuration](../../concepts/firewall-configuration.md) - Ports 80 and 443 must be open so the Let's Encrypt validation request can reach the box.
- [Reverse Proxy](../../concepts/reverse-proxy.md) - A web server already serving the domain, since Certbot modifies its config rather than standing alone.

## Realizes

- [HTTPS via Certbot / Let's Encrypt](../../concepts/ssl-tls.md) - Using Certbot to obtain and install a free Let's Encrypt SSL certificate so the deployed site is served securely over HTTPS.

## Contrasts with

- [Caddy](./caddy.md) - A web server with managed HTTPS built in, provisioning and renewing the same Let's Encrypt certificates with no separate tool or step.

## Works with

- [Nginx](./nginx.md) - The reverse proxy whose site config Certbot rewrites to add the 443 listener and redirect.
- [Docker](./docker.md) - The containerized app stack that runs behind the proxy once TLS is in place.
- [n8n](./n8n.md) - The self-hosted service exposed at a secure subdomain in Cole's worked example.

## Related

- [Agent Deployment](../../concepts/agent-deployment.md) - Getting agents to production: containerize, network, reverse-proxy, secure, and pick a cost-predictable host.
- [Containerization & Docker Networking](../../concepts/containerization.md) - Running each service as a container in one stack that talks over a private network by service name.

## Sources

- [Deploy ANY AI App to the Cloud FAST](../../sources/deploy-any-ai-app-to-the-cloud-fast.md) - "[0:14:14] what we can do is install CTB that's what we're going to use for our SSL seert"
