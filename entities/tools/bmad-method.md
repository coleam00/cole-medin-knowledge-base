---
type: entity
subtype: tool
title: "BMAD Method"
description: "An open-source context-engineering framework (installed via npx bmad-method install) that ships expert sub-agent personas (analyst, PM, architect, scrum master, dev, QA) as markdown prompts driving separate greenfield and brownfield planning and development workflows."
resource: "https://github.com/bmad-code-org/BMAD-METHOD"
tags: [ai-coding, coding-agent, bmad-method, agent-teams, planning]
videos: [archon-beta-launch-livestream-what-you-missed, my-complete-agentic-coding-workflow-to-build-anything-no-fluff-or-overengineering]
created: 2026-07-21
updated: 2026-07-21
---

# BMAD Method

BMAD ("breakthrough method of agile AI-driven development") is a context-engineering framework that hands you a full software team as prompts. Cole's definition: "what BMAD gives us is a bunch of different sub agents that are experts at different parts of our development workflow. So like in the agentic planning workflow, we have our analyst, we have our project manager, we have our architect" [0:10:00], and then "when we go into development, we have our scrum master agent that's kind of guiding all these different development agents to knock out the different stories" [0:10:15]. Two workflows, planning and development, each staffed by named personas with their own roles, principles, and invokable commands.

Installation is a single command, and what it drops is deliberately unremarkable: "BMAD will do is just it's going to install a bunch of configuration and sub agents like a lot of different markdown files to get us set up with BMAD in our codebase" [0:14:15]. Critically these are **not** native subagents. Each persona is a markdown file the assistant reads to change character, which is why BMAD runs unchanged in Claude Code, Cursor, or Windsurf. It also does not overwrite your project; it adds a folder alongside it, and it branches on [greenfield vs. brownfield](../../concepts/greenfield-vs-brownfield.md) so an existing codebase gets a different workflow than a fresh one.

Cole's live-stream use of it is a proof that context-engineering strategies **stack**: he runs BMAD's brainstorm, project brief, and sharded PRD, wires [Archon](./archon.md) in so each persona does RAG over crawled docs and stores its artifacts as project documents and Kanban tasks, then layers the [PRP Framework](../../concepts/prp-framework.md) on top for validation gates at execution time. The lessons he surfaces are the usual ones amplified by structure: a prior BMAD run generated 123 tasks, so cap scope, validate every output, and reset context between personas.

His considered stance is a tradeoff, not an endorsement. In the later workflow video he recommends a small set of your own slash commands "over a more complex framework like BMAD or the GitHub spec kit. They're really, really powerful, but it's hard to really make it your own."

## Realizes

- [Context Engineering](../../concepts/context-engineering.md) - the whole framework is a packaged answer to what goes into the window at each stage.
- [Agent Teams](../../concepts/agent-teams.md) - analyst, PM, architect, scrum master, dev, and QA as a coordinated cast.
- [Role Prompting](../../concepts/role-prompting.md) - each persona is a role, style, and principles block in markdown.
- [Planning with AI](../../concepts/planning-with-ai.md) - brainstorm, brief, PRD, shard, before any code.
- [PRD-First Development](../../concepts/prd-first-development.md) - the sharded PRD is the artifact everything downstream reads.
- [Granular Task Management](../../concepts/granular-task-management.md) - stories the scrum master persona feeds to dev agents one at a time.
- [Greenfield vs. Brownfield Projects](../../concepts/greenfield-vs-brownfield.md) - separate workflows for new versus existing codebases.

## Contrasts with

- [GitHub Spec Kit](./github-spec-kit.md) - the other heavyweight framework Cole names in the same breath, with the same customization objection.
- [PRP Framework](../../concepts/prp-framework.md) - lighter and validation-first; Cole stacks it on top of BMAD rather than choosing between them.
- [Slash Commands](../../concepts/slash-commands.md) - his recommended alternative: a handful of commands you own and can evolve.
- [Subagents Pattern](../../concepts/subagents-pattern.md) - BMAD deliberately uses persona prompts instead of native subagents, trading isolation for portability.

## Works with

- [Archon](./archon.md) - supplies RAG over crawled docs plus document and task storage for every BMAD artifact.
- [Claude Code](./claude-code.md) - the assistant Cole drives BMAD through in the live stream.
- [Cursor](./cursor.md) and [Windsurf](./windsurf.md) - markdown personas work in any assistant, which is the point.

## Related

- [Global Rules](../../concepts/global-rules.md) - BMAD's config sits alongside your existing rules rather than replacing them.

- [Stacking Context-Engineering Strategies](../../concepts/strategy-stacking.md) - BMAD plus Archon plus PRP in one run is the canonical demonstration.
- [Spec-Driven Development](../../concepts/spec-driven-development.md) - the family of methods BMAD belongs to.
- [Validation](../../concepts/validation.md) - the missing gate BMAD alone does not give you, which is why PRP gets stacked on.
- [Agentic Workflow Engineering](../../concepts/agentic-workflow-engineering.md) - designing the sequence of agents rather than one big prompt.
- [Agentic Coding](../../concepts/agentic-coding.md) - the practice BMAD formalizes.

## Sources

- [Archon Beta Launch Livestream - What You Missed!](../../sources/archon-beta-launch-livestream-what-you-missed.md) - "[0:10:00] what BMAD gives us is a bunch of different sub agents that are experts at different parts of our development workflow. So like in the agentic planning workflow, we have our analyst, we have our project manager, we have our architect"
- [Archon Beta Launch Livestream - What You Missed!](../../sources/archon-beta-launch-livestream-what-you-missed.md) - "[0:10:15] when we go into development, we have our scrum master agent that's kind of guiding all these different development agents to knock out the different stories"
- [Archon Beta Launch Livestream - What You Missed!](../../sources/archon-beta-launch-livestream-what-you-missed.md) - "[0:14:15] BMAD will do is just it's going to install a bunch of configuration and sub agents like a lot of different markdown files to get us set up with BMAD in our codebase"
- [My COMPLETE Agentic Coding Workflow to Build Anything (No Fluff or Overengineering)](../../sources/my-complete-agentic-coding-workflow-to-build-anything-no-fluff-or-overengineering.md)
