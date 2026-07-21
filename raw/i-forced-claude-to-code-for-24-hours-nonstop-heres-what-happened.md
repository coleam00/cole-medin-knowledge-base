---
type: raw-transcript
title: "I Forced Claude to Code for 24 Hours NONSTOP, Here's What Happened"
youtube_id: usQ2HBTTWxs
url: https://www.youtube.com/watch?v=usQ2HBTTWxs
slug: i-forced-claude-to-code-for-24-hours-nonstop-heres-what-happened
published: 2025-12-03
duration: "0:26:48"
fetched_at: 2026-07-21
immutable: true
---

## Transcript

**[0:00:00]** A few days ago, Anthropic released this article where they have open sourced their harness for building longunning agents. All a harness is is a coordination layer on top of coding agents that allows them to work for hours and hours on a task without overwhelming their context window. So

**[0:00:18]** basically splitting work between different agents and context windows on the same very very large task. And I've been fascinated with this idea recently. And so what I want to do with you right now is take this anthropic harness, put cloud code into it, and have it work for

**[0:00:35]** 24 hours straight and see what results we get at the end. And I know, I know this is very experimental. You're not going to do this kind of thing for a production application, but I think this is really exciting to experiment with. And I really do think that in the near

**[0:00:49]** future, longunning agents are going to be something we use a lot to kick off our coding assistants as background tasks to start an application for us like build auto proof of concept and then we come in and keep building on top of it. And I can tell you that after

**[0:01:03]** reading through this article, which I'll have linked in the description of course, and trying it myself already, the strategies here are legit. And like I said, I've already been experimenting with and building these kinds of things, but I'm definitely going to be taking inspiration from some of the strategies

**[0:01:19]** that Anthropic has here. And I also created this really neat Excal diagram to help you grasp everything that goes into this harness. And it really is simple overall, which I appreciate quite a bit. And there are a lot of really smart ideas to take out of this. Plus,

**[0:01:34]** of course, you don't have to use cloud code. This whole harness really is just a bunch of prompts and files. And so you could use this with any coding assistant, codeex, open code, you pick your poison. So more on this in a bit, but the application that we're going to

**[0:01:47]** be building over 24 hours is a copy of claw.ai. So you're probably familiar with this if you use Claude at all. It also looks very similar to Claude desktop. It's just a simple interface for us to talk to Claude, upload files, manage projects, and different conversations. I chose this because

**[0:02:05]** that's the demo they have in the article that I was showing you earlier. And whenever I read one of these articles and they give an example of what they can build, I always wonder like, is this actually possible or did they do something else to make it just look

**[0:02:18]** nicer than it actually turns out? And so I want to test this article for real by giving 24 hours for cloud code to build this thing. And so what you're looking at right here is what I have from a previous execution only after a couple of hours. There are a lot of features

**[0:02:33]** missing here if I were to poke around. And so we're going to see after 24 hours, can we build this but completely working with conversations and artifacts and files and projects, all the features that we have with Claude as the application. Now I could go right into the live demo and we'll do that in a

**[0:02:51]** little bit, but the real value for you is understanding how this harness works even so you can take ideas from this to evolve your own system for AI coding. So I'll explain this really quick because it is pretty simple. Overall, it relies on the concept of testdriven development, which is very powerful for

**[0:03:09]** AI coding. We define the success criteria, all of our tests upfront before we do any of the actual coding. And so then we're constantly checking our work against this set of tests that defines what it means to have a finished product. It's very cool. And all the ideas that I have in this diagram are

**[0:03:27]** coming directly from this article and then also the open source repo for the harness, which I'll link to below. You can start using this right away and this is what we're going to be using for our live demo in a bit. So with this harness, everything starts with the app

**[0:03:41]** spec text file. I typically call this a PRD. It's basically the scope of work for what you want to build for your MVP. So this is the primary context that goes into the first session that our harness kicks off. And this is the session for our initializer agent. The sole job of

