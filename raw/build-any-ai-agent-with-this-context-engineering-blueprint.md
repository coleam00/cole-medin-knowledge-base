---
type: raw-transcript
title: "Build ANY AI Agent with this Context Engineering Blueprint"
youtube_id: ni8Xl0ANx0E
url: https://www.youtube.com/watch?v=ni8Xl0ANx0E
slug: build-any-ai-agent-with-this-context-engineering-blueprint
published: 2025-07-23
duration: "0:24:52"
fetched_at: 2026-07-21
immutable: true
---

## Transcript

**[0:00:00]** Recently, I have been obsessed with context engineering. I'll be the first one to admit it. But it's for a good reason. I've been pouring my heart and soul into developing reliable and even more importantly, repeatable ways to give super robust context to LLM so we can build anything. And what I want to

**[0:00:18]** show you right now is what I've been cooking up in the lab recently, working on context engineering, but for building AI agents in just minutes using paidantic AI. And as a part of this video, we'll even go through and use this template to build an AI agent together. Now, using AI coding

**[0:00:36]** assistants to build AI agents should be pretty straightforward. I mean, there's a very standard way to define our prompts and our tools and our dependencies. But if you've ever tried it yourself, you know, it is not that simple. We can't just go into our windsurf or our cursor or our kirao or

**[0:00:53]** our cloud code or the millions of other tools that we have right now for coding and just say something like build me an AI agent for customer support. I mean you just know that this is not going to cut it. I mean, you might get something with this, but it's going to be more of

**[0:01:07]** a demo that definitely breaks with real users and real data, and you're probably going to get stuck in the hell that we've all had with AI coding assistants at some point where we have just this infinite loop of iterating on a few problems. But the problem here is not

**[0:01:20]** your AI coding assistant or LLM. It's the context that you are providing. We can't just vibe code and skip right to implementation. We need an entire planning phase up front to sharpen our axe and give the context necessary for the AI coding assistant to have what it takes to plausibly oneshot the solution

**[0:01:40]** effectively. And that is what context engineering aims to solve and the strategy that I've been focusing on a lot recently is using Arasmus' PRP framework that I've been talking about a lot on my channel recently. And so I have this template available for you that I've covered on my channel and now

**[0:01:55]** I have a specific version of it that is hypertuned for building AI agents with podantic AI. This is the focus of this video here and it's going to be fun. Now the PRP framework is just one way to context engineer, but it is my favorite by far and it's so straightforward

**[0:02:11]** because we are using the AI coding assistant in very strategic ways to help us generate the context. That's the key. And so going back to the root of the repo here. It's just a three-step process that we have to follow with the PRP framework at a high level. So first

**[0:02:24]** you have to edit a file to describe in detail the application or in our case the agent that we want to create and then we take this initial MD and we use the AI coding assistant to help us expand that into a full what is called product requirements prompt. It's like a

**[0:02:41]** PRD if you're familiar with that, but more specifically crafted to be a prompt with extensive context to help the AI coding assistant then build out our feature when we execute the PRP. So very simple three-step process. And the main thing that we do here, if I go into the

**[0:02:58]** PRP folder, we have this template for a base PRP. So we essentially take this combine it with our own feature requirements in our initial MD and this creates the full set of context that we need that includes things like documentation to reference the code structure that we want at the end any

**[0:03:16]** gotchas that we have best practices and patterns for developing whatever we're trying to develop. It's a very complete set of context. And so the best part with this is I can take this base PRP. I can take the other parts that we have here like our commands to generate and

**[0:03:35]** execute PRPS and I can hyper tune these to specific use cases. And that is exactly what I've done here for Pantic AI for you to be able to create AI agents super easily. So, I'm just trying to set the stage here and show you what went into creating this because I spent

**[0:03:50]** hours and hours pulling in my old Pantic AI projects, doing research and finding best practices, and then essentially creating a PRP to create this template for you. So, I used AI coding assistants to help me build this as well. And so, like for example, we have a base PRP,

**[0:04:07]** but now hyper tuned to Pyantic AI. So, I have like best practices and examples and patterns built in for Pyantic AI specifically. So now when you go through that three-step process of describing your agent and then generating the PRP and executing it, it has all this information for Padantic AI already

**[0:04:24]** built into it. And this reduces hallucination so so much. And I'm going to keep doing this for other use cases as well. Like I have this folder here. I showed MCP servers in my last video. I'm going to keep building more and more just creating these super beautiful

**[0:04:39]** starting points for you. So, you have to spend hours and hours less context engineering because I've already done it for you. Like, I can take these templates, give them to you, and you can basically just like dive right into creating your agent in just a couple of minutes. It's that easy. And that's what

