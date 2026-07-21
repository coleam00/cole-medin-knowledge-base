---
type: raw-transcript
title: "FULL Guide to Becoming a Principled Agentic Engineer (Build Anything with AI)"
youtube_id: luBkbzjo-TA
url: https://www.youtube.com/watch?v=luBkbzjo-TA
slug: full-guide-to-becoming-a-principled-agentic-engineer-build-anything-with-ai
published: 2026-04-29
duration: "1:06:59"
fetched_at: 2026-07-21
immutable: true
---

## Transcript

**[0:00:00]** What I have for you today is a polished up version of a super valuepacked live workshop that I just did yesterday. I hosted the AI transformation workshop with Leor Weinstein. He's a big name in the AI space. It was a blast. And so what you're about to see is my portion

**[0:00:17]** of the event teaching you in very simple terms how to build a foundational system for getting reliable and repeatable results with AI coding assistance. And this is important right now because people, they overengineer and over complicate AI coding frameworks all of the time, making it seem like you need

**[0:00:35]** some fancy harness or specialized agents just to do any real work at scale. But that really isn't the case. So I boil things down into the core principles for AI coding here in three phases. Teaching you how to ideulate with coding agents, how to build an iterative loop, and then

**[0:00:52]** how to evolve your coding agents over time. A lot of this I've covered on my channel, but never in one place. There's a reason this workshop is one hour. It's super valuep packed and you if you go through this entire thing, you come out of it with a full system that you have

**[0:01:06]** real ownership of. And the best part is it's not even that complicated. And so without further ado, here is the live workshop. Our job as an engineer is to no longer write the code, but to do the higher leverage tasks like the planning and validating. And that's the framework

**[0:01:23]** that I want to cover here. And um also for product managers in the room, there's a lot that I have to say that applies to you guys as well. There's a threepart process that I want to walk through with you right now. We're going to start with how do we ideulate around

**[0:01:39]** the work that we want our coding agents to do for us for building literally anything, a website, uh funnel, uh any kind of platform. This is going to apply no matter what you want to build. And then we'll get into for the developer when we are knocking out a piece of work

**[0:01:54]** like a ticket in Jira or handling a GitHub issue or starting a new application. What does that process look like? It's using the piv loop. That's my core methodology that we'll cover. And then we'll get into the system evolution mindset. And this is probably the most powerful part of the entire system. How

**[0:02:10]** we make our coding agents more powerful over time as we run into issues using them. And uh one disclaimer that I want to give before we get into everything here is that uh a lot of what I'm covering here is a training that I do for organizations. But usually for them

**[0:02:29]** it's more of a 4hour session where I really get into the entire process. And so I've compacted everything down into one hour to share with you guys right now. So a highle overview, but I'm still going to get really practical with you guys. And I'm going to give you a live

**[0:02:43]** demonstration of everything here so that you can come out of this one hour knowing exactly what the process looks like that you can mold for yourself to go from idea all the way to production code with the help of AI coding assistance. And the important thing here is we're not vibe coding because we are

**[0:02:59]** putting ourselves in the driver's seat along the way through all of the planning and validation that we do. That is the the core framework that I'm going to cover with you. And uh really this whole process it applies no matter the tools that you're using. And so I'm

**[0:03:15]** going to be using cloud code for our event here just because that is my favorite AI coding assistant at least right now. And then I'm going to be using Jira as my place to manage all of the work that we scope out with the help of Claude code. But this entire process

**[0:03:30]** is going to work if you're using you know codeex with GitHub or you're using GitHub copilot with linear. Really, it's just you need to have one place to manage your work and organize your work and then one place to work with a large language model to create your code.

**[0:03:45]** That's the only requirement that I have here, even if you do want to follow along. And also in the description for our live stream here, if you click into the description, I'm just like looking at it on my left monitor here, I have a link to a GitHub repository. And uh this

**[0:04:02]** GitHub repository has the demonstration application that we're going to be building on top of today. And then it also has all of the resources that I'm going to be showcasing here. My rules, my commands, my skills. We'll talk about what those look like and I'll use some of them live, but a lot of that lives

**[0:04:20]** here in thecloud folder. So if you see any part of my process that you really want to steal for yourself, please feel free to do so. This repository is open source, ready for you to come in and take any of the skills or all the commands that I'm using to package up my

**[0:04:34]** workflows. And so really, we're not going to be doing a lot of manually typing today because it's going to be here are the prompts that I've been using time and time again. I have it as a command that I can reference and have the coding agent go through that

**[0:04:47]** procedure that I'm using pretty much every single time that I'm delegating the coding to AI. So yeah, the last thing I want to say before we get into things here is there are a lot of frameworks for AI coding available to us that are open- source. So maybe you guys

**[0:05:01]** have explored GitHub specit or BMAD or Cloudflow or GSD, um, Gastown. I mean, I could go on naming dozens and dozens of them. There are all of these opinionated strategies out there right now to guide you through a process kind of similar to what I'm going to show you here. Like

**[0:05:19]** this is a process for researching then planning then building then validating with AI coding assistance driving a lot of it and I have a lot of respect for these platforms. There are a lot of really powerful timeless software engineering strategies built into them but at the same time a lot of these

**[0:05:36]** frameworks are very overengineered. They try to do too much at once and it's really difficult to take an existing off-the-shelf framework and mold it to your software development life cycle. So like I said, I do a lot of corporate trainings where I teach companies how to take something very foundational like

**[0:05:57]** this and mold it to their existing practice because you don't want to just throw out the window the entire process your team has already been using for working with coding agents. Instead, you want to mold the process around AI, but you still are going to have some of your

**[0:06:12]** conventions and the way that the team works. It's not really realistic to just throw everything out the window. But when you're using something like BMAD or GSD, you're trying to take an offtheshelf solution, you're kind of forced to do that because it's so bloated that it's hard to like really

**[0:06:26]** make it your own. And so what I teach here is simple on purpose because I want to show you the foundation that you can then build on top of to mold it into your process for planning, your process for QA, whatever that looks like for each stage of the software development

**[0:06:41]** life cycle. And so we'll start with planning here. And planning, this part actually applies to product managers just as much as developers. So a lot of organizations that I work with um the trainings that I do, they'll bring their entire uh PM team into the training as well because they're actually the first

**[0:07:00]** ones that have a touch point with the coding agent when you're planning the next scope of work for an application. So the product manager is the one initially doing you know let's say the sprint planning and it's important for them just like the developers to work with coding agents to speed up that

**[0:07:15]** process. Here's the application that we have right now. here are the bugs we want to fix and the issues that we want to build or the new features we want to build for this sprint. And same thing applies to green field development. You're going to be building that initial

**[0:07:28]** scope of work for the MVP of an application. And this process applies to both. And so what I'm going to do with you guys right now is uh I am going to show this diagram at a high level. Just walk through it really quickly with you this component right here. And then

**[0:07:44]** we're going to get into something very practical. I'm going to go into my uh codebase here and we are going to go through everything live. I'm going to show you what it looks like for brownfield development to take an existing application, plan out a brand new sprint with a bunch of new set sets

