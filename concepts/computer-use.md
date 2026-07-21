---
type: concept
title: "Computer Use"
description: "Giving an agent control of a computer (mouse, keyboard, screen) so it can operate real software the way a person would."
tags: [agents, computer-use, claude, automation]
videos: [claude-computer-use-boltnew-the-ultimate-ai-coding-combo]
created: 2026-07-21
updated: 2026-07-21
---

# Computer Use

Computer use is giving an agent direct control of a computer so it can operate any software the way a person does. Cole describes Anthropic's implementation plainly: "It is a way to use Claude to control your computer and do things for you like type in your input boxes, search the web, click through different applications, and it works so so well." [0:03:43] Instead of calling a purpose-built API tool for each task, the agent takes screenshots, reasons about what is on screen, and issues mouse and keyboard actions, which lets it drive tools that have no API at all.

The significance is the generality. Most agent [tools](./tool-use.md) are narrow, one function per action, whereas a computer-use agent inherits the entire surface of the desktop as its action space. That is why Cole calls it a breakthrough: "it's a first of its kind, which is what allows us to do what I'm about to show you here." [0:03:50] The same reason-act-observe pattern of the [agent loop](./agent-loop.md) still applies; the difference is that "observe" means reading a screenshot and "act" means clicking and typing.

Because the agent can touch anything on the machine, computer use raises the stakes for oversight. Handing a model unrestricted control of your applications is powerful but risky, which is why [human-in-the-loop](./human-in-the-loop.md) supervision matters more here than in a narrowly-scoped agent, you want to watch what it clicks before it commits an irreversible action.

## Related

- [Agentic RAG](./agentic-rag.md) - an alternative way to give agents access to information without driving a UI.
- [Human in the Loop](./human-in-the-loop.md) - supervision for an agent with broad control of your machine.

## Tools

- [Claude](../entities/tools/claude.md) - Anthropic's Claude Computer Use is the first-of-its-kind implementation Cole demos.
- [Bolt.new](../entities/tools/bolt-new.md) - the AI coding tool Cole pairs with computer use in the demo.

## Sources

- [Claude Computer Use + Bolt.new - The ULTIMATE AI Coding Combo?!](../sources/claude-computer-use-boltnew-the-ultimate-ai-coding-combo.md) - "[0:03:43] It is a way to use Claude to control your computer and do things for you like type in your input boxes, search the web, click through different applications, and it works so so well"
