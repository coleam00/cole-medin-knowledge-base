---
type: concept
title: "Vibe Coding"
description: "Building software by conversationally prompting an AI without closely reading the code, useful for prototypes but risky for production."
tags: [vibe-coding, prototyping, prompting]
videos: [google-just-dropped-a-masterclass-on-agentic-engineering-its-so-good, full-guide-to-becoming-a-principled-agentic-engineer-build-anything-with-ai, is-software-engineering-finally-dead, this-one-command-makes-coding-agents-find-all-their-mistakes-use-it-now, i-was-wrong-about-ralph-wiggum, ralph-wiggum-is-the-final-evolution-of-vibe-coding-heres-what-comes-next, ai-exploded-in-2025-heres-everything-that-happened, are-agent-harnesses-bringing-back-vibe-coding, github-is-the-future-of-ai-coding-heres-why, the-true-power-of-ai-coding-build-your-own-workflows-full-guide, archon-beta-launch-livestream-what-you-missed, a-complete-guide-to-claude-code-here-are-all-the-best-strategies, context-engineering-101-the-simple-strategy-to-100x-ai-coding, context-engineering-is-the-new-vibe-coding-learn-this-now, introducing-rag-20-agentic-rag-knowledge-graphs-free-template, how-id-learn-ai-agents-fast-if-i-had-to-start-over-full-roadmap, the-ultimate-guide-to-building-your-own-mcp-servers-free-template, brand-new-stealth-llm-released-on-openrouter-its-a-beast, code-100x-faster-with-ai-heres-how-no-hype-full-process, lets-settle-the-o3-mini-vs-r1-debate-for-coding-once-and-for-all, deepseek-r1-just-revolutionized-ai-forever, pydantic-ai-deepseek-v3-the-best-ai-agent-combo, i-forked-boltnew-and-made-it-way-better, build-a-full-stack-app-for-your-n8n-ai-agent-in-20-minutes, i-built-a-full-rag-ai-agent-with-no-code-in-4-minutes-with-vectorshift]
created: 2026-07-21
updated: 2026-07-21
---

# Vibe Coding

Vibe coding is building software by conversationally prompting an AI and trusting the output without closely reading the code. Cole's working definition: "vibe coding is where you send in a prompt without much planning. And then your validation is, hey, does it seem like it work?" The term was coined by Andrej Karpathy and went mainstream fast, "the AI engineer Andre Karpathy coined the term Vibe coding and it has gained so much popularity that it literally has its own Wikipedia page now." At its extreme it means abandoning the code entirely: "we're fully giving into the vibes of our coding agent. We're embracing exponentials. We're forgetting the code even exists," with "no structured plan... You trust the AI, and you allow it to just iterate and iterate."

Cole is consistently not a proponent of vibe coding for anything you intend to keep. The failure mode is the missing validation: "validation is always important and that's the big thing that like is so wrong with vibe coding, right? Is there just never that validation." Intuition does not carry to real systems, "We know that vibe coding builds prototypes that break when you try to scale," and the deeper problem is human review: "It's vibe coding. AI code without human review that is the problem. Because here's the thing, intuition does not scale. Structure does." His hard rule for production is blunt: "never vive anything into production. We have to be the software engineer." He also flags the security exposure, citing a builder who "gets hacked... Maxed out usage on API keys, people bypassing subscriptions, probably because he didn't have correct database security."

The nuance Cole has come to accept is that vibe coding has a legitimate niche: throwaway prototypes and proofs of concept. "Sometimes vibe coding is actually enough for proof of concepts or you just want to create an MVP. I used to just always dismiss vibe coding. But I think there is genuinely a place for it." And it is not a dead end. With a sufficiently engineered harness, the ergonomics of vibe coding can return safely: "if we solve these problems and we have a very engineered harness that has human in the loop and all of the self- validation, then vibe coding is viable." That is the opposite of raw vibe coding, where "you just give all power to the coding assistant. You trust it entirely and you're not engineering a system."

## Contrasts with

- [Agentic Coding](./agentic-coding.md) - the engineered alternative that replaces vibes with a defined process.
- [The PIV Loop](./the-piv-loop.md) - the plan/implement/validate discipline vibe coding skips.
- [Planning with AI](./planning-with-ai.md) - vibe coding sends a prompt "without much planning."
- [Validation](./validation.md) - the quality gate that is "just never" present in vibe coding.
- [Context Engineering](./context-engineering.md) - "the new vibe coding": structure and curated context instead of intuition.

## Related

- [The Evolution of AI Coding](./the-evolution-of-ai-coding.md) - vibe coding as one era on the path toward engineered harnesses.
- [The Ralph Loop](./the-ralph-loop.md) - framed as "the final evolution of vibe coding," made safe by loops and validation.
- [AI Coding Harness](./ai-coding-harness.md) - the engineered system that makes vibe-coding ergonomics viable again.
- [Human in the Loop](./human-in-the-loop.md) - the review vibe coding removes and a good harness restores.
- [Reduce Assumptions](./reduce-assumptions.md) - vibe coding leaves the agent's assumptions unchecked.
- [Agent Security](./agent-security.md) - unreviewed vibe-coded apps ship exploitable security holes.
- [Model Selection](./model-selection.md) - stronger models can one-shot prototypes, tempting more vibe coding.
- [Build Your Own MCP Server](./build-your-own-mcp-server.md) and [Claude Code Hooks](./claude-code-hooks.md) - Cole teaches building these while insisting you understand, not vibe, what you ship.
- [Rapid Prototyping](./rapid-prototyping.md) - the legitimate niche where vibe coding is "enough."

