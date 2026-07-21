---
type: raw-transcript
title: "I Built a Safer OpenClaw Alternative Using Claude Code"
youtube_id: XmweZ4fLkcI
url: https://www.youtube.com/watch?v=XmweZ4fLkcI
slug: i-built-a-safer-openclaw-alternative-using-claude-code
published: 2026-02-11
duration: "0:15:15"
fetched_at: 2026-07-21
immutable: true
---

## Transcript

**[0:00:00]** I have never seen a project blow up as much as OpenClaw. It is the personal AI assistant right now and people are loving it because it feels like the first agent that truly gets you. And over time, it builds up a memory of what you're working on and your preferences.

**[0:00:14]** And it is a fully open-source tool. And so this is the GitHub repository. They exploded up to 185,000 stars. I have not seen a repository on GitHub with this many stars. even beats out N8N now, which is just crazy to me. But it's no secret that there are a lot of security

**[0:00:33]** issues with OpenClaw, both because of how much control we're giving to the underlying agent and because of some issues with the codebase itself. So that plus wanting to build something more custom to me has inspired me to basically build my own version of OpenClaw. That's what I want to talk to

**[0:00:49]** you about today because it's easier than you would think to take the ideas that really make OpenClaw feel magical and build it for yourself. I was able to replicate everything that's powerful about OpenClaw in just a couple of days. Just took me a couple thousand lines of Python code and markdown. And so I'll

**[0:01:08]** talk about how I did it. You can do this yourself pretty easily. And honestly, I encourage you to do that. I think the balance we should strike here is we should learn from these powerful open- source assistants that are out in the wild, but build something ourself so we

**[0:01:23]** truly understand and control the solution and we can customize it to our liking. Now, there are already some open- source solutions that are a lightweight and secure version of OpenClaw like NanoClaw, but this just didn't check all the boxes that I want for my own personal assistant/secbrain. That's why I'm building my own. Now, I

**[0:01:41]** don't have a repo to share with you like OpenClaw, but I would kind of defeat the purpose of this video anyway. I'm trying to make a point here that you should build your own take inspiration from these other tools like OpenClaw. That's what I want to show you how to do right

**[0:01:54]** now. Now, I have already shared some of the skills that I have for my second brain. So, there's a video I did on my channel that I'll link to right here if you want to check that out. I will be sharing a lot more on my channel in the

**[0:02:05]** coming months as I continue to build out my assistant as well. So definitely stay tuned for that. So anyway, I want to really quickly cover some of the security issues with OpenClaw. Then we'll get into what are the beautiful parts of the tool. How can we take it

**[0:02:18]** for ourselves to build our own second brain? And so there are two primary lanes of security issues with OpenClaw. I'm going to focus first on some of the architecture issues with the codebase. Recently, there was a one-click remote code execution vulnerability that allows attackers to steal all of your data and

**[0:02:37]** keys from your OpenClaw instance. All they have to do is get you to click on a single malicious link, which it's pretty easy to get a lot of different people to click on malicious links. And then once they do that, then it's going to send an O token. Their OpenClaw will send an O

**[0:02:52]** token back to the attacker. They can use that to log into the victim's openclaw. And because all the credentials are just stored in plain text, they will now have access to all of the API keys and tokens for your platform adapters and other things that you've given your personal

**[0:03:06]** assistant access to. And then we also have the issue with Claw Hub. This is a marketplace that is publicly available where people are publishing skills that promise to extend the capabilities of OpenClaw. But research found that there are hundreds of malicious packages. And so it's this beautiful concept that

**[0:03:23]** people can share these ways to make open cloud more powerful, but in reality it falls apart because there are a ton out there where really they're just stealing your API keys, wallet private keys, SSH credentials, the list goes on because again everything is just stored in plain text where you are hosting OpenClaw. And

**[0:03:40]** also I've been doing a lot of research. So, I'll have links to all this in the description, by the way. But there was a researcher where it took him fewer than 2 hours to hijack an OpenClaw instance, get access to everything inside. Now, the one thing that I will say is that

**[0:03:55]** the creator of OpenClaw, Peter, he really is doing a good job keeping up with the security issues, adding new features to OpenClaw. And so, I do have hope that there is a good future for the tool. But even if you address all of these architecture problems like I'm

**[0:04:11]** speaking to, I do think that OpenClaw will still be a security nightmare as Cisco puts it and that's because of that second lane of security problems that I am talking about. There is this massive code base. Open Claw is pretty big. We don't understand it and we're just

**[0:04:27]** running it and trusting it. But it's giving so much power to our agents and that I think is just so dangerous. Most people are not ready for their agent to wield all the power that OpenClaw gives it. So that's why I'm a proponent of building your own solution because then

**[0:04:42]** you truly understand and control what your agent is doing and you can customize it to the exact level of control that you need for your agent. And so don't get me wrong, like Cisco says here, from a capability perspective, OpenClaw is groundbreaking. That's why I want to use it as a