**[0:08:03]** of work we want to perform. And then I'm going to pick one of those and we're going to go through the piv loop, the process that we're going to repeat for every single Jira ticket. And again, that could be a GitHub issue, it could be a linear ticket, whatever it is. And

**[0:08:17]** so, you'll see the full process end to end. There's a lot of value that I have packed into the hour for you guys here. So, okay, the beginning of the process here is as simple as it possibly can be. You are going to open up your coding agent, like I'll, you know, just pop

**[0:08:32]** open Claude Code right here. And you're just going to have a conversation about what you want to build. There is no structure at first. And like I said earlier, it is simple on purpose because I want the barrier to entry for you to be so incredibly low that you begin just

**[0:08:48]** brainstorming ideas with the coding agent. And then we're going to evolve to more structure over time. And that's the process that I'm going to share with you as I start to bring in some skills and commands that I have in my AI layer in my AI coding system.

**[0:09:03]** And so, um, first of all, when you have this conversation, you just do what I like to call a brain dump. Like most of the time I'll literally I'll just use a speechtoext tool so that I just talk. I go on and on about what I want to build.

**[0:09:16]** At this point it is helpful to be as specific as possible. And so you would say, you know, like this is my application. Here are the new things that I want to build. Here are the bugs I want to fix. And then you go into the clarifying stage. And so the most

**[0:09:29]** important part when you're first planning work with a coding agent is to reduce the number of assumptions that it is making. Because honestly, most of the time when a coding agent does a bad job, it's not like the code is just broken. It's that it's not aligned with what you

**[0:09:44]** are actually looking to build. And really, the responsibility is on you there because it is your role to and and your responsibility to make sure the coding agent is really on the same page with you for what you are building. So, it's a lot of just curating this context

**[0:09:59]** with the help of the coding agent being very specific for what you want to build. And so the most powerful strategy here, and you'll see this in action in just a little bit, is to have the coding agent ask you questions. Like we will specifically ask it to ask us questions.

**[0:10:13]** And you can go through this process for a good 20, 30 minutes, even beyond that if you really want to set the stage well going into the development later on. So product managers, this is your job when you're working with cloud code. And even if you're, you know, you're a solo

**[0:10:27]** developer shipping things without a product manager, this is still an important step to go through. It's very important to stay high level at first. We're not getting into the weeds right now for how we're going to test things or what files we have to change in our codebase. At this point, we're just

**[0:10:41]** trying to figure out what are the requirements that we need to translate into code. And then we'll have a separate planning process where we're getting more into okay, here's how we're actually going to code it and the parts of code of the codebase that we need to edit. So, at this point, we're very very

**[0:10:55]** high level. And then after you have a conversation with the coding agent where you figured out exactly what you want to build, what is our scope of work for this sprint or this new application, then it's time to create your AI layer. And I have this marked as optional here

**[0:11:11]** just because when you are working on an existing codebase, you might already have that AI layer already created. But if you don't have it, I highly recommend investing a lot of time upfront building this. Now, for our one hour here, it's not like I have a lot of time to like

**[0:11:26]** really get into best practices for building your global rules and your skills and commands, but I'm just saying like this is the part of the workflow where you will create that. And so, your global rules, these are the conventions, the rules that you always want your coding agent to follow. Like here are

**[0:11:41]** our coding styles, here's our testing strategy, our logging strategy, things like that. And then your commands, we're going to see a lot of these in action today. and your skills. These are your reusable workflows. So, anytime you find yourself prompting something more than three times, you should turn it into a

**[0:11:58]** command or skill because that's just a prompt that you're going to load into your coding agent when the time comes. Like, this is my process for planning. This is my process for creating PRDs or stories in Jira, for example. That way, we don't have to type things out and

**[0:12:14]** it's a reusable workflow that we can share and create a standard across with our team. very very important. So we don't want to do manual prompting as much as possible turn things into something in the AI layer that you can invoke right like we can take a command

**[0:12:30]** in skill and say you know slash plan now we are going into our planning process and so that actually goes into the first command that we'll use here and again I'll show this all in action in just a little bit so the first command is a process guiding the coding agent from an

**[0:12:48]** unstructured conversation into a structured PRD. Like I said, we go from exploration to structure so that we have a single document that is produced from this command that outlines all of the core sections for our PRD is short for product requirement document. So this is like the initial scope of

**[0:13:09]** work for an application if we're doing green field development or these are all of the tickets that we need to handle if it's a new sprint that we are planning for in Jira for example. And then I can take the PRD and also have Claude code split it up into individual pieces of

**[0:13:26]** work to create as my Jira tickets. We'll see this in action. And so it handles literally everything. It parses this document. It figures out what are the individual phases or pieces of work that we should create as tickets and then we'll even use the Jira MCP server to

**[0:13:44]** create those things so that we don't have to do that backstage work like Leor was talking about of creating those tickets in Jira. We want to have our coding agent handle all of that administrative work. And so we end with tickets in Jira and then we can pick one

**[0:14:00]** of them. So this is where you know the product manager would hand things over to the developer to pick a ticket and then go into the full piv loop. This is the full process we go through to handle individual sets of work with our coding agent. So we'll get into this next, but

**[0:14:15]** first I want to show you a live demonstration of our ideation phase. And so I'll go over to my codebase now and I'll just describe very briefly the application that I have for a demonstration here. And so this repository again I have it linked in the description. I also linked it in the

**[0:14:37]** chat. Um actually I didn't link it in the chat. So I'll do that right now. So let me go out copy this and I'll paste this in our chat here. If you guys want to just poke around the resources that I have for you guys and or even follow

**[0:14:50]** along, you can feel free to do that. But the application for my demonstration is just a quick poll builder. So, you know, you put in your question like, uh, how experienced are you with AI coding? And then we have our options here like I'm a beginner, I am intermediate, or I am

**[0:15:08]** advanced. All right, cool. And then I create a poll. Yeah, the point of this application is that it's super simple because I'm going to be focusing on the process, not focusing on the application itself, right? So, I want something very quick to build on top of so that I can

**[0:15:22]** quickly go through how I create stories, handle tickets, go through the pivot loop and the system evolution. And so, uh, what I'm going to do to begin is I'm going to go into cloud code and I'm going to plan my next fictitious sprint. So we have this very basic

**[0:15:41]** application right now where we can create a poll and if I you know actually had the application deployed then people could use it and go and and answer the poll. But there are a lot of features that are missing. And so I have a prompt prepared ahead of time that I'm just

**[0:15:57]** going to paste in right now just so that you guys don't have to watch paint dry as I give my initial brain dump. But again, this is your point where you just dump all of your ideas of what you want to build, being as specific as possible. So even if you wanted to specify things

**[0:16:13]** like your tech stack and your architecture, if you're more technical, this is where you do that. But even if you are less technical and you are, you know, a product manager, for example, you can still stay pretty high level here and just describe the features that you want to build.

