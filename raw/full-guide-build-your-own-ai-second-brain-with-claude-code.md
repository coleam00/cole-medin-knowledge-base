---
type: raw-transcript
title: "Full Guide - Build Your Own AI Second Brain with Claude Code"
youtube_id: 1FiER-40zng
url: https://www.youtube.com/watch?v=1FiER-40zng
slug: full-guide-build-your-own-ai-second-brain-with-claude-code
published: 2026-04-01
duration: "0:25:05"
fetched_at: 2026-07-21
immutable: true
---

## Transcript

**[0:00:00]** I've been building my second brain with Claude code for the last 3 months and it's gotten to the point where it saves me at least a dozen hours of work and I promise you I'm not exaggerating for the sake of this video. So right now, I want to show you all of the components of my

**[0:00:16]** second brain, talk about the skills and the use cases, the things that I'm automating. I've been running a very similar business for the last year and a half and so I know how long it takes for me to do a lot of these things that I've started to automate with the help of my

**[0:00:31]** second brain and there is a stark contrast for a lot of parts of the business with how long it took back then and how long it takes now. So I don't use my second brain to work less, but it takes things off my plate so I can move

**[0:00:45]** my business forward faster, focusing more on the high-leverage tasks. That's the main goal of building a second brain is to release some of your capacity so you can dedicate it to things that matter more. So I'm here in my Slack, which is one of the places where to my

**[0:01:01]** second brain just like I would a friend or co-worker. So a lot of examples here are things I do with my second brain. I have it help me ideate for my content, creating YouTube scripts based on my tone of voice and my content calendar, managing my inbox, helping me research

**[0:01:16]** and keep up with all the craziness in the AI industry right now, but also specific to my interests. It even helps me with image generation and diagram generation, like creating thumbnails, managing my habits to keep me on track every single day with the things I want to accomplish. I use my second brain to

**[0:01:32]** help me ideate, research and keep my business and my entire life very organized. And my second brain, which I built on top of Claude code and Obsidian, has been the biggest deal for my business since I started using Claude code itself. And the best part about this entire architecture, which I'll

**[0:01:50]** cover with you, is that everything compounds on itself. As you use your second brain more and more, it becomes more in tune with you, anticipating your needs. It builds up examples of how you communicate and work that it references later. The entire application evolves over time and you build this entire

**[0:02:06]** knowledge base. That's why I integrate with Obsidian because it's where I store all of my knowledge and have my agent evolve it over time. Every single document that you see here in my Obsidian graph is a part of my second brain. It builds up an index over time

**[0:02:20]** of all of my emails, all of my announcements and YouTube scripts. It literally is a brain that is expanding over time as I use it. All right, so here's what we're going to go through today. First, I'm going to address the elephant in the room. Why build your own

**[0:02:34]** AI second brain in the first place when we have things like Openclaw out there? Then we'll get into the architecture. I'll show you exactly what goes into each one of the components here, how we build in skills and use cases for our second brain, how we make it evolve

**[0:02:47]** itself over time. And then once you understand the core architecture of the second brain, then we're going to get into something special that I have for you here. This is a GitHub repo that I'll link to in the description. We're going to go through this Claude code skill that will walk you through

**[0:03:02]** creating your PRD for your second brain. So I'm not giving away all the code for my second brain, but the point is for you to build your own in the first place and this is how you start. And so at the end of the video, I'll go through this

**[0:03:13]** live with you, creating that document that outlines the full scope of work to create your second brain in phases to break it down nice and simple for you. All right, so I'm going to dive right into answering the big question here. Why do we care about building our own

**[0:03:26]** second brain when we can just run Openclaw? And so to start, I need to explain to you the lethal trifecta. And this is actually really important to understand just for agents in general. So the idea behind the lethal trifecta is we have a huge uptick in concern for

