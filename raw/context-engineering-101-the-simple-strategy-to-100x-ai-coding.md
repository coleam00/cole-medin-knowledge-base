---
type: raw-transcript
title: "Context Engineering 101 - The Simple Strategy to 100x AI Coding"
youtube_id: Mk87sFlUG28
url: https://www.youtube.com/watch?v=Mk87sFlUG28
slug: context-engineering-101-the-simple-strategy-to-100x-ai-coding
published: 2025-07-16
duration: "0:37:46"
fetched_at: 2026-07-21
immutable: true
---

## Transcript

**[0:00:00]** Context engineering is the new big thing for AI coding. Not because it's brand new, but because people are finally acknowledging that putting the time up front to provide extensive context to AI coding assistance is what separates real results from vibe coding and basic prompt engineering. And most people are

**[0:00:18]** still experimenting with these ideas without a true systematic process. And so in this video, I want to dive into using context engineering for real production builds. essentially taking my template that I covered on my channel recently, but going much deeper for you. Now, here's why context engineering is

**[0:00:36]** such a big deal. We know that vibe coding builds prototypes that break when you try to scale. And prompt engineering is all about word tweaking. Working with specific phrases to get single better outputs from LLMs. In fact, the way I've heard it recently is context engineering is a superset of prompt engineering.

**[0:00:54]** It's a part of it, but context engineering is so much more. It's providing all information, examples, best practices, constraints to AI coding assistants upfront. It certainly is a time investment, but man will it 10x your process for building literally anything. And I mean that. Now, there are many ways to go about context

**[0:01:13]** engineering. But the strategy that I keep coming back to time and time again that my template for you is also based on is the PRP framework from Raasmus. And this is just genius. And Raasmus is actually a guest for a part of this video today. So I'm really excited for

**[0:01:29]** you to see that. He's going to dive into PRP, his philosophy behind it, why it works so well, how you can get started with it right now. And then what we've done together is we have actually taken my base template that I have in the context engineering repo and we've made

**[0:01:43]** one that's specific to building MCP servers. So you can use the PRP framework to build any production ready MCP server that you want just as a super practical use case. And we're actually going to go through and build one together in this video using this exact blueprint. So let me show you what I

**[0:02:00]** mean. If we go back to the root of the context engineering repo, which this is the template that I'll have linked for you in the description of the video, by the way, everything that we have here is a generic template for using the PRP framework. Like if we go into our slash

**[0:02:14]** commands here, these are just very generic slash commands that would work no matter the application that you want to build. And then if we go back out and we look at our PRPS, we have the template here. Again, just very, very generic. This applies to any kind of

**[0:02:28]** software, but there's certainly an opportunity to make a template for you that's already crafted to be much more specific to a certain kind of use case. And that's exactly what Raasmus and I have been working on for you. So, we actually took the productionready Cloudflare MCP server I showed in the

**[0:02:46]** last video on my channel and we built a template around it. So, we're going back here to the use cases MCP server folder in my template. We've taken the MCP server that I built my last video as an example built into this template and if we look at the slash commands for

**[0:03:02]** example, we've made things much more specific to building MCP servers. And even more importantly, we did the same thing with the base PRP. This is the reference that we use to create that full PRP. And now everything is very specific to building MCP servers. And so now you can use this as a launching pad

**[0:03:20]** no matter the MCP server that you want to create. And you're going to get much better results because things are so hyper tuned to building an MCP server. And by the way, going through this process yourself to build an MCP could not be easier. And this is what I'm

**[0:03:35]** going to show you how to do after we have our chat with Raasmus. So literally you just have to go into this initial.mmd file which I talked about initial.md in my first video on context engineering. You fill out the information for the MCP that you want to create and then you generate your PRP

**[0:03:50]** with this slash command which can just be a prompt for any other AI coding assistant besides cloud code. And then it's important to validate the PRP and be a part of this process. Don't trust the AI blindly. But then you can execute your PRP and this is going to build your

**[0:04:05]** MCP server and you can just iterate from there. It is that easy to get started and a lot of this is revolving around the power of this MCP PRPbased template that we've crafted for you. And this my friend is just the beginning. Actually a huge project that I'm starting in the

