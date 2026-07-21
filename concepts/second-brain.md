---
type: concept
title: "Second Brain"
description: "A personal, always-on AI system that captures, recalls, and acts on your knowledge and daily context."
tags: [second-brain, memory, personal-ai]
videos: [i-love-the-karpathy-llm-wiki-but-it-doesnt-scale-heres-what-does, finally-an-open-standard-for-the-karpathy-llm-wiki-is-here, the-creators-of-claude-code-and-openclaw-dont-prompt-their-agents-anymore, i-built-self-evolving-claude-code-memory-w-karpathys-llm-knowledge-bases, full-guide-build-your-own-ai-second-brain-with-claude-code, everything-you-thought-about-building-ai-agents-is-wrong, i-built-a-safer-openclaw-alternative-using-claude-code, i-built-my-second-brain-with-claude-code-obsidian-skills-heres-how, claude-codes-real-purpose-its-bigger-than-you-think]
created: 2026-07-21
updated: 2026-07-21
---

# Second Brain

A second brain is a personal, always-on AI that captures your knowledge, recalls it in context, and acts on your daily life, built on top of a coding agent and a note vault. For Cole it has been transformative: "my second brain, which I built on top of Claude code and Obsidian, has been the biggest deal for my business since I started using Claude code itself" - ["Full Guide - Build Your Own AI Second Brain with Claude Code"](../sources/full-guide-build-your-own-ai-second-brain-with-claude-code.md) [0:01:32]. Its power is cumulative: "everything compounds on itself. As you use your second brain more and more, it becomes more in tune with you, anticipating your needs" [0:01:50].

## Markdown-driven and simple

The defining architectural choice is that the whole system is plain markdown, not a database. "everything for a personal agent is markdown driven... it's just the simplest and most flexible. It is so easy to build up your knowledge base over time as you're having conversations with your second brain" - ["I Love the Karpathy LLM Wiki but it Doesn't Scale"](../sources/i-love-the-karpathy-llm-wiki-but-it-doesnt-scale-heres-what-does.md) [0:01:20]. That simplicity is deliberate, because a personal agent does not carry production's burdens: "at this point we don't really care about governance or access control or a lot of the traceability and auditability that you need in production systems" [0:01:53]. [Obsidian](../entities/tools/obsidian.md) is the canvas over those files: "This is my second brain, my knowledge base where I do all my note-taking and my YouTube scripting." - ["Claude Code's Real Purpose"](../sources/claude-codes-real-purpose-its-bigger-than-you-think.md) [0:00:18].

## Proactive and extensible

A second brain crosses from note-taking into agent when it acts before you ask. Built on the [Claude Agent SDK](../entities/tools/claude-agent-sdk.md) and inspired by [OpenClaw](../entities/tools/openclaw.md), "It builds memories over time. It does daily reflection to basically learn from its work and my requests over time" - ["Everything You Thought About Building AI Agents is Wrong"](../sources/everything-you-thought-about-building-ai-agents-is-wrong.md) [0:06:04]. The payoff is a genuinely personal agent: "It is able to remember our decisions, preferences, and context... It can check our services, do things for us before we even ask... and we can add any capability with a single file." - ["I Built a Safer OpenClaw Alternative"](../sources/i-built-a-safer-openclaw-alternative-using-claude-code.md) [0:07:55], [0:08:12]. The trend is that "pretty much everybody is building their own LLM wiki in their second brain." - ["Finally, an Open Standard for the Karpathy LLM Wiki is HERE"](../sources/finally-an-open-standard-for-the-karpathy-llm-wiki-is-here.md) [0:01:07].

## Builds on

- [Memory Systems](./memory-systems.md) - the persistent short- and long-term memory a second brain runs on.
- [The LLM Wiki](./the-llm-wiki.md) - the Karpathy-style knowledge structure most second brains adopt.
- [AI Coding Harness](./ai-coding-harness.md) - the agent runtime the second brain is built on top of.

## Part of

- [Heartbeat](./heartbeat.md) - the scheduled loop that makes a second brain proactive.

## Related

