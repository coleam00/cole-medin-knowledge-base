---
type: raw-transcript
title: "The Creators of Claude Code and OpenClaw don't Prompt Their Agents Anymore?!"
youtube_id: UztrFXaSWv0
url: https://www.youtube.com/watch?v=UztrFXaSWv0
slug: the-creators-of-claude-code-and-openclaw-dont-prompt-their-agents-anymore
published: 2026-06-17
duration: "0:24:37"
fetched_at: 2026-07-21
immutable: true
---

## Transcript

**[0:00:00]** Apparently, we're not even supposed to be prompting our AI coding assistants anymore. The real skill is designing loops that prompt your agents so they work for you 24/7. And I got to say, I am not sold on this idea right now. It feels like some of the bigger players in

**[0:00:15]** the AI space like Peter Steinberger, the creator of OpenClaw, Boris Churnney is doing this as well, the lead at Claude Code, they're pushing this new fad, whether they like it or not, of loop engineering. It's becoming the next buzzword. And I promise I'm not going to be hyping up loop engineering here.

**[0:00:32]** There are some good lessons to be learned from what's surfacing, but also with loops, and you've probably seen this with dynamic workflows and cloud code for example, they're not always the most reliable and they are extremely tokenhungry. So unless you have an infinite budget like Peter pretty much,

**[0:00:48]** then you have to be really careful with these kinds of systems. They're not always practical. And so that's what I want to cover with you in this video. I just want to get really honest and really practical with you. We're going to cover three things. We're going to

**[0:01:00]** cover loops in a really simple sense. It's not actually that complicated. So, I want to show you how you can run these and then I want to talk about the trade-offs and then solutions to that. So, really nice and structured here. And so, as far as some of the solutions

**[0:01:12]** we'll get into towards the end of the video, I want to show you how we can build a system where we can really observe the loops, the orchestrators and the workers, how we can optimize for cost with the workflows we build and using different providers like PI. And

**[0:01:25]** so it really it's like here's how you can run loops. Here are the downsides. Here's how we can solve for them and really get to the point where we're building harnesses for these longer running tasks because it is really powerful for certain things, but then also covering the honest trade-offs with

**[0:01:40]** it. Okay, so we saw what Peter said. Now let's take a look at what Boris, the creator of Claude Code, said, and it is really similar. He said, "I don't prompt Claude anymore. I write loops and the loops do the work. My job is to write loops." Okay, Boris, I think we get it.

**[0:01:55]** And like I said, loop engineering is kind of a buzzword, but also there are some really good takeaways when you dive into this. So, like Boris through a lot of like interviews and podcasts has shared his workflow. We can get glimpses into how it works. A lot of it is built

**[0:02:09]** around the newer features in claude code. Like /loop is the most basic example, and I told you we're going to simplify things here. Loop engineering is really not that complicated. I don't even know if it deserves its own term. And so with /loop, we set an interval for running a prompt. So like for

**[0:02:25]** example, every 5 minutes, I'm going to check for new GitHub issues in this repo and handle any that come in. So it's pretty neat. We set up Claude to basically wake itself up every 5 minutes. And of course, you can adjust this. And it's going to look for input

**[0:02:39]** in an external system like GitHub, for example. And so as long as our terminal is up and running with cloud code, it's able to autonomously handle this. So basically it's a every 5 minute loop looking at GitHub issues. There's also /goal that we have in cloud code and

**[0:02:55]** codeex. So we set some criteria like here is how you know you are done and then we're forcing the coding agent to work until it is done. Kind of like Ralph loops that went viral a few months ago. And then last we have / routines. And so these are the schedule jobs. Like

**[0:03:11]** every hour I want you to wake up look at some larger spec document and then handle the next task. And so really loop engineering is combining or creating a system around all these things routines/loop so that we can give a larger scope of work as input to an AI coding assistant

**[0:03:28]** and have it work through it incrementally right because we never want to have a coding agent try to handle too much at once or it will get completely overwhelmed. And the main idea with loop engineering is we want to have some main orchestrator agent that we talk to. We do minimal prompting,

