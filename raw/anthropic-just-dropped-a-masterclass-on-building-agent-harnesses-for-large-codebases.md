---
type: raw-transcript
title: "Anthropic Just Dropped a Masterclass on Building Agent Harnesses (for Large Codebases)"
youtube_id: efRIrLXoOVA
url: https://www.youtube.com/watch?v=efRIrLXoOVA
slug: anthropic-just-dropped-a-masterclass-on-building-agent-harnesses-for-large-codebases
published: 2026-05-20
duration: "0:28:11"
fetched_at: 2026-07-21
immutable: true
---

## Transcript

**[0:00:00]** Claude and AI coding tutorials are a dime a dozen these days. But what people are not really covering nearly enough is how to use these tools to work in large code bases. That's what I want to cover with you right now. Because you probably already have a complex codebase or two

**[0:00:18]** or three. You've got the apps and platforms that you're building your second brain. You have these code bases that are tens or even hundreds of thousands of lines long. And it can be tough to get these coding agents to navigate those larger code bases and work in them effectively. And even if

**[0:00:33]** you don't have a complex codebase yet, you'll get there, my friend. You start with a simple idea, a simple codebase. But as you evolve that codebase, the coding agent strategies that work before, they fall flat on their face. That's why I'm excited to get into this. Enthropic put out this article just a

**[0:00:50]** few days ago, how to use cloud code to work in large code bases. And really these ideas apply no matter the coding agent that you are using. And there's a lot of gold in this blog post. So I want to get into all of this. They do stay

**[0:01:03]** pretty high level in the blog post though. And so I also took all of their strategies and I built them into a demo codebase for this video. So not only are we covering the article, but we're also going to see concrete examples of all the strategies in action. And I even

**[0:01:19]** have a claude plugin that makes it super easy for you in two commands to take a lot of the strategies that we're covering here and immediately bring them into any codebase that you are working on. And so we'll get to that, but I want to start pretty high level, share these

**[0:01:33]** strategies, and let's see them in action as well. So, Enthropic starts by talking about all of the pretty impressive places where cloud code is currently being used at an enterprise level across multi-million line model repos, decades old legacy systems, distributed architecture spanning dozens of repositories. Basically, they're just

**[0:01:52]** making the point here that if you think your codebase is too complex for cloud code, you are wrong. And then they go into how cloud code navigates a codebase, at least before we have more of an AI layer. So the tool out of the box, it uses something called a gentic

**[0:02:08]** search. So we're not performing traditional rag or semantic search. There's no codebase indexing with cloud code. Instead, it's going to navigate a codebase more as an engineer would with command line tools like GP, just looking at the folder structure, using all of the command line tools at its disposal

**[0:02:26]** to identify the places for especially a larger codebase to pay attention to and where it needs to edit. And so this is really powerful because then there's no index that you have to keep in sync. But the tradeoff is that claude works best when it has enough starting context to

**[0:02:41]** know where to look. And so this really gets us into a lot of the strategies that we'll cover here. It's all about how do we curate that context up front so Claude can navigate a more complex codebase effectively knowing where to actually look based on the requests that

**[0:02:56]** we have for it. So that then brings us to the main point of this blog post that really sets the stage for all the strategies. The harness matters as much as the model. A lot of people get really hyperfixated on model benchmarks and they think that tools like cloud code

**[0:03:12]** and codeex the power really comes from how good the underlying large language model is. And yes, that matters. But honestly, what matters even more is the ecosystem built around the model, the harness. And I like to call it the AI layer. I think that's more descriptive. It's really everything that they lay out

**[0:03:28]** right here with quite a few paragraphs. I also have a nice diagram to make this even simpler. The AI layer is the set of context and tools that you give your coding agent to work on a codebase. And so, traditionally, a codebase would have two main parts. It would have the code

**[0:03:43]** and then it would have the tests. And so now with the AI layer, we have a third component of every codebase introduced. This is everything like your global rules, your skills, your MCP servers and sub agents. Really, every single individual feature of cloud code that gives tools or context that is a part of

**[0:04:02]** your AI layer. And so there's seven things that we have here. Couple you might not be as familiar with like LSP and hooks, but we'll talk about all of that because really each of these seven map to one of the strategies that Claude Code covers. This is where I have a

