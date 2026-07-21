---
type: concept
title: "Human in the Loop"
description: "Keeping a human as the approver and steerer of agentic work rather than fully automating, so AI augments engineers instead of replacing them."
tags: [approval, oversight, augmentation]
videos: [this-completely-changes-the-way-we-build-production-ai-agents-vercel-eve, the-best-ai-coding-setup-isnt-the-most-autonomous-one-heres-why, google-just-dropped-a-masterclass-on-agentic-engineering-its-so-good, the-creators-of-claude-code-and-openclaw-dont-prompt-their-agents-anymore, full-guide-to-becoming-a-principled-agentic-engineer-build-anything-with-ai, pi-coding-agent-archon-build-any-ai-coding-workflow-no-claude-code-bloat, im-building-an-ai-dark-factory-that-ships-its-own-code-public-experiment, the-next-evolution-of-ai-coding-is-harnesses-heres-how-to-build-them, stripes-coding-agents-ship-1300-prs-every-week-heres-how-they-do-it, ralph-wiggum-is-the-final-evolution-of-vibe-coding-heres-what-comes-next, build-a-rag-ai-agent-with-real-time-source-validation-copilotkit-pydantic-ai, are-agent-harnesses-bringing-back-vibe-coding, my-complete-agentic-coding-workflow-to-build-anything-no-fluff-or-overengineering, why-is-everyone-missing-this-with-ai-agents-memory-tools-that-scale, give-me-28-minutes-and-ill-completely-change-the-way-you-build-ai-agents, 10x-your-ai-agents-with-this-one-agent-architecture, openais-brand-new-agents-sdk-crash-course, this-is-hands-down-the-best-way-to-build-ai-agents, google-anthropic-and-openais-guides-to-ai-agents-all-in-18-minutes, the-true-power-of-ai-coding-build-your-own-workflows-full-guide, ag-ui-just-released-the-new-wave-of-ai-agent-apps]
created: 2026-07-21
updated: 2026-07-21
---

# Human in the Loop

Human in the loop keeps a person as the approver and steerer of agentic work, pausing at risky moments so AI augments the engineer rather than running wild. The plainest statement of the pattern: "then we have human in the loop. So, pausing at risky steps for approval. So, that way we can have our agent do real things, but not just have that risk of it running wild." [0:04:11] The reason it is nearly universal is that "llms hallucinate all the time and so practically any AI agent you would ever want to make you want some sort of human [approval] involved to approve certain actions." [0:20:32]

Mechanically, this is an **interrupt**: the workflow suspends and waits. In LangGraph "we use this concept... called an interrupt that's essentially their way to do human in the loop" [0:39:41]; Archon builds it into "any individual node in the workflow. So we can always have it pause for us to validate something before it continues." [0:14:34] The approval surface can be Slack buttons [0:14:47], accept/reject diffs in an editor via ACP [0:00:33], or a quick multiple-choice Q&A that lets you "just click through things really quickly." [0:13:29]

The strongest argument is against removing it. On long autonomous runs, "not having human in the loop... is pretty scary and dangerous because a lot of times you have to do course correction" [0:12:31], and letting an agent "go go and then you have it run for a day and by the time it comes back you just have crap." [0:14:47] Even Stripe, shipping 1,300 PRs a week, insists "we are never vibe coding... They are always doing human review at the end of every stripe run" [0:12:46], because "humans review the code still, but they don't write a single line of it." [0:00:15]

It is also what separates disciplined agentic engineering from vibe coding: "you definitely fall more into vibe coding if you're not reviewing the output yourself." [0:13:08] Cole's own bar for production is uncompromising, "I still am reviewing all the code myself and then also doing manual testing." [0:56:08] The framing is augmentation, not automation: an agent that "create[s] email drafts" instead of sending them [0:09:22], where "we're the final say in whatever is created, but we're delegating the grunt work." [0:05:40] Done right, the human plus the agent beats either alone: "me plus the AI coding assistant is just way better than only me." [0:10:44]

## Part of

- [The PIV Loop](./the-piv-loop.md) - planning and validation are the human-owned bookends around agent implementation.

## Contrasts with