**[0:16:28]** And so I'm saying like here's my brain dump for phase two. Like the next thing that I want to build on top of the application. Let's say I want to build a live presentation mode. Like right now in the poll builder when I I can't really like see answers come in live.

**[0:16:42]** Like if I click see current results, I'd have to refresh the page in order to see new entries. I also want to build a QR code generation, multi-question polls, multiple choice questions. Like there's like a lot of things that I want to build on top. this is my next sprint

**[0:16:58]** that I want to uh you know my end goal is to have all these things created as uh Jira tickets that I could then pass on to developers or pass on to my coding agents if I am a developer and so I've described everything here um usually if I'm not just doing a live

**[0:17:13]** demonstration I would make this prompt a lot longer but I just wanted to keep it concise right now and then the important thing here this is what I was saying in the diagram before you write anything ask me clarify ing questions one at a time using the ask user question tool.

**[0:17:31]** And so now this is where I'm going to make sure that I get on the same page with my coding agent. And so one at a time it's going to ask me these questions. And in Claude Code we have this ask user question tool where we can see these questions pop up with multiple

**[0:17:44]** choice answers for us. So it's really easy to blitz through things because a lot of times what it recommends is actually what I'm going to go with. But it still gives me the opportunity if I want to say like, hey, no, you're wrong here. Like, let's actually do it this

**[0:17:57]** way instead. So, we can, you know, remove that ass that incorrect assumption that it was making. And for other coding agents that don't have this specific tool, it's this whole process is still going to work. It's just going to be a little bit slower because you'll have to type out each of your answers

**[0:18:12]** more like you're just chatting with an agent. Uh, but it still works in exactly the same way. So, it's asking us questions here like how should real-time updates work? I'll just go with what it recommends here just for the sake of speed, but also you have this option to

**[0:18:24]** chat with it. So for each individual thing, if you really want to dive deep with the coding agent, which a lot of times I would recommend you do, you have the opportunity to do that. And of course, how deep you go does depend on how technical you really are. Like right

**[0:18:37]** there, you know, how should real-time updates work? That is a pretty technical question. So if you want to just go with what it recommends, that's definitely okay. But if you have that knowledge and like really understand the architecture of the codebase, it's just more power to you. You're able to to really make sure

**[0:18:52]** that you clear assumptions. Otherwise, if you're, you know, more on the product manager side, you might have a couple of wrong assumptions that sneak into your Jira tickets, but that's why you work with the developers as you're planning things, right? Like you'd have your sprint meeting where you'd make sure you

**[0:19:06]** clarify these kinds of things. Uh but the goal is just for the coding agent to help us with that starting point of having all the context in Jira ready for developers to refine and pick up and work on. And so for the sake of demo I'm going to

**[0:19:19]** say uh let's uh end the questions here just because sometimes it can go on for you know a good 10 15 minutes asking us a lot of questions. I'll allow it to make some assumptions for the sake of speed but uh at this point you know I've already shown you what I need for what

**[0:19:33]** this process generally looks like. And so at the end of of our chat here, this context, this short-term memory for cloud code is what we're going to turn into the PRD. So we are about to run our first command where we create that product requirement document. The input

**[0:19:51]** is the conversation. The output is a single document, a source of truth that we could, you know, then upload to Confluence or check into source control, wherever we want to store that. And then we can create the JER tickets from that. All right. So that was the last question

**[0:20:06]** there. Now it's it's uh taking in my message. So it will move on to creating our PRD. And Cloud Code is smart enough to know the capabilities that are available. So when I've gone through this process, a lot of times it'll just go right to loading the create PRD skill

**[0:20:22]** and it'll walk itself through creating that document in exactly the structure that I am looking for. And so I'll go ahead and open that so we can see ahead of time what that actually looks like. And again, all of these commands that I'm about to walk through are available in the GitHub repository

**[0:20:39]** that I have linked in the description. So I'll go to create PRD. That is our first command. And again, commands and skills are really just procedures. They are prompts that we get to load in in real time whenever we want. And so create PRD. This is going to generate a

**[0:20:55]** comprehensive product requirements document. we are we get to also specify like where it also outputs this file. So commands and skills support arguments. So that's how we can make things dynamic and we'll we'll talk about arguments quite a bit because most of my procedures have arguments. So I can make

**[0:21:11]** them specific to what I am doing right now. And the main thing that we are outlining in this PRD uh command is the structure that we're looking for. Like we want every PRD to have an executive summary, a mission, target users. This is a lot of product manager speak. So if

**[0:21:27]** you come from the product manager space, really this is your opportunity to take how you already write PRDs and make it so your coding agent does it in the exact same thing. Again, the foundations that I'm laying for here in this process is not for you to completely have a

**[0:21:42]** blank slate for your software development life cycle, but to take your best practices that you've established as a team and teach it to your agents. That's what we're doing with skills and commands. And so your PRDs are going to look the same, but your agent is saving you hours and hours and hours because it

**[0:21:57]** gets to generate this based on our conversation. And so right here, like what I can do is um it kind of went through this process itself like it loaded the skill automatically, but I'll just show you like if I wanted to invoke it myself, I can just do create PRD and then I can

**[0:22:14]** specify the file name as an argument like this. It's just when you invoke something or similar to when you invoke something in the command line for all you developers. So we just have spaceepparated arguments for anything that we want uh the command to respect like where we're going to output it. So

**[0:22:29]** we're going to have something in the agents folder. It'll just be like a markdown prdown file. And then of course we could you know like use the Jira MCP server to upload or the Atlassian MCP server to upload it to Confluence. We could upload this document to Google

**[0:22:45]** Drive or put it as context in a GitHub issue. however you want to you know store this artifact that is like the initial source of truth for that new application or that new sprint that we are planning and so once we have our PRD created and it's going to take a little bit um

**[0:23:02]** because it's generating a larger document here you can see that claude is currently thinking through the structure so it's taking this conversation reasoning about everything that we we have discussed here and then creating a document from that once we have our PR RD we are going to create our stories.

**[0:23:20]** Now you could do this as a single command where you create the PRD and the stories all with a single call to claude code. The reason I have these separated is because once you have the PRD created, it is a good time for you to validate things yourself. So going back

**[0:23:38]** to the diagram here, it is important for us to delegate as much coding to the coding agent as we possibly can. That's the backstage work for developers now. But we want to remain in the driver's seat because every single artifact that our coding agent produces, whether it's a PRD or it's a set of code, we want to

**[0:24:00]** review that and we want to have human in the loop so that we can iterate on anything. And so when we create our PRD, it's not good enough to just immediately create stories from that. Like it's important for us to review the artifact and make sure that things are really

**[0:24:15]** aligned with what we are looking to do next because yes, we had it ask a bunch of clarifying questions, but maybe we didn't have it ask enough questions or maybe it didn't quite understand our answers. That's why it's important for us to still review things. So, I I know

