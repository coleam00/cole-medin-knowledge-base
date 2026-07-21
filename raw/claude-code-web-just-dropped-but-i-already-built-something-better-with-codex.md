---
type: raw-transcript
title: "Claude Code Web JUST Dropped but I Already Built Something BETTER (with Codex!)"
youtube_id: injqJTy5Tus
url: https://www.youtube.com/watch?v=injqJTy5Tus
slug: claude-code-web-just-dropped-but-i-already-built-something-better-with-codex
published: 2025-10-22
duration: "0:18:01"
fetched_at: 2026-07-21
immutable: true
---

## Transcript

**[0:00:00]** Anthropic has just released cloud code for the web. It's pretty cool. I can send off any request to my AI coding assistant on any GitHub repository and it just goes to town completely remote agentic coding. And there are a lot of other tools out there for this kind of

**[0:00:16]** thing already like Jules, OpenAI, Codeex has their cloud version. So a lot of options out there for remote agentic coding. Now, as much as these tools fascinate me, I don't think they're very practical for me yet. And the biggest reason for that is I feel like I don't

**[0:00:33]** have a lot of flexibility and control when using these tools. I can't define my own commands and prompts that I can chain together. It's hard for me to connect my own MCP servers. Some of these tools, it's not even possible. And maybe this is partially my fault, but I

**[0:00:47]** really don't like setting up my AI layer, things like my global rules separately from where I'm actually sending in the request to the AI coding assistant. And so that's why I truly believe I've built something better. And that's what I want to show you in this video because I have integrated OpenAI's

**[0:01:05]** codeex as the coding assistant directly into Telegram. Not only that, it's my own workflow that I have defined powering the bot behind the scenes. And so I can kick off this request from my own application anywhere that I want, even on my phone. And so this is another

**[0:01:21]** advantage here is I can use my own applications like Telegram or Slack, GitHub, wherever I want to work. I can integrate Codeex directly. It's my own custom solution. All right. So I want to start by demoing this workflow for you live. We're going to update a website from code all the way to a production

**[0:01:37]** deployment with the help of Codeex. It's super cool. Then I'll cover how everything works under the hood with the Telegram integration and the codeex SDK, how the human in the loop works that you'll see in a little bit, and of course, how you can run this all yourself. This is all completely open

**[0:01:51]** source for you. And I also want to say that I chose Codeex very intentionally here over Claude Code. I know a lot of you are frustrated with their rate limits right now. So, I just want to show that like we're not reliant on cloud code for any of these freaking

**[0:02:04]** awesome things we can build. That's why I'll be using codeex here. And this entire repo I'll have linked in the description. Like I said, all open source for you. I've got instructions for running everything, even setting up your Telegram bot. So, very easy to get started. If this workflow is fascinating

**[0:02:18]** to you, which I really hope it is, and you want to try this out for yourself and everything that I cover in this video is completely free. Telegram, the cloud platform where I have things deployed, the human and loop tools with browserbased later, all that is free to

**[0:02:32]** get started. And so, first of all, what are we doing for the demo here? Well, I have this website that I'm going to use for the workflow, and you can actually go to this right now. It's coach.dynamus.ai. It's a really cool agent that I'm building for my YouTube channel right

**[0:02:48]** now. So, it's going to be a rag agent that's trained on all my YouTube videos and open source repos and everything. So, you can go and ask any questions about building agents or using AI coding assistants. I'm actually super pumped for this. And this isn't just a mock

**[0:03:01]** website. you can actually go and fill out this form to be notified when this agent is available. It'll be a free resource for you as a part of my YouTube community. So, yeah, I want to make some changes to this website as a quick demo for you cuz let's say I'm out on the

**[0:03:14]** golf course and I have this genius idea for this website, but I don't want to wait until I get home to make that change. And so, I can go in Telegram on my phone, talk to Codeex and say, go and implement this idea into my website. And then it's going to deploy that to a

**[0:03:31]** staging environment that I have. So I have a secondary like test version of the website where the coding assistant can make changes. So I can go and validate. I even have some tools with browser base that I'll show you for it to validate its own work. And then after

**[0:03:44]** I can say, okay, the changes are good. Now go and deploy it to the primary production version of the website. That's everything we're going to do is this full workflow directly in Telegram. So with that, let's go ahead and see this in action. And to show the true

