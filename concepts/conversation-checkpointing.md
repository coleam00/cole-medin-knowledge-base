---
type: concept
title: "Reverting and Forking Conversations"
description: "Rolling a coding session back to an earlier message or forking from it to undo bad AI changes and explore alternatives."
tags: [ai-coding, workflow, checkpointing]
videos: [our-boltnew-forks-most-requested-feature-is-finally-here]
created: 2026-07-21
updated: 2026-07-21
---

# Reverting and Forking Conversations

Conversation checkpointing is the ability to treat each message in a coding session as a save point you can jump back to or branch from. Cole describes the two operations directly: "you can revert to a specific message in the conversation which is really really helpful because if it messes up and you just want to scrap what it did in the last message," and "you can Fork the chat from this message as well."

The value is recovery and exploration. When an agent produces a bad change, reverting lets you discard that turn without unwinding the whole session by hand, returning both the conversation and the code to a known-good state. Forking is the exploratory counterpart: from a single trusted checkpoint you can branch into multiple alternative directions and compare them, rather than committing to one path and losing the earlier state. Cole flags these as long-awaited essentials, "really really awesome features that we just need so so bad," reflecting how central clean rollback is to an iterative AI coding loop where the model regularly goes off course.

## Related

- [Context Reset](./context-reset.md) - reverting is a targeted reset that discards a bad turn while keeping earlier good state.
- [Human in the Loop](./human-in-the-loop.md) - checkpointing is the control surface the human uses to accept, discard, or branch the agent's work.

## Tools

- [bolt.diy](../entities/tools/bolt-diy.md) - the open-source Bolt fork that shipped per-message revert and fork.

## Sources

- [Our Bolt.new Fork's Most Requested Feature is FINALLY Here](../sources/our-boltnew-forks-most-requested-feature-is-finally-here.md) - "[0:04:01] you can revert to a specific message in the conversation which is really really helpful because if it messes up and you just want to scrap what it did in the last message."