**[0:03:59]** our initializer agent is to get our project set up. So when it finishes, we're not going to have anything actually working yet, but we're going to have these four things created to then go into our coding agents. And we'll get into this in a little bit. And so the

**[0:04:13]** first thing that our initializer agent creates is this feature list JSON file. This has the 200 or more test cases that need to pass for our application to be considered complete. And this number is configurable in the anthropic harness. I know that is an insane number, but like

**[0:04:29]** I said, this is very experimental. We just want to see what it looks like to have a coding agent run for a very long time implementing a lot of different things. And so all of this is just based on our PRD breaking it down into very granular tasks. And then we also create

**[0:04:44]** a script to initialize our project like get the website spun up. We create the scaffolding. So kind of like the boilerplate having that in place for our coding agents. And then finally we initialize a git repository because git is absolutely crucial for any AI coding system. So with the initializer agent,

**[0:05:02]** we've covered two out of the three core artifacts for our harness. We have the feature list and the initialization script. The last core artifact here is our claude progress. This is the file that is updated at the end of every session, giving a summary of what was just done. This is how our initializer

**[0:05:21]** agent and then each of our coding agents are able to communicate with each other even though we create a brand new context window between each agent. And so the way that the initializer agent works is it sets up all the scaffolding and then it gives an overview of what

**[0:05:35]** it's set up in this file. Then we go to the second session in the system which is the first time we're running a coding agent. And so it is going to go to the cloud progress understand what was just done by the initializer. Then it's going to spin up the website with the init

**[0:05:51]** script. And then it'll read the feature list to figure out what is the first feature that I should knock out. And then it's going to run through this process to kind of catch itself up to speed on what we have in the codebase, implement the next feature, document

**[0:06:04]** that commit, and then go on to the next loop of the coding agent. So it gets its bearings. I often call this priming. It's going to understand what we already have, including reading the feature list to figure out what to build next. It's going to maybe do some regression

**[0:06:19]** testing, making sure that previous features are still working. That's a really important part of this harness as well. It'll pick the next feature, implement and test it, and then it'll update the cloud progress with a summary of what it did, and then make a get commit. So, we have a save state after

**[0:06:34]** each one of our context windows, and then it's going to loop n number of times. This is going to go over and over and over again until all of the test cases are passing in our feature list JSON file. And what allows this to go forever basically is just the fact that

**[0:06:51]** we have this new context window every time we go into the next coding agent. And we have these core artifacts plus the process to make it so that even though we start a new context window every time, we can quickly catch ourselves up to speed on what has to be

**[0:07:06]** implemented. Even do a bit of regression testing before we now go into the next feature. So each coding agent is very granular and focused and that's what makes this process pretty reliable overall. And there are also some guardrails that we have in place for security. There are some validation

**[0:07:23]** tools so the agent can actually visit the browser and verify things visually. It's a pretty cool process. So we'll get into that as we start the demo here. Now if you thought that we're using the Claude Code CLI for this harness, you my friend are mistaken. We have true power

**[0:07:39]** and flexibility when we interact with cloud code directly in our Python or TypeScript code. And so for this demonstration, this harness that we're going to be using in a little bit here, we are using the Claude agent SDK to create our Claude code client and interact with it directly in Python

**[0:07:56]** code. And I really do think that this is also the direction that we're heading with coding assistance because it's really easy to build our own systems like this harness when we control things programmatically. And there are a lot of other AI coding assistants like Codeex and Open Code that are also coming out

**[0:08:12]** with SDKs. And I even included the Codeex SDK along with the clawed agent SDK in the remote agentic coding system that I covered in the live stream on Saturday, which is very exciting by the way. But I've done a lot of experimentation with this. So that's why I'm saying that I could very easily take

**[0:08:27]** this repository, swap out cloud code for codecs, and then still use the exact same harness because it is just those artifact files. and then the prompts that I'll show you later as well. So with that, let's actually get into the repository here and spin up our demo. All right, so I have the repository

