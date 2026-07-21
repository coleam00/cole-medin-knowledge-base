---
type: raw-transcript
title: "The Best AI Coding Setup Isn't the Most Autonomous One (Here's Why)"
youtube_id: muwRbfuKbR4
url: https://www.youtube.com/watch?v=muwRbfuKbR4
slug: the-best-ai-coding-setup-isnt-the-most-autonomous-one-heres-why
published: 2026-07-03
duration: "0:21:15"
fetched_at: 2026-07-21
immutable: true
---

## Transcript

**[0:00:00]** Everyone is using AI coding assistance very differently. You'd be surprised how large the spectrum is, even for companies that are using these tools to ship production code. And the best explanation I found for the different ways we can use coding agents is from Dan Shapiro. So in this blog post, the

**[0:00:18]** five levels from spicy autocomplete to the dark factory. And it's really important for you to understand the level that you're currently at and what you should be shooting for and the level that's best for you. also changes over time as you create a more structured approach to AI coding. And so in this

**[0:00:35]** video, I want to break down each one of the levels nice and simple for you and help you understand where you should be at right now. And I just want to share some honest thoughts, especially on some of the last levels, especially with the dark factory. I see a lot of companies

**[0:00:51]** go for this right now, and I've even built my own. But there are a lot of downsides to the dark factory, as powerful as it is. And so we'll get into the meat of that as well. All right, so let's get right into the different levels of AI coding. And this entire

**[0:01:05]** article uses the analogy of driving a vehicle because there's a company in 2013 that created the five levels of driving automation. And it's very neat because we can map each one of these levels directly to how we interact with AI coding assistants. How much are we leaning on them versus keeping our hands

**[0:01:22]** on the driver's wheel when we are interacting with them and having them create the code for us? And so level number one is spicy autocomplete. I love this name, by the way. And here you're still writing every single line of code yourself. You're just using the coding agent as a reference tool or some kind

**[0:01:40]** of enhanced search. So it's like a smarter stack overflow. And so it never has the final say. It doesn't get to write a line of code, but you're constantly leaning on it for how should I architect this or how should I write this function? And so it's like your

**[0:01:53]** parents vo. So maybe even having automatic transition. This is the most manual you can possibly be. You have to manage the car at a very fundamental level. And so you can see that it's actually level zero because we're not really having the coding agent do anything for us. And so then we get into

**[0:02:10]** level one. And so this is like the coding intern or when you're driving a car, you have cruise control. It's that first level of autonomy where that there's at least one part of the car that's being managed on your behalf. And so here your coding agent is going to

**[0:02:26]** write the unimportant or boilerplate code. And so setting up your initial repository, maybe installing packages, writing unit tests, doing simple refactors, that kind of thing. You're not leaning on it for anything that takes true reasoning, but you're still saving a good amount of time here. And then level two takes us to the junior

**[0:02:43]** developer. This is where you really start to lean on the coding agent or lean on the car to operate pretty autonomously, but only in some situations. So when you're driving, it's like you have autopilot on the highway. But when you're actually driving in the city and there's a lot of turns and

**[0:02:58]** rules that need to be followed, you can't trust it anymore. So it's a junior developer where you're doing a lot of pair programming. You are handing off a lot of the boring work, but there still are going to be those things where you don't trust it entirely and you're

**[0:03:10]** driving the process very manually. And there's a good chance that this is where you are at right now. Because if you don't have a very established system for how to leverage AI coding assistants and have them evolve over time, and we'll talk about that in a little bit, then

**[0:03:25]** you probably don't trust it for every kind of task. There are certain things where you think it's just going to be better for you to do it yourself, especially if you're more technically inclined. And I do really encourage you to get past level two. So, when we start

**[0:03:39]** to talk about level three here, this is where I really want you to be. And so it's easy to get here because you're trusting it with the easy stuff like autopilot on the highway. But when you really create a system for planning and implementing and validating, that's when

