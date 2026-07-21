---
type: concept
title: "Containerization & Docker Networking"
description: "Running each service and your own agent as Docker containers in one stack so they communicate over a private network by service name, and exposing a tool as a Dockerized HTTP API when it can't be installed natively."
tags: [docker, networking, deployment, containers, api]
videos: [the-ultimate-guide-to-local-ai-and-ai-agents-the-future-is-here, n8n-crawl4ai-scrape-any-website-in-minutes-with-no-code]
created: 2026-07-21
updated: 2026-07-21
---

# Containerization & Docker Networking

Containerization packages an agent and every service it depends on into isolated Docker containers that run together as a stack. The subtlety that trips people up is networking: inside a container, `localhost` no longer means the machine, it means the container itself. As Cole explains, "when you are within a container, localhost means that you are referencing still within the container. Open web UI needs to reach out to the Ollama container, not itself." [1:22:00] This one confusion is the most common failure he sees: "this whole like localhost versus host.docker.internal versus using the service name, that's the thing I see people get tripped up on the most." [1:35:00]

The rule that makes a multi-container stack work is **address services by their container name**. When Ollama runs in a container, "you want to change this to Ollama, you're specifically calling out the service that is running the Ollama container." [1:22:30] Every service on the same Docker network becomes reachable by name, which is why an agent's config should reference `supabase` or `n8n` rather than `localhost`. This gives you a private internal network where containers talk to each other directly, without exposing anything to the host or the internet unless you choose to.

Containerization is also the escape hatch for tools you cannot install natively. When a scraper won't sit inside n8n, Docker becomes the bridge: "for n8n we have to deploy Crawl4AI in a completely different way and that is why I mentioned Docker... Docker is our ticket to deploy Crawl4AI in a way where we can actually interact with it as an API endpoint." [0:04:54] The tradeoff is resources, "the Crawl4AI Docker container is a little bit of a resource hog cu it is running an entire headless browser." [0:06:51] Deployed to a managed host, the same container gets a clean public interface for free: "the app platform here on digital ocean automatically gives us an SSL protected full https endpoint ready for us to hit within our n8n workflow." [0:11:48]

## Part of

- [Agent Deployment](./agent-deployment.md)

## Related

- [Agent as an API Endpoint](./agent-as-api-endpoint.md)
- [Local & Self-Hosted AI](./local-ai.md)
- [Reverse Proxy](./reverse-proxy.md)
- [Agent Graphs](./agent-graphs.md)
- [No-Code Automation](./no-code-automation.md)

## Tools

- [Docker](../entities/tools/docker.md) - the container runtime and networking layer at the center of this pattern.
- [Crawl4AI](../entities/tools/crawl4ai.md) - a scraper Dockerized into an HTTP API when it can't run natively.
- [n8n](../entities/tools/n8n.md) - the workflow container that reaches other services by name.
- [Open Web UI](../entities/tools/open-web-ui.md) - the front-end container that must address Ollama, not itself.
- [Supabase](../entities/tools/supabase.md) - a database run in-network alongside the agent.
- [DigitalOcean](../entities/organizations/digital-ocean.md) - an app platform that hands a Dockerized service a full HTTPS endpoint.
- [Nginx](../entities/tools/nginx.md) - Open-source web server used as the reverse proxy that maps a public URL and domain to a local app's port, with configs symlinked from sites-available to sites-enabled and validated with nginx -t.
- [Node.js](../entities/tools/nodejs.md) - JavaScript runtime used as an install prerequisite, whose npm scripts act as optional convenience wrappers around the underlying Docker build and run commands.

## Sources

- [The Ultimate Guide to Local AI and AI Agents (The Future is Here)](../sources/the-ultimate-guide-to-local-ai-and-ai-agents-the-future-is-here.md) - "[1:35:00] this whole like localhost versus host.docker.internal versus using the service name, that's the thing I see people get tripped up on the most"
- [n8n + Crawl4AI - Scrape ANY Website in Minutes with NO Code](../sources/n8n-crawl4ai-scrape-any-website-in-minutes-with-no-code.md) - "[0:04:54] Docker is our ticket to deploy Crawl4AI in a way where we can actually interact with it as an API endpoint"
