---
type: entity
subtype: tool
title: "Google Agents CLI"
description: "Google's free open-source CLI and skill collection that instructs a coding agent to build, evaluate, deploy, and monitor agents on the ADK."
resource: "https://github.com/google/adk-python"
tags: [agent-framework, sdk]
videos: [googles-agents-cli-the-cli-skills-combination-to-ship-ai-agents-easily, harness-engineering-what-separates-top-agentic-engineers-right-now]
created: 2026-07-21
updated: 2026-07-21
---

# Google Agents CLI

The Google Agents CLI is a free, open-source command-line tool that ships as a bundle of [Skills](../../concepts/skills.md) for a coding agent - not a chat product you talk to, but instructions your existing assistant loads to build agents correctly. Cole's definition is precise: "It's a collection of skills that I can bring into my coding agent that give it full clear instructions on how to build agents with the Google agent SDK and even deploy them to production and monitor them" ([0:08:10]). He introduces it as the on-ramp to the framework itself - "we're going to be using Google's agent CLI for this. It is a very powerful tool. It's open source" ([0:00:15]) - making it the harness layer that sits above the [Google ADK](./google-adk.md).

## How Cole uses it / why it matters

The Agents CLI is Cole's flagship example of a vendor shipping a real [AI Coding Harness](../../concepts/ai-coding-harness.md) instead of documentation. Its differentiator is coverage of the whole lifecycle, which is exactly where most skill collections stop short: "this is what I love about Google's Agent CLI. There are a lot of frameworks out there that have skills to help you build agents, but they don't take it as far as going to your deployment and even production observability" ([0:04:07]). Scaffold, write agent code, run evals, deploy, publish, trace - each stage is a skill the coding agent loads on demand, which is [Progressive Disclosure](../../concepts/progressive-disclosure.md) applied to a whole [Agent Development Lifecycle](../../concepts/agent-development-lifecycle.md).

The payoff Cole demonstrates is wall-clock: "6 minutes later and our agent is now deployed to production. So, it literally spun up an instance in GCP for us to host our agent" ([0:12:43]). That is the point of harness engineering. The model was always capable of writing ADK code and gcloud commands; what the skills supply is the correct sequence, the flags, and the validation gates, so [Agent Deployment](../../concepts/agent-deployment.md) stops being a multi-day yak shave. It is also a template other vendors should copy - a CLI plus skills is how you make your framework the path of least resistance for every coding agent on the market.

## Realizes

- [Skills](../../concepts/skills.md) - Ships as model-invoked capability packages loaded on demand by the coding agent.
- [AI Coding Harness](../../concepts/ai-coding-harness.md) - The scaffolding of instructions, commands, and validation that makes the model reliable at agent building.
- [Agent Development Lifecycle](../../concepts/agent-development-lifecycle.md) - Covers scaffold, build, evaluate, deploy, publish, and observe rather than just codegen.
- [Agent Deployment](../../concepts/agent-deployment.md) - Spins up a GCP instance and ships the agent to production in minutes.
- [Agent Observability](../../concepts/agent-observability.md) - Extends past deployment into production tracing and monitoring.

## Contrasts with

- [Archon](./archon.md) - Cole's own open-source harness builder, the same idea authored by you rather than by the vendor.
- [Claude Agent SDK](./claude-agent-sdk.md) - A programmatic harness library, versus a skill bundle that steers whatever agent you already run.

## Works with

- [Google ADK (Agent Development Kit)](./google-adk.md) - The agent framework the CLI exists to build on top of.
- [Claude Code](./claude-code.md) - The coding agent Cole loads the skills into to drive the whole flow.
- [Vertex AI](./vertex-ai.md) - Google's platform the deployed agents run against.

## Related

- [Progressive Disclosure](../../concepts/progressive-disclosure.md) - Loading only the skill the current stage needs instead of every instruction upfront.
- [Meta-Harness](../../concepts/meta-harness.md) - A layer above individual coding assistants orchestrating them on larger jobs.
- [Agent Evaluation](../../concepts/agent-evaluation.md) - The eval-and-fix loop the CLI's skills encode before deployment.
- [Agents That Build Agents](../../concepts/agents-that-build-agents.md) - A coding agent producing production agents, which is what this toolchain enables.
- [Commandify Everything](../../concepts/commandify-everything.md) - Packaging a repeated multi-step process into invocable commands.

## Sources

- [Google's Agents CLI: The CLI + Skills Combination to Ship AI Agents EASILY](../../sources/googles-agents-cli-the-cli-skills-combination-to-ship-ai-agents-easily.md) - "[0:00:15] we're going to be using Google's agent CLI for this. It is a very powerful tool. It's open source."
- [Google's Agents CLI: The CLI + Skills Combination to Ship AI Agents EASILY](../../sources/googles-agents-cli-the-cli-skills-combination-to-ship-ai-agents-easily.md) - "[0:04:07] this is what I love about Google's Agent CLI. There are a lot of frameworks out there that have skills to help you build agents, but they don't take it as far as going to your deployment and even production observability."
- [Google's Agents CLI: The CLI + Skills Combination to Ship AI Agents EASILY](../../sources/googles-agents-cli-the-cli-skills-combination-to-ship-ai-agents-easily.md) - "[0:12:43] 6 minutes later and our agent is now deployed to production. So, it literally spun up an instance in GCP for us to host our agent."
- [Harness Engineering: What Separates Top Agentic Engineers Right Now](../../sources/harness-engineering-what-separates-top-agentic-engineers-right-now.md) - "[0:08:10] It's a collection of skills that I can bring into my coding agent that give it full clear instructions on how to build agents with the Google agent SDK and even deploy them to production and monitor them."
