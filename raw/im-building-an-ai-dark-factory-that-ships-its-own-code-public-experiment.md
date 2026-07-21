---
type: raw-transcript
title: "I'm Building an AI Dark Factory That Ships Its Own Code (Public Experiment)"
youtube_id: 6woc6ii-zoE
url: https://www.youtube.com/watch?v=6woc6ii-zoE
slug: im-building-an-ai-dark-factory-that-ships-its-own-code-public-experiment
published: 2026-04-15
duration: "0:25:13"
fetched_at: 2026-07-21
immutable: true
---

## Transcript

**[0:00:00]** I'm starting a public experiment where I am going to be pushing the limits of what is possible with AI coding assistance. Building what is known as a dark factory. Sounds very ominous, I know, but it is super cool. Not 100% practical yet for production code. We'll talk about that. That's why it's called

**[0:00:19]** an experiment. But this really is a glimpse into what is going to be possible with our code bases at some point thanks to AI. What we're doing with a dark factory is building an entire system where we hand the reigns of a codebase over to AI entirely. So

**[0:00:36]** our coding agent is going to manage the planning, implementing, pushing all changes and pull requests right to production. There is no human in the loop. And on my channel, it's funny cuz in my bio, I've always said, "Join me as I push the limits of what is possible

**[0:00:52]** with AI." Literally, ever since I started my channel in 2024, I've had this line. And I feel like I've done a pretty good job living up to it over the last couple of years. And right now, it's just another example where I'm continuing to do things that like this

**[0:01:07]** isn't brand new. The Dark Factory isn't brand new, but no one's ever really run a public experiment before, which is why I'm so excited to start this. And so I've actually already done a couple of live streams where I've been building out the system using Archon and Claude

**[0:01:22]** Code and Miniax M2.7. I'm going to be doing a lot more live streams as well, just building this in public. That's part of what makes it a public experiment. And so in this video, I want to talk about the origins of the Dark Factory and then get into my

**[0:01:36]** architecture, exactly how I'm building a system to make this crazy idea at least somewhat reliable. We'll see how the experiment goes as I build it out. I'm going to get to the point where this application will be deployed to the cloud. You can visit it, try it out

**[0:01:50]** yourself, and then file issues that will automatically be handled by the dark factory. It's going to be a very cool setup. I'm not done with it yet, but I want to build in public, show you what I'm working on and what I have built already. So, the term dark factory was

**[0:02:03]** actually coined over a couple of decades ago when we first had what's called lights out manufacturing. So, these physical facilities where we don't need lights because there are only robots, right? Why should the company pay the electric bill to keep the lights on when there's nothing in there that actually

**[0:02:19]** needs to see? We've had robots building robots ever since around 2001. That's what we're looking at right here. And so, yeah, Dark Factory first actually referred to physical facilities and then Dan Shapiro was the one to apply this to code bases and generative AI. And before we get into my whole architecture for

**[0:02:37]** the dark factory, which I think you'll find fascinating, I do really want to cover the different levels of using generative AI for coding, which obviously ends in the dark factory. This is the ultimate use of generative AI completely giving the reigns of our codebase over to it. So, I want to talk

**[0:02:54]** about how we evolved to this stage and kind of where we are right now for production code and then where I'm going with this experiment. And I really love Dan's blog post here because he gives a really good analogy comparing the different levels of self-driving cars to using generative AI for coding. And so

**[0:03:11]** he starts with level zero, which he calls spicy autocomplete. Not really sure why he calls it spicy, but hey, I'm here for it. This is where AI serves as a reference tool or enhanced search. So like a smarter Stack Overflow. If you come from an engineering background, you've probably used Stack Overflow way

**[0:03:27]** too much and now you're using AI coding assistants and leaning on them even more. But the point here is that the developer still manually writes the code. You're just using AI as a consultant. Like, hey, how should I address this problem? Maybe give me this function so I can copy it into my

**[0:03:42]** codebase like you did with Stack Overflow before. And so, as it relates to driving, you still got your hands on the wheel. And maybe it's so manual that it's still stick shift, for example. I think that's what this image is trying to convey here. And then that brings us

**[0:03:55]** to level one, the coding intern. So now you're starting to lean on generative AI for the very basic things like unimportant or boilerplate code. So it's akin to having cruise control for your vehicle. You still are controlling the direction of the car, but at least maybe you have the car maintaining a certain

**[0:04:12]** speed for you without you having to have your foot on the gas or the brakes. And then we go to level two, the junior developer. So when you're really starting to take advantage of AI coding assistance and autonomous coding, this is your introduction level, the junior developer. So at this point, you only

