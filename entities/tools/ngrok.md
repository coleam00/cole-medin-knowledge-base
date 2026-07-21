---
type: entity
subtype: tool
title: "ngrok"
description: "Tunneling tool that exposes a local dev server on a public HTTPS URL so third-party webhooks (here ChargeBee's) can reach a local endpoint during development."
resource: "https://ngrok.com"
tags: [deployment, infrastructure]
videos: [how-to-properly-use-claude-code-agent-teams-full-live-build]
created: 2026-07-21
updated: 2026-07-21
---

# ngrok

ngrok solves one narrow, recurring problem: a webhook provider on the public internet needs to POST to code that only exists on your laptop. It opens a tunnel from a public HTTPS address to a port on localhost, so an external service can call your dev server as if it were deployed. Cole states the purpose plainly while wiring up a payment integration: "this is my way to get an HTTPS URL so that I can expose this to the worldwide web so that we can uh handle the requests coming in from ChargeB." ([0:26:04](../../sources/how-to-properly-use-claude-code-agent-teams-full-live-build.md)).

In that live build he is adding a ChargeBee token-purchase flow to an existing [Next.js](./nextjs.md) plus [Supabase](./supabase.md) chat app, and the tunnel is standing infrastructure rather than a step in the plan: "I already have a Ingro set up here ready to go. So I have the chargeb web hook that's already set up to send requests to slashi/webhooks/chargeb" ([0:24:12](../../sources/how-to-properly-use-claude-code-agent-teams-full-live-build.md)). The HTTPS part is not incidental. Payment providers, and most serious webhook senders, refuse to deliver to plain HTTP, so a raw port-forward would not do.

What the tunnel buys is a real feedback loop. The [webhook handler](../../concepts/webhook-driven-agent.md) can be exercised with genuine provider payloads and signatures against local code you can edit and re-run in seconds, which is the only honest way to build one. That fits how Cole works during a [Claude Code](./claude-code.md) agent-teams build: the agents write the endpoint, and [end-to-end validation](../../concepts/end-to-end-validation.md) means driving the actual flow through the actual interface rather than trusting unit tests around a mocked request body.

ngrok is deliberately temporary. It is a development shim, not the deployment story. When the app ships, a permanent public address comes from a [reverse proxy](../../concepts/reverse-proxy.md) on a real domain with a real certificate, and the tunnel disappears. Treat the public URL as a live opening into your machine and give the endpoint behind it the same [protection](../../concepts/api-security.md) you would give a production one.

## Realizes

- [Webhook-Driven Agents](../../concepts/webhook-driven-agent.md) - Triggering agents and handlers from external events via webhooks so they run reactively as part of automated workflows.

## Contrasts with

- [Reverse Proxy](../../concepts/reverse-proxy.md) - The permanent version of the same idea: a public URL routed to an internal port, on your own domain and certificate rather than a throwaway tunnel.
- [Nginx](./nginx.md) - The proxy that replaces the tunnel once the app is actually deployed.

## Works with

- [Claude Code](./claude-code.md) - The agent team writing the webhook endpoint the tunnel points at.
- [Next.js](./nextjs.md) - The app hosting the `/api/webhooks/chargebee` route being exposed.
- [Supabase](./supabase.md) - The database the webhook handler writes token purchases into.

## Related

- [Webhook Tool Pattern](../../concepts/webhook-tool-pattern.md) - Exposing and wiring agents through webhook triggers and public URLs any frontend can call.
- [Securing Agent APIs](../../concepts/api-security.md) - Bearer-token auth and secret handling for endpoints that are publicly reachable.
- [End-to-End Validation](../../concepts/end-to-end-validation.md) - Proving the integration works through its real interface, which the tunnel makes possible locally.
- [Agent Teams](../../concepts/agent-teams.md) - The multi-agent build this integration was constructed inside of.
- [MCP Transports](../../concepts/mcp-transports.md) - The related local-versus-remote question for how clients reach a server.

## Sources

- [How to Properly Use Claude Code Agent Teams (FULL LIVE BUILD)](../../sources/how-to-properly-use-claude-code-agent-teams-full-live-build.md) - "[0:24:12] I already have a Ingro set up here ready to go. So I have the chargeb web hook that's already set up to send requests to slashi/webhooks/chargeb"
- [How to Properly Use Claude Code Agent Teams (FULL LIVE BUILD)](../../sources/how-to-properly-use-claude-code-agent-teams-full-live-build.md) - "[0:26:04] this is my way to get an HTTPS URL so that I can expose this to the worldwide web so that we can uh handle the requests coming in from ChargeB."
