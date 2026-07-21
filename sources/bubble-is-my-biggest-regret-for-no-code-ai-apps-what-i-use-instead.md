---
type: source
title: "Bubble is My BIGGEST Regret for No Code AI Apps - What I Use Instead"
description: "No-code AI app builders with usage-based workload-unit pricing (like Bubble) can silently drain your wallet at scale, so prefer platforms with predictable infrastructure-based pricing (like Moment) that also let you build both the AI agent and the front end in one place."
youtube_id: rbVp40BIBBs
url: https://www.youtube.com/watch?v=rbVp40BIBBs
slug: bubble-is-my-biggest-regret-for-no-code-ai-apps-what-i-use-instead
published: 2024-09-20
duration: "0:12:02"
recency_rank: 163
raw: "../raw/bubble-is-my-biggest-regret-for-no-code-ai-apps-what-i-use-instead.md"
tags: [no-code, pricing, full-stack, ai-agents]
created: 2026-07-21
updated: 2026-07-21
---

# Bubble is My BIGGEST Regret for No Code AI Apps - What I Use Instead

Cole argues that most popular no-code app builders that are bolting on generative AI (Bubble being the prime example) trap builders with hidden, usage-based fees. Bubble meters your app in "workload units" (each database request or API call), and once you exceed the plan's included units you pay roughly 30 cents per 1,000 operations. Because every page load and interaction spends multiple units, real applications blow through the limit fast, making costs unpredictable and, at scale, ruinous.

He contrasts this with Moment, a no-code platform that lets you build full-stack AI applications: agents with RAG, tool calling, dynamic prompts, databases, API integrations, and workflows plus a website and app front end all in one place. Its key selling point is predictable, infrastructure-based pricing: you pay for fixed cores, memory, and storage rather than per-operation, so cost is fixed no matter how many times users hit your APIs or database. He cites Moment's own competitor test where a batch of operations Moment does for free cost about $155 (and 5,000 workload units) on Bubble.

The back half is a walkthrough of an agent Cole built in Moment that extracts action items from meeting notes and adds them to Google Calendar. He shows the agent config (model, temperature, dynamic prompt inputs, roles and constraints, structured output, tool calling via any API), the responsive website builder, and "action flow" workflows that stitch the front end to the agent, database, and Google Calendar API. The broader lesson he generalizes: for any service, prefer predictable infrastructure pricing over per-operation metering.

## Concepts covered

- [No-Code AI Agents](../concepts/no-code-agents.md)
- [Usage-Based Pricing Trap](../concepts/usage-based-pricing-trap.md)
- [Agent Deployment](../concepts/agent-deployment.md)
- [Full-Stack AI Application](../concepts/full-stack-ai-application.md)
- [Tool Calling](../concepts/tool-use.md)
- [Agent Prompting Techniques](../concepts/agent-prompting.md)
- [Structured Outputs](../concepts/structured-outputs.md)
- [Agentic Workflow Engineering](../concepts/agentic-workflow-engineering.md)

## Entities

- [Cole Medin](../entities/people/cole-medin.md)

## Key moments

- **[0:00:00]** Framing: few no-code platforms do both AI agents and websites well, but full-stack AI apps need both
- **[0:00:31]** The core problem with builders like Bubble: hidden fees that scale with your AI app
- **[0:00:45]** Introduces Moment as an affordable full-stack no-code AI platform (RAG, tool calling, dynamic prompts, front end)
- **[0:02:02]** Bubble pricing breakdown: workload units meter every database and API operation
- **[0:02:50]** About 30 cents per 1,000 operations; example of a page reload costing roughly 10 cents
- **[0:03:06]** Moment's predictable infrastructure pricing: pay for cores, memory, and storage, not per operation
- **[0:04:08]** Moment's competitor test: work free on Moment cost about $155 and 5,000 workload units on Bubble
- **[0:05:39]** Walkthrough begins: building a meeting-notes-to-action-items agent in Moment
- **[0:06:09]** Agent config: model, temperature, dynamic prompt inputs, roles and constraints, structured output, tool calling
- **[0:07:19]** Front end: responsive website builder with components and mobile preview
- **[0:08:13]** Action flow workflows wire front-end buttons to the agent, database, and Google Calendar API
- **[0:09:29]** Live demo: paste meeting notes, extract 3 action items, add them to Google Calendar

## Transcript

[Raw transcript](../raw/bubble-is-my-biggest-regret-for-no-code-ai-apps-what-i-use-instead.md)