**[0:04:20]** Dynamis community is essentially building out a massive repository of all of these use cases. So no matter the programming language that we're using or the type of application that we're building, there's going to be a template here using the PRP framework, but much more hyper tuned to what we want to

**[0:04:36]** build. And that's exactly what I'm showing you here with MCP just as a super good example. And by the way, if you're interested in this and just taking your AI coding to the next level in general, definitely check out Dynamus.ai. There's so many things happening there like building out all of

**[0:04:51]** these PRP templates. So, I'm about to show you a live example of the MCP server that we built based on this template, and we did it in two shots. There was one follow-up prompt that we had to do to fix two bugs. But after that, we have 18 perfectly working tools

**[0:05:07]** in this very non-trivial MCP server. It's so cool. This is the PRP taskmaster MCP. You give a PRP and it'll extract tasks based on that and help you manage them. It is very similar to Claude Taskmaster but for PRPS instead of PRDS. Now it's not the most practical MCP

**[0:05:28]** server though I will probably be building it into Archon at some point. So stay tuned for that for Archon version two. But I wanted to give a nod to Claude Taskmaster because it really is an incredible MCP for context engineering. And I thought this would be a good example showing how we can

**[0:05:43]** replicate something that's already out in the wild that is really incredible and like I said not trivial. And so I've got a prompt pre-crafted here. And this is what I love doing when I'm testing an MCP server for the first time. I just say, "We've got this new MCP." I tell it

**[0:05:57]** what it's responsible for doing. And then I just say, "I want you to test all the functionality of this server with a flow that actually makes sense for starting a new project, adding tasks and dependencies, documentation. We have the tools to manage all of these different things. And I'm just saying don't go

**[0:06:13]** overboard. We just want a simple demonstration here and then create a sample PRP just to start things off. So I'm just using mock data here and I've got my database already set up. So we have our projects table tasks task dependencies. There's quite a bit that's going on behind the scenes to manage

**[0:06:30]** everything with this MCP. And so yeah, let's just go ahead and kick things off here. And so it's going to start by mocking a PRP, sending that in to extract the tasks from it. And so I'm going to pause and come back once it has done this because this part takes a

**[0:06:43]** little bit. is actually using the anthropic API under the hood here. And there we go. Our project is created. We can actually verify this. So, if I go to the projects, yep, we got a simple to-do app that we've have added to our database. And now it wants to list

**[0:06:56]** projects. So, we'll go ahead and let it do that. And then we're going to also have the tasks already in here. So, if I go into my tasks, we can see that we have a few already. And so, now it'll just go through list the tasks and just

**[0:07:08]** kind of go through a mock flow, I assume, of marking some tasks off. Yep. So getting the project overview is probably going to add some documentation as well. But yeah, you can see how it it's just knocking out one tool at a time, testing everything for me so that

**[0:07:20]** I just know that my MCP server is working correctly. And especially when you are using something like the PRP framework and you're coding something with the help of AI pretty heavily, it is important to validate everything like you do want to test every single tool in your MCP server for example. And that's

**[0:07:36]** a big thing that we'll see in our conversation with Raasmus is validation is still super important. Like when you generate your PRP, you still want to make sure that you're analyzing it, being a part of the process, not just generating the PRP and then executing it, right? And it's the same thing with

**[0:07:52]** the output as well. Like you want to understand the code that it outputed. Validate that test things like I'm doing right here and have the AI coding assistant create tests as well. And so yeah, I think that's enough of the testing here. Everything is looking really, really good. I don't want to

**[0:08:06]** bore you with the rest of this demo, but yeah, that is our MCP server at a high level. And like I said, we could use this template to build literally any MCP server, and it's going to be production ready. And there we go. We have all of the core functionality tested for our

**[0:08:21]** MCP server. Things are looking really good. So, here's what's coming up next for you. First, a quick word from our sponsor. Then, we'll dive into the conversation with Raasmus. And man, that is one that you don't want to miss. It was a pleasure having him on the channel. And then last but not least,

