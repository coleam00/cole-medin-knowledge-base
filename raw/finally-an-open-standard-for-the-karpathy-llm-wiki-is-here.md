---
type: raw-transcript
title: "Finally, an Open Standard for the Karpathy LLM Wiki is HERE"
youtube_id: T33iI6izAKw
url: https://www.youtube.com/watch?v=T33iI6izAKw
slug: finally-an-open-standard-for-the-karpathy-llm-wiki-is-here
published: 2026-07-01
duration: "0:19:39"
fetched_at: 2026-07-21
immutable: true
---

## Transcript

**[0:00:00]** A couple months ago, Andre Karpathy released the idea of the LLM wiki. It's a pattern for building personal knowledge bases using LLMs and it totally took off and for good reason. There's a lot of power in the simplicity here. So, this single markdown document in GitHub called it gist got to 40,000

**[0:00:19]** stars. And seriously, you can take this file, copy it, paste it into your coding agent, and ask it to build you an LLM wiki and it's going to be able to just basically oneshot it. So, it's really easy to get started. And the idea here is when we're building a personal

**[0:00:33]** knowledge base for our second brain, instead of just dumping in a bunch of documents or indexing things for rag, we can have the LLM help us build something smarter, incrementally building and maintaining a persistent wiki with structured interlink collections of markdown files. And so the idea here is

**[0:00:50]** as we're adding in more sources over time like meeting transcripts, plan documents, articles from online, it's going to not just index it, but it's going to read each file, extract key information, and integrate it into the existing wiki. So updating things like the entity pages that it creates over

**[0:01:07]** time, so we have that knowledge graph for agent to traverse through and remember all the important information that we're bringing in. So, at this point, pretty much everybody is building their own LLM wiki in their second brain. But this isn't enough. And the main problem that we have here is when

**[0:01:23]** you take this gist and you build your own version of an LLM wiki, it's going to be structured differently than the next person doing the same thing. There's no standard. And so, there's really not a way to share your LLM wiki with someone else. And that's a bummer.

**[0:01:37]** You can think of a lot of different use cases where you'd want to curate a knowledge base over time and then share it with other people like other people on your team. Maybe you want one wiki for the team that everyone's second brains are accessing independently. Maybe I want to create a wiki for my

**[0:01:52]** YouTube content and then share that with you. There are a million reasons. But if your agent doesn't know exactly how I've structured my wiki with the different metadata and my entity files, it's not going to be able to search through it optimally. We need a standard so that

**[0:02:06]** everyone's building wikis in the same way so that we can share them freely. And so that is what Google has released here with their open knowledge format. It is a beautifully simple thing just like Harpathy's LLM wiki idea where it's just a simple standard built on top so

**[0:02:23]** that you can guarantee you're building your wiki in a way where other people's second brains can understand it and vice versa. And so in this video I want to cover why OKF is so powerful. It really is the future of personal agents. And I want to show you how easy it is to get

**[0:02:38]** started with this standard, both for new LM wikis and even transferring existing ones into this format. Very easy to do that. And no matter the wiki, no matter how much you're going to share it or not, this is important even as an optimization on top of Karpathy's LM

**[0:02:54]** wiki idea. And I know that Google is lagging in the AI race right now. Gemini is not as good as GPT and Claude, but they have been releasing some really good stuff on how to leverage LLMs effectively. And I think that's a totally different lane than building LLMs. Well, so I think this is something

**[0:03:10]** really worth leaning into even if OKF doesn't end up becoming the standard down the line for personal agents. There's going to be something like this. And so it's good to understand this now. Okay. Now, let's really get into OKF. So there are two things that they're standardizing here. The first is how we

**[0:03:27]** are organizing information like our entity documents and our concepts. And then the second standardization is the exact fields that we're going to have in our metadata. So this is the information that we tag at the top of every single document to give the agent a richer set of information. So we can even like

**[0:03:45]** query based on the title or the tags. So we have categorization. This is one of the most important things to let the agent traverse through our wiki like a knowledge graph. And really the best way to make this concrete for you is to show you what a traditional Karpathy wiki

**[0:04:01]** looks like. So we'll take a look at this. This is one of the first wiks that I built when Karpathy released this idea. And then we'll get into some of the problems that we have here. So at the top of every single wiki is your index file. You have the agent maintain

**[0:04:14]** this every single time it's bringing new information in. And the index file, it reads this when it's first searching through your knowledge base, pretty much every single time. And so this just gives you a high-level overview of all the documents that you have access to in the wiki. So the article and then a

