---
type: raw-transcript
title: "Are Agent Harnesses Bringing Back Vibe Coding?"
youtube_id: 13HP_bSeNjU
url: https://www.youtube.com/watch?v=13HP_bSeNjU
slug: are-agent-harnesses-bringing-back-vibe-coding
published: 2025-12-17
duration: "0:25:42"
fetched_at: 2026-07-21
immutable: true
---

## Transcript

**[0:00:00]** Recently, there has been a shift in the AI industry that we need to talk about. And that's what I want to cover in this video with you. It's the idea of an agent harness and the promise that comes with it that with a harness, we finally have the ability to execute longunning

**[0:00:16]** tasks with our agents reliably. And so, as an example, with coding agents, using a harness, we can trust it fully with a complete feature implementation, what a lot of people like to call Vibe coding. Now, is that viable right now? Well, that's part of what I want to address

**[0:00:32]** with you because life isn't just rainbows and daisies. There's a lot of nuances that we need to uncover here together. And so, in this video, I want to talk about the evolution of the AI agent architecture. How we got to this point where harnesses are really starting to become the most important

**[0:00:48]** thing. And I also want to talk about why that's the case even though harnesses really aren't a brand new concept. And then of course I want to get concrete with you and talk about what the harness architecture actually looks like. And then honestly most importantly I want to

**[0:01:02]** cover the two big unsolved problems. Why aren't people using harnesses for literally everything right now? Because harnesses, let me tell you, will be a big deal once we solve these things. And I'm going to be focusing on AI coding in this video, but really harnesses apply to using an agent for any kind of very

**[0:01:21]** large task. So let's start with our timeline here. We have prompt engineering which has evolved into context engineering which has now more recently evolved into agent harnesses. And these three ideas are very related because it's all about how we interact with the LLM or the agent. And I know it

**[0:01:37]** feels like a lifetime ago, but GBT3 was released in May of 2020 and the idea of prompt engineering was birthed around then as well. It's all about optimizing the single interactions that we have with LLMs. articulating the instruction set the best we can, getting the best output with the right format, that kind

**[0:01:57]** of thing. And now more recently, prompt engineering has evolved into context engineering. So we're still taking all the strategies that we have here, but we're applying it to entire sessions or context windows instead of single interactions. And so here it is all about providing the right context to the

**[0:02:14]** LLM at the right time. We have this balancing act where we don't want context rot. We don't want to overwhelm the context window of the LLM, but also we do want to be very comprehensive and specific with the instructions that we give the agent. And there are a lot of

**[0:02:29]** strategies that we have for context engineering that I'll cover more when we get into the harness architecture as well because all the ideas that we have with context engineering are very wrapped up in harnesses. And that is a really good thing because this is an evolution versus saying, you know, screw

**[0:02:44]** context engineering, agent harnesses is the new thing. It's not like that because agent harnesses is all about how we can optimize different context windows or sessions and connect them together to handle more longrunning tasks. And so in each individual session, we're still applying all these strategies, but now this is creating the

**[0:03:04]** infrastructure, the wrapper around our agents. So we can have many work in unison on one project with things like checkpoints and handoffs so they can communicate with each other. We have human in the loop. So there are break points for us to validate things as well. So there's a lot of agent self-

**[0:03:19]** validation and human validation that we need in these harnesses so that we can truly trust these longunning tasks. And so I just love how these have evolved into each other, right? Like harnesses rely on everything that we've learned from context engineering and prompt engineering. So this is not a

**[0:03:35]** replacement. So we focus first on optimizing single interactions, then single sessions. Now we are connecting different context windows together with harnesses and there are a lot of really good examples of this. Langchain has built deep agents. Enthropic has their initializer coder architecture for longunning coding tasks. I actually

**[0:03:53]** covered this in a video already that I'll link to right here. And then I'm even working on my own remote agentic coding system that builds harnesses within the Dynamus community. So yes, I am doing a lot of research on this myself because I really do think that this is the natural evolution for AI

**[0:04:09]** agents. And yes, this is not something that is brand new. There are a lot of platforms out there like Langchain deep agents, like Manis, for example, that we had way back at the start of this year. They've already implemented a harness, but it's really just becoming more of a

**[0:04:26]** standard right now that we have this natural evolution for context engineering to agent harnesses and it's going to become like the necessary thing if you want to make the most state-of-the-art agents or if you just want to continue to make your agents and coding assistants more and more