**[0:04:54]** we're going to be doing in this video. I'll show you how it works. And we'll build an AI agent together that's not actually that trivial. It's an agent that can do web research and manage our inbox, doing things like drafting emails as well. So, this is what we're going to

**[0:05:07]** create together. And I've actually already built this with both Claude Code and Curo before recording just to validate this. And I also literally used the template to build an agent to then refine the template more like just fixing up things that I didn't quite get right. So yeah, trust me, I put a lot of

**[0:05:23]** time into building this template for you. And so that's enough of me talking about it. I just want to like actually dive in and build the agent out with you now. All right. So I've got my repo cloned locally. Now, we can dive into building our AI agent with the PRP

**[0:05:37]** framework and this template that I have for you, which I'll have a link in the description to this template and the entire context engineering repo. This is all open source and available for you. And like I said, I'm going to keep building out more use cases as well. In

**[0:05:50]** fact, I'm going to be making this a project in the Dynamis community. And so, if you want to get way more involved with AI coding and context engineering and you want to be a part of an awesome project, definitely check out Dynamus.ai. We got a lot of awesome

**[0:06:03]** stuff going on there for AI coding and context engineering. But anyway, back to our readme here. Let's go ahead and get started getting ready to build our agent. So, the first thing after you clone this repository, we want to take our Pantic AI template and we want to

**[0:06:18]** copy it to a working directory essentially where we're going to take the template and build it into a complete agent. And I've set it up this way in case you want to reuse this template many times. So, we have this target directory where it's just going to copy everything that we need for our

**[0:06:32]** slash commands and our global rules and our base PRP to wherever we want. And so, within my terminal here, I'm just running the copy template.pycript like the readme says. And I'm going to have everything copied over to this folder. So, it's going to happen just like pretty much instantaneously there. There

**[0:06:49]** we go. We copied over all of our examples. We have that initial MD that we have to fill out. We have our base PRP and then our slash commands. Which by the way, if you're not using cloud code, you can still use these slash commands. You just basically in your

**[0:07:03]** prompt to your AI coding assistant, tell it to use the command as the prompt. And I actually did that with Kira. I'll just show you an example of this really quick. I'm not building with Kira in this video. I'm going to be building with cloud code. But just to show you

**[0:07:15]** that I've done this with other AI coding assistants as well. And so you can see my prompt. I literally told it use.cloud/comand/ cloud/comand/execute podantic AI PRP as your prompt and then the argument because we have to pass in the PRP that we want to execute. I just give it the the name of that file as

**[0:07:32]** well. And there we go. Kira goes ahead and does all the implementation just like we would see in cloud code. And it did a phenomenal job by the way. Like I'm very impressed with Kira as one of the new up andcoming AI coding assistants. Definitely let me know in

**[0:07:46]** the comments if you want me to dive more into Kira or other AI coding assistants. But right now, Cloud Code is still my primary driver. So, I'm going to be focusing on that in this video. But yeah, so we've got our new repository set up. And so, I'm going to copy this

**[0:07:59]** directory. I'm going to change into it. And then I'll just open in my ID, which I'm just using WinSurf here, but I open up the terminal to use Cloud Code. So, I'll I'll go ahead and do that right now. So, I'll close Cascade. We're in a terminal. I'm using Windows, so I'll go

**[0:08:13]** to Ubuntu, so I can access Claude here. All right. So, there we go. And then what I want to show you really quickly is what is copied over for this template. So we have our claw.md. These are our global rules that I've also hyper tuned to building pideantic AI

**[0:08:27]** agents. And you can read through all this if you are curious the way that I've specified you know like the general file structure for agents best practices for configuring environment variables and how we set up the specific provider and LLM that we want to use. There's a lot of work that I put into this. And

**[0:08:42]** then we have that podantic AI specific base PRP. And then the main thing that I want to start with here is our initial MD because this is our first step. And we're going to dive into this now. We're going to set up all the requirements around our agent and then generate the

**[0:08:57]** PRP based on that. The sponsor of today's video is Scribba, a platform that turns coding tutorials into pair programming sessions where you can literally edit the instructor's code in real time. And there are exercises that are built right into the tutorials. It really does revolutionize the way that

**[0:09:14]** you learn how to code. And while AI can help us code faster, like we're covering in this video, it is still crucial for you to understand the fundamentals, both backend and front-end development. I mean, there's a reason why I talk so much about validation when I'm covering the PRP framework. And Scribba recently