**[0:24:30]** that takes some time and the promise with AI is that it speeds things up a lot. But even if you do take time refining the PRD with the coding agent, it's still going to save you so many hours compared to if you did this entire process yourself. And so for the create stories command,

**[0:24:49]** we run this after we have reviewed the PRD and maybe made some changes to it. And so for this command, we give it the path to our PRD. Obviously, we want Claude Code to know like this is the PRD that we want to create our stories from. And then we can also specify the Jira

**[0:25:07]** project and epic. And so what I have in Jira created ahead of time is I just have a a simple project created with an epic that doesn't have any tasks in it right now. So this is what we're going to populate live in a little bit with our create stories command. And so I had

**[0:25:25]** to do a little bit of manual work to actually create the epic. But after that point, I'm not doing any work myself in the Jira platform. That's all backstage. I don't want to do that myself. And so I want to have a single process that goes from here are my ideas to everything is

**[0:25:43]** populated here. And it feels like magic every time this happens. So we'll get to that in a second, but obviously we need to have the PRD created first. And you can see that right now it's outputting a lot of tokens cuz it's in the middle of creating that file for us. So we just

**[0:25:58]** have to be patient. But uh that gives me some time here just to show you really quickly what uh we have in this command here. So first of all, we have a phasebyphase procedure that we're walking claude code through. Again, commands are just prompts that we're we're having the coding agent run

**[0:26:15]** through. So we're having it load the PRD because we can also run this in a separate Cloud Code session if we don't want to run it in the same one. So we can load the PRD. That's all the context it needs. Then it's going to break down into stories and I can render this so it

**[0:26:29]** looks a little bit nicer here. So we create a user story and we can specify the format as well. We can define the acceptance criteria. So just like we create the structure for the PRD in the create PRD command, we can do the same thing for the stories here. So your team

**[0:26:45]** probably already has a convention or if you're a solar solo developer, you still probably have some kind of convention for how you want to create these artifacts. Here are my tasks. Here are my issues. Whatever that is. And so we bake that into the command and that makes it more reliable, repeatable, and

**[0:27:01]** it makes it so that you don't have to have a brand new process that everyone is extremely uncomfortable with, right? Like we want to make it uh easy to adopt these new tools and new processes. And so then we go on to the structure for each story. Here is exactly what

**[0:27:16]** you're going to create. Here's how we're going to order them. We even have some validation built in. So it kind of checks its own work to make sure that it has, you know, fully extracted all the phases out of the PRD, for example. And then we have the output. We're going to

**[0:27:28]** save everything to markdown documents. And then if we have the Jira integration, so I actually set this command up so that if you're not working with Jira, then you can still just work with the stories in local files. A lot of solo developers just manage their entire system with markdown, and that's

**[0:27:44]** totally respectable. So this command works for that. But if we do have the Jira integration and we tell it how to check for that, then it's going to create everything in the epic that we specified um in the argument here. So like if these things are filled in and

**[0:27:59]** we'll see that in just a second. So okay, we created our PRD and so we can take a look at this. So this document, I'm not going to read through the entire thing right now because it's a pretty long document. The point of uh what I'm demonstrating right here is mainly to

**[0:28:15]** show you that the structure that we have laid out in the create PRD command is exactly what we see in our final PRD. So we have our executive summary, our mission, our target users, everything that I showed you in the markdown here. And then we also have what is in scope.

**[0:28:32]** So for our phase 2 sprint, we want the multi-question polls, per user toggle, the full screen presenter presentation page, uh everything that we gave in our initial brain dump. So this PRD is the result of our conversation plus the create PRD process, right? Like those two things together, this is the baby of

**[0:28:53]** that. And so now this PRD we can run through our create stories command. And this is the thing is like after that initial brain dump, I'm really not doing much typing. I'm running commands. I'm answering questions. That's really all I have to do. And so I'm going to go ahead

**[0:29:10]** and copy this. And like I said, you could do this in a separate context window if you wanted to, but I'm just going to do it right here because it was relatively short. So I'm not going to iterate on the PRD for the sake of speed here. So I this is one moment where it's, you

**[0:29:25]** know, do as I say, not as I do. But uh generally if I am off camera and really working through my initial planning for something, I'm going to spend a lot of time looking through each section here and making sure that everything is as I intend. And so I'll run create stories

**[0:29:40]** with uh the P path to my PRD. And then I have to give the ID of my Jira project and also the ID of my tag. And so for those of you who are using Jira, you just get that like this is the ID of your project and then this is the ID of

**[0:29:56]** your epic. And then if you're doing something else like using GitHub or linear, you're going to go through the exact same process. You're just going to use, you know, the GitHub CLI to create issues instead of the Jira MCP server or you're going to use the linear MCP

**[0:30:10]** server. So again, it doesn't matter in the end what tool you're actually using. So I'm going to go ahead and run this. So it's going to break down. It's going to follow that exact process that I just showed you, breaking down the PRD. And then after a few minutes, it'll take a

**[0:30:23]** little bit of time for it to reason about that. We'll see all of the subtasks start to get populated here in Jira. And then at that point, we can have developers just pick them up and go through the pivot loop that I'll cover with you guys next. And that's the

**[0:30:37]** beauty of it is also you can have developers work on everything in parallel. They can assign themselves. You can also, you know, use the Jira MCP server to have the the developer get assigned automatically when it picks up a piece of work. You can create a system in your task management software where

**[0:30:53]** really agents are managing everything. It's kind of like the the whole COXOS that Leor was showing you guys where you have the agent managing all of the grunt work of organizing and um you know all of the you know CRUD operations of creating tasks and updating them and

**[0:31:10]** assigning them and everything. We can have agents manage all of that with the Jira MCP server. And I'll show you guys what that looks like. If if you go into cloud code and do slashMCP, you can see that I have the Atlassian uh MCP server connected. So, by the way,

**[0:31:25]** this also gives me access to Confluence, not just Jira. So, if you wanted to like store documents in Confluence, like you wanted to store the PRD in Confluence and then have a developer load that PRD with the Jira MC or the Atlassian MCP server, they can do that as well. Um,

**[0:31:41]** and so if you are an Atlassian kind of shop where you have Confluence and you have Jira, you can have your coding agents manage all of that. And it's really the same thing no matter the platform that you're using. And so the way that I have this MCP server

**[0:31:53]** configured is just with this um MCP.json file. And if you're curious how I set this up, this is the crazy thing, guys, is that you can have Claude Code help you with anything. It has access to its own documentation. So if you say, you know, help me copy over Koh's commands,

**[0:32:13]** and you just give it the path, it can bring all that into your own project or you say, help me set up the Atlassian MCP server. It'll search the web. It'll pull the exact configuration. It knows to create a file called MCP.json. It'll set up everything for you. The the time

**[0:32:30]** in in our world where we had to be technical to do these kinds of things is no longer here, right? like a product manager, a QA engineer can use cloud code to do any part of their job just like a developer can because you don't have to know how to run commands or set

