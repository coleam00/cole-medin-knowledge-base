---
type: concept
title: "LLM Data Privacy Tiers"
description: "The privacy ladder from closed models that may train on your data, to hosted open-model providers, to true self-hosting - and using mock data until you reach the tier your workload requires."
tags: [privacy, data-protection]
videos: [the-hard-truth-about-hosting-your-own-llms]
created: 2026-07-21
updated: 2026-07-21
---

# LLM Data Privacy Tiers

Data privacy with LLMs is not a binary of "safe" versus "leaking." It is a ladder with three rungs, and the job is to pick the lowest rung your workload can actually live on.

**Tier 1 - closed-model APIs.** You send prompts to a vendor whose terms may allow training on them. The failure mode is not interception but absorption: the risk is a provider "that's going to train the model on your data and eventually theoretically regurgitate it back out to other people" [0:07:22]. Convenient and capable, and unacceptable for genuinely confidential input.

**Tier 2 - hosted open-weight providers.** Serverless inference platforms run open models for you and generally do not train on what you send. You still hand data to a third party, but the weights are public and the terms are narrower, so as a middle rung "it's still a lot better than sending your data to a close Source model like GPT or CLA" [0:07:22]. This is where most teams sit in practice: near-frontier speed, no GPU purchase, meaningfully better data terms.

**Tier 3 - self-hosting.** The weights and the data both stay on infrastructure you control, which is the only tier that removes the third party entirely. It is also the tier that costs hardware and operational effort, which is exactly why it should be a decision, not a reflex.

The practical bridge across the tiers is mock data. Prototype on the cheap, capable rung and simply do not feed it the sensitive rows: "if you're developing a proof of concept using Gro... you might want to use mock data for things that's really really private" [0:07:38]. Synthetic or scrubbed data lets a proof of concept prove the architecture without ever putting the real records at the wrong tier, and you only pay for the higher rung once the thing is real.

## Part of

- [Local vs. Cloud Decision Framework](./local-vs-cloud-decision-framework.md) - "is the data sensitive?" is one of the four questions, and this page is the detailed answer to it.

## Contrasts with

- [Self-Hosting Cost Crossover](./self-hosting-cost-crossover.md) - the competing axis. Privacy pushes you up the ladder; cost pulls you back down until volume justifies owning hardware.

## Related

- [Local & Self-Hosted AI](./local-ai.md) - tier 3 in full, where control of the data and the weights is the whole point.
- [Local LLM Hardware Requirements](./local-llm-hardware-requirements.md) - what tier 3 actually costs in VRAM before it is an option.
- [Provider Independence](./provider-independence.md) - the strategic sibling: privacy is about who sees your data, independence is about who can cut you off.
- [Agent Security](./agent-security.md), [Securing Agent APIs](./api-security.md) - the surrounding controls; tier choice does nothing if the endpoint in front of the model is open.
- [Lethal Trifecta](./lethal-trifecta.md) - the exfiltration risk that lives inside the application even when the model host is trusted.
- [Fine-Tuning](./fine-tuning.md) - training on proprietary data raises the stakes, since the data is now baked into weights rather than passing through a prompt.

## Works with

- [Groq](../entities/organizations/groq.md), [Together AI](../entities/organizations/together-ai.md) - tier-2 hosts serving open-weight models fast without training on your traffic.
- [OpenRouter](../entities/tools/openrouter.md) - a single interface that spans tiers 1 and 2, so moving a workload up the ladder is a model-string change.
- [Ollama](../entities/tools/ollama.md) - the tier-3 serving layer on hardware you own.
- [OpenAI](../entities/organizations/openai.md), [Anthropic](../entities/organizations/anthropic.md) - the tier-1 closed providers the ladder is defined against.

## Sources

- [The HARD Truth About Hosting Your Own LLMs](../sources/the-hard-truth-about-hosting-your-own-llms.md) - "[0:07:22] it's still a lot better than sending your data to a close Source model like GPT or CLA that's going to train the model on your data and eventually theoretically regurgitate it back out to other people"
- [The HARD Truth About Hosting Your Own LLMs](../sources/the-hard-truth-about-hosting-your-own-llms.md) - "[0:07:38] if you're developing a proof of concept using Gro... you might want to use mock data for things that's really really private"
