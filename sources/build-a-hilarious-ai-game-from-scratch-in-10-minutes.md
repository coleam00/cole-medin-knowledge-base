---
type: source
title: "Build a Hilarious AI Game from SCRATCH in 10 Minutes"
description: "You can build a genuinely fun, useful AI app fast by pairing a single well-structured LLM prompt with schema validation and a simple state machine in a Streamlit chat UI."
youtube_id: BZJBDYkUDf0
url: https://www.youtube.com/watch?v=BZJBDYkUDf0
slug: build-a-hilarious-ai-game-from-scratch-in-10-minutes
published: 2024-07-17
duration: "0:13:07"
recency_rank: 182
raw: "../raw/build-a-hilarious-ai-game-from-scratch-in-10-minutes.md"
tags: [structured-outputs, effective-prompting, chat-interfaces, streaming-responses]
created: 2026-07-21
updated: 2026-07-21
---

# Build a Hilarious AI Game from SCRATCH in 10 Minutes

Cole builds an AI Mad Libs chatbot from an empty skeleton in about five minutes. The core idea is to prompt GPT (recommended: gpt-4o) exactly once to generate an entire Mad Lib, returning JSON with two fields: the story text and a list of blanks to fill. That single-prompt design keeps the app fast and cheap because there is no second call needed to render the finished story to the user.

The reliability of the app comes from enforcing a JSON schema with LangChain output parsers. A class defines the expected shape (a string for text and a list of strings for blanks), and the parser validates the model's response against it, throwing an error and failing the script if the output does not match. Cole stresses this as the antidote to LLM hallucination and "trash output": if parsing succeeds you are guaranteed a well-formed object you can safely key off of for the rest of the app. He also chains prompt, chat model, and output parser as a single LangChain chain.

The app flow is driven by a two-state machine stored in Streamlit session state: "choosing theme" (generate the Mad Lib) and "choosing words" (fill blanks one at a time, then print the completed story and reset to choosing theme for an infinite loop). A small helper function mimics token streaming since real OpenAI streaming cannot be used when the response must first be parsed as JSON. Cole then demos it live with an "AI taking over the world" theme.

## Concepts covered

- [Structured Outputs](../concepts/structured-outputs.md)
- [Effective Prompting](../concepts/effective-prompting.md)
- [Chat Interfaces](../concepts/chat-interfaces.md)
- [Streaming Responses](../concepts/streaming-responses.md)

## Entities

- [Cole Medin](../entities/people/cole-medin.md)
- [OpenAI](../entities/organizations/openai.md)
- [LangChain](../entities/tools/langchain.md)
- [Streamlit](../entities/tools/streamlit.md)
- [GitHub](../entities/tools/github.md)

## Key moments

- **[0:00:00]** Intro: pitch for an AI Mad Libs chatbot that generates a themed Mad Lib and fills blanks one at a time
- **[0:01:29]** Load environment variables and OpenAI API key; recommends gpt-4o with a default fallback
- **[0:01:42]** The single generation prompt: produce the whole Mad Lib and blanks in one call with a defined JSON schema
- **[0:02:41]** Enforcing the JSON schema via LangChain output parsers to validate the LLM response
- **[0:03:28]** Helper function to simulate streaming text to the user since real streaming cannot be used with JSON parsing
- **[0:04:11]** Streamlit session state: messages list plus a state of "choosing theme" or "choosing words"
- **[0:06:13]** Schema validation catches hallucinated "trash output" so a passing parse guarantees usable JSON
- **[0:06:56]** Building the LangChain chain: prompt to GPT to JSON output parser, invoked with the user's theme
- **[0:08:26]** Word-filling logic: replace the first blank with the bolded user word, advance or finish
- **[0:09:36]** Live demo of the finished Streamlit Mad Libs bot with the theme "AI taking over the world"

## Transcript

[Raw transcript](../raw/build-a-hilarious-ai-game-from-scratch-in-10-minutes.md)