**[0:03:54]** you go into level three, the developer. This is where you get to the point where your coding agent is writing a majority of the codebase, which is what it says right here. But honestly, I would take this a little bit further. When you get to level three, and this is mostly where

**[0:04:07]** I operate, this is where you're delegating all of the coding to your agent. And I myself haven't written a single line of code for over a year now, which is crazy to think because I've spent years and years of my life writing code every single day. And so as an

**[0:04:22]** engineer, it took a while to get to the point where I had the system and built the trust to get to level three. But there's a good chance this is where you should be. This is the sweet spot of reliability and autonomy. Cuz as it relates to driving a car, it's like a

**[0:04:36]** Whimo with a safety driver. you're letting the coding agent really go or you're letting the car do all the driving, but you're still in the driver's seat. You're still attentive. You're still driving the process. And so what I like to say here for level three is the only reason that we delegate all

**[0:04:52]** the coding to the agent and trust it to do that is because we're sandwiching the implementation with a lot of planning and a lot of validation that we are very much a part of. And so you delegate all the coding, but you still remain in the driver's seat. But that starts to change

**[0:05:07]** once we get to level four. This is the level where we reach the engineering team. You're handing off much larger sets of work for the coding agent to knock out autonomously. And so you're still at the helm, but you're sleeping for long periods of time because we're letting the agent rip through larger

**[0:05:24]** sets of work based on something like an epic, a PRD, or a spec. Level three is more like each individual task. We're doing the planning and validation with the coding agent, but here we're just doing the very high level direction setting up front and then the validation at the very end like a set of pull

**[0:05:40]** requests for example. And so we're letting it go go based on a larger spec. And so it's not quite the dark factory. We'll talk about this in just a second where there's not even a driver's seat like right like we still have control of the system to an extent but we're just

**[0:05:56]** not doing that very often. And at this level, this is where your reliability really starts to tank until you have a trusted and really wellestablished workflow for AI coding, going from idea all the way to production. And it takes a while to get there. That's why I recommend you stay at level three or you

**[0:06:12]** at least stay here for a long time because you build up that system and then you can start to make your coding agent more autonomous. So really just taking the system that you were more a part of and then taking out the human in the loop as you go to get to levels four

**[0:06:28]** and five. And so I'll talk about in a little bit what it actually takes to create this system. What actually is a system for AI coding? But first let's talk about the dark factory for a bit. So at level five, it really isn't even a car anymore. Let me zoom in on this so

**[0:06:42]** you can see this image. Well, there is no driver's wheel. We can't even take control and grab the reinss even if we wanted to. Now, there's still a console in this vehicle, whatever it is, this spaceship. So, the console allows us to still input our highest level directions

**[0:06:58]** possible, but yeah, we're not controlling any of the development. And so, the way that a dark factory works is your input is your spec, the large document that outlines everything you want to build. And what you get out of the dark factory is shipped code. And so that's probably the biggest difference

**[0:07:14]** between level five and four. Level four, you're not trusting the coding agent to ship right to production. But in level five, you actually are. And if that sounds kind of scary, it should. That's why I'm saying you have to be very careful when you get to this level of

**[0:07:28]** autonomy. Cuz if there's one thing you have described wrong in the spec or the coding agent just makes some kind of incorrect assumption, that can lead to dozens of shift deployments that are just botching what you wanted to actually create. But in the end, the dark factory is ideal. If your business

**[0:07:46]** can get to the point where you have a process where you can send in a spec and get out shipped code, that my friend is the dream. And we're starting to get to the point where the dark factory is becoming realistic. Now, I want to be very careful how I put this right now

**[0:08:02]** because I don't want you to just reach for the dark factory immediately, but I think that there is a possibility you can get here with the current tooling and LLM we have available. And so, you can probably jump to level three very fast. I mean, that's what I teach on my

