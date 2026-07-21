---
type: concept
title: "Firewall Configuration"
description: "Enabling the server firewall (UFW) and opening the necessary ports - HTTP/HTTPS (80/443) or the app's port - so external machines can reach the deployed app before proxy and SSL setup can succeed."
tags: [security, networking, deployment, ufw, ports]
videos: [deploy-any-ai-app-to-the-cloud-fast, complete-guide-to-langserve-make-your-ai-agent-actually-useful]
created: 2026-07-21
updated: 2026-07-21
---

# Firewall Configuration

Firewall configuration is the deployment step of enabling a server's firewall (UFW on Ubuntu) and explicitly opening the ports external clients need to reach your app. It comes first, before containers run and before any proxy or certificate work. As Cole sequences it, "before we actually run anything with these containers we need to get a few things set up and that's what I'm going to walk you through here starting with the firewalls." Skip it and later steps silently fail because traffic never reaches the box.

Which ports you open depends on how the app is exposed. For a public web app fronted by a reverse proxy, you open the standard web ports 80 and 443, and doing so is a hard prerequisite for the SSL step that follows: "the next command that I'm going to run here is going to be to open up ports 80 and 443 without these open in a later step when we set up our SSL CT for https it will fail so we have to run these." For an app served directly on a custom port, you open that port instead, "before we can actually run our LangServe endpoint we need to open up the firewall so that that Port 8000 is actually available for external machines like our laptops to connect into the droplet."

The mental model is that the firewall is a default-deny gate: nothing external reaches the server until you punch a specific hole for it. That makes firewall configuration both a security control (only the ports you name are reachable) and a connectivity precondition (the certificate authority's HTTP challenge, the reverse proxy's inbound traffic, and direct client connections all depend on the right ports being open first). Getting the ordering wrong is a common cause of a "why can't I reach my app" or a failed HTTPS provisioning step.

## Part of

- [Agent Deployment](./agent-deployment.md) - firewall setup is one of the first steps in standing an agent up on a server.

## Prerequisites for

- [SSL/TLS](./ssl-tls.md) - ports 80 and 443 must be open or certificate provisioning for HTTPS fails.
- [Certbot](../entities/tools/certbot.md) - EFF tool that obtains and installs free Let's Encrypt SSL certificates and rewrites the web-server config so a deployed site is served over HTTPS.

## Related

- [Reverse Proxy](./reverse-proxy.md) - the proxy that receives traffic on the ports you open.
- [Containerization & Docker Networking](./containerization.md) - the containers that must be reachable through the firewall.
- [Custom Domain via DNS A Record](./custom-domain-dns.md) - points a domain at the server whose ports you have opened.
- [Securing Agent APIs](./api-security.md) - the broader security posture the firewall contributes to.
- [Permission Management](./permission-management.md) - Allowlisting the specific safe commands an agent may run unattended, and using an isolated firewalled container when you do skip permissions entirely.

## Implemented by

- [LangServe](../entities/tools/langserve.md) - the endpoint that needs port 8000 opened to be reachable.

## Sources

- [Deploy ANY AI App to the Cloud FAST](../sources/deploy-any-ai-app-to-the-cloud-fast.md) - "[0:08:41] the next command that I'm going to run here is going to be to open up ports 80 and 443 without these open in a later step when we set up our SSL CT for https it will fail so we have to run these"
- [Deploy ANY AI App to the Cloud FAST](../sources/deploy-any-ai-app-to-the-cloud-fast.md) - "[0:08:10] before we actually run anything with these containers we need to get a few things set up and that's what I'm going to walk you through here starting with the firewalls"
- [COMPLETE Guide to LangServe - Make Your AI Agent Actually Useful](../sources/complete-guide-to-langserve-make-your-ai-agent-actually-useful.md) - "[0:12:34] before we can actually run our LangServe endpoint we need to open up the firewall so that that Port 8000 is actually available for external machines like our laptops to connect into the droplet"