**[0:03:42]** just telling it what we want at a high level, and it figures out how to set up the loop and the entire system. And it's really easy to do this in Cloud Code. This is really cool. You just tell it to use the loop skill. So, there's a

**[0:03:55]** capability built right into the tool where it knows how to set up these loop systems based on what we ask it to do. So, I passed in some kind of simple spec document here, like I just have this as an example. These are the tasks that we wanted to go through incrementally. And

**[0:04:08]** so, my prompt is telling it to load the skill. So now how to set up the loop and then every cycle it's just going to do the first unchecked task do the validation and then that loop is done and then on the next loop it'll go through and do the next task and so

**[0:04:21]** eventually all the tasks will be complete and then our primary cloud code session here that set up everything is going to report back to us right so like right here cloud code is sort of the orchestrator but then also the workers because it sets up the loop itself but

**[0:04:35]** it is really cool to watch this run so I'll send off a request here and I'll Wait for it to run a little bit. I'll come back and show you kind of how it works. But you can see that it loads the loop skills the very first thing. So it

**[0:04:47]** knows how to orchestrate things and it'll do the slash loop by itself that I just showed how you can do manually. Okay. So I came back a couple minutes later and it's already done with the first two tasks. So it's gone through two iterations of the loop already. And

**[0:05:00]** so if we go up to the top, we can see that it says this is sequential task list. It's going to do the first task and then it's going to schedule a quick wakeup. So, it sets up the slash loop by itself. And if we scroll down a little

**[0:05:10]** bit after it does and validates the first task, we can see that it's resuming with a /loop wake up. And look at that. I didn't write this prompt myself at all. I know this is a very, very basic example, but I want to stay simple on purpose, but it wrote the

**[0:05:26]** prompt /loop work through plan.mmd one task at a time. And so the kinds of systems that Boris is building is obviously going to be a lot more elaborate with how we're telling it to run the looping and building in routines and describing how we want it to prompt

**[0:05:39]** and work through our context. But at the basic sense, this is really all it takes. And so now it's just going to keep knocking things out one at a time. So that is loop engineering in the most basic form possible. But now I want to get into some of the downsides here,

**[0:05:56]** which some of them are definitely pretty obvious to you already. Problem number one, there is no way you're going to convince me that loop engineering is the way to get the best results possible with AI coding assistance. I mean, come on, this has to be hyperbole here. Boris

**[0:06:10]** Journey says that there are days he manages tens of thousands of AI agents at once. Like, really? Is is that actually practical? Is that going to scale? Like are you really building cla code with tens of thousands of agents per day? I mean maybe that does explain some of the bugs we have in cloud code.

**[0:06:26]** I feel like there's constantly a couple annoying ones, but yeah, overall like building these kinds of loops if we make it a very tight controlled system, that's what I'll talk about in a little bit. I think it's good. And for building proof of concepts and exploring ideas, like I think it's really good, but it's

**[0:06:42]** not like I want to drive all my AI coding with them. And then the second big problem is cost. Because with loop engineering, we're relying on some kind of orchestrator to set up the system and really determine how to get to the end goal. So, it figures out how many

**[0:06:56]** workers to spin off, how many loops to do, and that gets super expensive. So, the dashboard that I built that I'll show you at the end of this video, I built cost tracking into it. And so, for a single run, like here are all the loops that the orchestrator went

**[0:07:09]** through, it costed me over a million tokens just to build a relatively simple application. And yes, I'm sure there are a lot of optimizations that I can do here, but I think you can see just by looking at this, I mean, this is part of why I built the dashboard. You can see

**[0:07:23]** why it would be so expensive because we send in our initial spec to the orchestrator and it has to reason about that and then figure out how many workers to spin off. Then it has to prompt them all. They each spend tokens and then the results come back. The