**[0:08:36]** I'll show you my full replicable process for building this MCP server with the PRP template that I showed you already. This, my friend, is Peak AI coding. The sponsor of today's video is Lindy. Think of it like if AI and Zapier had a baby, but what really makes their platform

**[0:08:53]** stand out to me is their feature for parallel agents called agent swarms. Take a look at this. So you build your workflows just like you would with something like N8N, but you can create these loops here where it's going to spin up many different agents to knock out a bunch of tasks for you at the

**[0:09:08]** exact same time. So this workflow specifically is for deep research. And so I can have many agents spun up at the same time. You could change this to the top 10, the top 20. So to research all these subtopics at the exact same time. So it's much faster than something like

**[0:09:22]** OpenAI's deep research. And so just to go along with the theme of our video here, I'll ask what are the best strategies for using claude code. And we'll see in a second once it enters the loop, it's going to create multiple different agents all at the same time

**[0:09:36]** spun up to research different angles for my question. And so it'll still take some time because it does pretty deep research here. And so we'll see in a little bit all the loops will complete and then it'll give us our final response. And there we go. All the loops

**[0:09:50]** have completed. It's done. the deep research for each of my different angles. And then in a second here, we'll see the final summary spit out. So, this is the research that was done for each of these agents. And there we go. We now have our full deep research. Also, Lindy

**[0:10:04]** has partnered with Pipeream to give you more than 5,000 integrations across 25 different apps and 4,000 web scrapers through their partnership with Appify. There is not a platform with more integrations than Lindy. So, I'll have a link in the description to Lindy. You'll also get 400 credits for free to try out

**[0:10:21]** the platform when you use that link. So definitely go ahead and check them out. All right, we have the man himself here, Raasmus, the creator of the PRP framework, and I'm just really excited to bring you in, talk about the framework, your vision for it, your philosophy behind it, because there are

**[0:10:38]** a million ways to context engineer. It's a pretty new phrase overall, but it's not a new idea, right? Um, but the PRP framework is just what I've been going to time and time again recently. And it's just made my AI coding that much better, like 10 times, hundred times

**[0:10:53]** better. And so I just absolutely love it. And I know that you've been developing out this framework for over a year now, which is insanely impressive. And so I just wanted to hear from you what inspired this and where you're going with it. So yeah, if you want to

**[0:11:07]** feel free and just introduce yourself, kick things off um telling us about the PRP framework. Uh, by the way guys, we met in the Dynamis community and when he was first sharing this PRP framework, it just stuck out to me immediately. Like I knew it wasn't just another one of the

**[0:11:21]** thousand strategies I'd heard like this is the real deal. So yeah, let's hear from you Raasmus. Yeah, thanks for that intro. So yeah, um, first of all, uh, since you also featured the PRP framework in your context engineering video, just want to say thanks to everyone who has embraced

**[0:11:36]** it and sent me all of the amazing projects that you have built on top of it. uh I've seen some really awesome stuff there. Uh but yeah, so what uh PRP is, it's a product requirement prompt. I've spent many years as a product manager and business analyst writing a

**[0:11:53]** lot of technical documentation and PRDS in particular. So PRP is really my attempt at building a prompt framework around uh product management. So like bringing the context needed uh for a coding agent to build the feature or the product that I wanted to build. So that's uh uh the basic idea.

**[0:12:18]** Uh in in short I would like to just describe it here. So it's uh a PRP is a PRD plus curated codebase intelligence plus agent runbook and it's aiming to be the minimum viable packet an AI needs to plausibly ship production ready code uh on the first pass. So as you as you said

**[0:12:41]** as well I've been developing this for kind of over a year. It has had in that year it has many many shapes and forms uh and it started out using like aer and klein as the main drivers and uh yeah it's very inspired by in the devdan and

**[0:12:59]** the client community and the memory prompting uh framework uh that that a lot of people use over there but yeah that's how we got started. uh I needed it for a for an existing project that I was building at the time, valuation engine. So yeah, I I used PRP

**[0:13:16]** or the very baby version of PRP to to build that out and and ship it to production. So yeah, that's really cool. Thanks for sharing, Rasmus. And the thing that sticks out in this read me here is the industry mantra, garbage in, garbage out applies doubly to prompt engineering.