**[0:04:41]** reliable. Because here's the other thing. There's this harsh truth that you and I have to come to terms with. And that is the raw power of LLMs is just simply not exploding anymore like it was the last couple of years. I mean, yeah, the benchmarks are still getting more

**[0:04:56]** and more impressive like with Gemini 3 and Claude Opus 4.5, but really it's the layer around our LLMs, what we build on top of our agents that is making the difference here. the reasoning, memory systems, prompting techniques, tool optimization, everything except increasing the raw power of the LLM

**[0:05:16]** itself. And this is actually a fantastic opportunity for us because this layer on top of LLMs is what we get to create and optimize for ourselves. We can't really make the LLM more powerful. And we definitely are hitting this scaling limit with how far we can push LLMs with

**[0:05:34]** the current architecture. And this sentiment is definitely echoed if you listen to any of the top AI researchers right now. 2020 through 2025 was really the year of scaling, scaling, scaling, seeing how far we can push LLMs with the parameter count and the data set that we're training on, that kind of thing.

**[0:05:51]** But we've hit the limit there. And so now we're back to the drawing board. Kind of the the next chapter of researching for AI. So instead of scaling, we are researching what's that new architecture we shift towards. Maybe something like world models. I'll probably do a video on that as well. Or

**[0:06:06]** just the wrapper on top of LLMs, like exactly what we're covering here with agent harnesses. This is the next unlock for the next level of capability that we have for our agents. All right, so with that, let's get into what an agent harness can actually look like. I want

**[0:06:21]** to get concrete with you and give you some examples. So hopefully after we go over this, you'll really start to see how powerful agent harnesses can be. And so like I said earlier, the whole point of harness is that we are connecting many different agent sessions together. This can be different specialized agents

**[0:06:38]** or just one agent that we're running in a loop because we're clearing the context window periodically so it can handle a longer task and not run into context rot. We're totally overwhelming the LLM. And with the anthropic harness that I talked about earlier, and I'll get into this as an example in a bit, we

**[0:06:55]** actually have both. we have a specialized agent and another specialized agent but then also this second one we are running in a loop for most of the harness and so both are very powerful and your harness might look a little bit different like maybe you don't have an initializer but you have

**[0:07:10]** like three different agents that you run in parallel I mean the way that you structure the architecture for the harness is really depending on the task but what I've seen as the most common architecture is to have some kind of initializer that sets the stage for the longrunning task And then you have the

**[0:07:26]** task agent that is responsible for making incremental progress. And then we're just restarting the context window and having some kind of process for the next agent to quickly catch itself up to speed on where we're at with the task and what comes next. And this process is still using all of the strategies that

**[0:07:43]** we have for context engineering within each individual session. So we have the context engine that wraps our agents and then the harness layer wraps that. So we have memory compaction. We have retrieval. So the agent can pull the documents and information that it needs. We have the idea of isolation with sub

**[0:08:00]** aents for things like research. Offloading information to be used later using something like a database or a file system. Of course we have validation. So the coding assistant or other kinds of agents can validate their own work. This is all important. None of this is going away. And so when I

**[0:08:18]** covered context engineering for the first time and I'll link to that video right here, everything that I covered here is still very very relevant and it is worth repeating again. Agent harnesses is not replacing context engineering. And so you might be very familiar with this diagram here. I've

**[0:08:36]** covered this many times on my channel the past few months. These are all the components of context engineering. So we have rag pulling in documents and external sources of information. Prompt engineering is a part of context engineering as well. We still need to have each individual prompt to the agent

**[0:08:53]** be very optimized. We have memory systems being able to leverage the file system or git logs. And then short-term memory making sure that we are optimizing the context that we have in the current session. All these things are still very very applicable. But now we just have this layer on top to

**[0:09:10]** connect different sessions. And so one of the most important parts of harnesses is guard rails. running these checks at the very beginning or the very end of each agent or some of the agents in a harness. For example, right at the end of the initializer agent, a lot of times

**[0:09:25]** what you'll see is that they'll run a set of checks to make sure that the project or the codebase is really optimized well and set up for the task agents going forward. Also, checkpoints. And so between these different agents having these checks that we run to make sure that the agent is not going

**[0:09:42]** completely off the rails that is very very important. And then handoffs. And so thinking about what kind of context do we need the agent to offload so that the next agent when we start a brand new context window can read that information to quickly catch itself up to speed. And

**[0:09:59]** so this is a really important part of the priming as I call it because think about this. We have to imagine a software project where each new engineer arrives with no memory. And so how do we quickly fill that memory but also in a really concise way with the information

