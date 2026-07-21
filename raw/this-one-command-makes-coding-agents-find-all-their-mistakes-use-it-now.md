---
type: raw-transcript
title: "This One Command Makes Coding Agents Find All Their Mistakes (Use it Now)"
youtube_id: YeCHI1dmpZY
url: https://www.youtube.com/watch?v=YeCHI1dmpZY
slug: this-one-command-makes-coding-agents-find-all-their-mistakes-use-it-now
published: 2026-02-25
duration: "0:20:02"
fetched_at: 2026-07-21
immutable: true
---

## Transcript

**[0:00:00]** AI coding assistants. We love them, but they're actually pretty terrible at validating their own work unless you give them a framework to follow. And that is what I've been experimenting with for hundreds of hours at this point, getting really specific for the coding agent. So, it's not skimping out

**[0:00:16]** on the validation. It does that all the time. And so that it's actually testing the application as a user would. And so, I have packaged up my entire validation process that I go through for most of my AI generated code. and I put it into a single command. This diagram that you're

**[0:00:33]** looking at here outlines everything that I got packaged up for you. And the best part is this is pretty general. And so I'll have a link in the description to this command. You could literally go and run this on any codebase right now as long as it has a frontend. And so I want

**[0:00:47]** to explain right now how this command works and help you understand some of the ideas that go into this so that you can improve your own workflows for your coding agents to validate their own work. There's a lot of golden nuggets that I have in here for you. I've been

**[0:01:02]** doing a lot of iterating on this. And the reason this is so important is because coding agents now are generating code so incredibly quickly that it's almost impossible for us to keep up with the validation. And AI generated code is still your responsibility. So you need to validate. I'm not going to be a

**[0:01:18]** proponent of Vive coding. And so really what this workflow is doing is just delegating as much of the validation as possible to the coding agent. This is the workflow that I'll show you in a little bit here, just a sneak peek preview. And so we want it to fix as

**[0:01:32]** many issues up front, even point us to where we should address things ourself, so that by the time control passes back to us, there's just a lot less of that mental burden, that drag of having to review hundreds or even thousands of lines of code that was generated in the

**[0:01:47]** last 20 minutes. And man, let me tell you, it feels like a weight lifted off my shoulders using this kind of process, especially with the evolution that I'm currently at. That's why I'm so excited to show this to you right now. It's why I'm calling it the self-healing AI

**[0:02:02]** coding workflow. It's not that coding agents are going to be perfect with this, but it does come pretty close. I've been really impressed with the results recently. So, I'll show you each little component of this workflow very quickly, how it works. We'll see it in action. and I'll also talk about how you

**[0:02:17]** can incorporate something like this into your own AI coding workflows. So, here is the command or the claude code skill that we're going to be using right now. And so, I'll link to this exact skill.md in the description if you just want to take this command, use it for yourself

**[0:02:31]** on any codebase right away. It works out of the box. It even automatically installs the Verscel agent browser CLI. This is the browser automation tool that I've been leaning on very heavily recently. I also made a video on it already that I'll link to right here. And so this is a big part of the

**[0:02:47]** process, but it's going to work for really any coding agent as well. You could also change this up to work with any other browser automation tool like Chrome DevTools, MCP, whatever you want to use. And it's really just giving a lot of specificity, a framework to the coding agent for how to do research,

**[0:03:04]** what should the flow look like for self- validation. And I figured instead of going through this entire markdown document, it'd be a lot better for me to explain things more visually. So that's why I have this diagram that I'll go over really quickly so you can understand all the components that I

**[0:03:18]** have built into this. So for your own agentic engineering, there are two ways that you can use this workflow. You can either just use it whenever you want outside of any feature development. So maybe you just want to at some certain point run full end toend testing on your

**[0:03:32]** codebase. That's what I'll cover first as a live demo. And then the other way that I'll speak to more towards the end of the video is you can build this workflow directly in your feature implementation process. So after the coding agent writes any kind of feature, it's going to dive right into this to do

**[0:03:47]** regression testing and making sure that what it just built is working well. So first of all, since this is a command, we are going to invoke it with /2e test. And that will kick off the six-step workflow that we have here. Starting with our prerec check. So because we are

**[0:04:02]** using a browser automation tool very heavily in this process I do require you to have a frontend for your codebase which for me personally that is a majority of my applications probably is for you as well which is why I'm saying we can use this command for pretty much

**[0:04:18]** every single codebase. If you want to do any kind of testing for backendon apps definitely requires a different kind of workflow that I'll definitely cover in future content. Another check here is if you're running on Windows because if you are you can't use the Verscell agent browser CLI but you can simply just use