**[0:08:44]** cloned locally and going through the prerequisites here to get everything ready to run is really, really straightforward. The only thing that I tweaked in my local version is I absolutely do not want to use my enthropic API key. That is going to charge me out the wazoo with the task

**[0:09:00]** running this long. I definitely want to take advantage of my Mac subscription and use my Claude subscription token. And so the way that you get that is you do claude and then setup dash token. It'll walk you through a little ooth flow. It'll give you a token that you

**[0:09:15]** can set as the environment variable cla token. So you just have to set that instead of your enthropic API key. And then I changed the code right here. And then I also removed something at the top of the client function. So that's all you have to do if you want to replicate

**[0:09:31]** what I set up here. Otherwise, you can of course use your anthropic API key. Just get ready to pay a good amount, especially if you're using open opus 4.5 for your coding agent. Other than that though, I just followed all the steps in the readme here. And so it got to the

**[0:09:46]** point where now I can run this command right here. So I run the autonomous agent demo and then all I have to select is the directory that I want to build this project in. And so I'm just using the exact same app spec that came with this repository because like I said, I

**[0:10:03]** want to clone Claude just like they have in the article. So they already had this full prompt created for me, which is very, very detailed. Obviously, we need something very detailed in order to create that featureless JSON file that has all of these different features and test cases that we need passing for the

**[0:10:20]** app to be complete. So this is my app spec. I'm going to send this in as context for the application build. And then once I kick things off, that's when I want to kind of explore the prompts more with you and also talk about how we are invoking the claude agent SDK. But

**[0:10:35]** right now, let's go ahead and spin this off. And this begins the 24 hours for our demo here. So, autonomous coding agent demo. We're using Opus 4.5 for our model. And we are going to start with our initializer agent. So, this is session number one. just like I was

**[0:10:51]** showing in the Excal Draw diagram and we are using this appspec as our PRD that outlines all of the features that we want to build. And so all the tool calls that we typically see within the Cloud Code CLI, we can see these here. It doesn't look quite as pretty, but we can

**[0:11:07]** watch it work. And so this is it's going to go for a while. The first session does take 10 to 20 minutes because it has to generate those 200 very detailed test cases. So, we have to be patient and that's why I'm going to take this as an opportunity to show you around the

**[0:11:22]** prompts more and then we'll come back to this when we get to the first coding agent session. So, the big question you have right now is where do the prompts come from? Because we're not using the cloud code CLI. We're not entering anything in ourselves or using any kind

**[0:11:36]** of slash command. But that my friend is the beauty of the claude agent SDK because within our Python code we are loading the initializer prompt from right here and then every session after that is just going to be loading in this coding prompt. So they're just markdown documents just like our rules and

**[0:11:52]** commands that you're typically working with with your AI coding assistants. And so for our initializer here, everything that we're about to go through should ring a lot of bells because we're just working with the same process that we outlined in the Excaladraw. And so we're giving it context like you were the

**[0:12:09]** first agent in a longunning autonomous development process. And so you start by reading the appspec or the PRD. This contains the complete specification for what you need to build. And then based on that PRD, you're going to create that massive feature list JSON file that I showed you briefly earlier. So it's very

**[0:12:28]** very structured for every single feature that we need to build. We have the category, the description, the steps to validate the feature. This is really cool. And then also just true or false. Is this currently passing? So whenever a coding agent knocks out one of these features, it just goes back in the

**[0:12:44]** feature list JSON and changes this from false to true. So if I like scroll down to the very bottom here, this is from an old run, by the way, it would just like change this from false to true. And then we create that initialization script so the coding agent can spin up the website

**[0:12:58]** every time we have a new context window. It initializes the git repository and then creates the boilerplate for our application structure. And so then the coding agents already have at least something to work on top of even though nothing's actually working in the app at this point. And then finally, it creates

