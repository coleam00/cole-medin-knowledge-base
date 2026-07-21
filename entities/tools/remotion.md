---
type: entity
subtype: tool
title: "Remotion"
description: "The earlier tool that first gave Claude Code a skill to generate videos; Cole found it less reliable than HyperFrames."
resource: "https://www.remotion.dev"
tags: [video, media, skills, claude-code]
videos: [build-render-entire-videos-with-claude-code-full-workflow, i-built-my-second-brain-with-claude-code-obsidian-skills-heres-how]
created: 2026-07-21
updated: 2026-07-21
---

# Remotion

Remotion is a programmatic video framework (videos are defined and rendered from React code) that reached Cole's audience mainly through its Claude Code [skill](../../concepts/skills.md), which let an agent generate video from a prompt. He credits it as the tool that first proved the idea and went viral for it: "It went viral a couple of months ago for really the first tool that had a skill giving Claude code the ability to generate videos wasn't really the most reliable in my experience. Hyperframes is definitely a step up" [0:00:47]. That quote captures both halves of how Cole positions Remotion, historically important as the proof of concept, but superseded in his own workflow by HyperFrames on reliability.

The reason Remotion matters here is the pattern it demonstrated rather than the tool itself. A [skill](../../concepts/skills.md) is a packaged capability an agent loads on demand, and the Remotion skill showed that a coding agent could be handed video generation as just another capability. Cole folds exactly this into his own setup: "There's the new Remotion skill that allows Claude Code to generate videos, things like B-roll that I can include for videos on my channel" [0:02:32]. So in his second-brain system Remotion is the on-ramp for agent-generated B-roll, a concrete instance of extending an agent through skills rather than bespoke integration.

In his full video-rendering workflow, though, Cole is candid that reliability is the deciding factor, and there Remotion lost ground to HyperFrames. The takeaway across both videos is consistent: Remotion earns the historical credit for making Claude Code generate video at all, while day-to-day production work migrated to a more dependable option. Pairing that video generation with narration from a TTS tool like [ElevenLabs](./elevenlabs.md) is what closes the loop on a fully agent-produced video.

## Realizes

- [Skills](../../concepts/skills.md) - reusable, model-invoked capability packages that load specialized instructions and tools on demand; Remotion reached Cole as a Claude Code skill.
- [Generative UI](../../concepts/generative-ui.md) - code-defined, generated visual output; Remotion defines and renders videos from React code in the same family.

## Works with

- [ElevenLabs](./elevenlabs.md) - the paid text-to-speech provider used for high-quality narration that pairs with Remotion over generated video.

## Related

- [Effective Prompting](../../concepts/effective-prompting.md) - keeping prompts simple, specific, and high-quality; the prompts that drive generated video.
- [Prompt Engineering](../../concepts/prompt-engineering.md) - the craft of wording and structuring a prompt so an LLM reliably produces the output you want.
- [Adversarial Agents](../../concepts/adversarial-agents.md) - pitting a generator against an adversarial critic; quality-checking patterns in the automated-media workflow.
- [Voice Agents](../../concepts/voice-agents.md) - real-time voice-to-voice agents built from speech-to-text and text-to-speech pipelines.
- [Aqua Voice](./aqua-voice.md) - speech-to-text platform Cole uses to dictate into any text box; a sibling voice-and-media tool.
- [Vapi](./vapi.md) - no-code voice AI platform cited as easy but a black box; a sibling voice-and-media tool.
- [HyperFrames](./hyperframes.md) - An HTML-based video rendering tool with a built-in preview editor that lets AI agents generate and mold animated scenes, positioned as a more reliable step up from Remotion.
- [Kokoro](./kokoro.md) - A free, open-source text-to-speech model that lets you run the entire AI video-generation workflow at no cost.
- [Sora 2](./sora-2.md) - OpenAI's video-plus-audio generation model that took the world by storm in 2025 and drew a $1B Disney investment.

## Sources

- [Build + Render ENTIRE Videos with Claude Code (Full Workflow)](../../sources/build-render-entire-videos-with-claude-code-full-workflow.md) - "[0:00:47] It went viral a couple of months ago for really the first tool that had a skill giving Claude code the ability to generate videos wasn't really the most reliable in my experience. Hyperframes is definitely a step up"
- [I Built My Second Brain with Claude Code + Obsidian + Skills (Here's How)](../../sources/i-built-my-second-brain-with-claude-code-obsidian-skills-heres-how.md) - "[0:02:32] There's the new Remotion skill that allows Claude Code to generate videos, things like B-roll that I can include for videos on my channel"