**[0:04:30]** quick summary so it knows if this is something that it should look into based on the user's request. And so every single time we add in new documents, this is evolving. And so the agent will read this and then based on what we asked it to do or the question, if it

**[0:04:44]** figures like I should look at superbase o this concept right here, this entity document, then it'll drill into this. We also have the metadata like I talked about earlier like the title and the tags so that it can also search based on this like if it wants to look at the

**[0:04:58]** category of security then it can filter out just those documents and so then we have the full sort of like skill.md here this is like progressive disclosure like skills where the index tells it the knowledge it has and then it can read the full document if it's appropriate

**[0:05:14]** and then we also link to related concepts down here and that link is what really gives us this graph view where You can see how all of our entities and other documents are connected together. So, the agent can sift through this to really get a comprehensive set of

**[0:05:28]** information if the question really calls for it. And so, looking at one of these documents here, it might feel like it's overwhelming to build up all this knowledge over time, but seriously, with an LLM wiki, you are just giving the reins completely over to an LLM. So, you

**[0:05:43]** don't have to be technical. You don't have to spend a lot of time maintaining this. Literally the whole benefit of the wiki is that up until we've had LLMs for this, it was way too tedious to create this sort of knowledge base where we're responsible for understanding related

**[0:05:58]** concepts and building that over time as we're adding in new information. Like there's so much tedious work here that LLM are really, really good at. But as much as they're good at this, they aren't going to create this system in the same way that someone else will with

**[0:06:12]** with their LLM, right? like the way that we link related concepts might be different. The way we structure information, even the metadata, like what if we don't have tags, but we have a field called categories. I mean, even something as simple as that, that that little change might make it so that if I

**[0:06:28]** gave the knowledge base to another person's agent, it wouldn't know how to search through things categorically. It would have to dive into the metadata first to understand that, and it might not decide to do so. I mean, all these little problems will start to compound when you don't have the same metadata,

**[0:06:44]** you don't have the same folders. That's what we're looking to do here with OKF. All right. So now, if you want to build with OKF, create a new knowledge base with this format or even refactor one to use the open knowledge format, look no further than their spec.md file. So,

**[0:06:59]** this is in their repo. I'll link to it in the description. This is just like Karpathy's gist where you copy this document. Like you literally just click this one button right here, put it into your coding agent, and tell it to either build you a wiki following the open

**[0:07:13]** knowledge format or even refactor an existing one. Like I said, it's going to knock either of those out of the park because this is kind of like a skill. It teaches the coding agent everything it needs to know about the standard. Like here is the terminology. Here's how we

**[0:07:26]** structure the bundles. I'll show you more on this in a little bit. Here is how we build the YAML front matter. different attributes that we have for each one of our documents like the tags for categorization, right? Like this single source of truth is all that it needs. And because it's such a simple

**[0:07:42]** format, a simple standard overall, it's not really going to get confused going through this. I mean, it's a pretty long file, but in terms of what large language models can handle these days, especially with, you know, GPT 5.5 or Opus 4.8, this is not much instruction. And it it also doesn't really matter the

**[0:07:59]** scale of your current knowledge base if you are refactoring because you can specifically ask it to use sub agents to work through the different sections of your knowledge base to refactor it to this format. So really easy to scale, really easy to just have the agent rip through this spec. The sponsor of

**[0:08:16]** today's video is Post Hog, a single place for you to understand how users are actually using your application to debug and fix issues and test and roll out all of your changes. And I'm excited for this because I am using Post Hog myself in Archon, my open-source AI

**[0:08:32]** coding harness builder. I'm legitimately leaning on the data insights that I get from Post Hog every single day so that I know exactly how to improve Archon in the way that users actually need. And installing Posthog is incredibly easy. You just click on the install with AI button on their homepage that I'll have

**[0:08:49]** linked to in the description and boom, it's a single command you can run a wizard that will essentially be a senior engineer helping you set up analytics for your entire application in just minutes. And you can also create custom data views like this is the dashboard that I'm looking at every single day to

**[0:09:05]** see how people are actually using Archon. And then we can also drill down to get very granular as well. So the individual runs of Archon, I can click into this here to see all the details. And so we can go very high level all the way to individual parameters as we need.

**[0:09:20]** It's got the analytics for everything. And so production is the time where you can't be flying blind. When you have something deployed out to the world, you need observability. And Post Hog is the best for that. So I'll have a link in the description. I would highly recommend checking them out. And I