**[0:03:58]** power of this, of course, I'm not going to send in the request for my desktop. I'll do it from my phone. So, I've already got it typed out just to save a little bit of time here, but I'm calling out the repository specifically that I wanted to make changes in just like I

**[0:04:10]** would do by selecting that in cloud code for the web or something like codeex in the cloud. I know it's not as nice that you don't have like a drop down to select your repos, but this is more of an experimental thing that I'm working on right now. And there we go. It's

**[0:04:22]** already getting to work. It's giving me all the tool calls in real time. So, it has to start by cloning the repository because I really am starting with a blank slate inside this container, which by the way, we can see all the logs as well, all the different actions that

**[0:04:35]** it's taking and the text that it's giving back to us using the GitHub CLI to perform all these actions for me. So, I have the authentication set up in the container. So, there we go. Cloned the repo. Now, it created a new branch that's part of the workflow that I have,

**[0:04:48]** which by the way, this entire workflow is just defined in an agents.md file that I have within the repository. And so I'll show you that really quick. Part of this workflow is when the container is created, it takes this agents.m MD and it puts it in where the codeex SDK

**[0:05:06]** is going to read. And this defines the entire workflow. When I ask for a new feature, there we go. It's going to create that branch. It's going to make these changes and push it into that staging. So we can see that in the secondary version of the website. It's

**[0:05:17]** taking care of all this right now. And so I'm going to pause and come back once we have things ready for verification in our staging environment. And there we go. Just 1 minute later, we have everything good to go in our staging environment. So it updated the copy and

**[0:05:34]** then it set up the config I need for GitHub to push the change and then it also merged the pull request from that feature branch it created into the staging environment. And it gives me a summary at the end. And then as a part of the agents.mmd, I also gave it the

**[0:05:47]** URLs I have. So it reports back to me the URLs I can go visit to validate things. Right now the staging one is the one that is updated. And so going to my GitHub here, I'll just show you really quick. Boom. This is our pull request that is merged. And then in render,

**[0:06:00]** which is just the platform I'm using to deploy things here. I'm just on the free tier. Super easy to get started with render. I've got my production. And then I have my staging. I can click in here. I can view the logs. Sure enough, just one minute ago, we have a successful

**[0:06:13]** deployment. So now, moment of truth. Going over to our URL here for the staging environment. This is the old copy that we have at the front. I'm going to do a full refresh here. And boom, there we go. Your personal AI coach using Cole's YouTube content. So, I just wanted to change that here cuz I

**[0:06:29]** think the old text was a little bit egotistical. So, there we go. We fixed it. But it's still here in production with the old copy. And so, I wanted to not have it deploy things to production end to end because I want some time for human in the loop. And not only can I

**[0:06:44]** verify the staging URL myself, but the other thing I can do back in a telegram. This is part of the workflow that I've built. And and guys, this is the kind of thing you can't just do in codeexcloud or cloud code for the web. I can have this as a part of my workflow with the

**[0:06:57]** stage hand MCP server. I'll explain that in a second. I could say go and validate the changes in the staging environment. And this is going to leverage this MCP server I have for browser use. So, it's going to visit this URL itself, make sure that the changes are deployed, and

**[0:07:15]** then there's even going to be a session replay that I can go visit myself to validate its own validation, right? Like I'm just constantly making sure that the coding assistant is doing things correctly because even with remote agent coding, we still want to be a part of the process validating things. And so

**[0:07:31]** going in the container logs, we can see the different MCP calls to the stage hand MCP. It's creating a remote browser session, visiting our staging URL, making sure all the changes look good, and then reporting that back to us. And we can even go and view the session

**[0:07:46]** later. And so we'll see that in a little bit once it gives us the verification response. So I'll pause and come back again for that. And take a look at this. As we have codeex validating the website, we can see its live session in a browser base looking at everything

**[0:08:00]** that it's viewing to validate its own work. Super super cool. The visibility that we have into this is awesome. So, if you don't know, browserbase is a platform for running these remote browser sessions for agents. And the stage handm is our way to very easily direct our agent to navigate this

**[0:08:17]** website. And they have a lot of other cool things they're releasing like for example, agentic autofill for credential access is something they have coming out soon. So, I might be covering browser base and more content in the future. Uh, there are definitely a lot of options we have for browser use here. The main

