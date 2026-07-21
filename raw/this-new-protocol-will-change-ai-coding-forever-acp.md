---
type: raw-transcript
title: "This New Protocol Will Change AI Coding Forever (ACP)"
youtube_id: 5gUR55_gbzc
url: https://www.youtube.com/watch?v=5gUR55_gbzc
slug: this-new-protocol-will-change-ai-coding-forever-acp
published: 2025-09-10
duration: "0:22:35"
fetched_at: 2026-07-21
immutable: true
---

## Transcript

**[0:00:00]** The future of AI coding is here and my friend, I mean that most sincerely. Zed has just introduced the agent client protocol or ACP for short. It's a standard just like MCP, but for connecting any coding assistant to any code editor. And Zed's integration is only in beta, but if you want a glimpse

**[0:00:20]** into how we're going to be working with AI in the near future, this is it. So, right now, I'll show you ACP in action and how you can get started with it yourself right now. Lot of exciting stuff today. I'll start by showing you how we can run both cloud code and

**[0:00:33]** Gemini CLI threads in Zed and switch between them at the click of a button. And with ACP, we get live updates in our code editor as the coding assistant is working. And we can accept and reject changes, which are things that I've always wanted in Cloud Code. It makes

**[0:00:49]** the development experience so much better. And since ACP is a standard, we're able to create our own custom agents that we can attach as coding agents into any editor, just like with MCP, we're able to build tools that we can connect into any agent. I'll show you how that works as well, and even

**[0:01:06]** show you some ideas we're cooking up along these lines with Archon. So, I'll be sure to cover how ACP works at a fundamental level as well. Definitely is worth understanding this incredible new technology. So, I first found out about ACP from this Zed announcement announcing that they now have support

**[0:01:22]** for Cloud Code. If you don't know, Zed is a code editor just like VS Code and its forks like Windsurf and Cursor. And so, I was really interested how exactly they integrated with Cloud Code. So, I clicked into this, read through it, and it immediately jumped out to me that

**[0:01:37]** they didn't just build a one-off integration with Cloud Code. They wanted to build something better and that is the agent client protocol. The standard like I said for connecting any coding agent to any code editor and this is just such a gamecher. It makes it so easy to switch between coding

**[0:01:55]** assistants. That's becoming increasingly important right now as we start to get more and more options. Cloud code is becoming less and less of an obvious winner right now. And so we want to move between these code editors and try different ones seamlessly. And that's what ACP gives us. It's about time that

**[0:02:11]** we have this standard. And more on this later, it makes it easier for us to run a lot of code agents in parallel. And all you have to do to get started with ACP is install Zed. That's what we're looking at right here. It's a completely free and open source code editor. And

**[0:02:26]** I'll have links in the description to install this depending on your operating system. And I'm sure in the very near future, we're going to have a lot of other code editors like VS Code also support ACP. But right now, we've got Zed. And then for coding assistance, Gemini CLI actually has a direct

**[0:02:40]** integration with ACP. And then Cloud Code is through an adapter. More on that later. And I'm sure they're going to be a lot more coding assistance in the near future here that will also be supporting ACP. And once you have it installed, hooking into the Gemini CLI or Cloud

**[0:02:55]** Code right within Zed could not be easier. Literally, all you have to do is open up this agent panel on the right hand side. So it's just this button in the bottom right to toggle it on and off. And then you click on this plus button right here. And you can start a

**[0:03:08]** new Gemini CLI thread, Claude Code thread, or any custom agent that you build, which I'll showcase in a little bit here. So, for example, let's start a Gemini CLI thread. It'll load up the connection to the Gemini CLI. It'll have you authenticate if it's your first time, which that is all done right

**[0:03:25]** within the code editor as well. So, it's super super easy. I can reauthenticate if I need to. I don't even have to do any external setup to bring these coding assistants into my editor because that is also a part of ACP. It is a beautiful thing. And so now I can send in a

**[0:03:41]** request here like change the greeting message in and I can at@mention files like you would expect to something random. All of the native features that we have for these coding assistants work with zed through ACP as well. So things like sub agents and custom slash commands like we have with cloud code,

