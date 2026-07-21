---
type: concept
title: "Agent Prompting Techniques"
description: "Prompt-level techniques that shape agent behavior: a system/goal/do/don't template, dynamic runtime injection, internal thought messages, current-date grounding, and intent inference."
tags: [system-prompt, dynamic-prompting, intent, templates]
videos: [bubble-is-my-biggest-regret-for-no-code-ai-apps-what-i-use-instead, openais-o1-is-barely-usable-but-i-fixed-it, youre-wasting-time-coding-your-ai-agents, prompt-engineering-is-a-bunch-of-bs-heres-the-5-of-it-to-learn, i-finally-built-an-ai-agent-to-organize-my-life-ai-agents-masterclass-4]
created: 2026-07-21
updated: 2026-07-21
---

# Agent Prompting Techniques

Agent prompting is the set of prompt-level moves that shape how an autonomous agent behaves before, during, and after it acts. Cole reduces the whole art to a small template: "for any kind of complex prompt I just have four categories I have the system prompt which is who you are the goal and then things to do and things not to do" ([0:03:49]). The system prompt establishes identity with concrete adjectives ("you tell it who the agent is and you give it adjectives to describe it like you are intuitive friendly you are skilled", [0:03:22]), the goal fixes the objective, and the do/don't lists constrain the behavior in between.

## How it works

Beyond the static template, agent prompts are assembled dynamically at runtime. Data the agent needs is injected into the prompt just before the call: "the meeting is going to be passed into the agent and then added onto the prompt like this right here" ([0:06:24]), and "you can even give roles and constraints there's so many different levels of customization" ([0:06:37]). A critical piece of that runtime context is grounding the model in the present moment, "we want to tell our Asana assistant what day it is so it can accurately determine due dates when we give relative dates like this Saturday or next Friday" ([0:05:47]).

Two more techniques make agents feel autonomous. First, internal thought messages: a self-addressed reasoning trace that never reaches the user. "a thought is going to be an AI message that starts with thought colon and it's going to be an internal dialogue that the llm has with itself" ([0:09:26]), and "it's just meant to give the llm context for itself about what happened when it invoked a tool or any errors that it needs to correct" ([0:09:42]). Second, intent inference: prompting so the agent acts on what the user means, not only what they literally type. "I don't want to have to explicitly say that I want it to delete that task um but using natural language it can pick up on the fact that I do want to do that" ([0:03:25]).

## Builds on

- [Prompt Engineering](./prompt-engineering.md)
- [System Prompt Engineering](./system-prompt-engineering.md)

## Related

- [Tree-of-Thought Prompting](./tree-of-thought.md) - Letting a model explore many possibilities and outcomes in parallel branches before committing to an answer, rather than a single linear chain of thought.
- [The Agent Loop (Reason-Act-Observe)](./agent-loop.md)
- [Tool Use](./tool-use.md)
- [Agentic Workflow Engineering](./agentic-workflow-engineering.md)
- [Self-Correcting Agents](./self-correction.md)
- [Structured Outputs](./structured-outputs.md)
- [Effective Prompting](./effective-prompting.md)

## Tools

- [Pydantic AI](../entities/tools/pydantic-ai.md)
- [Asana](../entities/tools/asana.md)
- [Google Calendar](../entities/tools/google-calendar.md) - Google's calendar service, integrated via API as the action target for agents that turn extracted meeting action items into scheduled events.
- [Prompting Guide](../entities/tools/prompting-guide.md) - promptingguide.ai, the free resource Cole names as the single prompt-engineering guide worth studying end to end.

## Sources

- ["Prompt Engineering" is a Bunch of BS - Here's the 5% of it to Learn](../sources/prompt-engineering-is-a-bunch-of-bs-heres-the-5-of-it-to-learn.md) - "[0:03:49] for any kind of complex prompt I just have four categories I have the system prompt which is who you are the goal and then things to do and things not to do"
- [Bubble is My BIGGEST Regret for No Code AI Apps - What I Use Instead](../sources/bubble-is-my-biggest-regret-for-no-code-ai-apps-what-i-use-instead.md) - "[0:06:24] the meeting is going to be passed into the agent and then added onto the prompt like this right here"
- [OpenAI's o1 is Barely Usable, but I Fixed it...](../sources/openais-o1-is-barely-usable-but-i-fixed-it.md) - "[0:09:26] a thought is going to be an AI message that starts with thought colon and it's going to be an internal dialogue that the llm has with itself and so it's not to be shared with the user"
- [You're WASTING TIME Coding Your AI Agents](../sources/youre-wasting-time-coding-your-ai-agents.md) - "[0:05:47] we want to tell our Asana assistant what day it is so it can accurately determine due dates when we give relative dates like this Saturday or next Friday"
- [I FINALLY Built an AI Agent to Organize my Life - AI Agents Masterclass #4](../sources/i-finally-built-an-ai-agent-to-organize-my-life-ai-agents-masterclass-4.md) - "[0:03:25] I don't want to have to explicitly say that I want it to delete that task um but using natural language it can pick up on the fact that I do want to do that"