**[0:03:42]** our AI agent if all three of the criteria are met because this means that our agent is going to be very susceptible to security risks like prompt injection. You've probably heard about that a lot if you've set up Openclaw and done research on it yourself. And so we have private data

**[0:03:58]** access, untrusted content and an exfiltration vector. Let me explain each of the three of these really quick. They're super important. So first of all, we have private data access. If your agent has access to something like an email or calendar, that is step number one for the trifecta and for our

**[0:04:14]** second brains, this always applies. Otherwise, it wouldn't really be that helpful to us. And then the second pillar here is untrusted content. If there's any kind of input that can come into our AI agent that isn't from us, things like incoming emails or even web page content, all of those could

**[0:04:32]** theoretically contain malicious instructions for a prompt injection attack. And then last but not least, we have the exfiltration vector. It doesn't really matter if your agent can access private info and receive incoming information if there's no way to send your sensitive data out to the malicious attacker, your agent is going to be a

**[0:04:52]** lot harder to compromise. However, for our second brains, yeah, it's always going to have the ability to send a message or post to an API endpoint. We're giving so much power to our tools, especially something like Openclaw like I'll talk about in a second here. And so the argument with the lethal

**[0:05:08]** trifecta is really all three of these need to be in place. Like if there's a way to send sensitive information to a malicious user and then access our private information. But there isn't really a way to receive a prompt injection attack. Like we can't receive any other inputs, then there's

**[0:05:26]** not really a risk here. Like if only these two things apply, there's a lot less of a security concern. Or if there is untrusted content coming in and we do have an exfiltration vector, but there's no private information for the agent to access, then again, the risk for our

**[0:05:40]** agent goes down significantly. But like I already said, all three of these are always going to apply to our second brains. They have all three by default. It's really hard to make a useful second brain without being exposed to the lethal trifecta. Okay, so cool. What's the point you're

**[0:05:57]** trying to make here? Well, hear me out on this. If we are really forced to be exposed to the lethal trifecta with our second brain cuz that's the only way that it's useful, then what it means is we have to be very careful about our implementation cuz we want to limit each

**[0:06:11]** one of these pillars as much as possible. And honestly, Openclaw and other solutions that are already out there, they don't do a very good job limiting especially the private data access and the exfiltration vectors. They've been doing like Openclaw's been doing a lot of work recently on handling

**[0:06:27]** prompt injection attacks and I have to hand it to them. Some of the security risks and other things that were a big deal at first have been addressed. And so Openclaw is something that is constantly evolving, but there still are a lot of security issues and the main

**[0:06:41]** problem, even outside of the, you know, issues in the code base itself, is that it is a massive code base that you don't understand. You're running something that it's hard for you to adjust yourself. It's hard for you to understand. You're giving so much control to an AI agent and you don't

**[0:06:58]** really know in what ways you're actually giving control. Like you don't have understanding of how the lethal trifecta is really affecting you. And so when you build your own, you actually get to control what you build. You define the permissions up front. You create the foundation so you get to layer on the

**[0:07:14]** capabilities as you evolve your second brain versus just running something that works and does way too much out of the box right away. And yes, it does mean that it is more work for us to create our own second brain and not just use something out of the box. But in the

**[0:07:28]** end, you're going to create something that is customized to exactly what you need and it's going to be a lot simpler, following the classic advice we've always had for building AI agents. You just want to work with simple composable patterns. And yeah, for a lot of the second brain that I'll show you here,

**[0:07:44]** it's just Claude code with skills that drives most of the capability here. It's a beautiful thing. And then for a lot of the rest of the architecture that I'll cover with you in just a second here, the beautiful thing here is we're not just building it from scratch. As much

**[0:07:59]** as I just dissed Openclaw for being a security risk, it is a beautifully crafted application. Like don't get me wrong, Openclaw is very impressive and there's a reason that it really took the internet by storm. And so we're not going to ignore it, but we're also not going to run it directly. Instead, what