**[0:10:13]** it needs to continue to make incremental progress. And then of course we have human in the loop. Being able to put ourselves in the middle of this long range task when necessary to continue to validate things because yes we have the checkpoints and the guard rails but we

**[0:10:29]** don't always want to trust the AI coding assistant and the system entirely. We want to inject ourselves when we want full reliability. And that's partially why I said there's some nuances here. Like agent harnesses is not enabling vibe coding entirely because there is still a lot of structure that we're

**[0:10:45]** setting up here. And in an ideal world, you are going to have a lot of human in the loop in your process. Still, the sponsor of today's video is out systems and their agent workbench. A full platform for you to build, deploy, and govern AI agents. You get built-in

**[0:11:00]** observability, guardrails, human in the loop, one-click deployments across your environments, everything you need for enterprise agents baked in from day one. And this is super relevant because we're talking about state-of-the-art agents in this video. But there is a reason why most enterprise AI agents never make it past the pilot phase. Prototyping is the

**[0:11:20]** easy part, but when you need an audit trail, the ability to trace what your agent is doing and why in production, that's when things fall apart because that is the difficult part and what outsystems agent workbench provides for us. So the agent workbench is a lowode agent builder. We have these very simple

**[0:11:38]** and easy to extend workflows for all the different components to an agent. And so each one of these steps is actually a sub workflow. We can manage short-term memory, our system prompts, even adding long-term memory and multi- aention workflows. There's so much that we can do to extend this. And at the LLM level,

**[0:11:54]** we can also define the tools that we have and make custom ones. And when we're ready to test the application, we can spin up this web application automatically. It builds this for us. And so, for example, with the simple agent here, I gave it a tool to check

**[0:12:07]** the weather. So, here's the weather in Minneapolis today, for example. And then when we're testing our agent and when we have it running in production, we have the whole dashboard here for all the analytics and everything that we need for enterprise AI. We've got analytics for our agents across our different

**[0:12:22]** environments. We can view all the errors. We can trace every single request. So much more in this platform as well, like being able to manage users for each of our agents and our environments. And so this is what we need for enterprise ready AI. If you want to build agents that actually can

**[0:12:37]** go beyond the pilot phase, definitely check out the outsystems agent workbench. All right, so let's go over an example for what this flow can look like in a harness and then I'll go over some other examples like the anthropic agent harness I've been talking so much about and then some things with lang

**[0:12:53]** chain and manis. And so as an example here for coding specifically, when we start a new session and we have no memory, we need to prime. We first need to understand what has already been built and what is our next task. And so we can read progress files, things that

**[0:13:09]** were offloaded from the previous session. We can look at the git log to understand what has been built. So using git as a part of our memory as well. We can read the codebase and use the codebase as a way to figure out what has already been built. And so we do all

**[0:13:22]** that as our priming. And then we do the checkpoints. So running tests, verifying the environment health, making sure that everything has regression tested before we move on to selecting the highest priority feature and implementing the next thing. So assuming everything is good here, then we're going to pick the

**[0:13:38]** next feature, implement it and do the self validation as well. This is also our opportunity to add in human in the loop. If for example, we want to verify that everything is looking good with this feature before we move on to the next one. And so they can there can be

**[0:13:52]** like a built-in interrupt that adds us into the loop and then we can like check off a box and the system will automatically continue. And so it's not like we have to kick off each step of the way otherwise it isn't really a harness. And so then at the end the

**[0:14:05]** agent will leave clean handoff artifacts. That is again the offloading and then we move on to the next session. And this is just an example of what the flow can look like. But I am very much going off of the initializer task agent architecture. This can of course look

**[0:14:19]** quite different for other sorts of harnesses, but there is a lot that we can take away from this that would apply very universally to any harness that we would make. And so for example, using the file system as memory is a really common thing even for non-coding harnesses. And so like with lane chains

**[0:14:38]** deep agents for example, this is not just for coding. They have context management using file system tools. Also, Manis, they have this really awesome article that I'll link to in the description talking about their strategies for context engineering. And they call out here as well that they use

**[0:14:54]** the file system as context. And so then it's not entirely up to us to make the perfect offloading because we can just look at the codebase to see what the progress has been up until this point as well as some progress files and the git log. So it's very comprehensive what we

**[0:15:10]** have set up here for the memory and covering this example here for an AI coding session flow. It leads us very naturally into covering anthropics harness for longunning agents. So I linked to my video earlier where I covered that already, but I will also link to this article in the description

