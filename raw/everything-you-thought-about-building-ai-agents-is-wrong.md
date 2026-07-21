---
type: raw-transcript
title: "Everything You Thought About Building AI Agents is Wrong"
youtube_id: gmaHRwijOXs
url: https://www.youtube.com/watch?v=gmaHRwijOXs
slug: everything-you-thought-about-building-ai-agents-is-wrong
published: 2026-03-25
duration: "0:15:53"
fetched_at: 2026-07-21
immutable: true
---

## Transcript

**[0:00:00]** These days, the only AI agents that people seem to care about anymore are AI coding assistants. No one seems to cover anymore building agents with Langchain or N8N or Pantic AI. If you follow mainstream YouTube or LinkedIn, it just seems like these frameworks don't matter anymore. And honestly, I've kind of

**[0:00:18]** fallen into this camp myself. I used to cover all the time building agents with Pantic AI and N8N and the OpenAI agents SDK, building local AI agents. I was all about this. But then my channel has definitely shifted a lot more towards just using AI coding assistance effectively. That's just what is the

**[0:00:37]** most relevant right now. And a lot of these coding agents have released SDKs so we can build our own agents on top of all the power they give us out of the box. And so there's this big narrative right now that we don't need these frameworks anymore. Let's just build

**[0:00:50]** everything on top of the cloud agent SDK. And that is actually kind of true for some use cases. for these, everything you thought about building AI agents needs to be thrown out of the window. But then for other use cases, this isn't true at all. So there's a lot

**[0:01:05]** of nuance that we have to cover here. If you look at all of the business use cases out there with the billions of agents that are being built, a lot of them, maybe even a majority, are still being built on top of these more classic use cases. But then some are

**[0:01:19]** transitioning. It's making more sense to just build them right on top of these SDKs. So I want to cover this nuance with you. When it makes sense to build on top of the SDKs, when it makes sense to use a framework, there are some other important evolutions we have to talk

**[0:01:32]** about as well, like relying a lot more on skills now and different ways of performing rag. I want to cover all this and make the decisions very easy for you. All right, so let's start by talking about the old way of building AI agents. A lot of this still applies, but

**[0:01:48]** every agent was built this way in 2024 and 2025. So, you'd start by picking your framework. All of these are valid. There's honestly way too many options out there, but you just pick the one that you're the most comfortable with or your organization uses. And then you define the tools for your agent, all the

**[0:02:05]** capabilities like searching through a file system, accessing your inbox, that kind of thing. And then from there, this isn't a hard requirement, but most AI agents, especially back then, had some kind of rag. So you define your chunking, embedding, and retrieval strategy for your agent to search through a knowledge base. And then

**[0:02:23]** finally, you would wire up the agent loop. So state and memory management, things like short-term memory, being able to store all your conversations in a database. And of course, I got some examples here to go with everything that I'm talking about in the diagram. So I'll link to this repo in the

**[0:02:37]** description. I want to start here with like the most classic rag agent ever. Not that these ideas have gone away, but this is just how we would see almost every single agent defined in 2024 and 2025. So you'd start with your agent definition using a framework like Pineant AI. You define your model, your

**[0:02:55]** system prompt, the tools like this is a tool to search our knowledge base with rag cuz rag was in almost every single agent. So you'd have your chunking strategy and your embedding strategy and your ingestion pipeline. There was a lot of code here. And so within our database

**[0:03:10]** like I love using neon for my Postgress database. I still do for a lot of my agents. We have our documents here and then we have our chunks a lot of chunks. We'd manage all of our messages and sessions. Everything for our agent was managed in our own database. This is the

**[0:03:27]** way that it was done before all of the time. Now the point I'm trying to make here is a lot of times that is still necessary but there is a lot of glue code to create the agent infrastructure ourself. There is a lot of complexity there and so a lot of people are

**[0:03:41]** shifting over to using the batteries included SDKs. So building non-coding agents on top of a coding agent foundation with something like the claude agent SDK or the codeex SDK. And the beauty of using this as a starting point is there's a ton of prompting and tools that are built into the solution

**[0:04:01]** for us already. And they manage the conversation history for us. So we don't even have to store that part in our database. So it just gives us a launching pad and we have support for skills and MCP servers. Those are the newer ways to build tools into our

**[0:04:16]** agents as well. And so it's not that you'll use these all of the time and I'll cover that in just a second here. But it's so much easier to build agents on top of these SDKs versus doing it the old way, building with one of these frameworks. Take a look at how simple

**[0:04:32]** and powerful this is. Now I have my entire AI agent using the Claude agent SDK in a single TypeScript file and instead of defining my own AI agent, I just call right into Claude code and I define all of my options like the tools that it's allowed to use. So the ones

