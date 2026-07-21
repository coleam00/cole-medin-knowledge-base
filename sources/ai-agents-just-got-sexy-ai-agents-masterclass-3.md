---
type: source
title: "AI Agents Just Got Sexy - AI Agents Masterclass #3"
description: "You can wrap an existing tool-calling AI agent in a beautiful, deployable chat UI in about five minutes using Streamlit, then add typewriter-style streaming with Python generators."
youtube_id: ft9Z67d1wik
url: https://www.youtube.com/watch?v=ft9Z67d1wik
slug: ai-agents-just-got-sexy-ai-agents-masterclass-3
published: 2024-07-07
duration: "0:16:18"
recency_rank: 185
raw: "../raw/ai-agents-just-got-sexy-ai-agents-masterclass-3.md"
tags: [generative-ui, streaming-responses, chat-interfaces, agent-deployment]
created: 2026-07-21
updated: 2026-07-21
---

# AI Agents Just Got Sexy - AI Agents Masterclass #3

In the third AI Agents Masterclass video, Cole Medin takes the Asana-integrated LangChain agent built in prior videos and puts a real user interface around it using Streamlit, arguing that many people either ship agents with an ugly terminal interface or waste weeks hand-building React/HTML front ends when they do not need to. Because Streamlit re-runs the entire Python script on every UI change, the core lesson is managing chat history and user input through Streamlit's session state, guarded by an initialization check so the message history is not reset on every rerun. The main function loops over session-state messages, renders each with st.chat_message plus st.markdown, and reacts to st.chat_input, updating both the UI and the session state together to keep them consistent.

The second half adds streaming so responses type out chunk-by-chunk instead of appearing all at once. Cole explains that streaming is trivial for a plain chatbot (return the stream and hand it to Streamlit), but trickier with tool calling because the agent may call the LLM twice: once to decide on a tool, and again after the tool result. The solution is Python generators: instead of returning the stream (which would end the function before the tool runs), the prompt function yields each chunk while continuing on to invoke the tool and produce a second stream, whose chunks are also yielded. Streamlit's st.write_stream consumes the generator, and the full response is reassembled manually to store in session state.

The result is a clean, deployable web chatbot that creates real Asana tasks, renders returned links as hyperlinks via markdown, and streams responses live thanks to Streamlit's hot reloading. Cole frames it as the UI foundation for all future masterclass projects, previewing a next video that expands the agent into a full task manager.

## Concepts covered

- [Generative UI](../concepts/generative-ui.md)
- [Context Engineering](../concepts/context-engineering.md)
- [Streaming Responses](../concepts/streaming-responses.md)
- [Tool Design](../concepts/tool-design.md)
- [Tool Calling](../concepts/tool-use.md)
- [Agent Deployment](../concepts/agent-deployment.md)

## Entities

- [Streamlit](../entities/tools/streamlit.md)
- [LangChain](../entities/tools/langchain.md)
- [Asana](../entities/tools/asana.md)
- [Cole Medin](../entities/people/cole-medin.md)

## Key moments

- **[0:00:00]** Problem framing: agents with ugly or over-engineered UIs; promise of a simple beautiful interface
- **[0:01:24]** Import Streamlit; the LLM-calling functions do not need to change, only main()
- **[0:02:19]** Add a title component with st.title
- **[0:03:05]** Initialize chat history in session state, seeded with a system message plus current date
- **[0:03:51]** Key insight: Streamlit re-runs the whole script on every UI change, so guard state init with an if-check
- **[0:04:52]** Loop over session-state messages and render each with st.chat_message plus st.markdown
- **[0:05:41]** React to st.chat_input; update both the UI and session state together
- **[0:07:02]** Run with "streamlit run agent_with_ui.py"; browser tab opens automatically
- **[0:08:24]** Live demo: create an Asana task from chat; returned link renders as a hyperlink
- **[0:09:09]** Bonus section: adding typewriter-style streaming
- **[0:10:04]** Why streaming plus tool calling is tricky: two LLM calls, cannot return early
- **[0:10:37]** Use Python generators (yield) to stream chunks while still invoking the tool
- **[0:11:05]** st.write_stream renders the generator; rebuild the full message for session state
- **[0:14:03]** Streamlit hot reloading applies code changes without restarting
- **[0:14:33]** Streaming demo, including a tool call that creates a task after a warning

## Transcript

[Raw transcript](../raw/ai-agents-just-got-sexy-ai-agents-masterclass-3.md)
