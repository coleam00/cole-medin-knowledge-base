---
type: entity
subtype: tool
title: "Claude Code"
description: "Anthropic's terminal-based agentic coding assistant that is the subject of this complete-guide walkthrough."
resource: "https://www.anthropic.com/claude-code"
tags: [coding-agent, anthropic, terminal, primary-driver]
videos: [this-completely-changes-the-way-we-build-production-ai-agents-vercel-eve, i-turned-claude-code-into-a-complete-video-generation-system-with-archon, i-love-the-karpathy-llm-wiki-but-it-doesnt-scale-heres-what-does, google-just-dropped-a-masterclass-on-agentic-engineering-its-so-good, the-creators-of-claude-code-and-openclaw-dont-prompt-their-agents-anymore, omnigent-the-new-meta-harness-for-every-coding-agent-claude-code-codex-pi-more, googles-agents-cli-the-cli-skills-combination-to-ship-ai-agents-easily, claude-plans-gemini-designs-the-workflow-to-build-beautiful-frontends, harness-engineering-what-separates-top-agentic-engineers-right-now, anthropic-just-dropped-a-masterclass-on-building-agent-harnesses-for-large-codebases, build-render-entire-videos-with-claude-code-full-workflow, ai-youtube-is-only-claude-hype-now, full-guide-to-becoming-a-principled-agentic-engineer-build-anything-with-ai, parallel-claude-code-git-worktrees-this-setup-will-change-how-you-ship, pi-coding-agent-archon-build-any-ai-coding-workflow-no-claude-code-bloat, im-building-an-ai-dark-factory-that-ships-its-own-code-public-experiment, the-next-evolution-of-ai-coding-is-harnesses-heres-how-to-build-them, i-built-self-evolving-claude-code-memory-w-karpathys-llm-knowledge-bases, full-guide-build-your-own-ai-second-brain-with-claude-code, coding-agent-reliability-explodes-when-they-argue-new-adversarial-dev-technique, everything-you-thought-about-building-ai-agents-is-wrong, youre-hardly-using-what-claude-code-has-to-offer-its-insane, the-subagent-era-is-officially-here-learn-this-now, ive-used-claude-code-for-2000-hours-heres-how-i-build-anything-with-it, stripes-coding-agents-ship-1300-prs-every-week-heres-how-they-do-it, build-beautiful-diagrams-with-claude-code-full-workflow, this-one-command-makes-coding-agents-find-all-their-mistakes-use-it-now, my-complete-agentic-coding-workflow-to-build-anything-no-fluff-or-overengineering, why-the-best-ai-coding-tools-abandoned-rag-and-what-they-use-instead, how-to-properly-use-claude-code-agent-teams-full-live-build, i-built-a-safer-openclaw-alternative-using-claude-code, claude-codes-agent-teams-are-insane-multiple-ai-agents-coding-together-in-real-time, turn-claude-code-into-your-full-engineering-team-with-subagents, claude-skills-arent-just-for-claude-heres-how-to-build-them-for-any-agent, i-built-my-second-brain-with-claude-code-obsidian-skills-heres-how, i-was-wrong-about-ralph-wiggum, your-ai-coding-workflow-needs-this-new-agent-browser-cli, ralph-wiggum-is-the-final-evolution-of-vibe-coding-heres-what-comes-next, the-5-techniques-separating-top-agentic-engineers-right-now, ai-exploded-in-2025-heres-everything-that-happened, i-forced-claude-to-code-for-24-hours-nonstop-heres-what-happened, the-way-we-use-ai-will-completely-change-in-2026-hot-takes, is-gemini-3-really-the-best-ai-ever, ai-fixes-my-code-better-than-me-now-heres-how, github-is-the-future-of-ai-coding-heres-why, the-big-problem-with-mcp-servers-and-the-solution, the-only-ai-tech-stack-you-need-in-2026, learn-90-of-building-ai-agents-in-30-minutes, super-special-livestream-this-weekend-live-ai-agent-build, claude-code-web-just-dropped-but-i-already-built-something-better-with-codex, should-i-build-my-ai-agents-with-n8n-or-python, claude-codes-real-purpose-its-bigger-than-you-think, the-official-archon-guide-10x-your-ai-coding-workflow, docker-just-made-using-mcp-servers-100x-easier-one-click-installs, claude-sonnet-45-the-new-coding-king-sonnet-45-vs-gpt-5-codex, the-true-power-of-ai-coding-build-your-own-workflows-full-guide, the-future-of-ai-and-saas-is-agentic-experiences-heres-how-to-build-them, this-new-protocol-will-change-ai-coding-forever-acp, your-ultimate-n8n-rag-ai-agent-template-just-got-a-massive-upgrade, i-built-my-claude-code-subagents-dream-team-to-create-any-ai-agent, archon-beta-launch-livestream-what-you-missed, introducing-archon-the-revolutionary-operating-system-for-ai-coding, a-complete-guide-to-claude-code-here-are-all-the-best-strategies, build-any-ai-agent-with-this-context-engineering-blueprint, context-engineering-101-the-simple-strategy-to-100x-ai-coding, build-and-ship-any-mcp-server-in-minutes-full-guide, context-engineering-is-the-new-vibe-coding-learn-this-now, introducing-rag-20-agentic-rag-knowledge-graphs-free-template, ai-code-that-fixes-itself-an-mcp-you-can-try-now, code-100x-faster-with-ai-heres-how-no-hype-full-process, claude-computer-use-boltnew-the-ultimate-ai-coding-combo, v0-claude-a-game-changer-for-building-ai-apps]
created: 2026-07-21
updated: 2026-07-21
---

