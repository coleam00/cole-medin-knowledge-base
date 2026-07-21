---
type: raw-transcript
title: "Google, Anthropic, and OpenAI's Guides to AI Agents ALL in 18 Minutes"
youtube_id: TlbcAphLGSc
url: https://www.youtube.com/watch?v=TlbcAphLGSc
slug: google-anthropic-and-openais-guides-to-ai-agents-all-in-18-minutes
published: 2025-05-18
duration: "0:18:02"
fetched_at: 2026-07-21
immutable: true
---

## Transcript

**[0:00:00]** The internet is filled with information for us to learn what AI agents are and how to build them effectively. But there's just so much information out there that it's actually pretty overwhelming. And so the three top and most overarching resources that I have found that explained agents very clearly

**[0:00:16]** is this agent white paper by Google this article on building effective agents from Anthropic, and then this agent guide from OpenAI. Now, these articles themselves are pretty long though. In fact, I did a word count. It's over 14,000 words when you combine all of these articles together. And so

**[0:00:34]** it's not the kind of thing that you or I would just want to go through in a single sitting. And so what I have done for you is I have combined all these articles together. And I've spent hours with the help of AI, of course synthesizing all of this information

**[0:00:48]** into a less than 20 minute presentation. So you can basically get everything you need out of these resources for building AI agents in just 20 minutes. And pay attention to this because if you master the fundamentals for agents that are laid out here, you're going to be ahead

**[0:01:03]** of 99% of people and it's going to be that much easier for you to build any agent that you want to tackle in the future. And so, let's just dive right into it. So, all three of these guides they start out by defining for us what an agent is. And to summarize all of

**[0:01:17]** that, an agent is a system that uses a large language model to reason like GPT Gemini, or Claude. And as it is reasoning, it will decide to take actions to do things on our behalf like summarize a Slack conversation, send an email, write or execute code. And then

**[0:01:34]** when it takes those actions, it's going to observe what happened. And so we have this reasoning loop where the LLM will decide to do things. So it'll take actions. It'll figure out what happened when it took that action to potentially then take more actions as a follow-up or

**[0:01:49]** to just continue its process. And we don't know how many actions the agent is going to take. Sometimes it might take zero actions and just answer our question right away. Other times it'll take two. Sometimes it'll take five. We're giving it that flexibility leveraging its reasoning power to figure

**[0:02:04]** out how many actions to take. And just to show you what that looks like in each of these guides really quickly. Within the Google paper, they say that an agent can be defined as an application that attempts to achieve a goal by observing the world and acting upon it. And then

**[0:02:18]** within the anthropic article, an agent is a system where the LLM dynamically directs their own processes and tool usage. So very very similar. And then within our OpenAI guide, they have an even shorter definition. Agents are systems that independently accomplish tasks on your behalf. And then after each of these guides explain what an

**[0:02:38]** agent is, they do something that I respect a lot because they cover then when you should build an AI agent versus when it is actually overengineering because there are a lot of automations that make sense to just build a traditional workflow, maybe including a large language model in the mix, but not

**[0:02:54]** actually building an agent. Agents are powerful because of their extra reasoning capability, but because we're giving so much responsibility to them it's more dangerous and it makes our systems more unpredictable. And so I'll actually show you an example of this. So I have N8N just as a tool here to help

**[0:03:10]** us visualize a workflow versus an actual AI agent. And so in this first example that we have here, this is just a linear workflow. We're using a large language model to create a post for X and then one for LinkedIn and then another one for our blog. In this case, we are using

**[0:03:27]** large language models, but it's not like we have an agent that can make decisions on our behalf. We are always going to generate one expost, one LinkedIn post and one blog post using LLMs. It's not interacting with our environment in ways that is based on its own reasoning. It's

**[0:03:41]** just a linear process. On the other hand, this is an AI agent. This is one that I built earlier on my channel before where it's able to interact with GitHub repositories, look at all the files that are there, and analyze individual files. And this tool that we give it, it can decide to look at three

**[0:03:56]** files or zero or 10. It has that reasoning capability to figure out when it should interact with its environment and how much. So that makes it an agent but it's going to be more unpredictable because maybe it shouldn't look at a file, but it decides to anyway or we