**[0:04:17]** concrete example for each of them. Let's get into this. So, the initial strategies that Enthropic covers are all about making it as easy as possible for Claude Code to navigate your codebase at scale. And a lot of it centers around the first and maybe even most important part of your entire AI layer, which is

**[0:04:35]** your global rules. So, take a look at this. They have this visual representation for how often the each part of the AI layer is used throughout a cloud code session. You can see that most of them are sporadic like your hooks and skills and the LSP for navigation. We'll talk about all these

**[0:04:52]** as well. But your global rules as your foundation, it is dictating the behavior of cloud code the entire time. So you better spend a good amount of time strategizing around your context curation here. And so their first tip is to keep your global rules lean and layered. Something that I see a lot of

**[0:05:11]** people do unfortunately is create these global rule files that are thousands of lines long. That is not a good idea. There are actually studies out there that prove that that can hurt your coding agent performance. Even if you think that being really specific and comprehensive helps, you're just going

**[0:05:25]** to overwhelm your LLM with context. You just need core information. What is the codebase about? Give it a little bit of an idea of the tech stack or architecture, for example. I mean, this is just an example that I have in this repo. Um, then your general conventions

**[0:05:38]** and gotas like what I have right here. Commands to run for things like testing and getting the dev server spun up. Like that's all you really need. So keeping it lean. And what Enthropic means by layered is you can actually have claw.md files in subdirectories. And so I have

**[0:05:55]** the main claw. MD at the root of my repository here. That means that whenever I start a clawed session like this, it is always going to have these rules loaded. But then as soon as I navigate in and start editing files in one of these subdirectories, it's also

**[0:06:13]** going to load in that claw.md automatically. So if I start working in the API service, for example, I'm going to load in my core rules or I should say those are already loaded. But then I'm also going to load in the API service rules that I have in the separate

**[0:06:27]** claw.md. So I'm building up the list of conventions based on where I'm actually operating in the codebase. It's like the idea of progressive disclosure that we have with claude code skills. This is really powerful because if you have a massive codebase, you're going to have a ton of conventions, but most of them are

**[0:06:44]** going to be specific to certain slices of the codebase. So, let's just load in the conventions we need depending on where we're working because whenever you have some kind of GitHub issue or GR ticket or whatever, hopefully it's scoped to a very specific part of your codebase. And then another thing you can

**[0:07:00]** do if you're really confident where you need to work in a codebase is you can actually initialize cloud code in that subdirectory. So if I know for example that based on a Jira ticket or GitHub issue I'm only going to be working in the API service then I can you know

**[0:07:15]** rightclick in VS code copy my path and then within here just for the sake of example I guess I'm already there but I can change my directory to that path and then I can open up claude here. And the power of this is now this is the current

**[0:07:28]** working directory for clawed code. So unless I tell it to, it's really going to stick to editing files in just this directory. So it'll load the claw.md here. And then it still will load the rootclaw.md. So you can see that it does automatically walk up the directory tree

**[0:07:44]** and load every claw.md. So the root context isn't lost, but we're just honing claw code in on that part of the codebase. And so basically you're doing the navigation here. So the rest of their strategies are like you know how can you help Claude navigate things effectively but most of the time

**[0:08:00]** especially if you are an engineer you know where to start. Now if you don't know where to start that's where this strategy comes in building up some kind of codebased map when the directory structure doesn't do the work and this usually I put in my global rule. So, I

**[0:08:15]** don't have it in this example here, but often what I'll do is I'll have a section that outlines the directory structure, like all the subdirectories, maybe like a brief description of each of them. That way, Claude can help me do the discovery, help me figure out what slice of the larger codebase to focus on

**[0:08:32]** based on the work that I have. So, usually it comes down to Claude's going to help you figure that out or you're just going to immediately know and initialize Claude code there. The sponsor of today's video is Jet Brains Academy. Now, I've tried a lot of AI courses in the past, and most of them

**[0:08:48]** have this problem. The way that I'd put it is that the course ends where the real work actually begins. And what I mean by that is you'll go through some material and some really basic exercises, but then you don't get to really deploy anything. And Jet Brains Academy is different with their skill