**[0:04:57]** reference point for building the memory system and the proactive part of the agent. It's everything that personal AI assistant developers have wanted to achieve for literally years at this point, but it's just way too risky for me. And so that's why I want to take the good components from it and just use it

**[0:05:14]** as a resource. So that's what I want to cover with you right now. There are four components that make OpenClaw feel so magical and these are the things that I've replicated for myself. And I want to stay pretty high level here because I encourage you to go through this process

**[0:05:28]** yourself. And it is so so easy. And so within OpenCloud, we have the memory system, the heartbeat, that's the proactive nature of the agent, we have the channel adapters, and the skills registry. These are the four core components that work so incredibly well. And the best part about the memory

**[0:05:46]** system is it's elegant, but also extremely simple. The entire thing is markdown driven. We have the soul.md where the agent evolves its identity over time. It kind of evolves the identity of you and the user MD. The core memories are stored and maintained in the memory.mmd. We can also define

**[0:06:04]** the agents behavior and in agents.mmd. This is kind of like the global rules for your coding agents. And then we're keeping track of session logs every single day. And for better search over all of this, there's also a SQLite database with a very light implementation of rag built in as well.

**[0:06:22]** So again, super elegant but super simple. And then we have our heartbeat. So we're leveraging this heartbeat.md. This is a markdown document that tells OpenClaw whenever it runs autonomously on a scheduled basis, it should look there to see what can I do for Cole right now that he would appreciate. So,

**[0:06:40]** it does things for us without having to ask for it explicitly. And this is not a new concept. There are a lot of agents that have implemented this in the past, but OpenClaw for the first time feels like this agent that can do things for us that we truly appreciate. It's not

**[0:06:56]** just wasted work. And so you'll wake up in the morning and OpenClaw will give you this report like, "Okay, I drafted this email and I created this pull request in your GitHub repository." And time and time again, people are like, "Oh, wow. That's like really good. It legitimately did things that I would

**[0:07:11]** want it to do." And then next we have the channel adapters. This is what allows us to talk to OpenClaw in any platform that we want. WhatsApp, Telegram, Slack, Discord. The beauty of this is pretty much anything that we'd want to use is available out of the box.

**[0:07:26]** And we support threads with a lot of these platforms. And so we can have multiple conversations going with our OpenCloud instance at the exact same time. And then last but not least, we have the skills registry. So I know there are the security issues with it that I covered earlier. But the beauty

**[0:07:41]** of this is even with just a single file, we can add a new capability to open claw like here's how I want to build frontends, a guide for that. Here's how it can help me generate powerpoints. And then we can use that for ourselves very easily, but then also share it with

**[0:07:55]** other people. And so all of this together is what gives us this magical experience of feeling like we finally have an ultra personalized AI agent. It is able to remember our decisions, preferences, and context. It can check our services, do things for us before we even ask. We can talk to it from

**[0:08:12]** anywhere, and we can add any capability with a single file. So it can act on our behalf, anticipate our needs, and it knows us better every single day. And that's what I wanted to build for myself. And so I'll show you here how each of these features I have built it

**[0:08:27]** into my own second brain. Starting with the memory system. And take a look at this. The memory files that I have for my system is very similar to what is built into OpenClaw. And that is on purpose because what I did is I clone the repo locally. I took my coding agent

**[0:08:43]** which is claude code. I pointed it there and I said, "Look at how they built their memory system and I want you to build it for me adapted to my tech stack for my second brain." And it thrived on this example. Let me tell you, coding agents work really well when you give

**[0:08:57]** them good examples. So, if we're working on top of something that is simple and elegant and just works really well, that is the ultimate brain food for the context for the coding agent. And so, it oneshotted this whole thing for me and even adapted it to my codebase. It has

**[0:09:13]** the same rag strategy with SQLite. Markdown is the database. And I also added Obsidian for syncing because something that I want to make a video on on my channel soon. And let me know in the comments if you're interested in this is I took my second brain, I

**[0:09:26]** deployed it to a VPS, but I still want to have quick local searching when I'm using the Cloud Code CLI locally. And so I'm syncing my memory system. All these markdown documents, I'm storing it in Obsidian. And so my tech stack is Obsidian for storage, Markdown obviously for the memory system, SQLite for the

**[0:09:45]** database, and I'm using Postgress when I deploy it remotely, and then I'm using the Claude agent SDK for the proactive part of the agent that I'll talk about in a little bit. And so that's my way to run Cloud Code from my Python scripts. And then obviously Claude Code is my

**[0:10:00]** primary driver. I want to use this because then I can use my anthropic subscription. So, I'm not paying hundreds and thousands of dollars for API credits, which if you didn't know, people have been getting their anthropic subscriptions banned when they're using it with OpenCloud. It's against the Anthropic terms of service. But if we're

