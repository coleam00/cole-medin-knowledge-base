---
type: concept
title: "Phases of Work"
description: "Breaking a build into ordered phases so the agent completes and validates one coherent chunk before starting the next."
tags: [phases, decomposition, planning]
videos: [claude-plans-gemini-designs-the-workflow-to-build-beautiful-frontends, full-guide-build-your-own-ai-second-brain-with-claude-code, coding-agent-reliability-explodes-when-they-argue-new-adversarial-dev-technique, this-one-command-makes-coding-agents-find-all-their-mistakes-use-it-now, my-complete-agentic-coding-workflow-to-build-anything-no-fluff-or-overengineering, turn-claude-code-into-your-full-engineering-team-with-subagents, im-addicted-to-windsurf-send-help]
created: 2026-07-21
updated: 2026-07-21
---

# Phases of Work

Phases of work is the practice of breaking a build into an ordered sequence of coherent chunks, so a coding agent completes and validates one phase before starting the next. The motivating constraint is a model's limited attention: "Large language models, even the best ones like Opus right now, get overwhelmed when you try to have them do too much at once." The remedy is focus per unit: "we're going to get the best results when every step, every coding agent session, is focused on one particular thing." It is the whole-build-scale version of the same rule that [One Feature Per Prompt](./one-feature-per-prompt.md) states at the prompt level: "it is much better to give it one request at a time otherwise it's going to confuse itself as it tries to fulfill all your requests at once."

Phases are derived from the plan and ordered for buildability. In a [PRD-First](./prd-first-development.md) workflow, "each of the phases that we have laid out in this PRD maps to everything that I've shown you... And it's put in an order where we can build them one at a time," precisely because "we don't want to have our coding agent try to build your entire second brain in one shot. That is not going to work and it's going to be really hard to stay in the driver's seat." Each phase is sized as a granular, validatable increment: "the important thing with this is that we have our phases of work... Each one of these is going to be a granular implementation one of our pivloop... we're not trying to have the coding agent ever do too much at once." Cole has the planner "pick out phases one at a time from the PRD so we have granular implementations for our PIV loops."

Phasing carries a hard gate between chunks. In an adversarial split, "both the implementator and evaluator agents are going to agree on how they're going to split the larger spec into manageable chunks through these different sprints," and only "if everything passes here, then we can move on to the next sprint." Harnesses encode the same shape: they "always start with an initializer" to set the stage, then the loop picks "the next feature, implement it, update and commit," and command-driven workflows run explicit numbered stages, "we check all the prerexs. If we are good then we go to phase one, our research phase."

## Part of

- [The PIV Loop](./the-piv-loop.md) - each phase is one plan-implement-validate cycle.
- [Agentic Workflow Engineering](./agentic-workflow-engineering.md) - phasing is a structural pattern of engineered workflows.
- [AI Coding Harness](./ai-coding-harness.md) - harnesses implement phasing as an initializer plus a per-feature loop.

## Builds on

- [PRD-First Development](./prd-first-development.md) - the PRD is what gets sharded into ordered phases.
- [Planning with AI](./planning-with-ai.md) - phasing is a product of the plan that precedes implementation.

## Related

- [One Feature Per Prompt](./one-feature-per-prompt.md) - the same "never too much at once" rule at prompt scale.
- [End-to-End Validation](./end-to-end-validation.md) and [Validation](./validation.md) - the gate that must pass before the next phase begins.
- [Context Isolation](./context-isolation.md) - each phase runs in its own focused session.
- [Commandify Everything](./commandify-everything.md) - phases are often driven by numbered slash-command workflows.
- [Contract-First](./contract-first.md), [Issue Is the Spec](./issue-is-the-spec.md), [Reduce Assumptions](./reduce-assumptions.md) - complementary disciplines for defining what each phase must deliver.

## Sources

- [Claude Plans, Gemini Designs: The Workflow to Build BEAUTIFUL Frontends](../sources/claude-plans-gemini-designs-the-workflow-to-build-beautiful-frontends.md) - "[0:05:46] Large language models, even the best ones like Opus right now, get overwhelmed when you try to have them do too much at once."
- [Claude Plans, Gemini Designs: The Workflow to Build BEAUTIFUL Frontends](../sources/claude-plans-gemini-designs-the-workflow-to-build-beautiful-frontends.md) - "[0:06:16] we're going to get the best results when every step, every coding agent session, is focused on one particular thing."
- [Full Guide - Build Your Own AI Second Brain with Claude Code](../sources/full-guide-build-your-own-ai-second-brain-with-claude-code.md) - "[0:22:54] each of the phases that we have laid out in this PRD maps to everything that I've shown you... And it's put in an order where we can build them one at a time"
- [Full Guide - Build Your Own AI Second Brain with Claude Code](../sources/full-guide-build-your-own-ai-second-brain-with-claude-code.md) - "[0:23:23] We don't want to have our coding agent try to build your entire second brain in one shot. That is not going to work and it's going to be really hard to stay in the driver's seat"
- [My COMPLETE Agentic Coding Workflow to Build Anything (No Fluff or Overengineering)](../sources/my-complete-agentic-coding-workflow-to-build-anything-no-fluff-or-overengineering.md) - "[0:15:13] the important thing with this is that we have our phases of work... Each one of these is going to be a granular implementation one of our pivloop... we're not trying to have the coding agent ever do too much at once."
- [My COMPLETE Agentic Coding Workflow to Build Anything (No Fluff or Overengineering)](../sources/my-complete-agentic-coding-workflow-to-build-anything-no-fluff-or-overengineering.md) - "[0:23:12] I want it to pick out phases one at a time from the PRD so we have granular implementations for our PIV loops"
- [Coding Agent Reliability EXPLODES When They Argue (New Adversarial Dev Technique)](../sources/coding-agent-reliability-explodes-when-they-argue-new-adversarial-dev-technique.md) - "[0:10:58] both the implementator and evaluator agents are going to agree on how they're going to split the larger spec into manageable chunks through these different sprints."
- [Coding Agent Reliability EXPLODES When They Argue (New Adversarial Dev Technique)](../sources/coding-agent-reliability-explodes-when-they-argue-new-adversarial-dev-technique.md) - "[0:11:30] If everything passes here, then we can move on to the next sprint."
- [This One Command Makes Coding Agents Find All Their Mistakes (Use it Now)](../sources/this-one-command-makes-coding-agents-find-all-their-mistakes-use-it-now.md) - "[0:04:02] we check all the prerexs. If we are good then we go to phase one, our research phase."
- [Turn Claude Code into Your Full Engineering Team with Subagents](../sources/turn-claude-code-into-your-full-engineering-team-with-subagents.md) - "[0:10:36] Most of the harnesses that I've seen over the past few months, they always start with an initializer. Because before we get into the main loop of implementing all of the features... we need to set the stage for our project."
- [I'm Addicted to Windsurf, Send Help](../sources/im-addicted-to-windsurf-send-help.md) - "[0:09:33] it is much better to give it one request at a time otherwise it's going to confuse itself as it tries to fulfill all your requests at once"
