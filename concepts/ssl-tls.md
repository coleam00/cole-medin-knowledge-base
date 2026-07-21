---
type: concept
title: "HTTPS via Certbot / Let's Encrypt"
description: "Using Certbot to obtain and install a free Let's Encrypt SSL certificate so the deployed site is served securely over HTTPS."
tags: [security, ssl, https, deployment, certbot, lets-encrypt]
videos: [deploy-any-ai-app-to-the-cloud-fast]
created: 2026-07-21
updated: 2026-07-21
---

# HTTPS via Certbot / Let's Encrypt

Serving a deployed app over HTTPS means encrypting traffic with a TLS certificate, and the standard free path is Certbot fetching a certificate from Let's Encrypt. In Cole's deploy walkthrough the step is short and mechanical: once the domain is pointing at the server, "what we can do is install CTB that's what we're going to use for our SSL seert" (Certbot, for the SSL cert). [0:14:14] Certbot handles the ACME challenge with Let's Encrypt, proves you control the domain, and installs the issued certificate for you. Success is confirmed by Certbot's own output: "the message that we get as a success is going to look very similar here where it says deploying certificate and then successfully deployed the certificate." [0:14:44]

Why it matters: without a certificate, browsers flag the site as insecure and traffic travels in plaintext. HTTPS is effectively mandatory for anything user-facing, and Let's Encrypt made it free and automatable, so there is no reason to skip it. In practice this step is the last mile of a deploy, and it depends on two things being in place first. The domain must already resolve to the server via DNS so Certbot can validate ownership, and the certificate is installed against the same reverse proxy that fronts your services, which is where TLS is terminated for every backend at once. Certificates issued by Let's Encrypt are short-lived, so Certbot also sets up automatic renewal so HTTPS keeps working without manual reissue.

## Prerequisites

- [Custom Domain via DNS A Record](./custom-domain-dns.md)

## Related

- [Reverse Proxy](./reverse-proxy.md)
- [Firewall Configuration](./firewall-configuration.md)
- [Agent Deployment](./agent-deployment.md)
- [Full-Stack AI Application](./full-stack-ai-application.md)
- [Certbot](../entities/tools/certbot.md) - EFF tool that obtains and installs free Let's Encrypt SSL certificates and rewrites the web-server config so a deployed site is served over HTTPS.
- [Nginx](../entities/tools/nginx.md) - Open-source web server used as the reverse proxy that maps a public URL and domain to a local app's port, with configs symlinked from sites-available to sites-enabled and validated with nginx -t.

## Sources

- [Deploy ANY AI App to the Cloud FAST](../sources/deploy-any-ai-app-to-the-cloud-fast.md) - "[0:14:14] now moving on what we can do is install CTB that's what we're going to use for our SSL seert"
- [Deploy ANY AI App to the Cloud FAST](../sources/deploy-any-ai-app-to-the-cloud-fast.md) - "[0:14:44] the message that we get as a success is going to look very similar here where it says deploying certificate and then successfully deployed the certificate"