**[0:09:32]** released their full stack developer path. Over 100 hours of incredible content taking you from beginner to pro for both backend and front-end development, so you can develop some of the most in- demand tech skills in the industry. So, just to show you really quick how powerful and unique Scribba

**[0:09:49]** is, take a look at this. So, I'm going to play one of the videos here. And I have the instructor muted, but he is talking right now. He's moving his mouse around on the screen. So, he's in the middle of showing me something, but at any point in the lesson, I can pause the

**[0:10:02]** video. I can go to any of the files just like I'm in a text editor on my local computer and I can change anything like I could say instead of add ingredients, add food. I can do control S or run in the top right. And there we go. Our

**[0:10:14]** preview is updated live. So, we can update to just tweak things and try things out at any point during any video. And then also there are these challenges that we have throughout the content where they explicitly will ask us to implement something. So we really are pair programming as a part of our

**[0:10:29]** lessons. It's so powerful. It helps you learn so fast. Also, Scribba has a lot of other courses as well like these ones that they offer for AI. They even partnered with Mistl Hugging Face and Cloudflare recently to bring these to you guys. It's so cool. You also get AI

**[0:10:46]** feedback on your code in all of your courses. and they have a super supportive community through Discord. So really, Scribba is the place to go if you want to level up your tech skills, master what is in demand right now. So I'll have a link in the description to

**[0:10:59]** Scribba. I definitely recommend checking them out. So first of all, when we build an AI agent with Pideantic AI, and really this is going to apply no matter the framework you use. Agents generally consist of three parts. And I'm just showing the weather agent from their documentation just to give you a highle

**[0:11:15]** overview. This is why I crafted the initial MD template in the way that I did. So, first of all, our agents will always have dependencies. These are things that we need in our tools like API keys, database connections. In this case, we have an HTTP client that we

**[0:11:31]** need to browse the internet. And then we also have our agent definition itself. This is the second component where we have things like our system prompt. And then last but not least, our agents always have tools. These are functions or MCP servers that we attach to our agent so it can actually do things on

**[0:11:47]** our behalf and that's usually most of the implementation for our agents. So those are the three components and that's why I've crafted the initial MD in this way because it's very important to be specific to the AI coding assistant when building agents what you're looking for for those three

**[0:12:03]** components. And so first of all at a very high level we have our feature. What is the AI agent that we want to build? and you just want to replace everything in brackets here in the template. I have a really simple, like super super simple example here as well.

**[0:12:17]** You definitely want to be more detailed than this, but this is just a starting point for you. And then diving into the exact tools that you want. Like for our research agent, we want our agent to be able to use, let's say, the Brave API to browse the internet and summarize web

**[0:12:30]** research. We want another sub agent to manage our inbox and do things like draft emails. Like, get specific for the tools here. And after I walk through this, I'll show you what my final initial MD looks like as well. And then for dependencies, again, things like API keys and database connections for our

**[0:12:47]** system prompt. You don't have to write out the entire system prompt here, but you can if you want. Otherwise, you can just kind of generally describe what you want in your system prompt to make sure that you're steering your agents correctly. And then what I generally include for all of my PRP initial MD

**[0:13:03]** templates is a section for examples. So you could pull past projects that you've worked on. Like I have a lot of Pantic AI agents I've already built. So I have some of these put in the example folder already. So we kind of have a starting point for examples. So you can just go

**[0:13:19]** off of this if you want. And this could also be resources you found online. Maybe even just taking things directly from the Podantic AI documentation, putting those in the example folder as well. And I just find that examples are so so powerful for AI coding assistance. is even better than just looking at the

**[0:13:36]** documentation or doing web research. But documentation still is important. So speaking of that, we've got a section for that as well. Like here, just to show you kind of what this looks like, I call out some of the links that we have from the official Pantic AI docs for

**[0:13:48]** things like creating agents and integrating tools. And then the last section that we have here, which is actually pretty important, is just a place for you to put any other kinds of considerations that you have for your AI coding assistant, like the way that you wanted to manage environment variables,

**[0:14:02]** for example. And this is also the perfect place to put any gotchas, as I like to call them. Like when you've used AI coding assistance to build agents in the past, for example, what are those things that it always messes up on? And this is your place to correct that

**[0:14:17]** behavior because usually when it messes up on something in one project, it's probably going to do something like that in another project. And so just being able to adapt your prompting and your context as you learn the kinds of things that it likes to mess up on. So yeah,

**[0:14:31]** very important to include that in this section as well. And so with that, I'm going to go ahead and paste in my full initial MD that I have for my agent. And there we go. All right, paste it in. And I'll have this linked in the description as well if you want to see like the full