**[0:08:17]** we're going to do is take inspiration from Openclaw. So literally as I built my second brain on top of Claude code, I pointed it to the Openclaw GitHub repository cuz it's fully open source and I said, "Look here and see how they implement the memory layer with the

**[0:08:32]** soul.md and the user.md. I want you to see how they implement the heartbeat for the proactive part of the agent." And it took a lot of inspiration from that code base and brought the things that I liked about it into my own version, but I still get to maintain control and build

**[0:08:46]** up the exact permissions and capabilities I'm giving to my agent over time. That is the big unlock here. So we build it ourselves, but we take inspiration from what's already out there so that we can stand on the shoulder of giants. So with that, let's actually get into the architecture now.

**[0:09:01]** I'll show you at a high level how I built each one of these components. Now, it would take a very long time to build the entire thing from scratch with you. That's also why I have the template as a starting point. But if you do want to see me build this entire second brain

**[0:09:15]** from scratch, I'm running a special 4-hour workshop in the Dynamis community this Friday, April 3rd at 11:00 a.m. Central Time where I will take this starter template that I'm showing you right now and show you what it looks like to build everything live, taking inspiration from solutions like

**[0:09:31]** Openclaw. So by the end of it, you'll have your own working second brain with everything I'm about to cover with you. So check that out if you are interested. Otherwise, let's go ahead and get right into the architecture here. So the first big thing that I took inspiration from

**[0:09:45]** with Openclaw is the memory layer. So if you've seen Openclaw before, you'll recognize some of these files like the soul.md, the user.md, the memory.md. That architecture is genius and it's so simple. As part of the power of our second brain is that we're managing things with just markdown documents,

**[0:10:03]** which is also why Obsidian is such a powerful tool to use alongside Claude Code for your second brain. So, I talk to my brain with Claude Code, but then Obsidian is my canvas to view things like the diagrams that it generates for me like we're looking at right here, all

**[0:10:20]** of my different documents, so I can like load up the user.md like we're looking at right here. So, as it evolves this over time, I can watch this and even, you know, correct some things that I need to. And so, within my memory folder that I have right here in my Obsidian

**[0:10:34]** vault, I have everything that we're going to get into here. Actually, quite a few things. I manage my entire life with my second brain now. So, we have the user.md that I just showed you, the memory.md, so keeping track of all my key decisions that I'm making every

**[0:10:47]** single day. Like these are some of the key decisions that I made as I was first building my custom second brain. And then we have the soul.md, so this is the personality that I give to my second brain. And again, just taking this directly from Open Claw cuz I love this

**[0:11:01]** approach. There's no security issues with this part of Open Claw, so I'm just leaning right into it. And all of these core files that we have in our memory layer inspired by Open Claw, we're bringing them right into the context of our Claude Code up front through a session start hook. So, we

**[0:11:18]** automatically load the soul, user, and memory.mds into the context of our Claude Code. And hooks are actually a pretty important part of our Claude Code second brain beyond this as well because we also have a pre-compact hook. So, whenever our conversation is getting really, really long, we have to do a

**[0:11:35]** memory compaction or move on to another conversation, we need to make sure that we save this conversation to our daily log because we want our second brain to learn from every single conversation. So, we build up this quite long daily log every single day. And then we have

**[0:11:52]** this daily reflection process. So, this happens through just a cron job. I run this once a day. This uses the Claude Agent SDK under the hood, and it just goes through this promotion process cuz we have this super long raw daily log from all of our conversations. We have

**[0:12:07]** to figure out what do we care about remembering all of the time, right? Like what should we promote to the memory.md file that is always loaded into the context of our Claude Code. So, it extracts things like key decisions, lessons learned, important facts. This is one of the most important parts that

**[0:12:24]** of our system that allows our agent to evolve over time. And then we do the same thing whenever we end a conversation as well. I mean, especially cuz we aren't always compacting, right? Whenever we end a Claude Code session, we have the hook here that does the same thing. So, daily