**[0:03:59]** all of that is still going to work. So we lose nothing and now we have everything in this development environment. So we can see these changes live in our IDE. We can accept and reject these things. The kind of stuff that I've always wanted to have with Claude code. So I'll reject this one for

**[0:04:15]** now. I don't need it to run this command because yeah, that's just quick demo of the Gemini CLI. And then if I want, boom, there we go. I'm now loaded up a new thread for Claude code. And I can do another request like change the goodbye message to something random. Or I could

**[0:04:29]** build a slash command to do this, right? And so, yeah, send in this request. It's going to make an edit just like the Gemini CLI, but it's using an entirely different coding assistant, even though it seems like it isn't because it was that easy to switch between them. And

**[0:04:41]** there we go. We got the change request from Cloud Code. Everything looks the same as Gemini CLI. I can show it looks like to reject this now. So, I can reject and give feedback. The kind of thing that I used to do in Windsurf and Cursor all of the time that I had to do

**[0:04:53]** more of like a Git integration to revert stuff with Cloud Code up until this point. Now, I will say that this integration definitely feels like it's in beta in some ways. First of all, sometimes when I open a new Gemini CLI thread, it'll hang there trying to load

**[0:05:08]** or connect to the Gemini CLI. Obviously, it's working right here. I've had that happen a couple of times. Also, it appears that the thread history doesn't work, which is kind of a bummer. So, a couple of glitches I think that need to be worked through here. But, I hope that

**[0:05:21]** you can see that this is definitely the future for AI coding. Just look at how easy that was to interact with the coding assistants in my IDE and switch between them as well. It also is very much worth understanding how ACP works fundamentally. I used to say this all

**[0:05:37]** the time for MCP as well. Even if ACP doesn't end up being the primary standard adopted for connecting coding agents to code editors, whatever that main standard ends up being, it's going to look a lot like ACP. And I can say that with confidence because Zed clearly has a good head on their shoulders with

**[0:05:56]** this implementation. They took a lot of inspiration from other protocols like MCP and also the language server protocol. This is the standard for connecting programming languages to code editors. So it's definitely the most similar protocol. It's been around for about a decade now. And so they're building on top of the shoulders of

**[0:06:15]** giants here. Definitely doing it right. And so I want to focus on ACP here. I'm not going to dive a ton into leveraging AI coding assistance in this video or just focusing on the protocol. I will say though that if you want to 10x your AI coding workflow, really take it to

**[0:06:30]** the next level, check out this link that I'll have on the screen right here. I've got a really exciting workshop coming up that you won't want to miss. I'm just going to leave that golden nugget here. Definitely check out that site. And with that, let's go ahead and move on. So, I

**[0:06:43]** will have a link in the description to this ACP documentation if you really want to dive into the architecture and how it works under the hood. I'm just going to cover kind of the high-level ideas here just to help you see how powerful this really is. And so, we've

**[0:06:57]** got our first simple diagram here where we have our code editor that has a standard IO. So, just a local connection to the coding assistance that we have running. So it spins up an instance of the Gemini CLI or an instance of cloud code under the hood that it's connecting

**[0:07:12]** to within Zed and it's very similar to how MCP works. So like I said, they definitely are taking inspiration from these protocols that are working very very well. And if we go to an overview of the protocol, this is where they start to talk about how the communication works under the hood

**[0:07:28]** between our coding assistants and code editors. So, it's following a JSON RPC protocol just like MCP does. And so, I'll show you a couple examples of what this looks like. It's actually very simple because there's just a few set operations that a coding agent is going to perform. And so, I'll go to the

**[0:07:47]** prompt turn tab here so you can see what this looks like. First of all, we create a session between the client and the agent. It's kind of like a handshake. And then just as things are happening like tool calls or permission requests or just chunks of text that it needs to

**[0:08:01]** send, these are just going back and forth between the code editor and the coding assistant. And so this is an example of the JSON event for a user message. So whenever we have a user enter something into the editor, it's going to send this JSON event through ACP to our coding assistant so it can

**[0:08:21]** understand what the user is asking for. It's going to even include things like images or resources, calling out specific files that we want it to edit. And then when the agent responds, there are a couple of different responses that it can give. Like first of all, this is

