---
type: entity
subtype: tool
title: "Excalidraw"
description: "Free, open-source hand-drawn-style diagramming tool whose JSON format coding agents can generate directly, rendered at excalidraw.com or through the Obsidian Excalidraw plugin."
resource: "https://excalidraw.com"
tags: [diagrams, productivity, integration]
videos: [build-beautiful-diagrams-with-claude-code-full-workflow]
created: 2026-07-21
updated: 2026-07-21
---

# Excalidraw

Excalidraw is a free, open-source diagramming tool with a hand-drawn visual style, and in Cole's workflow it is less a drawing app than a file format a coding agent can write. It is his default: "I love using Excaladrop for all of my diagrams... I build dozens of these every single month" [0:00:18]. What makes it agent-friendly is that a diagram is plain JSON, so [Claude Code](./claude-code.md) can emit an entire diagram as a file rather than a human dragging shapes. Rendering is deliberately zero-friction and zero-cost: "you can just go to excalraw.com and load it from your local file system or you can use the Excal plugin in Obsidian. Both are very valid and excal.com is entirely free" [0:02:33], which makes [Obsidian](./obsidian.md) a viable home for generated diagrams alongside notes.

Because the format is text, Excalidraw is the substrate for one of Cole's clearest [skills](../../concepts/skills.md) examples: a diagramming skill he open-sourced on [GitHub](./github.md) that any coding agent can install by dropping the SKILL.md and its reference folder into the skills directory. The skill teaches the agent to argue visually, so structure and labels carry the meaning even with explanatory text stripped out, rather than stacking content into boxes.

The interesting mechanic is what happens after generation. The agent renders its own JSON to a PNG through a Python script, looks at the screenshot, finds janky arrows or bad colors or missing information, and edits the JSON in place, typically two to four times. That [visual self-validation loop](../../concepts/visual-self-validation.md) only works because the diagram is a text file the agent can both read back and rewrite. The workflow also has to respect [context window limits](../../concepts/context-window-limits.md): complex diagrams are built section by section to stay under the agent's 32,000-token output ceiling.

Output is never right on the first pass, since the model is making an enormous number of micro-decisions about color, shape, and position. Cole treats it as a strong starting point that a human refines with a few directed edits, and a color palette reference file keeps everything on brand.

## Realizes

- [Visual Self-Validation Loop](../../concepts/visual-self-validation.md) - Giving an agent the ability to render its own visual output to an image, look at the screenshot, spot imperfections, and edit the source in place over several iterations.
- [Skills](../../concepts/skills.md) - Reusable, model-invoked capability packages that load specialized instructions and tools on demand to extend an agent.

## Works with

- [Claude Code](./claude-code.md) - Anthropic's terminal-based agentic coding assistant, the agent that generates and iterates on the diagram JSON.
- [Obsidian](./obsidian.md) - Free, local, markdown-based knowledge app that renders Excalidraw diagram JSON through its plugin.
- [GitHub](./github.md) - Where the diagram skill is published, cloned, and dropped into an agent's skills folder.

## Related

- [Validation](../../concepts/validation.md) - Building explicit checks into agentic workflows so the AI verifies its own output against real success criteria before moving on.
- [Human in the Loop](../../concepts/human-in-the-loop.md) - Keeping a human as the approver and steerer of agentic work; here, the few directed edits after the agent's first pass.
- [Progressive Disclosure](../../concepts/progressive-disclosure.md) - Loading context, skills, and tools on demand only when a task needs them instead of front-loading everything into the context window.
- [Context Window Limits](../../concepts/context-window-limits.md) - Managing finite context by summarizing, compacting, and sizing what you load so the model stays sharp on long tasks.
- [Deterministic Workflows](../../concepts/deterministic-workflows.md) - Encoding known steps as fixed code paths and reserving the LLM for the genuinely fuzzy decisions, trading autonomy for reliability.
- [Effective Prompting](../../concepts/effective-prompting.md) - Keeping prompts simple, specific, and high-quality, and knowing when prompt tricks matter versus when they're overrated.

## Sources

- [Build BEAUTIFUL Diagrams with Claude Code (Full Workflow)](../../sources/build-beautiful-diagrams-with-claude-code-full-workflow.md) - "[0:00:18] I love using Excaladrop for all of my diagrams... I build dozens of these every single month."
- [Build BEAUTIFUL Diagrams with Claude Code (Full Workflow)](../../sources/build-beautiful-diagrams-with-claude-code-full-workflow.md) - "[0:02:33] you can just go to excalraw.com and load it from your local file system or you can use the Excal plugin in Obsidian. Both are very valid and excal.com is entirely free."