**[0:13:33]** And that is so true. And that also speaks to the fact that like prompt engineering very much is a part of context engineering and the PRP framework, but really those are a superset. There's so much more that goes into how we're engineering the context here, especially with the PRP framework

**[0:13:48]** and how far we can take things with it. And so speaking of that, actually, let's uh hop over to the template now in GitHub. Specifically, what we wanted to give you guys with this template is just a clear example of how you can apply the PRP framework to build something new.

**[0:14:04]** And so, this is very much based off of my last video on context engineering where I gave more of an intro, but now we're showing you a real example with a template that you can use literally to take this use a PRP framework to build any MCP server that you want. So it's

**[0:14:18]** also based on my last video where I showed building production ready MCP servers with Cloudflare and TypeScript, but now we've put everything related to PRP on top of it so that you can go through and build your own MCP. So Razis, I'll I'll just let you do the

**[0:14:32]** explaining for how this works and how people can get started with this. You're definitely going to do that better than me. Yeah. So that's exactly what you just described is what we did, right? So, we took what you did in your past two videos, context engineering uh with the

**[0:14:46]** PRP framework and also the MCP server uh starter template that you built and we put together specialized PRP prompts and templates that will help you build any MCP server you can build. And I can pretty confidently say that this is probably the easiest way to build an MCP

**[0:15:08]** server. So uh what you really need to do is you take your plan uh whatever you want to build and you define it in initial.mmd. So this can be uh try to describe it like as good as you can like all your tools you want to have your business logic in as much detail as

**[0:15:28]** you can. Uh and then you will uh take that plan and then you will run that through the PRP framework. So you can use LLMs to start planning your your work and everything. So I highly encourage you to use LLMs also in your planning and preparation. Uh then you will run the first slash

**[0:15:47]** command which is the PRB uh base create or MCP create and you will pass your plan as the argument. And what this really does is this is what uh this is where the context gathering part happens. So it will pull in all of the context that it thinks it's that it

**[0:16:06]** needs to to finish your work like all the uh context that the AI itself thinks that it will need to to complete the work uh of your plan and it will pull it into this base template. If we take a quick look at this base template though, we have already done a lot of that

**[0:16:22]** context engineering uh for you. So a lot of the references that the AI will need is already in here. So it will only build on top of what we have already created for you here. So this uh base template already has a lot of references to uh the template that Cole built uh

**[0:16:39]** last week. So it references all of the patterns, it references the tool, the tool registry, how to do that, the database and and yeah, it really references a lot of things here that comes from that template. Uh so uh when you run the first command, it will pull

**[0:16:56]** your idea and add more context really to this uh template as needed. The beauty of that is we have this template already made for you. So there's a lot of context engineering that goes into the PRP framework, but there's just a lot less when you have this as a starting point. And that's

**[0:17:17]** actually something that Raasmus and I want to start up really soon here is working on a repository of all of these base PRP templates. So no matter the programming language you're using or the specific type of project like an MCP server you want to make, there's going to be some template to give you this

**[0:17:32]** massive launching pad. So you can create all of this context but not have to do it all from scratch. Like you have this starting point and then also there's a lot of like manual work that goes into really making these PRPs robust as well. And I know that you wanted to touch on

**[0:17:46]** that too, Raasmus. Yeah, I mean you can just take the example that that me and Cole has built here like we spent a lot of time like manually or semianually I would say because we took a lot of help from cloud code of course to prepare the context

**[0:18:00]** for this base template. So uh whenever you have created your um like your base template, you always should read through it and make sure that it actually references the things that you uh want and that you need it to reference so that it doesn't say something weird. So

**[0:18:19]** a lot of time I spend a lot of time actually like reading through these and making sure that they are good before I execute them because especially when I execute things in parallel I need to make sure that they are not uh tangled too much. So even if I run them in

**[0:18:35]** different workies I don't want to have the conflicts when I try to merge it later on. So if if you want to scale this up especially, you need to make sure that they're not tangled, but you also need to make sure that they are actually following the business logic

**[0:18:47]** that you intend them to follow. So read through your your PRPs before you run the execute command, which is the last step. Yeah, definitely. Yeah, validation is always important and that's the big thing that like is so wrong with vibe coding, right? Is there just never that validation and we need that even for the

