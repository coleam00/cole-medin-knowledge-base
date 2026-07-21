---
type: concept
title: "Remote MCP Server"
description: "An MCP server hosted in the cloud rather than run locally, making tool access scalable, shareable, and deployable behind a production URL."
tags: [mcp, deployment, cloudflare]
videos: [build-and-ship-any-mcp-server-in-minutes-full-guide]
created: 2026-07-21
updated: 2026-07-21
---

# Remote MCP Server

A remote MCP server is an [MCP](./mcp.md) server that runs on cloud infrastructure and is reached over HTTP at a public address, instead of being spawned as a local subprocess on the developer's own machine. The payoff is a single deployable artifact anyone can point a client at: "We now have our production URL for our remote MCP server. It's so so cool. We can use this to then connect to it with cloud desktop" [0:24:56]. Remote hosting was one of the pieces missing when MCP launched, and it is the piece that moved MCP from a local toy to something shippable: "We have enterprisegrade remote MCP deployments with platforms like Cloudflare that actually make it really straightforward" [0:01:28].

The mental shift is that a remote MCP server is just an API endpoint wearing a standard coat for agents. Everything you already know about running backends applies: authentication, role-based access, input sanitization, graceful error handling, monitoring, and secret management. In Cole's Cloudflare template the OAuth provider handles the login handshake server-side, a KV store tracks authenticated users, `wrangler deploy` ships the worker, and `wrangler secret put` injects production credentials. Because the server now sits on the public internet, the sensitive tools (a write-query tool, for instance) need to be gated per user rather than trusted by default, which is exactly the [agent authorization](./agent-authorization.md) problem.

## Prerequisites

- [MCP Server & Client Architecture](./mcp-architecture.md) - what a server exposes and how a client consumes it.
- [MCP Transports](./mcp-transports.md) - streamable HTTP is the transport that makes remote hosting scalable, versus local stdio.

## Builds on

- [Model Context Protocol (MCP)](./mcp.md) - the standard being deployed.
- [Build Your Own MCP Server](./build-your-own-mcp-server.md) - the local tool-registration pattern you deploy remotely.

## Contrasts with

- [The Problems With MCP Servers](./mcp-problems.md) - remote hosting and OAuth close the security and distribution gaps that made early MCP a toy.

## Implemented by

- [Cloudflare](../entities/organizations/cloudflare.md) - Workers plus the OAuth provider Cole uses for enterprise-grade remote deployment.
- [FastMCP](../entities/tools/fastmcp.md) - the Python path to the same server shape.
- [Claude Desktop](../entities/tools/claude-desktop.md) - a client that connects to the production URL.
- [MCP (Model Context Protocol)](../entities/tools/mcp.md), [Sentry](../entities/tools/sentry.md) - the protocol implementation and the production monitoring layered on top.
- [TypeScript](../entities/tools/typescript.md) - The go-to language for building MCP servers, especially remote ones deployed to Cloudflare.

## Related

- [MCP Authentication with OAuth](./mcp-oauth.md) - the login flow a public server needs.
- [Securing Agent APIs](./api-security.md), [Agent Security](./agent-security.md) - a remote MCP inherits every backend threat model.
- [Agent Deployment](./agent-deployment.md), [Reverse Proxy](./reverse-proxy.md), [HTTPS via Certbot / Let's Encrypt](./ssl-tls.md), [Custom Domain via DNS A Record](./custom-domain-dns.md) - the self-hosted route to the same public URL.
- [Tool Design](./tool-design.md), [Tool Standardization (USB-C for AI)](./tool-standardization.md) - what you are actually shipping.
- [MCP with Custom Agents](./mcp-with-custom-agents.md), [Remote Agentic Coding](./remote-agentic-coding.md) - consumers of a hosted server.
- [Docs and Templates as Coding-Assistant Context](./docs-as-agent-context.md) - handing the template plus the MCP security checklist to a coding assistant so it builds the next server for you.

## Sources

- [Build and Ship Any MCP Server in MINUTES (Full Guide)](../sources/build-and-ship-any-mcp-server-in-minutes-full-guide.md) - "[0:01:28] We have enterprisegrade remote MCP deployments with platforms like Cloudflare that actually make it really straightforward."
- [Build and Ship Any MCP Server in MINUTES (Full Guide)](../sources/build-and-ship-any-mcp-server-in-minutes-full-guide.md) - "[0:24:56] We now have our production URL for our remote MCP server. It's so so cool. We can use this to then connect to it with cloud desktop."