**[0:32:46]** up MCP servers anymore. I mean, yes, it's still helpful just in case the coding agent trips up. So, it's faster for a developer, but uh also coding agents are really good at debugging things. If the MCP server doesn't connect right away, you can ask it like, "Hey, I'm getting this error. Help me

**[0:33:02]** figure it out." maybe like search the web for some more Atlassian documentation for example and so really for like all these things I didn't configure that all myself like I have my repository of commands and skills I pointed cloud code there and I said all right Claude for this AI transformation

**[0:33:18]** workshop that I'm doing with Leor I want you to set up a brand new repository and bring in my resources and customize it to work with Jira instead of GitHub for example and it it just did all of that for me. So, a little bit meta there, but

**[0:33:30]** I hope that demonstration is um is cool just to see like how easy it is to get anything configured in your AI coding environment. And so, for all these resources that I share with you, you don't even have to bring them in yourself. So, we can see that it created all of

**[0:33:46]** the stories here and then it asked me a question like, do you want to push to Jira now? So, I said yes. And now it's going to take advantage of that Atlassian MCP server to populate everything. And so I don't think we'll have it yet. Let me refresh the page.

**[0:34:00]** But we'll in just a second here we'll start to see things get populated. I think it's in the middle of reasoning through that. Okay. Yep. So we can see that the token count go up as it is formulating those tool calls basically. So the agent is performing these operations under the

**[0:34:18]** hood. And we're almost done with the first step by the way. And once we get into the piv loop, things go pretty quickly because we're doing so much of the work up front with our ideation. So we're getting to this stage right now where we are getting our tickets in

**[0:34:31]** Jira. And then we'll pick a ticket and then this is where we just rip through the implementation with the piv loop. So all right, let's uh go back to claude and see where we are at. All right, calling at lassian seven times. You can also include do control O

**[0:34:48]** so that you can uh see the full tool call if you want some more visibility into what it's doing. So it's using the create issue MCP tool. It's got my ID, the project, all the things that we specified as parameters like the epic and the green circle here means that the

**[0:35:05]** tool call actually finished. So I'll do control O to decompress again and then go back over. And now when I refresh, we'll see some or maybe even all of the issues created or tickets I should say. Take a look at that. So we don't have all of them yet. It's in the middle of

**[0:35:21]** running those tool calls, but we have things populated already. And the cool thing here is if we click into any one of these like um let's say I'll just click into the first one for example at14. If I click into this, we have a lot of context given here in the ticket as

**[0:35:39]** well. So another really cool thing is like for a product manager usually your description isn't even going to be this good because you don't have full context for the more technical details. So you can also use claude to provide more context to the developers up front if you want to work with it to you know

**[0:35:55]** create this kind of issue description. And of course for the ticket descriptions it's entirely up to you and your commands for what exactly you'd put here. Like in my create stories command, I specifically said I want the story and acceptance criteria. And then we could even add more context

**[0:36:12]** here. Like we could have some more research on how the coding agent would recommend doing this. We could put that as a comment here. Sometimes my cloud code will actually do that by itself. It's cool to see. Um so yeah, it's uh actually it is so it's adding technical

**[0:36:25]** notes as comments to each of the issues. So, not only are we creating issues, but we're providing more context as the coding agent has done some research for each of the implementations, like looking into the codebase, providing those initial suggestions for how we' build each one of these things.

**[0:36:44]** And so, I'll let that run in the background here because that's not like super important for me to have finished before I go to the next thing for you guys. And the next thing is really like let's just pick one of these and let's work on it, right? Right? Like at this

**[0:36:57]** point at an organization level, the product manager would take this this list and send it over to the development team. You know, might have some scrum meeting or whatever to talk about these things and and again refine things. If you uh need to like fix up any of these

**[0:37:15]** issues and then you go on to the development or if you are a solo developer then these might be GitHub issues that you're now going to handle one at a time. And so we just need to pick one of these to work on. And uh let's see. I'm trying to think like

**[0:37:32]** maybe the audience vote page would be a good one. As an audience, I want mobile first page that shows only active questions. Lets me submit my answer. Auto advances when the presenter moves on. That's a decent one. What else could I work on here? I mean, there's a lot of

**[0:37:45]** good features. I'm trying to like think of like the best one that would be good for a live demonstration. Uh presenter projection p. Actually, this this is a good one here cuz that's actually what I was planning for my prep. So, I want a full screen page that

**[0:37:57]** shows active questions, animated bar chart, real-time updates as things are coming in. That's definitely something that we're we're missing right now because this looks pretty bland for the results page. So, we'll tackle this issue first. And the really cool thing is the input into our development process just is this issue. And that's

**[0:38:18]** actually something I've been doing a lot more recently with AI coding assistance is my input to writing the code is always some artifact. Like for me personally, uh I do a lot kind of as more of like a solo developer or working on open source projects. So usually the

**[0:38:34]** GitHub issues is actually my entry point. So I'll put my artifacts here. I just wanted to show Jira because that's how so many teams work. But uh your Jira tickets like that is the input. And so going into the pivot loop here, we're going to go through a similar first step

**[0:38:50]** where we're just going to explore our solution. And the input into this is just one of the tickets that we pick. So the developer takes that work. You can use the Jira MCP to assign yourself and then we start exploring the solution. And so for planning with AI coding, you

**[0:39:09]** always have two layers. You have the project level planning and that's everything that we did here right like this is like the PM level planning and then you have the task planning and that is the individual ticket level and the important thing that I I've already explained a little bit here but I just

**[0:39:28]** want to be like really clear on this is the layer one planning is higher level here are the features that we want to build or the bugs we want to fix at this point we are not digging into the code now that we're peaking a single ticket for layer 2. This is where we get more

**[0:39:44]** in the weeds of things. This is where we're going to analyze the codebase, the documentation, figure out what parts of the codebase we actually have to touch. We're starting to dive that deep. And it's really helpful for the coding agent to do this two-step process because then now that we're getting really into the

**[0:40:01]** weeds of things, we already have a lot of context for what we want to build overall. At this point, the ticket has translated the stakeholder or business requirements, whatever you want to call it. And we maybe even have some higher level recommendations for what part of the code we want to touch. And now we're

**[0:40:16]** just really getting into that. So just like creating our PRD, when we are creating the actual implementation, we start very unstructured. We're just going to have a conversation with our coding agent figuring out how should we go about solving this problem, fixing this bug, you know, implementing this

**[0:40:35]** new feature, whatever that is. And then we go from unstructured to structured. So this is very similar like creating a plan for implementation is very similar to creating a PRD. And we're going to have a command for planning out the feature just like we have a command for

**[0:40:51]** creating our PRD. And so I'll show you guys what this looks like right now. So I'm going to go back into my codebase here and I'm going to begin a brand new conversation. So let me escape out of this. I have a brand new conversation with Claude because you can imagine that

**[0:41:08]** like you as a developer, you are picking up a single ticket and you don't have any context around creating the PRD or stories or anything. So we're going to pretend like this conversation doesn't exist because it's going to be someone else doing this or maybe you doing it at

