---
type: concept
title: "Agent Security"
description: "Sandboxing agents, scoping permissions, and keeping secrets out of the model to limit blast radius and prevent abuse."
tags: [security, permissions, secrets, agents, safety]
videos: [full-guide-build-your-own-ai-second-brain-with-claude-code, i-built-a-safer-openclaw-alternative-using-claude-code, i-was-wrong-about-ralph-wiggum, a-complete-guide-to-claude-code-here-are-all-the-best-strategies, why-is-everyone-missing-this-with-ai-agents-memory-tools-that-scale, build-and-ship-any-mcp-server-in-minutes-full-guide, code-100x-faster-with-ai-heres-how-no-hype-full-process, create-your-own-private-local-ai-cloud-stack-in-under-20-minutes, deploying-billions-of-ai-agents-is-easier-than-you-think, insane-new-strategy-for-building-ai-agent-apps, the-glow-up-every-ai-agent-needs, flowise-n8n-the-best-no-code-local-ai-agent-combo, were-taking-this-ai-coding-assistant-to-the-moon-plus-installation-instructions, build-a-full-stack-app-for-your-n8n-ai-agent-in-20-minutes, developers-this-is-how-you-stay-relevant-with-ai-ai-agents-masterclass-1]
created: 2026-07-21
updated: 2026-07-21
---

# Agent Security

Agent security is the discipline of limiting an agent's blast radius: sandboxing what it can run, scoping what it can touch, and keeping secrets out of the model entirely. The governing posture is zero-trust: "I'm starting with sort of like a zero-trust mindset. Like let's start with just read-only, and then add in capabilities and be very controlled about that." [0:16:18] An agent starts able to read Slack but not post, then earns write access deliberately rather than by default. [0:15:46]

The threat is real and current. An OpenClaw instance carried "a one-click remote code execution vulnerability that allows attackers to steal all of your data and keys... All they have to do is get you to click on a single malicious link." [0:02:18] Cole's warning generalizes: "it's giving so much power to our agents and that I think is just so dangerous. Most people are not ready for their agent to wield all the power that OpenClaw gives it." [0:04:27]

**Sandboxing and permission scoping** are the first line of defense. Running "in sandbox mode... we can let this go for a while and it's not just going to go haywire and delete everything from our computer" [0:06:44], and specific files can be hard-blocked in `settings.json`. [0:15:05] Permission allowlists demand care: "I never add the rm the remove command because I always want to approve before it deletes any files" [0:10:35], and never "give it bash star because this means that it can run any command without asking... That is way too dangerous." [0:10:51]

**Secrets never enter the model.** "Do not trust the LLM with your API keys and securing your database" [0:04:26]; use environment variables, and reserve the truly sensitive credential (a Supabase service role key) as "the only thing that you would really want to keep secret and probably never given to a prompt for an llm." [0:09:35] For agents exposed as endpoints, an API bearer token gates access "so that people can't just access my [agent]... and suck my llm credits." [0:02:50] Tool authentication scales through OAuth flows, dynamically requesting access "only asking for permission when the time comes... for the very first time" [0:02:45], with role-based access "especially protecting those more sensitive tools like executing any write query in our database." [0:15:10]

## Prerequisites

- [Global Rules](./global-rules.md)
- [Context Engineering](./context-engineering.md)

## Related

- [The Lethal Trifecta](./lethal-trifecta.md) - the specific attack pattern agent security defenses are meant to break.
- [Agent Deployment](./agent-deployment.md)
- [Agent as an API Endpoint](./agent-as-api-endpoint.md)
- [Securing Agent APIs](./api-security.md)
- [Multi-Tenant Agents](./multi-tenant-agents.md)
- [Vibe Coding](./vibe-coding.md)
- [Build Your Own MCP Server](./build-your-own-mcp-server.md)
- [Local & Self-Hosted AI](./local-ai.md)
- [Agentic Coding](./agentic-coding.md)
- [Permission Management](./permission-management.md) - Allowlisting the specific safe commands an agent may run unattended, and using an isolated firewalled container when you do skip permissions entirely.

## Tools