**[0:04:29]** have one hand on the wheel instead of two because you have an interactive paraprogrammer partnership. You're starting to trade off control completely to the AI coding assistant for certain tasks, but you're still writing some of the code yourself. And so then obviously the next evolution is getting to the

**[0:04:46]** point where AI generates a majority of the code base. And so this is actually where I'd recommend you to be when you want to most reliably ship production-grade software with AI because you're handing over the reins, but like this picture shows with the driving analogy, you still have your

**[0:05:03]** eyes on the road. You're ready to course correct at any point. When you really want reliable results with coding agents, you need to have human in the loop for reviewing every plan and every piece of code that is written. So that's what it says right here, right? Like you

**[0:05:18]** are still the bottleneck for verification before progressing. And coding agents aren't really to the point where we can move past this level and not sacrifice at least some level of reliability. And so this is the level that like I teach in my Aenta coding course in the Dynamus community. It's a

**[0:05:34]** good place to be. But if you want to push things further and you really have a harness, a system built for reliability, then you can start to move into level four. I think this is the year where we'll see this more common place for, you know, teams that are

**[0:05:48]** actually shipping production level code. So this is where you are building a sort of harness for AI to run on unattended tasks for very long periods of time. So when we think about harnesses like when Enthropic has open source and the Ralph loop and GSD like all of these

**[0:06:04]** frameworks that allow many different coding agent sessions to be strung together to tackle entire PRDs like very large sets of work. And so now we actually get to sleep at the wheel, right? Like a lot of people use these harnesses to have coding agents work completely overnight for them and then

**[0:06:20]** they review things at the end. So the important thing here, this is the big distinguishment between level 4 and the dark factory is we're still checking the final results much later. There's still going to be like let's look at that pull request and review and test it manually

**[0:06:33]** before we just ship it right to production. And so then going into obviously now the dark factory level five, this is where we aren't even reviewing the code before it goes to production. It is a crazy idea. Even I'm kind of uncomfortable with this myself. Like I said, that's why I'm calling it

**[0:06:49]** an experiment. This is really exciting. So, the engineer still manages the goal and the system. Like I was showing very briefly earlier, like there's a lot of work that I'm putting into building my system up front to really make it so that it's following my principles, my workflow, and my highle guidance. And

**[0:07:06]** so, we provide our plain English descriptions of what we want built and the rules we want it to follow. But then the AI defines the implementation, writes the code, tests, fixes bugs, and ships things to production. And continuing to just gloat over this analogy here, we still have a steering

**[0:07:22]** wheel in level four. So even though we're sleeping, we can wake up and course correct if we realize that it's totally taking us in the wrong direction. But now with this vehicle, which side note, I would love my vehicle look like this someday. We don't even have a steering wheel, right? There's

**[0:07:37]** still some kind of console here to be able to input our own instructions, but we don't really get the opportunity to course correct at a micro level. So that is what the dark factory is and that is what I am building. And like I said earlier, even besides Dan's blog post,

**[0:07:53]** the idea of a dark factory is not new. Strongdm is a company that went pretty viral a couple of months ago because they are implementing a dark factory to ship thousands of lines of production code that they never write or review. And I'll link to this blog post in the

**[0:08:09]** description. It is a really interesting read going through their journey of getting to the point where they now have no handcoded software engineering. This is the rule that they have for their team. And so initially it was just a hunch. It was an experiment just like what I'm doing. How far could we get

**[0:08:24]** without writing any code by hand? And they didn't think they could go very far. But they share their journey of building a system to make everything actually quite reliable. That's exactly what I'm working on myself. But the thing is, even though they're writing a lot about it, and they did actually open

**[0:08:40]** source their spec, so you can see the spec for building the system, they haven't open sourced it as a public experiment like I'm doing. And there are other companies working on something like a dark factory as well, like Spotify. They have their background coding agent, but again, nothing is

**[0:08:54]** open- source here. And so there's nothing until now where you can peer into a system, watch it work autonomously, even submit issues yourself to contribute to the experiment. That's why I'm so excited for this. Now, I know I spent a lot of time talking about what other people

**[0:09:10]** have to say about dark factories before even showing my architecture. But I did that very intentionally cuz it just sets the stage so well for this experiment that I'm running so you can grasp what a dark factory is and then where all the ideas are coming from that I took a lot

**[0:09:23]** of inspiration from. Because trust me, I did a lot of research and planning before I did anything here. The system has to be really good for this experiment to succeed. That's what I'm working my butt off on right now. So, I'm not done building everything and connecting all the dots, but I will link

