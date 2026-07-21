---
type: entity
subtype: tool
title: "Postman"
description: "API platform (video sponsor) that became git-native, syncing collections/specs/tests as local YAML with an agent mode across the API lifecycle."
resource: "https://www.postman.com"
tags: [api, developer-tools, testing, integration]
videos: [stripes-coding-agents-ship-1300-prs-every-week-heres-how-they-do-it, the-way-we-use-ai-will-completely-change-in-2026-hot-takes]
created: 2026-07-21
updated: 2026-07-21
---

# Postman

Postman is a long-running API development platform, and in Cole's coverage it appears as a sponsor whose recent overhaul repositions it for the agentic era: an "AI native API platform." The change he keeps pointing at is that Postman went git-native, "the new Postman solves this because it's now git native, which is very powerful." Instead of collections, specs, and tests living only in Postman's cloud, they sync as local YAML files that sit in the repo next to the code, which makes the API surface something an agent can read, diff, and edit through ordinary [code execution](../../concepts/code-execution.md) rather than a proprietary UI.

## How Cole uses it

Cole frames Postman around two shifts. First, **git-native APIs as agent-friendly context.** Because collections and specs are now files under version control, they fold naturally into an agentic-coding loop, the same [PIV loop](../../concepts/the-piv-loop.md) and [parallel agentic coding](../../concepts/parallel-agentic-coding.md) he uses for application code now extends to the API layer, with the human reviewing changes at the [human-in-the-loop](../../concepts/human-in-the-loop.md) gate. He ties this to a real trend: "57% of organizations say that AI has increased the number of APIs that they manage," so tools that let agents help manage that sprawl matter more.

Second, **Postman as a place to build and host agents, not just test APIs.** He highlights that "they are now helping you build APIs for your AI agents" and that the platform ships an agent builder: "They have an AI agent builder ... here we can build productionready AI agents sitting behind the Postman API infrastructure." The pitch is an end-to-end API lifecycle, design, spec, test, and now an agent mode across it, with production agents running on the same API plumbing teams already trust. Cole's angle is characteristically pragmatic: whichever model you choose ([model selection](../../concepts/model-selection.md) is orthogonal), a git-native, agent-aware API tool removes friction that used to keep the API layer walled off from the coding agent.

## Related

- [Parallel Agentic Coding](../../concepts/parallel-agentic-coding.md) - git-native specs join the agentic coding loop
- [The PIV Loop](../../concepts/the-piv-loop.md) - plan/implement/validate extended to the API layer
- [Code Execution](../../concepts/code-execution.md) - specs and tests as editable local files
- [Human in the Loop](../../concepts/human-in-the-loop.md) - reviewing agent-authored API changes
- [Model Selection](../../concepts/model-selection.md)
- [Progressive Disclosure](../../concepts/progressive-disclosure.md)
- [GitHub](./github.md) - the version-control substrate a git-native Postman rides on

## Sources

- [Stripe's Coding Agents Ship 1,300 PRs EVERY Week - Here's How They Do It](../../sources/stripes-coding-agents-ship-1300-prs-every-week-heres-how-they-do-it.md) - "[0:09:32] the new Postman solves this because it's now git native, which is very powerful."
- [The Way We Use AI Will Completely Change in 2026 (Hot Takes)](../../sources/the-way-we-use-ai-will-completely-change-in-2026-hot-takes.md) - "[0:07:09] They have an AI agent builder ... here we can build productionready AI agents sitting behind the Postman API infrastructure."