- [Arcade](../entities/tools/arcade.md) - solves tool authentication and per-user OAuth scoping.
- [Claude Code](../entities/tools/claude-code.md) - permission allowlists and `settings.json` file blocks.
- [OpenClaw](../entities/tools/openclaw.md) - the cautionary example of an over-permissioned agent.
- [Claw Hub](../entities/tools/claw-hub.md) - OpenClaw's public skills marketplace, where research found hundreds of malicious packages stealing API keys and SSH credentials, the canonical example of untrusted third-party agent capabilities.
- [MCP](../entities/tools/mcp.md) - secured with OAuth and role-based access.
- [Supabase](../entities/tools/supabase.md)
- [GitHub](../entities/tools/github.md)
- [Gmail](../entities/tools/gmail.md) - Google's email service, the canonical per-user integration in this video: hardcoded Gmail credentials illustrate the scaling problem, and a Gmail toolkit is what the agent authorizes per user.
- [Guardrails AI](../entities/tools/guardrails-ai.md) - Open-source Python framework Cole leans on for agent input/output guardrails, blocking things like PII entering a prompt or unsafe content leaving the LLM.

## Sources

- [Full Guide - Build Your Own AI Second Brain with Claude Code](../sources/full-guide-build-your-own-ai-second-brain-with-claude-code.md) - "[0:16:18] I'm starting with sort of like a zero-trust mindset. Like let's start with just read-only, and then add in capabilities and be very controlled about that"
- [I Built a Safer OpenClaw Alternative Using Claude Code](../sources/i-built-a-safer-openclaw-alternative-using-claude-code.md) - "[0:02:18] there was a one-click remote code execution vulnerability that allows attackers to steal all of your data and keys from your OpenClaw instance."
- [A Complete Guide to Claude Code - Here are ALL the Best Strategies](../sources/a-complete-guide-to-claude-code-here-are-all-the-best-strategies.md) - "[0:10:51] never just to give it bash star because this means that it can run any command without asking for your approval ... That is way too dangerous."
- [I Was Wrong About Ralph Wiggum](../sources/i-was-wrong-about-ralph-wiggum.md) - "[0:06:44] It's running in sandbox mode ... we can let this go for a while and it's not just going to go haywire and delete everything from our computer"
- [Code 100x Faster with AI, Here's How (No Hype, FULL Process)](../sources/code-100x-faster-with-ai-heres-how-no-hype-full-process.md) - "[0:04:26] the very last thing is to implement environment variables yourself. Do not trust the LLM with your API keys and securing your database"
- [INSANE New Strategy for Building AI Agent Apps](../sources/insane-new-strategy-for-building-ai-agent-apps.md) - "[0:09:35] the service roll key this is the only thing that you would really want to keep secret and probably never given to a prompt for an llm"
- [Why is Everyone Missing This with AI Agents?! (Memory + Tools that Scale)](../sources/why-is-everyone-missing-this-with-ai-agents-memory-tools-that-scale.md) - "[0:02:45] we also are only asking for permission when the time comes for our agent to use one of these services on behalf of our user for the very first time"
- [Build and Ship Any MCP Server in MINUTES (Full Guide)](../sources/build-and-ship-any-mcp-server-in-minutes-full-guide.md) - "[0:15:10] We want role-based access using GitHub OAuth in our case, especially protecting those more sensitive tools like executing any write query in our database."
- [The GLOW-UP Every AI Agent Needs](../sources/the-glow-up-every-ai-agent-needs.md) - "[0:14:03] this API Bearer token this is how we're going to protect our API endpoint that goes into our AI agent"
- [Build a FULL Stack App for your n8n AI Agent in 20 Minutes](../sources/build-a-full-stack-app-for-your-n8n-ai-agent-in-20-minutes.md) - "[0:02:50] I still want a little bit of protection so that people can't just access my n8n workflow and suck my llm credits"
- [Developers, THIS is How you Stay Relevant with AI - AI Agents Masterclass #1](../sources/developers-this-is-how-you-stay-relevant-with-ai-ai-agents-masterclass-1.md) - "[0:02:31] these are variables that are containing things like secrets or configuration that you don't want to have just pasted in your code"
- [Deploying Billions of AI Agents is Easier than You Think](../sources/deploying-billions-of-ai-agents-is-easier-than-you-think.md) - "[0:11:18] you can have environment variables here that you deploy for different instances"
