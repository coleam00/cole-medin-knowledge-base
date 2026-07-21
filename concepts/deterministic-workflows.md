---
type: concept
title: "Deterministic Workflows"
description: "Encoding known steps as fixed code paths and reserving the LLM for the genuinely fuzzy decisions, trading autonomy for reliability."
tags: [determinism, reliability, workflows, agentic-coding]
videos: [the-best-ai-coding-setup-isnt-the-most-autonomous-one-heres-why, the-creators-of-claude-code-and-openclaw-dont-prompt-their-agents-anymore, im-building-an-ai-dark-factory-that-ships-its-own-code-public-experiment, the-next-evolution-of-ai-coding-is-harnesses-heres-how-to-build-them, stripes-coding-agents-ship-1300-prs-every-week-heres-how-they-do-it, build-beautiful-diagrams-with-claude-code-full-workflow, your-ai-coding-workflow-needs-this-new-agent-browser-cli, github-is-the-future-of-ai-coding-heres-why, my-top-20-lessons-from-building-100s-of-ai-agents-super-actionable, give-me-28-minutes-and-ill-completely-change-the-way-you-build-ai-agents, 10x-your-ai-agents-with-this-one-agent-architecture, are-you-building-real-ai-agents-or-just-using-llms, this-is-hands-down-the-best-way-to-build-ai-agents]
created: 2026-07-21
updated: 2026-07-21
---

# Deterministic Workflows

A deterministic workflow encodes the steps you already know how to do as fixed code, spending the LLM's reasoning only where the problem is genuinely fuzzy. Cole's definition is precise: "if we give the same input, we're always going to get the same output. That's what I mean by a deterministic workflow," in contrast to an agent where "we aren't guaranteed to always get the same output out because the agent is giving that ability to reason." The governing principle is to withhold decisions from the model: "We want to actually take the decision away from the coding agent as much as we can only applying the reasoning of the LLM when we actually need it to write the code."

The motivation is reliability. Fixed steps guarantee that things you cannot afford to skip actually happen: "sometimes we want to enforce certain things to happen, like context creation or validation, that we don't want to leave up to the coding agent cuz it might forget to do so." Tests are the canonical example, "we don't want to rely on the coding agent to remember to do the tests all the time," and so is the test itself: "We might want our agent to write the code but not actually decide the test to run because we know what it looks like for our test to pass." Cheap, well-understood operations like "formatting code, running a linter, triggering a deployment" belong in code, not in a prompt.

This yields a hybrid architecture where "the system is controlling the agent," not the reverse: "We have these guarantees and we force the agent to retry whenever there are any issues." Cole notes the compounding effect: "putting LLMs in contained boxes like having separate nodes for the agents separate for deterministic steps it compounds into systemwide reliability upside." The judgment call is where to draw the line, when the path is linear and known, "it is better that we make it sequential and just make it a regular workflow," but when a step needs iteration or open-ended reasoning, that is exactly where the non-deterministic agent earns its place.

## Contrasts with

- [Agents vs. Workflows](./agents-vs-workflows.md) - agents choose steps at runtime; deterministic workflows fix them in advance.
- [The Agent Loop (Reason-Act-Observe)](./agent-loop.md) - the non-deterministic reasoning cycle deterministic code replaces where possible.

## Part of

- [Agentic Workflow Engineering](./agentic-workflow-engineering.md) - deterministic steps are the reliable backbone of engineered workflows.
- [AI Coding Harness](./ai-coding-harness.md) - the harness enforces the fixed steps around the agent.

## Related

- [Agent Graphs](./agent-graphs.md) - nodes can be deterministic code or LLM calls, mixed in one graph.
- [Validation](./validation.md) and [Guardrails](./guardrails.md) - checks best enforced deterministically, not left to the agent.
- [Subagents Pattern](./subagents-pattern.md) and [Tool Design](./tool-design.md) - business logic wrapped as deterministic tools the agent invokes.
- [Human in the Loop](./human-in-the-loop.md) - determinism reduces where a human must intervene.
- [Dark Factory](./dark-factory.md) - a self-shipping system built from mixed deterministic and agentic steps.
- [Agentic Coding](./agentic-coding.md) - deterministic scaffolding around the parts the agent still writes.
- [Compounding Error Rates](./compounding-error-rates.md) - Because agentic systems chain many steps that must each succeed, per-step error rates multiply, so a chain of 95%-reliable steps collapses to low end-to-end reliability.

## Tools

