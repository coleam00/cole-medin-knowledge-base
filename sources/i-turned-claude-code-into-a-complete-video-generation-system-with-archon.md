---
type: source
title: "I Turned Claude Code Into a Complete Video Generation System (with Archon)"
description: "Archon's agentic harness pattern isn't limited to AI coding; the same Ralph-loop orchestration can fan out parallel agents to generate an entire product catalog of marketing videos using the Higgsfield CLI."
youtube_id: deeOA6YVfqw
url: https://www.youtube.com/watch?v=deeOA6YVfqw
slug: i-turned-claude-code-into-a-complete-video-generation-system-with-archon
published: 2026-07-12
duration: "0:14:08"
recency_rank: 2
raw: "../raw/i-turned-claude-code-into-a-complete-video-generation-system-with-archon.md"
tags: [archon, agentic-workflows, ralph-loop]
created: 2026-07-21
updated: 2026-07-21
---

Cole demonstrates that Archon, his open-source harness builder originally created for AI coding, generalizes to any long-running agentic workflow. He builds an "AI content factory" that generates marketing videos for a whole e-commerce product catalog, driven entirely by Archon workflows plus Higgsfield, a video-generation platform with a CLI so the coding agent never leaves its terminal. Because generating dozens of videos is far too large a task for a single coding-agent session, an orchestrator fans out to parallel worker agents that each pull one product from a queue.

The system is structured as two Ralph loops. The first "explore" workflow generates concept images for each product, has Gemini score/validate them, auto-scraps bad ones, and surfaces the good ones to a human review queue (approve in the UI, which updates a local markdown document). Only approved images move to the second "render" workflow, which animates each approved concept into a full video. Doing image-first-then-video validation saves rendering credits by confirming a good product representation before spending on the expensive video render.

Each worker follows the Ralph-loop pattern: grab the next item from the queue, and if nothing comes back, output "complete" to exit the loop. The explore workflow runs five workers in parallel; the render workflow runs three (fewer because rendering costs more credits). Cole frames the whole thing as taking ideas from AI coding, harness engineering, and the Ralph loop and applying them to content marketing, with the primary coding agent (Claude Code, Codex, etc.) acting as the orchestrator that monitors the running Archon workflow.

## Concepts covered

- [Agentic Workflow Engineering](../concepts/agentic-workflow-engineering.md)
- [The Ralph Loop](../concepts/the-ralph-loop.md)
- [AI Coding Harness](../concepts/ai-coding-harness.md)
- [Parallel Agentic Coding](../concepts/parallel-agentic-coding.md)
- [Human in the Loop](../concepts/human-in-the-loop.md)
- [Validation](../concepts/validation.md)
- [Skills](../concepts/skills.md)

## Entities

- [Archon](../entities/tools/archon.md)
- [Claude Code](../entities/tools/claude-code.md)
- [Codex](../entities/tools/codex.md)
- [Cole Medin](../entities/people/cole-medin.md)

## Key moments

- **[0:00:00]** Archon recap: open-source harness builder for AI coding, ~23k stars, connecting many agents for long autonomous tasks
- **[0:00:36]** People use Archon for non-coding agentic workflows (research, content creation)
- **[0:01:19]** Introduces the AI content factory: marketing videos for a product catalog, driven by Archon + Higgsfield
- **[0:02:46]** Why Archon is needed: generating videos for dozens of products is too large for a single agent; need parallel fan-out
- **[0:03:32]** Higgsfield building block: prompt-to-video, with a CLI so you never leave the coding agent terminal
- **[0:04:12]** The Higgsfield skill instructs the agent how to use the CLI; live single-video generation with a branded reference image
- **[0:06:12]** Image-generate then validate then render-video to save credits before committing to expensive video
- **[0:07:09]** Both workflows are Ralph loops for content instead of coding; harness pattern generalizes
- **[0:07:38]** Worker prompt: take next queue item; if none returned, output complete to exit the loop; 5 workers in parallel
- **[0:08:24]** Explore workflow scores images, scraps bad ones, surfaces good ones to a human approve queue
- **[0:08:54]** Render workflow (second Ralph loop): each worker animates one approved ad then stops; 3 workers in parallel
- **[0:09:55]** Live demo: coding agent runs Archon CLI which uses Higgsfield CLI; Gemini validates/scores images
- **[0:11:42]** Result: catalog goes from still images to videos for everything
- **[0:13:20]** Approve images directly in the UI, which updates the local markdown doc that feeds the render workflow

## Transcript

[Raw transcript](../raw/i-turned-claude-code-into-a-complete-video-generation-system-with-archon.md)