**[0:09:04]** paths. Here, when you learn a concept, you get to apply it to a real project immediately. And so you do your work and go through the lessons in the IDE and then you get to right away deploy what you've built in AWS sandboxes. So you start by picking a path. Let's say we

**[0:09:20]** want to do build and deploy custom LLMs with Python and AWS. It seems very relevant right now. And so we have the course layout here. This is the syllabus. And you can see that each of the sections, it'll open the course in your PyCharm IDE. So we get to go

**[0:09:34]** through the material where we're doing all of our coding already. The AI assistance is built right into the IDE. I can navigate through the lessons and go through all the material right here really easily. And then as I'm doing my exercises, it's just right here in the IDE. So, I get to code as I normally do.

**[0:09:50]** And then when it comes time to run and deploy things like the fine-tune model that we have in this lesson, we get to do it in an AWS sandbox. This is not a mock. It is running in the cloud, but it's fully prepaid. You don't need an AWS account. This is what I wish I had

**[0:10:05]** when I was learning how to build and fine-tune models. So, when you finish a skill path, you have real projects deployed live that you can host on GitHub, talk about interviews, and get hired for, and you have certificates both from Jetrains and AWS to back it up. So, if you're looking to build

**[0:10:20]** proficiency and credibility with Generative AI and LLM engineering, I would highly recommend checking out Jetrain Academyy's skill pads. I'll have a link to them in the description. Cool. So there are some more strategies to cover here like scoping your tests and lint commands per subdirectory, ignoring certain files like build artifacts so

**[0:10:37]** your coding agent never reads them. But I want to move on now to talk about the next part of the AI layer and that is hooks. And you'll see in a second why I want to cover this right after global rules. So you can use hooks to make your

**[0:10:51]** entire AI layer, your entire setup self-improving. This is really, really cool. This is part of the goal that I was talking about. So most teams think of hooks as scripts that prevent Claude from doing something wrong. So a lot of people use hooks like a pre-tool use hook to stop Claude from editing in

**[0:11:08]** certain directories, removing files or folders, that kind of thing. But their more valuable use is continuous improvement. And so take a look at this. A stop hook can reflect on what happened during a session and propose claw.md updates while the context is fresh. Right? so that the hook runs at the end

**[0:11:27]** of the session. And I have a live demo of this. I'll show you. I actually built out both of these hooks here. And then a start hook can load team specific contexts dynamically. So every dev gets the right setup without manual configuration. So based on the role or

**[0:11:41]** the part of the codebase they're editing, we can have a hook that will even go out to confluence for example and pull documentation for that team, that function, that part of the codebase, whatever. So I have actually a pretty basic example of that here. And so I have a hook. And so you can see in

**[0:11:58]** my settings.json, this is where I have the start and end hooks defined. So propose claw.md updates for the stop hook. And then the session start context for the start hook. And so what this hook does, this is just more of a basic example, is it's going to load context

**[0:12:15]** around git. And so any kind of unstaged changes that I have like a change to this file here looking at the git history as well. So take a look at this. If I go into claude and I start a new session and then I say what did the

**[0:12:27]** start session hook tell you about this session. Obviously it's a little cheesy but just to show you that it loaded the context. We have this orientation here. The working tree is clean. Here are our recent commits, right? And so like this is just giving it some context going

**[0:12:42]** into like here is what we're currently working on and here is what we worked on recently. And you could extend this like I said to pull things from Confluence based on the developer that is starting Cloud Code. There's a lot that you can do here. And then take a look at this to

**[0:12:54]** demo the stop hook for you. I'm going to give a really simple request for something that I want to change. Obviously if I was doing work for real I go through more extensive process of planning and implementing and validating. But here I'm just asking it to make a simple change so that I have

**[0:13:10]** something to then propose a change to the global rules because something really important that you need to do and you can see that the process actually ran here in order to propose some changes. Something that's really important to do is as you're evolving your codebase you need to make sure that

**[0:13:25]** your rules are evolving as well. It's really really bad when your claw.md goes stale because you made some changes in the codebase where it kind of you know dictates something needs to be added to the global rules or something has to be updated. And so that's why it's really

**[0:13:40]** powerful to have this kind of process that automatically proposes these changes. So take a look at this. This hook runs whenever Claude stops. So whenever it's done with its turn. So you saw that terminal pop up for a little bit. It runs a separate cloud session in headless mode to look at these changes,

