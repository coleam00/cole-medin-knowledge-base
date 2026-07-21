---
type: raw-transcript
title: "I Built Self-Evolving Claude Code Memory w/ Karpathy's LLM Knowledge Bases"
youtube_id: 7huCP6RkcY4
url: https://www.youtube.com/watch?v=7huCP6RkcY4
slug: i-built-self-evolving-claude-code-memory-w-karpathys-llm-knowledge-bases
published: 2026-04-06
duration: "0:19:24"
fetched_at: 2026-07-21
immutable: true
---

## Transcript

**[0:00:00]** Let's face it, every week you and I are playing the game, what's the latest and greatest in the AI space, right? It changes every single week. And right now, everyone is focused on LLM knowledge bases, which originated from this tweet from Andre Karpathy. And there are a lot of really cool ideas

**[0:00:17]** here that I want to get into with you. And I built my own memory system on top of this. I think you're really going to like it's simple, but super effective. So, more on that in a bit, but let's get into a bit of context here. So Karpathy

**[0:00:29]** starts by saying something I'm finding very useful recently is using LLM to build personal knowledge bases for various topics of research interest. So taking external information bringing it into our own system and organizing it in the best way for agents to query. And this is a big use case for AI second

**[0:00:48]** brains right now which is something I've been focusing on a lot recently. And I love seeing that he's using Obsidian as a core part of his stack. I always call it my canvas for working with things with my second brain. So cool to see that. And he really gives us his entire

**[0:01:02]** playbook here. It's nice and simple. So he talks about how he brings in information data ingestion, how he views it, how he queries it, how he formats it, health checks that he's built in as well. And so I want to cover this entire architecture here and that'll guide us

**[0:01:16]** into the custom solution that I've built on top. And I'm excited to show you this because here's the thing. This entire thing that he's presenting is working with external data which there are a lot of use cases for that. But what I've built here is working with internal

**[0:01:31]** data. So giving claude code a memory that evolves with your codebase. So basing the whole LLM knowledge base on our conversations with our coding agent or second brain instead of bringing in external data. But I've structured everything in exactly the same way. all of the optimizations for how we index

**[0:01:49]** and create systems for our agent to explore the information. It's really cool. So, let's get into the infrastructure and then I'll show you how you can use this to evolve any codebase. And yes, cloud code does already have a memory system built in and there are open- source solutions out

**[0:02:04]** there already for claim memory. But I wanted to build this specifically because I am following everything Harpathy laid out here to a tea just for internal instead of external information. It's a lot simpler than other approaches already out there and I would argue even more effective. You'll see what I mean when we get into it. So,

**[0:02:22]** something really interesting that he says at the top here is he's spending more of his tokens with his agents manipulating knowledge like Markdown and Obsidian instead of manipulating code. But he works with knowledge in a very similar way that we work with code. That brings us to the compiler analogy. This

**[0:02:39]** is the simplest way to explain everything that he's built in the system here because the way that we're handling knowledge is very similar to how we take source code all the way into a final application for the end user to run with a compiler. And so let let's take it

**[0:02:54]** from the top here. So we start with our source code which for the case of our LLM personal knowledge bases, it's our articles, papers, anything that we are finding online that we want to bring into our system. So I'll go to the Obsidian vault because this is what

**[0:03:08]** Karpathi uses. This is what I use for my AI second brain. We have the raw folder here. This is the entry point into our system where we'll dump anything articles papers transcripts everything just as raw markdown. And then we'll take that and move it into the compiler stage. This is where we

**[0:03:24]** have a large language model process all this raw information. So creating summaries, linking documents together, just generally figuring out how to structure our knowledge. And for the system that Karpathy has designed here for the compiler, we do actually have scripts. We have code that takes our raw information, gives it to an LLM to

**[0:03:44]** produce the wiki here. So that brings us to the next step. The compiler goes to the executable. This is what we run or in the case of our personal knowledge base. This is what we query. So he calls it a wiki. This is where we have our compiled articles, everything produced

**[0:03:58]** from the large language model and we have the back links. We are connecting pieces of knowledge together. So going back to Obsidian again, we have our graph view. This is one of the coolest parts of Obsidian where we can see how our different pieces of knowledge, our different markdown documents are

**[0:04:14]** connected together through back links. And this is powerful because it gives our agent the ability to traverse through the graph to search better and even connect different pieces of knowledge together to give us a more comprehensive answer. So this is what we run. This is what we search. But before