**[0:13:15]** that claude progress to just give a summary of what it set up. And so this is an example of the cloud progress right here. This is completely wiped and uh redone every time we have the end of a session. So that is the initializer. And if we go look at our terminal right

**[0:13:32]** here, it is still running. So at this point, we've created our feature set. Now we're just working on some of these other things like creating the initial project directory structure. So, it's working through everything that we just saw in the initializer prompt. Now, once the coding agents start running, that's

**[0:13:49]** when we use our coding prompt. And so, this one is a little bit more complicated, but it's still not too bad overall. And so, we obviously have to start by getting our bearings because we're dropping a fresh context window into an existing project. And so there's a couple of commands that we want to run

**[0:14:06]** just like understand our PRD. Look at the feature list to see what we should build next. Look at the cloud progress so we can see what the initializer agent did if this is our second session. Otherwise, we're looking at what the coding agent did in the previous run.

**[0:14:21]** Taking advantage of the git history as well. Like I said, git is a very crucial part of our process and our harness here. And then we're going to start up the servers with the initialization script. So going back to our diagram here, we are reading all of our core

**[0:14:36]** artifacts and taking advantage of those in our agent loop here. And then we're going to do some verification. So before we do anything new, it's going to do a little bit of regression testing. So just spot checking here. We look at a couple of the more recently implemented

**[0:14:50]** features that are marked as true uh for the passing in the featureless JSON here. And it's just going to make sure that those things are still working. And this is really important because as we're building out so much code in our project here, we might be breaking old

**[0:15:06]** things. So I really appreciate that regression testing is built into this. Now, if there are any issues that are found, then we're going to address them. So go back to the feature JSON, mark it as false, fix the issue, and then go through the steps again to verify that

**[0:15:20]** everything is working. And we have the Puppeteer MCP server attached to the coding assistant. Like if we go and look at how everything is configured here. We're giving it the Puppeteer MCP server. So it can actually go and verify that things are working on the website. Like this is what we have right now for

**[0:15:38]** our initializer agent running. It actually spun up the website to make sure that our little hello world boilerplate is working. And so as it's building out the application, it can even validate things visually, which is very, very powerful. So we'll see a lot more of this as it's building things

**[0:15:53]** out. And then to finish off the coding prompt here, obviously once it does all of its regression testing, it's going to choose one feature from our JSON file. So kind of like you know the next one that has passes as false. And then it's going to implement it, test it, go back

**[0:16:09]** and mark it as complete after it does even like the full browser automation validation with Puppeteer like we just saw. And we have clear instructions here. Make sure that you only updated the passes field. you cannot change anything else because one thing that coding assistants do a lot is they get

**[0:16:26]** lazy and they say like oh I did the first four steps of validation I don't need to do the last one so let me just remove it so we're making sure we avoid that by saying you cannot update the steps you can only update false to true and then of course our very last step is

**[0:16:40]** to make that save state with git so we are committing our progress and then updating the clawed progress so that the next coding agent can read through exactly what was done with the last loop and So then we end our session and the rest of this here is just kind of

**[0:16:54]** miscellaneous instructions. That's really the end of the process that we have for the coding agent and we're just going to be running this over and over and over again. So at this point we've gone through all the prompting for this system. It really is simple. We rely on

**[0:17:08]** these core artifacts. We have one prompt for the initializer and then one prompt for all of our coding agents. And by the way, if you want to understand best practices for security, permissions, things like that, for defining our agents in code, this repository is fantastic for this. I don't want to dive

**[0:17:25]** into the code too much, but it's worth showing you a little bit how this works with the cloud agent SDK. So, when we create our client, first of all, we pass in a project directory. The coding agent is only able to operate in this project directory, which is already a good layer

**[0:17:42]** of security, right? The file operations are restricted to the project directory only. We have our sandbox environment. And then we have our permissions where we just accept all edits. So we don't need human approval for changes. Obviously that would not work for an autonomous system. And then we define