**[0:08:32]** thing that I want to drive home is that we want as a part of our validation process some kind of MCP server or tool for our AI coding assistant to actually view the deployed website and validate everything. That's exactly what we have here. All right. So, back in the chat,

**[0:08:49]** the validation is complete. It's telling me that I can check myself, which we already did that. So, now it's asking me, do you want to push this live to production? The end of our workflow. Super cool. Let's go ahead and do that. Yes, go and push this to prod. All

**[0:09:04]** right. And so now it's going to go through another process of creating a pull request, but this time from staging into main. And I have it set up in render my cloud platform just like with staging where when there's a commit to main, it's automatically going to build

**[0:09:17]** things and deploy things to production for me. So it really is end to end. I could have done this entire thing from my phone and we'd have our change that we get to validate and update the live website. So I'll come back again once we're good there. All right, perfect.

**[0:09:30]** So, it told me that the production build is in process now because it merged the poll request from staging into main. And so, I can go and take a look at the logs and render for my production version of the website. And sure enough, yep, we got our successful deployment. So, I'll

**[0:09:45]** go back over to the real URL, coach.dimus.ai. Refresh this. And boom, there we go. Your personal AI coach using Cole's YouTube content. So, now we have it deployed completely end to end. So, I know that was a bit of a longer demo here, but I hope that you found this

**[0:10:00]** really fascinating, the kind of workflow that I'm able to build. And we can do this for websites, for AI agents, for any type of application. You can incorporate any rules or slash commands that you want. That's the power that we have that we don't necessarily have with something like Codeex Cloud or Cloud

**[0:10:14]** Code for the web because like I'll show you in a little bit. It really is our own application that we're building here. I'm using the Codeex SDK to programmatically invoke codecs in my own environment. All right. So, with that, I want to show you now how I built this

**[0:10:30]** integration, at least on a high level, because hear me out on this. I really do think that the future of AI coding is using these SDKs like the Codeex SDK or the Claude agent SDK to define and build our own custom AI coding assistance that can integrate with any workflow we want

**[0:10:47]** and any application like WhatsApp or Telegram or Slack just like I showed you. And so, I'll have a link in the description to the Codeex SDK documentation that we're looking at right here. here it is a TypeScript library. So everything I just showed you that's available in the repo for you is

**[0:11:02]** a TypeScript application and honestly the most useful place for their documentation is their TypeScript repo right here. So I'll also link this in the description at a high level. And if you saw my last video on the cloud agent SDK, things are actually pretty similar with the codeex SDK. It's a package that

**[0:11:19]** we install just with TypeScript instead of uh Python because Python is where I use the cloud agent SDK. Then we import it into our code. And then we start what is called a thread. That's how we manage different conversations with codecs within our TypeScript code. And then we

**[0:11:35]** can run these threads just by sending in the latest user prompt. And this is automatically going to load in all of our slash commands we have in ourcodex folder. It's going to load in the agents.md that we have in our current directory where we're running this script. So we have that entire AI layer

**[0:11:49]** just like when we run codecs in the CLI but now we get to define it in our own workflows in code integrating with our own applications and whenever you are invoking you can also call this run stream function here so you can loop through all the events that we get

**[0:12:04]** that's how in telegram I was able to stream out all of the actions in real time as they took place and we can watch for the very end of that turn as well so that we can end that interaction and then move on to the next message. And

**[0:12:19]** whenever you are invoking your threads here, you can get a thread ID so that you can resume your thread. And so I have this set up in Telegram. Like I'll actually show you that really quickly. If I were to reset my conversation, now we have a brand new conversation. So I

**[0:12:33]** set up this Telegram in integration to always have one conversation going per user. And you can reset it whenever you want. And so until I hit the reset here, what I'm doing within the code is I'm resuming a thread every time I send in a new message in Telegram. And that's

**[0:12:49]** pretty much it. Like there aren't that many things that we define in the code here besides our current working directory because everything else is just loading in the AI layer from our current workspace. Things like our global rules. Now, the other thing that's really important to call out is

**[0:13:03]** how authentication works here. And this is the same with the cloud Asian SDK. when you sign into the codec cli like you just go into your terminal and run the codeex o command those credentials are automatically going to be available for when you run the SDK as well I'll

