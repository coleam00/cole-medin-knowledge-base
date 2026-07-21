---
type: source
title: "Build BEAUTIFUL Diagrams with Claude Code (Full Workflow)"
description: "Packaging a diagramming workflow into a reusable skill lets any coding agent produce beautiful, educational Excalidraw diagrams that argue visually and self-validate by rendering and critiquing their own output."
youtube_id: m3fqyXZ4k4I
url: https://www.youtube.com/watch?v=m3fqyXZ4k4I
slug: build-beautiful-diagrams-with-claude-code-full-workflow
published: 2026-03-02
duration: "0:09:54"
recency_rank: 30
raw: "../raw/build-beautiful-diagrams-with-claude-code-full-workflow.md"
tags: [skills, diagrams, claude-code, validation]
created: 2026-07-21
updated: 2026-07-21
---

# Build BEAUTIFUL Diagrams with Claude Code (Full Workflow)

Cole shares an Excalidraw diagram skill he built and open-sourced so any coding agent (Claude Code or otherwise) can generate polished, practical diagrams from any input source: a markdown file, a YouTube script, a PDF, a codebase, or raw text. Installation is just cloning the repo and dropping its contents (including the SKILL.md instruction set and a reference folder) into the agent's skills directory. The agent loads the skill on demand, generates the Excalidraw JSON, and the user renders it for free at excalidraw.com or via the Obsidian Excalidraw plugin.

The heart of the skill is teaching the agent to 'argue visually' rather than dumping content into blocks. The structure and labels should carry the argument so that even with explanatory text stripped out, the concept is still legible. The skill has the agent ask two questions: does the visual structure mirror the concept's behavior, and could someone learn something concrete from this diagram. Its standout feature is a self-validation loop: the agent renders the diagram to a PNG via a Python script, looks at the screenshot, finds visual imperfections (janky arrows, bad colors, missing information), and edits the JSON in place, typically iterating two to four times.

The workflow is: start with your idea, assess the diagram's depth (complex diagrams must be built section by section to avoid Claude Code's 32,000-token output limit), map the pattern into shapes and text, build the JSON, then run the validation loop. Output is never perfect on the first pass because the LLM makes an enormous number of micro-decisions (every color, shape, position), so it produces a strong starting point that the human then refines with a few directed edits. Everything is tunable, most importantly a color palette reference file the agent edits to keep diagrams on-brand.

## Concepts covered

- [Skills](../concepts/skills.md)
- [Validation](../concepts/validation.md)
- [Human in the Loop](../concepts/human-in-the-loop.md)
- [Deterministic Workflows](../concepts/deterministic-workflows.md)
- [Effective Prompting](../concepts/effective-prompting.md)
- [Progressive Disclosure](../concepts/progressive-disclosure.md)

## Entities

- [Claude Code](../entities/tools/claude-code.md)
- [Obsidian](../entities/tools/obsidian.md)
- [GitHub](../entities/tools/github.md)
- [Cole Medin](../entities/people/cole-medin.md)
- [Dynamous](../entities/organizations/dynamous.md)

## Key moments

- **[0:00:35]** Cole packages his entire diagramming workflow into a skill so any coding agent can build diagrams
- **[0:00:50]** How to install: clone the GitHub repo, copy contents into your agent's skills folder
- **[0:01:52]** Demo: prompt the agent to create a diagram from a file, script, or PDF
- **[0:02:40]** The skill validates visually, renders the diagram, screenshots the PNG, iterates on imperfections
- **[0:04:13]** Output is never perfect first try; took 2-3 iterations for the meta diagram
- **[0:05:27]** Core philosophy: teaching the agent to argue visually, not just stack blocks
- **[0:06:44]** Depth assessment, complex diagrams built section by section to avoid the 32k token limit
- **[0:08:32]** Color palette reference file makes diagrams on-brand and fully customizable

## Transcript

[Raw transcript](../raw/build-beautiful-diagrams-with-claude-code-full-workflow.md)