**[0:41:23]** a different time. So brand new conversation. The first thing that I always do when I am preparing for an implementation is I run what is called a prime command. So another example of if you're going to prompt a coding agent to do something over and over again, just

**[0:41:39]** turn it into a prompt. Turn it into a command because that way we don't have to type it out again. And so this prime command quite simply its job is to walk a coding agent through understanding the codebase. We want to know what we already have to help us think about what

**[0:41:56]** comes next. Right? So we're going to load external context which this is where we can specify confluence pages or Jira tickets that we want it to understand. In our case we are actually going to specify a Jira issue. Right? We're going to understand the codebase from the lens of this Jira ticket. this

**[0:42:14]** new thing that we want to build, but also aside from that, we're just going to generally understand the codebase. So, we're going to study the features. We're going to study app routes. We're going to check recent git commits. I love using git as long-term memory for my coding agents. So, a lot of times

**[0:42:31]** what you've done recently in a codebase is going to help guide what you do next because you're going to look at like the code patterns you followed for recent commits and things like that. This is a a very very powerful part of any new conversation with a coding agent. And

**[0:42:44]** obviously the steps that you want your coding agent to go through to analyze the codebase is very custom to your codebase. So all of the commands that I have here are starting points for you, but you're always going to get the most out of them if you customize the

**[0:43:00]** commands to your process, your architecture, your code bases. And so I'll start by running a slashp prime here. And one of the arguments that we have is a comma-epparated list of Jira issues. And so for example, uh going back to our browser here in Jira, um I just want to use um this issue

**[0:43:21]** right here. So the ID for it is AT23 for our uh presenter projection page. So I'll do slashprime and then just AT23. So it's going to understand the entire codebase but also from the lens of this issue. So first it'll use the Atlassian or Jira MCP server to pull that context.

**[0:43:43]** I can do control O and we can see right here that uh first it's listing accessible resources and then it's going to call the tool to get that specific issue. It's performing a bunch of reads here. Also looking at the git logs in parallel. There's just a ton of context

**[0:43:57]** loading that it's doing at the exact same time here. Now, you want to be careful to not load too much context into your coding agent because it's not like you want, you know, 50% of your coding agent's context window to be just loaded with a bunch of research it's

**[0:44:10]** doing, but we definitely want to load in the core files and the core uh history of what we've done recently. And so, if you ever want to, you know, tweak that lever of how much context you're bringing into a session up front, it's just you change the prime command,

**[0:44:26]** right? Like you change this over time. Like maybe you only load in the first part of a Jira issue or you only read from this part of the codebase. It's totally up to you for how you formulate your commands to optimize things for your process. So here we go. Project

**[0:44:39]** context loaded. We are going to be handling the presenter projection page. So it pulled full context there. Gives me a quick summary of my codebase. And um yeah, I think we're we're good to go. Um though it actually it actually says something interesting here. So this is really cool. This is a good uh live

**[0:44:57]** teaching moment. It is able to recognize based on querying my state in Jira that there are some blockers that we need to take care of before we could really go on to AT23. So it understands the dependency mapping. That is actually one of the things that I have built into

**[0:45:16]** create stories here where it can help you understand dependencies. So maybe we would actually have to handle AT22 with a QR code first. And um I think this is this is something that we'll take on. So maybe we'll do like okay look at AT22. What do we need to implement for that?

**[0:45:34]** Right? We're starting very unstructured in our planning here. We're actually shifting gears right away which is totally okay. But we're just going to have it get a little bit of understanding of this feature that we want to build and we'll start to ideulate there. So we're going to

**[0:45:47]** explore how we want to build this, understand the codebase, and then get into that structure plan that we'll go and send into implementation. And so at this point, uh, we have full context from the issue. But now we just do a little bit of exploration. And what this looks like totally is up to your

**[0:46:06]** own process. In fact, this is one of the things that I don't actually have as a command because it's very free form at this point. So I can, you know, for example, go into my speech to text tool and say, "All right, let's build AT22. I want you to spin up a few sub agents to

**[0:46:21]** research the codebase and help me ideulate around uh how I would build this new feature into our poll application. So just like a really quick prompt here and also showing you sub agents because sub aents is something that I use all of the time for research. If you aren't

**[0:46:40]** familiar, sub aents is basically a way for you to spin up a subprocess, another agent that runs under the hood to go and look at a bunch of things or perform a bunch of work and then report back a summary to our main cloud code agent here. And it's really powerful for

**[0:46:58]** research because when we are exploring a codebase or doing web research, we are loading in tens of thousands of tokens of information. Like you can see that this one already loaded in 32,000 tokens. We are going to completely overwhelm our main agent if we had it do all the research by itself. And with

**[0:47:18]** research, you really only need a quick summary at the end, right? Like here are generally the files that we have to edit. Or if you're doing web research, like here are the core articles that you should read that would help with best practices for this tech stack. So we've

**[0:47:31]** already used over a 100,000 tokens here, but we only have a few thousand tokens that are returned back to our main agent. And so yes, with claude code with we now have the 1 million token limit with Opus. And there are a lot of other models through codeex and GitHub copilot

**[0:47:47]** and everything where you have 1 million tokens. But here's the thing, just because you can fit a million tokens into a large language model does not mean that you should because they get overwhelmed just like people do. So we want to deploy strategies for managing context. Well, sub agents is one of the

**[0:48:06]** best strategies for that. So we just have to wait for these three exploration agents to finish and then our main agent will get back a summary so it can reason. We can see that these are all done now. So it'll reason about what these sub agents did and then it'll

**[0:48:20]** provide me a final output here with its recommendation for how we can handle this Jira ticket. And so at this point, uh, going back to our diagram here, we're still at this initial exploration, right? Like we're going to explore ideas architecture concepts text stack. I'm not going to go through each

**[0:48:38]** one of these things right now for the sake of speed, but this is our chance to ask questions or like we did when we created the PRD, have it ask us questions as well because it's important to remove assumptions going into writing the actual code. It might even be more

**[0:48:53]** well probably not more important than assumptions in the PRD cuz the PRD is so high stakes but it it is very important as well. So we go through this process where once we feel confident that we're on the same page with the coding agent then we'll run a command that'll create

**[0:49:08]** a structured markdown document for our plan. We want again we we want the output of our planning process to be a single artifact and that artifact is going to contain all of the information that the coding agent needs to do the actual implementation. And so I'll show what that looks like in

**[0:49:29]** a little bit. But uh first I want to actually invoke the command to create the plan and then I'll explain more how it works just so that we can have things move along well for us here. So here's the synthesis with real decisions to make. Here's what we know. Okay. And

**[0:49:44]** three decisions worth making before coding. So it's asking me some questions here. I'm going to blitz past these for the sake of demonstration, but it is worth taking the time with this usually. So I'll do slash plan. This is my command where I can now describe the feature that I want to build. So, I'm

**[0:50:02]** just going to say here, go with your uh recommendations and create the plan for AT22. So, I'm just going to give it permission here to just pick whatever it wants. Usually though, it would be worth taking your time and answering these things and having it ask you more questions as