**[0:13:58]** look at the global rules and propose if anything needs to be tweaked. And so it outputs that in a markdown document. Take a look at this. I have my claude markdown review. And so we have the reflection that just ran right now. Here are the two areas that were touched. So

**[0:14:13]** it's going to look at those subdirectory global rules as well. And here it decided no changes needed. Adding a trial enum value follows the existing model only convention. So the thing that we really care about at a high level still holds up based on these changes. And so maybe it's not the best example

**[0:14:29]** because it didn't decide to change anything, but I think that's also really powerful because usually we don't need to change our claw code or claw.md conventions. That's especially why we keep these files so lean. But maybe for example, I could say, you know, make a change that would require updating the

**[0:14:44]** claude.md. So I'll come back and see what it does with this. And so there we go. We had it change something bigger in the billing service. And now in our markdown review, it is recommending making an update to the second bullet in the claw.md for our billing service

**[0:15:00]** subdirectory. Pretty neat. So now we can take these recommendations and we can action on it ourselves. We can have a conversation with a separate claude session to make these changes. It's up to you how you want to take this forward. The power I'm just trying to show you here is we can have this

**[0:15:14]** self-reflection process constantly running in the background making these suggestions that we can a you know just action on when we're actually ready to. So the next part of the AI layer that Anthropic focuses on here is skills. And you probably know what a skill is. They've been blowing up all over the

**[0:15:30]** internet the past few months. It's really like the main way to extend cloud code right now with new workflows and capabilities. And so like this is an example of a skill right here for adding API routes in this codebase. Really a skill is some kind of set of steps, some

**[0:15:46]** kind of process reusable prompt that you have for clawed code. And these are really important in large code bases because you're going to have dozens or maybe even hundreds of task types. Like this would apply to a task type of building an API endpoint. And so not all

**[0:16:02]** expertise needs to be present in every session which is the same reason why we have different claw. MD files in subdirectories which there is definitely some overlap here that I'll talk about in a second. And so skill solve this through progressive disclosure. So we're offloading specialized workflows and

**[0:16:18]** domain knowledge and we load it when we actually need it. So that way we're not bringing in prompting and workflows for things that don't apply to the current task at hand. And so when we define a skill we have the name and the description. The description is what is

**[0:16:33]** given to the coding agent right away. And if it decides like, okay, based on the description, I should use this skill, then it'll read the full skill.md file. I've talked about skills a lot on my channel already. But the parameter that most people don't know about, and this is what Anthropic talks about right

**[0:16:50]** here, we can make it so that skills can be scoped to specific paths. So they only activate in relevant parts of the codebase. Like we know that this process for adding API routes that we want to be very repeatable. It only applies when we're going to be reading and editing

**[0:17:06]** files in the API services directory. And so we can scope it there. Really, really powerful. It's a way to basically enforce that like when we touch this part of the codebase, we're going to bring this convention, this workflow into the session context. And so like I said, there is a little bit of overlap

**[0:17:23]** here with that and the subdirectory claw. MD files, right? like we're loading this in only when we work here. Same thing when we operate in here, we're also going to read this claw.md. The distinction that I like to make is that global rules are your conventions. It's the rules that you need to follow.

**[0:17:40]** Like every route is registered here, for example. Your skills are the workflows. So, we have rules and we have workflows. So, that distinguishment kind of helps me understand the overlap. But really for a lot of these sorts of conventions, you can kind of do it as a skill or a

**[0:17:57]** claw.md. The more important thing here is we just want to scope these conventions and rules to the part of the codebase where they actually matter. So we're not overwhelming our coding agent with context it doesn't care about. So Anthropic talks about plugins next, but I'm going to cover that at the end

**[0:18:12]** because I'll show you how to use my plugin to incorporate all these ideas in your own codebase. So let's move on to talk about language server protocols. I'm excited for this because I just started incorporating this into my own cloud code ecosystem. It's really powerful. Essentially, you give Claude

**[0:18:29]** the same navigation that a developer has in their IDE. And a lot of bigger companies especially build own custom LSPs to really help Claude navigate through their codebase effectively. And so an LSP is something that is really built into any IDE by default. It's the kind of thing that allows you to know

