---
type: raw-transcript
title: "Super Special Livestream this Weekend! (LIVE AI Agent Build)"
youtube_id: pjF-0dliYhg
url: https://www.youtube.com/watch?v=pjF-0dliYhg
slug: super-special-livestream-this-weekend-live-ai-agent-build
published: 2025-10-24
duration: "0:07:13"
fetched_at: 2026-07-21
immutable: true
---

## Transcript

**[0:00:00]** quick announcement that I'm super excited for. This Sunday, October 26th, at 11:00 a.m. Central time, I'm doing my first ever live AI agent build as a live stream. All my other streams in the past have been more focused on Q&A. I did something kind of similar with NAND in

**[0:00:17]** the past, but this is the real deal. Building a complete AI agent and using AI coding assistance. And if you're watching this after the stream already happened, no worries. I'll have a link to the recording in the description. And not only will I be showing you how to

**[0:00:30]** use AI coding assistance to build any AI agent, I also have an awesome use case for our stream. I teased recently that I'm working on this AI agent that I'll be showing how I build on my YouTube channel. It's your own personal AI coach. So, it's an AI agent with a lot

**[0:00:47]** of advanced rag techniques that's trained on all of my YouTube content. I want to extend that to more than just YouTube later as well. And so it's a really practical agent to be a resource alongside all of my YouTube content. And we're going to be building this from the

**[0:01:01]** ground up together, which I'm just so excited for. So link in the description to the live stream. Go over there, enable notifications for it. Again, that's this Sunday, the 26th, at 11:00 a.m. Central time. Building our personal AI coach for both AI agents and AI coding assistants because that's what I

**[0:01:18]** cover on my channel. And this is going to be trained on my YouTube content to start. And then I want to expand the knowledge base over time to include other sources as well. So I got big plans for this agent, but I want to build it with you live. I think that's

**[0:01:31]** going to be so exciting. And so there are four core technologies that we're going to be focusing on in the live stream. So just giving you a little bit of a teaser for what's coming as we build this together. And so starting with YouTube, this is obviously going to

**[0:01:44]** be the primary data source for our rag pipeline. So, we'll build a simple yet effective rag pipeline together for ingesting YouTube videos and we'll include the extraction of metadata and timestamps. Like, it's not going to be extremely trivial and we're going to do that so we can have more advanced rag

**[0:02:01]** tools that I'll talk about in a sec. And this is going to work for any YouTube channel. So, theoretically, this agent that I build, you could turn it into an expert for really any content creator. Pretty cool. And for the AI agent framework, we're going to obviously be

**[0:02:15]** building in Python. That's what I always cover on my channel. And Pyantic AI is still my favorite AI agent framework and it has been for quite a while. And we'll be giving our Pyantic AI agent a few different rag tools to query YouTube videos. And I'm going to make it so that

**[0:02:30]** it's going to work for really any large language model. So we'll be able to use Open Router, Olama, Anthropic, OpenAI, all these different providers. I want to be very LLM agnostic and I'll be focusing a lot on the tools that I give to the agent because I want to apply

**[0:02:45]** some more advanced rag strategies to make that a really practical part of the stream as well. So applying different strategies for ultra accurate retrieval and even giving the agent to pull transcripts if it needs. So it's more like an agentic rag solution where the agent gets to reason about how it

**[0:03:02]** searches through the YouTube transcripts and we'll have token streaming with a complete front end. like this is going to be a full stack application that I've got in store for you. And speaking of full stack, for our database, we will be using a superbase. And so this will be

**[0:03:17]** where we store all of our YouTube videos, including the transcripts and the embeddings that we have for rag and then metadata as well for more advanced rag techniques. being able to do metadata filtering and things like that to make sure that our rag solution can be very precise and then authentication

**[0:03:33]** for our front-end application because I do want to make this something that is deployed to the cloud ready for you, anyone viewing my YouTube videos to leverage at some point. And so obviously you'll need authentication for that. And then last but not least, something I covered pretty recently on my channel is

**[0:03:48]** a tool for rag called Dockling. And this is especially useful for the hybrid chunking that they have available. So, more on this when we build with Dockling together in a couple of days here. But this chunking strategy is actually going to be super critical for accurate rag for a YouTube transcript. So, we'll be

**[0:04:06]** using Dockling for that local models so everything is blazing fast and later I can extend this to support uploading PDFs for when I expand the different sources for the knowledge base. So, that's everything going into this agent. So, it's going to be super practical, super hands-on. It's going to be pretty

**[0:04:22]** casual and engaging as well, like I always like to make my live streams. It's going to be a blast. And the goal that I have for you, the primary goal is to give you a super straightforward example of building a pretty practical AI agent. I hope this seems really

**[0:04:36]** practical to you and it's going to be using a full AI coding assistant workflow. So, of course, we're going to be using AI coding assistants. I'll use claude code in the stream, but I'll talk about how this will work with really any AI coding assistant. And then for task

**[0:04:50]** management and rag, we're going to use the good old archon because this is my open source tool that I have available for you to enhance any AI coding workflow. So of course, I wouldn't miss including it in everything that we've got right now. And by the way, a massive

**[0:05:04]** reason that I'm doing this live stream is cuz I want to celebrate the release of the Agentic coding course in Dynamis. So, I'll have a link to this in the description as well, so you can check it out because if you want to master AI coding assistance and learn how to build

**[0:05:19]** reliable, repeatable systems that get you results you didn't even know was possible with AI coding assistance. This is for you. I promise you're not going to find anything better. And you got to understand, I have to tell you about this right now because the first batch of the course was released right into

**[0:05:35]** the Dynamis community literally today. So, it's on the forefront of my mind. I'm super excited for this. We're going to be releasing the course in batches to the community over the next month and having live workshops to go along with these releases. So, it's going to be super engaging. I just released the

**[0:05:50]** module about the core mental models of AI coding and principles. Then, we'll get into building your own system that is optimized for your use case and your code bases. And then getting into how you can automate your workflows, integrate with your applications. We'll even get into more advanced things like

**[0:06:07]** remote AI coding. And then finally getting into some more out-of-the-box solutions that you can leverage and learn from to build your systems like the PRP framework, the BMAD method, and the GitHub spec kit. So really covering the full landscape for AI coding and taking your systems to a level that is

**[0:06:24]** just probably unimaginable for you right now. And the core mental model that I cover here is that every mistake is an opportunity to evolve your system. So when AI screws up something in your code, instead of just fixing it yourself, you fix your system and retry. And when you iterate on this over and

**[0:06:42]** over again, you end up with this system that is perfectly crafted for you. And that really is your competitive advantage. So definitely check out the Dynamus Aentic coding course. But with that, back to the main announcement for this video for the live stream. Again, that is this Sunday, the 26th, at 11:00

**[0:06:59]** a.m. Central time. It's going to be super practical, super fun, and we're building something that's going to be an incredible resource for the channel going forward. And so with that, I will see you this Sunday for the first ever live agent
