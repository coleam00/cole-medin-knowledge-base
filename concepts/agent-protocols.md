---
type: concept
title: "Agent Protocols"
description: "Emerging standards (A2A, agent cards, discovery) that let agents interoperate and be called across clients."
tags: [protocols, a2a, interoperability, agents, acp, mcp]
videos: [this-completely-changes-the-way-we-build-production-ai-agents-vercel-eve, i-built-a-safer-openclaw-alternative-using-claude-code, the-way-we-use-ai-will-completely-change-in-2026-hot-takes, this-new-protocol-will-change-ai-coding-forever-acp, ag-ui-just-released-the-new-wave-of-ai-agent-apps, google-is-quietly-revolutionizing-ai-agents-this-is-huge, the-ultimate-guide-to-building-your-own-mcp-servers-free-template, claude-mcp-has-changed-ai-forever-heres-what-you-need-to-know, deploying-billions-of-ai-agents-is-easier-than-you-think, effortless-rag-in-n8n-use-all-your-files-pdfs-excel-and-more, complete-guide-to-langserve-make-your-ai-agent-actually-useful]
created: 2026-07-21
updated: 2026-07-21
---

# Agent Protocols

Agent protocols are the open standards that let agents, tools, editors, and other agents interoperate without bespoke glue for every pair. "It's been the year of agent protocols like Anthropic's MCP, making it so easy to connect tools to our agents, or Google's A2A, making it very seamless to connect agents to other agents." [0:00:00] Each protocol standardizes a different edge of the agent: [MCP](./mcp.md) connects agents to tools, A2A connects agents to agents, [ACP](./agent-client-protocol.md) connects agents to editors, and AG-UI connects agents to front ends.

Why standards, not one-off integrations? "I'm a very big fan of standards, like MCP and A2A and OKF... standards are what move the industry forward. Because when everyone has the same approach, we're able to learn from each other and build on top of each other." [0:05:25] The same MCP server "is any application that supports MCP like Windsurf Cursor, N8N, Claw Desktop, your own AI agents" [0:02:29], so one implementation reaches every compatible client instead of N private connectors.

**Agent-to-agent (A2A)** extends the pattern to a peer network. "Google recently introduced their agent to agent protocol which is a standard for agents to communicate effectively with each other. It's very similar to how MCP is the standard to connect agents to tools." [0:00:00] The keystone is a self-describing metadata file, the agent card: "It's so powerful to have this way for an agent to describe its capabilities, how to interact with it, any kind of authentication requirements to other agents so they know how to work with each other all through a single metadata file." [0:07:18] That discovery layer points toward a future where "we have AI agents that operate in a peer network. They can discover each other's capabilities in real time and interact very autonomously." [0:10:50]

Adoption, not novelty, is the gating factor. "In order for it to be useful, we have to have a lot of people adopt it at the same time. Otherwise, if we build an agent that is A2A compatible, then it has no other agents to talk to." [0:11:34] MCP itself proves the lag: "It was November of last year that MCP was first released by Anthropic. It wasn't widely adopted until maybe around March of this year. So like four or five months." [0:20:21] Newer protocols are worth exploring but still maturing: "Obviously this protocol is brand spanking new and so it's not super mature at this point... maybe not using it for literally everything yet." [0:19:48] The protocols are complementary rather than competing.

## Related

- [Model Context Protocol (MCP)](./mcp.md) - the tool-connection standard that anchored the whole family.
- [Agent Client Protocol (ACP)](./agent-client-protocol.md) - the agent-to-editor member of the family.
- [Build Your Own MCP Server](./build-your-own-mcp-server.md) - implementing the tool side of the protocol.
- [Provider Independence](./provider-independence.md) - the strategic reason to bet on standards.
- [Agent as an API Endpoint](./agent-as-api-endpoint.md) - exposing an agent so other systems can call it.
- [Agent Deployment](./agent-deployment.md)
- [Agent Security](./agent-security.md) - authentication and scoping across agent boundaries.
- [Agent Teams](./agent-teams.md) - multi-agent systems the peer network enables.
- [Agentic Coding](./agentic-coding.md)
- [Context Engineering](./context-engineering.md)
- [Generative UI](./generative-ui.md) - front-end protocols like AG-UI.
- [Knowledge Bases](./knowledge-bases.md)