**[0:12:39]** log is where we dump everything, and then we do our promotion process to, you know, this core file. This is probably the most important file for the entire second brain. And then another important thing here is the memory.md because it is a more concise version of our daily

**[0:12:54]** logs, it doesn't always have all the information we'd want to search back through. And so, we also do allow our agent to perform rag. So, we index all of our daily logs into a SQLite database, and you could do Postgres as well, doesn't really matter, but we index it there so our agent can search

**[0:13:11]** through all of the daily logs. If we want to find something really specific that might not have been quite important enough to make its way into the memory.md, but we still might want to reference that in a later conversation. So, when our agent performs rag, it has access to all of the documents that you

**[0:13:27]** see here in the Obsidian graph view, everything in our daily logs folder. I mean, take a look at this. I have a file for every single day since I've been running my second brain. Okay, so I started with the memory layer because it really is the core part of our second

**[0:13:42]** brain. But we also need to give arms to our second brain. They need to be able to do things on our behalf, and that is where skills come in. And Claude Code plus skills is all we need for our capabilities. Again, going back to our other diagram here, we want to focus on

**[0:13:59]** simple composable patterns. That's how you want to build agents all of the time, and that's all we need. We don't need other applications running to our second brain. We don't even need MCP servers. I literally use my skills for everything. And so, I'll show you inside the belly of the beast right here. This

**[0:14:13]** is my repo for my own second brain. It's pretty messy cuz this is where I do my work every single day. But if we look in the .claude/skills directory, take a look at this. There are so many skills that I'm using. I'm using all of these at least on a weekly basis. I've covered

**[0:14:27]** a lot of them on my channel before like the Excalidraw diagram skill. Link to the video for that right here. I love using this all of the time to generate diagrams like the one that you're looking at right here. And the thing is, for the Excalidraw diagram skill, all of

**[0:14:42]** the skills that I have for generating PowerPoints and helping me create YouTube scripts, like all of these, the memory layer is powering them, right? Like the skill is going to create a very generic diagram or a very generic YouTube script unless it is able to access the memory here, understanding

**[0:14:58]** how I've scripted similar videos in the past or just like going back to my memory.md or my user.md. So, the skills are made very specific to me through, you know, some of the prompting in the skill itself, but especially because every single conversation, the memory is powering all the capabilities that I

**[0:15:14]** leverage through my skills. And then one of the core skills that I have for my second brain is one that explains all of my direct integrations and exactly how to use the APIs that I've set up for to work with my services like Gmail, Asana, Circle where I have my Dynamis AI

**[0:15:31]** community, Slack. Wherever I am doing work, my second brain has access to it as well. And I have a skill that explains all the capabilities that it has right here. Now, the important thing that makes this different than what you would have with Open Claw by default is

**[0:15:46]** I'm very careful through my Python API layer the different capabilities that I give it access to through these different APIs. And so, it can only read my Slack. It can't actually post messages. It can't create things in Google Docs. It can't manage my calendar, but it can tell me events that

**[0:16:04]** I have. But sometimes where necessary, I do give it right access. Like it can create Gmail drafts, it just can't send emails. I can have it manage Asana tasks, but only in certain projects. And so, because this is my own second brain, I have full control. I can [snorts] be

**[0:16:18]** very, very nitpicky about the permissions that I'm actually giving it, and I can evolve it over time if I want, but I'm starting with sort of like a zero-trust mindset. Like let's start with just read-only, and then add in capabilities and be very controlled about that. And for all of my direct

**[0:16:34]** integrations, I've implemented them with a very common pattern. And what that means is I can have my second brain evolve itself creating new integrations by just one-shotting them with Claude Code. It is so easy because it can reference existing integrations and its memory of how it's built things in the

**[0:16:50]** past to basically do the whole planning part of the AI coding workflow itself. And that's also how I built my chat interface. So, Slack is created in a way where I could just copy this for any other platform I want to integrate like Telegram or Discord. And so, being able

