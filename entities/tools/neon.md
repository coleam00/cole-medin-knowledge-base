---
type: entity
subtype: tool
title: "Neon"
description: "Serverless Postgres platform Cole favors, acquired by Databricks in 2025."
resource: "https://neon.tech"
tags: [database, postgres, serverless, backend, branching]
videos: [every-rag-strategy-explained-in-13-minutes-no-fluff, the-easiest-possible-strategy-for-accurate-rag-step-by-step-guide, introducing-rag-20-agentic-rag-knowledge-graphs-free-template, your-ultimate-n8n-rag-ai-agent-template-just-got-a-massive-upgrade, the-only-ai-tech-stack-you-need-in-2026, parallel-claude-code-git-worktrees-this-setup-will-change-how-you-ship, the-creators-of-claude-code-and-openclaw-dont-prompt-their-agents-anymore, everything-you-thought-about-building-ai-agents-is-wrong, this-one-command-makes-coding-agents-find-all-their-mistakes-use-it-now, my-complete-agentic-coding-workflow-to-build-anything-no-fluff-or-overengineering, ai-exploded-in-2025-heres-everything-that-happened, i-was-wrong-about-ralph-wiggum, build-render-entire-videos-with-claude-code-full-workflow]
created: 2026-07-21
updated: 2026-07-21
---

# Neon

Neon is a serverless Postgres platform that has become Cole's go-to database, especially where scalability and speed matter: "So I'm here in my Neon dashboard, which is quickly becoming my go-to for Postgres" (every-rag-strategy, 0:03:54). It is still Postgres, so everything Cole does with pgvector carries over, "I'm using the neon platform for Postgres. Now this is a SQL database... but I can use my PG vector extensions" (introducing-rag-20, 0:01:37), but the serverless model adds autoscaling: "there definitely are some distinct advantages to using Neon over other platforms because it is serverless Postgres. And the biggest advantage to that is we have autoscaling" (the-easiest-possible-strategy, 0:16:59). He frames the tradeoff against Supabase as maturity versus scale: "I've been using Supabase for longer but experimenting with Neon more recently especially because of their scalability" (the-only-ai-tech-stack, 0:02:39). Neon was acquired by Databricks in 2025, "They also acquired Neon recently, one of my favorite database platforms" (ai-exploded-in-2025, 0:16:12).

Neon's standout feature for Cole is database branching, which pairs perfectly with git worktrees for parallel agentic coding. "I am creating a what is called a neon branch... most databases support this but neon just does this so well" (parallel-claude-code-git-worktrees, 0:18:40), and the branch is a full snapshot: "if I click into one of the branches and I look at the tables we have all of the tables and data copied over from the main production instance" (parallel-claude-code, 0:19:12). That lets each parallel agent run against its own isolated copy of production data. Because Neon is durable Postgres, Cole also uses it to persist workflow and agent state so a long run survives a machine restart: "This is my Neon database. I'm storing all of my logs and runs in Postgres so that I can resume a workflow even if my machine goes down" (the-creators-of-claude-code, 0:12:45), and for Ralph-style loops "it's storing all the information, the conversations in my neon database" (i-was-wrong-about-ralph-wiggum, 0:19:45). Credibility comes from its pedigree, "Neon literally powers Vzero and Replet... one of the co-founders of Neon, has been contributing to Postgres for over 20 years" (the-easiest-possible-strategy, 0:18:04). When scaffolding new apps he now asks agents to research and wire in Neon plus Neon auth directly (my-complete-agentic-coding-workflow, 0:06:31).

## Contrasts with

- [Supabase](./supabase.md) - A single platform providing Postgres for scalable chat memory plus the pgvector store for RAG embeddings, recommended over in-memory alternatives.
- [Postgres + pgvector](./postgres-pgvector.md) - A Postgres extension for storing vector embeddings, used within Supabase as a production-ready vector store for RAG.

## Related