**[0:04:35]** WSL. That's what I'm literally doing in this video. So we check all the prerexs. If we are good then we go to phase one, our research phase. So the point of this phase is to ground ourself in the application. what are all the ways that users would actually use this

**[0:04:50]** application so that we can test all of that and then also understanding our data schema and just how we're working with the database overall because almost every single full stack application is working with a database and so the cool part about this is we have three sub agents that run in parallel. This is

**[0:05:07]** built directly into the workflow. So one agent is going to understand the structure of the codebase and how users will use it. another understands the database schema and then the other one is doing the code review part of our validation. So the rest of this process is more let's go through the application

**[0:05:22]** as a user would. But this sub aent is going to find things like logic errors that we have in our code. And so all three sub aents run in parallel. And then the research is compiled in the context for our primary agent. And then at that point we are ready to get into

**[0:05:37]** our full endto-end testing. And so we instruct the agent to start the dev server. So it'll spin up the entire application. So it's ready to go to the URL. And then it's going to define a task list here. And so each one of the tasks is going to be one of the user

**[0:05:52]** journeys that we want it to test. Making sure we can sign in, making sure that we can edit our profile or many other things that will get pretty specific to your codebase. But it'll figure that out in real time based on its understanding here. Okay, what are each of the tasks

**[0:06:08]** that we have to lay out? And it'll really spend a good amount of time with each one of them. So then next with our workflow, we pretty much have a for loop built directly in because we're going to look at this task list and we're going to pull out each of the user journeys

**[0:06:20]** and knock them out one at a time in a very comprehensive way. So just giving you a little bit of a demonstration here for what the timeline looks like. This is what our coding agent is going to be going through. So it's going to use a mix of the agent browser CLI to navigate

**[0:06:34]** the website and database queries to make sure that things are looking good in the back end as we are creating updating and deleting records. I am being specific to Postgress here because currently I am using Neon with Postgress but you can really use any database and the command

**[0:06:49]** will adapt itself. And so as an example here the agent will take a snapshot. This is how it understands what we currently have in the page. Then it'll query the database to make sure things are looking good. interact with a certain element and verify like if there's a record that was supposed to be

**[0:07:03]** created for example and then it'll also take screenshots along the way. So not only can it verify that the flows are working correctly, but also that the UI looks good because coding agents these days can analyze images. So we'll have a bunch of PGs that it'll create along the

**[0:07:18]** way and store in a directory for us to review after. So the screenshots are awesome for the agent to review itself, but then also for us to validate after that the end toend testing really is complete. And so at this point, the coding agent is going to check its work

**[0:07:32]** and it's going to figure out is there any big issues that we need to address here. If there is anything that is entirely blocking the coding agent from really validating the user journey, then it will fix the code, retest, take new screenshots, and validate and do this in

**[0:07:45]** a loop until the user journey is complete. Now, the really important distinction to make here is that there still will be remaining issues after the endto-end testing. In fact, there are usually more remaining issues than ones that are fixed because I have specifically prompted the coding agent to only fix the big blockers. And so for

**[0:08:04]** all of the other more, you know, moderate or minor issues, I want to work with the coding agent to figure out like, do I want to address this and how do I want to do so? So, it's only fixing this stuff to get it to the point where

**[0:08:15]** it can test the entire user journey. And then once it does that, it'll take it from the top and just go through the next user journey that we have in the task list. So very systematically knocking these out one at a time, doing some responsive checking at the end,

**[0:08:30]** just a lighter like go through the pages and make sure it looks good on mobile, tablet, and desktop. And then it gives us the end toend report at the end. And this is very important. I'm not just telling it to share with the user what happened willy-nilly. I have a lot of

**[0:08:42]** structure built at the bottom of the prompt, the bottom of the skill.md. So it's always outputting to me in the exact same way every time. Here is what we fixed. Here are the issues that were remaining. And here is everything that I went through. And so the goal here is

**[0:08:55]** with the report combined with the screenshots, I can really go through things super quickly and make sure the agent truly did a good job identifying all the user journeys and going through them. And then optionally, it can output to a markdown report. So at this point, the context window is going to be pretty

**[0:09:12]** bloated with the coding agent going through all this testing. So if there's anything more that I want to work with the agent to reason about and address, I want to do that in a new context window. So, I'll take the report from the output here, send that into a new session with

**[0:09:26]** my coding agent. The sponsor of today's video is Bright Data, the platform that unlocks the web for your AI agents, and it's built to handle hundreds of agents that you have running in parallel. So, in this video, we've been focusing on browser automation for local host. There is no anti-bot protection. But when your