**[0:17:06]** to have your second brain reference itself as well as other solutions like Open Claw just means that it's very It's just incredibly easy to build on top of your second brain. All right, so the last thing that I want to cover with my second brain before I get into the

**[0:17:21]** template for you is the heartbeat. And this really brings everything together because it's where we build the proactive nature of our second brain. It can start to anticipate our needs and do things on our behalf that we want it to without us having to even ask it. And

**[0:17:36]** so, we have all of these direct integrations with these services like Gmail and my my task management, but I don't always want to be the one to prompt it to do things for me. Like what if I wanted to automatically draft replies to a bunch of my emails? That's

**[0:17:51]** where the heartbeat comes in. So, it's going to gather information through all of the APIs with the direct integrations. So, we have this deterministic part before we even go into Claude Code where we're gathering a context around my life that's happening right now. And then we send all of that

**[0:18:08]** pertinent information into Claude Code. So, we're using the Agent SDK because we're invoking Claude Code programmatically. I'm not prompting it myself. So, I have a preconfigured prompt where it's that plus all of the information from the APIs that's sent into Claude Code so it can reason about like, "Okay, let me draft these replies.

**[0:18:25]** Let me handle this pull request in GitHub. Like what do I need to help code with right now?" It thinks about all that. It acts on that. And then it sends a notification to me in Slack to keep me in the loop for everything that I got going on in my life and the ways that

**[0:18:36]** it's helping me proactively. And so, I do have to blur a lot of this here because it's pretty sensitive information, but just showing you an example of what it looks like for my second brain to be sending me these alerts. And then if I want to, I can

**[0:18:47]** always reply to one of these in a thread in Slack to continue the conversation for something that it did for me. So, this is just a starting point, but it is a beautiful starting point. The heartbeat is the thing that saves me the most time out of everything in the

**[0:19:00]** second brain. All right, so now that you know how my second brain works, I want to help you build it. Now, like I said at the start of the video, I'm not just going to give my entire code base away cuz it also defeats the purpose of you building your

**[0:19:15]** own. Otherwise, I'm just going to be building another Open Claw. I want you to create the foundation for yourself, but still give you a starting point. And I thought long and hard about how to do that. How do I help you scope out the work without giving you a template and

**[0:19:29]** just another Open Claw? And so, what I've come up with here is a system. So, I have this requirements document that you can fill out, and then you can feed this in as context to your coding agent to create the PRD. This is your initial scope of work. It'll have all the phases

**[0:19:44]** to build everything in the second brain that I've gone over with you. And everything that you're looking at right here is in the GitHub repo that I'll link to in the description. So, you just clone the repository, find this my second brain requirements markdown document, and then you can edit

**[0:19:58]** everything here. So, you fill in all the blanks to describe exactly what you want your second brain to help you with, the level of permission and proactivity that you want. And then once you have this filled out, then you open your Claude code or code extra open coder whatever,

**[0:20:12]** and you run this skill, the create second brain PRD. You just have to give the path to your filled in requirements. So, right click, copy relative path, paste it in, and then boom, that is all you have to do. And I'll show you a live example of this in just a second here.

**[0:20:25]** But this will produce a requirements document that has all of the phases to build out everything that I've covered with you with my second brain. And so you're using what I built as a starting point, but because it's a PRD and not a code base, it's very easy to edit

**[0:20:39]** everything. tweak it to your heart's content to really customize it to you before you actually write a single line of code. And to make this even easier for you, I have an example of the requirements that's already filled out that you can use as a reference if you'd

**[0:20:52]** like. And this is what I'm going to show you right now. So, I just made up a random person here. You just share some information about you so it knows your name and your time zone and things like that. You check off the platforms that you want your second brain to integrate