**[0:08:16]** YouTube channel and in the Dynamis community, like creating the system where you're still in the loop for each individual build, but you have quite a bit of autonomy. You're delegating all the coding to the agent. So, you start here. This is where I want you to be. And then you take out the human in the

**[0:08:30]** loop as you create that system where you really trust that it understands your codebase and your workflows and things are reliable. And so there are some companies that are starting to come out of the woodworks sharing how they do have a dark factory that's actually running. Strong DM is one example. I'll

**[0:08:47]** link to an article on that in the description. A lot of other companies aren't really documenting anything like Strong DM. So, it's just some rumors that are starting to surface of companies that are doing this successfully, even in the banking industry, even when the code has to be

**[0:09:01]** perfect when it's shipped to production. So, it's definitely possible, but we need the system to get there. And so, with that, let's actually get into what does a system for AI coding look like? And how do we build something that can even take the form of the dark factory?

**[0:09:16]** The sponsor of today's video is Sonar. They're making big moves in the AI coding space right now. The reality is that these days AI is writing a huge chunk of new code. And that my friend is not slowing down. But the problem is traditional code reviews and quality

**[0:09:30]** gates were never made for volume at this speed. And so bugs slip through and AI errors compound on themselves and your code base gets fragile quickly. That is why Sonar has acquired guitar. Guitar is AI code review that actually fixes your code. It's not just another agent you

**[0:09:46]** throw at the problem. It's an entire harness for validation, making your code more reliable with full visibility as well. The way that guitar works is you connect it to any of your GitHub or GitLab repositories. And then as soon as you open up a pull request, we can see

**[0:10:00]** Guitar here running a comprehensive code review. And not only does it do the code review, but can also fix the issues that it finds automatically as well. So right here, it identified and fixed a SQL injection vulnerability that I have in this poll request. And the best part for

**[0:10:17]** all of this is every single time it makes a fix, it automatically validates it against your CI. So it just increasing the reliability even more. It even reads your CI failures for you. So it can do things like ddupe your errors, help you identify flaky tests, and clean

**[0:10:33]** up your build and lint failures so you're not drowning in logs. And you can see this is all very in line with Sonar's agent centric development life cycle. A framework that's based on the three pillars of guide, verify, and solve. And guitar fits very well into their verify pillar. And teams using

**[0:10:52]** Sonar are 44% less likely to hit production outages caused by AI generated code. And it's not about replacing your human judgment. It's just a serious safety net under everything your agent ships. And Guitar has a 14-day free prot trial. No credit card required. I'll link to it in the

**[0:11:09]** description. All right, so I put a lot of time into thinking about how I can quickly describe what a system is to you for AI coding. And I want to be concise because that's really not the point of this video to dive super deep into the weeds of system engineering or context

**[0:11:23]** engineering, but I want to give you an idea of what you're going to be creating and evolving to trust your coding agent to be more autonomous over time. And so I decided to pull from the Dynamus agentic coding course. So, taking a couple of the things that I have there

**[0:11:38]** and just showing it really fast. And so, I want to start by talking about the AI layer because these are the different components that you build on top of your coding agent. Things like your rules and skills. So, your coding agent understands your conventions, your context of your codebase, and your

**[0:11:55]** workflows. And when you think about harness engineering, which is building the system for AI coding, it really starts at layer zero with the tool that you pick. So you don't control this, but you get to pick the coding agent. And the coding agent, it really is a harness

**[0:12:10]** because it wraps the large language model with the tools and instructions to make it operate as an AI coding assistant. And then we build the layer on top. This is what we control because we wrap the coding agent that it itself wraps the LLM to provide a context not

**[0:12:25]** on how to be an AI coding assistant, but how we want it to be a coding agent specifically on our codebase with our workflows. And so there's really six components that we're building up here. We create our rules. These are the conventions we want our coding agent to

