---
type: entity
subtype: tool
title: "Retool"
description: "Internal-app platform that imports React code and connects to a database to deploy dashboards with a governed, permissioned, audit-trailed path to production."
resource: "https://retool.com"
tags: [no-code, app-builder]
videos: [the-creators-of-claude-code-and-openclaw-dont-prompt-their-agents-anymore]
created: 2026-07-21
updated: 2026-07-21
---

# Retool

Retool is an internal-app platform Cole uses to take a locally built control dashboard and put it in production without hand-rolling hosting, auth, and permissions. It is the deployment half of his [loop engineering](../../concepts/loop-engineering.md) setup: "Retool is a tool specifically I've been leaning on a lot for these kinds of deployments... it's so easy to create an app here and then we can import React code" [0:21:23]. The trigger is practical - once agents run autonomously in the background, you want a control surface you can hit from anywhere and share with teammates, not a local dev server.

The import path is the notable part. Cole had [Claude Code](./claude-code.md) build the whole orchestrator dashboard in [React](./react.md) with deployment in mind, then dropped the front-end zip into Retool, whose own agent wires it up: it connects to the API running [Pi](./pi-coding-agent.md) behind the scenes, and to the [Neon](./neon.md) Postgres database storing every run for durability, by creating a Postgres resource with the connection details. The result is a hosted URL that behaves exactly like the local app. From there the app stays editable in the cloud, by chat, as the dashboard evolves.

What makes it more than hosting is governance. Retool permission groups gate individual actions behind an API endpoint and an identity, so pausing and resuming an autonomous run requires an approved click by someone who is allowed to make it - [human in the loop](../../concepts/human-in-the-loop.md) enforced by the platform rather than by convention. Cole's summary of the value: "Your team regardless has a single governed path to production with audit trails" [0:23:26], whether the app was built inside Retool or imported from code.

He uses this pattern beyond agent orchestration, deploying observability dashboards for his [second brain](../../concepts/second-brain.md) and his AI coding systems. The general shape is worth stealing even if you never use Retool: build the control plane locally with a coding agent, then move it to a platform that supplies auth, permissions, and audit trails so a long-running agent system has a real front door.

## Realizes

- [Agent Deployment](../../concepts/agent-deployment.md) - Getting agents to production, containerizing, networking, reverse-proxying, and choosing a provider-agnostic, cost-predictable host.
- [Human in the Loop](../../concepts/human-in-the-loop.md) - Keeping a human as the approver and steerer of agentic work rather than fully automating, so AI augments engineers instead of replacing them.
- [Permission Management](../../concepts/permission-management.md) - Allowlisting the specific safe actions an agent may take unattended rather than granting blanket autonomy.
- [Agent Observability](../../concepts/agent-observability.md) - Instrumenting agents with tracing, logging, and cost/token metrics so you can see and debug what they actually did.
- [Full-Stack AI Application](../../concepts/full-stack-ai-application.md) - Combining an AI agent with a real front end, database, and API integrations, with the agent acting as the brain connecting the UI to back-end services.

## Contrasts with

- [No-Code vs. Code](../../concepts/no-code-vs-code.md) - The use-case-by-use-case decision to build agents visually or in code; Retool's code-import path refuses the either/or.
- [Hybrid No-Code + Code Architecture](../../concepts/hybrid-no-code-and-code.md) - Using a visual platform for the surface and orchestration while heavy logic lives in code you deploy separately.

## Works with

- [React](./react.md) - The front-end library the dashboard is written in; Retool imports the built code directly.
- [Neon](./neon.md) - Serverless Postgres platform Cole favors, connected as a Retool resource to surface stored agent runs.
- [Pi](./pi-coding-agent.md) - A minimalistic, open-source coding agent; the API the deployed dashboard drives behind the scenes.
- [Claude Code](./claude-code.md) - Built the entire React dashboard locally before it was imported and deployed.

## Related

- [Loop Engineering](../../concepts/loop-engineering.md) - Designing self-prompting loops so coding agents pick up and run work autonomously instead of you prompting them each time.
- [Long-Running Agents](../../concepts/long-running-agents.md) - Coding agents that run autonomously for hours as background tasks, the workload this dashboard supervises.
- [Second Brain](../../concepts/second-brain.md) - A personal, always-on AI system whose observability dashboards Cole also deploys this way.

## Sources

- [The Creators of Claude Code and OpenClaw don't Prompt Their Agents Anymore?!](../../sources/the-creators-of-claude-code-and-openclaw-dont-prompt-their-agents-anymore.md) - "[0:21:23] Retool is a tool specifically I've been leaning on a lot for these kinds of deployments... it's so easy to create an app here and then we can import React code."
- [The Creators of Claude Code and OpenClaw don't Prompt Their Agents Anymore?!](../../sources/the-creators-of-claude-code-and-openclaw-dont-prompt-their-agents-anymore.md) - "[0:23:26] Your team regardless has a single governed path to production with audit trails."
