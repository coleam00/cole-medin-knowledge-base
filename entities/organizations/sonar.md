---
type: entity
subtype: organization
title: "Sonar"
description: "Code-quality and security company behind SonarQube; promotes an agent-centric development lifecycle (guide, verify, solve) and hosts Sonar Summit, where Cole gives a fireside chat on self-validation and guardrails."
resource: "https://www.sonarsource.com"
tags: [organization, code-quality, security, sponsor, validation]
videos: [the-best-ai-coding-setup-isnt-the-most-autonomous-one-heres-why, claude-plans-gemini-designs-the-workflow-to-build-beautiful-frontends, claude-codes-agent-teams-are-insane-multiple-ai-agents-coding-together-in-real-time]
created: 2026-07-21
updated: 2026-07-21
---

# Sonar

Sonar (SonarSource, maker of SonarQube) is a code-quality and security company that Cole frames as a natural fit for the way he already thinks about AI coding: "this is all very in line with Sonar's agent centric development life cycle. A framework that's based on the three pillars of guide, verify, and solve" ([0:10:33]). Those three pillars map cleanly onto Cole's own emphasis on [Planning with AI](../../concepts/planning-with-ai.md) (guide), [Validation](../../concepts/validation.md) (verify), and agent execution (solve), which is why he presents Sonar as reinforcing rather than competing with his workflow.

The product Cole highlights is SonarQube Advanced Security, positioned as a safety gate rather than a passive linter: "that is what SonarQube's advanced security gives us. You can think of it like a circuit breaker" ([0:07:53]). It consolidates several checks into one place: "We have unified SCA, SAST, and secrets detection all in one platform" ([0:08:09]). In Cole's mental model this is the deterministic [Guardrails](../../concepts/guardrails.md) and [End-to-End Validation](../../concepts/end-to-end-validation.md) layer that lets an agent run without being fully autonomous, keeping a [Human in the Loop](../../concepts/human-in-the-loop.md) review cheap.

Sonar is also an event host and sponsor. Cole took part in its first global virtual conference: "It is the Sonar Summit, which is Sonar's first ever global virtual event. And I'm doing a fireside chat on building self-validation and guardrails into AI coding systems" ([0:08:15]). The talk topic, self-validation and guardrails, is the same thread that runs through his coverage of the company.

## Realizes

- [Validation](../../concepts/validation.md) - Building explicit checks into agentic workflows so the AI verifies its own output against real success criteria before moving on.
- [Guardrails](../../concepts/guardrails.md) - Constraints and checks that keep agents from hallucinating, going off the rails, or emitting unsafe output.
- [End-to-End Validation](../../concepts/end-to-end-validation.md) - Validating the whole system through its real interface (not just unit-level checks) so the agent proves the feature actually works.

## Related

- [Planning with AI](../../concepts/planning-with-ai.md) - Using the AI to produce a detailed plan before implementation so execution follows a reviewed blueprint instead of improvising.
- [Human in the Loop](../../concepts/human-in-the-loop.md) - Keeping a human as the approver and steerer of agentic work rather than fully automating, so AI augments engineers instead of replacing them.
- [Agentic Workflow Engineering](../../concepts/agentic-workflow-engineering.md) - Designing repeatable AI workflows as engineered systems with defined steps, orchestration, and background execution rather than ad-hoc prompting.
- [Context Isolation](../../concepts/context-isolation.md) - Giving each agent or subagent its own clean context window so unrelated tokens never dilute the task at hand.
- [Skills](../../concepts/skills.md) - Reusable, model-invoked capability packages that load specialized instructions and tools on demand to extend an agent.
- [Cole Medin](../people/cole-medin.md) - AI engineer and educator whose YouTube channel and Dynamous community teach agentic coding; creator of Archon and the source of this entire knowledge base.

## Sources

- [The Best AI Coding Setup Isn't the Most Autonomous One (Here's Why)](../../sources/the-best-ai-coding-setup-isnt-the-most-autonomous-one-heres-why.md) - "[0:10:33] this is all very in line with Sonar's agent centric development life cycle. A framework that's based on the three pillars of guide, verify, and solve."
- [Claude Plans, Gemini Designs: The Workflow to Build BEAUTIFUL Frontends](../../sources/claude-plans-gemini-designs-the-workflow-to-build-beautiful-frontends.md) - "[0:07:53] that is what SonarQube's advanced security gives us. You can think of it like a circuit breaker."
- [Claude Code's Agent Teams Are Insane - Multiple AI Agents Coding Together in Real Time](../../sources/claude-codes-agent-teams-are-insane-multiple-ai-agents-coding-together-in-real-time.md) - "[0:08:15] It is the Sonar Summit, which is Sonar's first ever global virtual event. And I'm doing a fireside chat on building self-validation and guardrails into AI coding systems."