**[0:07:36]** orchestrator has to then reason about that again and then send off the next wave. No matter how you design the system, there's a lot of context passing and reasoning to make everything work here in a distributed way. So, it's a really powerful system and it's cool how far you can take this kind of stuff with

**[0:07:53]** the self- validation, but man, does it get so expensive. And then really quick, the third problem with loop engineering is at least for a lot of setups, you're not really working between different coding agent sessions. Like when you're just using /loop in claw code like Boris talks about a lot, it's really just

**[0:08:10]** continuing in the same coding agent session. So if you loop for a while, you're going to completely bloat your context for your LLM and overwhelm it. And so we need a system where we can distribute the work actually between different coding agent sessions and make it so they can all communicate to each

**[0:08:28]** other and have an idea of like where they fit in the larger goal. And so that's what I want to cover for the rest of the video here. So I want to talk about how I actually work on a day-to-day basis because this will cover how we can solve for a lot of these

**[0:08:42]** problems we have with loop engineering. So I use my tool Archon, but I'm not just trying to like push Archon on you here. I just want to talk about how I use it in a way that solves for the problems of cost, reliability, and how do we actually orchestrate many

**[0:08:57]** different coding agent sessions. And so go through this with me here. So, Archon is my harness builder. Allows us to build workflows that orchestrate many coding agent sessions to handle larger tasks. And so, for example, a really classic AI coding workflow is you do your planning, you do your

**[0:09:15]** implementation and then you do your code review or your testing. And so, we can build this as a single Archon workflow. There's a ton of content that I have on Archon on my channel. I'll link to a video right here to help you get started if you're interested in this. But again,

**[0:09:29]** I just want to focus on like how I use this on a day-to-day basis to kind of do loops. Like you can do loop engineering with Archon. You can build the Ralph loop with Archon. So I'll show you an example of a workflow here. If I go into

**[0:09:42]** the default workflows, there's a ton that we have that ship with Archon. Let's take a look at fix GitHub issue for example. And so I don't want to get too in the weeds here, but I just want to show you really quickly at a high level how this workflow works. And

**[0:09:55]** another really important thing with Archon is that we're not having the agent drive the entire thing. It's more deterministic because we set up the process in this workflow file and then we even have certain steps that are deterministic. Like the agent is not driving it. We are guaranteeing that

**[0:10:11]** it's going to happen. So when we're building these loops and larger tasks that we have our coding agent knock out, we want to actually take the decision away from the coding agent as much as we can only applying the reasoning of the LLM when we actually need it to write

**[0:10:26]** the code. For example, like we might want our agent to write the code but not actually decide the test to run because we know what it looks like for our test to pass. And so for this workflow, first we extract the issue number. So the input here is some GitHub issue that we

**[0:10:39]** want to fix or address. So we extract the context, we fetch the issue context and then we classify it. So we have a large language model decide at first are we addressing a bug or are we implementing a new feature and then the workflow is going to be dynamic based on

**[0:10:56]** that decision. So the kind of thing that your orchestrator would usually decide we're more enforcing a specific process here like this is the kind of thing that I want to sort of layer on top of loop engineering like let me be in the loop let me determine how the workflow can

**[0:11:12]** progress and so then we research the issue investigate it and then we go do the implementation and the validation and we create the pull request right step by step each one of the steps we're using markdown documents as context so we're handing things off between the steps But then each step is running in

**[0:11:28]** its own coding agent session. So if we're handling a larger GitHub issue, it's not like this entire thing is running with / loop and cloud code getting totally overwhelmed with each of the tasks that we're doing as we're planning, implementing, and validating. And the way that I can manage cost here

**[0:11:43]** is every single node in this archon workflow, I can actually decide what model am I going to use. And so for example with the classify step here at the top when we're figuring out you know what kind of issue do we need to address in the rest of the workflow. This is

**[0:11:57]** kind of like the orchestrator decision we can use a small model like maybe using haik coup or miniax m3 kim 2.7 for example right like what we can do in archon is even mix providers. So we can use cloud code for the implementation and then we can use codecs for the