**[0:18:46]** like in VS Code, I can control-click here to immediately navigate to the definition for the class that I used in this other file. So that kind of like type hinting and navigation and highlighting like all that is an LSP. And so essentially with an MCP server, we can give cloud code this exact

**[0:19:06]** functionality that we as the engineers have in our IDE to make it so that we have better search capabilities than just GP by itself or can complement some of the tools like GP that are built into cloud code natively just through the CLI commands that it has. And so what I

**[0:19:22]** built here, I'm actually kind of knocking two birds with one stone because they talk about LSP and then talk about MCP servers as a way to extend everything is I built a local MCP server that comes with this codebase. It comes with the plugin that I'll cover in

**[0:19:36]** a little bit as well that gives Cloud Code some new codebase search capabilities. And so take a look at this. I'm going to go into a new Cloud session here. If I do SLMCP, you can see that I have the codebase search enabled. There are three tools here to complement

**[0:19:52]** the search capabilities that I already have. And so I'm going to paste in a prompt find every place that monthly total sense is referenced in this repo. And I know that's like oddly specific, but that's the point is we need something very specific to search for here. And I'm telling it not to use GP

**[0:20:07]** just for the sake of the demo. I'm telling it to use a symbol level approach. And that's going to key in that it needs to leverage the MCP server that I built here that leverages the language server protocol. So, it's able to do more intelligent searches that it

**[0:20:21]** might figure out it needs to if I don't tell it to not use GP or you could just, you know, build in some instructions in your global rules for how you want to use these searches. But you can see here that it used my whereas and find references tools in my custom MCP

**[0:20:34]** server. And so here are the results. We have one definition and two references. Pretty cool. So I I know that like I'm talking about complex code bases here, but my demo is kind of simple in the end, but I kind of have to have that balance there of like a somewhat

**[0:20:48]** complicated codebase, but still it has to be easy to like parse through and show the results here. But that's an example of using an MCP server to expose a language server protocol. And really for massive code bases once you get like into the six digits for lines of code

**[0:21:06]** you need something like this because Grep by itself is going to be slow and really token inefficient as you're trying to navigate through a codebase. This is a lot more of a directed search looking for things like the definitions and references for things like classes and variables. So that's a quick

**[0:21:23]** overview of LSP and MCP and how I use them together. You got to have some kind of harness to give better search capability to cla code when you're working in larger code bases. And really they operate like skills just use sporadically throughout your session. So like with skills we're loading in

**[0:21:39]** instructions when we need those conventions or workflows whatever LSP whenever we need to perform those searches to find definitions references things like that we'll call upon the tools. MCP pretty similar, right? Like we need to perform a search, take some kind of external action. We call upon one or multiple tools for an MCP server

**[0:21:57]** at that time. Now, the last part of the AI layer that we still have to cover is sub aents. But this one's nice and simple. The the advice anthropic has here is simple, but still really powerful. We want to use sub aents to split exploration from editing. So the

**[0:22:12]** idea with a sub agent is that we send in a task like we wanted to search the web for you know best practices for this kind of architecture or maybe to do some kind of codebase exploration to find the part of the codebase to focus on. We send in a task and it runs with its own

**[0:22:30]** context window. It does all the analysis it needs to and then it returns a summary back to our primary cloud code session to reason about an action on. And these kind of exploration tasks that we want to give to a sub agent, you can imagine them getting to hundreds of

**[0:22:47]** thousands of tokens. So if we're not using a sub agent and we have our primary cloud code session do that web research or codebase exploration, by the time we get to the actual editing, we're already going to have this extremely bloated context window. That's why we want to dispatch the work to the sub

**[0:23:02]** agents. Especially because with exploration, usually all we need is that summary back, right? Like here are the recommendations for the tech stack. here's a part of the codebase we're going to have to address based on this Jira ticket. Like that's the kind of thing that you task a sub agent with.

**[0:23:15]** And so I don't actually have that much of a demo here for sub agents because I use them liberally like all the time especially at start of the conversation. I'll say something like I want you to spin up three sub agents here. One to research the database, one the back end,

**[0:23:29]** one the front end. Help me figure out how I can add in authentication. I don't know. I'm just kind of throwing off something off the cuff here. But you have sub agents built into a lot of these coding agents now like cloud code and codeex. And so you don't even have