**[0:09:36]** talked about this a little bit at the start of the video, but this really is the future of personal agents. It's like what MCP did for agentto tool communication, this OKF is doing for agent to knowledgebased communication. And one of the most important things in the spec here is that they talk about it

**[0:09:54]** being a standard both for consuming knowledge bases like searching through them, but also producing knowledge bases. How do we evolve the wiki over time? build up the entity pages like Karpathy talked about in the initial gist. We really are building on top of it. And one of the really interesting

**[0:10:11]** things to think about here is yes, this is fantastic for sharing knowledge bases or having a teamwide knowledge base. This is also really good though even if you're never going to share a knowledge base. Think about this. If everybody has the same standard for how they are building up their own personal knowledge

**[0:10:28]** base, everyone can share ideas more like, oh, here are the entity pages that are working really well for me and this is how I want to organize things under the standard. And then because you have the standard as the foundation, it's easier for other people to take those

**[0:10:41]** ideas. And so what we're also I think what we're going to see is like yes, I don't think OKF is going to in the end be the standard, but we're going to see something like that and we're going to see the standard evolve over time so that it's easier and easier for people

**[0:10:55]** to create these really rich knowledge bases without having to spend a lot of time upfront designing it with the LLM. Now, of course, sharing wikis with other people is the biggest benefit of OKF. And that leads me into the example that I have for you that's also a gift I'm

**[0:11:10]** very excited to share. I have built a bundle, that's what you call an OKF Wiki, that packages up all of my favorite AI coding YouTube videos on my channel. And so, here's the thing. I'm excited for this. I know that a lot of you, you don't watch my entire video

**[0:11:28]** every single time. You're going to sift through things. You're going to just take the transcript and feed it into your second brain and ask questions. You guys are already doing something like this, but now making it easier for you because I'm prepackaging up sets of videos. I actually want to start doing

**[0:11:42]** this so that you can very easily bring it into your second brain and ask questions as it relates to what you actually care about or what you are working on specifically. And so take a look at this. All you have to do is first of all take this spec and give it

**[0:11:55]** to your coding agent. You have it teach itself OKF. And then you go to this repo with my AI coding knowledge bundle. I'll have this linked in the description as well. And you just paste this prompt into your coding agent. That's it. You give it the link to this repo. You tell

**[0:12:11]** it to read the readme and set up everything and it already understands OKF. So, it links those two things together. Brings the bundle into your local Obsidian or Notion or whatever you're managing your knowledge. And then boom, you can instantly start asking questions. You don't have to bring in

**[0:12:25]** the transcripts yourself. This is the easiest way for just content creators in general to share their knowledge with the world. They can create bundles. I'm creating bundles for all my videos now. And so this is just one example of what OKF unlocks for us. And so I'll also

**[0:12:40]** show you what this bundle looks like because it's a really good example of what OKF is really doing for us. All right, let's get into the belly of the beast. Now I'll show you how I've been setting up OKF and we'll get into the example bundle as well. And so something

**[0:12:53]** that I do for my second brain, every single system that I build in, I always have a tople document that talks about how it works. Like this is how I'm working with OKF bundles. And then here are the different bundles that I have. So I basically have an index so it knows

**[0:13:08]** the different bundles that it can go into and search and read the index that we have in there. So we kind of have like two layers of indexing. And then I also built a simple CLI script. This is actually there in the example bundle that you can clone that makes it easy

**[0:13:23]** for it to in the command line list out my bundles to view a specific index and then you know once it finds one of those files it wants to read then we have the command line tool to read by a specific bundle and concept ID. So I've added

**[0:13:36]** like a little bit of organization on top of OKF with just how I manage many different bundles but otherwise I'm following the format exactly. And so let's actually look at one of these. I'll click into bundles here and we'll go into the one that I just shared the

**[0:13:50]** GitHub for. So, if we look at the index here, we can see that I have two different sections and this is actually a smaller bundle. So, I didn't want to do something super complicated. So, there really are just two sections. I have the videos that I've put in this

**[0:14:05]** bundle, which it's it's rather small. There's only four videos, but these are like the best and most up-to-date ones on my channel for AI coding. And then I have the concepts as well. So different things that I talk about throughout multiple of the videos that I want to

**[0:14:19]** extract into its own entity page. And so the index here says here are the sections. And then I don't actually have a list of each one of the individual files because I'm just going to have the agent read the files that we have in concepts or videos, right? Like it can

**[0:14:34]** list out here are all the files or it can read the index within concepts itself, right? So, however you want it to navigate, it's going to be able to go through these different layers of documents or just do a keyword search. And so, clicking into any one of these,