**[0:12:14]** review and then for all of our context loading and exploration up front. We can use a smaller model like Kimmyk 2.7. And so that's one of the other big issues I see with using /goal or routines or loops in cloud code is you're just using one model for pretty much everything.

**[0:12:30]** That's part of the problem of why it's so expensive because when we're doing larger amounts of work like this, of course, you're going to have to spend more tokens. But you don't always need to spend the most per token for every step of your workflow. And I know I'm

**[0:12:45]** really really driving this in the ground right now, but yet another reason you want some kind of harness like what you can build with Archon is we have durability. So this is my Neon database. I'm storing all of my logs and runs in Postgress so that I can resume a

**[0:12:59]** workflow even if my machine goes down or I cancel things like whatever I do I'm always able to resume on exactly the step that I was in that larger loop or that larger workflow. So I have all my conversations the code bases that I'm operating on with Archon. Everything is

**[0:13:14]** durable and it's super easy to resume any work that I'm doing. Okay, cool. So now I want to show you how I actually use Archon on a day-to-day basis. a lot of ties that we can draw to loop engineering and things that I've really fixed with it, right? And so in a very

**[0:13:29]** very basic sense, one of the most classic workflows that I use with archon is fixing GitHub issues. Most of the input for my day-to-day work is issues in a repo. Either I'll create them or someone else will. And so we can use archon to send off workflows to run in

**[0:13:44]** parallel handling multiple GitHub issues at the exact same time. And this is very much like loop engineering because we have our primary cloud code here as our orchestrator and it's figuring out based on my higher level request. I'm going to create the prompts and dispatch the workflows. Work trees are also a really

**[0:14:03]** important part of loop engineering. Boris talks about this as well. If we're having many different agents handling tasks in a loop, we need to make sure they're running in isolation so they're not stepping on each other's toes. That is how we scale our output with AI coding assistance. And so we have our

**[0:14:18]** cloud code here kicking off four workflows to handle GitHub issues. It's going to validate the PRs after like make sure that they are actually created and this is where we can come in with human in the loop as well. And then it'll run four more workflows to validate like perform a code review on

**[0:14:34]** each of the issues as well. So very comprehensive kind of a loop in a sense where it's like handle the issues validate and then do a code review. And uh another thing as far as like making this more reliable is with archon workflows, we can also build human in

**[0:14:47]** the loop within any individual node in the workflow. So we can always have it pause for us to validate something before it continues. Which is one of the biggest problems with loop engineering right now in general is that a lot of times people set up these systems to

**[0:14:59]** just go go and then you have it run for a day and by the time it comes back you just have crap. Like I've had that myself as I've tested a lot of things within cloud code like routines and sloop. And so I'll send this off here and I'll just pause and come back once

**[0:15:14]** it's done. So we can walk through everything that it accomplished here. And the best part about all of this is we actually have nine coding agent sessions for this entire loop or whatever you want to call this entire harness, right? Like one per GitHub issue fix, one per review, and then we

**[0:15:29]** have our primary orchestrator. So, we're doing a ton of work, but at the same time, we actually are pretty lean for each individual session because actually, I kind of have to correct myself. It's more than just nine sessions because even within each individual Archon workflow, we're running separate coding agent sessions

**[0:15:46]** where we can have different models. We can optimize for cost. There is a lot of engineering that goes on behind the scenes here. All right, so I'm back after the entire thing ran. I just want to show you how comprehensive we can be here. And so we have the four workflow

**[0:16:00]** runs for actually fixing the issues. And then cloud code here is really monitoring and orchestrating everything, right? So like as the different tasks are done, it's coming in and checking on them. And then finally, we have everything done together. So all four fixed workflows are done. Then it

**[0:16:14]** launches the code reviews cuz it confirmed that all of the pull requests are ready to be reviewed. And you can even ask for a status update. So like while the Archon workflows are running, if we want to see where we're at, we can of course check the logs in the Archon

