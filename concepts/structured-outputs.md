---
type: concept
title: "Structured Outputs"
description: "Constraining LLM output to a validated schema (with retries on failure) so downstream code can rely on its shape."
tags: [structured-output, schema, validation, parsing, structured-data, reliability]
videos: [openais-brand-new-agents-sdk-crash-course, weve-been-building-ai-agents-wrong-until-now, 10x-your-ai-agents-with-this-one-agent-architecture, build-a-hilarious-ai-game-from-scratch-in-10-minutes, function-calling-with-any-llm-for-local-ai-agents-feat-langchain-huggingface-and-llama-3, openais-o1-is-barely-usable-but-i-fixed-it, 3-most-important-prompt-engineering-techniques-you-need-to-know, this-one-command-makes-coding-agents-find-all-their-mistakes-use-it-now, build-a-chatgpt-style-app-for-your-n8n-ai-agents-in-minutes, effortless-rag-in-n8n-use-all-your-files-pdfs-excel-and-more, bubble-is-my-biggest-regret-for-no-code-ai-apps-what-i-use-instead]
created: 2026-07-21
updated: 2026-07-21
---

# Structured Outputs

Structured outputs constrain an LLM to return data in a fixed, validated shape instead of free-form text. Cole defines it directly: "what structured outputs are is a way to standardize the response from En large language model essentially forcing it to give a Json response so that there are specific values we can always expect it to give." [0:07:15] You give the model a schema, usually a class, "that defines the schema in Json that you want the llm to produce and it'll use this class to validate that the large language models response matches the schema." [0:02:41] If the response does not match, the validation layer catches it and can force a retry.

The reason this matters is that code cannot depend on prose. "When you're working with the API for something like GPT and you need the AI to return something in a specific format or your program won't be able to understand that response," [0:05:30] you have to pin the shape down, because "I need the format to be the same every single time this won't cut it because the AI might decide to answer it differently... where my program would break." [0:06:09] Structured outputs also double as a reliability lever against bad generations: "this is one of the ways to reduce hallucinations with llms," [0:08:17] and, as Cole puts it, "a lot of times AI can hallucinate and give trash output and this way we know that is not trash output very very important." [0:06:13]

Structured outputs are also the mechanism underneath [tool use](./tool-use.md). To call a tool an agent must emit a machine-parseable request: "we can't just have it spit out raw text because we have to understand when it wants to use a tool and what arguments to use for each tool," [0:05:43] and the guaranteed result is "a Json object that has the tool calls and it has the content nothing more nothing less." [0:08:29] In practice this is often a one-liner over a framework: "we just add this single line to our pantic AI agent the result type is and then we pass in our class that we defined." [0:20:39] Cole's broader point is that validation, not raw generation, is where agent reliability is won: many tools "don't focus on validation for the output of llms or testing llms... all these things they all have to do with validation." [0:02:57]

## Builds on

- [Contract-First Development](./contract-first.md) - a schema is a contract downstream code and the model both agree to.
- [Structured vs. Unstructured Data](./structured-vs-unstructured-data.md) - structured outputs turn model prose into structured data.

## Related

- [Tool Use](./tool-use.md) - tool calls are structured outputs the agent must emit to act.
- [Guardrails](./guardrails.md) - schema validation is a guardrail on model output.
- [Production-Grade Agents](./production-grade-agents.md) - reliable shapes are a prerequisite for production.
- [Agent Prompting](./agent-prompting.md) - prompting can request a format even without native schema support.
- [Few-Shot Prompting](./few-shot-prompting.md) - examples help the model hit the target format.
- [Prompt Engineering](./prompt-engineering.md) - the fallback when you cannot enforce a schema in code.
- [Agentic Workflow Engineering](./agentic-workflow-engineering.md) - predictable field mapping between workflow nodes.
- [Context Reset](./context-reset.md) - a clean, typed response is easier to carry across resets.
- [Web Crawling](./web-crawling.md) - extracting structured records from scraped pages.
- [Human in the Loop](./human-in-the-loop.md) - a validated shape is easier for a human to review.

