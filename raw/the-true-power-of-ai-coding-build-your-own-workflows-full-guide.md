---
type: raw-transcript
title: "The True Power of AI Coding - Build Your OWN Workflows (Full Guide)"
youtube_id: mHBk8Z7Exag
url: https://www.youtube.com/watch?v=mHBk8Z7Exag
slug: the-true-power-of-ai-coding-build-your-own-workflows-full-guide
published: 2025-09-24
duration: "0:26:04"
fetched_at: 2026-07-21
immutable: true
---

## Transcript

**[0:00:00]** No matter what you are building, if you're working with AI coding assistants, it is a lot more than just prompts. It's all about creating systems, workflows that can evolve to fit your needs. I know it's tempting to just wing it. But if you want to build anything substantial, you do need

**[0:00:17]** structure. There's a reason why we have so many strategies around context engineering like the PRP framework or BMAD, the GitHub spec kit. There's a million of them out there. And that's actually the problem as well. It's easy to get lost in the sauce, so to speak, with all these different strategies and

**[0:00:33]** how they apply to you. Now, the solution to this problem is what I'm going to be covering with you in this video. We're going to be scrapping the notion of existing frameworks like PRP and BMAD, and we're going to be building our own. I'll show you how it works. Because if

**[0:00:47]** we can understand the philosophy and strategies that go into all these existing frameworks, not only can we use them better because we actually understand them, but also we can tweak them to our needs and even build our own workflows and systems. This is where the power really comes into your hand. And

**[0:01:03]** this diagram that you're looking at here is everything I'm going to cover with you in this video. It sums it up really nicely because I want to keep things simple and fundamental here. I want to give you a process that you can apply that'll take you super far with AI

**[0:01:18]** coding assistance no matter what you are making. So the primary mental model that guides most of my coding is the three-step process of planning, then implementing and then validating. That's we're going to build a workflow around. And so I'll just go through at a really high level everything that we're

**[0:01:33]** covering here. Then we'll get into detail and I'll show you a real example as well. And so first of all, I always start with planning. And I have a multi-step process for this. I start with vibe planning. That's what I like to call it. We're basically just exploring very free form the different

**[0:01:49]** ideas that we want to implement for a new project or the codebase for an existing project. And then from there, we create our initial requirements for that new feature or new project. And then we prepare all of the context so the AI coding assistant has what it needs to get the job done. And slash

**[0:02:04]** commands are great for this. We're going to be covering slash commands and sub aents and other components of AI coding in this video as well. And then once we have all of the context we need, we want to then execute on it to actually produce our code. And creating a

**[0:02:18]** predefined workflow through slash commands is fantastic for this as well. So we can define how we want to manage tasks and research our codebase, those kinds of things. And once we have the code outputed, it is time for validation. And we want to leverage AI coding assistants to validate their own

**[0:02:35]** work and then put ourselves in the process as well. making sure that we can really be the project manager for the AI coding assistant. And then the last thing that I'll be covering throughout this video here is the different concepts for AI coding assistance and how they apply to different parts of our

**[0:02:52]** workflow like global rules and sub aents and slash commands. For example, we don't actually want to use sub aents in the implementation phase. So I'll talk about how that works, really the philosophy behind it. This will also help you understand how these different strategies work like PRP and BMAD. Now,

**[0:03:09]** what I'll be building live here is not the focus of this video. So, I thought I would take this as an opportunity to do something fun and different, showing you something that I'm working on personally because I've been overhauling my productivity workflows recently, switching to an app called Obsidian. It

**[0:03:24]** is a free and local knowledge management platform. You can kind of think of it like Notion except there's also a ton of open source plugins to extend it. I'm working on some myself. I will probably be creating a lot more content around Obsidian in the future because you can

**[0:03:39]** also use it as your second brain. It's super cool and there's a lot of AI integrations that I have been working on including what I'm going to showcase in this video. So, we have the co-pilot chat on the right hand side. This is connected to, you can see it right here