**[0:16:27]** web UI. I have that as well. But then also we can just ask our orchestrator, right? So it really is in control of our entire situation here. And then finally, all the reviews are done and it gives us the things that need our attention now. So we can really come in and direct

**[0:16:42]** things from here. So it's the harness driving everything, but we still can be in the loop wherever we want. And I know there's a lot that goes into effectively orchestrating parallel coding agents. So there's a lot of content on my channel where I cover this kind of thing. Like

**[0:16:56]** for example, one thing that you have to do a lot is branches in your database, right? Like if each coding agent is working on something in parallel, you don't want them to be stepping on each other's toes, not just with code changes, but also database changes. So work trees and neon is a super powerful

**[0:17:11]** thing. A lot of different things like port conflicts that we want to solve for as well. So I'll link to a video right here where I cover that stuff and just generally how we can make parallel AI coding more reliable. So assuming you take care of all of that, you can really

**[0:17:23]** let Archon rip on as many GitHub issues or whatever in parallel. Very cool how far we can take our output here. All right, so we have covered a lot in this video already. Loop engineering basics, the downsides of it, how I'm using Archon to extract the good parts out

**[0:17:38]** into more deterministic workflows. But last, I want to cover a system that I built for loop engineering in its purest form. Because I presented these issues to you, but I I do see a lot of promise with this. I want to try to build a system that solves for these problems.

**[0:17:53]** And so I've built this dashboard that I'm really excited to show you right now. I actually have it open sourced on GitHub. Link to this in the description. And I have built this to solve for a lot of the problems that we have with loop engineering right now. So first of all,

**[0:18:07]** we have durability. Uh just like with Archon, all of the loops that we run and the different events and logs, I'm storing this here so we can always resume a workflow later on. So we're managing all of our state in an external database. So we're not relying on that

**[0:18:23]** staying in any coding agent session. And so our main orchestrator, it is going to read through this state here and then figure out like okay, what is the next thing that we need to do? And so then it's going to call upon the workers to accomplish all of that like build a new

**[0:18:38]** feature or do some kind of validation whatever it needs to do. And then those workers are going to go back and they're going to update the state that we have in our database. Like again I'm using Neon for Postgress here. And so this is our loop, right? Because then the next

**[0:18:50]** time the orchestrator runs, it's going to get that updated state from the workers and then figure out the next workers to invoke. And there are a couple of problems that I'm solving by building something like this. And and I want to start by saying like this is more experimental. I'm just showing you

**[0:19:04]** something that I'm working on and kind of building into my own second brain. But first of all, I'm driving everything with Pi. So I'm actually using my Kimmy subscription with Kimmy K 2.6, 6 now Kimmy K 2.7 to drive all of these workflows. So yes, it is a lot of

**[0:19:19]** tokens, but I'm not using Opus for everything, but I'm still getting really good results because of the harness that I built here that elevates the model. And then I have a lot of observability built into this dashboard. I mean, obviously it being a dashboard, it solves part of that reliability problem,

**[0:19:34]** which obviously I'm still working on. But just being able to see exactly the decisions that are going on here means that it's easier for me to uh look at this, even have my coding agent analyze the runs in the database, and then figure out how to improve the loop, how

**[0:19:48]** to improve the harness here. And so I just have been going through a lot of really simple examples, but like non-trivial enough where it does have to go through quite a few rounds to build it. So like building a single page combine board as a static web app. I

**[0:20:02]** just take this prompt and I'll show you it running live right now. Like I'll just send this in and I will start a loop. And it's really cool. We can see that the orchestrator is deciding how to split up the work right now. And then we also have like the full run history

**[0:20:14]** here. It's pretty neat. Like it's super easy to get this up and running. Uh if you just want to check out the GitHub repo linked in the description. But after a little bit the orchestrator will decide here is how I'm going to create that first wave and then we'll see the

