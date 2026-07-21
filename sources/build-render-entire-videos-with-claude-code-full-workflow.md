---
type: source
title: "Build + Render ENTIRE Videos with Claude Code (Full Workflow)"
description: "By stitching HyperFrames (HTML-based rendering), a TTS engine, and an Archon-orchestrated Claude Code skill into a template-driven workflow, you can now generate full short videos with synced animation and audio end-to-end from a single idea or URL."
youtube_id: Ya51a1EJPZk
url: https://www.youtube.com/watch?v=Ya51a1EJPZk
slug: build-render-entire-videos-with-claude-code-full-workflow
published: 2026-05-13
duration: "0:15:14"
recency_rank: 14
raw: "../raw/build-render-entire-videos-with-claude-code-full-workflow.md"
tags: [video-generation, workflow, archon]
created: 2026-07-21
updated: 2026-07-21
---

# Build + Render ENTIRE Videos with Claude Code (Full Workflow)

Cole demonstrates an open-source repository that turns a one-line idea (or a URL like a blog post) into a finished, narrated short video, entirely AI-generated. The stack combines Claude Code as the agent, HyperFrames as the HTML-based scene renderer with a built-in preview editor (positioned as a more reliable step up from Remotion), ElevenLabs or the free Kokoro for voice, and Archon as the workflow engine that provides parallel execution, durability, and run isolation (state persisted to SQLite or a Neon Postgres database). Setup is deliberately trivial: clone the repo, open Claude Code, and tell it to read the README and set everything up.

The core of the system is a single Claude Code skill wrapped in an Archon workflow. Given a topic, it creates a unique run ID and isolated folder, copies a template, researches the topic through an anti-fabrication gate (so it doesn't hallucinate), and writes a script that is heavily prompt-engineered with TTS tags, breaks, and natural abbreviations. It makes one call to the TTS engine for the full audio, then syncs animation timing to that audio (audio-first), builds an index.html composition in HyperFrames, lints and inspects frame-by-frame for layout overflow, and opens a local preview. Only after review and granular iteration does it render the final MP4 - and adjustments (fixing an awkward inflection or transition) don't require re-running the whole render.

The workflow is template-driven: three example templates ship (including an Anthropic one), but the real power is having Claude Code read the README and interview you to build a custom template with your own style, scene structure, and length. Once a custom template exists (e.g. a 50-second 'concept short' with before/after analogy panels), a fresh Claude Code session that's asked to 'create a video on MCP' will automatically pick the right template. Cole frames this as an ongoing experiment rather than production-ready output, but useful today for explainers for a team or community and for quickly explaining new features to yourself.

## Concepts covered

- [Effective Prompting](../concepts/effective-prompting.md)
- [Voice Agents](../concepts/voice-agents.md)
- [Prompt Engineering](../concepts/prompt-engineering.md)
- [Adversarial Agents](../concepts/adversarial-agents.md)
- [Generative UI](../concepts/generative-ui.md)
- [Agent Deployment](../concepts/agent-deployment.md)
- [End-to-End Validation](../concepts/end-to-end-validation.md)
- [Skills](../concepts/skills.md)

## Entities

- [Remotion](../entities/tools/remotion.md)
- [Claude Code](../entities/tools/claude-code.md)
- [Archon](../entities/tools/archon.md)
- [ElevenLabs](../entities/tools/elevenlabs.md)
- [Neon](../entities/tools/neon.md)
- [Anthropic](../entities/organizations/anthropic.md)
- [Cole Medin](../entities/people/cole-medin.md)

## Key moments

- **[0:00:16]** Shows an AI-generated YouTube short with synced audio and transitions as proof it works
- **[0:00:30]** Names the stack: HyperFrames (rendering), Claude Code, ElevenLabs/Kokoro (voice), Archon (orchestration)
- **[0:02:47]** Setup demo: clone repo, open Claude Code, two-sentence prompt to read README and generate first video
- **[0:03:58]** Everything is free unless you opt into ElevenLabs; Kokoro keeps it fully free
- **[0:05:41]** Archon persists workflow state to Neon Postgres and supports parallel video generation
- **[0:06:00]** Plays the 25-second Claude Code 'agent view' video generated with no iteration
- **[0:07:36]** Excalidraw diagram walkthrough of the full workflow steps
- **[0:08:11]** Anti-fabrication gate on the research step so it doesn't hallucinate
- **[0:08:39]** Audio-first: single TTS call for full script, then sync animation timing to the audio
- **[0:09:12]** HyperFrames composition is just index.html; lint + frame-by-frame layout overflow inspection
- **[0:09:44]** Built-in HyperFrames preview mode to review and adjust before rendering the MP4
- **[0:11:12]** Second example: custom 30-second Archon explainer template
- **[0:12:07]** How to build your own template by having Claude Code interview you

## Transcript

[Raw transcript](../raw/build-render-entire-videos-with-claude-code-full-workflow.md)