- [Vibe Coding](./vibe-coding.md) - accepting agent output without reviewing it, the exact posture human-in-the-loop guards against.

## Related

- [Guardrails](./guardrails.md)
- [Validation](./validation.md)
- [Code Review](./code-review.md)
- [Planning with AI](./planning-with-ai.md)
- [Agentic Coding](./agentic-coding.md)
- [AI Coding Harness](./ai-coding-harness.md)
- [Agentic Workflow Engineering](./agentic-workflow-engineering.md)
- [Deterministic Workflows](./deterministic-workflows.md)
- [Agentic Experiences](./agentic-experiences.md)
- [Agentic RAG](./agentic-rag.md)
- [Compounding Error Rates](./compounding-error-rates.md) - Because agentic systems chain many steps that must each succeed, per-step error rates multiply, so a chain of 95%-reliable steps collapses to low end-to-end reliability.
- [The Five Levels of AI Coding Autonomy](./five-levels-of-ai-coding-autonomy.md) - Dan Shapiro's framework mapping the SAE five levels of driving automation onto how much control you hand a coding agent, from 'spicy autocomplete' (level 0) to the 'dark factory' (level 5).

## Tools

- [Archon](../entities/tools/archon.md) - human-in-the-loop pauses buildable into any workflow node.
- [LangGraph](../entities/tools/langgraph.md) - the interrupt primitive for pausing a graph.
- [Claude Code](../entities/tools/claude-code.md)
- [CopilotKit](../entities/tools/copilotkit.md)
- [AG-UI](../entities/tools/ag-ui.md)
- [Pydantic AI](../entities/tools/pydantic-ai.md)
- [Slack](../entities/tools/slack.md) - approve/deny buttons as the human interface.
- [Windsurf](../entities/tools/windsurf.md) - accept/reject changes per file.
- [Pi Coding Agent](../entities/tools/pi-coding-agent.md)
- [Stripe](../entities/organizations/stripe.md) - human review at the end of every agent run at scale.
- [Gmail](../entities/tools/gmail.md) - Google's email service, the canonical per-user integration in this video: hardcoded Gmail credentials illustrate the scaling problem, and a Gmail toolkit is what the agent authorizes per user.

## Sources