- [Archon](../entities/tools/archon.md) - workflows mix deterministic and agentic nodes in one pipeline.
- [Roast](../entities/tools/roast.md) - Shopify's open-source structured AI workflow engine that combines deterministic and agentic nodes, Cole's recommended starting point for building your own harness.
- [Claude Code](../entities/tools/claude-code.md) - the coding agent invoked only for the fuzzy steps.
- [GitHub](../entities/tools/github.md) - GitHub Action YAML fixes the process; the agent only does the code changes.
- [GitHub Actions](../entities/tools/github-actions.md) - GitHub's built-in CI/CD system that runs trigger-based workflows to invoke coding assistants in isolated, GitHub-hosted environments.

## Sources

- [My Top 20 Lessons from Building 100s of AI Agents](../sources/my-top-20-lessons-from-building-100s-of-ai-agents-super-actionable.md) - "[0:07:31] if we give the same input, we're always going to get the same output. That's what I mean by a deterministic workflow."
- [The Creators of Claude Code and OpenClaw don't Prompt Their Agents Anymore?!](../sources/the-creators-of-claude-code-and-openclaw-dont-prompt-their-agents-anymore.md) - "[0:10:11] We want to actually take the decision away from the coding agent as much as we can only applying the reasoning of the LLM when we actually need it to write the code."
- [The Next Evolution of AI Coding Is Harnesses](../sources/the-next-evolution-of-ai-coding-is-harnesses-heres-how-to-build-them.md) - "[0:01:42] sometimes we want to enforce certain things to happen, like context creation or validation, that we don't want to leave up to the coding agent cuz it might forget to do so."
- [The Best AI Coding Setup Isn't the Most Autonomous One](../sources/the-best-ai-coding-setup-isnt-the-most-autonomous-one-heres-why.md) - "[0:20:01] you can make it more reliable by having some things that are handled deterministically just with code like formatting code, running a llinter, triggering a deployment."
- [Stripe's Coding Agents Ship 1,300 PRs EVERY Week](../sources/stripes-coding-agents-ship-1300-prs-every-week-heres-how-they-do-it.md) - "[0:14:02] putting LLMs in contained boxes like having separate nodes for the agents separate for deterministic steps it compounds into systemwide reliability upside."
- [Are You Building REAL AI Agents or Just Using LLMs?](../sources/are-you-building-real-ai-agents-or-just-using-llms.md) - "[0:08:35] we don't really want to give the agent the option to control the workflow here so it is better that we make it sequential and just make it a regular workflow."
- [I'm Building an AI Dark Factory That Ships Its Own Code](../sources/im-building-an-ai-dark-factory-that-ships-its-own-code-public-experiment.md) - "[0:20:16] it shows the power of archon combining deterministic and non-deterministic steps to get a single larger job done."
- [GitHub is the Future of AI Coding (Here's Why)](../sources/github-is-the-future-of-ai-coding-heres-why.md) - "[0:11:11] we define the process and then the coding assistant only comes in to do the code changes and then after the code changes are done we return the control right back to our GitHub action workflow."
- [Your AI Coding Workflow NEEDS This New Agent Browser CLI](../sources/your-ai-coding-workflow-needs-this-new-agent-browser-cli.md) - "[0:06:56] Instead of allowing the agent to figure out the business logic, you create a workflow, something that is deterministic that you give as a tool for the agent to invoke."
- [Give Me 28 Minutes and I'll Completely Change the Way You Build AI Agents](../sources/give-me-28-minutes-and-ill-completely-change-the-way-you-build-ai-agents.md) - "[0:02:46] we follow a much more linear and deterministic path. We always have some input that is processed in some way in the exact same way every time."
- [10x Your AI Agents with this ONE Agent Architecture](../sources/10x-your-ai-agents-with-this-one-agent-architecture.md) - "[0:21:41] each node doesn't even have to call upon an llm you can just have deterministic code if you want and sometimes that's even better."
- [This is Hands Down the BEST Way to Build AI Agents](../sources/this-is-hands-down-the-best-way-to-build-ai-agents.md) - "[0:05:43] this whole flow is very non-deterministic it's not always the case that the researcher is going to get exactly what it needs in the first try."
- [Build BEAUTIFUL Diagrams with Claude Code (Full Workflow)](../sources/build-beautiful-diagrams-with-claude-code-full-workflow.md) - "[0:04:57] It has to decide every color, every shape, the entire layout... There's so many micro decisions going into creating just this single rather simple diagram."
