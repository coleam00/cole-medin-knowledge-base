---
type: concept
title: "Custom Domain via DNS A Record"
description: "Pointing a subdomain at your server's IP by adding an A record at your DNS provider so users reach the app by name instead of a raw IP address."
tags: [dns, networking, deployment, domain]
videos: [deploy-any-ai-app-to-the-cloud-fast]
created: 2026-07-21
updated: 2026-07-21
---

# Custom Domain via DNS A Record

Once an agent or app is deployed to a cloud server, it lives at a raw IP address on some port, which is neither memorable nor presentable. A custom domain fixes that by mapping a human-readable name to that IP. The goal, in Cole's words, is that "when you actually want to deploy it you want a URL like N.Y yourdomain.com that would then redirect to the instance of n8n that's running on Port 5678." [0:02:33]

The mechanism is a single **DNS A record**, an "address" record that ties a hostname to an IPv4 address. You create it at your DNS provider: "you want to add a new record so it'll be an a record the host will be n8n or whatever subdomain that you picked to host and then for your IP address you paste in the IP before of the digital ocean droplet." [0:13:26] The host field is the subdomain (for example `n8n`), and the value is the public IP of the server, here a DigitalOcean droplet. After DNS propagates, requests to that subdomain resolve to your server.

The A record is only the first half of a presentable deployment. It gets traffic to the right machine, but a [reverse proxy](./reverse-proxy.md) still has to route the incoming request to the correct container and port, and [TLS](./ssl-tls.md) has to secure the connection so the domain serves over HTTPS rather than plain HTTP. Together, DNS plus reverse proxy plus certificates turn a bare IP into a named, encrypted endpoint users can trust.

## Part of

- [Agent Deployment](./agent-deployment.md)

## Related

- [Reverse Proxy](./reverse-proxy.md)
- [HTTPS via Certbot / Let's Encrypt](./ssl-tls.md)
- [Containerization & Docker Networking](./containerization.md)

## Tools

- [DigitalOcean](../entities/organizations/digital-ocean.md) - the droplet whose IPv4 address the A record points to.
- [n8n](../entities/tools/n8n.md) - the example service reached by subdomain instead of IP and port.
- [Certbot](../entities/tools/certbot.md) - EFF tool that obtains and installs free Let's Encrypt SSL certificates and rewrites the web-server config so a deployed site is served over HTTPS.

## Sources

- [Deploy ANY AI App to the Cloud FAST](../sources/deploy-any-ai-app-to-the-cloud-fast.md) - "[0:13:26] you want to add a new record so it'll be an a record the host will be n8n or whatever subdomain that you picked to host and then for your IP address you paste in the IP before of the digital ocean droplet"