- [Self-Evolving Memory](./self-evolving-memory.md) - daily reflection that lets the second brain learn over time.
- [Git as Long-Term Memory](./git-as-long-term-memory.md) - versioned markdown as the durable substrate.
- [Skills](./skills.md) - adding any capability to the second brain with a single file.
- [Knowledge Bases](./knowledge-bases.md) - the growing corpus a second brain accumulates from conversations.
- [Human in the Loop](./human-in-the-loop.md) - the personal, review-as-you-go posture versus production governance.
- [The Ralph Loop](./the-ralph-loop.md) - an autonomous-task pattern Cole is folding into second-brain dashboards.
- [Coding Agent as General Assistant](./coding-agent-as-general-assistant.md) - A coding agent is really five capabilities (file ops, search, terminal, web search, code intelligence) and removing code intelligence leaves exactly the general on-machine assistant a second brain needs.

## Tools

- [Claude Code](../entities/tools/claude-code.md) - the agent the second brain is built on.
- [Obsidian](../entities/tools/obsidian.md) - the local, free markdown vault used as the canvas.
- [Claude Agent SDK](../entities/tools/claude-agent-sdk.md) - the runtime for the heartbeat and memory layers.
- [OpenClaw](../entities/tools/openclaw.md) - the autonomous-agent inspiration for the proactive layer.

## Sources

- [Full Guide - Build Your Own AI Second Brain with Claude Code](../sources/full-guide-build-your-own-ai-second-brain-with-claude-code.md) - "[0:01:32] my second brain, which I built on top of Claude code and Obsidian, has been the biggest deal for my business since I started using Claude code itself"
- [I Love the Karpathy LLM Wiki but it Doesn't Scale. Here's What Does.](../sources/i-love-the-karpathy-llm-wiki-but-it-doesnt-scale-heres-what-does.md) - "[0:01:20] everything for a personal agent is markdown driven... it's just the simplest and most flexible. It is so easy to build up your knowledge base over time as you're having conversations with your second brain"
- [I Built a Safer OpenClaw Alternative Using Claude Code](../sources/i-built-a-safer-openclaw-alternative-using-claude-code.md) - "[0:07:55] It is able to remember our decisions, preferences, and context. It can check our services, do things for us before we even ask. We can talk to it from anywhere, and we can add any capability with a single file."
- [Everything You Thought About Building AI Agents is Wrong](../sources/everything-you-thought-about-building-ai-agents-is-wrong.md) - "[0:06:04] It handles all my integrations and everything I wanted to take care of. It builds memories over time. It does daily reflection to basically learn from its work and my requests over time"
- [Claude Code's Real Purpose (It's Bigger Than You Think)](../sources/claude-codes-real-purpose-its-bigger-than-you-think.md) - "[0:00:18] Behind the scenes, I have it working on my Obsidian vault. This is my second brain, my knowledge base where I do all my note-taking and my YouTube scripting."
- [Finally, an Open Standard for the Karpathy LLM Wiki is HERE](../sources/finally-an-open-standard-for-the-karpathy-llm-wiki-is-here.md) - "[0:01:07] At this point, pretty much everybody is building their own LLM wiki in their second brain."
- [I Built My Second Brain with Claude Code + Obsidian + Skills (Here's How)](../sources/i-built-my-second-brain-with-claude-code-obsidian-skills-heres-how.md) - "[0:01:21] having this system legitimately makes me more excited to wake up every single day because it helps me ideulate and keep my ideas organized"
- [I Built Self-Evolving Claude Code Memory w/ Karpathy's LLM Knowledge Bases](../sources/i-built-self-evolving-claude-code-memory-w-karpathys-llm-knowledge-bases.md) - "[0:00:48] I always call it my canvas for working with things with my second brain"
- [The Creators of Claude Code and OpenClaw don't Prompt Their Agents Anymore?!](../sources/the-creators-of-claude-code-and-openclaw-dont-prompt-their-agents-anymore.md) - "[0:20:55] Building a dashboard to manage more autonomous tasks in something like your second brain is a big thing that I'm focusing on right now."
