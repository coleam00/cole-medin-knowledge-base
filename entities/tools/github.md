---
type: entity
subtype: tool
title: "GitHub"
description: "The gh command-line tool that lets Claude Code manage issues and pull requests directly on a remote GitHub repository."
resource: "https://cli.github.com"
tags: [git, cli, version-control, ci-cd, infrastructure]
videos: [pydantic-ai-20-the-new-best-way-to-build-ai-agents-is-composing-capabilities, finally-an-open-standard-for-the-karpathy-llm-wiki-is-here, anthropic-just-dropped-a-masterclass-on-building-agent-harnesses-for-large-codebases, full-guide-to-becoming-a-principled-agentic-engineer-build-anything-with-ai, parallel-claude-code-git-worktrees-this-setup-will-change-how-you-ship, im-building-an-ai-dark-factory-that-ships-its-own-code-public-experiment, the-next-evolution-of-ai-coding-is-harnesses-heres-how-to-build-them, the-subagent-era-is-officially-here-learn-this-now, ive-used-claude-code-for-2000-hours-heres-how-i-build-anything-with-it, build-beautiful-diagrams-with-claude-code-full-workflow, my-complete-agentic-coding-workflow-to-build-anything-no-fluff-or-overengineering, turn-claude-code-into-your-full-engineering-team-with-subagents, the-5-techniques-separating-top-agentic-engineers-right-now, the-kiro-ai-coding-hackathon-has-officially-started-build-anything-win-big-prizes, is-gemini-3-really-the-best-ai-ever, ai-fixes-my-code-better-than-me-now-heres-how, github-is-the-future-of-ai-coding-heres-why, every-rag-strategy-explained-in-13-minutes-no-fluff, claude-code-web-just-dropped-but-i-already-built-something-better-with-codex, docker-just-made-using-mcp-servers-100x-easier-one-click-installs, turn-any-file-into-llm-knowledge-in-seconds, the-true-power-of-ai-coding-build-your-own-workflows-full-guide, i-built-my-claude-code-subagents-dream-team-to-create-any-ai-agent, introducing-archon-the-revolutionary-operating-system-for-ai-coding, a-complete-guide-to-claude-code-here-are-all-the-best-strategies, build-and-ship-any-mcp-server-in-minutes-full-guide, context-engineering-is-the-new-vibe-coding-learn-this-now, ai-code-that-fixes-itself-an-mcp-you-can-try-now, build-an-army-of-ai-agents-on-autopilot-with-archon-heres-how, code-100x-faster-with-ai-heres-how-no-hype-full-process, the-mcp-integration-everyone-is-sleeping-on-mcp-custom-ai-agents, are-you-building-real-ai-agents-or-just-using-llms, deploying-billions-of-ai-agents-is-easier-than-you-think, insane-new-strategy-for-building-ai-agent-apps, the-future-of-rag-is-agentic-learn-this-strategy-now, turn-any-website-into-llm-knowledge-in-seconds, the-glow-up-every-ai-agent-needs, pydantic-ai-deepseek-v3-the-best-ai-agent-combo, how-to-dominate-with-ai-in-2025, i-created-the-best-ai-agent-platform-in-just-2-months, our-boltnew-forks-most-requested-feature-is-finally-here, ottodev-is-becoming-the-best-open-source-ai-coding-assistant, were-taking-this-ai-coding-assistant-to-the-moon-plus-installation-instructions, ollama-openais-swarm-easily-run-ai-agents-locally, this-boltnew-fork-is-exploding-dont-miss-out-on-whats-happening, im-building-the-best-open-source-ai-coding-assistant-with-your-help, this-ai-agent-with-rag-manages-my-life, the-most-value-packed-rag-guide-on-youtube-feat-llama-31-405b, build-a-hilarious-ai-game-from-scratch-in-10-minutes, i-finally-built-an-ai-agent-to-organize-my-life-ai-agents-masterclass-4, i-made-a-custom-ai-chatbot-site-in-47-lines-of-code, the-secret-sauce-for-simple-powerful-ai-apps-ai-agents-masterclass-2, chatgpt-users-be-aware-of-this-major-weakness, use-chatgpt-in-two-clicks-on-any-website-with-a-custom-chrome-extension, chatgpt-is-the-gift-that-keeps-on-giving-introducing-auto-gpt]
created: 2026-07-21
updated: 2026-07-21
---