**[0:20:26]** workers dispatched. So there we go. The orchestrator spent 6,000 tokens with that initial planning and then prompting our first three workers in round number one. And so we don't have to watch paint dry seeing this go to completion here. But you get the idea. We saw the full

**[0:20:41]** run in the logs earlier of how it'll go round by round doing validation each time. And we can even have human in the loop so that we get to actually take a look at what has happened in the first round before the orchestrator moves on to the next. That is the kind of

**[0:20:55]** reliability that I feel like we really need to have right now in order to build anything more than simple demos with uh this kind of loop engineering setup. And so yeah, I I would encourage you to just play around with this kind of idea. Like building a a dashboard to manage more

**[0:21:09]** autonomous tasks in something like your second brain is a big thing that I'm focusing on right now. And we can even take this kind of dashboard and deploy it to the cloud as well. So we can access it from anywhere. maybe even start to share our loop setup with our

**[0:21:23]** teammates. And these days, it's just so easy to take applications that you build locally for these kinds of control systems and deploy them to production so you can use it remotely or have a team use it. Retool is a tool specifically I've been leaning on a lot for these

**[0:21:37]** kinds of deployments. And so it's just so easy to create an app here and then we can import React code. So I just had Cloud Code build the entire dashboard in React with the idea of I'm going to deploy this here. It's so incredibly easy. So, I just go in and I take the

**[0:21:52]** zip file of the front end that I just showed you and then its agent is going to go through wiring everything up. So, it'll connect to the backend with the API that I have running with PI. It'll get everything deployed to a real URL that I can use. It's really neat. So,

**[0:22:05]** for example, here connecting to my Neon database where I'm storing all of the runs for durability. It asks me to set up a connection here. So, I can create a new resource. I can select Postgress because that's what Neon is running under the hood and then set up all of my

**[0:22:19]** connection information here. So really easy to make that connections. I'm just deploying the front end here and then connecting it to wherever I'm hosting my app hosting PI running behind the scenes. So I'll get all this hooked up off camera and then I'll show you the final result here. And there we go.

**[0:22:33]** Everything is deployed. We can see our app hosted in the cloud just like it was running locally. Very cool. So now we have a URL where we can share this. There's also a lot of other cool things you can do in retool like you can set up permission groups and so certain actions

**[0:22:46]** that you can gate with an API endpoint. So you have to approve it and have the right permissions to do so. So for example being able to pause the workflow and then resume it. If I click this right here you can see that approve and resume and you can see the identity that

**[0:23:00]** I have through retool. It's giving me permission to actually do that. And then it's also very easy to edit this application. I can continue to make changes with it here in the cloud as I need adding new features to the front end, whatever I need as I'm evolving my

**[0:23:13]** dashboard. So yeah, I've just been doing a lot of this with like deploying dashboards for observability and helping me with all my systems for my second brain and my AI coding. Very powerful stuff. And a quick shout out to the retool team. Ever since I've been using their platform, I've been working with

**[0:23:26]** them and I even collab to bring this integration in the video today. It's a great platform because you get to build your applications directly in retool or you can import it like I showed earlier. But then your team regardless has a single governed path to production with audit trails. Really easy to make your

**[0:23:43]** changes just with chat like I showed here and the review system with human in the loop. All of it that you need to ship your apps to production. And I'll have a link in the description. If you go now, you get free app imports through July 1st and bonus AI credits on all

**[0:23:56]** paid plans. So that's everything I have to cover for Loop Engineering. the basics, the problems with it, how I'm solving for it because I I really do want to incorporate loop engineering. Like I like the concept of it and I want to drive how autonomous my coding agents

**[0:24:10]** can be, but you got to have the right system otherwise things are going to completely fall apart like we've already talked about. And so I hope I've inspired some ideas for you even like how to use Archon or start to build this sort of harness for yourself. Really, I

**[0:24:23]** would just fold loop engineering into harness engineering. It doesn't quite deserve its own buzzword, right? But like there are some good ideas here. And so I hope you found this useful. If you did, I would really appreciate a like and a subscribe.
