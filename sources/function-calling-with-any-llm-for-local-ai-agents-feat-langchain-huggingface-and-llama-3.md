---
type: source
title: "Function Calling with ANY LLM for Local AI Agents (Feat. LangChain, HuggingFace, and Llama 3)"
description: "You can add function/tool calling to any local LLM that lacks it natively by injecting tool descriptions into the system prompt and forcing the model to return a validated JSON schema of tool calls."
youtube_id: PPDsrvuPhWQ
url: https://www.youtube.com/watch?v=PPDsrvuPhWQ
slug: function-calling-with-any-llm-for-local-ai-agents-feat-langchain-huggingface-and-llama-3
published: 2024-07-10
duration: "0:15:57"
recency_rank: 184
raw: "../raw/function-calling-with-any-llm-for-local-ai-agents-feat-langchain-huggingface-and-llama-3.md"
tags: [tool-use, local-ai, structured-outputs, guardrails]
created: 2026-07-21
updated: 2026-07-21
---

# Function Calling with ANY LLM for Local AI Agents (Feat. LangChain, HuggingFace, and Llama 3)

Cole demonstrates how to implement custom function calling from scratch so that lightweight, local models like Meta's Llama 3 or Microsoft's Phi, which do not ship with native function calling like GPT and Claude, can still act as true AI agents. The trick is entirely prompt-and-parsing based: build a mapping of function names to Python function objects, auto-generate tool descriptions from each function's docstring (name, arguments, types, return value), and inject that list plus a strict JSON schema into the system prompt so the model knows when and how to call each tool.

The model is required to respond in a JSON object with two keys: a `tool_calls` array (each with a name and arguments) and a `content` string for raw user-facing text. LangChain's JSON output parser validates the response against the schema; if the model produces malformed output, the code recurses to retry with a bounded retry count so it never loops forever. Because local models hallucinate more, the code also tracks already-invoked tools to prevent duplicate calls. Tool results are fed back as internal "thought" messages so the model can compose a final natural-language reply.

The demo app is built with Streamlit and LangChain, pulls the model from HuggingFace (via a serverless endpoint, swappable for a fully local HuggingFace pipeline or Ollama), and uses a single Asana "create task" tool to prove real external-service interaction. Cole shows Llama 3 correctly creating an Asana task from the message "I need to mow the lawn by Saturday," while warning that local models are weaker than GPT/Claude and this custom approach will surface more hallucinations.

## Concepts covered

- [Tool Calling](../concepts/tool-use.md)
- [Local & Self-Hosted AI](../concepts/local-ai.md)
- [Structured Outputs](../concepts/structured-outputs.md)
- [Tool Design](../concepts/tool-design.md)
- [Guardrails](../concepts/guardrails.md)
- [What Is an AI Agent](../concepts/what-is-an-ai-agent.md)
- [Model Selection](../concepts/model-selection.md)

## Entities

- [LangChain](../entities/tools/langchain.md)
- [Hugging Face](../entities/organizations/hugging-face.md)
- [Llama](../entities/tools/llama.md)
- [Streamlit](../entities/tools/streamlit.md)
- [Asana](../entities/tools/asana.md)
- [Ollama](../entities/tools/ollama.md)
- [OpenAI](../entities/organizations/openai.md)
- [Cole Medin](../entities/people/cole-medin.md)

## Key moments

- **[0:00:00]** Function calling is what turns LLMs into agents that interact with external services
- **[0:00:18]** Problem framed: local models like Llama and Phi lack built-in function calling
- **[0:02:27]** Asana chosen as the external service; single create-task tool for demo
- **[0:04:29]** Tool descriptions built by pulling docstrings from Python functions
- **[0:05:43]** System prompt must force JSON output so tool calls are parseable
- **[0:07:32]** Recursion/retry logic when the model does not conform to the schema
- **[0:07:32]** Deduplication of tool calls to guard against local-model hallucination
- **[0:13:55]** Live demo: Llama 3 creates the "mow the lawn" Asana task
- **[0:15:14]** Warning: local models hallucinate more and may output malformed JSON

## Transcript

[Raw transcript](../raw/function-calling-with-any-llm-for-local-ai-agents-feat-langchain-huggingface-and-llama-3.md)