**[0:10:18]** using Cloud Code and the Claude Asian SDK ourself directly and we're doing it just in our own environment, then it's totally allowed even if you deploy it to a VPS. And so, it's very cost-effective to build your own second brain as well. And then for the heartbeat, it follows a

**[0:10:34]** very similar pattern. All right, Claude, look at how the heartbeat was implemented in OpenClaw. Let's build it oursself with our own integrations. And so I'm using the Claude agent SDK. It's a scheduled job that runs every 30 minutes for me right now. And we send a prompt into the Cloud Agent SDK. So I'm

**[0:10:49]** using Cloud Code directly from my Python script. And I'm telling it to look at my memory, look at recent emails I've gotten, things that are scheduled on my calendar, my tasks in a sauna, and then give me notifications for anything that need my attention. And then something I'm still working on is more of the

**[0:11:04]** proactive piece where it will even build things for me or draft emails on my behalf. And so we can take this as far as we want because we have all of Claude code, but just wrapped up in a script that we're invoking every 30 minutes. So it makes it feel like the agent is

**[0:11:18]** constantly alive thinking about how it can do stuff for us. And then for my adapters, I have a very simple version of what OpenClaw has built. One of the things that I don't like about OpenClaw is it's really cool how many adapters we have, but most of the time you're just

**[0:11:34]** going to find one that works for you and that's all you really need. And that's what I found for myself. I really like talking to my second brain in Slack. I'll even show you. I have that pulled up right now. I mean, it looks a little silly cuz I got deleted messages and

**[0:11:46]** things. I'm still working on testing my whole second brain, but I can talk to it in Slack from anywhere. It's super cool. And that's really all I need. I don't really need Discord and Telegram. I just have the one platform that works for me. So, I have this as my adapter and then

**[0:11:59]** the terminal for when I'm using Cloud Code on my desktop or laptop. That is all I need for my adapters. But I still did have it copy the architecture of OpenClaw. So, it's really easy to just with cloud code or whatever coding agent, I can just oneshot another

**[0:12:12]** adapter if I ever wanted to use something like Discord or Microsoft Teams. And then finally, for the skills here, since I'm using the Cloud Agents SDK and Cloud Code, they both have the idea of skills just built right in. So whenever I want to give more instructions kind of like the skills

**[0:12:28]** registry for how to do something for me like uh generate the Excal diagram like literally the one you're looking at right here was built by my second brain or ideate for content help me create YouTube scripts I just need to create a skill and so one of the skills I have in

**[0:12:42]** my second brain is a skill on how to create more skills and so it's very easy for me to evolve the capabilities of my second brain just by having a conversation with it and yeah there's no public registry here so I'm not able to share my skills at least yet. I'm

**[0:12:57]** working on that, but it's a lot more secure because then I'm not downloading potentially malicious skills. I'm just building everything myself and it's really easy to do so. And so I'm getting the ultra personalized agent using OpenClaw to build things very, very quickly. And if there's ever an update

**[0:13:13]** to OpenClaw where it adds this new thing that's absolutely incredible, well then I'm just going to pull the changes from the repository, point my cloud code to it again, and say, "Hey, they just added this thing. Let's go ahead and build it oursel. Now, of course, you don't have

**[0:13:26]** to copy my exact tech stack, but it is working really, really well for me, and I do plan on putting out some more content soon, covering more in detail how I built this out and sharing some resources for you. But just overall, you have to follow this super simple

**[0:13:42]** process. So, just as a quick review, you clone the OpenCloud repo locally and it's MIT licensed. You can do anything you want with the code. Then you point your coding agent at it, say, "Hey, explain how the memory system works." now build that into my own system. You

**[0:13:55]** can specify any customizations that you want as well to make it even better than OpenClaw for you specifically. And then you just repeat that for every part of the platform that you want for yourself. It is that easy. I mean, it kind of feels like I'm just saying something

**[0:14:08]** really obvious here, but I really haven't seen people do this and it just works so well for me that I have to share it with you because this is making a real difference for me. I like OpenClaw. I did some experimentation hosting it for myself when it first came

**[0:14:22]** out, but I'm really really getting a lot out of what I'm building for myself and I feel like it's just going to get better and better for me over time. Not because I'm engineering something better than Peter with OpenClaw, but because I know exactly what I want and I can build

**[0:14:37]** for that and I think that will resonate with you as well. So again, I will have a lot more content on my channel for my second brain coming up soon. And I'm doing a lot of workshops in the Dynamus community as well, going a lot deeper into this stuff. So, I'll have a link in

**[0:14:51]** the description to Dynamus if you want to check it out. It's my community where I do weekly workshops. I have courses on building agents and using AI coding assistants. And I've got a lot of resources coming for building your own second brain. And so, if you appreciate this video and you're looking forward to

**[0:15:05]** more things on second brain content and agentic engineering, I would really appreciate a like and a subscribe. And with that, I will see you in the next