**[0:15:27]** where Anthropic has open source the harness entirely. I even made my own version where I'm using linear as the place to track the task progression instead of using the local file system like they do. And so I put a lot of work into this just experimenting what it

**[0:15:42]** looks like to take a harness and have the agent update its progress where we already work. Doing this in linear doing it in somewhere else like Slack or ASA Jira we can integrate all these platforms and these harnesses to add in human in the loop and just make it

**[0:15:56]** really really powerful. And so a lot of the concepts that we have in this diagram here will be very familiar to you because it's what we've covered in the last few minutes here. And so when we begin our harness, it's starting from a blank slate. And so we have this

**[0:16:11]** appspec where we define the project we want to create. It's basically a PRD. And so we send that in as primary context to our initializer agent. And so what the initializer agent does is it takes our appspec and then it creates this feature list JSON file. This is

**[0:16:28]** what I translated into linear. It basically outlines 200 plus features that need to be developed and all the validation that we can do for every one of them. It creates a script to initialize the project. It scaffolds out the project and then also initializes the git repo because we're going to be

**[0:16:43]** using git as a core part of our memory for all of our coding agents. And so this is session number one. And then every session going forward is going to be using our coding agent in a loop because this sets the stage and then the coding agents are going to be making the

**[0:16:57]** incremental progress going forward. And then we have our core artifacts here for the offloading and the handoffs. So we have the feature list which we're going to constantly go back and update. This is our source of truth for what has already been built and verified. We also have the claude progress text file. This

**[0:17:14]** is the core file for handoffs. So at the end of every coding agent session, it is going to update this progress file. And this is now one of the first things that we will read with a brand new context window to understand what has been built in the previous session. And so the way

**[0:17:30]** the coding agent works, it is very similar to the process that I outlined right here. We get our bearings or priming as I was calling it. So reading files, looking at the git log, we'll do regression testing, then pick the next feature, implement and test it, and then

**[0:17:43]** finally update and then make that commit in git. And so it's very important to not forget the commit as well because it is such a core part of our memory. We're just going to loop here until all of the tests pass. And so we get to the point

**[0:17:55]** where theoretically the full application is implemented as long as the initializer agent did a good job outlining everything in the feature list. And I ran this for 24 hours straight in my video where I covered this harness. And it literally built a full claw.ai clone. This thing is

**[0:18:13]** working really well. Like we have the settings here. I can switch between themes. I can go between different conversations. I can pin them. I can have them in a folder. I can do a new chat and like actually talk to Claude here. So like it's a fully working chat

**[0:18:25]** application. And I did nothing. It's more experimental. I wouldn't recommend running this harness 24 hours straight with no human in the loop, but I just wanted to see how far I could take it. And it was really cool to watch it like do a bad job, but then like detect that

**[0:18:39]** through validation and then correct and then go on to the next feature and the next session. Like I just watched it rip through this over a day and it was really really cool. And then adapting it to work with linear was also really cool. So like the cloud progress I

**[0:18:53]** turned into this more like meta task that I have in linear. So it like updates this over time and makes comments as it goes through each of the sessions. And so all this is like really new for me and I'm just starting to experiment with harnesses. But yeah, the

**[0:19:07]** power is just becoming more and more obvious for me here especially once we get to the point where we're implementing human in the loop everything like that. And so that kind of gets us into the two unsolved problems here. This is the last thing that I want to talk about with you

**[0:19:21]** because these harnesses are really cool. But at this point, I would consider them more experimental because of these two things. So let's get into that. So the first big problem that we have is bounded attention. This is the idea of context rot. When we add more and more

**[0:19:35]** information into the context window for an LLM, it gets into the dumb zone, as it's been called recently, where the LLM just gets very overwhelmed. And yes, this is the problem that harnesses is aiming to solve. But my argument here is that it is only partially solved. And so

**[0:19:51]** we have a lot of the infrastructure and ideas in place like memory compaction, progress files for offloading, sub aents for isolation, memory handoffs, but I think that it is very far from being optimized. So optimal summarization like for example with the clawed progress in the anthropic harness when I watch this

**[0:20:11]** get created and updated throughout the different sessions a lot of times it's really obvious to me that it was missing core information. So like sometimes the coding agent would do a really good job summarizing its work. Other times it would completely miss things like validation that failed and what it had

**[0:20:25]** to do to correct it. And so like one thing that happens with these harnesses a lot is you'll see a pattern where the same mistake will happen over and over and over again because if the handoff doesn't include how it resolves that then it's just going to propagate