**[0:12:39]** follow. We have our sub agents, how we want to delegate work and manage our context. And then we have our skills, our packaged up workflows. Like this is how we want our coding agent to do planning. Here's how we want it to implement. What's the procedure we want

**[0:12:53]** it to work itself through based on the input we give it for what we want to build. And I don't need to get into the details for all six components here of the AI layer. I have a video that I'll link to right here where I really get

**[0:13:04]** into all this. Just know that these are the components we create to make our coding agent understand our conventions and process. We build these up and we compose them together to create our full workflow. And that is the system. And so I'll cover this diagram really quickly because this is the flow, right? Like we

**[0:13:22]** build up the AI layer and now here's how we use it. And so we create it at first. That's what this stage represents for both green field or brown field. are either going to be building up our initial rules and workflows from the idea of what we want to create if we're

**[0:13:34]** starting from scratch or if we're working on top of an existing codebase. We're going to understand the code and document it. We're going to document our conventions, build up our workflows, and then either way, it's going to converge into the exact same process that I call the R piv loop. This is how I build any

**[0:13:50]** new feature or fix any bug in any codebase. And so I start by researching just exploring how we're going to be tackling this problem. And then from there I do structured planning and again I have rules and sub agents and skills that drive this more higher level process. That is the system. So I create

**[0:14:10]** a structured plan that has things like my validation strategy and the task list that I have for the agent. And like I said earlier, when you are at level three, which is what I recommend, you're very much a part of the process here. We're having the conversation with the

**[0:14:24]** coding agent to establish things, having it grill us with questions, to remove assumptions, and then we create that final plan that we then send into implementation. So, we have another skill, another workflow for it to operate on that plan that we create. And of course, we have a lot of validation

**[0:14:39]** at the end. And so, the system here for how the coding agent can run unit tests and even do full endto-end testing. And then human validation if you want to really make sure that your reliability is topnotch. So, there you go. That is the fastest I've ever blitzed through

**[0:14:54]** helping you understand a full system for AI coding. So I hope that makes sense at a high level. We build the components that create our harness and then this is the flow to leverage it. And I won't talk about system evolution too much here, but we also have the whole idea of

**[0:15:07]** every single time your coding agent makes a mistake. It's worth not just patching it and moving on, but having that conversation with your coding agent to figure out what part of our AI layer can we improve so that issue doesn't happen again or at least it's less likely to happen again. Like maybe

**[0:15:22]** there's a workflow we can refine or a new rule that we can add to address the issue that the coding agent created. And so going back to the article now, when you get to level three, that's when you really start to have the system that I showed you just now very briefly. you

**[0:15:36]** have for yourself or even as a team standard the rules and skills everything in the AI layer and then you're composing that together in the flow that I described and so how exactly you're going to with your coding agent go through all the steps it takes to go

**[0:15:50]** from idea to production or pull request and so when you do that system evolution every single R piv loop you're figuring out how can I make the AI layer how can I make my process better over time you'll start to get to the point where when you have a new request come in

**[0:16:05]** you're like, you know what? I think my coding agent or I know my coding agent is just going to knock this out of the park. Like, I don't even really have to iterate on the plan or I don't even think I have to validate things besides a couple of quick spot checks. When you

**[0:16:18]** get to that point, that's when you know you can start to go to level four and maybe even level five. You start to sort of build that muscle of what you can trust your system to accomplish. You grow that muscle. You grow that system over time and you can start to trust it

**[0:16:33]** with multiple tasks. operating through it autonomously. That's level four. And then dark factory, that's when you have to take your system even beyond what I've shown you. So, last thing I want to cover here is just talking about what goes into really taking a system like I described and turning it into a

**[0:16:49]** fullyfledged dark factory. So, I found this article that I'll link to in the description that I think very nicely puts how you want to build up a dark factory. What are all the different components? Cuz like they say right here, a dark factory isn't just AI writes code. It's a system with distinct