**[0:04:31]** we actually get to the final step with the runtime, we also have a test suite to continue with the analogy of code. Here we are performing linting. He calls it linting over our documents. So we're finding gaps where maybe we need to do more research. Any kind of stale data,

**[0:04:47]** things that maybe we have in our raw folder that aren't actually in our wiki yet and we need to take care of that discrepancy. any kind of broken links. Like if we have one document linking to another that doesn't exist, we're going to take care of all of that. And so

**[0:05:00]** we're even going so far in this system as to making sure that our data has integrity. That's pretty important. We want to have an accurate personal knowledge base. And then finally, we get into the last step here where we are running queries, right? This is the runtime where we are taking advantage of

**[0:05:17]** our wiki, having our agents search through it to find information for what we are currently working on. And the really interesting thing here is Karpathy said, "I thought I had to reach for fancy rag, but the large language model has been pretty good about automaintaining index files." And so one

**[0:05:32]** of the most important files in this entire setup within the wiki, we have the index. So this file describes to the agent here are all the different folders and resources that you have access to. So it uses this as a starting point. So we don't even have to do fancy rag. The

**[0:05:48]** agent can just navigate through all the files that we have as marked on in our obsidian vault. It doesn't have to do any semantic search. There's no vector database here. It's nice and simple. It's one of the beauties of this strategy that really drew me to build on

**[0:06:02]** top of it. Okay, so let's now go from the compiler analogy to the exact data flow. I think this will really take it home for you. Then we'll get into my implementation that I built on top. I'll talk about how it relates to all these ideas here. So, okay, we start with our

**[0:06:16]** external information, and Carpathy specifically calls out the Obsidian Web Clipper. It's a really neat extension to Obsidian that allows us to very easily take anything from the internet and bring it directly into our vault or in this case, right into our raw folder, the source of truth, like we talked

**[0:06:34]** about earlier, the unprocessed markdown that we feed that into the large language model to create our wiki for us. And so, I've built up a simple example here for demonstration. My raw folder just has some different articles on AI topics. And then within the wiki, this is what is processed. This is what

**[0:06:50]** our agent actually queries. We have this concepts folder and this is where we tie everything together. We're taking ideas, concepts out of our raw documents. And we also have connections, how different things are relating together. And then of course we have the index. This is the main file that we want our agent to

**[0:07:07]** always have access to so that it has a highle idea of where it's going to start looking based on our question. And then the last thing that we have here is the agents.mmd. So this is like global rules for your coding agent, right? And so really what we do in our global rules

**[0:07:22]** here is we're describing the entire system for LLM knowledge bases so the agent understands here's where my information comes from. Here's the compiled version that I'm going to search. Here is the index and the log file, right? Like the entire system we explain to the agent. So it has that

**[0:07:39]** meta reasoning. It understands what it's been dropped in. When you start a new session with your second brain or coding agent, whatever it is. And the best part is if you want to build this entire LLM knowledgebased system for yourself, all you need to do is send this prompt into

**[0:07:55]** your coding agent. It could not be simpler. So this came directly from Karpathy. He had a follow-up tweet where he linked to this. This is essentially a PRD, right? A product requirement document that outlines everything we have to build for you to include this system in your own coding agent or

**[0:08:12]** second brain. And so you just prompt this in no other context and it's just going to oneshot the whole thing for you. And that's what I built into my version as well. If you look at the readme here for the quick start, you don't even have to clone the repo

**[0:08:25]** yourself. You just send this prompt into your claude code, clone it, and then set up everything with the claude code hooks, everything that I have to make this LLM personal knowledge base, but for internal information instead of external. So, inspired by the entire architecture we just covered here, but

**[0:08:44]** that's the key difference is now this is giving Claude code a memory that evolves with your codebase. So, instead of taking things from the internet, we are going to automatically capture session logs with hooks. And so session logs are kind of like the raw folder where we're just putting in our conversations and

**[0:09:01]** then we're going to use the claude agent SDK behind the scenes to automatically extract everything into structured cross reference knowledge articles. So your coding agent like you can do this per codebase. It's going to get smarter and smarter over time because it remembers the decisions you've made and how you've

**[0:09:18]** evolved your project. The sponsor of today's video is InsForge. Insorgge is an open- source platform that gives your coding agent everything it needs to ship full stack apps. Think if you had Verscell, Superbase, and Open Router all in one platform. So we have a database, we've got authentication, storage, we