**[0:04:12]** want it to analyze a file and it skips that. That's the kind of mistakes that agents can make that we wouldn't make in a traditional workflow. Like it's never going to accidentally skip creating the expost because that is hardwired into this linear process. So I hope that makes sense. So you want to build agents

**[0:04:29]** when you need that complex decision-m around the tools that it is using to interact with our environment. And you also want to build agents when brittle logic is present. And what I mean by that is sometimes the rules in your system is a bunch of gray area. And so

**[0:04:46]** when you present situations to an agent you want it to kind of deploy its extra reasoning capability to understand how to navigate the situations that you presented. But if your automations are very predictable and stable logic is enough, like just regular code or regular workflow automation, then you

**[0:05:04]** don't want to overengineer for an agent. Next up, we have the four components that go into any AI agent. And that is our large language model. That's the brain that gives us all of our reasoning power. We have the tools for it to interact with our environment. We have

**[0:05:19]** the instructions, usually known as the system prompt, where we instruct the behavior and tone for our agent. And then last we have our memory. This is going to be both for short-term memory conversation history, and long-term memory. So our agent can remember our goals and preferences and instructions

**[0:05:35]** between conversations. And going back to our guides, Google definitely explains this the best in my opinion. You can see they lay out the four different components very well here for our instructions, memory, our LLM, and then the tools. And then Enthropic, it's almost as good. They have all the

**[0:05:51]** components here except they don't explicitly call out the system prompt which is really crucial for our agent. And then OpenAI has the model tools and instructions, but they don't have the memory here. And so that's why I think Google explains this the best. These four components are so crucial. And

**[0:06:06]** whenever you have an issue with your agent in general, it's always going to be one of these four things. And so it's worth thinking to yourself, is this the LLM reasoning not being good enough? Do I need to give better tools, implement better memory, maybe refine my system

**[0:06:20]** prompt? It's going to be one of those things. And so that's why it's so powerful for you to understand these four components that go into building any AI agent. Next, we have the different reasoning patterns for AI agents. So, first we have react. This is reason, then act, then observe. This is

**[0:06:35]** the main one that we'll focus on in a little bit. Then we have chain of thought. So, stepby-step logic. This is your classic telling an LLM to think through a problem step by step. And that generally does give us better results. And then last, this is the most

**[0:06:49]** technical one that none of these guys really focus on too much is the whole idea of tree of thought. Letting our AI agent explore many different possibilities and outcomes in parallel. But React is the primary one. And this is called out in the Google paper that this is the one that is really standard

**[0:07:06]** for most agents. This is what they really spend a lot of time focusing on. And so like with everything else, I've got a beautiful diagram here showing us what that looks like. And this should look very similar to our other diagram just showing agents in general because they really follow this react cycle of

**[0:07:20]** reasoning about what they should do taking that action, observing on what happened when they took that action, and then reflecting to adjust their strategy, take additional actions whatever might be necessary. The sponsor of today's video is Augment Code. It's the coding agent that actually understands your code base. Because one

**[0:07:38]** of the biggest problems that we have with AI coding assistants in general right now is they start to completely fall apart when your projects get bigger. I'm sure you've seen that for yourself and Augment Code is the solution for that. I've been playing around with it recently. I've been very

**[0:07:52]** impressed and a lot of you have been trying it yourself and specifically asking me to cover it both on my YouTube channel and in the Dynamis community. And so that's what I'm doing for you right now. So Augment is an extension that you can get for a lot of different

**[0:08:04]** IDEs. Like in this case, I have it for Visual Studio Code. And when you first open up a project with Augment, it'll have you index the codebase. This is their way to take your codebase and turn it into a knowledge base for the AI coding assistant. It's very, very

**[0:08:19]** powerful. And look at how fast that was. So, so fast. And I know that there are other AIDes that index your codebase under the hood like Cursor and Windsurf but they don't have this super powerful explicit process like we have with Augment. And with their new agent mode

**[0:08:34]** you can work with your code automatically. Have the agent make changes just like you would in cursor and windsurf. But just to show you really quickly how well this agent understands my codebase. First, look at these questions. Like you can tell that it has a deep knowledge of my codebase