**[0:08:34]** an example of the JSON that we need our coding assistant to give through ACP when it wants to communicate a task list that it wants to knock out. We see that all the time with cloud code. Or if it wants to just send some plain text, it looks like this. We have a a type of

**[0:08:50]** agent message chunk. Here's the text that it's going to send through. So, we can stream that out in our editor. Or if it wants to make an update to a file or read a file, those are all done through agent tool calls. And so, we have a session update of type tool call. And

**[0:09:04]** then we can give it a title, any other kind of metadata. Basically, anything that you would ever see within cloud code or the Gemini CLI where you can see the tool call, you can see the file that it's affecting or the line numbers. All of that metadata is passed through the

**[0:09:19]** JSON payloads here with ACP. And there's a couple other things I don't want to dive super deep into right now. Definitely check this out if you're curious and if you want to build your own custom agents because armed with this information, we can also start to play around with the idea of not using

**[0:09:35]** cloud code, not using Gemini CLI, but actually building our own custom agent. And they have an example of that in GitHub as well. The sponsor of today's video is fly.io, IO, a developer first cloud platform that makes deploying your AI Asians, frontends, really any type of application super straightforward. We're

**[0:09:52]** talking about using AI coding assistance in this video, and you can build amazing things with them, but you have to have a place to deploy to production. And that is where Fly.io comes in. And what makes them stand apart is they have their own infrastructure. They're not just another

**[0:10:08]** AWS wrapper, which means that everything is going to be cheaper and faster for you. And you can deploy very easily, no matter the framework that you use. And all you have to do to get started with fly.io is create your account for free to get started. And then you can install

**[0:10:22]** the CLI so you can work with it on your computer. And then you log in with the fly off command. And then take a look at this. I can go into the directory where I have my application and run fly launch. It is going to automatically recognize the type of my application and

**[0:10:37]** configure things to deploy everything automatically. There's basically nothing more that I have to do. It is that easy. I can customize any configuration that I want. Otherwise, I just went with the default values. So, it went ahead and built the container for my type of application, deployed to the cloud, and

**[0:10:52]** gave me a domain, which I can customize later. So, here in the dashboard, we can see our application. Click into our URL here, and boom, there we go. We have our front end deployed on Flat.io's global infrastructure. And this is actually the front end that we're building on top of

**[0:11:06]** in the AI coding workshop that I mentioned earlier. It was that easy to get everything deployed to production and fly.io is free to get started. So if you have those awesome projects that you've been building with AI coding assistance and it's time to bring them to production, this is your platform to

**[0:11:22]** do so. I'd highly recommend checking them out. Link in the description. So if we want to build a custom agent using ACP, we just need to build an application that follows this architecture. We use a large language model under the hood to accept requests to make code changes and then use tools

**[0:11:38]** to do so and communicate that back out through ACP. So they have a TypeScript example in their GitHub repository. I'll link to this below as well if you want to check it out. This is what we're going to test out within Zed right now. And so they have instructions in this

**[0:11:52]** repo where you can just clone it and then you add into the configuration in Zed. I'll show you what that looks like in a little bit as well. And so clicking into agent.ts, ts. I'll just show you how this works really quickly. This isn't going to be an intelligent

**[0:12:05]** conversation with a real coding agent. It's just a bunch of hardcoded messages that are going to be sent through ACP when we send in a request. So, it's just kind of a demo that we have here. But first of all, we have our initialize function. This is what happens whenever

**[0:12:19]** we make a new connection to the coding assistant to set things up. And then when we make a new session or in Z a new thread, this function is ran. And so once we are in the prompting mode, this is where we're going to simulate a turn. And so this simulate turn function. This

**[0:12:35]** is where you would typically invoke a large language model and get out the tool request for it to read certain files or edit certain files. In this case, like I said, we just have hard-coded JSON messages following the ACP protocol to give these updates to the frontend. So we send in a request

**[0:12:52]** and then the agent is hardcoded to communicate through ACP back to our code editor. I'll help you with that. Let me start by reading some files to understand the current situation. And then it sends a mock tool call saying that it's going to read a specific file. And then it does another update here