# GitHub

GitHub is the remote hosting platform for Git repositories that, across Cole's catalog, does double duty: it is where nearly every project he demos lives (the "link in the description" repo), and, increasingly, it is the *control surface* an agent operates through. The load-bearing piece for agentic coding is the `gh` command-line tool. As Cole puts it, "now that you have GH in your development environment, you have the GitHub CLI command. Claude Code can start using this to operate on your remote GitHub repository." Because the CLI is text-in, text-out and already authenticated, Claude Code and Codex can read issues, open pull requests, comment, and tag agents without any bespoke integration, the platform every developer already uses becomes the agent's API.

## How Cole uses it

Two roles recur. First, **GitHub as the agent's inbox and entry point.** In the harness and Dark Factory work, a GitHub issue is the unit of work: "the entry point to anything that we're going to work on in the factory is a GitHub issue," and elsewhere "the GitHub issues is actually my entry point. So I'll put my artifacts here." Labels on issues and PRs steer the pipeline, and the agent uses `gh` to view an issue, plan against it, push a branch, and open the PR, closing the loop humans review. The parallel-worktrees workflow is the same move at speed: "use the GitHub CLI to view issue one and help me make a plan for it. It is that simple."

Second, **GitHub as version control that doubles as agent memory.** Cole leans on the fact that "everyone's already using Git and GitHub for version control. And so we can take advantage of a tool that we're already using to provide long-term memory to our agent." Commit history and PRs give the agent durable, inspectable state for free. On top of that sit **GitHub Actions** for CI/CD ("It's the tooling for CI and CD built right into GitHub, which is freaking awesome") and GitHub OAuth for authenticating MCP servers and remote agent containers, where "you grab your GitHub token just going to this URL." The bulk of the remaining videos use GitHub in its plainest role: the public repo cloned to follow along, which keeps the whole teaching catalog reproducible.

## Realizes

- [The Issue Is the Spec](../../concepts/issue-is-the-spec.md) - Treating a well-written ticket or issue as the complete specification the agent implements against.
- [Git as Long-Term Memory](../../concepts/git-as-long-term-memory.md) - Treating the git history and versioned files as durable, inspectable memory for agents instead of opaque model state.
- [Agent Deployment](../../concepts/agent-deployment.md) - Getting agents to production, containerizing, networking, reverse-proxying, and choosing a provider-agnostic, cost-predictable host.
- [Agentic Workflow Engineering](../../concepts/agentic-workflow-engineering.md) - Designing repeatable AI workflows as engineered systems with defined steps, orchestration, and background execution rather than ad-hoc prompting.
- [Context Engineering](../../concepts/context-engineering.md) - The deliberate practice of curating exactly what goes into an LLM's limited context window.
- [Human in the Loop](../../concepts/human-in-the-loop.md) - Keeping a human as the approver and steerer of agentic work rather than fully automating, so AI augments engineers instead of replacing them.
- [Global Rules](../../concepts/global-rules.md) - Persistent project- or user-level rule files that inject standing context and conventions into every agent run.
- [Model Selection](../../concepts/model-selection.md) - Choosing the right LLM per task by trading off quality, speed, and cost.
- [Provider Independence](../../concepts/provider-independence.md) - Architecting agents so the underlying model, framework, or client can be swapped without a rewrite, avoiding lock-in through low-level abstractions.

## Works with