**[0:14:48]** like the PIV loop, for example, this is the primary mental model that I always teach for AI coding. Very important to have a process for yourself to plan, implement, and validate whatever you're creating with a coding agent. And so, we have the YAML front matter at the top.

**[0:15:03]** And the type, this is what is required by OKF. It is the single required field in the metadata because this is what gives categorization to your documents. So like this is the type of concept. If I go to a video here, the type is video. So we can search over just the videos

**[0:15:19]** over just the concepts which is especially powerful once you get bundles that are a lot bigger than this. Again, this is just an example here. But then we also have all of the optional titles in OKF. So title, tags, related videos. This is how we link things together,

**[0:15:33]** right? Like you saw with that other wiki I showed earlier, it was just things were linked at the bottom. However, this now makes it so it's easier to navigate, creating a standard for how we are linking our entities together. And so each one of these are optional. Only

**[0:15:48]** type is required in OKF. But just because you don't always have these doesn't mean that your agent won't understand it, right? Like if your agent is a consumer of OKF, if you gave it the spec and taught it to be a consumer, it's going to know how to leverage these

**[0:16:03]** fields for better searching and traversing through the knowledge graph that we have here. And so then this is just all of our information on the piv loop. I kept it nice and simple. And then also linking to videos as well, which maybe is like a little bit redundant with related videos. So I

**[0:16:17]** could probably make this bundle a bit better, but I just wanted to have this as an initial example. And it is something that you can immediately bring into your second brain. Just start asking questions. Like I'll show you an example here in my terminal. So first of all, at the top level of my second

**[0:16:31]** brain, I just asked what bundles do I have? It ran a command here. So it used that little CLI tool to list out all the bundles that I have. And then it told me that and then I just asked it a question. So not even telling it what

**[0:16:43]** bundle specifically to look through. I said, "What's Cole's single biggest idea for getting reliable code out of an AI coding assistant?" and it ran four commands in total. So first of all it decided to read the coal AI coding index that's the GitHub that I have for you

**[0:16:57]** and then based on the index it knew like okay let's take a look at the concepts here and then from the concepts it's like okay the single most important thing I don't know what in the index told it that but it's like context engineering let's read the concept of

**[0:17:10]** context engineering so we can see the progressive disclosure as the agent is figuring out where it needs to look down to find the answer for me and then we get the final answer here So just beautiful to watch it work. When we have something structured like this, it's so

**[0:17:26]** easy for it to start with really not much context at all and then drill down into exactly what we need. That's what OKF gives us as a standard. All right. So if you're not sold on the idea of having a standard for the LM wiki at this point, I don't know what to tell

**[0:17:41]** you. The one critique that I think is actually pretty valid with OKF is a lot of people are saying that it's too simple, right? like there's not a lot of value or substance that's actually added on top of the Karpathy wiki. So, I've I've seen that a few times just as I've

**[0:17:56]** been doing a lot of research. I mean, I put a lot of time into prepping for these videos. I think it's kind of valid because if we look at like what it's really doing on top of the Carpathy wiki, it's it's speaking to like exactly how you organize your different files.

**[0:18:09]** Like they they specifically have like indexes within the folders and a top level index like you saw in my bundle. I mean, that's something I didn't really have in wikis before. And then we have the specific fields in our metadata like the type is required. The other ones are

**[0:18:23]** optional but these are the ones that they recommend. Like that's pretty much it. It's how we organize and what is the metadata. That's pretty much all that we actually have in the standard. And so like the argument is kind of valid where it's like what is it really giving? Like

**[0:18:37]** there's there's not much there. But I think that's also the point, right? Like minimally opinionated. It's the bare minimum layer that we need on top so that we can produce and consume these wiks in exactly the same way across everyone's agents that lean into OKF. Like I think that's actually a good

**[0:18:56]** thing. I think that's a benefit, not a downside. The fact that there's not much substance here might seem counterintuitive, but I think that is actually a good thing. And I encourage you just try out the bundle that I have for you here. give it the spec and then

**[0:19:10]** give it this prompt and then just start asking questions about AI coding like how I use sub aents uh what is the piv loop like just start asking and and seeing how easy it is for your agent to grab those things for you and so that's everything that I got for you today on

**[0:19:24]** OKF really is the future of personal agents if you appreciated this video you're looking forward to more things on AI coding and second brains I'd really appreciate a like and a subscribe and with that I will see you in the next video.