**[0:19:03]** context that we're engineering. And I think like the the last big piece that we haven't hit on here is our claw.md or just whatever your global rules are for your AI coding assistant, which by the way, you can use this whole process with the Gemini CLI or cursor or windsurf.

**[0:19:19]** You don't have the idea of slash commands like you do in cloud code, but you can just take these slash commands and then use them as regular prompts, right? And so, yeah, diving into global rules now. Uh, I want to dive into this with you, Raasmus, because I think a

**[0:19:31]** really big distinction we need to make here is when do you put context in the global rules like cloud.mmd versus when does it belong in the PRP? Yeah. So, uh, I I like to think of it like this, like I I treat my cloud MD as where I put like the constant rules that

**[0:19:51]** will very rarely change. So things that will be true forever in my codebase and things that will be added to my codebase that also will be true forever or for a very long time. So whenever you add like a new principle like a new naming standard or maybe a

**[0:20:07]** new uh function that is really really core to your codebase also you can add it there. Uh so so yeah things that will stay the same for a long time. Uh but also append new things that keep coming in. You can also put cloud MD files in specific folders that references

**[0:20:22]** specific things in that module or folder. That's also really powerful. Then I like to think of the slash commands as really where they should just be like dropins uh for for whatever uh thing you're working on. So they shouldn't hold any specific. So the create command is just a planning it's

**[0:20:42]** just like a huge planning workflow really. what like a research workflow that has really nothing to do with anything specific. It becomes specific because you pass in your specific plan. And the same goes with execute. Execute command is just a ch prompt chain or um a prompt that will

**[0:21:03]** tell the AI how to execute your PRP. So it has nothing to do with the PRP itself. And then the base PRP is really where you put your specific context to that specific piece of work that you're doing right now. Yeah, that's really good. And I just like the phrasing there like cloud.mmd

**[0:21:22]** is where the things go that aren't going to change because really when you start to work on existing codebase, you'll have kind of a mini PRP for each feature that you want to develop because there's always going to be slightly different ways that you want it to go about

**[0:21:34]** implementing a feature. But claw.md that's the things that are the same between all of those features. And actually that kind of leads to the next question that I wanted to ask you Raasmus is how well does the PRP framework work on existing code bases? I know it's something that people have

**[0:21:48]** been asking quite a bit. Yeah, I mean I think uh it's purposely built for working on existing code bases. So that's the use case I needed it for when I started building it. It definitely wasn't perfect when I started building it, but I bet I made a quite

**[0:22:05]** big bet that it would soon work well with with better model. And I think especially with cloud code, we have seen that happened. So like even the difference between how it worked with cloud 3.7 and cloud 4 is is like insane. Like I used to kick off like a 100 line

**[0:22:24]** PRP and and it would run it like reliably nine times out of 10, maybe seven times out of 10. And after cloud 4, I can kick off like a 500 line prompt reliably, a thousand line prompt semi-reliably. And I have have kicked off 1500 line prompts reliably, you

**[0:22:43]** know, not not 10 out of 10, of course, but you know, like experimentally I I try try a lot of things. Yeah. Yeah. And it's important to say like it ain't perfect. It definitely isn't. But it feels close. like it's just incredible the kind of things that we can build with the PRP framework and

**[0:22:59]** just using that as our way to context engineer. And uh the last question that I want to ask you Raasmus, actually the one that I've gotten the most ever since I made my context engineering intro video is why put this much time into context engineering? I know that we've

**[0:23:16]** talked about this throughout our conversation, but I definitely sense there going to be some people that are still hesitant to put this much time into sharpening their axe, so to speak. So, what would you have to say to that? Like, why should we put the time into engineering this much context?

**[0:23:32]** Yeah. So, for me, it's obvious because I come from product management. So, I used to do this anyways. So I used to do this type of work anyways but not for an AI assistant but for a team of developers. So it's really just builds on that like someone building a real project someone

**[0:23:50]** is doing this work whether it's you or whether it's an AI or someone else. So really thinking deep about the the important questions like why are we building this in the first place? Who are we building it for? How exactly should the user experience look like? Those are really important question