- [Git](./git.md) - Version control used as a core part of harness memory: commits and the git log let fresh sessions reconstruct progress, and enable automatic rollback.
- [Git Worktree](./git-worktree.md) - Git feature that duplicates the codebase across isolated branches so multiple coding agents can run in parallel without collisions.
- [Claude Code](./claude-code.md) - Anthropic's terminal-based agentic coding assistant, the primary agent driving `gh`.
- [Codex](./codex.md) - OpenAI's cloud-based software-engineering agent integrated with GitHub, plus a Codex CLI.
- [Archon](./archon.md) - Cole's free, open-source AI command center and harness builder for AI coding that fixes GitHub issues end to end.
- [Docker](./docker.md) - Containerization prerequisite; containers authenticated with a GitHub token pull code to build and serve agents.
- [GitHub Actions](./github-actions.md) - GitHub's built-in CI/CD system that runs trigger-based workflows to invoke coding assistants in isolated, GitHub-hosted environments.
- [GitHub Copilot](./github-copilot.md) - GitHub's AI coding agent, which recently added subagent support for research, code analysis, and code review (distinct from the gh CLI tool already covered).
- [GitHub Spec Kit](./github-spec-kit.md) - GitHub's spec-driven development toolkit, providing slash commands for vibe planning, initial requirements, and plan creation, cited alongside PRP and BMAD as another expression of the same plan-implement-validate philosophy.

## Sources

