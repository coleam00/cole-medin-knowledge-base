---
type: raw-transcript
title: "Pydantic AI 2.0: The New Best Way to Build AI Agents is Composing Capabilities"
youtube_id: PY7xIxybYNc
url: https://www.youtube.com/watch?v=PY7xIxybYNc
slug: pydantic-ai-20-the-new-best-way-to-build-ai-agents-is-composing-capabilities
published: 2026-07-10
duration: "0:15:02"
fetched_at: 2026-07-21
immutable: true
---

## Transcript

**[0:00:00]** Pidantic AI has been my favorite AI agent framework for a long time now. I've been making content on it since January of last year. They are always leading the industry, making it really easy to build AI agents, but giving you the full customizability and control at the same time that you really need to

**[0:00:17]** ship production agents. And so that in my mind is what makes them stand above other frameworks like Langchain and Crew AI. And Pideantic AI has done it again. They just put out their 2.0 0 release and this is a big evolution in the way that we build AI agents. This version of

**[0:00:35]** the framework centers around a single primitive called the capability. This is the main thing that we build out now when we're creating our AI agents. And I just love this. It's such a beautiful simplification that at the same time encapsulates everything that you need for an agent. And it accounts for

**[0:00:52]** everything the industry has been converging on recently for the different components that go into building agents like our hooks and our guard rails and our skills and MCP servers. And I love this so much that I wanted to make a video dedicated to covering this idea of the capability and the 2.0 release. Now,

**[0:01:09]** Pyantkai, they're not sponsoring this video. And I don't normally make a video just on an update to a framework, but this is good enough where it it feels like we're starting to see this shift now, this powerful evolution of how we build our agents. So, let's get into

**[0:01:23]** this here. So, a capability bundles an agent's instructions, tools, life cycle hooks, and model settings into a single composable unit. So, a whole extension can reach every layer of the agent through one concept, which this is a little bit of word salad to be honest. Basically, what they're saying here is

**[0:01:40]** no matter the responsibility you want your agent to have, it's going to be comprised of a set of tools so it can reach the outside world and instructions and guard rails to guide it. And so whatever that is, we can package it all together as a single capability which is

**[0:01:54]** a single input into defining our agent. And so now our AI agents can be thought of quite simply as just a set of these composable units, these capabilities. We're combining all of them together to give the agent all the responsibilities that we want for it. And the best part

**[0:02:11]** about this, because it's so composable and really it's just like piecing Lego blocks together, we can very easily reuse these capabilities between the AI agents that we have for oursel or our business. And it's also useful to think about capabilities as the layer above MCP servers. If you think about it, MCP

**[0:02:29]** is similar. It's a packaging of tools that you can hand to your AI agent. And it's very easy to share it between AI agents as well. That's one of the main benefits of MCP. And MCP servers are a subset of what you've added into a capability like we're seeing in the

**[0:02:46]** example right here. But also, capabilities are a lot more than just the arm of the agent, aka the tools. It's also the instructions and the settings and the hooks and the guardrails, how we want the human to interact with the agent and inject things. Like all of that is packaged

**[0:03:00]** together here. And the other thing I want to say is like none of this is new, right? Like underneath the capability, everything that comprises the capability is things you're already working with probably especially with your AI coding assistant like your skills and hooks and things like that. But it's just the way

**[0:03:18]** that we're simplifying bringing them into an AI agent framework that I think is such a beautiful thing here. So with this new release and the idea of the capability, it feels like Pantic AI has gone from falling behind a little bit to leading the industry yet again. And the

**[0:03:33]** reason I say they were falling behind a little bit is really just because of the rise of the coding agent SDKs. It is so incredibly easy now to just build your AI agents, especially your more personal agents, on top of something like the Clawed agent SDK or the Codeex SDK. They

**[0:03:50]** are slower and more tokenheavy than a traditional framework like Pideant AI. So, there's definitely trade-offs. I've covered that on my channel recently as well, but especially for more personal use cases. Generally, when you build an AI agent, you're just going to be using something like this or maybe just

**[0:04:05]** building something directly into your Hermes or OpenClaw. And so there's just been a smaller subset of agents that are still useful for Pyantic AI, especially because these agent frameworks, they integrate so well with the different primitives we've already been talking about like hooks and sub aents and MCP

**[0:04:23]** servers. Like it's so easy to incorporate these things in. I mean, you can see the examples here of how it kind of looks a lot like capabilities where it's just a couple of lines adding in an MCP server or if we want to add in a hook, for example. And so Pantai has

**[0:04:36]** caught up to this, right? Like it's very easy to add in these capabilities now. And I would argue it's even easier. Like PantiAI is like the winner in my mind right now. The sponsor of today's video is Nimbleist, a free open-source visual workspace for building with cloud code