**[0:09:37]** can route to 50 different large language models. We have hosting as well. It is everything you need. And we give our agent the ability to manage all of this through a CLI and an agent skill. And take a look at this. It literally takes less than 5 minutes to install the

**[0:09:50]** InsForge CLI and skill on any codebase. And then I can go into cloud code and prompt it to create an application. So here I'll have it make both a backend and a front end. And I'm specifically asking it to use infors to create my database table, set up authentication to

**[0:10:05]** host it as well. Once it goes through this entire process here, then we end with a hosted application. What I'm showing you right here is a live URL. And I have authentication set up. So I can even demo this here. I created an account off camera. I'll sign in. We

**[0:10:20]** have access to our database behind the scenes. So, this is not just local storage, a hosted application, live database. I can even use an AI model to recommend a task for me here. So, showing off the AI part of InsForge as well. We have got everything running and

**[0:10:33]** we didn't have to configure anything oursel. Insource and free to get started. Plus, you can use promo code ins promo for a free month of pro. I'll have a link in the description. So, seriously, you should just try this right now. Open up Cloud Code in whatever codebase you're

**[0:10:48]** currently working on, your second brain, Open Cloud, whatever, and just send in this prompt. It'll immediately level up the long-term memory for your coding agent when it's working on that project specifically. We're building up lessons and takeaways for this codebase. And so, I have the repository cloned locally.

**[0:11:05]** I'm just going to work within it directly to give you an example here, but you're going to use this prompt to bring it into wherever you are already working. And so you don't have to do this, but I would recommend starting with an Obsidian vault. It's our canvas

**[0:11:17]** to view all of the memories and the whole wiki that we create with Claude Code. And so you'll open a folder as a vault. Once you have Obsidian installed, it's free and super easy to install. So I'll open here and you just have to give it a path to where wherever you have the

**[0:11:32]** code base that you've brought in this system. So I'll just select this folder right here. That'll create a brand new Obsidian vault. I usually like to make it look nice as well when I first create a vault. So, I'll go into the settings in the bottom left. I'll go to

**[0:11:44]** appearance and then manage to select a theme. They got a lot of really awesome ones. Obsidianite is my favorite. So, I will click install and use. And then I usually like to switch to the dark theme as well. There we go. Now, it looks like the other vault I showed you earlier for

**[0:11:58]** a demo. And so, this is where we're going to manage the daily logs. I'll talk about this in a second. And then also, this is our wiki equivalent where we have our index. I mean, everything. This is exactly what Karpathy has set up with the concepts and connections

**[0:12:13]** everything that we use a large language model to process from our raw input. So this entire system is only driven by claude code hooks. That's the beautifully simple part about it. That's why all you have to do is send in this prompt to get everything set up for your

**[0:12:27]** codebase where you run cloud code. We don't have to install anything else. We don't have to set up any integrations. And so going to our settings.json, JSON. This is where you always define your hooks for cloud code. I want to at least at a high level show you how everything

**[0:12:41]** works here. I think it'll really click for you. So, we start with a session start hook. And so, this is going to run whenever we start a new cloud code session. And all we're doing with this simple Python script is loading in the agents.mmd. We covered this earlier.

**[0:12:56]** That's so our cloud code understands the system that we put in it. And then it's also loading in, if we go into the knowledge, this is our wiki equivalent. We're loading in our index.mmd. You've already seen this as well. This is our actively maintained list of files. So

**[0:13:10]** our agent can query more efficiently. And so whenever we begin a new cloud code session, it has both of those things already. And so now I can ask a question just for demo purposes. I have a knowledge base already built up for a project. And so I'm asking something

**[0:13:25]** that it wouldn't really know by itself without having to do deep analysis in the codebase. But right here, it's just going to rely directly on what we have in our knowledge base. Take a look at that. Based on your knowledge base, here are the key things to watch out for.

**[0:13:38]** Then some technical details we don't have to cover here. But then it calls out the specific KB articles that it referenced in order to get us this answer. And so the index told it where to point. It ran some queries that we'll talk about in a little bit. And it

**[0:13:52]** pulled things from our knowledge. And so again, we have the equivalent of our raw folder with our daily logs. This is where we're going to capture summaries of every single conversation with cloud code. I'll show you how we do that with the other hooks in a second. So, daily

**[0:14:06]** logs, that's our raw equivalent. And then we have our wiki. This is where we have the things that are better formatted, linked together. We have the whole graph view here in Obsidian. This is what our agent is searching through. And I know this is a really basic example here, but just like think for a

