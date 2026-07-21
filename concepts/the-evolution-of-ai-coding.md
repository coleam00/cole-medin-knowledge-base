---
type: concept
title: "The Evolution of AI Coding"
description: "How AI coding assistants moved from novelty to daily driver, and where the landscape, adoption, and commentary are heading."
tags: [ai-coding, trends, evolution, adoption, commentary]
videos: [the-best-ai-coding-setup-isnt-the-most-autonomous-one-heres-why, google-just-dropped-a-masterclass-on-agentic-engineering-its-so-good, googles-agents-cli-the-cli-skills-combination-to-ship-ai-agents-easily, ai-youtube-is-only-claude-hype-now, im-building-an-ai-dark-factory-that-ships-its-own-code-public-experiment, the-next-evolution-of-ai-coding-is-harnesses-heres-how-to-build-them, youre-hardly-using-what-claude-code-has-to-offer-its-insane, is-software-engineering-finally-dead, turn-claude-code-into-your-full-engineering-team-with-subagents, ralph-wiggum-is-the-final-evolution-of-vibe-coding-heres-what-comes-next, ai-exploded-in-2025-heres-everything-that-happened, are-agent-harnesses-bringing-back-vibe-coding, should-i-build-my-ai-agents-with-n8n-or-python, google-is-quietly-revolutionizing-ai-agents-this-is-huge, im-addicted-to-windsurf-send-help, claude-computer-use-boltnew-the-ultimate-ai-coding-combo]
created: 2026-07-21
updated: 2026-07-21
---

# The Evolution of AI Coding

The evolution of AI coding is the arc from autocomplete plugins to autonomous, orchestrated agents, told across Cole's catalog as a spectrum of maturing capability rather than a single leap. He compresses the timeline directly: "it was only a couple of years ago that we all were using these tools just for autocomplete. And then in the last year especially, we've gotten to autonomous agents that build out entire features end to end. And now Claude Code is leading the charge, turning their coding agent into essentially a multi-agent orchestration platform" [0:00:17]. The framing matters because "AI coding is a spectrum, not a switch... most people think of it as something that's binary. Either you're vibe coding or you're doing agentic engineering," and the skill is "you pick the right one for the job."

## The two evolutions

Cole tracks the shift on two axes. The first is **technique**: "prompt engineering, that was all the rage back in 2022 through 2024... then that evolved into context engineering... And now that has evolved into harness engineering, where we're dealing with many different coding agent sessions, all tying that together through a harness." He extends the same lineage to [intent engineering](./the-piv-loop.md) ("prompt engineering to context engineering then to the new intent engineering") and is careful that each stage builds on the last: "harnesses rely on everything that we've learned from context engineering and prompt engineering. So this is not a replacement."

The second is **autonomy**, borrowed from the five levels of self-driving cars: "five levels from spicy autocomplete to the dark factory. And it's really important for you to understand the level that you're currently at and what you should be shooting for." Level zero, "spicy autocomplete," is "a reference tool or enhanced search. So like a smarter Stack Overflow"; the ceiling is the fully autonomous [dark factory](./dark-factory.md). Vibe coding sits on this ladder too, and Cole marks its limit: "That is the ceiling of vibe coding because we can't go beyond forcing our coding agent to run until it finally says the application is complete."

## Adoption and commentary

The landscape narrative also covers how the tools and their discourse spread. Protocols mature slowly, "MCP was never a hype train... people just gradually realize over time that it's the real deal," because "for more technical protocols, it takes time for people to grasp them." Adoption reshapes adjacent tools ("part of the advantage of n8n being easier to build things... that's starting to diminish just thanks to AI coding assistance") and even the human role ("everything except for the coding is our responsibility because we are the ones doing the context engineering"). Cole positions his own coverage against churn: "I'm not going to rush to make a video within 4 hours of that thing being released. I'm going to actually tinker with it, incorporate it into my systems, and then teach you that."

## Builds on

- [Agentic Coding](./agentic-coding.md) - the mainstream present of the arc.
- [Context Engineering](./context-engineering.md), [AI Coding Harness](./ai-coding-harness.md), [Agentic Workflow Engineering](./agentic-workflow-engineering.md) - the successive techniques the evolution runs through.

## Related

- [The PIV Loop](./the-piv-loop.md) - intent engineering, the stage Cole names after context engineering.
- [Vibe Coding](./vibe-coding.md), [Dark Factory](./dark-factory.md) - endpoints on the autonomy spectrum.
- [Human in the Loop](./human-in-the-loop.md) - the recurring argument that more autonomy is not always the right setting.
- [Agent Teams](./agent-teams.md), [System Evolution](./system-evolution.md), [Agent Protocols](./agent-protocols.md), [Model Context Protocol (MCP)](./mcp.md) - the multi-agent, self-improving, and protocol layers the newest stage depends on.

## Tools