**[0:08:48]** just in the suggested questions. And I can ask one of these like what does my authentication flow look like both with Ozero and how I integrate that with Superbase. It calls out different components, gives me the necessary code to understand what's going on. like this is the perfect answer. So, I'll have a

**[0:09:03]** link in the description to Augment Code. You can sign up for a free 14-day trial to see all this power for yourself. I would highly recommend checking it out if you want to use AI to work with larger projects and production applications. And then the next component I could definitely spend an

**[0:09:18]** entire video series covering because we have common patterns for building agents and multi- aent workflows. So, we have prompt chaining which is having multiple agents just running sequentially. We have routing where we use one LLM to route the request to specialized agents. We have tool use which we've seen

**[0:09:36]** already. We have evaluator loops where we have an LLM produce some output and then we have another LLM evaluate it have a loop of selfcorrection if necessary. Then we have the orchestrator and worker flow where we have one primary agent that is managing many other agents taking the task and

**[0:09:52]** splitting it up. And then we have autonomous loops. This is the most dangerous one but this is where an AI agent decides everything. We don't have the human involved in any kind of way. The agents manage their own inputs and outputs for basically the entire process. And the best guide to dive into

**[0:10:08]** for all these patterns is definitely the one from anthropic on building effective agents because they have these diagrams that show us very clearly what these different processes look like. So for prompt chaining for example, we have this example here. For routing, we have parallelization. We have the whole idea

**[0:10:24]** of the orchestrator and worker pattern that I mentioned earlier. And then we have the evaluator and optimizer. And so definitely read through these different examples in this article if you're curious on these different patterns. Basically any agent that you're going to be building or any multi- aent workflow

**[0:10:38]** is going to follow one of these. And then a special note here from the OpenAI guide. They talk about building a single agent system versus multi- aent. And typically what it comes down to is you want to use a single agent system as much as possible because it is the

**[0:10:52]** simplest. But then you'll start to run into issues like tool overload where there's just so much given to one agent. Usually you don't want more than 10 to 15 tools for one agent. Once you get to that point, you want to split your process into multiple different agents

**[0:11:07]** with something like the orchestrator and worker architecture. And when you have more complex logic, it's the same kind of deal. That's when you want to go into multi- aent systems where you have agent handoffs and manager agents like the orchestrators or decentralized where you just have a lot of different agents that

**[0:11:23]** are operating together to tackle a problem in tandem. So that's just a really important note to go along with these patterns that we have here because a lot of them do apply to multi- aent workflows. Then that brings us to the allimportant safety and guard rails because here's the thing, no matter how

**[0:11:39]** powerful of an LLM you are using, it is going to hallucinate. And so making sure those hallucinations don't affect our AI system as a whole is all based around how good our guard rails are. So we can limit certain actions for our agent like if it's interacting with our database

**[0:11:54]** maybe only making sure it can use readonly tools. We have human review. So adding in humanly in the loop to approve actions and allow for our feedback to direct the agent filtering certain outputs. And then also the important thing that these guys call out is that you always want to test your agents in a

**[0:12:11]** safe environment before deploying them to production. Making sure that there aren't situations where your agent completely falls apart and your guardrails don't help. And I do want to call out here that the OpenAI guide specifically covers guardrails the best in my opinion. And they even talk about the different types of guardrails here

**[0:12:27]** on page 26. Definitely worth reading into this if you have a system where for example you have to filter out PII or maybe you just want relevance classifiers for your rag application to make sure that the answer that it's giving based on the chunks it retrieved from rag is actually relevant and that

**[0:12:43]** it is answering the user's question. Those are the kind of things that you want to implement as guardrails. And within one of my previous videos on my channel, one of my more recent ones, I even showed you an example here where we have an AI agent that produces some

**[0:12:56]** output and then that goes to this critic node. This is a guardrail that's going to evaluate. Did the output of this agent match the expectations that I have for this process? And then if it doesn't, it's going to retry. So we have this whole idea of the guardrail looping

**[0:13:11]** back. It's kind of like the evaluator and optimizer pattern that we saw within anthropic here. So it'll loop back to then correct itself and do this any number of times until we have the accepted output. So very very important. Guardrails are the way to make sure that your systems are reliable. And then the