**[0:17:58]** the specific commands that claude code is able to run in the cloud agent SDK. Reading files, writing files, using the Puppeteer MCP server for the browser automation, all that good stuff. And it even goes so far as having a hook. So every time we use a tool, if it is

**[0:18:15]** running a bash command, we also have this entirely separate Python script that manages the different kinds of bash commands that we're allowing cloud code to run. So it can't do things like delete directories or work outside of our current codebase. And so this is really really powerful. It gets quite

**[0:18:32]** technical, but if you are more technical and you want to understand like how can it end processes without killing itself, for example, it's definitely worth diving into this. And then finishing things off for the client here, we have the MCP server for Puppeteer, which by the way, the Puppeteer MCP server, it

**[0:18:49]** takes a while to validate things cuz the agent, it spins up the browser, it waits for things to load, then it clicks on a button and waits for that to load. And so we go for 24 hours, but it's not like we're spending millions and millions of tokens because we are waiting quite a

**[0:19:03]** while for all the browser automation stuff. But yeah, we have our system prompt that we can customize as well, which is really cool. We define our model, all the allowed tools and the hooks and things, our current working directory. There's so much configuration that we have for the cloud agent SDK,

**[0:19:18]** which is part of why we need something like this when we have this harness that we want to control so much. And so when we actually invoke the agent, if it is the first run, we're going to get the initializer prompt. Otherwise, we get the coding prompt. It's just reading

**[0:19:33]** these in from these markdown documents. And then we send that into this function right here, which leverages the client that I showed you just now, how we define. So it runs this query here with the latest message, which this is going to be the message that's just loaded in

**[0:19:48]** from one of these markdown documents. We stream out all of the text and tool calls and we put that out to the terminal. That's exactly what we're looking at right here as we have our autonomous agent running. All right, our initializer agent has finished and we have the first commit for our initial

**[0:20:03]** setup. And one thing that this harness that this application does after every session is it automatically runs all the tests to give us a progress update. Now obviously right here we have a progress report of 0% because the initializer agent is only creating the foundation. it is not responsible for doing any

**[0:20:21]** feature development that would make one of these tests pass. And so that brings us to the second session or the first time we run our coding agent. It is going to create that secured sandbox environment and then go through the exact process that we saw in the coding

**[0:20:36]** agent prompt. So it does its prime here where it lists out the files, looks at the PRD and the cloud progress from the initializer agent, looks at the git log and the feature list, all these things that we've already gone over. It spins up the website with that initialization

**[0:20:49]** script and then we can see it using the Puppeteer MCP server to visualize things, even take a screenshot. It's looking at the API. You just saw it go there like just very briefly. It was doing a little bit of work and we can also see the website more plainly if we

**[0:21:03]** just like visit it in our own browser as well. So this is my personal browser and then what we're looking at right here, there's nothing being shown right now, but this is the browser that the agent is currently operating in. So this is the what we have built so far as I have

**[0:21:16]** the first coding agent run. So it's kind of just creating the initial user interface at this point. I'm not going to click through things right now, but most of this stuff is probably not working at all because we have just gotten started with the process here. And the first agent is going to be very

**[0:21:31]** granular in what it builds. So all this output here, I know that it's a little ugly, but it's pretty much what we see in the Cloud Code CLI. And so it just goes through the first feature and does all the testing it needs. And then in a little bit here, it'll probably update

**[0:21:46]** the cloud progress and then move on to our second coding agent session. And so at this point, I've covered everything that I want to cover. And so what I'm going to do here is pause and then next time you see me, the 24 hours is going to be up. We're going to come back to

**[0:22:02]** the terminal here, see what session we're on, see how many tests are passing, and then we'll also see what our application looks like. So, I'm doing this live with you. I have no idea how it it's going to turn out. I've tested the same thing, but only with a

**[0:22:13]** few hours. That's all I gave it. And so, yeah, let's come back together and see how it shapes up. All right, we are now at the 24-hour mark, and we have gotten to the 54th coding agent session. Absolutely crazy. I have no idea how many tokens I've used for this, but it