**[0:13:18]** show you that when I run the codeex o it creates this o json file I'm not going to open this obviously because that'll share my secrets but in this file you have a few different credentials that we need to authenticate with openai for using codeex and so this is going to be

**[0:13:33]** used automatically when we use the codeex SDK K. Now the slightly tricky thing with this here is that we are running everything within a container. So we don't have the luxury of just using our already authenticated codeex because we're running things in an isolated environment in this container.

**[0:13:54]** And so I have this called out in the readme specifically how you can set up your environment variables so that you're bringing in the different values that you have from that o JSON file. So you authenticate with codeex on your computer, copy the credentials in here, and then you add those as environment

**[0:14:12]** variables. So that's how I have the access set up. And actually took me a bit to figure this all out. So this is one of like the big things that I'm saving you time here with is how we can create this totally isolated container ready to work with all of our

**[0:14:25]** repositories that has the codeex authentication good to go. And speaking of repositories, we have a very similar thing with GitHub. So you grab your GitHub token just going to this URL and then we're setting this as an environment variable for the container as well. So we spin up the container

**[0:14:40]** already authenticated with both codeex and GitHub and that's really all we need to emulate what these other cloud solutions give us like codeex cloud. We just need access to codeex and access to GitHub. We're doing both these through environment variables and then obviously setting the one for our telegram bot as

**[0:14:57]** well. And then I have everything related to the stage hand MCP server as optional. So if you don't want to do that browser automation as a part of the validation and the human in the loop and you just want to go and view the website yourself, you definitely can do that. I

**[0:15:10]** just think it's really cool how we have those session replays where we can go and actually check what the AI coding assistant did to validate the website. So that's everything for the environment variable. So I guess I'm kind of walking you through a setup here because I really want you to go and try this out

**[0:15:23]** yourself. Like this is just so cool really out of the box. like you only have to set up these things, spin up the container and boom, now right within your Telegram after you have your bot created, you can just go to town with codecs. And in the Dynamus community, I

**[0:15:36]** even showed recently how we can deploy something like this completely remotely to something like a digital ocean droplet. So you don't even have to have this running on your computer to always have access to your coding assistant, even from your phone. It's just freaking awesome. And then just a one minute

**[0:15:52]** really quickly on the code in case you're curious. So we're using the Telegraph library in Typescript for our Telegram integration. And this is our function to handle any message that we have come in from Telegram. So we get the user ID, we get the user message, and then we're going to get or create

**[0:16:07]** that session in Telegram based on that user ID. And then very similarly with the codeex SDK, we're going to either get or create a brand new thread like I showed you the threads in the repository for the SDK. And then we're going to send an update that the bot is currently

**[0:16:22]** typing. And then we're going to run that stream function that I have. And so this gets into all the code that I have for the codeex SDK specifically. And this is going to look very similar to what we saw in GitHub. So when we create a thread, we're just doing codeex.st start

**[0:16:37]** thread, right? And we're passing in our current working directory. And there are even commands that I have in Telegram for us to switch our current working directory. If we want to work on different repositories, we don't even have to restart our container. And then also we can resume a thread, right? just

**[0:16:51]** giving the thread ID that we have saved in a file. And then when we want to invoke the codeex SDK, so we're either going to get a thread by creating one or get a thread by resuming one. Now we just call thread.runstreamed with our current user prompt. It is that easy to

**[0:17:09]** use the codeex SDK in code. So I told you it was really just going to be a couple minute explanation here. There's not that much that we have to do. It almost is as simple as just booting up Codeex in the CLI and sending in your coding requests, but now we can do it

**[0:17:22]** from anywhere. So, there you go. That's all I have for you today. I just wanted to show you a super kick-ass workflow. And hopefully this really sparks your imagination for the kinds of things you can do because the sky really is your limit when we are defining our agents

**[0:17:36]** programmatically integrating with any application. There's a lot more flexibility than using one of these other tools as cool as they are. So, I hope that you found this super valuable and go and try this integration yourself. If you appreciated this video and you're looking forward to more things on building AI agents and AI

**[0:17:54]** coding assistants, I'd really appreciate a like and a subscribe. And with that, I will see you in the next