# Claude Code

Claude Code is Anthropic's terminal-based agentic coding assistant, and it is the recurring protagonist of Cole's catalog. "Claude Code was made generally available May 22nd of last year along with the release of Claude 4," he notes, and "I have used the tool for over 2,000 hours now." Elsewhere he is blunter: "I live and breathe in this terminal," calling it "the best of the best by far" and "still my primary driver."

What makes it stand apart, in Cole's telling, is how [agentic](../../concepts/agentic-coding.md) its loop is. Instead of a vector database it leans on [agentic search](../../concepts/agentic-search.md): "there is no vector database, no traditional rag, and it gives me a fantastic overview at the end." It is the surface where he practices [context engineering](../../concepts/context-engineering.md), keeps a lightweight `CLAUDE.md` as his [global rules](../../concepts/global-rules.md), and drops in [skills](../../concepts/skills.md) that "drive most of the capability." It also pioneered features other agents copied: "Claude Code was the first coding agent to introduce subagents," it added [hooks](../../concepts/claude-code-hooks.md), and Git worktrees are "supported natively." Agent teams arrived "with the release of Opus 4.6."

[Model selection](../../concepts/model-selection.md) happens inline ("just do slash model"), sub-agents can be pinned to Haiku or Sonnet, and Opus now runs with a one-million-token window. It connects to an MCP server with "a single command," and Cole leans on its [human-in-the-loop](../../concepts/human-in-the-loop.md) affordances like the ask-user-question tool plus [validation](../../concepts/validation.md) commands to catch mistakes. He also stresses it is bigger than code: "you can use Claude Code for a lot more than just coding," from second brains to YouTube scripting to diagrams and full video generation. It is the foundation the Claude Agent SDK exposes programmatically. The main critique is feature bloat: "there's so many features, bugs being introduced all the time," which is exactly what pushed some engineers toward leaner harnesses.

## Realizes