**[0:23:41]** to define your own custom sub aents like a lot of people did before. You just send off a request like this. And now it's just going to use the explorer sub agent that we have built into cloud code. And so it takes care of that whole like dispatch getting the summary back

**[0:23:54]** and everything. All right. So the rest of the article that we haven't covered yet is really covering a lot of the strategies that I already hit on like writing LSP servers so cloud can search by symbol not by string. talking about actively maintaining the claw.md file. So this is where the stop hook comes in

**[0:24:09]** to make those recommendations as we're operating with claude code. The other thing that I want to hit on here is the plugin that I have for you. So if you go to the read me for this demo repo that I'll link to in the description, I have instructions for taking this to your own

**[0:24:26]** codebase. Now, obviously, some of the things like the claw.mds and the subdirectories are specific to me, but this plugin is going to give you the self-improving stop hook, the explorer sub aent, so it's more of like a custom sub agent that I built that you can use, and it's going to give you the codebase

**[0:24:40]** search MCP server with that LSP. So, you have that whole searching harness. And then I'm going to give you a more generic skill that you can use in as an example that shows what it looks like to use that path parameter to scope a skill to a certain subdirectory. So just kind

**[0:24:57]** of consider this plugin a starting point if you want to like really quickly pull in these things to experiment on your own codebase. You can install this plugin on any codebase, even one that you already have built out with its own AI layer already. So all you have to do

**[0:25:10]** is slash in cloud code /plugin marketplace add and then give the path to the repository. So you still have to clone this repo locally because I don't have this hosted in npm. So you give the path and then make sure you add the tooling folder at the end. And then you

**[0:25:24]** just do plug-in install helpline AI layer at helpline tooling. Then you go through the whole installation process here and then boom, it'll install all these things for you to start playing around with. So that's one way to do it. I just wanted to add a plugin to make it

**[0:25:36]** really convenient. The other way to get started with a lot of the ideas that I have here, aside from, you know, reading the anthropic blog post, is just to clone this repository, point your Claude code at it, you know, like copy this directory, you know, rightclick, copy path, give this to Claude Code, and say,

**[0:25:52]** "Hey, these are a bunch of cool strategies Cole shared with me for working with complex code bases. Help me understand how they work and how I can incorporate it for my codebase." That's always the easiest way to really take any repo these days is just give it to

**[0:26:05]** cloud code and have it uh help you understand it and apply it. So that'd be my recommendation for getting started here. So I hope that you found these strategies really useful that you can apply them right away to your larger code bases. Even if you had some of

**[0:26:19]** these things incorporated already, I hope there are some good golden nuggets for you. And so the last thing that I want to end on is talking about some really good advice that Enthropic also gives at the bottom of their article here. It's all about assigning ownership for cloud code management and adoption.

**[0:26:34]** And I've been around a lot of companies as I've done my consultings and trainings. I know this is really good advice. Essentially, what they're saying here is to have a an individual or more likely a smaller team to champion the initial buildout of the AI layer for your organization.

**[0:26:51]** And so what that looks like is you start with a quiet investment period. you have a couple of people that build out the the rules and skills and the LSP and the MCP servers, the whole AI layer for the organization and then roll it out to people over time. And the power of this

**[0:27:06]** is you get to create something that's really foundational for everyone to adopt together and then people can get more consistent results with Cloud Code or whatever coding agent faster so that they're not disappointed when they first use the tool. You want to avoid people being really disappointed when they

**[0:27:23]** first use it because they don't have an AI layer and you want to avoid everyone evolving their own separate AI layers when really you want a standard for the organization. So really really good advice that they have here. This is also something that I help with and so I do

**[0:27:36]** offer enterprise trainings where I help you build up the AI layer, understand the core methodologies for AI coding and create that standard for your adoption of coding agent tools like cloud code. So definitely I got my email in my bio. Reach out to me if you're interested in

**[0:27:51]** that. Otherwise, I hope that these strategies were useful for you. I appreciate you going through everything here. Let me know if you have any questions in the comments below. Otherwise, if you appreciate this video and you're looking forward to more things on AI coding and cloud code, I

**[0:28:05]** would really appreciate a like and a subscribe. And with that, I will see you in the next video.