**[0:09:40]** to this repo in the description. I'm getting pretty close to having this run end to end. I have my Archon workflows built. I'll talk about Archon in a little bit. I have the whole tagging system set up and I have my machine where I'm going to be hosting this

**[0:09:53]** running 24/7. And so I'm almost there and I'll make another video. This is like public public and you can even like create issues to contribute. But right now I just want to show you how the system works at its core. So we have the governance layer. This is really

**[0:10:06]** important. I'll talk about that how I'm using archon to orchestrate the entire flow, all the workflows and then talk about the loop and even some strategies I have for things like regression testing. And as I explain everything here, I'll also be going back and forth between that diagram and the repo here

**[0:10:22]** so I can show you the actual artifacts that I'm using and show you what it looks like for our issues and pull requests. And so let's go ahead and start with the governance layer here. So going back to Dan's blog post and we have this image of the car for the dark

**[0:10:36]** factory. The governance layer is like the console where we still input the high-level instructions like where we want to go i.e. What is the mission for our codebase here? So we have our mission marked on document. This outlines the coding agent exactly what we want to build, what is in scope, what

**[0:10:53]** is out of scope. We have our factory rules which guides how we operate for implementing and reviewing and merging. And then also our cloud MD. So we have the global rules around our tech stack and architecture. Making sure our coding agent has all of the context and needs

**[0:11:08]** around the codebase itself. So codebased context and then dark factory context, right? And then I guess the mission.md is kind of both wrapped up in one. And this is really really important because if we're going to give the reigns completely over to AI, but we're expecting it to be aligned with our

**[0:11:24]** mission as well, we better make sure that we are quite specific. And so I don't want these files to be too large, but I do want them to be pretty comprehensive, outlining exactly the kinds of issues that I would accept, how I want to validate my poll requests,

**[0:11:39]** things like that. And every single workflow that we run to implement and plan and validate is going to load these three files into context. So our system always understands our mission and the rules that it needs to follow. So going back to our repo here, I have my three

**[0:11:57]** files at the root. And so starting with the mission.md, we start by what is the application, which I actually haven't explained this to you yet, but I'm really excited not just for the dark factory, but the underlying application that we're building as well. It is going to be an agentic application that is rag

**[0:12:13]** powered. It'll let you ask questions to an agent that can perform rag to search through my YouTube video. So it's kind of like your own AI tutor that's trained on my content. And like I said, my goal is to make this a publicly accessible application. I'll obviously have to have

**[0:12:27]** some kind of rate limiting because it'll use my open router API key under the hood, but it'll be a way for you to just ask things over my content. I'm really excited for that. And so we also outline who it's for, the core capabilities. These are the things that are in scope.

**[0:12:40]** So if I make a GitHub issue that's related to one of these features, that means the dark factory is going to approve that issue and then implement it through the full factory process. And then we also have probably even more importantly what is out of scope, what the factory must never build. And so

**[0:12:57]** we're being very clear here what the boundaries are. We don't want our application to completely go off the rails with public issues that are just totally random things. And so we want to specify the kinds of things that we're not okay with. Like I want this to at

**[0:13:10]** least to start be an aentic platform focused on my YouTube channel, rag for my channel. So no support for other channels, no non-youtube content. And I don't want to swap the model or anything like that. That would just break the application. I don't want to add any kind of like payments or subscriptions

**[0:13:26]** or a mobile app, right? Like keep it simple, keep it focused. And so whenever we what I call triage our issues like figure out from all these issues which ones do we want to address the mission.md is going to really give the guidance there. And then things that the

**[0:13:40]** factory is not allowed to change like we don't want it to you know for example change its own mission statement. So being very clear on that as well. And then we have our factory rules. This is more about how the operations work for the factory. Like here is how we triage

**[0:13:54]** issues, what it looks like with our label system that I've created. So we use uh labels for our issues and our pull requests to really guide the whole process. And then also what it looks like for implementation, things that we don't allow, requirements that we have for every pull request. Like I want to

**[0:14:11]** keep each pull request pretty concise. That's a really bad way to break your system is if you allow it to create poll requests that are thousands of thousands of lines long. You're not going to get a good review if you do that. Quality gates for automerging things that are

**[0:14:25]** mandatory for our testing like using browser automation tools. So, we're really testing the application as a user would. I don't need to like go through this entire document here, but you get the idea of how we're just being very, very specific for our process. And this document's pretty long. I mean, it's 311

**[0:14:41]** lines in total. So definitely concise enough to fit pretty neatly at the start of the context for our coding agent, but also it's quite comprehensive because if it isn't for the factory rules and mission.md, I really have no way to align with the dark factory at all. And