- [Agentic Coding](../../concepts/agentic-coding.md) - Letting an AI agent drive software development end-to-end, from planning through implementation and validation, with human steering.
- [Agentic Search](../../concepts/agentic-search.md) - An agent answering a question by reasoning across multiple search tools and full-document fallbacks instead of relying on a single retrieval call.
- [Context Engineering](../../concepts/context-engineering.md) - The deliberate practice of curating exactly what goes into an LLM's limited context window - system messages, schemas, chat history, and dynamic variables - to avoid overload and keep outputs sharp.
- [Skills](../../concepts/skills.md) - Reusable, model-invoked capability packages that load specialized instructions and tools on demand to extend an agent.
- [Global Rules](../../concepts/global-rules.md) - Persistent project- or user-level rule files that inject standing context and conventions into every agent run.
- [Claude Code Hooks](../../concepts/claude-code-hooks.md) - Lifecycle hooks that run deterministic code at defined points in a Claude Code session to enforce behavior the model can't be trusted to.
- [Model Selection](../../concepts/model-selection.md) - Choosing the right LLM per task by trading off quality, speed, and cost, often routing easy requests to cheap models and hard ones to expensive models.
- [Human in the Loop](../../concepts/human-in-the-loop.md) - Keeping a human as the approver and steerer of agentic work rather than fully automating, so AI augments engineers instead of replacing them.
- [Validation](../../concepts/validation.md) - Building explicit checks into agentic workflows so the AI verifies its own output against real success criteria before moving on.

## Contrasts with

- [Codex](./codex.md) - OpenAI's cloud-based software-engineering agent integrated with GitHub, plus a Codex CLI.
- [Cursor](./cursor.md) - AI coding assistant that can consume AG-UI's llms.txt docs to help build with the protocol.
- [Windsurf](./windsurf.md) - AI coding IDE Cole used to build the Python AG-UI backend and consume the protocol docs.
- [Pi](./pi-coding-agent.md) - A minimalistic, open-source coding agent cited as another example of a company-built harness around a model.
- [Gemini CLI](./gemini-cli.md) - Google's coding CLI, where subagent support is experimental and which has a direct integration with the Agent Client Protocol.

## Works with

- [Archon](./archon.md) - Cole's free, open-source AI command center and harness builder for AI coding; started as an AI agent that builds other AI agents.
- [Git Worktrees](./git-worktree.md) - Git feature that duplicates the codebase across isolated branches so multiple coding agents can run in parallel without collisions.

## Related

- [Claude](./claude.md) - Named as an example of a large language model that can be turned into an agent.
- [Claude Desktop](./claude-desktop.md) - The MCP client used to demo connecting to the server, configured via developer settings and mcp-remote pointed at the streamable HTTP endpoint.

## Sources