**[0:13:08]** saying that it is going to replace some content in a file. So just communicating some fake tool calls that act like the agent would act if there was a real coding agent hooked up here. All right, so back over in Zed because I followed the instructions in the GitHub to get my

**[0:13:24]** custom agent installed. And the way that you get to that configuration, by the way, is you click on the three dots in the top right, go to the settings, and then we can add an external agent like I've already done here. So, we've got the Gemini CLI, we've got Cloud Code.

**[0:13:35]** Now, we can add our own. So, it opens up this JSON right here for you right away to add in the path to your own custom agent. Like in this case, this is the TypeScript file that we have pulled down from GitHub. So, I'm going to actually delete this here. I don't need to add

**[0:13:48]** another one, but I can save this. And then you'll have your external agent that you can connect to. So going back here, I can open up a new thread with my custom agent. And it's nothing fancy right here. It's just those hardcoded messages that we saw being passed

**[0:14:03]** through ACP. But just look at how seamless that was. Like the code was pretty simple overall in that TypeScript file. But now we have everything integrated already with Zed and with any code editor in the future that works with ACP. So, it's that easy to build our own custom agent with all the

**[0:14:19]** different operations that we typically see with coding assistants. And like I alluded to earlier, and I promised I would hit on this more, Cloud Code does not have a direct integration with ACP. So, for Zed to add it into their platform, they had to build an adapter. And this is simpler than you would

**[0:14:36]** think, thanks to ACP. So, we can look at the source code here for the adapter. They have an agent.ts TS just like the custom agent example that we saw a little bit ago. And clicking into this, a lot of the code is going to look very similar because basically all we have to

**[0:14:50]** do to connect cloud code to any editor through ACP is we need to convert any of our cloud code SDK messages into the format, the JSON format needed for the ACP standard. And so this function right here, it takes any cloud code message and based on the type, like if it's text

**[0:15:11]** or the model is thinking or it's using a tool to read a file, we're going to take the output of the cloud code SDK, like all the different values in these chunks, and we're going to transform that into the JSON object necessary for ACP. So it's really just a data change.

**[0:15:27]** We're just changing the format. That's all it takes. And so this integration, this full adapter for cloud code to zed thanks to ACP is only around 600 lines of code. It's so simple and we can take this beautiful notion of this standard here and apply it to other kinds of

**[0:15:45]** integrations. Like when I saw this, my mind just started running wild for the possibilities here with Archon in particular, my open-source project, which is the command center for AI coding assistance. And one of the things that we've always wanted to build into it is integrating it with different

**[0:15:59]** coding agents directly. And ACP is definitely our ticket for that. So I actually had Raasmus on my team. He did a proof of concept integrating Archon with ACP. So yeah, let's take a look at that right now. It's super super interesting. All right, so we just took a look at implementing custom agents

**[0:16:17]** into Zed through ACP. Now, the ability for us to do this kind of integration ourselves has just opened up the floodgate of ideas for me and Raasmus. So, I brought him in here to show a proof of concept that he did for Archon using ACP with Archon to connect it to

**[0:16:34]** Cloud Code and other coding assistants. And this is very much a PC at this point, but I just want to share with you some of the vision that we have here, some of the ways that we can uh implement Archon with these coding agents using ACP. We've always wanted to

**[0:16:49]** do something like what you're about to see, but ACP just makes it that much easier because it provides that standard for connecting applications like Archon and other code editors to our coding agents. So, Raasmus, thanks for being here and building out this proof of concept. Why don't you share some of

**[0:17:06]** your vision for connecting Archon to coding agents? Yeah, so yeah, thanks for having me again. And uh yeah, what you just said uh our vision has always been to like have Aron be able to invoke coding agents, not only cloud code but other agents like the Gemini CLI or the cursor

**[0:17:24]** agents or even Devon or any any of the coding agents really. And what ACP will allow us to do is to do that in one sweep. So if all of these uh other agents also adopt this protocol, we will be able to implement all of them very very easily and very very quickly as