**[0:14:57]** then uh last but not least, we have our claw.md. And so this is more of your classic global rules for a coding agent. You know, your text stack and the repository layout. So it has sort of an index of your codebase. uh you know commands that you have for testing and running things

**[0:15:12]** and your standards for testing code conventions. We got all that in our claw.md. So these three files together loaded at the start of every conversation. And now this is the exciting part. So we talked about the context loaded into every workflow. Now let's talk about the workflows. This is

**[0:15:28]** where I use Archon. And so Archon is an open- source project that I recently released. I'll link to the introduction video right here if you really want to dive into using it. It is the world's first open-source harness builder. So, you take your AI coding process, no matter what it is, and you can package

**[0:15:45]** it up into deterministic and repeatable AI coding workflows. Very exciting. It's the perfect fit to be the backbone for the dark factory because I define the process. Here are the steps I want to happen for triaging issues and implementing and validating and I can run them all as archon workflows. And so

**[0:16:05]** going to the three layers here, the harness is archon, right? Like it is the workflow engine. And then the coding agent, I'm using claude code behind the scenes. But the catch here is I'm not actually using anthropic models. I have claude code routed to use miniax m2.7 as

**[0:16:22]** the model driving the entire dark factory. So cloud code you, if you didn't know this, you can use environment variables to route it to other providers like GLM, miniax, open router. I want to use M2.7. And it's a purely economical decision because for the throughput that we're going to have for this dark factory,

**[0:16:42]** especially once I start accepting public issues, there's no way I can use my Anthropic subscription. I'd hit the rate limits so quickly. So Miniax M2.7, it's a pretty powerful model. It's very cheap and fast, though. So it's going to allow us to run the experiment continuously without having to throttle after a

**[0:17:01]** certain number of issues every single day. So I will have to probably pay a good amount of API credits to make this work. But also Archon allows us to specify different models for different workflows and run things with code instead of coding agents. So the entire process and working on making it pretty

**[0:17:16]** token efficient as well. So I'll actually just explain the archon workflows by getting right into the factory loop here. I think this makes the most sense. So the entry point to anything that we're going to work on in the factory is a GitHub issue. either we are going to create a GitHub issue or

**[0:17:33]** the dark factory will create an issue itself if there's a follow-up item that it finds in its regression testing and then we go into the triage workflow. This is going to run on a scheduled basis. So it'll look at all of the recent issues that haven't been triaged

**[0:17:49]** yet and it'll figure out what to do with them. And so I'll show you what this looks like if I go to the issue list here. I have a couple of examples just as I've been starting to test the dark factory here. And you can see that we

**[0:18:01]** have factory accepted or we have priority low. So like we're assigning priority and if we're going to address them or not during this archon triage workflow. And if I go to closed, we'll see ones that are rejected as well. And whenever it rejects one, it's also going to put a comment here just letting us

**[0:18:18]** know like, hey, why are we rejecting this in the first place? So rejected as a duplicate of number 19. I know there's a lot of other comments here as well, but that's just because of the mess of me testing everything right now. And this entire triage process is run as an

**[0:18:31]** archon workflow. So let me actually go over to the archon workflows and show you what this looks like. So within the archon folder, this is where we have the custom workflows defined for archon. And again, check out that video that I linked to earlier if you want to dive

**[0:18:45]** more into archon. But let me open up the triage workflow here. So it's pretty concise overall. It's mostly just the scripts that make this file long, but it is really a three-step process. So this workflow starts by fetching all of the recent issues and it's not using an AI

**[0:19:02]** agent to do this, right? Like we can just have a bash script that pulls all the recent issues. Then we're going to send that into an agent to reason about which ones we actually want to address based on the mission.md and factory rules. So we load these into the

**[0:19:17]** workflow as well. And then this is where we do the classify step. So I specify the model as sonnet but it's actually routing to miniax m2.7 under the hood. And this command right here is just a markdown document that goes through the process of how to triage and then of

**[0:19:33]** course leveraging these two files as well. And then we apply our decisions. So we have a structured output here where it's going to say like okay we're going to go with this issue for a priority of low. This one with a priority of medium we're going to reject

**[0:19:47]** this one. We produce that JSON and that's going to end up in this decision file right here. We're going to read through that and just have a simple bash script that applies all of the GitHub issues and closing things, doing all that deterministically. And it's neat because we can also take a look in the

**[0:20:02]** Archon web UI to see what this workflow looks like. So, we're pulling all of our context in parallel like the mission.md and factory rules and all the issues, sending that into the coding agent that reasons about which ones we should close and which ones we should address. And