**[0:14:21]** second how powerful this actually is. If I asked this question without this whole system built in, it would have had to look through the git log and even that might not have had the lessons for what to watch out for. It would have had to spin up sub aents to look through the

**[0:14:34]** codebase, which would be painfully slow, especially if the codebase was bigger. But since we're maintaining takeaways from all of our conversations with cloud code, I was able to get this answer in like 10 seconds. You saw it happen live. And so the other really powerful part of this entire system is the other two

**[0:14:51]** hooks. We have a pre-ompact and a session end. And they're both actually doing a very similar thing. Whenever we're about to lose context, either through closing off a session or doing memory compaction, we want to send the latest messages from cloud code into another large language model to process

**[0:15:10]** and create the summary. And that summary is what we're going to put in the daily log file. So like this is the summary from one conversation, you know, decisions that were made, lessons that were learned, action items, and then we go on to the next session. We have a

**[0:15:22]** very standard format here handling every single Claude code session. And the way that this works is this hook, actually both of these hooks, they are going to call the Claude agent SDK under the hood. So we have a separate Claude process running where it's just given the transcript from the conversation and

**[0:15:41]** it summarizes things here. So, we're doing that initial layer of data processing. And not to get too technical here, but one other really powerful part of this is we have the flush process. And so once a day, we're going to take the logs, we're going to extract the

**[0:15:58]** concepts and connections from them. And then that's what we populate in the wiki. And then our search is going to focus here in knowledge, but then it can also look through the daily logs if we want as well. So we have full information about everything here. lessons learned, decisions made. If you

**[0:16:13]** want to customize this, you can even go into the scripts here. You can go into the flush or you could go into the compile and you can actually change the prompt that we send into the cloud agent SDK under the hood. So, another beautiful part about this whole setup,

**[0:16:28]** unlike Claude Code's memory system, is you can customize this to your heart's content. And Claude Code can even walk you through making the customizations because it has access to the agents.m MD. It knows how everything works. It knows where the prompts are. It knows how the memory promotion process works.

**[0:16:44]** It knows where the daily logs are. So, it's very it's a very self-contained system that can improve itself. And speaking of improving itself, that's actually the last big thing that I want to cover with you. I want to talk about the compounding loop. Cuz think about this with me for a second. We always

**[0:16:58]** will start by asking some kind of question. We want to leverage our knowledge base. We're going to get some kind of answer with our agent searching across many different wiki articles. So it's extending its arm across our knowledge base, synthesizing information together, but then it's going to file

**[0:17:14]** that single answer. So we're constantly connecting information between our conversations and saving that. And so our wiki grows over time because of that. And then also all the new information coming in from all of our future Claude code sessions. And so we're building up our knowledge base over time. The agent is going to be able

**[0:17:32]** to search through our knowledge better over time. As we ask more questions, it just gets better and better and better. And we really don't have to do anything to maintain this. For example, if I extend the conversation where I asked our first question here to have it do

**[0:17:47]** more web research, I have more takeaways. All I have to do is end this session or do a memory compaction and then automatically we can see that the logs are I saw this just come up here. We already have the cloud agent SDK running in the background. It can use

**[0:18:01]** your anthropic subscription just like cloud code. You don't have to set up any API key or anything and it's automatically going to extract takeaways and put it in our daily logs. Let's actually look at this right now cuz I believe it already finished. There we go. Take a look at this. So this is our

**[0:18:14]** session that just ran. We were exploring best practices for handling external service data and then we have these key exchanges lessons learned from our additional web research. We're building this up over time. It'll eventually get promoted into our wiki here. We don't have to do anything and the questions

**[0:18:31]** that we ask our agent are just going to get better and better answers over time. Very very powerful. So there you go. That is LLM knowledge bases for internal data long-term memory for our second brains instead of external data like Karpathy's implementation. But of course, thanks to him for all of the

**[0:18:48]** inspiration here. And Claude Code Hooks is something I've been building into my second brain for a long time now. And so I recently did a 4-hour workshop in the Dynamis community where I showed everything. I actually built my second brain again from scratch. And so definitely check out the Dynamus

**[0:19:04]** community linked in the description and pin comment if you're interested in building your own second brain on top of Cloud Code and the Cloud Agent SDK. Otherwise, if you appreciated this video and you're looking forward to more things on building agents and second brains, I would really appreciate a like

**[0:19:20]** and a subscribe. And with that, I will see you in the next