## Tools

- [bolt.new](../entities/tools/bolt-new.md) - browser-based one-shot app builder, a classic vibe-coding surface.
- [Cursor](../entities/tools/cursor.md) - "the final boss for the most autonomous agent" that can run a whole issue-to-PR flow.

## Sources

- [Google Just Dropped a Masterclass on Agentic Engineering](../sources/google-just-dropped-a-masterclass-on-agentic-engineering-its-so-good.md) - "[0:04:02] vibe coding is where you send in a prompt without much planning. And then your validation is, hey, does it seem like it work?"
- [Google Just Dropped a Masterclass on Agentic Engineering](../sources/google-just-dropped-a-masterclass-on-agentic-engineering-its-so-good.md) - "[0:04:51] Sometimes vibe coding is actually enough for proof of concepts or you just want to create an MVP. I used to just always dismiss vibe coding. But I think there is genuinely a place for it."
- [Ralph Wiggum is the Final Evolution of Vibe Coding](../sources/ralph-wiggum-is-the-final-evolution-of-vibe-coding-heres-what-comes-next.md) - "[0:03:05] when vibe coding was coined at the start of last year... we're fully giving into the vibes of our coding agent. We're embracing exponentials. We're forgetting the code even exists."
- [Context Engineering is the New Vibe Coding (Learn this Now)](../sources/context-engineering-is-the-new-vibe-coding-learn-this-now.md) - "[0:01:11] It's vibe coding. AI code without human review that is the problem. Because here's the thing, intuition does not scale. Structure does."
- [Context Engineering 101 - The Simple Strategy to 100x AI Coding](../sources/context-engineering-101-the-simple-strategy-to-100x-ai-coding.md) - "[0:19:03] validation is always important and that's the big thing that like is so wrong with vibe coding, right? Is there just never that validation."
- [Is Software Engineering Finally Dead?](../sources/is-software-engineering-finally-dead.md) - "[0:15:36] the first thing I'd recommend is never vive anything into production. We have to be the software engineer."
- [Are Agent Harnesses Bringing Back Vibe Coding?](../sources/are-agent-harnesses-bringing-back-vibe-coding.md) - "[0:23:38] if we solve these problems and we have a very engineered harness that has human in the loop and all of the self- validation, then vibe coding is viable."
- [Are Agent Harnesses Bringing Back Vibe Coding?](../sources/are-agent-harnesses-bringing-back-vibe-coding.md) - "[0:23:54] the general idea of Vive coding is that you just give all power to the coding assistant. You trust it entirely and you're not engineering a system."
- [FULL Guide to Becoming a Principled Agentic Engineer](../sources/full-guide-to-becoming-a-principled-agentic-engineer-build-anything-with-ai.md) - "[0:02:53] we're not vibe coding because we are putting ourselves in the driver's seat along the way through all of the planning and validation that we do."
- [AI Exploded in 2025 - Here's Everything That Happened](../sources/ai-exploded-in-2025-heres-everything-that-happened.md) - "[0:02:38] the AI engineer Andre Karpathy coined the term Vibe coding and it has gained so much popularity that it literally has its own Wikipedia page now."
- [Code 100x Faster with AI, Here's How](../sources/code-100x-faster-with-ai-heres-how-no-hype-full-process.md) - "[0:05:14] I generally don't recommend vibe coding, but even if you do vibe code, at least make sure that you understand if your project is secure or not."
- [Context Engineering 101 - The Simple Strategy to 100x AI Coding](../sources/context-engineering-101-the-simple-strategy-to-100x-ai-coding.md) - "[0:00:36] We know that vibe coding builds prototypes that break when you try to scale."
- [I Was Wrong About Ralph Wiggum](../sources/i-was-wrong-about-ralph-wiggum.md) - "[0:00:00] you know that I'm not a fan of Vibe coding. We need to be in the driver's seat when we're working with our coding agents."
- [GitHub is the Future of AI Coding (Here's Why)](../sources/github-is-the-future-of-ai-coding-heres-why.md) - "[0:13:16] cursor is definitely the final boss for the most autonomous agent."
- [I Forked Bolt.new and Made it WAY Better](../sources/i-forked-boltnew-and-made-it-way-better.md) - "[0:00:14] the amount that bolt. new speeds up my full stack development is truly unmatched."
- [I Built a FULL RAG AI Agent with No Code in 4 Minutes with VectorShift](../sources/i-built-a-full-rag-ai-agent-with-no-code-in-4-minutes-with-vectorshift.md) - "[0:00:16] it's really really common where your use case is pretty simple or you just want a fast proof of concept... it doesn't make sense to pour all the time to just reinvent the wheel."
- [Introducing RAG 2.0: Agentic RAG + Knowledge Graphs](../sources/introducing-rag-20-agentic-rag-knowledge-graphs-free-template.md) - "[0:28:37] I do not condone vibe coding. I definitely encourage you to have the knowledge to validate the output from the AI coding assistant and to kind of add that last 10% at the end."
- [Archon Beta Launch Livestream - What You Missed!](../sources/archon-beta-launch-livestream-what-you-missed.md) - "[0:44:00] Vive coding is never going to get you 100% of the way there... what we did today rushing through things was more vibe coding than I'd want to do."