**[0:20:16]** then this is the bottom step where we do all the labeling. And so that's the triage workflow. It's pretty simple, but it's really powerful and it shows the power of archon combining deterministic and non-deterministic steps to get a single larger job done. And then the next workflow that we have is the one to

**[0:20:32]** implement. So for every single work issue that we triage that we want to address, we're going to kick off archon workflows in parallel for implementation. We don't even have to do it sequentially because Archon gives us the work tree and isolation support so that we can manage all of these

**[0:20:47]** different implementations at the exact same time. And this workflow is a little bit more elaborate. I'll show you what this looks like in the Archon web UI here. There's a lot of steps that we have because for every single issue, we need to do some research and we need to

**[0:21:02]** classify is this a bug to be fixed or a new feature that we're going to plan. So we'll plan out the new feature or investigate the bug depending on what it is. Then go into the implementation, creating the pull request, and then validating things in parallel as well.

**[0:21:16]** So pretty comprehensive. I don't need to get into the entire thing, but you can always just go into the workflows folder here and check this out cuz I'll have everything linked in the description. But that is our implement step. And then I have a separate process for validation. And I have very

**[0:21:32]** intentionally created this as a separate workflow because I want to follow the hold out pattern from strong DM. This is one of the most important things for reliability here. So I want to touch on this for a minute. So one of the biggest problems with AI right now is

**[0:21:45]** psychopancy. LLMs are way too prone to agree with our ideas even when they're stupid and they build up a ton of bias for their own opinions throughout a conversation. That is why it is so important to have a key separation here. one agent to do the implementation, one

**[0:22:01]** to do the validation. And I go so far in the system as to even having separate archon workflows to make this distinction very clear. We don't want any of the bias to carry over. And so what the hold out pattern does is we give our validation agent the user

**[0:22:16]** journey that we either fixed or created and then the exact diffs for the code, what was just implemented. but we give it no context into the development process. Any kind of bias that it could pick up from that, we don't even want to make that a possibility. And so what

**[0:22:33]** Strong DM says here, going back to their article, a test that is stored in a codebase can be lazily rewritten to match the code. There's a lot of other problems related to this as well. Basically, coding agents can say things are good when they aren't actually. And they can just rewrite tests to kind of

**[0:22:48]** mock success even when there are problems. They are stuffing under the rug. And so, we're going from just pure tests to scenarios now to satisfaction, testing entire user journeys and not getting tied into the context of the implementation itself. And so, I don't want to get super deep into the workflow

**[0:23:08]** for validation here. It's actually pretty comprehensive. We do a lot of endto-end testing with browser automation. So we can really test a user journey as a user would navigate through this site. So there's a lot that goes into this workflow here. But the point is once we get done with the validation

**[0:23:24]** here in this workflow, we are theoretically confident to now merge directly into main because this is a dark factory. There is no human approval here. And so now this just runs in a continuous loop. Basically we have a cron job, right? We have a scheduled job that's going to run every hour or

**[0:23:39]** whatever. Handle these issues. So we triage, implement, validate in a loop forever and ever and ever. That is the idea that we have with this dark factory. And that's pretty much the entire system. The only other thing that I'm also working on right now that I don't have built yet is I want to have

**[0:23:54]** some like larger process that runs maybe once a week that does regression testing over the entire system. So I somehow have a document that outlines every single user journey. here's all the ways we can interact with the agent and viewing sources from the rag pipeline, everything like that. And then it'll

**[0:24:10]** create GitHub issues for anything it finds that isn't perfect. So that's another part that I'm still working on here. I'll share more on that later. But yeah, this is my dark factory at a high level. So I hope you can really see the amount of effort that I put into

**[0:24:22]** building the system up until this point. It's actually quite a bit to explain, a little bit overwhelming, but that's what it takes to build something that I can trust to any extent for taking coding agents this far with a dark factory. So, I hope that you found this interesting.

**[0:24:36]** I hope that you'll come along with the journey with me as I build this out. I'm going to be putting out a lot more content and doing live streams as well as I'm building these workflows, connecting everything together within the next week or two. I want this up and

**[0:24:48]** running. So, there'll be a full deployed application that you can test. You can add issues yourself, see if the dark factory will accept it. Right now, I'm just in the middle of getting that all hooked up. And so, yeah, more of this coming soon. So, if you appreciated this

**[0:25:01]** video and you're looking forward to more on using AI coding assistance and building out this dark factory, I would really appreciate a like and a subscribe. And with that, I will see you in the next video.