**[0:09:44]** agents need to access the real internet, things like LinkedIn profiles, e-commerce sites, all of these sites are actively trying to block your agent. That is why you need bright data. And the way it works is genuinely impressive. Your requests from your agents are routed through 150 million residential IPs. Captions are solved

**[0:10:03]** automatically. Browser fingerprints are rotated. Your agent becomes a real person. And Bright Data has an MCP server that makes it super easy to get started. They also have an API. That's what I'm using for this demo really quick to show you the power of bright data getting structured public data on

**[0:10:19]** demand. So, for example, I can say I'm looking for 10 software engineers in Minneapolis. And watch, look at all the logs. It's solved the captures automatically. It's pulling LinkedIn information. So, I have all their profiles. I can research an individual person. Now, this is just a demonstration. There are a million

**[0:10:35]** different things that you can do with bright data. pulling any kind of information even from sources like LinkedIn that are usually really hard to crawl. Now, 14 of the top 20 AI labs are already running their agents through bright data. Over 100 million interactions go through their platform

**[0:10:51]** every day. So, they really are the most reliable solution when you need real time access to the web for your agents. Plus, you can use code Cole Medine. I also have a link in the description to get your first $20 of credits for free. So, definitely check out Bright Data.

**[0:11:05]** All right, so let's go ahead and do a live demo now that we understand how the command works, all the components of it. And so I have the skill.md right here in my local repository for an application that I built in the last video on my channel. So I built this link and bio

**[0:11:19]** page builder. It's kind of like linkree where you can design your own website where you put all your links up. You can send this to people like check this out. This is where you can go to see all of my socials and things like that. So this is the application that we're testing

**[0:11:31]** here. There's quite a bit built into this for authentication and managing different themes and being able to create your own links. And so we're going to have quite a few user journeys to go through here. And so I'll do /e2 test. No parameters or anything. And if you're using a coding agent that doesn't

**[0:11:45]** support commands, then you can literally just point it to the skill.md tell it to read that as its prompt and execute those instructions. And so I'll go ahead and send this off and it's going to start right away by checking those prerexs. So it'll make sure I have the

**[0:11:59]** RCell agent browser CLI that I'm running on Linux or in this case in WSL and then pretty soon here it'll kick off the sub agents for research. So take a look at this. It's kicking off the first one to understand the app structure and journeys. Now the next one to understand

**[0:12:15]** the database schema and then in just a second here we'll see the code review one. There we go. The bunk hunting code analysis. And so I'm obviously not going to go through this entire thing with you. So let me pause and come back once it goes on to the next stage. So I'll

**[0:12:28]** show you all the important stuff here. All right, very good. We can see that all three of the sub aents have finished and now it goes on to the next step of starting our entire application and it knows how to do this like the exact command to run because it's one of the

**[0:12:42]** things that this sub aent finds for us. And so even if your application has a couple of steps like you have docker containers that you have to spin up, it's still going to figure out all of that. And then it'll even run into some of these issues once in a while where it

**[0:12:55]** has to self-correct. And so don't worry, you might see a lot of errors throughout the entire process. Like right here, it tried to visit the site before it was compiled and started as an Nex.js app. And so it corrects itself. It waits a while. Finally, the server's up. Now we

**[0:13:08]** are using the agent browser CLI to visit it. Taking a screenshot here as well. We could already take a look at this if we want to watch its progress as it is validating. And then here is our task list. So now that it visited the website at first just to get its graphs. Now

**[0:13:24]** it's going through all of the user journeys. And this is the part that takes the longest for sure because we have that for loop. We're doing quite a bit to validate every single one of the tasks that we have here. And so we'll see a combination of the agent browser

**[0:13:38]** and whatever calls it's going to make in order to visit the database and validate our records. All right. Right. So now we're getting to some of the interesting parts of the validation where it has to do write operations from within the user interface. And so for example, updating

**[0:13:53]** our profile for this website. And so it's going to save and then verify the database update. So we see it take a snapshot so it understands. Okay, here is the save button. Now let me click that. Now let me take a screenshot. Read the screenshot to make sure that we have

**[0:14:08]** a good UX of saving. It says we save. We have a pop-up everything like that. And then make a call to the database. So it creates a query here to make sure that the record is confirmed. The profile is updated with the new display name, bio, and avatar URL. So it's looking good in

**[0:14:22]** the front end and it's looking good in our database. And so just going to the Neon console really quickly here. There's just a few tables that I have for this application. So profiles, this is where we just made an update, right? So you can see here that we have some of

**[0:14:35]** these E2E test users that were created. So the coding agent creates a brand new user, making sure it can update profiles and then go in and create link items for that profile tied to the right profile. Like there's a lot that happens with the database under the hood and if there's

