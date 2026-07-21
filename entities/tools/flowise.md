---
type: entity
subtype: tool
title: "Flowise"
description: "Low-code LLM app / agent builder included and exposed in the stack."
resource: "https://flowiseai.com"
tags: [no-code, ai-agents, langchain]
videos: [create-your-own-private-local-ai-cloud-stack-in-under-20-minutes, run-supabase-100-locally-for-your-ai-agents, im-hosting-a-huge-ai-hackathon-competition, revealing-my-complete-ai-agent-blueprint, i-created-the-best-ai-agent-platform-in-just-2-months, flowise-n8n-the-best-no-code-local-ai-agent-combo, turn-any-ai-agent-into-a-live-person-voice-chat-setup-in-minutes]
created: 2026-07-21
updated: 2026-07-21
---

# Flowise

Flowise is a low-code, open-source LLM app and agent builder that Cole includes alongside n8n in his local AI stack. He defines it plainly: "flow wise is a low no code AI automation tool it is completely free open source and built on top of Lang chain." It is Y Combinator backed, widely adopted, and "super easy to install," which is why he reaches for it as a fast agent-building surface.

In Cole's workflow, Flowise and [n8n](./n8n.md) are complementary rather than competing: n8n remains his favorite for workflow automations and deep integration with hundreds of applications, while Flowise serves as a dedicated low-code [agent builder](../../concepts/rapid-prototyping.md). He bundles it into his private [local AI](../../concepts/local-ai.md) cloud stack next to Supabase and Open WebUI, opening ports for each service so the whole stack runs self-hosted. Because it sits on top of LangChain, it is a natural place to stand up a [RAG](../../concepts/rag.md) pipeline quickly and to prototype before a code rewrite.

He consistently names Flowise in the same breath as [Voiceflow](./voiceflow.md) and n8n as one of the no/low-code platforms suitable for building "a prototype... using a no or low code tool," and it was an accepted build platform for his AI agent hackathon. It sits in the same family as other drag-and-drop [visual workflow builders](../../concepts/visual-workflow-builder.md) like Langflow and VectorShift. Flowise touches the same lifecycle concerns as its siblings, [agent development](../../concepts/agent-development-lifecycle.md), [deployment](../../concepts/agent-deployment.md), and [agent security](../../concepts/agent-security.md), while trading raw control for speed of assembly.

## Related

- [Agent Deployment](../../concepts/agent-deployment.md)
- [Local & Self-Hosted AI](../../concepts/local-ai.md)
- [Retrieval-Augmented Generation (RAG)](../../concepts/rag.md)
- [Agent Security](../../concepts/agent-security.md)
- [Agent Development Lifecycle](../../concepts/agent-development-lifecycle.md)
- [Rapid Prototyping](../../concepts/rapid-prototyping.md)
- [n8n](./n8n.md)
- [Voiceflow](./voiceflow.md)
- [LangChain](./langchain.md)

## Sources

- [Create Your Own Private Local AI Cloud Stack in Under 20 Minutes](../../sources/create-your-own-private-local-ai-cloud-stack-in-under-20-minutes.md)
- [Run Supabase 100% LOCALLY for Your AI Agents](../../sources/run-supabase-100-locally-for-your-ai-agents.md) - "[0:02:45] then I added in flow wise for another low code AI agent Builder"
- [I'm Hosting a HUGE AI Hackathon Competition](../../sources/im-hosting-a-huge-ai-hackathon-competition.md)
- [Revealing my COMPLETE AI Agent Blueprint](../../sources/revealing-my-complete-ai-agent-blueprint.md) - "[0:03:43] building a prototype for it using a no or low code tool like n8n flow wise or voice flow"
- [I Created the BEST AI Agent Platform in Just 2 MONTHS!](../../sources/i-created-the-best-ai-agent-platform-in-just-2-months.md)
- [Flowise + n8n - The BEST No Code + Local AI Agent Combo](../../sources/flowise-n8n-the-best-no-code-local-ai-agent-combo.md) - "[0:01:20] flow wise is a low no code AI automation tool it is completely free open source and built on top of Lang chain"
- [Turn ANY AI Agent into a Live Person - Voice Chat Setup in Minutes](../../sources/turn-any-ai-agent-into-a-live-person-voice-chat-setup-in-minutes.md)