**[0:22:30]** is probably a lot. Thank goodness I'm using my Claude subscription. And we have 54% of our tests passing at this point, which after an entire day might not seem like a very high percentage, but we have given it a lot of different features to work through and implement.

**[0:22:45]** So having over 100 of the tests passing at this point is pretty cool. And going to our browser here, this is the website that I have spun up in my own browser, not the testing one with Puppeteer. It is pretty impressive everything that we have built out right now. And honestly,

**[0:23:00]** I don't even know what the last half of the tests are for because it already feels like I have a completely functional clone of claw.ai. And it's cool. We can go through all of the past conversations that it generated as it was verifying things through each of the

**[0:23:15]** loops. We have really nice markdown formatting. We are able to create these different HTML pages and even write and execute code. We have a settings where we can change the theme and our default model and a slider for the max tokens. Like this is just so so featurerich.

**[0:23:32]** Like it's a lot more than if you were to just in a single prompt ask it to make a clone cuz it's not going to build out all this functionality. Even being able to see the token count for the responses and I'll create a new chat here and send

**[0:23:43]** in something myself. So I can see the number of characters and estimated tokens for my own prompts. And you can see here that like the UI isn't perfect. And so I definitely didn't expect this to be perfect. We still want to come in and add a human in the loop. But it

**[0:23:58]** still is really cool how much I was able to build here without laying a finger on anything. And honestly, who knows? If I let it go for another day and it goes through all of the features, maybe this would be an absolutely perfect application cuz it really is crazy the

**[0:24:13]** kinds of things we can build with Claude Opus 4.5. And then having a harness like this to let it do so much validation and iteration on an application. And also it's really cool to look through the featureless JSON as well. So passes is true for a ton of these different

**[0:24:28]** features now. So I have to scroll all the way down to the middle to start seeing the ones that are false for passes. So now we start to see the next things that we have to work on. And these are very very specific scroll bars and mobile styling and dividers. like

**[0:24:44]** we're getting to the very nitty-gritty details of making a very complete Claude clone. And then in the cloud progress, we can see what happened in the previous session and then even an overview of what happened in sessions before that. One thing that's really confusing here is I don't know why it says session 34

**[0:24:59]** when we know that we're on session 54. So like the harness seems to have veered off a little bit, but it still is knocking out feature after feature pretty quickly. I've been watching the logs towards the end of the execution and that's one of the things that I was

**[0:25:13]** really nervous with is that like it'd work really well for the first, you know, 10 20 sessions, but then it would start to hallucinate a lot and like go through features willy-nilly here and start to totally mess up the cloud progress, but like overall it seems to be very aligned even as we go through

**[0:25:28]** dozens of sessions. So, I got to hand it to Anthropic here. Overall, I'm very impressed. Not that I haven't had these kind of longunning sessions work before, but being able to do something really out of the box with a resource that they have open sourced is really fantastic.

**[0:25:43]** And so I would encourage you to try this out yourself. Clone this repository that again I will have linked in the description. You can even go within the app spec here and change what you want to build. So if you don't just want to follow along with what they show here

**[0:25:56]** and build the claude clone, you can build any application that you want, any kind of backend, any kind of front end, it works with all of this. you just probably want to have some kind of user interface to take advantage of the Puppeteer MCP server integration. But otherwise, it's really up to you what

**[0:26:11]** you want to use this harness to create. And so, I hope that you appreciated this video and it gave you some ideas for ways that you can build this kind of harness into your own AI coding system. So, if you appreciated this video and you're curious how you can take these

**[0:26:25]** kinds of ideas and use them to build your own system for AI coding, definitely check out the Dynamus Agentic Coding course that I'll have a link to in the description and the pin comment. This is the best resource you'll find on the internet for learning how to build

**[0:26:40]** reliable and repeatable workflows for AI coding. So, definitely check it out and I will see you in the next video.