**[0:24:07]** questions to answer and then making the decisions of how to build that like when you build your first prototype of something or or a version of something you have to like make that decision and then go test it on users and when you work on a real existing codebase you

**[0:24:23]** will get a lot of that feedback from users already. So you can like build your PRP based on the user feedback that you're getting already. So that's that's why it works so well on existing things too. not only that you get already have user feedback to get but you also have

**[0:24:37]** an existing codebase to follow. That's exactly what this example is showing as well that when we have like like this couldn't have been possible to to oneshot this like large piece of work without having such a good foundation that this MCP server template really has. So the AI will have like all of

**[0:24:55]** these patterns to follow that already exists uh that will help us build this out uh reliably. Yeah, that is really good. Thank you, Raasmus. That's everything that I had for questions here and you just set the stage so well for why we should care about PRP and how it works too. And so

**[0:25:12]** now what I want to walk everyone through is a a live example using this template to build an MCP server from scratch. And so I'll show you everything that Rasmus walked us through, but we're going to go through it step by step. So I'll create that initial MD, right? I'll generate

**[0:25:28]** the PRP. We'll build the MCP server and validate everything. And it's just amazing the results we get. So thank you Raasmus for walking us through everything. And now let's get into the demo. So here we are in the readme for the MCP server template that I have in

**[0:25:41]** the context engineering intro repository. This is what I was showing earlier in GitHub. And so now I have it cloned locally. I'll walk you through the three steps here to create our MCP server from scratch with all the context that we have as a launching point. And so we'll create the initial MD where we

**[0:25:57]** describe the MCP server that we want. We will generate and validate our PRP and then finally execute it and then you can iterate from there and deploy to Cloudflare workers. And definitely check out my last video on this MCP server that I have as a starting point for you

**[0:26:11]** if you want to go into the whole deploy to Cloudflare side of things. And speaking of that MCP server that is a part of the context here. So we're essentially taking that MCP server turning it into a scaffold that we have in this template. So we have everything

**[0:26:26]** around PRP plus the MCP server as a scaffold. And then all we need to do with our PRP when we generate and execute it is essentially tell it how to take the skeleton of an MCP server and add all of our custom tools. That's what we're going to be doing here. And so we

**[0:26:42]** need to start by editing our initial MD. So that's within the PRP's folder. And then within here we can describe the MCP server that we want to create based on this template. And so I have an example kind of fully written out here. This is to build our PRP taskmaster MCP that I

**[0:27:00]** demoed earlier, but you can adjust this to whatever you want to build. I just generally recommend keeping the feature section. Then we have the examples and documentation, which a lot of that we already have set up in this MCP specific PRP base that we've been talking about. And then other considerations is also

**[0:27:16]** very important. This is a good place to reference any gotchas that AI coding assistants seem to mess up on a lot. like I talk about uh how to use environment variables for example and this is very much following the initial MD that I described setting up in my

**[0:27:31]** last video on context engineering. So it's very much the case that we took the root of this repository and now we've just made a super specific version to building MCP servers with my last MCP as added context kind of like a scaffold right so that's the beauty of this and

**[0:27:47]** so what I've done in my initial MD is I've said something pretty simple here like we want to build an MCP we want to create a simple version of the taskmaster but parsing u PRPS instead of PRDs and I probably could have been a lot more specific here but I just wanted

**[0:28:02]** to show this as a demo. And so your initial MD might be quite a bit longer. You might want to be a lot more specific. This is just to get you started. It's just to give you a general idea of what would go in each section. So the these are all the features that

**[0:28:14]** we want in our MCP, like the different tools we're looking for. And like Raasma said, you might want to actually have a PRP per tool if you really want to make sure it nails it. In our case, this is actually working really well, which is just insane. And then for the example

**[0:28:26]** documentation, most of it is already within our PRP MCP base. And then also I'm giving it the GitHub repository to claude taskmaster. So as a part of our PRP we are going to tell cloud code to actually go look at the implementation so it understands all the tools there so