- [Pydantic AI 2.0: The New Best Way to Build AI Agents is Composing Capabilities](../../sources/pydantic-ai-20-the-new-best-way-to-build-ai-agents-is-composing-capabilities.md)
- [Finally, an Open Standard for the Karpathy LLM Wiki is HERE](../../sources/finally-an-open-standard-for-the-karpathy-llm-wiki-is-here.md)
- [Anthropic Just Dropped a Masterclass on Building Agent Harnesses (for Large Codebases)](../../sources/anthropic-just-dropped-a-masterclass-on-building-agent-harnesses-for-large-codebases.md)
- [FULL Guide to Becoming a Principled Agentic Engineer (Build Anything with AI)](../../sources/full-guide-to-becoming-a-principled-agentic-engineer-build-anything-with-ai.md) - "[0:38:34] the GitHub issues is actually my entry point. So I'll put my artifacts here."
- [Parallel Claude Code + Git Worktrees: This Setup Will Change How You Ship](../../sources/parallel-claude-code-git-worktrees-this-setup-will-change-how-you-ship.md) - "[0:07:08] use the GitHub CLI to view issue one and help me make a plan for it. It is that simple."
- [I'm Building an AI Dark Factory That Ships Its Own Code (Public Experiment)](../../sources/im-building-an-ai-dark-factory-that-ships-its-own-code-public-experiment.md) - "[0:17:16] the entry point to anything that we're going to work on in the factory is a GitHub issue"
- [The Next Evolution of AI Coding Is Harnesses - Here's How to Build Them](../../sources/the-next-evolution-of-ai-coding-is-harnesses-heres-how-to-build-them.md)
- [The Subagent Era Is Officially Here - Learn this Now](../../sources/the-subagent-era-is-officially-here-learn-this-now.md)
- [I've Used Claude Code for 2,000+ Hours - Here's How I Build Anything With It](../../sources/ive-used-claude-code-for-2000-hours-heres-how-i-build-anything-with-it.md) - "[0:05:49] everyone's already using Git and GitHub for version control. And so we can take advantage of a tool that we're already using to provide long-term memory to our agent."
- [Build BEAUTIFUL Diagrams with Claude Code (Full Workflow)](../../sources/build-beautiful-diagrams-with-claude-code-full-workflow.md)
- [My COMPLETE Agentic Coding Workflow to Build Anything (No Fluff or Overengineering)](../../sources/my-complete-agentic-coding-workflow-to-build-anything-no-fluff-or-overengineering.md)
- [Turn Claude Code into Your Full Engineering Team with Subagents](../../sources/turn-claude-code-into-your-full-engineering-team-with-subagents.md)
- [The 5 Techniques Separating Top Agentic Engineers Right Now](../../sources/the-5-techniques-separating-top-agentic-engineers-right-now.md)
- [The Kiro AI Coding Hackathon has Officially Started! Build ANYTHING, Win Big Prizes.](../../sources/the-kiro-ai-coding-hackathon-has-officially-started-build-anything-win-big-prizes.md)
- [Is Gemini 3 Really the Best AI Ever?](../../sources/is-gemini-3-really-the-best-ai-ever.md) - "[0:08:13] that's exactly what we have with open source repos, especially with something like GitHub."
- [AI Fixes My Code Better than Me Now?! (Here's How)](../../sources/ai-fixes-my-code-better-than-me-now-heres-how.md) - "[0:05:11] even using tools like the GitHub CLI to actually create issues in pull requests and tag the agent"
- [GitHub is the Future of AI Coding (Here's Why)](../../sources/github-is-the-future-of-ai-coding-heres-why.md) - "[0:02:06] for all of these coding assistant integrations, I'm using GitHub actions. It's the tooling for CI and CD built right into GitHub, which is freaking awesome."
- [Every RAG Strategy Explained in 13 Minutes (No Fluff)](../../sources/every-rag-strategy-explained-in-13-minutes-no-fluff.md)
- [Claude Code Web JUST Dropped but I Already Built Something BETTER (with Codex!)](../../sources/claude-code-web-just-dropped-but-i-already-built-something-better-with-codex.md) - "[0:04:35] using the GitHub CLI to perform all these actions for me. So, I have the authentication set up in the container."
- [Docker Just Made Using MCP Servers 100x Easier (One Click Installs!)](../../sources/docker-just-made-using-mcp-servers-100x-easier-one-click-installs.md)
- [Turn ANY File into LLM Knowledge in SECONDS](../../sources/turn-any-file-into-llm-knowledge-in-seconds.md)
- [The True Power of AI Coding - Build Your OWN Workflows (Full Guide)](../../sources/the-true-power-of-ai-coding-build-your-own-workflows-full-guide.md)
- [I Built My Claude Code Subagents DREAM TEAM to Create Any AI Agent](../../sources/i-built-my-claude-code-subagents-dream-team-to-create-any-ai-agent.md)
- [Introducing Archon - The Revolutionary Operating System for AI Coding](../../sources/introducing-archon-the-revolutionary-operating-system-for-ai-coding.md)
- [A Complete Guide to Claude Code - Here are ALL the Best Strategies](../../sources/a-complete-guide-to-claude-code-here-are-all-the-best-strategies.md) - "[0:33:58] now that you have GH in your development environment, you have the GitHub CLI command. Claude Code can start using this to operate on your remote GitHub repository."
- [Build and Ship Any MCP Server in MINUTES (Full Guide)](../../sources/build-and-ship-any-mcp-server-in-minutes-full-guide.md)
- [Context Engineering is the New Vibe Coding (Learn this Now)](../../sources/context-engineering-is-the-new-vibe-coding-learn-this-now.md)
- [AI Code That Fixes Itself (An MCP You Can Try Now)](../../sources/ai-code-that-fixes-itself-an-mcp-you-can-try-now.md)
- [Build an ARMY of AI Agents on Autopilot with Archon, Here's How](../../sources/build-an-army-of-ai-agents-on-autopilot-with-archon-heres-how.md)
- [Code 100x Faster with AI, Here's How (No Hype, FULL Process)](../../sources/code-100x-faster-with-ai-heres-how-no-hype-full-process.md)
- [The MCP Integration EVERYONE is Sleeping On (MCP + Custom AI Agents)](../../sources/the-mcp-integration-everyone-is-sleeping-on-mcp-custom-ai-agents.md)
- [Are You Building REAL AI Agents or Just Using LLMs?](../../sources/are-you-building-real-ai-agents-or-just-using-llms.md)
- [Deploying Billions of AI Agents is Easier than You Think](../../sources/deploying-billions-of-ai-agents-is-easier-than-you-think.md)
- [INSANE New Strategy for Building AI Agent Apps](../../sources/insane-new-strategy-for-building-ai-agent-apps.md)
- [The Future of RAG is Agentic - Learn this Strategy NOW](../../sources/the-future-of-rag-is-agentic-learn-this-strategy-now.md)
- [Turn ANY Website into LLM Knowledge in SECONDS](../../sources/turn-any-website-into-llm-knowledge-in-seconds.md)
- [The GLOW-UP Every AI Agent Needs](../../sources/the-glow-up-every-ai-agent-needs.md)
- [Pydantic AI + DeepSeek V3 - The BEST AI Agent Combo](../../sources/pydantic-ai-deepseek-v3-the-best-ai-agent-combo.md)
- [How to DOMINATE with AI in 2025](../../sources/how-to-dominate-with-ai-in-2025.md)
- [I Created the BEST AI Agent Platform in Just 2 MONTHS!](../../sources/i-created-the-best-ai-agent-platform-in-just-2-months.md)
- [Our Bolt.new Fork's Most Requested Feature is FINALLY Here](../../sources/our-boltnew-forks-most-requested-feature-is-finally-here.md)
- [oTToDev is Becoming the BEST Open Source AI Coding Assistant](../../sources/ottodev-is-becoming-the-best-open-source-ai-coding-assistant.md)
- [We're Taking this AI Coding Assistant to the MOON [Plus Installation Instructions!]](../../sources/were-taking-this-ai-coding-assistant-to-the-moon-plus-installation-instructions.md)
- [Ollama + OpenAI's Swarm - EASILY Run AI Agents Locally](../../sources/ollama-openais-swarm-easily-run-ai-agents-locally.md)
- [This Bolt.new Fork is EXPLODING - Don't Miss out on What's Happening!](../../sources/this-boltnew-fork-is-exploding-dont-miss-out-on-whats-happening.md)
- [I'm Building the BEST Open Source AI Coding Assistant with YOUR Help](../../sources/im-building-the-best-open-source-ai-coding-assistant-with-your-help.md)
- [This AI Agent with RAG Manages MY LIFE](../../sources/this-ai-agent-with-rag-manages-my-life.md)
- [The Most Value Packed RAG Guide on YouTube (Feat. Llama 3.1 405B!)](../../sources/the-most-value-packed-rag-guide-on-youtube-feat-llama-31-405b.md)
- [Build a Hilarious AI Game from SCRATCH in 10 Minutes](../../sources/build-a-hilarious-ai-game-from-scratch-in-10-minutes.md)
- [I FINALLY Built an AI Agent to Organize my Life - AI Agents Masterclass #4](../../sources/i-finally-built-an-ai-agent-to-organize-my-life-ai-agents-masterclass-4.md)
- [I Made a Custom AI Chatbot Site in 47 Lines of Code](../../sources/i-made-a-custom-ai-chatbot-site-in-47-lines-of-code.md)
- [The Secret Sauce for SIMPLE + POWERFUL AI Apps - AI Agents Masterclass #2](../../sources/the-secret-sauce-for-simple-powerful-ai-apps-ai-agents-masterclass-2.md)
- [ChatGPT Users BE AWARE of this Major Weakness](../../sources/chatgpt-users-be-aware-of-this-major-weakness.md)
- [Use ChatGPT in Two Clicks on ANY website with a Custom Chrome Extension](../../sources/use-chatgpt-in-two-clicks-on-any-website-with-a-custom-chrome-extension.md)
- [ChatGPT is the GIFT that keeps on GIVING - Introducing Auto-GPT](../../sources/chatgpt-is-the-gift-that-keeps-on-giving-introducing-auto-gpt.md)