**[0:03:54]** in the bottom right the Dynamis Obsidian agent. I have my own AI agent that I have running in Docker on my computer and that is what Obsidian is connected to. It's super cool. So, I can say tell me about and then I can reference files within Obsidian like the one that you're

**[0:04:07]** looking at right here. I can send this in and it's going to my custom agent. This connection here is what we're going to be building out in this video just as an example for the custom workflows that we're creating here. It's super cool. Take a look at that. All right. Now,

**[0:04:20]** let's dive into the process and we'll start with the planning phase here, which honestly is the most important phase by far because if you're not curating your context correctly for the AI coding assistant, it will fall on its face. And by the way, everything in this video is going to be rather brief. I

**[0:04:36]** just want to start with the basics here. If you really want to dive deep into mastering AI coding assistance with me, definitely come be a part of the half-day workshop that I'm hosting on September 27th. This is where we really dive deep. All of my strategies in one

**[0:04:52]** place for getting the most out of AI coding assistance. So, hope to see you there. Link below. Definitely check it out. I am going to be pouring so much value into that workshop. And so, right now, you kind of get a taste actually of a lot of what we're going to be covering

**[0:05:04]** here. I want to help you build your own AI coding workflows so you can understand the philosophy and strategies that go into all these different frameworks. And so, with that, we can start with the planning phase. Now, the first thing I always do to start the planning phase is vibe planning. Now,

**[0:05:20]** hear me out on this. If you've seen my AI coding content in the past, you know that I'm not a fan of vibe coding, but that's different because that's when we get into the actual implementation. We definitely want a lot of structure and validation there. But when we're in the

**[0:05:34]** planning phase initially, all we're doing is exploring ideas, architecture, concepts, figuring out our tech stack. We're doing that with our AI coding assistant as our research companion. And I purposefully do not want this to be structured because I want a more freeformed mindset as I'm working in this initial phase. And so for new

**[0:05:55]** projects, this means researching online resources, previous projects that you've implemented. I actually love to do this where I'll create an examples folder in my codebase and take existing projects and put it there and research that with my coding assistant. And then for existing projects, it's generally researching and analyzing the existing

**[0:06:13]** codebase to see where our new feature is going to fit in. And of course, this isn't an exhaustive list. It's really whatever you want to do to have a conversation with your AI coding assistant so you're both on the same page of what needs to be fully planned

**[0:06:26]** and implemented. And so once you have that conversation with the coding assistant, within that same context window, I'll have it help me create what I like to call an initial MD. This is the first file that we create for our planning. Just a simple markdown document. The goal is to produce a

**[0:06:44]** markdown doc with a detailed feature request, otherwise known as a PRD. This is the kind of document that's more high level, the kind of thing you could give to another human to describe what you're looking to build. So, at this point, we're not super specific to prompting strategies for the coding assistant yet.

**[0:07:01]** And so, for a new project, generally, you want this to be very high level. a simple MVP for the application you want to build, including a lot of references to the supporting documentation and examples that you found in the vibe planning stage. And then for the existing project, it's pretty similar,

**[0:07:18]** but it's going to be a lot more focused and detailed that specific feature you want to build into the existing codebase, including a lot of references to what I like to call integration points. The files that have to be edited, maybe the files you want to reference for architecture. Again, all

**[0:07:34]** of those things that you discover with the coding assistant in the vibe planning stage. So once we have this initial MD, that's when we want to take our requirements and turn it into a full-fledged prompt for the AI coding assistant. And this is really where the strategies around context engineering

**[0:07:52]** come into play. You've probably seen this diagram on my channel before, but I recreated it from scratch in Excaladraw. Hope you're proud of me. I put way too much effort into making this. It's kind of silly, but anyway, we have RAG, providing external documentation to our coding assistant, memory, like our