**[0:28:42]** it can replicate that for our PRP taskmaster MCP. And then just a few considerations that I've got here at the bottom. So that is my initial MD. And then going back to the readme here, let me open up the readme. Once you have that set up, now we just need to

**[0:28:56]** generate our PRP. So I'm going to do Ctrl J to open up a terminal here in my VS code. And then I'll type in Claude. So we are within Claude. And then I will do slash and then all we have to do is slash PRP MCPre. I can press tab to

**[0:29:11]** autocomplete. And then I just have to specify my initial MD which you can just call out the file name itself or even better the relative path to the file in the repository like this. Boom. There we go. So I'll go ahead and send this in. I'll do shift tab so that autoedit is

**[0:29:25]** on. And now it's going to do a bunch of research based on the MCP that I want to create based on the PRP MCP base. And it's going to create a custom PRP for me based on this template. And it's going to take a while. It does quite a bit of

**[0:29:40]** research and architecting and planning. And so I'll pause and come back once we have our PRP and then we'll validate it together. And there we go. After about 10 to 15 minutes, we have our custom PRP generated. So I'll do Ctrl J to exile to my terminal. Click into this PRP and

**[0:29:58]** let's take a look. And so remember, we need to validate everything here. And these are pretty long. Generally, these PRPs can get quite lengthy, but it is worth taking a look at everything, at least glazing over the details here, making sure there's nothing crazy, making sure that it's actually going to

**[0:30:14]** implement the MCP server or the application that you want to implement. And so yeah, let's take it from the top here. So we are building an MCP server. The goal is to build a productionready MCP for a PRP parsing system. Task management tools. We got GitHub OOTH, Cloudflow worker deployments. We're

**[0:30:31]** using Postgress to manage everything in our database. This is looking really good. And it lists out the tools that we want for PRP parsing, task management, documentation, basically everything that you saw in the demo earlier. Really, really good authentication, database. And one thing I want to show you that's

**[0:30:47]** really important is we always want to have a section in the PRP that talks about all the documentation and references that we want to bring into the context for our AI coding assistant when we execute the PRP. And so this is something that you definitely want to reveal in detail because everything that

**[0:31:03]** we have listed here it's going to be reading through and using as its reference point for implementation. So it'll understand here how to register new tools for our MCP and hook that into our scaffolding. That's super important. It's going to analyze the existing codebase to see how we set up our MCP

**[0:31:18]** server. We've got official documentation from MCP. So, generally, you want to have a good mix between external sources like our official MCP docs and then our existing codebase and examples that we're giving and all that together holistically creates all of the context along with the PRP. There's just so much

**[0:31:36]** that goes into this. The other thing that's really cool is generally with PRPs, what Rasmus and I have been doing is having it list out the current structure for the codebase and then the desired structure, what we want to add or modify for the final MCP server implementation. And man, this just gives

**[0:31:52]** so much structure. And I've seen Cloud Code especially just stick with this so well. Like every time I use this kind of PRP, whatever it outputs, like it actually matches this structure like file by file. It's so so cool. And so there's not a lot that I've actually

**[0:32:08]** wanted to change at this point. Uh so if we keep scrolling down, one thing that I did notice off camerara here is that it wants to update thedev.vars, which that's kind of Cloudflare's equivalent of av. You don't typically want your AI coding assistants to actually go and edit your secrets

**[0:32:24]** directly. So I would want to take this section out. And so that's just to give you an example of something that like you very much would want to change. And that's why it's so important to validate your PRPs. I don't want to bore you with the details of like tweaking everything

**[0:32:37]** right here. And so my plan right now is to go through this entire PRP myself like I'd recommend you doing. I'll adjust things as I see fit. Then I'll come back and we will execute this PRP. All right. So I've made some adjustments to the PRP. Really making sure that it's

**[0:32:52]** implementing what I want it to do based on my initial MD. There's not a ton that I had to change overall. Like it did a really good job. And so now we can move on to the last part of the process where we execute our PRP. And yeah, this is

**[0:33:04]** really simple overall, especially because of how we can use this template as such a good starting point for building MCPS. And that's what I want to continue to build out for a lot of other use cases you would care about making as well. And so what I would generally