**[0:14:52]** any issues there, it might not necessarily be reflected in the front end, which is why it's really important that we're doing this level of validation as well. And then while we're in the Neon dashboard, one thing I want to mention really quickly is when we're doing this kind of endto-end testing and

**[0:15:04]** we're building all these fake profiles and links and just database entries in general, it kind of bloats our database. Even with a dev database, we might not want to have all those records just sitting around. And so one thing that I like doing with Neon is creating a

**[0:15:20]** branch. So this is something specific to Neon and how they work with Postgress. we can make these branches where it'll essentially take a snapshot of our current data and then give us this secondary database that we can do whatever the heck we want with and then we can delete that go back to our main

**[0:15:35]** branch whenever we want and so that way I can just create this you know like end to end test to and then this is the database that I'm connected to for my end toend test and you could even build this directly into the workflow if you want I'm not doing that right now

**[0:15:48]** because I want this to be more of a general workflow that works no matter your database but there are some pretty powerful things you can do to keep your test in isolation, keeping your database clean while still giving your agent full reign over your database to create records and validate records, everything

**[0:16:03]** it has to do. All right, take a look at this. Our validation is done and it actually fixed quite a few things during its end toend testing and then some other issues that we'll need to address with our agent later. So, it found some from its end to end testing and then

**[0:16:17]** also some from the bug hunt sub aent that ran towards the beginning. We have our end toend screenshots folder. So we can also validate a lot of these things to make sure that it really did all the testing that we expect it to. But yeah, this is looking super super good. And

**[0:16:31]** then it also asks us if we'd want to create a markdown to send into another coding agent to address these issues. And so from here you can take it as you want. You can address each one of these issues one at a time. You could just send this entire markdown into another

**[0:16:44]** coding agent. Entirely up to you. But the important thing here is that we found even the small issues like this is so detailed. I love the specificity that this workflow gives our coding agents. The kinds of things that the agent is really never going to catch by itself or

**[0:16:59]** at least very rarely. So one last golden nugget that I want to cover with you really quickly is how can we use this end toend test skill directly in our feature development. So, in the last video on my channel that I already linked to, I covered my full process for

**[0:17:14]** AI coding with green field development. And the PIV loop is the core framework here. Plan, implement, and validate. And what I always do for my planning is I create a structured markdown document that outlines everything that we need to build and the entire validation strategy before we go into implementation. And

**[0:17:32]** this is our opportunity to specify. We can literally just tell the agent, I want you to use the endto-end test skill after you've written the code to test things in a very comprehensive way. And so for the skill that I have linked in the GitHub repo, I've actually disabled

**[0:17:47]** model invocation. You can do this with all claude code skills. So if I remove this line, you can do that yourself. Then the agent can use the end toend test skill. That's just kind of a safety cuz most of the time you might just want to invoke this yourself. But you remove

**[0:18:00]** that line and then and I covered this in the last video course. So I have my plan feature command. This is where I outline the exact structure for my plans that I want to send into implementation. So we can just add a line here. So I have the

**[0:18:13]** validation commands. I have a section for any additional validation. This is exactly the template that I have in the last video. So we could just change this and say use the E2E test skill to do comprehensive testing. Right? Like literally that simple. That's all we have to do. And so now it's going to

**[0:18:31]** basically use this as a subskll. So it's kind of a subworkflow as a part of this la larger implementation workflow which you have to be careful about token usage here. And that really is the last warning that I have for you for this entire process. It is somewhat

**[0:18:45]** tokenheavy and it's going to take a while. So it's definitely the kind of thing where you want to send this off and then work on something else. Step away from your computer, whatever it is. Just let this go. But the point of it is not to be fast. The point of it is to be

**[0:19:01]** comprehensive. And so the time I have to wait for this to finish and the tokens that I have to spend, it's worth it to me. In fact, I think it's saving me tokens in the end because it's finding all these issues that otherwise I'd have to deal with with my coding agents later

**[0:19:14]** on. And I've run this dozens of times in the last week and I haven't even hit the rate limit for my Claude Code Max subscription. So it's pretty token efficient overall. mainly why it takes so long is just because we have to wait for all of these uh you know page

**[0:19:29]** interactions and so sometimes it'll like run asleep after clicks on a button to wait for it to load things like that so it is pretty token efficient overall so yeah I would encourage you to take this skill this command just apply it on some codebase with a front end right now I

**[0:19:43]** think you'll be pretty impressed with the kinds of things that it can find the issues that it will surface for you and so if you appreciated this video and you're looking forward to more things on AI coding and self-healing AI coding workflows. I'd really appreciate a like and a subscribe. And with that, I will

**[0:19:58]** see you in the next video.
