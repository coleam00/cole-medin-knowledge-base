---
type: concept
title: "Context Rot"
description: "The degradation of an agent's output quality as its context window fills with stale, irrelevant, or accumulated information over a long session."
tags: [context, context-window, agent-quality, long-sessions]
videos: [the-subagent-era-is-officially-here-learn-this-now, ive-used-claude-code-for-2000-hours-heres-how-i-build-anything-with-it, google-just-dropped-a-masterclass-on-agentic-engineering-its-so-good, are-agent-harnesses-bringing-back-vibe-coding, youre-hardly-using-what-claude-code-has-to-offer-its-insane, the-big-problem-with-mcp-servers-and-the-solution, the-creators-of-claude-code-and-openclaw-dont-prompt-their-agents-anymore, 10x-your-ai-agents-with-this-one-agent-architecture, im-addicted-to-windsurf-send-help, ai-agents-the-future-of-ai-or-a-passing-fad]
created: 2026-07-21
updated: 2026-07-21
---

# Context Rot

Context rot is the decline in an agent's output quality as its window fills with accumulated, stale, or irrelevant information. The core intuition is human: "the simple idea behind context rot is large language models get overwhelmed with information just like people do." It is not a hard cliff at the token limit but a gradual slide: "The larger our window gets, the more the large language model has a hard time pulling out exactly what we need for the current turn with our coding agent. This is the idea of context rot." Crucially, having a large window does not license filling it: "Just because your Claude Code, codex, whatever can support 1 million tokens doesn't mean you should overload it with that much information. We see a general decline no matter the large language model as we load it with more context."

Cole calls it the number-one failure cause in agentic coding: "about 80% of the time when your coding agent messes up in your codebase, it's because you aren't managing your context well enough" and elsewhere "context rot is the biggest problem with AI coding assistants right now." Symptoms are concrete: hallucinations climbing as the session grows, and the classic "needle in the haystack problem where the piece of the prompt that you need the AI to pay attention to... is so lost in a massive prompt that it misses it." A practical warning line: "once you get to about 250 or 300,000 tokens, you will see a huge uptick in hallucinations," at which point you "do a memory compaction or write a handoff prompt and start a new session."

Rot has a named theoretical framing, "bounded attention... When we add more and more information into the context window for an LLM, it gets into the dumb zone." It is also the driver behind avoiding tool bloat and MCP overload: "It is all about token consumption and context rot... just because the LLM can fit the tokens doesn't mean it can handle it gracefully" (see [The Problems With MCP Servers](./mcp-problems.md)).

## Contrasts with

- [Context Window Limits](./context-window-limits.md) - the hard token ceiling, versus context rot's soft quality decline well before it.

## Related

- [Context Reset](./context-reset.md) - clearing the window periodically stops rot accumulating.
- [Context Isolation](./context-isolation.md) - offloading token-heavy work to isolated subagents keeps the main window clean.
- [Context Engineering](./context-engineering.md) - the overarching discipline that treats context as precious to avoid rot.
- [The Problems With MCP Servers](./mcp-problems.md) - tool/token bloat is a leading rot source.
- [Agent Teams](./agent-teams.md) and [Subagents Pattern](./subagents-pattern.md) - distribute work across windows to sidestep rot.
- [AI Coding Harness](./ai-coding-harness.md), [The Ralph Loop](./the-ralph-loop.md), [The WHISK Framework](./the-whisk-framework.md) - loop patterns built to run long without rotting.
- [What Is an AI Agent](./what-is-an-ai-agent.md) - foundational context on why windows fill.

## Tools

- [Claude Code](../entities/tools/claude-code.md) - `/context` shows current token usage; `/compact` and `/clear` fight rot.

## Sources

- [The Subagent Era Is Officially Here](../sources/the-subagent-era-is-officially-here-learn-this-now.md) - "[0:02:59] the simple idea behind context rot is large language models get overwhelmed with information just like people do."
- [I've Used Claude Code for 2,000+ Hours](../sources/ive-used-claude-code-for-2000-hours-heres-how-i-build-anything-with-it.md) - "[0:04:16] The larger our window gets, the more the large language model has a hard time pulling out exactly what we need for the current turn. This is the idea of context rot."
- [You're Hardly Using What Claude Code Has to Offer](../sources/youre-hardly-using-what-claude-code-has-to-offer-its-insane.md) - "[0:01:49] once you get to about 250 or 300,000 tokens, you will see a huge uptick in hallucinations."
- [Google Just Dropped a Masterclass on Agentic Engineering](../sources/google-just-dropped-a-masterclass-on-agentic-engineering-its-so-good.md) - "[0:15:33] We don't want to fill the window of our LLM, our coding agent, too much because LLMs get overwhelmed with information just like people do."
- [Are Agent Harnesses Bringing Back Vibe Coding?](../sources/are-agent-harnesses-bringing-back-vibe-coding.md) - "[0:19:21] the first big problem that we have is bounded attention. This is the idea of context rot. When we add more and more information into the context window for an LLM, it gets into the dumb zone."
- [The BIG Problem with MCP Servers (and the Solution!)](../sources/the-big-problem-with-mcp-servers-and-the-solution.md) - "[0:01:55] just because the LLM can fit the tokens doesn't mean it can handle it gracefully."
- [The Creators of Claude Code and OpenClaw don't Prompt Their Agents Anymore?!](../sources/the-creators-of-claude-code-and-openclaw-dont-prompt-their-agents-anymore.md) - "[0:07:53] if you loop for a while, you're going to completely bloat your context for your LLM and overwhelm it."
- [10x Your AI Agents with this ONE Agent Architecture](../sources/10x-your-ai-agents-with-this-one-agent-architecture.md) - "[0:00:23] as you continue to add more instructions and tools it starts to hallucinate even with the things that it was doing well with at first."
- [I'm Addicted to Windsurf, Send Help](../sources/im-addicted-to-windsurf-send-help.md) - "[0:08:25] large language models can get very very confused when conversations start to get long... it starts to hallucinate a bunch."
- [AI Agents: The Future of AI or a Passing Fad?](../sources/ai-agents-the-future-of-ai-or-a-passing-fad.md) - "[0:03:45] the bigger your prompt the more likely you are to experience the needle in the haystack problem."