**[0:17:05]** components that handle different stages of the development pipeline. If we're going to go from massive spec all the way to ship code, we have to have a lot of different agents operating to triage the different tasks from the spec to build each one of them to review the

**[0:17:20]** pull requests to manage the deployments to do the regression testing. There is so much that goes into a dark factory. In fact, I did quite a few live streams on my YouTube channel. I'll link to one right here where I built a dark factory live and I used Archon, my open- source

**[0:17:34]** harness builder, to create a lot of the workflows to manage all these different parts of the development pipeline. And it was a lot of work and there was still a million things I needed to do to truly make it reliable. It was just more of an experiment that I did. I called it my

**[0:17:48]** dark factory experiment. But anyway, it starts with a planning agent. So once we have the larger spec distributed into individual tasks, we need an agent to handle the planning for that one task. And so that's just like what I showed you in the system earlier where we want

**[0:18:04]** to create that structured markdown document, our plan of attack for that specific feature or bug. And then we send that into the code generation agent. So we have a handoff there where usually it's a markdown document is passed to another agent to execute and create that pull request. and then the

**[0:18:21]** validation layer to review that pull request. It's important to not do your code review in the same context window where you do the implementation because there's a lot of bias that's built up there. And then of course we have the deployment system. Again, no human in the loop going straight into production.

**[0:18:35]** So we want an agent that manages that maybe doing things like regression testing as well. And then we need the orchestration layer. We need that higher level agent to take the spec and split it into tasks to manage the handoffs between the different agents and make sure that we don't have duplicate work

**[0:18:50]** or that one agent is stalling waiting for inputs that are never going to arrive. I mean, even just reading through this, you can start to imagine all of the complexities, the millions of things that can go wrong because agents can veer off of your initial spec and have a ton of tasks that don't make any

**[0:19:04]** sense. They can stall waiting for a handoff from another agent that crashed. If there's no human in the loop, you risk that those failures happening without much visibility because the whole point of it is you don't have to pay attention to it. And so you really got to make sure that things are

**[0:19:18]** reliable before you ever get to this point. And building the orchestration layer on top of your existing system is also an engineering effort of its own. So it's not even just like get the system to a point where it's reliable. It's get to the point where it's reliable and then you have to build the

**[0:19:33]** next layer on top of it. So it is a lot of work to get here. So again, the dark factory is the dream, but yes, it takes a lot of engineering effort. And if you want to read the rest of the article, I would encourage you to do so. A lot of

**[0:19:45]** good stuff here, and they cover some things I've been working on with archon as well, like deterministic and agentic nodes. Sometimes you need the reasoning capability of an LLM for a step in a workflow. But other times, you don't. And you can make it more reliable by having some things that are handled

**[0:20:01]** deterministically just with code like formatting code, running a llinter, triggering a deployment. You don't always need an LLM. And so that's one of the things I have built into Archon and just the idea of engineering harnesses to drive these things like what Stripe did with Stripe Minions. And then they

**[0:20:16]** also go into the different failure modes that we talked about here like cascading failures. Evaluation gaming is another really interesting one. These are the things we have to engineer for to make it so the dark factory is realistic at all. And yes, it can be kind of daunting

**[0:20:31]** when you look at something like this and think about what really goes into making it reliable. But this is also the future of AI coding. We already see companies that are starting to engineer these things successfully. And it's only going to get more realistic as coding agents and LLM get more and more powerful. And

**[0:20:47]** so this is something that I'm really leaning into and I encourage you to do as well. I've already done some experimentation with it. like I talked about earlier and I do want to do more content on building a dark factory. So, also let me know in the comments if

**[0:20:59]** you'd be interested in that. And so, with that, that's all I got for you today. If you appreciated this video and you're looking forward to more things on Agentic Engineering and maybe dark factory building as well, I would really appreciate a like and a subscribe. And with that, I will see you in the next

**[0:21:13]** video.