## Tools

- [MCP](../entities/tools/mcp.md) - the agent-to-tool standard.
- [AG-UI](../entities/tools/ag-ui.md) - the agent-to-front-end protocol.
- [Anthropic](../entities/organizations/anthropic.md) - released MCP.
- [Google](../entities/organizations/google.md) - released the A2A protocol.
- [LangServe](../entities/tools/langserve.md) - exposes agents as standardized API endpoints.
- [n8n](../entities/tools/n8n.md) - consumes agents through webhooks and MCP.

## Sources

- [AG-UI Just Released: The NEW WAVE of AI Agent Apps](../sources/ag-ui-just-released-the-new-wave-of-ai-agent-apps.md) - "[0:00:00] even more than that, it's been the year of agent protocols like Anthropic's MCP, making it so easy to connect tools to our agents, or Google's A2A, making it very seamless to connect agents to other agents"
- [Google is Quietly Revolutionizing AI Agents (This is HUGE)](../sources/google-is-quietly-revolutionizing-ai-agents-this-is-huge.md) - "[0:07:18] It's so powerful to have this way for an agent to describe its capabilities, how to interact with it, any kind of authentication requirements to other agents so they know how to work with each other all through a single metadata file."
- [This Completely Changes the Way We Build Production AI Agents (Vercel Eve)](../sources/this-completely-changes-the-way-we-build-production-ai-agents-vercel-eve.md) - "[0:05:25] I'm a very big fan of standards, like MCP and A2A and OKF... standards are what move the industry forward."
- [The Way We Use AI Will Completely Change in 2026 (Hot Takes)](../sources/the-way-we-use-ai-will-completely-change-in-2026-hot-takes.md) - "[0:11:34] In order for it to be useful, we have to have a lot of people adopt it at the same time. Otherwise, if we build an agent that is A2A compatible, then it has no other agents to talk to."
- [AG-UI Just Released: The NEW WAVE of AI Agent Apps](../sources/ag-ui-just-released-the-new-wave-of-ai-agent-apps.md) - "[0:20:21] It was November of last year that MCP was first released by Anthropic. It wasn't widely adopted until maybe around March of this year. So like four or five months"
- [This New Protocol Will Change AI Coding Forever (ACP)](../sources/this-new-protocol-will-change-ai-coding-forever-acp.md) - "[0:00:49] since ACP is a standard, we're able to create our own custom agents that we can attach as coding agents into any editor, just like with MCP, we're able to build tools that we can connect into any agent."
- [The ULTIMATE Guide to Building Your Own MCP Servers (Free Template)](../sources/the-ultimate-guide-to-building-your-own-mcp-servers-free-template.md) - "[0:06:50] I'm showing you how we have one MCP server that we're able to connect to from all these different clients and we built everything ourselves."
- [Claude MCP has Changed AI Forever - Here's What You NEED to Know](../sources/claude-mcp-has-changed-ai-forever-heres-what-you-need-to-know.md) - "[0:23:13] agent support like this gets me fired up adding in the ability for complex agentic workflows with mcps and having sub agents that are directly supported as mCP servers hierarchical agent system"
- [Deploying Billions of AI Agents is Easier than You Think](../sources/deploying-billions-of-ai-agents-is-easier-than-you-think.md) - "[0:00:13] I think we're going to live in a world where there are going to be hundreds of millions of billions of different AI agents eventually probably more AI agents than there are people in the world"
- [COMPLETE Guide to LangServe - Make Your AI Agent Actually Useful](../sources/complete-guide-to-langserve-make-your-ai-agent-actually-useful.md) - "[0:00:48] there's literally only three lines of code that I have to change in my front end my streamlet UI to interact with my new Lang serve endpoint"
- [Effortless RAG in n8n - Use ALL Your Files (PDFs, Excel, and More)](../sources/effortless-rag-in-n8n-use-all-your-files-pdfs-excel-and-more.md) - "[0:02:44] the other trigger right here is a web hook and this is how we can use our NN agent as an API"