- [This Completely Changes the Way We Build Production AI Agents (Vercel Eve)](../sources/this-completely-changes-the-way-we-build-production-ai-agents-vercel-eve.md) - "[0:04:11] then we have human in the loop. So, pausing at risky steps for approval... but not just have that risk of it running wild."
- [This is Hands Down the BEST Way to Build AI Agents](../sources/this-is-hands-down-the-best-way-to-build-ai-agents.md) - "[0:20:32] llms hallucinate all the time and so practically any AI agent you would ever want to make you want some sort of human [approval] involved to approve certain actions"
- [The Creators of Claude Code and OpenClaw don't Prompt Their Agents Anymore?!](../sources/the-creators-of-claude-code-and-openclaw-dont-prompt-their-agents-anymore.md) - "[0:14:34] With archon workflows, we can also build human in the loop within any individual node in the workflow. So we can always have it pause for us to validate something before it continues."
- [Stripe's Coding Agents Ship 1,300 PRs EVERY Week - Here's How They Do It](../sources/stripes-coding-agents-ship-1300-prs-every-week-heres-how-they-do-it.md) - "[0:12:46] we are never vibe coding here at Stripe, right? They are always doing human review at the end of every stripe run."
- [Ralph Wiggum is the Final Evolution of Vibe Coding (Here's What Comes Next)](../sources/ralph-wiggum-is-the-final-evolution-of-vibe-coding-heres-what-comes-next.md) - "[0:12:31] not having human in the loop, especially when you're doing very longunning tasks, is pretty scary and dangerous because a lot of times you have to do course correction."
- [Google Just Dropped a Masterclass on Agentic Engineering (It's SO Good)](../sources/google-just-dropped-a-masterclass-on-agentic-engineering-its-so-good.md) - "[0:13:08] you definitely fall more into vibe coding if you're not reviewing the output yourself."
- [FULL Guide to Becoming a Principled Agentic Engineer (Build Anything with AI)](../sources/full-guide-to-becoming-a-principled-agentic-engineer-build-anything-with-ai.md) - "[0:56:08] for any serious production coding that I'm doing, I still am reviewing all the code myself and then also doing manual testing."
- [AI Fixes My Code Better than Me Now?! (Here's How)](../sources/ai-fixes-my-code-better-than-me-now-heres-how.md) - "[0:10:44] I wouldn't ship this to production only trusting its validation... but me plus the AI coding assistant is just way better than only me"
- [10x Your AI Agents with this ONE Agent Architecture](../sources/10x-your-ai-agents-with-this-one-agent-architecture.md) - "[0:34:37] we're using this concept in LangGraph called an interrupt this is how you add human in the loop to LangGraph"
- [Give Me 28 Minutes and I'll Completely Change the Way You Build AI Agents](../sources/give-me-28-minutes-and-ill-completely-change-the-way-you-build-ai-agents.md) - "[0:08:08] This kind of interrupt that we have, it's called human in the loop... waiting for the input from the human before we continue."
- [OpenAI's BRAND NEW Agents SDK (Crash Course)](../sources/openais-brand-new-agents-sdk-crash-course.md) - "[0:29:03] another big thing that the agent SDK is missing is human in the loop... before you call a specific tool or execute a specific agent actually seek approval from the human"
- [Google, Anthropic, and OpenAI's Guides to AI Agents ALL in 18 Minutes](../sources/google-anthropic-and-openais-guides-to-ai-agents-all-in-18-minutes.md) - "[0:14:27] maintaining human oversight, things like human in the loop to make sure we are a part of the more crucial decisions that our agents are making because you don't want to trust them 100%"
- [Build a RAG AI Agent with REAL-TIME Source Validation (CopilotKit + Pydantic AI)](../sources/build-a-rag-ai-agent-with-real-time-source-validation-copilotkit-pydantic-ai.md) - "[0:09:52] we're going to generate the answer based on only the chunks that we have approved. And so that way we have human in the loop rag."
- [This New Protocol Will Change AI Coding Forever (ACP)](../sources/this-new-protocol-will-change-ai-coding-forever-acp.md) - "[0:00:33] with ACP, we get live updates in our code editor as the coding assistant is working. And we can accept and reject changes"
- [My COMPLETE Agentic Coding Workflow to Build Anything](../sources/my-complete-agentic-coding-workflow-to-build-anything-no-fluff-or-overengineering.md) - "[0:25:57] I am sandwiching the implementation with the planning and the validation that I am very much a part of"
- [The Way We Use AI Will Completely Change in 2026 (Hot Takes)](../sources/the-way-we-use-ai-will-completely-change-in-2026-hot-takes.md) - "[0:05:40] we're still in the loop. We are the final say in whatever is created, but we're delegating the grunt work, all the coding to our coding agents."
- [Pi Coding Agent + Archon: Build ANY AI Coding Workflow (No Claude Code Bloat)](../sources/pi-coding-agent-archon-build-any-ai-coding-workflow-no-claude-code-bloat.md) - "[0:10:03] It has human in the loop for the plan with planotator. So it walks you through the entire process but also keeps you in the loop."
- [I'm Building an AI Dark Factory That Ships Its Own Code (Public Experiment)](../sources/im-building-an-ai-dark-factory-that-ships-its-own-code-public-experiment.md) - "[0:05:18] you are still the bottleneck for verification before progressing."
- [AG-UI Just Released: The NEW WAVE of AI Agent Apps](../sources/ag-ui-just-released-the-new-wave-of-ai-agent-apps.md) - "[0:02:11] Especially for things like human in the loop just making sure that we are still a part of the process whatever our agent is doing."
- [Why is Everyone Missing This with AI Agents?! (Memory + Tools that Scale)](../sources/why-is-everyone-missing-this-with-ai-agents-memory-tools-that-scale.md) - "[0:14:00] when we reach the authorization node, we actually have to pause the graph entirely because we need to wait for the user to authorize the agent"
- [The True Power of AI Coding - Build Your OWN Workflows (Full Guide)](../sources/the-true-power-of-ai-coding-build-your-own-workflows-full-guide.md) - "[0:18:33] while the coding assistant is running, I will validate to make sure that it's using my MCP servers properly"
