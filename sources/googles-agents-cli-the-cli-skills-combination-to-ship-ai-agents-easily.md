---
type: source
title: "Google's Agents CLI: The CLI + Skills Combination to Ship AI Agents EASILY"
description: "By pairing Google's Agents CLI (capabilities) with skills (instructions), a coding assistant can drive an AI agent from idea to a scalable production deployment entirely through natural language, without the developer touching the docs or the terminal."
youtube_id: 1wfY7GCVvh0
url: https://www.youtube.com/watch?v=1wfY7GCVvh0
slug: googles-agents-cli-the-cli-skills-combination-to-ship-ai-agents-easily
published: 2026-06-10
duration: "0:15:19"
recency_rank: 10
raw: "../raw/googles-agents-cli-the-cli-skills-combination-to-ship-ai-agents-easily.md"
tags: [adk, agents-cli, agent-deployment]
created: 2026-07-21
updated: 2026-07-21
---

Cole demonstrates Google's open-source Agents CLI, a tool for building agents with Google's ADK framework, and argues that a CLI-plus-skills combination has made shipping production agents dramatically easier than even a year ago. The core mental model: the CLI provides the capabilities (scaffold, evaluate, run, optimize prompts, deploy), while the skills that ship with it tell the coding agent how to use the CLI, including baking the entire ADK documentation into the agent so you never read the docs yourself. Because every stage of the agent lifecycle has both a CLI command and a matching skill, a coding agent like Claude Code can drive the whole process end to end from your spec.

He does a live build of an "ask your data" agent that takes a CSV plus a question and uses code execution (Python/Pandas) to answer it, choosing code execution deliberately because doing it securely in isolated sandboxes is exactly the hard part the ADK and Google Cloud handle for you at deploy time. Working entirely in Claude Code, he installs the CLI and skills with a single command, builds the agent, wires up a simple Streamlit UI to test it, then in fresh conversations evaluates it against a generated test set and deploys it to GCP, all without running a single terminal command himself.

The video also addresses why "traditional" frameworks like ADK, Pydantic AI, or LangChain still matter in the era of coding agent SDKs. Coding agent SDKs are powerful and great for things you run yourself (like a second brain) where output quality beats speed and cost, but they are less token-efficient and slower. For anything embedded in a platform or served to customers, where a first token within ~4 seconds decides whether users stay, you want a minimalistic framework you control for prompting and tooling so the agent is fast, lightweight, and scalable to millions of users. The deployed agent gets memory, evaluation, sandboxed code execution, full trace auditability, and its own identity with configurable permissions.

## Concepts covered

- [AI Coding Harness](../concepts/ai-coding-harness.md)
- [Skills](../concepts/skills.md)
- [Context Engineering](../concepts/context-engineering.md)
- [Code Execution](../concepts/code-execution.md)
- [Validation](../concepts/validation.md)
- [Model Selection](../concepts/model-selection.md)
- [Planning with AI](../concepts/planning-with-ai.md)
- [Agentic Coding](../concepts/agentic-coding.md)
- [Agent Deployment](../concepts/agent-deployment.md)
- [The Evolution of AI Coding](../concepts/the-evolution-of-ai-coding.md)

## Entities

- [Claude Code](../entities/tools/claude-code.md)
- [Claude Agent SDK](../entities/tools/claude-agent-sdk.md)
- [Pydantic AI](../entities/tools/pydantic-ai.md)
- [LangChain](../entities/tools/langchain.md)
- [Streamlit](../entities/tools/streamlit.md)
- [Cole Medin](../entities/people/cole-medin.md)

## Key moments

- **[0:00:00]** Thesis: a CLI + skills combination lets your coding assistant take an agent from idea to reliable deployment
- **[0:01:14]** Memory lane: from line-by-line LangChain builds in VS Code to living in docs, to today where skills inject all the docs
- **[0:03:17]** Core framing: the CLI is the capability, the skills are the instructions on how to use it
- **[0:05:03]** Live build begins entirely in Claude Code; installs the CLI + skills with a single command via natural language
- **[0:05:46]** Builds an "ask your data" agent (CSV + question) using code execution, deliberately chosen as the hard-to-secure case
- **[0:07:42]** The elephant in the room: why still use traditional frameworks (ADK/Pydantic AI/LangChain) when we have coding agent SDKs
- **[0:09:11]** The 4-second first-token rule: platform agents must be fast and lightweight to scale to millions
- **[0:11:03]** Evaluates the agent in a fresh conversation using a generated test set; all cases pass
- **[0:12:16]** Deploys to GCP with "deploy this agent"; gets a console playground URL, traces, sandboxed execution
- **[0:13:14]** Production agent has memory, evals, sandboxed code execution, trace auditability, and its own identity/permissions

## Transcript

[Raw transcript](../raw/googles-agents-cli-the-cli-skills-combination-to-ship-ai-agents-easily.md)