## Tools

- [Pydantic AI](../entities/tools/pydantic-ai.md) - the validation layer Cole reaches for; set `result_type` to a class and it enforces the schema.
- [OpenAI Agents SDK](../entities/tools/openai-agents-sdk.md) - supports structured outputs to standardize agent responses.
- [LangChain](../entities/tools/langchain.md) - provides JSON output parsers that enforce a defined shape.
- [n8n](../entities/tools/n8n.md) - field mapping between nodes depends on matching output attribute names.

## Sources

- [OpenAI's BRAND NEW Agents SDK (Crash Course)](../sources/openais-brand-new-agents-sdk-crash-course.md) - "[0:07:15] what structured outputs are is a way to standardize the response from En large language model essentially forcing it to give a Json response so that there are specific values we can always expect it to give"
- [We've Been Building AI Agents WRONG Until Now](../sources/weve-been-building-ai-agents-wrong-until-now.md) - "[0:02:10] you expect often times specific input from the large language model or specific output if you're working with structured output... and pantic is that validation layer to really ensure that you're getting that structured output"
- [10x Your AI Agents with this ONE Agent Architecture](../sources/10x-your-ai-agents-with-this-one-agent-architecture.md) - "[0:18:45] we are using structured outputs to guarantee that every single response from this agent has these key pieces of information"
- [Build a Hilarious AI Game from SCRATCH in 10 Minutes](../sources/build-a-hilarious-ai-game-from-scratch-in-10-minutes.md) - "[0:02:41] you give a class that defines the schema in Json that you want the llm to produce and it'll use this class to validate that the large language models response matches the schema"
- [Function Calling with ANY LLM for Local AI Agents (Feat. LangChain, HuggingFace, and Llama 3)](../sources/function-calling-with-any-llm-for-local-ai-agents-feat-langchain-huggingface-and-llama-3.md) - "[0:08:29] AI response this variable is guaranteed to be a Json object that has the tool calls and it has the content nothing more nothing less"
- [OpenAI's o1 is Barely Usable, but I Fixed it...](../sources/openais-o1-is-barely-usable-but-i-fixed-it.md) - "[0:11:37] what this is going to do is basically enforce that the output we get from the 01 llm is going to be a dictionary that has exactly these values and nothing different"
- [3 MOST Important Prompt Engineering Techniques you NEED to know!](../sources/3-most-important-prompt-engineering-techniques-you-need-to-know.md) - "[0:06:09] I need the format to be the same every single time this won't cut it because the AI might decide to answer it differently... where my program would break"
- [This One Command Makes Coding Agents Find All Their Mistakes (Use it Now)](../sources/this-one-command-makes-coding-agents-find-all-their-mistakes-use-it-now.md) - "[0:08:30] I have a lot of structure built at the bottom of the prompt, the bottom of the skill.md. So it's always outputting to me in the exact same way every time."
- [Build a ChatGPT Style App for Your n8n AI Agents in MINUTES](../sources/build-a-chatgpt-style-app-for-your-n8n-ai-agents-in-minutes.md) - "[0:15:48] I need to make sure that this maps with this value right here because that way my function in open web UI knows where to look to find the AI response."
- [Effortless RAG in n8n - Use ALL Your Files (PDFs, Excel, and More)](../sources/effortless-rag-in-n8n-use-all-your-files-pdfs-excel-and-more.md) - "[0:13:01] your data has to correspond to the output field from the extract node"
- [Bubble is My BIGGEST Regret for No Code AI Apps - What I Use Instead](../sources/bubble-is-my-biggest-regret-for-no-code-ai-apps-what-i-use-instead.md) - "[0:07:07] you can do structured output as well like you see right here everything that you need in an AI agent"