**[0:04:48]** that I want to leverage that are built right into the SDK. Also, I have sub agents that I have defined here. So we're adding in a lot more than we didn't even have in the other agent. MCP server, so I can build my own custom tools. So instead of defining the tools

**[0:05:03]** directly into our agent, we can create them as MCP servers, so they're a lot more reusable. We can do the same thing with skills. I have skills built into this agent as well, so it can generate powerpoints for me. There's actually more built into this agent, and it's

**[0:05:16]** less code overall. We don't even need the rag pipeline and everything because for a lot of these Claude Asian SDK agents, you're just going to rely on the file search capabilities built right into the SDK. We can have hooks. We can set the permissions. We can build our

**[0:05:32]** own system prompt. We have everything that we had before and more. And if I really wanted to use rag still and we might I'll talk about that in a little bit as well. We can just include that through skills and MCP servers. So I hope you can see how powerful it is to

**[0:05:48]** use these SDKs. It simplifies things so much for us because we're building on top of these tools that are powerful. There's so much attention going to these coding agents for a reason. And this is exactly what I'm using for my second brain. So I'm using the Claude agent SDK

**[0:06:04]** for the whole heartbeat system that I built for my own second brain inspired by OpenClaw. It handles all my integrations and everything I wanted to take care of. It builds memories over time. It does daily reflection to basically learn from its work and my requests over time. This entire thing is

**[0:06:21]** using the Claude Asian SDK, which by the way, if you're interested in learning how I've built my second brain using the Claude Asian SDK and Claude Code, I'm hosting a 4hour workshop in my Dynamis community Friday, April 3rd at 11:00 a.m. Central time. So, if you want [snorts] to save yourself hours and

**[0:06:39]** hours every single week building a second brain on top of Cloud Code, definitely come be a part of the community and join me for this workshop. And building a second brain with the cloud agent SDK is just one of many very powerful use cases. However, there are some big limitations with these

**[0:06:56]** batteries included SDKs. This is what's going to lead us into the importance of still building a lot of our agents with these frameworks. So, three key limitations that I want to hone in on with you right now. The first one is that these SDKs are significantly slower than what you can build with these

**[0:07:15]** frameworks. And the reason for that is there's a lot of reasoning overhead because there's so much built into these SDKs out of the box for you. So the convenience of having all these tools and support for things like sub agents and skills and the prompting that's already there for you, like all that

**[0:07:30]** makes it very easy to work with these tools, but it means that you're coming into building your agent with something that's already a bit bloated and that also makes it more tokenheavy. And so these two very much go hand inand. And then it's also a bit more non-deterministic because there's a lot

**[0:07:46]** of things that are managed for you. So it's non-deterministic in the sense that you don't get to define exactly how your agent operates quite as much. When we're building with a framework, we're more building from the ground up. So any kind of use case where speed or cost or

**[0:08:02]** utmost flexibility is extremely important, that's when you want to build on top of a framework like Panti. I'm still using Pideantki all of the time. Building with these frameworks is what's going to allow you to build agents with sub-second response times, the most flexibility possible because you're controlling everything, even the

**[0:08:20]** conversation history. For a lot of these production agents where you need a lot of observability and control, like being able to store the message history yourself and manage that yourself, you can't be using something like the Cloud Agent SDK cuz that's just not an option for you. Now, besides the obvious speed

**[0:08:36]** difference between the frameworks and the SDKs, there's one other big reason why most of the time when you have an agent deployed to production, it's going to use a framework instead of the SDK, and it is all about cost. Like we talked about earlier, these SDKs are very

**[0:08:52]** tokenheavy. So, most of the time when you use them, you're going to be using your subscription, like your anthropic subscription or your OpenAI subscription. But you're only allowed to use your subscription when it is just you interacting with the agent. Otherwise, it is a violation of the terms of service for any of these SDK

**[0:09:11]** platforms. And so, if you have multiple people using your agent in production, you have to use your API key. You have to pay an obscene amount for API costs. So, that's really another limitation for these SDKs here. So, that's why I usually use a framework. So, it's going

**[0:09:27]** to be a lot more cost-effective. you can really use it at scale and not worry about burning millions and millions of tokens. And using these frameworks, you still do have the ability to include all these modern techniques like skills and MCP servers. So, it might be a bit more

**[0:09:43]** work to set it up, but it's still very realistic. And let me show you this with an example. Actually, one of the things you might think is missing out of the box for these agent frameworks is support for skills. And so, that's the main way to give capabilities to our

**[0:09:57]** coding agents. now and we're just starting to see it added into these agent frameworks. And so what I did, I'll link to a video right here where I covered this more in depth, is I created a Pantic AI agent where I added in my own support for skills. So you have your

**[0:10:11]** skills directory here with all your skill.md files. Everything works the exact same as it would in in Cloud Code, but now we have our own custom agent where we have full control. It's going to be a lot faster and more token efficient. And so this setup looks pretty similar to the very first rag