**[0:17:41]** long as we have our base ACP implementation. So, what we have here right now is uh and yeah, I've been having a blast building this out with with Archon and uh here we have uh PC with cloud code, but we can just as easily use Gemini CLI because both of them works kind of out

**[0:18:00]** of the box with ACP and uh this is now directly integrated into Archon at this PC where you can basically connect your directory to to Archon. So the long-term vision here would be to kind of connect your git repository to Archon and you can attach your knowledge base to that git

**[0:18:21]** directory and you can attach your MCP servers to that git uh directory so that you can feed all of the context that you need to feed to your coding agent before you send your coding agent back uh into the background to do like a background task for you. So the agent will kind of

**[0:18:39]** spin up its own work tree, its own environment where it will can do whatever it wants and it will come back to you with a PR uh once it's ready. So basically you can just uh tell it where it should work. So I'll just give it a path to to one of my projects. I can

**[0:18:54]** start a coding session and I can see this uh uh interface here where I just have a chat. We have an active session and uh we can just send it a easy task. I'm just going to give it an example task here to create three different hello world files. One in uh Rust, one

**[0:19:11]** in Go, and one in Python. And uh let's just kick it off and see what it does. So we should see the this here what I have open is actually the HCP back end that is written in Rust. Uh and yeah, you can see here that it does it. It's

**[0:19:24]** actually spawns. You can see that it spawned three sub pages actually and did it in in one sweep. So yeah, that was quite an efficient uh task as well. I can actually open up the files here as well. And we can see that it all created this, it created this and this. So yeah,

**[0:19:40]** very simple example but uh quite powerful uh way of working with coding agents and I I believe personally that that's going to be the future way to work with with coding agents and archon is our interpretation or will be our interpretation of of the new interface for for coding.

**[0:19:58]** Exactly right. That is beautiful. Yeah. And like Razo said, this is just a proof of concept, not coming anytime soon to Archon necessarily. And this is a really basic example, but the power of this is we are not interacting with cloud code directly. We're not using the cloud code

**[0:20:11]** SDK, anything like that. It is all through ACP. That is how we're communicating here. And so it really would be a drop in replacement for any other agent like Gemini CLI that also supports ACP. That's the beauty of this. And another thing we can do in Archon is

**[0:20:26]** we can make it very easy to manage many agents in parallel. all using ACP. So, a user interface kind of like this, but being able to click into different agents as they're active working on longer running tasks. Something obviously much longer than the quick demo here. So, yeah, there's just so

**[0:20:42]** many ways that we can build this out with Archon. Yeah, exactly that. And imagine an interface here where you can actually select your agents. So you can like select cursor or you can select Gemini CLI or you can select codeex or whatever and you can uh send that off you know

**[0:20:56]** and you have a basically a chat that you can open or close you can inspect what it's doing or you can ignore it and at the end of the day it will come back to you with the with the PR anyways that you can review at the end. So this is

**[0:21:08]** really a way to to kick this off into the into the background and do the work for you. So very similar to what uh uh the codeex cloud is doing but that you the difference is that you can do it with any agent and you you do it locally

**[0:21:23]** on your own machine right yeah it's a beautiful thing so thank you Raasmus for showing us this working on the proof of concept the two big reasons I wanted to put this into the video here is one to show you some of the awesome plans we have for Archon

**[0:21:36]** that we've always had but ACP is going to make easier and then also I hope that this kind of can enlighten you even more on what ACP enables and why I really do think it is the future of AI coding. So, thanks for being here, Raasmus, and on

**[0:21:50]** to the rest of our video. So, I hope those ideas around archon really got your brain juices flowing. There's just so many ways that ACP really is the future of AI coding. And also, Raasmus has a video coming out on his channel that I'll link to in the description

**[0:22:04]** when it's available. Check that out if you want to dive even deeper into these ideas around archon and ACP. So yeah, that is all the content that I got for you right now on ACP. It's just an incredible technology, a standard that I'm definitely going to be following

**[0:22:18]** more and putting out some more content as we get more integrations with different code editors and coding assistants. So if you appreciate this video and you're looking forward to more things AI coding and AI agents, I would really appreciate a like and a subscribe. And with that, I will see you

**[0:22:32]** in the next