**[0:14:45]** agent that I build from this process, too. But yeah, I'm just building a padantic AI agent that has another agent as a tool because we're going to have our primary research agent and then an email draft agent as a sub aent. I'm going to keep it very simple here with

**[0:14:58]** the tools that I'm giving it as well. So, I'm going to give our research agent the ability to search the web with the Brave API. And then it has a tool to also delegate all the email related stuff like drafting emails to my email sub agent. And so, a rather simple

**[0:15:14]** example just to demonstrate things rather quickly for you here, but it's still like more than just a super super trivial agent. Like you could definitely take this further to make it like a real agent you would actually use. And then for dependencies, we just need the Brave API key and then everything for Google

**[0:15:30]** O. I have general instructions for the system prompt that I want for both agents. I'm keeping the examples the same because I already curated a really nice set of Pantic AI agent examples for us. And then documentation, keeping it very bare bones. And then my considerations is kind of everything

**[0:15:45]** that I already had in the base initial.mmd just because those are the things that I found it usually messes up on. Like it doesn't handle environment variables correctly, for example. So that is my initial MD. Now I'll just do CtrlJ to open my terminal back up. And I'll go into Claude. And now all I need

**[0:16:01]** to do is generate the PRP based on the initial MD that I created. So it's slashgenerate pyantic AI PRP. I'll hit tab to autocomplete. And then the one argument that we need here. And we can go into this and see what that looks like. If I do Ctrl J to close the

**[0:16:17]** terminal again, we have the one argument which is our feature file. That is our initial.md. So it takes that. we have the rest of the context for how it needs to generate a PRP and validate it. That is all within the prompt here. And so going back to my terminal here, I'll

**[0:16:31]** just pass in the relative path to my initial MD. If I can type right. There we go. All right. So we got our initial MD. We'll send this in. And like I said, if you don't have cloud code, you're not using slash commands, you can just use this as a regular prompt. Tell it to

**[0:16:46]** look at this file for its prompt. So I'll send this in. And now this process is going to take a good amount of time because it's going to do a lot of research and architecting on our behalf, thinking through step by step what needs to go into the PRP and then putting it

**[0:17:00]** in there. And then our end result is we'll have a new PRP in our PRP's folder. So I will pause and come back once that is generated. All right, our PRP is now generated. And the next thing I want to go through with you is at least at a high level how we can go in

**[0:17:15]** and validate our PRP. You don't want to trust the AI coding assistant blindly. Validation is so important. And so, at least at a high level, I want to show you what that looks like. And if you saw my last video doing the similar process, but for MCP servers, a lot of this is

**[0:17:30]** going to be pretty similar. But I still want to dive in and show you what this looks like specifically for building AI agents with Pantic AI. And so, we took our base PRP for Pantic AI. We took our initial MD. This is the baby of those two things. And this is what we're going

**[0:17:47]** to use to build our agent. So you got core principles, what to do and what not to do for highle instructions. We have exactly what we're building here with all the documentation that we need. And this is a beautiful blend of resources online, existing examples that we have

**[0:18:04]** in our examples folder. It's going to load all these things into context when it first builds our agent. That's exactly what we want it to do. even including documentation for things like Gmail and Brave so it knows how to build our tools properly as well. AI coding assistants love to hallucinate the way

**[0:18:20]** that we use these specific APIs when they don't have access to this documentation. Now, one thing that this PRP doesn't have that I wish it did is the final code structure. And we have that called out in the base PRP. So maybe I'd go through and like ask it to

**[0:18:33]** iterate and add that into the PRP. And so there's definitely going to be some things where you go through this, you're like, "Oh, that's not quite right." and you want to edit it yourself or ask it to change. Like I said, be a part of the process here. Validate and iterate on

**[0:18:46]** the PRP before you send it in to execute it. And so, yeah, it's covering Pantic AI gotas and general best practices for using Pantic AI, talking about our stack. I'm not going to go through everything in detail here, but like overall, this is looking pretty good. And the last thing that I want to cover

**[0:19:02]** here is what are called validation gates. This is one of my favorite parts of the PRP framework because you always want to describe to the AI coding assistant in the PRP. What do you need to do to actually validate that your code is good? And it doesn't mean that

**[0:19:17]** it's guaranteed to be perfect, but having it do things like write unit tests and iterate on them until they are all passing. That kind of thing is just so so powerful. And in this case here, let me scroll down to the validation gates. I don't necessarily need it to

**[0:19:31]** do, you know, like security production validation and integration testing. So like this is something I usually end up cleaning up where it like goes a bit overboard with validation gates. So just to show you one example of how I will go in and change things before I execute