**[0:50:19]** well. So, while this planning command runs, not to be confused with the plan mode in cloud code, this is a separate command that I have created right here. It's very similar to the create PRD plan where we have phases laid out like here's the research you should do

**[0:50:33]** initially. Explore the codebase. Make sure you have full understanding for how we're going to implement it. Then create the plan file. So just like we created a prd, we're now creating a plan.md and it has our structure. So we want a summary, a user story. It's going to be

**[0:50:51]** similar to the PRD, but now we're getting into the weeds of how we're actually going to implement it. And so, for example, one thing that we definitely didn't have in our PRD command is the patterns to follow. Like, here here's how we're coding things. Here are the files that need to be

**[0:51:08]** changed. Here's the task order, everything we're going to execute down to the individual level of the files that we're going to create and update or maybe the commands that we're going to run for testing. So, also laying out upfront, how do we want our coding agent to validate its own work? Because when

**[0:51:25]** we get into the implementation, we're going to send this plan into the coding agent. We are going to delegate all of the coding to the coding agent. And the only reason that I'm comfortable doing that is because I still find myself in the driver's seat because I'm a part of

**[0:51:40]** the planning process. I'm iterating on the plan. I'm doing the exploration and having it ask the right questions. And so we'll have it write the code and then we'll also have it do some of the validation, right? Like we can have the coding agent right after it does the

**[0:51:55]** implementation. We can have it write the unit tests, write the integration tests, do the linting and the type checking. It can take care of all of these things. Not that it's going to be perfect, but the point is we want it to take care of as much validation as possible so that

**[0:52:08]** by the time control passes back to us for our human validation, there's less that needs to be corrected. Right? We want to reduce us being the bottleneck for actually shipping the code that we're creating with the help of our coding agents. And so I'll jump back over to the codebase here. And we can

**[0:52:26]** see that our plan file is created. I'll take a look at this really quick. Uh just another one of those things that I don't want to spend the time iterating on too much right now. But we have the summary of our work. Uh we have the decisions that we've locked in. These

**[0:52:39]** are the things that we would have been working with the coding agent to establish. And then um we even have like the individual files that need to be created and updated. And then we have the task list. So usually the task list you don't create as Jura tickets, right? Because

**[0:52:56]** this is like so granular that this is for a single coding agent implementation. So you let the coding agent handle an internal task list as it is writing the code. And then we have the self- validation. So it's going to be running the type checking and linting and unit testing. We could also have it

**[0:53:11]** do endtoend testing if we wanted to use browser automation tools with um you know the agent browser CLI for example. So that's actually one of the skills that I have for you guys here. I can spin up the browser and navigate through it and like create polls and and vote on

**[0:53:25]** the polls just like a user would. And so for the sake of speed I won't do that but you can have coding agents do very very endto-end testing. You want it to validate as much as possible. So the important thing here is once you have iterated on the plan and you're

**[0:53:40]** confident in everything, you actually don't do the implementation right here, we want to start a brand new session with Claude code. So I'm going to open up a a fresh blank slate with Claude. The reason that I want to do this is because when you are working with AI

**[0:53:58]** coding assistants, you want to make sure that they are as focused as possible. And it's important to be focused in order to be focused to do your planning and implementing in separate sessions because also the coding agent has probably built up a lot of bias throughout this conversation as we've

**[0:54:15]** been working with it. We wanted to have a fresh set of eyes on the problem going into implementation. And so of course I have an execute command. And so all I have to do is slashimplement and then I give it the path to the plan that I created in the prior session. And the

**[0:54:30]** whole point of this markdown artifact is that it has all of the context that the coding agent needs to implement because it has the summary. It has the recommended files to change and the task list and the validation strategy. There's no reason for us to stay within this other context window in the first

**[0:54:46]** place. So I can send off this command. It's going to read the plan and then it's going to walk through the process I have in the implement command to do the implementation and the validation. And this um command that I have for implementation is actually very very concise. It's u only like a couple of

**[0:55:04]** hundred lines long here because really it's the the plan that guides the entire development. The main thing that I'm walking it through here is just the process of you know loading the plan preparing the implementation like maybe making a new git branch for example like any kind of

**[0:55:21]** of uh process that you have in your usual software development life cycle for how you want an engineer to work. We're just encoding that into the command here. We want to make sure that we're verifying any kinds of assumptions. So we're also sort of doing like a second pass on the plan before we

**[0:55:35]** go into the implementation. So yeah, then describing how we want to do validation for example, when we want to pass control back to the user, outlining all of that for the agent. And so going back to our diagram here, we're in this step right now, right? We we've cut a

**[0:55:50]** fresh session, sent the plan into implementation, and then we'll wait for it to write the code, do all of its own validation, and then we'll also step in and we'll do a code review. Right? And it's not like you have to do this. Uh, some people are are a big fan of just

**[0:56:08]** shipping the code right to production and having the coding agent do its own work. I'm you I'm not a fan of that myself. I still the engineer in me still wants to review all the code. So for any like serious production coding that I'm doing, I still am reviewing all the code

**[0:56:20]** myself and then also doing manual testing. And so we can see that after we do the implementation like I'll refresh the page here and we'll we'll check out this new feature. like we'll see the QR code that's generated and we'll make sure that's all working before we would

**[0:56:33]** actually be confident to you know merge that pull request into our main branch for example or whatever that looks like for your software development life cycle going into production. So that review is important and um you know while we wait for the coding agent to run through everything here you can see that it

**[0:56:51]** created its internal task list based on the plan. It's writing the code doing all the testing. It's actually going to get through this feature pretty quick because I purposely built a simple one. Uh, but as it is doing this, I want to quickly talk about the last part of the

**[0:57:04]** system here. Um, and then of course after this, we'll we'll quickly get into time for a Q&A with uh with Leor too. So the last thing I want to talk about is system evolution. So when whenever we do a piv loop, it is very very far from guaranteed

**[0:57:24]** that the implementation will be perfect. Coding agents are not perfect. They are non-deterministic by nature. Even if we work super super hard to align with it in the planning phases, there are still going to be mistakes. But the powerful part of this system is we don't have to

**[0:57:43]** just treat the bug as a one-off fix that we address and then move on to the next pivot loop or move on to that next ticket. We can spend some time to fix to also fix the system that allowed the bug. And what I mean by that is we can

**[0:57:58]** have a sort of you know retroactive session with the coding agent where we say okay Claude you allowed this problem to creep into my codebase. I want you to dive into your AI layer. Like take a look at the at your rules. Take a look at your commands and skills, the

**[0:58:15]** process, the workflow that I brought you through. And I want you to identify things that we could improve there so that this kind of issue doesn't happen again. Like for example, maybe it broke something in the polling here where um I don't know, let's say that like all of a

**[0:58:32]** sudden the website looks really ugly when it when it built this new feature because it didn't like create the same it didn't create the component in the same style as the rest of our codebase. Well, maybe that means that there's something in our global rules that we have to update for like our style