**[0:08:08]** conversation history. We have task management. This is super important for the planning phase, and we'll talk about this in a little bit. And then, of course, we have prompt engineering, which is a lot about how do we take our initial request and craft it in a way where we have a plan of attack for the

**[0:08:23]** coding assistant. And so, the goal in this stage, we are producing a second markdown document. So, we take our initial MD and we produce a detailed set of goals, tasks, and resources for the AI coding assistant. Basically giving it everything it needs to get the job done effectively. So, we're taking our PRD,

**[0:08:43]** turning it into a full-fledged implementation prompt. And by the way, this is exactly what the PRP framework accomplishes that I cover on my channel. And so I'm starting from the basics here, but it's kind of cool how like it naturally progresses into kind of a light bulb moment where it's like, "Oh

**[0:08:58]** yeah, PRP, that totally makes sense because that's exactly what we're doing." When you generate a PRP, you're taking your initial requirements and turning it into a much more structured document for the coding assistant that has things like the task list that you want to knock out, your desired codebase

**[0:09:13]** structure, your success criteria, all the documentation examples that you wanted to reference. That is what we're creating with our planning document. And there are a lot of tools to help us get the job done here. I'll show you Archon in a little bit with our live example, the PRP framework, of course, even

**[0:09:30]** simple web search tools that we have with things like cloud code. That is a part of the rag that we have for context engineering and archon is also for rag by the way and also our task management. And then a lot of other tools coming out like the GitHub spec kit is rather new,

**[0:09:45]** really cool, provides a lot of commands to help us do a very similar thing that we're doing here with the vibe planning and then you know creating our initial requirements and creating the plan. GitHub spec kit does a lot of that. And so again, understanding the philosophies here that go behind these different

**[0:09:59]** strategies. All right, let's get into the codebase now because I want to show you how this works in action. Now, for brevity sake, I already had the conversation complete, but I'll walk you through my general process, how I'm applying the principles to start to create this AI coding workflow that I'll

**[0:10:14]** showcase here. That is just an example of the kind of thing that you can build. And so, first of all, we're starting with a brand new conversation with cloud code. And this works no matter your coding assistant, of course. And the first thing I do whenever I start a new

**[0:10:28]** conversation working in an existing codebase like I'm doing for this Obsidian integration is I will run a primer slash command. And so we're starting to get into slash commands here. Slash commands are simply prompts that you want to turn into reusable workflows which very much goes with the

**[0:10:44]** theme that we have here. creating a system for AI coding both with mental models and also with literal workflows that we have created as these markdown slashcomands here. And so what the primer does is it lists out instructions for files to read to quickly catch the AI coding assistant up to speed on our

**[0:11:04]** project when we're starting a new conversation. And so that way it kind of feels like our coding assistant has been working with us on this project for a while now, but it is actually a fresh conversation. And so it does a bunch of research through the key files in my

**[0:11:16]** codebase. And then at this point I'm ready to move to the vibe planning and slash commands are pretty important for most stages of our workflow here. Really every single stage. And so I have this part of the diagram here talking about this for the planning stage. This is

**[0:11:33]** where we want to set up our global rules, the key instructions for our coding assistant. And then we use sub aents and slash commands to automate parts to create those workflows for parts of our planning stage. And we do a lot of that for validation and implementation as well. Except we don't

**[0:11:49]** use sub agents for implementation. I'll talk about that in a second here. So yeah, we're in the VI planning stage now. And this is where, like I said, we don't have structured prompts. It's super basic here. I just describe at a high level what I want to build because

**[0:12:01]** I want my AI agent to be able to connect to my Obsidian vault. I give an example that I pulled from a past project that I want it to reference. This is just the high level. Let's start to get into the code. Then once we do this exploration

**[0:12:15]** and we're confident in its understanding and you can kind of elaborate more and and fix up some of its understanding, you make sure you're on the same page with it. Then you will go and create the initial MD. And so you on the same page, you did your planning. Now we start to