**[0:33:17]** recommend doing once you go back into Claude here is I'd recommend exiting or clearing the conversation. Typically, you want to clear the context so you're starting with a blank slate when you move on to executing the PRP. And so now it's going to be PRP MCP execute. Again,

**[0:33:32]** just tab to autocomplete. And then what we want to do is just pass in the relative path to our new PRP. So it's PRP slash and then PRP parsermcp.md. There we go. All right. And I've got autoac accept edits on. Now it's going to first analyze the PRP and then it's

**[0:33:50]** going to go through all of the documentation and example files and everything. Create a comprehensive to-do list and then it's going to start knocking out the tasks one by one. And it's even going to implement what Raasmus likes to call validation gates. So it's going to have linting and it'll

**[0:34:05]** create unit tests and it'll run those unit tests and iterate on that until the MCP server is complete and working from at least what it can tell, right? And so it's a pretty extensive process. Like this is going to go on for a while. And so you can go and you know take your dog

**[0:34:19]** on a walk, go and work on another project, come back once this is done and you're going to have an insane starting point for an MCP. It doesn't always oneshot, but sometimes it can as well. And so, yeah, I will pause and come back once we have our implementation. And

**[0:34:35]** there we go. After about 25 minutes, Cloud Code knocked out all of the tasks for us. And we now have our fully implemented MCP server. Take a look at all of the tools that it built here. And we have green check marks across the board. And so now we can use Wrangler,

**[0:34:50]** the Cloudflare CLI, to run our MCP. And I'm not going to dive into the details for how that all works with Wrangler. and Cloudflare. You can definitely check out my last video where I really build out this MCP with you to get those kind of details. But right here, we can use

**[0:35:04]** the Wrangler dev command to run it, specifying the configuration that Cloud Code just made for our new MCP server, our PRP task master. So there we go. We'll run this. It'll simulate my production CloudFlare environment. So I basically have a local worker running. And this is my URL to access the MCP

**[0:35:21]** server either with streamable HTTP or SSE for legacy purposes. And so going back into my IDE here within my cloud desktop configuration, I've added this for my PRP taskmaster. So just pointing to that URL and then /mcp for streamable HTTP and then I can restart my cloud desktop. So let me do that really

**[0:35:42]** quickly. Bring it over here. All right, there we go. And then if you want to check and make sure that your MCP server is connected properly, you just click on search and tools. Go down and there we go. We have our PRP taskmaster with the 18 tools that we have implemented. This

**[0:35:56]** is just so so cool. All right. And so I will say that off camerara I had to iterate one time to get things working. There's just a couple of bugs and I think there's like one tool that I needed to tweak, but otherwise it worked really well. So it was a twoot for this

**[0:36:12]** MCP server and it is basically the same as my last demo. So I'll just use the same prompt here so we can kick this off and just kind of see it in action here like we did earlier. But yeah, we are good to go. And so now you could take

**[0:36:24]** this and deploy it to Cloudflare. You can follow the instructions in the readme and also in the repo specifically for my Cloudflare worker remote MCP, which I'll have that linked in the description as well. But yeah, the main thing that I wanted to show you here is done. We went through the three-step

**[0:36:38]** process creating an MCP server using context engineering specifically with the PRP framework. It is just fantastic. And so yeah, we can see this in action here. It's going to, yep, validate our PRP and ask us to approve this action, which I'll go ahead and do. I won't show

**[0:36:54]** the full demo again, but yeah, things are looking really good. So, we have built an MCP server from scratch. You can go through the same process no matter the MCP that you want to make. So, there you have it. That is everything that I wanted to show you for

**[0:37:07]** context engineering and specifically doing it with the PRP framework. So, I hope you can use this as a starting point to very easily build any MCP server that you want. And with a bit of imagination, you can see how you could adjust this to make anything that you

**[0:37:20]** want. That's the beauty of context engineering is it's going to 10x your workflow no matter what you want to make. And like I said, me and the Dynamist community, we want to build out this repository of all these different templates to help you get started with anything. And that is the future of AI

**[0:37:34]** coding. So if you appreciated this video and you're looking forward to more things AI coding and AI agents, I'd really appreciate a like and a subscribe. And with that, I will see you in the next