**[0:21:04]** with. So, wherever you do your work, you want your second brain to live as well. And then listing out all the tasks that you want it to do. I even have examples for every part of the template for you to work off of. And then add in whatever

**[0:21:15]** you want. The proactivity level is also very important. So, it's whatever you're comfortable with. Do you want your agent to be an observer so that it's really just read only actions on everything? Or maybe you want to go so far as it's a partner. It can act autonomously even

**[0:21:29]** sending emails on your behalf. You can pick your level. Generally what I do is the advisor. That's what my second brain is. And then for security boundaries, like what do you want your agent to never do? We want to have a big emphasis on security for our planning and our

**[0:21:43]** implementation. Memory categories, what types of knowledge we want it to track and maintain and search through over time. The infrastructure, so where do we want to deploy this? Like maybe you want your second brain only ever running on your computer. Other times you might want it running remotely so it's

**[0:21:57]** accessible 24/7. So, hosted in some kind of droplet like in Digital Ocean or Hostinger, and then you can access it from Slack remotely. I have that set up as well. And then just uh laying out your priorities for integrations cuz that'll determine exactly how it creates the phases in the PRD. So, you fill in

**[0:22:14]** everything just like I've done here. And then I'll actually do this right now. I'll do {slash} create second brain PRD. I'll pass the path to this example here. And it's going to take a while cuz it's going to do a lot of research. It's going to take into account all the

**[0:22:27]** customizations that you want to specify. This is also where you could point it to a repository like open claw and say, "I want to take inspiration for how open claw did this or how Nemo claw did this." So, there's a lot of resources out there already that you can feed in

**[0:22:42]** to your coding agent. That's the beauty of using a coding agent here is you can customize things as much as you want. So, I'll come back once I have the PRD created. I'll show you what that looks like too. And there we go. Our PRD is created. So,

**[0:22:54]** it outputs to the dot agents plans folder by default. Doesn't really matter where this is, but the important thing is that each of the phases that we have laid out in this PRD maps to everything that I've shown you in this diagram. And it's put in an order where we can build

**[0:23:09]** them one at a time. So, you can start by creating the memory foundation and you'll already have at least a part of a second brain that's pretty useful. And then you'll build in the hooks for context persistence and loading them into your sessions. You'll go on to building the memory search and then

**[0:23:23]** start getting into your integrations and the skills and adding in capabilities. You build it over time. We don't want to have our coding agent try to build your entire second brain in one shot. That is not going to work and it's going to be really hard to stay in the driver's seat

**[0:23:36]** of exactly what you're building in. So, that's why we do it in phases. And so, literally what you can do at this point, once you have your PRD, is you can go into a brand new Claude code session. You can point it to the PRD. Like I'll just copy this path, paste it in here,

**[0:23:50]** and say, "Let's build phase one." Right? Or if you have already built the first few phases, you can say, "Let's build phase four." And then you can kick off a planning session, figure out exactly what you want to build, if you want to tweak anything from the PRD. You go in,

**[0:24:03]** you create the code, you test it, and you can create your entire second brain this way in just a couple of days. It doesn't take long to get to the point where you have something as powerful as open claw, but it's entirely your own and it's a lot simpler to maintain and

**[0:24:18]** more secure. And so I would encourage you to try it out. I have the template and this diagram both in the GitHub repo linked in the description. Even if you already have a second brain, go through this process to get some inspiration to evolve what you already have. And

**[0:24:32]** remember, come and join Dynamis to be a part of the four-hour second brain workshop happening this Friday, April 3rd. I'm going to be building the entire thing from scratch, walking through it all in a lot more detail. So, I hope to see you there. And I hope that this

**[0:24:46]** video was a good starting point for you, even just showing you what goes into a powerful second brain that can save you hours and hours every single week. And so, if you appreciated this video and you're looking forward to more things on building agents and second brains, I

**[0:24:58]** would really appreciate a like and a subscribe. And with that, I will see you in the next video.