**[0:12:30]** add in our structure. And so in this case, I'm calling my initial MD OpenAI API compatibility. It's just a markdown document with that initial request that we have for our AI coding assistant. So we have the feature that we want at a high level, the endpoints that we want

**[0:12:44]** to build, some examples of how we want to interact with our agent. It's not super super planned out at this point, but this is our initial request that we're then going to turn into the full plan. That's the key here is at this point we're just creating our initial

**[0:13:01]** MD. And so we have that built out. And now at this point that is the end of our first conversation. We want to move now to another fresh conversation because we want to move on to the next stage of our workflow. Taking that request and turning it into the full plan with all

**[0:13:17]** of the context engineering. And so I've created yet another slash command for this part of the workflow. So I'm calling it create plan.md. And again, this is just an example of what your planning workflow can look like. You can build this however you want. Just generally, you'd want to kind of follow

**[0:13:34]** the principles that I have covered in this diagram. And so, I walk you through this three-step process. And now, I'm just building slashcomands and sub aents around this general flow, doing some things that are kind of more specific to my project as well. And so, you can build these kind of flows to however

**[0:13:50]** works best for what you are creating. And so for my create plan, basically I'm just telling it to take the requirements document, that's what we just finished creating, and then go through a few different phases. So read and understand the requirements. We have a research phase where I wanted to use web

**[0:14:07]** searching for rag and also archon if it is available. And then I also have this codebase analyst sub agent. So I created a sub agent that it calls upon to do a lot of that extensive research. And not to get too deep into sub agents right now, but they're very powerful because

**[0:14:23]** they have their own context window. So they can do a ton of research and then output a summary of that without it polluting our primary conversation. So we keep our context window concise and focused. And so this sub agent just does a lot of research around our existing

**[0:14:38]** codebase to figure out exactly what our plan should look like. So we need to create you know that implementation plan task by task our desired codebase structure the documentation we want to reference and the codebase analyst and this whole slash command helps us create that and so I'll go back into the

**[0:14:55]** conversation and kind of show you what that looks like. So first of all I ran the create plan here with the requirements document passed in as my argument in the command and it starts by calling the codebase analyst sub aent. So it does a ton of research. It figures

**[0:15:10]** out exactly how we're going to be integrating this new feature in our codebase. It does some rag searches with archon. It does some codebase example searches and then it produces our plan. And so this is kind of taking that initial MD to the next level with all of

**[0:15:27]** that context engineering. And so these things I've been speaking to, we'll find those here. Like here is our step by step all the tasks that we want to implement. And it gets really granular here which is always good. If you want to be specific with AI coding assistance, that's exactly what this

**[0:15:41]** plan gives us. We have the different files that we need to modify, the ones that we need to create, existing patterns to follow, everything that it needs to get the job done. Super cool. And we have the success criteria as well. Maybe I could add like a desired

**[0:15:56]** codebase structure, but it's more about editing existing files. So I think like for what I'm building here, this plan is absolutely perfect. So now that we have the plan created, that is the end of what I've gotten to so far. So now with that comprehensive plan, well, first of

**[0:16:12]** all, I'd recommend validating it, actually making some adjustments with the help of the coding assistant if necessary. But once you're confident in the plan, then it is time to move on to implementation. Now, for implementation, the most important thing is to have a workflow that guides the coding

**[0:16:28]** assistant on how to knock out the tasks one by one. And the task management here is the most important thing, especially if you're trying to do quite a bit in one request. If the coding assistant tries to do too much at once, that's when you have a lot of hallucinations.

**[0:16:44]** And so tasks are your way to have a larger request, but still have it be very focused and granular on one little thing each time. Like if we go back to our planning document, you could see that like we have very granular tasks that we're having a knockout one by one.

**[0:17:00]** And so we're going to create another slash command to define this workflow. And exactly what your slash command looks like depends entirely on what you're doing for your task management. And so in my case, I'm using archon for task management. And so my workflow speaks a lot to how exactly I want to