- [This Completely Changes the Way We Build Production AI Agents (Vercel Eve)](../../sources/this-completely-changes-the-way-we-build-production-ai-agents-vercel-eve.md)
- [I Turned Claude Code Into a Complete Video Generation System (with Archon)](../../sources/i-turned-claude-code-into-a-complete-video-generation-system-with-archon.md)
- [I Love the Karpathy LLM Wiki but it Doesn't Scale. Here's What Does.](../../sources/i-love-the-karpathy-llm-wiki-but-it-doesnt-scale-heres-what-does.md)
- [Google Just Dropped a Masterclass on Agentic Engineering (It's SO Good)](../../sources/google-just-dropped-a-masterclass-on-agentic-engineering-its-so-good.md)
- [The Creators of Claude Code and OpenClaw don't Prompt Their Agents Anymore?!](../../sources/the-creators-of-claude-code-and-openclaw-dont-prompt-their-agents-anymore.md)
- [Omnigent: The New Meta-Harness for EVERY Coding Agent - Claude Code, Codex, Pi, More](../../sources/omnigent-the-new-meta-harness-for-every-coding-agent-claude-code-codex-pi-more.md)
- [Google's Agents CLI: The CLI + Skills Combination to Ship AI Agents EASILY](../../sources/googles-agents-cli-the-cli-skills-combination-to-ship-ai-agents-easily.md)
- [Claude Plans, Gemini Designs: The Workflow to Build BEAUTIFUL Frontends](../../sources/claude-plans-gemini-designs-the-workflow-to-build-beautiful-frontends.md)
- [Harness Engineering: What Separates Top Agentic Engineers Right Now](../../sources/harness-engineering-what-separates-top-agentic-engineers-right-now.md)
- [Anthropic Just Dropped a Masterclass on Building Agent Harnesses (for Large Codebases)](../../sources/anthropic-just-dropped-a-masterclass-on-building-agent-harnesses-for-large-codebases.md)
- [Build + Render ENTIRE Videos with Claude Code (Full Workflow)](../../sources/build-render-entire-videos-with-claude-code-full-workflow.md)
- [AI YouTube Is Only Claude Hype Now](../../sources/ai-youtube-is-only-claude-hype-now.md)
- [FULL Guide to Becoming a Principled Agentic Engineer (Build Anything with AI)](../../sources/full-guide-to-becoming-a-principled-agentic-engineer-build-anything-with-ai.md) - "[0:03:15] I'm going to be using Claude Code for our event here just because that is my favorite AI coding assistant at least right now."
- [Parallel Claude Code + Git Worktrees: This Setup Will Change How You Ship](../../sources/parallel-claude-code-git-worktrees-this-setup-will-change-how-you-ship.md) - "[0:05:07] worktrees are supported natively in claude code. So I can do claude and then it's d-worktree or you can just do dashw"
- [Pi Coding Agent + Archon: Build ANY AI Coding Workflow (No Claude Code Bloat)](../../sources/pi-coding-agent-archon-build-any-ai-coding-workflow-no-claude-code-bloat.md) - "[0:02:52] Anthropic has not stopped shipping features. And so it's gotten to the point where this is what claude code looks like now. There's so many features, bugs being introduced all the time."
- [I'm Building an AI Dark Factory That Ships Its Own Code (Public Experiment)](../../sources/im-building-an-ai-dark-factory-that-ships-its-own-code-public-experiment.md)
- [The Next Evolution of AI Coding Is Harnesses - Here's How to Build Them](../../sources/the-next-evolution-of-ai-coding-is-harnesses-heres-how-to-build-them.md)
- [I Built Self-Evolving Claude Code Memory w/ Karpathy's LLM Knowledge Bases](../../sources/i-built-self-evolving-claude-code-memory-w-karpathys-llm-knowledge-bases.md)
- [Full Guide - Build Your Own AI Second Brain with Claude Code](../../sources/full-guide-build-your-own-ai-second-brain-with-claude-code.md)
- [Coding Agent Reliability EXPLODES When They Argue (New Adversarial Dev Technique)](../../sources/coding-agent-reliability-explodes-when-they-argue-new-adversarial-dev-technique.md)
- [Everything You Thought About Building AI Agents is Wrong](../../sources/everything-you-thought-about-building-ai-agents-is-wrong.md)
- [You're Hardly Using What Claude Code Has to Offer, it's Insane](../../sources/youre-hardly-using-what-claude-code-has-to-offer-its-insane.md) - "[0:00:00] Claude Code has been shipping features at a ridiculous pace recently."
- [The Subagent Era Is Officially Here - Learn this Now](../../sources/the-subagent-era-is-officially-here-learn-this-now.md) - "[0:05:32] Claude Code was the first coding agent to introduce subagents but even they have had a lot of recent changes adding support for building custom hooks per subagent."
- [I've Used Claude Code for 2,000+ Hours - Here's How I Build Anything With It](../../sources/ive-used-claude-code-for-2000-hours-heres-how-i-build-anything-with-it.md) - "[0:00:00] Claude Code was made generally available May 22nd of last year along with the release of Claude 4."
- [Stripe's Coding Agents Ship 1,300 PRs EVERY Week - Here's How They Do It](../../sources/stripes-coding-agents-ship-1300-prs-every-week-heres-how-they-do-it.md)
- [Build BEAUTIFUL Diagrams with Claude Code (Full Workflow)](../../sources/build-beautiful-diagrams-with-claude-code-full-workflow.md)
- [This One Command Makes Coding Agents Find All Their Mistakes (Use it Now)](../../sources/this-one-command-makes-coding-agents-find-all-their-mistakes-use-it-now.md)
- [My COMPLETE Agentic Coding Workflow to Build Anything (No Fluff or Overengineering)](../../sources/my-complete-agentic-coding-workflow-to-build-anything-no-fluff-or-overengineering.md)
- [Why the Best AI Coding Tools Abandoned RAG (And What They Use Instead)](../../sources/why-the-best-ai-coding-tools-abandoned-rag-and-what-they-use-instead.md) - "[0:07:19] So, the best example of this is Claude Code."
- [How to Properly Use Claude Code Agent Teams (FULL LIVE BUILD)](../../sources/how-to-properly-use-claude-code-agent-teams-full-live-build.md) - "[0:01:30] this is a feature that was just released to Claude Code uh with the release of Opus 4.6."
- [I Built a Safer OpenClaw Alternative Using Claude Code](../../sources/i-built-a-safer-openclaw-alternative-using-claude-code.md)
- [Claude Code's Agent Teams Are Insane - Multiple AI Agents Coding Together in Real Time](../../sources/claude-codes-agent-teams-are-insane-multiple-ai-agents-coding-together-in-real-time.md) - "[0:00:00] I have four instances of Claude code working at the exact same time together to perform a code review on my codebase. And this is all thanks to the new agents teams feature that Anthropic has built into Claude Code."
- [Turn Claude Code into Your Full Engineering Team with Subagents](../../sources/turn-claude-code-into-your-full-engineering-team-with-subagents.md)
- [Claude Skills Aren't Just for Claude - Here's How to Build Them for ANY Agent](../../sources/claude-skills-arent-just-for-claude-heres-how-to-build-them-for-any-agent.md)
- [I Built My Second Brain with Claude Code + Obsidian + Skills (Here's How)](../../sources/i-built-my-second-brain-with-claude-code-obsidian-skills-heres-how.md)
- [I Was Wrong About Ralph Wiggum](../../sources/i-was-wrong-about-ralph-wiggum.md)
- [Your AI Coding Workflow NEEDS This New Agent Browser CLI](../../sources/your-ai-coding-workflow-needs-this-new-agent-browser-cli.md)
- [Ralph Wiggum is the Final Evolution of Vibe Coding (Here's What Comes Next)](../../sources/ralph-wiggum-is-the-final-evolution-of-vibe-coding-heres-what-comes-next.md)
- [The 5 Techniques Separating Top Agentic Engineers Right Now](../../sources/the-5-techniques-separating-top-agentic-engineers-right-now.md)
- [AI Exploded in 2025 - Here's Everything That Happened](../../sources/ai-exploded-in-2025-heres-everything-that-happened.md)
- [I Forced Claude to Code for 24 Hours NONSTOP, Here's What Happened](../../sources/i-forced-claude-to-code-for-24-hours-nonstop-heres-what-happened.md)
- [The Way We Use AI Will Completely Change in 2026 (Hot Takes)](../../sources/the-way-we-use-ai-will-completely-change-in-2026-hot-takes.md)
- [Is Gemini 3 Really the Best AI Ever?](../../sources/is-gemini-3-really-the-best-ai-ever.md)
- [AI Fixes My Code Better than Me Now?! (Here's How)](../../sources/ai-fixes-my-code-better-than-me-now-heres-how.md)
- [GitHub is the Future of AI Coding (Here's Why)](../../sources/github-is-the-future-of-ai-coding-heres-why.md)
- [The BIG Problem with MCP Servers (and the Solution!)](../../sources/the-big-problem-with-mcp-servers-and-the-solution.md)
- [The ONLY AI Tech Stack You Need in 2026](../../sources/the-only-ai-tech-stack-you-need-in-2026.md)
- [Learn 90% of Building AI Agents in 30 Minutes](../../sources/learn-90-of-building-ai-agents-in-30-minutes.md)
- [Super Special Livestream this Weekend! (LIVE AI Agent Build)](../../sources/super-special-livestream-this-weekend-live-ai-agent-build.md)
- [Claude Code Web JUST Dropped but I Already Built Something BETTER (with Codex!)](../../sources/claude-code-web-just-dropped-but-i-already-built-something-better-with-codex.md)
- [Should I Build My AI Agents with n8n or Python?](../../sources/should-i-build-my-ai-agents-with-n8n-or-python.md)
- [Claude Code's Real Purpose (It's Bigger Than You Think)](../../sources/claude-codes-real-purpose-its-bigger-than-you-think.md) - "[0:00:00] Did you know that you can use Claude Code for a lot more than just coding?"
- [The OFFICIAL Archon Guide - 10x Your AI Coding Workflow](../../sources/the-official-archon-guide-10x-your-ai-coding-workflow.md)
- [Docker Just Made Using MCP Servers 100x Easier (One Click Installs!)](../../sources/docker-just-made-using-mcp-servers-100x-easier-one-click-installs.md)
- [Claude Sonnet 4.5 - The New Coding King? (Sonnet 4.5 vs. GPT 5 Codex)](../../sources/claude-sonnet-45-the-new-coding-king-sonnet-45-vs-gpt-5-codex.md) - "[0:00:56] we also have the official Claude Code version 2.0. So, a lot of improvements they've made with Claude Code, of course, being powered by Sonnet 4.5 by default now"
- [The True Power of AI Coding - Build Your OWN Workflows (Full Guide)](../../sources/the-true-power-of-ai-coding-build-your-own-workflows-full-guide.md)
- [The Future of AI and SaaS is Agentic Experiences (Here's How to Build Them)](../../sources/the-future-of-ai-and-saas-is-agentic-experiences-heres-how-to-build-them.md)
- [This New Protocol Will Change AI Coding Forever (ACP)](../../sources/this-new-protocol-will-change-ai-coding-forever-acp.md)
- [Your ULTIMATE n8n RAG AI Agent Template just got a Massive Upgrade](../../sources/your-ultimate-n8n-rag-ai-agent-template-just-got-a-massive-upgrade.md)
- [I Built My Claude Code Subagents DREAM TEAM to Create Any AI Agent](../../sources/i-built-my-claude-code-subagents-dream-team-to-create-any-ai-agent.md)
- [Archon Beta Launch Livestream - What You Missed!](../../sources/archon-beta-launch-livestream-what-you-missed.md)
- [Introducing Archon - The Revolutionary Operating System for AI Coding](../../sources/introducing-archon-the-revolutionary-operating-system-for-ai-coding.md)
- [A Complete Guide to Claude Code - Here are ALL the Best Strategies](../../sources/a-complete-guide-to-claude-code-here-are-all-the-best-strategies.md) - "[0:00:00] I have been addicted to Claude code the past couple of months. I live and breathe in this terminal."
- [Build ANY AI Agent with this Context Engineering Blueprint](../../sources/build-any-ai-agent-with-this-context-engineering-blueprint.md)
- [Context Engineering 101 - The Simple Strategy to 100x AI Coding](../../sources/context-engineering-101-the-simple-strategy-to-100x-ai-coding.md)
- [Build and Ship Any MCP Server in MINUTES (Full Guide)](../../sources/build-and-ship-any-mcp-server-in-minutes-full-guide.md)
- [Context Engineering is the New Vibe Coding (Learn this Now)](../../sources/context-engineering-is-the-new-vibe-coding-learn-this-now.md)
- [Introducing RAG 2.0: Agentic RAG + Knowledge Graphs (FREE Template)](../../sources/introducing-rag-20-agentic-rag-knowledge-graphs-free-template.md)
- [AI Code That Fixes Itself (An MCP You Can Try Now)](../../sources/ai-code-that-fixes-itself-an-mcp-you-can-try-now.md)
- [Code 100x Faster with AI, Here's How (No Hype, FULL Process)](../../sources/code-100x-faster-with-ai-heres-how-no-hype-full-process.md)
- [Claude Computer Use + Bolt.new - The ULTIMATE AI Coding Combo?!](../../sources/claude-computer-use-boltnew-the-ultimate-ai-coding-combo.md)
- [V0 + Claude: A GAME CHANGER for Building AI Apps](../../sources/v0-claude-a-game-changer-for-building-ai-apps.md)