**[0:13:27]** last few things I have here are pretty simple. So we'll get through them pretty quickly. Starting with what it looks like to have an effective AI implementation. And so just like with any automation, you want to start really simple. But then what you want to do specific to agents is have visibility

**[0:13:42]** into the agents reasoning so that you can see into what it is deciding to do. How many times is deciding to use different tools for a given question that you asked it. You also want clear instructions. This is both for your system prompt and then also for the

**[0:13:56]** descriptions that you give the agent for your tools so it knows how to leverage those effectively and when to use them at the right time. And then also these guides, they focus so much on the importance of evaluating your agents. In fact, I've heard it before that building

**[0:14:10]** AI agents is 25% coding or automating and then 75% evaluating because it's easy to get to that first 90% for your agent as far as performance. That's when it's good. But to really make your agent great, you have to evaluate constantly and you have to constantly be tweaking

**[0:14:27]** your tools and your fine-tuning and your system prompt and your knowledge base. So crucial. And then also maintaining human oversight, things like human in the loop to make sure we are a part of the more crucial decisions that our agents are making because you don't want to trust them 100% for a lot of

**[0:14:42]** different use cases. And these guys focus a lot on real world use cases as well. And so I want to cover some of these that they call out really quickly because these are the kind of things that you can implement as quick wins for your business or just automations for

**[0:14:55]** yourself like customer service classifying and responding to queries general business operations like approving refunds, reviewing documents automatically organizing files in your SharePoint or emails that you have in your Outlook or Gmail, whatever that might be. LLM are great at research tasks in general, too. And then we have

**[0:15:13]** our development tools. I mean, we know things like AI coding assistants are just so so powerful. And then last but not least is just general scheduling tasks like managing our calendar planning invites and sending meetings doing a lot of inbox management and also AI agents can be really useful for

**[0:15:29]** managing things within our task management softwares as well like ClickUp or ASA. So yeah, so many different use cases that we can build agents for that they call out. A lot of this is that lowhanging fruit for us to get those quick wins. And then I wanted to remain very framework agnostic with

**[0:15:44]** this guide. So not focusing on specific tools or frameworks, but there are some that are mentioned within these different resources that I want to call out really quickly. So Google talks a lot about different prompt templates in their agent white paper. They also cover Vertex AI. That's their cloud offering

**[0:15:59]** that gives you a lot of powerful agent capabilities right out of the box. They cover tools like Langchain. And then OpenAI talks a lot about their agents SDK and they have a lot of code examples in their guide based on the agents SDK. There are a lot of other really great

**[0:16:14]** frameworks as well like Langraph which I love. Agno Crew AI small agents from Hugging Face, Pideantic AI which is my favorite AI agent framework. So a lot of different ones to look into pros and cons for each. And then the very last final thought that I have to share with

**[0:16:29]** you is that when you're building agents really any automations in general, but this applies especially to agents, you want to focus on outcomes, not complexity. When you're building fancy agents and multi-agent architecture and you're adding in your guard rails and you're doing all this crazy stuff with your system prompting, it can be very

**[0:16:47]** tempting to focus on the complexity. And as you're building things for your company or yourself or your clients, you might present this as like, "Oh, look at how complex this was. Look at how much work I put into this." But really, they just care and you should just care about

**[0:17:01]** the results that you get from implementing this agent into your systems. That is the most important thing. And so, don't fall for the temptation of focusing on complexity just because there are so many cool ways that we can do really fancy things with agents. It still just comes down to what

**[0:17:16]** is your return on investment when you invest monetarily or with your time into building an agent. So there you have it. That is Google's agent white paper OpenAI's practical guide to agents and building effective agents from Anthropic, all condensed down into 20 minutes for you. And if you want to dive

**[0:17:33]** deeper into these topics and building good AI agents, definitely check out Dynamis.ai. It's my community that I started recently of early AI adopters like yourself. So, if you want to transform your career and business with AI, definitely give it a look. And I'll keep putting out more content on my

**[0:17:49]** YouTube channel for these topics as well. So, if you appreciated this content, you're looking forward to more things AI agents, I would really appreciate a like and a subscribe. And with that, I will see you in the next