**[0:17:18]** use archon. Now it's not the case that you have to use archon. That's the point here is this is just an example of my workflow. So it's creating all these tasks here for this OpenAI API compatible implementation. But you could be using Cloud Taskmaster or another Markdown document to manage your tasks.

**[0:17:35]** However you want to do it, even just the internal task management tools that we have within these coding assistants like Cloud Code. The important thing is just to create a workflow around the task management. And so when I go to my execute plan here, I'll just show you

**[0:17:50]** really quickly at a high level what this looks like. And this might end up looking a lot different for your workflow, but I want to read my plan that I've created. This could be a PRP if we're using the PRP framework or, you know, it could be the project brief if

**[0:18:02]** we're using the BMAD method. And then I want to set up the project in Archon if it isn't already. Create all these tasks. I want to analyze the code. And then I have this cycle here where I need to mark a task as to-do or doing. And then it'll go through that task and then

**[0:18:19]** move it to review and then move on to the next task. And it'll do that in a cycle until everything is done. And then it'll move on to validation. And we actually have a sub agent to help with validation as well. So it'll execute this guy to within its own context

**[0:18:33]** window, create a bunch of tests, and make sure that our code is good, and then report back to our primary coding assistant if there's anything that needs to be fixed up. And so yeah, generally my process around validation is while the coding assistant is running, I will validate to make sure that it's using my

**[0:18:49]** MCP servers properly, that it's editing the right files and looking in the right places, I generally watch it at least kind of closely to test these things. And then once we have the code outputed, this is where our plan should also speak to how the AI coding assistant can

**[0:19:05]** validate its own work. And then we want to be a part of this process as well. Performing a code review because we don't want to vibe code. We want to actually look at and understand the code that is being produced and then running any kind of manual tests that we want to

**[0:19:17]** like actually talking to the agent in Obsidian like we'll see at the end of this video here. And sub aents can be great for validation because again we want isolated context windows to not pollute our primary conversation so that we can have a sub agent run a bunch of

**[0:19:32]** different tests to make sure that everything is rock solid. And one last thing for validation. There's another agent that I love using to review my work. You can think of it as another validation sub aent and that is Code Rabbit. an AI powered code review platform and they are sponsoring this

**[0:19:49]** video but I do use them every single day for my work and it's free for open source projects so naturally I've integrated code rabbit with archon every single pull request that is made to the archon GitHub repository is automatically reviewed by the code rabbit agent it analyzes my codebase

**[0:20:08]** deeply and my poll request it understands how it affects things and outlines that here it gives me a beautiful sequence diagram for every PR it suggests reviewers and of course we have the allimportant actual code review here with the changes that it recommends and I will literally take these and give

**[0:20:24]** them to claude code or whatever AI coding assistant I'm using. So, it's become a crucial part of my development workflow, and I'm just very thankful to have Code Rabbit for Archon, especially with all the poll requests that we're managing every single week. And they have a CLI tool now, so you can use Code

**[0:20:41]** Rabbit not just to review your PRs in GitHub, but now you can also use it as one of your agents reviewing things locally when you're developing on your machine. Code Rabbit also offers free trials for their paid tiers and is free for open- source software like Archon like I mentioned earlier. And the

**[0:20:57]** reviews with the CLI and IDE tools are free with rate limits that apply of course. And so if you've been feeling overwhelmed with the amount of code that you've been creating with AI tools, this is your ticket to maintain quality without slowing down. I'll have a link to Code Rabbit in the description. I

**[0:21:14]** would definitely recommend trying them out. So on to implementation in action. And this is pretty simple overall because we did so much of the work up front in the planning stage. So now thanks to the plan that we've generated that has all the components of context engineering. All we have to do is

**[0:21:31]** execute our predefined workflow passing in the plan that we have created. So again we have the execute plan/comand where we take in our requirements. We break it down into all those tasks. And in this case I'm doing everything in archon. And so I went through this implementation already. So, we have all

