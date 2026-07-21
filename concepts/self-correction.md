---
type: concept
title: "Self-Correcting Agents"
description: "Feeding tool errors and results back to the model so it can reason about mistakes, avoid repeating calls, and retry until it gets the action right."
tags: [error-handling, retry, reflection, loop-prevention, ai-coding, validation, self-correction, workflow]
videos: [ai-code-that-fixes-itself-an-mcp-you-can-try-now, build-a-full-stack-app-for-your-n8n-ai-agent-in-20-minutes, dont-sleep-on-the-ultimate-ai-agent-combo-n8n-langchain-python, openais-o1-is-barely-usable-but-i-fixed-it, prompt-engineering-is-a-bunch-of-bs-heres-the-5-of-it-to-learn]
created: 2026-07-21
updated: 2026-07-21
---

# Self-Correcting Agents

Self-correction is the pattern of feeding an agent the consequences of its own actions, especially errors, back into its context so it can reason about what went wrong and try again. The mechanism is deliberately simple: catch the failure, describe it, and return it to the model. As Cole puts it, "if there's any error at all we'll just catch it and then return back to the agent telling it that there was an error with this specific function here's what the error was so that it can try to correct itself and maybe call the tool again" [0:12:45]. The same discipline applies when a tool call is malformed: "if we fail to invoke the tool for whatever reason like maybe the arguments were invalid then we're going to add a thought to the llm and basically tell it that you tried to invoke this tool but you failed to do so and here is why" [0:13:13].

This turns a one-shot generation into an iterative loop that converges. A capable model handles it well: after Claude emitted a known hallucination (`streamlit has no attribute experimental_rerun`), "it corrected itself first try for the experimental reruns ... when you have a model as powerful as Claude it does a really good job correcting itself and not getting into an infinite Loop of hallucination" [0:19:00]. The failure mode this guards against is exactly that infinite loop, where a weaker model keeps repeating a bad call. Even reasoning models are prone to it: "even o1 likes to do... sometimes it'll hallucinate and try to make the tool call a second time when it's already made the tool call and it should be just giving its final response" [0:14:24].

Self-correction gets much stronger when the feedback signal is grounded in ground truth rather than the model's own judgment. A hallucination detector backed by a knowledge graph lets the agent "generate a script, run it against the hallucination detector, find any mistakes that it made based on our knowledge graph, and then self-correct" [0:04:44], and can be wired in continuously so the agent "explore[s] this knowledge graph as it is generating code so that it can self-correct when it makes these little mistakes that usually get it caught in these infinite loops" [0:06:17]. This is also framed as reflection, "an AI being able to improve its own response" [0:01:58], one of the highest-leverage prompting behaviors.

## Builds on

- [The Agent Loop (Reason-Act-Observe)](./agent-loop.md) - self-correction is what happens in the observe-then-reason step when an action fails.
- [Tool Calling](./tool-use.md) - the errors most worth returning are failed or malformed tool invocations.

## Contrasts with

- [Sycophancy](./sycophancy.md) - self-correction depends on an honest error signal; a model that flatters or agrees away its mistakes never corrects them, which is why grounded external validation beats self-judgment.

## Related

- [End-to-End Validation](./end-to-end-validation.md) - running the code and returning the real result is the strongest correction signal.
- [Validation](./validation.md) - the general practice of checking output before trusting it.
- [Visual Self-Validation Loop](./visual-self-validation.md) - Giving an agent the ability to render its own visual output to an image, look at the screenshot, spot imperfections, and edit the source in place over several iterations.
- [Guardrails](./guardrails.md) - bounding retries and catching bad output so the loop stays safe.
- [Reduce Assumptions](./reduce-assumptions.md) - grounding the retry in real errors instead of guesses.
- [Agent Prompting Techniques](./agent-prompting.md) and [Prompt Engineering](./prompt-engineering.md) - how the error is phrased back to the model shapes whether it corrects.
- [Self-Criticism Prompting](./self-criticism-prompting.md) - prompting the model to critique its own draft, a lighter-weight form of reflection.
- [Webhook Tool Pattern](./webhook-tool-pattern.md) - a tool-call surface where caught errors feed the loop.
- [Vibe Coding](./vibe-coding.md) - where fast, error-driven retry loops are common.
- [Agent Observability](./agent-observability.md) - seeing the errors an agent hits is a prerequisite to correcting on them.
- [Hallucination Detection](./hallucination-detection.md) - Deterministically checking AI-generated code against a ground-truth structure (a parsed knowledge graph of the library) to flag methods and parameters that don't actually exist, then feeding the report back so the agent can fix them.

## Sources

- [AI Code That Fixes Itself (An MCP You Can Try Now)](../sources/ai-code-that-fixes-itself-an-mcp-you-can-try-now.md) - "It can generate a script, run it against the hallucination detector, find any mistakes that it made based on our knowledge graph, and then self-correct. That is the power that we have now." [0:04:44]
- [OpenAI's o1 is Barely Usable, but I Fixed it...](../sources/openais-o1-is-barely-usable-but-i-fixed-it.md) - "if we fail to invoke the tool for whatever reason like maybe the arguments were invalid then we're going to add a thought to the llm and basically tell it that you tried to invoke this tool but you failed to do so and here is why" [0:13:13]
- [Don't Sleep on the ULTIMATE AI Agent Combo (n8n, LangChain, Python)](../sources/dont-sleep-on-the-ultimate-ai-agent-combo-n8n-langchain-python.md) - "if there's any error at all we'll just catch it and then return back to the agent telling it that there was an error with this specific function here's what the error was so that it can try to correct itself and maybe call the tool again" [0:12:45]
- [Build a FULL Stack App for your n8n AI Agent in 20 Minutes](../sources/build-a-full-stack-app-for-your-n8n-ai-agent-in-20-minutes.md) - "it corrected itself first try for the experimental reruns ... when you have a model as powerful as Claude it does a really good job correcting itself and not getting into an infinite Loop of hallucination" [0:19:00]
- ["Prompt Engineering" is a Bunch of BS - Here's the 5% of it to Learn](../sources/prompt-engineering-is-a-bunch-of-bs-heres-the-5-of-it-to-learn.md) - "reflection as well which is self-reflection an AI being able to improve its own response as you can see in this diagram here these two are super important" [0:01:58]