**[0:20:38]** throughout the rest of the system. And so that's also why human in the loop is really important for these things. And then also the idea of predictive context like Mandis says in the article I showed earlier you can't predict which observation becomes critical 10 steps later. Now, you can try your best to

**[0:20:55]** predict, but this is definitely the hardest engineering problem that we have for harnesses overall. Like trying to make that prediction and prompt that for our coding assistants or other agents like what do the sessions coming after need to actually know from what you did and that also goes into cross- session

**[0:21:12]** continuity. So, yeah, bounded attention is what harnesses are trying to solve, but we're just not fully there yet. And then we also have the issue of reliability. Because here's the thing with harnesses, it is basically a multi- aent architecture where we are running dozens and dozens of agents together to

**[0:21:29]** accomplish a single longunning task. And so a lot of times AI agents will have something like a 95% reliability. Seems pretty good on paper, but the problem is this is reduced to a 36% reliability for the entire system if we are running 20 steps because the errors compound on

**[0:21:47]** each other. or maybe better put the error rate compounds on each other. And so I'll actually show you this by going to a calculator here that if we have a reliability of 0.95 or 95%. Well, to calculate what the reliability is of the system over 20 steps, we take that

**[0:22:02]** number and we put it to the power of 20. That's what gets us that number right here. So I'll multiply it by 100. That is the 36% that I'm referencing in the Excal diagram right here. So, if we were to have a harness that can truly do something completely end to end with us

**[0:22:18]** trusting it entirely, like Vibe coding, then we would need like 99.9% reliability for this system, especially if it's like 200 steps instead of 20. And man, let me tell you, we are not going to get to the point where a coding agent or any kind of agent is going to

**[0:22:33]** be 99.9% reliable. And so, this is partially solved because we have the checkpoints. So, the agents will self- validate. we can automatically roll back like when we have git integrated with a coding harness. We got the structure artifacts for handoffs. Like there's a lot that we have here in the infrastructure. But the

**[0:22:50]** main thing that we're missing is smart checkpoints and human in the loop. We need to have the right autonomy balance. And so the answer here, what I haven't really seen developed well in these harnesses is having strategic human checkpoints. So we still want things to be as autonomous as possible. So, it's

**[0:23:07]** truly a harness that is leveraging different agents for a longunning task, but we need easy injection points. So, there's just a quick like let's check a box or maybe validate the website if we're cloning claw.ai, like let's do something really quick and then have the system automatically restart and go to

**[0:23:24]** the next session once we give the okay. And like that's the kind of thing that I'm putting a lot of time into researching myself because if we can have really powerful human in the loop built into these harnesses, the sky is the limit for what we can accomplish.

**[0:23:38]** Like honestly, I would be so bold as to say that if we solve these problems and we have a very engineered harness that has human in the loop and all of the self- validation, then vibe coding is viable. Now, it's going to look a lot different because the general idea of

**[0:23:54]** Vive coding is that you just give all power to the coding assistant. You trust it entirely and you're not engineering a system. And so, it's very different here because yes, we are delegating all coding to AI if we build a very powerful harness. But the system is heavily

**[0:24:09]** engineered with human in the loop at a lot of different stages. And so, I'm sorry if you think that I'm going to tell you that like we can vive code any feature on any codebase ever. It's more like yes, we can if we have engineered things in a lot of detail with a harness

**[0:24:25]** like I'm talking about here. And like fundamentally, this is not an easy problem for us to solve. Like I said, things like predictive context are basically impossible. And so we just have to get as close to perfect as we can. But I really do think that like 2026 is going to be the year of agent

**[0:24:41]** harnesses, right? Like 2025 was the year of vibe coding and agents. Now we're going to make things more reliable with harnesses. human in the loop and I am very excited for that. So that my friend is everything that I have for you on agent harnesses and I know it takes some

**[0:24:56]** imagination right now to see how far we will be able to take harnesses but I firmly believe that this is the unlock for us to be able to delegate 99% or more of coding to our coding agents and applying this to really any kind of long-running agent like I've been

**[0:25:13]** talking about as well. And so yeah, vibe coding, it's going to sort of become viable but also look a lot different because we are engineering the system, engineering the harness, but we aren't going to be writing most of the code in the very near future. That's what I

**[0:25:27]** think we have in store for 2026 and I'm looking forward to that. So, if you appreciated this video and you're looking forward to more things on AI agents and AI coding, I would really appreciate a like and a subscribe, and I will see you in the next