**[0:21:47]** the tasks in done. It knocked it out 100%. Is actually really incredible. And so, I'll go back to the terminal here and show you uh the conversation that we have. And so, it's partially cut off because there's a lot of work that it did here. But, yeah, we just sent it in

**[0:22:01]** to implement literally everything. And it goes for a while here. There's a lot that it's taking care of, but I have quite a bit of trust in the coding assistant because of all the context that I gave it and how things are split up between the different tasks. And you

**[0:22:15]** can see that was doing a lot of the task management with archon here as it is changing things. So it's interled managing tasks making changes and then going through that cycle. And then at the very end here we have validation. And validation is kind of mixed into implementation as well. And that is

**[0:22:32]** where we invoke our specialized validator sub aent. And so it went for quite a while here. Actually probably longer than I really needed it to go. It did a lot of validating with unit testing and other things to make sure that our code is rock solid. And the

**[0:22:46]** important thing that I want to call out here is that for the validation that's when we go back to using sub aents. So planning and validation we use sub aents but I on purpose did not use any sub aents during the implementation. And the reason for that is when we're actually

**[0:23:03]** making the code changes doing the implementation, we want everything to remain in the primary context window for cloud code or whatever our AI coding assistant is. If we have different sub aents implement different parts of our codebase, they're not really communicating with each other and memory is not shared between them. So you start

**[0:23:22]** to have conflicting changes and overlapping changes. It becomes a mess when you use sub aents for the actual code creation. And so generally I always use sub agents for the research upfront and then also having a validator specialist so I can give a very specific system prompt to this agent for how to

**[0:23:39]** validate my code. So that's the really important distinction I want to make there. Otherwise for slash commands I'm using them in every single part of the implementation like you saw. And then global rules. I haven't covered too much in this video, but really this is what you'd set up in your planning phase

**[0:23:53]** initially. When you're trying to just think at a high level like what are the instructions that I want my coding assistant to follow literally no matter what I'm doing, starting the project from scratch, adding in a new feature, doing a bug fix, there are a lot of those kind of golden rules that you want

**[0:24:07]** to put within your claw.md whatever that file is called for your coding assistant. And then of course the last step here is our own review. You definitely want to perform a code review on everything that was outputed by your coding assistant. Otherwise, you're still just reverting back to Vive

**[0:24:23]** coding. So, perform a review and then run manual tests as well. Like I have my agent API running again in Docker. I have the connection already set up in Obsidian. So, I'll just show you this really quick. I'll go into my chat window here and I'll say summarize. And

**[0:24:36]** then I'll just reference this whole diagram that we've been going through throughout this video. So, I'll send this to send to my agent. It's communicating to literally what we just built using the OpenAI API compatible endpoints. And there we go. We have a summary of the full workflow based on

**[0:24:51]** our diagram here. Absolutely beautiful. The implementation is flawless. And now we have this workflow that we can use for other things as well. I mean the whole planning slash commands and primer that I had and the sub agents for validating and executing and my whole process for task management in archon

**[0:25:06]** like it's not actually that specific to this specific implementation. Like I can take this and reuse it for anything that I want to build. And that is the main thing that I'm trying to describe to you in this video is how you can create these combinations of rules and sub

**[0:25:24]** agents and slash commands and even just like a mental model of how you plan then implement and validate and like that becomes your process that you can reuse for anything. you've now built a system for working with AI coding assistants. And even when you start to incorporate other things like the PRP framework or

**[0:25:39]** the GitHub spec kit, you're still following that same mental model, just using those approaches to basically augment what you have and you can tweak it to your needs. So that's everything that I've got for you today. If you appreciated this video and you're looking forward to more things around AI

**[0:25:55]** coding and building out these kinds of workflows, I would really appreciate a like and a subscribe. And with that, I will see you in the next
