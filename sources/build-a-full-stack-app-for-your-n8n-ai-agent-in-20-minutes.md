---
type: source
title: "Build a FULL Stack App for your n8n AI Agent in 20 Minutes"
description: "You can wrap an n8n AI agent in a clean, secure, production-leaning front end in an afternoon by having Claude write a Streamlit app, exposing the agent over a webhook, and layering Supabase authentication across both the front end and the n8n workflow."
youtube_id: JyolNYRbAcs
url: https://www.youtube.com/watch?v=JyolNYRbAcs
slug: build-a-full-stack-app-for-your-n8n-ai-agent-in-20-minutes
published: 2024-10-02
duration: "0:20:27"
recency_rank: 158
raw: "../raw/build-a-full-stack-app-for-your-n8n-ai-agent-in-20-minutes.md"
tags: [full-stack, vibe-coding, n8n, supabase]
created: 2026-07-21
updated: 2026-07-21
---

# Build a FULL Stack App for your n8n AI Agent in 20 Minutes

Cole argues that an n8n agent alone isn't enough for real users: you need a proper front end, and the fastest way to get one is the Claude + Streamlit + Supabase combo rather than v0 or hand-coding a React/Next.js app. He has Claude generate a basic Streamlit chat interface, giving it a precise contract for the n8n webhook (a POST payload with session_id and chat_input, and an output key in the response JSON). On the n8n side he replaces the built-in chat trigger with a Webhook trigger plus a Respond to Webhook node, and uses an Edit Fields node that reads chat_input/session_id from either the chat widget or the webhook body so both paths work.

The first cut uses a hardcoded bearer token for very basic protection so strangers can't drain his LLM credits, but he stresses this isn't production-grade. He then re-prompts Claude to add real Supabase authentication with both login and signup tabs, passing the signed-in user's Supabase access token as the bearer token to the webhook. In n8n he turns off the webhook's own auth and instead verifies the token manually with an HTTP request to Supabase's /auth/v1/user endpoint (using the service-role secret as apikey and the user's token as authorization); a valid response returns a user object with an email, which gates the rest of the workflow.

Along the way he shares practical prompting habits: specify the exact webhook usage, tell Claude to build both login and signup, and pre-empt known hallucinations (like the deprecated st.experimental_rerun) by naming them in the prompt. Building with Claude is iterative, but a strong model corrects itself quickly instead of looping on hallucinations. He also notes security hardening options like storing the Supabase key in AWS Secrets Manager and relying on row-level security so the anon key can stay public.

## Concepts covered

- [Full-Stack AI Application](../concepts/full-stack-ai-application.md)
- [Vibe Coding](../concepts/vibe-coding.md)
- [Stacking Context-Engineering Strategies](../concepts/strategy-stacking.md)
- [Chat Interfaces](../concepts/chat-interfaces.md)
- [Contract-First Development](../concepts/contract-first.md)
- [Memory Systems](../concepts/memory-systems.md)
- [Agent Security](../concepts/agent-security.md)
- [Reduce Assumptions](../concepts/reduce-assumptions.md)
- [Self-Correcting Agents](../concepts/self-correction.md)

## Entities

- [n8n](../entities/tools/n8n.md)
- [Streamlit](../entities/tools/streamlit.md)
- [Supabase](../entities/tools/supabase.md)
- [Claude](../entities/tools/claude.md)
- [Postgres](../entities/tools/postgres-pgvector.md)
- [Cole Medin](../entities/people/cole-medin.md)

## Key moments

- **[0:01:03]** Introduces the Claude + Streamlit + Supabase combo and why it beats v0 / hand-coding
- **[0:02:35]** First Claude prompt: basic Streamlit chat app with hardcoded bearer token and webhook payload spec
- **[0:05:20]** n8n side: swap the chat trigger for a Webhook trigger plus Respond to Webhook node
- **[0:07:30]** Edit Fields node reads chat_input/session_id from either the chat widget or webhook body
- **[0:11:00]** Second Claude prompt: add Supabase auth, use the user's Supabase token as the bearer token
- **[0:13:33]** n8n verifies the Supabase token via an HTTP request to /auth/v1/user
- **[0:18:32]** Deprecated st.experimental_rerun hallucination surfaces; Claude self-corrects

## Transcript

[Raw transcript](../raw/build-a-full-stack-app-for-your-n8n-ai-agent-in-20-minutes.md)