**[0:58:46]** conventions. Or maybe we need to build something into our our validate workflow where whenever we validate the codebase, we make sure that like any new front-end component that we build is in compliance with the styles of our other components that are already in the codebase. Just kind of a random example I'm giving you

**[0:59:04]** there. But the point is generally when your coding agent does something wrong, there's going to be something in the context you give it that you can improve to not necessarily for sure fix the problem, but you're using it as an opportunity to continue to evolve your AI layer, making your rules more

**[0:59:20]** specific over time, making your workflows more reliable. And the best part of this is when you use every single Jira ticket as potentially an opportunity to improve your system, you get to improve the whole process for everybody because you can check in your rules and commands and skills into

**[0:59:38]** source control just like your codebase. The entire team can reuse these things and you can even create pull requests to update commands just like you create pull requests to update your codebase. So you can do code reviews making sure that everyone's in line with the changes you're making. I know that sounds like a

**[0:59:55]** decent amount of work, but it's so high leverage because every single time you improve a command or a skill, it might save engineers dozens and dozens of hours going forward because you've now made the validation process more reliable or you've made the style conventions respected more often, whatever that might end up looking like.

**[1:00:13]** And so really like the four things that I generally improve over time in a codebase is my commands, my ondemand context. This could also even mean like things in confluence. You just, you know, optimize your documents in Confluence for AI understanding your global rules and then also of course

**[1:00:30]** like your plan and PRD templates. You might want to to find and fix gaps in those over time. And so for every single codebase, I'm constantly doing this, right? Like if I have a piv loop where there is some kind of major issue, I step outside of the pivot loop to do

**[1:00:47]** this system evolution, I will update things that I created up front and then I'll go into the next piv loop. And if if actually there are no issues at all and the coding agent completely rocked that Jira ticket, then literally you just loop right back, right? You go through the planning

**[1:01:04]** process, you load that next Jira ticket and you go through the process. So it becomes very very cyclical. There's basically two loops here. You have the inner loop when everything's working well and you're just chugging through the work with the help of your coding agent. And then you have the outer loop

**[1:01:17]** when you're taking some time to reflect and make your system better. So, it's not like you always have to do the outer loop, but I encourage you to do it pretty often because not only are you improving your your commands and other parts of your system here, but you are

**[1:01:33]** also customizing your process to your specific codebase over time. It's like what I said, all of the commands and skills that I have for you guys here, they're a starting point, but they're more general, right? Like if you want to really optimize something for your process, you're going to start with

**[1:01:47]** these, find opportunities to make them more specific to your validation strategy or your planning strategy, whatever that might be. So, I hope that makes sense. I mean, that really is the whole process at a high level here. And so, I'm going to head back to Claude here and see where we are at. Okay, so

**[1:02:04]** the implementation is complete. We did it in a branch because our implementation command told it to. We ran all of our validation here. Here are the files that are changed. It's giving us a summary of everything that was done. It says that the implementation matched the plan. So I also have a part

**[1:02:19]** of the process here. This is actually something I did recently for my system evolution where after it does the implementation, it looks at the code and compares it to the plan to make sure that we didn't deviate. And then it also used the uh MCP server from Atlassian to

**[1:02:34]** update the ticket. So there's a lot of the admin work that we did as well, you know, creating the branch, creating the pull request, updating the Jira ticket. We don't have to have the developer spend their time doing that stuff retroactively. So now if I go back and I

**[1:02:46]** refresh my page here in Jira, we can see that uh everything is to-do except for this one piece of work that we picked up here. And I believe I think I think it also said there was even a comment. Yep, here we go. So it also posted a comment

**[1:02:59]** with full details. And maybe this is more, you know, context than we'd really want as a comment on a Jira ticket. But if you have a problem with this, then that would, you know, also be an opportunity for system evolution where you just specify in the implement command once you're done with your

**[1:03:14]** implementation, here is a more concise version of context that I'd want you to comment on the JR ticket. So now we can have this going into a code review, send it off to, you know, your VP to go and review, you know, whatever that is. So pretty cool. And then we can also test

**[1:03:28]** this in the application here. So, I'm going to refresh here. I'll create a new poll. Um, let's say what's for lunch and we'll just say um spicy mango chicken or spicy mango beef. All right, cool. So, I'll create this poll. And uh I don't actually see the QR code. I might

**[1:03:47]** need to restart the application. I think that might be why. So let me go back here and say uh all right I want you to restart the application and then use the agent browser skill so you can visit it and make sure we have the QR code and

**[1:03:59]** then let let me know like how I can see the QR code myself. All right so yeah I think I just have a stale version of the application. Um yeah so also I mean if I want to like look at more context I can literally just go to the ticket here. So we have a

**[1:04:16]** server helper. I mean, this is like a bit more technical. Like, honestly, I would probably rather have a higher level overview of what was actually built. Uh, again, something you could just change in the command. Um, but yeah, so let me go ahead and jump back over, see what Claude said.

**[1:04:33]** Um, code utility. There's no consumer of it yet. Oh, got it. Okay. So, it built out the code, but we need to actually make it so that the front end consumes it. Um, I want you to quickly uh implement the consumer just really fast. No validation, no GR ticket. Just go and

**[1:04:51]** add this right now so that I can see it live. Okay. So, that that's my bad. I didn't catch the fact that this was just getting the pipe the piping in place. And then it is that follow-up issue that we're originally looking at that does the presentation. So, that's on me. So,

**[1:05:06]** everything is working as intended, but we just have to Okay, so it created a QR demo page. So we can we can quickly look at that. So we'll see that in a second once it um once it does its own validation. So I I'm also showing a live demonstration of

**[1:05:22]** the agent browser where we can see it open up the website and uh it'll even like take a screenshot to and v validate things visually too. And then of course in parallel we can do the exact same thing. So I'll go back to the application and then I'll just do QR

**[1:05:36]** demo. Pretty cool. So yeah, I know that uh this is just a placeholder here, but I told it to build something quick to validate the piping that we put in place. And so then when we go on to the next issue, the one that was depending on this, then that's when we build in

**[1:05:50]** the full presentation view and actually use the the QR code for real. And again, the point of this isn't to show the full application, but just the process that builds these kinds of things. So all right, uh that that is that is really the process as a whole. We've

**[1:06:05]** covered we've covered it all from planning all the way to system evolution and creating those pull requests, getting that code into production. And uh I do want to reiterate that like this process it takes a good amount of time. It's it's not like you're going to blitz through something as fast as me. it it

**[1:06:22]** can be if you want but uh the important thing is even if you do take a lot of time iterating on the plans and validating the code it's still going to save you so many hours of work creating those documents updating things in Jira writing the code that the days are gone

**[1:06:37]** now of going to Stack Overflow in order to get your questions answered you don't have to copy and paste and be a Stack Overflow warrior anymore so yeah there you go that is the full process for AI coding it's foundational and simple enough where you can take this and mold

**[1:06:54]** it to whatever your software development process is.