- [Agentic RAG](../../concepts/agentic-rag.md) - Giving an agent retrieval as a tool so it decides when and how to search a knowledge base, picking strategies and issuing follow-up queries instead of a single static lookup.
- [Parallel Agentic Coding](../../concepts/parallel-agentic-coding.md) - Dispatching agents to background tasks in isolated git worktrees, each fed repo context and returning a reviewable PR.
- [Human in the Loop](../../concepts/human-in-the-loop.md) - Keeping a human as the approver and steerer of agentic work rather than fully automating, so AI augments engineers instead of replacing them.
- [End-to-End Validation](../../concepts/end-to-end-validation.md) - Validating the whole system through its real interface (not just unit-level checks) so the agent proves the feature actually works.
- [Vibe Coding](../../concepts/vibe-coding.md) - Building software by conversationally prompting an AI without closely reading the code, useful for prototypes but risky for production.
- [Global Rules](../../concepts/global-rules.md) - Persistent project- or user-level rule files that inject standing context and conventions into every agent run.
- [Skills](../../concepts/skills.md) - Reusable, model-invoked capability packages that load specialized instructions and tools on demand to extend an agent.

## Sources

- [Every RAG Strategy Explained in 13 Minutes (No Fluff)](../../sources/every-rag-strategy-explained-in-13-minutes-no-fluff.md) - "[0:03:54] So I'm here in my Neon dashboard, which is quickly becoming my go-to for Postgres."
- [The EASIEST Possible Strategy for Accurate RAG (Step by Step Guide)](../../sources/the-easiest-possible-strategy-for-accurate-rag-step-by-step-guide.md) - "[0:16:59] there definitely are some distinct advantages to using Neon over other platforms because it is serverless Postgres. And the biggest advantage to that is we have autoscaling"
- [Introducing RAG 2.0: Agentic RAG + Knowledge Graphs (FREE Template)](../../sources/introducing-rag-20-agentic-rag-knowledge-graphs-free-template.md) - "[0:01:37] I'm using the neon platform for Postgres. Now this is a SQL database... but I can use my PG vector extensions."
- [The ONLY AI Tech Stack You Need in 2026](../../sources/the-only-ai-tech-stack-you-need-in-2026.md) - "[0:02:39] I've been using Supabase for longer but experimenting with Neon more recently especially because of their scalability."
- [Parallel Claude Code + Git Worktrees: This Setup Will Change How You Ship](../../sources/parallel-claude-code-git-worktrees-this-setup-will-change-how-you-ship.md) - "[0:18:40] I am creating a what is called a neon branch... within neon and most databases support this but neon just does this so well."
- [The Creators of Claude Code and OpenClaw don't Prompt Their Agents Anymore?!](../../sources/the-creators-of-claude-code-and-openclaw-dont-prompt-their-agents-anymore.md) - "[0:12:45] This is my Neon database. I'm storing all of my logs and runs in Postgres so that I can resume a workflow even if my machine goes down."
- [Everything You Thought About Building AI Agents is Wrong](../../sources/everything-you-thought-about-building-ai-agents-is-wrong.md) - "[0:03:10] I love using neon for my Postgres database. I still do for a lot of my agents."
- [This One Command Makes Coding Agents Find All Their Mistakes (Use it Now)](../../sources/this-one-command-makes-coding-agents-find-all-their-mistakes-use-it-now.md) - "[0:15:20] one thing that I like doing with Neon is creating a branch... it'll essentially take a snapshot of our current data and then give us this secondary database."
- [My COMPLETE Agentic Coding Workflow to Build Anything (No Fluff or Overengineering)](../../sources/my-complete-agentic-coding-workflow-to-build-anything-no-fluff-or-overengineering.md) - "[0:06:31] I'd like to use Neon for my database and Neon authentication. So definitely spin up a subagent to do some research for that."
- [AI Exploded in 2025 - Here's Everything That Happened](../../sources/ai-exploded-in-2025-heres-everything-that-happened.md) - "[0:16:12] They also acquired Neon recently, one of my favorite database platforms"