- [Claude Code](../entities/tools/claude-code.md) - the tool Cole credits with leading the multi-agent orchestration turn.
- [Windsurf](../entities/tools/windsurf.md), [Codex](../entities/tools/codex.md), [n8n](../entities/tools/n8n.md) - waypoints in the landscape's shift from IDE assistants to agents.

## Sources

- [You're Hardly Using What Claude Code Has to Offer, it's Insane](../sources/youre-hardly-using-what-claude-code-has-to-offer-its-insane.md) - "[0:00:17] it was only a couple of years ago that we all were using these tools just for autocomplete... And now Claude Code is leading the charge, turning their coding agent into essentially a multi-agent orchestration platform."
- [Google Just Dropped a Masterclass on Agentic Engineering (It's SO Good)](../sources/google-just-dropped-a-masterclass-on-agentic-engineering-its-so-good.md) - "[0:03:47] AI coding is a spectrum, not a switch. And I really appreciate that because most people think of it as something that's binary."
- [The Next Evolution of AI Coding Is Harnesses - Here's How to Build Them](../sources/the-next-evolution-of-ai-coding-is-harnesses-heres-how-to-build-them.md) - "[0:03:23] then that evolved into context engineering... And now that has evolved into harness engineering, where we're dealing with many different coding agent sessions, all tying that together through a harness."
- [The Best AI Coding Setup Isn't the Most Autonomous One (Here's Why)](../sources/the-best-ai-coding-setup-isnt-the-most-autonomous-one-heres-why.md) - "[0:00:18] five levels from spicy autocomplete to the dark factory. And it's really important for you to understand the level that you're currently at and what you should be shooting for"
- [Is Software Engineering Finally Dead?](../sources/is-software-engineering-finally-dead.md) - "[0:08:01] the best way to quickly explain why we need to be a software engineer so much still is to look at the evolution of prompt engineering to context engineering then to the new intent engineering"
- [Ralph Wiggum is the Final Evolution of Vibe Coding (Here's What Comes Next)](../sources/ralph-wiggum-is-the-final-evolution-of-vibe-coding-heres-what-comes-next.md) - "[0:04:50] That is the ceiling of vibe coding because we can't go beyond forcing our coding agent to run until it finally says the application is complete."
- [Are Agent Harnesses Bringing Back Vibe Coding?](../sources/are-agent-harnesses-bringing-back-vibe-coding.md) - "[0:03:19] harnesses rely on everything that we've learned from context engineering and prompt engineering. So this is not a replacement."
- [I'm Building an AI Dark Factory That Ships Its Own Code (Public Experiment)](../sources/im-building-an-ai-dark-factory-that-ships-its-own-code-public-experiment.md) - "[0:03:11] he starts with level zero, which he calls spicy autocomplete... AI serves as a reference tool or enhanced search. So like a smarter Stack Overflow."
- [Google is Quietly Revolutionizing AI Agents (This is HUGE)](../sources/google-is-quietly-revolutionizing-ai-agents-this-is-huge.md) - "[0:00:21] MCP was never a hype train that people just gradually realize over time that it's the real deal."
- [AI YouTube Is Only Claude Hype Now](../sources/ai-youtube-is-only-claude-hype-now.md) - "[0:02:25] I'm not going to rush to make a video within 4 hours of that thing being released. I'm going to actually tinker with it, incorporate it into my systems, and then teach you that."
- [AI Exploded in 2025 - Here's Everything That Happened](../sources/ai-exploded-in-2025-heres-everything-that-happened.md) - "[0:06:00] This is when Claude really became the coding king for me... It still in my mind is the best agentic coding assistant"
- [I'm Addicted to Windsurf, Send Help](../sources/im-addicted-to-windsurf-send-help.md) - "[0:03:00] back in 2022 it was just manually coding... then co-pilots were introduced where you had AI help with little parts of your process like autocomplete... and then in 2024 we got to agents"
- [Should I Build My AI Agents with n8n or Python?](../sources/should-i-build-my-ai-agents-with-n8n-or-python.md) - "[0:13:44] part of the advantage of n8n being easier to build things. That's starting to diminish just thanks to AI coding assistance"
- [Google's Agents CLI: The CLI + Skills Combination to Ship AI Agents EASILY](../sources/googles-agents-cli-the-cli-skills-combination-to-ship-ai-agents-easily.md) - "[0:00:59] with tools like the agent CLI like I'll show you here it is significantly easier to build AI agents now even compared to 6 months ago."
- [Turn Claude Code into Your Full Engineering Team with Subagents](../sources/turn-claude-code-into-your-full-engineering-team-with-subagents.md) - "[0:00:55] This really is the future of AI coding."
- [Claude Computer Use + Bolt.new - The ULTIMATE AI Coding Combo?!](../sources/claude-computer-use-boltnew-the-ultimate-ai-coding-combo.md) - "[0:09:50] as we start to do things like even creating documentation on the web specifically for AI to scrape. I think that's a big thing coming in the future"