**[0:19:45]** the PRP, but otherwise this is looking really good. And then it also gives a confidence score, which another pro tip on this. What I can do is literally say, what would it take to get to a 10 out of 10 confidence score? And so it'll ask me a couple of follow-up questions to then

**[0:20:02]** adjust the PRP further to add anything that it's not really confident in right now. So this is just yet another thing to do um just to get better results once you go and do the implementation. And so yeah, it just says that it doesn't quite understand how to do the Gmail ooth 2

**[0:20:16]** flow right now. And so what I'm going to do off camera here is go through this process. I'm going to refine the PRP completely. Then I'll come back and we can execute it. All right, our PRP is now refined. I don't need to show you everything again. So, we can go ahead

**[0:20:31]** and move on to executing our PRP. So, when you copy over the template into a new folder with the copy template Python script, we take the original readme and I just rename it here because you also want your AI coding assistant to produce a brand new readme for your agent once

**[0:20:47]** you build it. So, I just re renamed this to readme template. But yeah, this has all of our instructions that I was showing you in the GitHub earlier. So, we filled our initial MD. We generated our PRP. Now, we can execute it. And so, the command for that, and actually what

**[0:21:02]** I recommend doing no matter what is clearing your conversation before you execute the PRP because you don't want to have all of the old context left over from when you were generating it. And so, I'll just do exit here. Go back into Claude. You could also do the /clear

**[0:21:16]** command. And then, no matter your AI coding assistant, you can just start a new session here. And so then the command that I'll use now is slashexecute podantic AI PRP tab to autocomplete. And then I'll pass in the path to my PRP. So it's PRPS research email agent CLI.md.

**[0:21:34]** That's just the name that the AI coding assistant came up with. There we go. All right. And then I'll do shift tab to enable autocomplete. And we are off to the races. All right. Our agent is being created now. And this process will go for a good amount of time because we

**[0:21:48]** have such an extensive set of instructions here and so much context for it to sift through as well. But man, the results that we get from this time and time again just blow me away. And so yet again, I will pause and come back once we have the initial version of our

**[0:22:04]** agent created. And there we go. Our agent is now complete. And I did iterate two times off camera just to fix a couple of small things. It wasn't handling the conversation history quite right in the CLI and then all of the tests weren't quite passing. So I wanted

**[0:22:18]** to make sure that was in tip-top shape, but otherwise this was amazing. It almost one-shotted the entire agents. And actually there's two agents here because we have the one for research and then the one for emails. And I went through the code and I validated everything after as well. And it's

**[0:22:33]** really important to do that to make sure that it isn't just vibe coding, right? Like you want to understand what it outputed here and validate it yourself. But this all looked really good to me. And you can view this repo if you want. I'll have this linked below as well if

**[0:22:45]** you want to see the final result for yourself. And then I literally just followed the readme to get everything set up myself. My environment variables, the credentials for Gmail, my virtual environment. I got all that set up. And so now I can run this in the command line. So python research email cli.py.

**[0:23:02]** We'll have a very similar demo here to what I showed at the start of the video. So, I can just say something simple like search for the latest on claude code and send a draft of the findings to and I'll just do my own email here. It doesn't

**[0:23:15]** really matter for a simple demo. So, it's going to use the Brave API first. There we go. Search in the web. And then at some point, Yep, there we go. It's going to hand off to my email sub agent now to create that draft for me. And it

**[0:23:28]** takes a little bit because it's going to craft the full email here. But in a second, it'll tell us that it has drafted the email. There we go. All right. Perfect. So, yeah. Now, I'm going to refresh my drafts on my other monitor here. All right. Nice. Yep. I'll bring

**[0:23:42]** it over. There we go. Take a look at this. Latest updates on cloud code to myself. And yeah, I mean, the email might be a little corny here. You can definitely work on the system prompt to like make it so that this actually sounds like what you want it to sound

**[0:23:55]** like. And really, there's probably a lot of room to continue to iterate on this agent here. This is just more of a demonstration I wanted to have for you for starting with the PRP framework to begin a new project. You can definitely take this a lot further as well. So, I

**[0:24:11]** will have links in the description to the Pantic AI template. You got the read me to go through the same process yourself. I'll even link to this agent that I created as well, so you can take a look at the final results if you want. That is everything that I've got now for

**[0:24:26]** context engineering the PRP framework for paidantic AI agents. I hope that you found this really valuable really taking this and building any AI agent that you want with it and certainly a lot more templates coming out for other use cases soon as well. So stay tuned for that. If

**[0:24:41]** you appreciated this content, you're looking forward to more things with AI coding and AI agents, I'd really appreciate a like and a subscribe. And with that, I will see you in the next