**[0:04:51]** or codecs. If you spend all your time in the terminal like I do, you know the pain of your agent making a ton of changes across your project and it becoming hard very quickly for you to track what's actually happening. Nimble wraps your coding agent in an actual

**[0:05:07]** workspace. And so as your agent is making changes, you see it as red and green diffs. And this applies to code, markdown, even diagrams, everything rendered visually. Plus, you can revert and accept any changes to your files and even annotate things. So your agent will address your feedback directly. And my

**[0:05:25]** favorite part about Nimble is the agent manager. Here I can manage many coding agent sessions in parallel, all operating in isolation. I also have a conbon board so I can view the stage that each one of the agents is in. Click into it to also view the conversation

**[0:05:40]** and then also for any of the changes that it's making I can click into any of these files. So I can look at the individual diffs as the agent is operating on my codebase. It's just so easy to navigate between the sessions and all the changes that are happening

**[0:05:52]** in my project. and all the connections that are made under the hood between the different files and agents that are running, all the tasks that are being taken care of. All of that is not just for me, it's also for the agent. It's able to traverse through a graph that it

**[0:06:05]** builds internally to get a holistic picture of everything that's happening in my project. And you know, I always love covering open- source projects and Nimbleist is seriously impressive. Definitely worth trying out. And it is 100% local. Everything lives as plain markdown on disk. There's no lock in, nothing you have to sign up for. I'll

**[0:06:23]** have a link to it in the description. All right. Now, to make the idea of capabilities really concrete for you really fast, I have this example. I have this GitHub repo, which of course I will link to in the description, where I built a pyantic AI agent both with 2.0

**[0:06:37]** and 1.0. So, we'll go through both and then I'll demo the newer one as well. And you can use this GitHub repo as a template or starting point for your coding agent to build a podanti 2.0 agent for yourself. Or the other thing you can do, which I would highly

**[0:06:52]** encourage you to try this, is to just give your coding agent the capability documentation directly. In the 2.0 launch article, they literally say right here, just point your coding agent at the capabilities docs, what we're looking at right now. I'll link to this in the description as well. And it's

**[0:07:08]** interesting. You can see like, man, this is a very long documentation page. Like, holy cow. And that just goes to show like how much customizability and control we have with Pinantic AI. But yeah, I say that because this is not meant for a human to consume. At least I

**[0:07:24]** don't really think so. Like this is more meant for a coding agent to consume to help you build it up. Like I really don't think you should be writing the Pantic AI agent code by hand anymore. I've not done it for over a year now. Please don't spend your time on that.

**[0:07:39]** And so we're going to look at the code in a little bit here just to explain some of the ideas, but I'm not going to get technical or in the weeds because I don't expect you to understand it 100% or write the code yourself. I just want to illustrate the points here of how

**[0:07:52]** we've evolved the capabilities and what they're really comprised of. All right, so what you're looking at right here is a Pantic AI 1.0 agent. Now, it's always been a fantastic framework. So, there's not a ton of critiques here. Like, I still wouldn't mind building my AI agents in this way. It's relatively easy

**[0:08:08]** to define your tools, add them into your agent, add in the system prompt and the model settings. It's still a good experience. But what you can see here is when we define our AI agent, it really is just a hodgepodge of all the instructions and tools that we have for

**[0:08:22]** it. There's no organization and there's no composability. We can't take a subset of the capabilities out of this and easily add it into another agent. We have to redefine and recreate things. And so again, it's a good experience, but it could be better. And that's what we have now with Panti 2.0. Take a look

**[0:08:41]** at this. So we have this kind of larger constructor here. Look at how simple this is now. So we have our model that we're specifying for the agent overall and then everything else is just a set of capabilities because this includes the instructions like we had to define

**[0:08:57]** right here and it includes the guardrails and hooks and tools like even more than I defined right here. We can package up in a single capability and then we can reuse it between our AI agents. Like this first one is a support agent. So it needs to access the

**[0:09:11]** knowledge base like perform rag in our database and then also be able to escalate things to a human. And then imagine at the front of your platform you have the FAQ widget where there's no escalation here but it still needs access to the knowledge base to answer basic user questions. And so here we

**[0:09:27]** don't have to rebuild anything. And as we evolve our knowledgebased capability over time like improving the instructions, guard rails and tools both the agents benefit from it at the exact same time. And then not to spend too much time in the code but just to show you how a capability is defined very

**[0:09:43]** quickly. We have our instructions. We have the tool set. So we just have a search knowledgebased function for our knowledgebased capability. The model settings and then a very simple example of a hook. And so this is just like in cloud code or codeex where we have a pre-tool use hook. We want some kind of

**[0:09:58]** deterministic action for the sake of security or guiding the agent properly whatever that might be. And then we have our escalation capability for the support agent defined in a very similar way. And so we'd have all of the core primitives there. We could add in more things like MCP servers as well, like we