**[0:10:26]** agent example that I gave. We define the model, the system prompt, the tool set here, but the tools are more about loading the skills. Now, this is the most modern way to add capabilities into our AI agent. So we have a dynamic system prompt where I basically describe

**[0:10:42]** to the agent, here are your available skills, and I load it dynamically from the skills directory. And then the rest of the system prompt is just describing to the agent how to leverage these skills. And so, for example, going into the agent right here, I just have a

**[0:10:54]** simple CLI. I can say, "What is the weather in New York?" And just like Cloud Code, this agent is able to call a tool to load the skill. So, it brings in the skill.md, which gives it instructions for how to make the API calls. And then we get the current

**[0:11:09]** weather in New York. But take a look at how fast that was. That would be take at least 10 seconds to get an answer from the Cloud Asian SDK just because of how bloated it is. And so it's very easy to build any capability you need into your

**[0:11:22]** own agents, especially with the help of AI coding assistance now. So sometimes you just want something out of the box. The cloud agent SDK is great. Other times you need that speed and scalability and it's not going to be that difficult to use a coding agent to help you build this all yourself. I use

**[0:11:38]** cloud code to help me build this Pantic AI agent. So with all of that context setting the stage, I now want to cover the super simple decision framework for you. Should you go with an SDK or a framework? So, we'll talk about this and then I'll get into rag because that's

**[0:11:52]** really the last component that I haven't hit on too much that I said was a part of the old way. It's still relevant, but then also some strategies with existing tools that replace it. We'll talk about that in a second. But for the decision framework here, it really just comes

**[0:12:05]** down to two questions to ask yourself. Who is going to use your agent? And what is your tolerance for things like speed and scale? If it is just you using the agent and some delay is okay, you don't need to scale, then I would highly recommend going with the cloud agent SDK

**[0:12:21]** or codeex SDK, something out of the box that gives you a ton of power and you have to worry about less of the infrastructure. But if a lot of other people are using your agent, you're deploying it to a production platform, it needs to scale and be fast, then you

**[0:12:36]** still should go with, you know, the classic way of using a framework like Pinantic AI or Langraph. And in the end, you do want to just start with the simplest implementation. So you won't go the other way, but sometimes you'll start with the cloud agent SDK just to

**[0:12:50]** test some tooling through skills or MCP and then you would transition to a pinant AI agent once you need to scale. So there is a little bit of like you can try with both, but usually this decision is going to make it very obvious for you right when you're starting with your use

**[0:13:06]** case. So I hope this decision framework is helpful for you. The last thing I want to talk about is what happened to rag. Why are so many coding agents and other agents not using traditional rag as the default playbook anymore? A lot of people are saying that rag is dead.

**[0:13:21]** So I want to clarify this for you right now. So in 2024, no one really questioned rag. Pretty much every single agent was using semantic search as a way to access external information. But then in 2025, people started to question this because we were relying a lot more on

**[0:13:39]** file search. Coding agents especially stopped using vector databases. They were using tools like Grep. Now that's why we see all of this built directly into the SDKs for smaller corpuses of knowledge. It was proven last year that file search actually outperforms rag or classic semantic search. Llama index did

**[0:13:59]** a study. Claude code a lot of these coding agents switching away. A lot of that was pointing towards the direction of rag is deaden. But there's a lot more nuance to this than people realize because for larger knowledge bases with thousands of documents, semantic search is still more accurate and way way

**[0:14:15]** cheaper. And so now we've kind of gotten to a middle ground this year with a gentic rag. We give our agent the ability to perform both semantic search and other kinds of searches like GP and keyword search. Graph rag is really popular as well, especi especially for massive code bases or projects with many

**[0:14:33]** different code bases. So at an enterprise level, rag is still used for AI coding. And then for most AI agents, we still need rag to access our knowledge bases. File search is not enough. It's a good starting point and it works better for smaller knowledge bases, but you still need that for a lot

**[0:14:51]** of your agents. For a lot of my AI agents, I'm still spending a good amount of time in my database trying different rag strategies, building around semantic search. Even with the Claude agent SDK, building semantic search through skills and MCP servers and second brains are a good demonstration of this. I've built

**[0:15:09]** mine on top of the Cloud Asian SDK, but I use both the capabilities built right in and then also I have my own rag setup that's actually inspired by OpenClaw also built in for semantic search. So to summarize everything here, match your tool for your use case. There are a

**[0:15:26]** million use cases that are great for the SDKs and just as many if not more where you want to use a framework and build it more from the ground up. And I hope this decision framework has made it really easy for you to think about that for your own AI agents. And so if you found

**[0:15:42]** this helpful and you're looking forward to more things on building AI agents and agentic coding, I would really appreciate a like and a subscribe. And with that, I will see you in the next