**[0:10:13]** saw with that GitHub example. Very easy to add in whatever the agent needs wrapped up in this capability. And if that's not enough, one of my favorite parts of capabilities is you can implement the idea of progressive disclosure. So just like with skills in cloud code, codeex, GitHub, copilot, you

**[0:10:30]** have the ability to give a brief description of the capability. So the agent has a catalog of what it can lean on, but it's only going to load the full instructions for the capability when it decides it actually needs it. And the reason that's important is because that

**[0:10:45]** way we can supply a bunch of different capabilities to our agent. whether it's the ones built right into Pantankant AI like these or a custom one we make, we can give it dozens, maybe even hundreds of capabilities and not overwhelm the LLM because it only has to really dig

**[0:10:59]** into and leverage the ones that it needs based on the user's current prompt. And so to show you an example of that, here I have the agent spun up in the CLI and I'll ask it a question. Can I connect orbit to Slack? And so this is something

**[0:11:12]** where it really doesn't need to leverage the escalation capability at all. I sure hope it doesn't. It just needs to search our knowledge base. And so sure enough, it says Orbit doesn't have a native Slack integration yet, though it's on the road map. And it even references a

**[0:11:25]** document that it found in the knowledge base. And so you can see that out of the capabilities that I gave it, it leveraged the thinking one that Padantkai supplies with the framework. And then it also leveraged the custom knowledgebased one. So it loaded the instructions for both of these and then

**[0:11:39]** used the tools there. like it used the search knowledgebased tool and did some reasoning, but it didn't leverage the escalation at all. And that's good. That wouldn't be worth loading those tokens in because it's going to make our agent slower and make the call more expensive. But let's say someone comes to the

**[0:11:56]** customer support bot where they actually have a concern that needs to be escalated to a human. Like, I was charged twice this month for my subscription. Can you refund the duplicate charge? I mean I hope your platform doesn't do that but just an example here where we need to leverage

**[0:12:08]** the escalation capability. And so now we are going to load it. There we go. We've loaded the escalation. Your support ticket has been created. Your ticket ID is blah blah blah. I mean none of this is real. This is just mock for a demonstration. But you get the idea. The

**[0:12:20]** agent is choosing the capabilities that it needs. And so not only is it more composable in order for us to share this easily with other agents, but it also means that our agent in the current conversation can be very focused to the responsibilities that it actually needs to lean into for this conversation. All

**[0:12:36]** right, so the last thing in this article here that's definitely worth covering is the idea of the harness and the leaner core for Panti. And I love how they're evolving the framework in this way. Essentially, there are two layers of capabilities in the framework. The first layer is the capabilities that they

**[0:12:53]** consider critical to most AI agents. Like most of the time when you build an agent, you're going to want thinking. You're going to want web search. You're going to want tool search that gives us that progressive disclosures to make us so you can really scale your agents. This is the first lane. And so you

**[0:13:08]** import these things from Pantanki, they're supported directly. They're part of the lean core. It's very easy to just add these in as capabilities. The only thing you really have to tweak is maybe a couple of parameters like this one for thinking. And then our other lane is the

**[0:13:21]** harness. These are the capabilities that Pideantic AI wants to support directly but doesn't consider critical for a majority of AI agent use cases. And so code mode is a good example. This is giving your agent the ability to write and execute code in a sandbox. And so yeah, pretty important for a good number

**[0:13:39]** of agents, just maybe not a majority of them. And this is a really cool capability by the way because Pyanticai or the Pyantic company, the parent company is working on their own lightweight sandbox called Monty, which is open source as well. It's fascinating. I could do a whole video on

**[0:13:54]** Monty, but outside of the scope what we're covering right now, you get the point. Like these kinds of capabilities, other like third-party ones they want to support that falls under the harness. It's the wrapper above the lean core of Panti, which I think, you know, is why they're calling it a harness. So really

**[0:14:11]** cool. I love this cuz then they keep the the core framework really lightweight while still giving you a lot of out of the box things if you want to reach for that. And so there you go. That's everything in the Panti 2.0 release and the new idea of the capability being our

**[0:14:23]** one primitive for building agents. It's a simplification without reducing how powerful our agents can be with Pyantkai. And so I encourage you to just play around with this. I mean I'm using Panti all the time still. It's something where when you want to deploy an agent to production and you have other people

**[0:14:40]** using your agent, you can't just lean on those coding agent SDKs or something like Hermes or Open Claw. You need a framework. Pantic AI really is my go-to. And so I'm planning on doing more content on Pideantic AI as well. And so if you appreciate this video, you're

**[0:14:52]** looking forward to more things on building agents and AI coding, I would really appreciate a like and a subscribe. And with that, I will see you in the next
