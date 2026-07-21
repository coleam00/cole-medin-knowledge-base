---
type: raw-transcript
title: "The Future of AI and SaaS is Agentic Experiences (Here's How to Build Them)"
youtube_id: BcvjGTxzK40
url: https://www.youtube.com/watch?v=BcvjGTxzK40
slug: the-future-of-ai-and-saas-is-agentic-experiences-heres-how-to-build-them
published: 2025-09-17
duration: "0:20:46"
fetched_at: 2026-07-21
immutable: true
---

## Transcript

**[0:00:00]** I've got something really exciting that I've been exploring recently that I want to share with you. It's all about creating aic experiences with something called AGUI. Now, let me set the stage for you a bit first. There's a good chance that you're stuck on the idea that we need to be building apps or SAS

**[0:00:17]** platforms around our AI agents. But that isn't where the future is headed. The real shift is embedding agents into our applications so they become a natural part of the product experience. And it seems natural, right? I mean, when the AI height bubble bursts, the products that are going to be left over are

**[0:00:34]** generally not going to be the ones competing as agents, but instead the ones that deeply integrate AI agents into a product that delivers its own unique value. That's what I mean by agentic experiences and the future of SAS because these platforms are the ones that are not going to be wiped out as

**[0:00:52]** our more general agents like chat GP and operator get more powerful and make the more niche agents just simply irrelevant. So right now I'll introduce you to how to build these kinds of agentic experiences which are not trivial by the way generally a lot harder than building isolated chat bots.

**[0:01:08]** But luckily I have the tech stack for you to make it simple. So, I'll introduce you to that, get into some demos and really important principles, and then we'll build together. I'll even take an agent that I've created previously on my channel and create a full application around it. So, the

**[0:01:24]** primary part of our tech stack here is a protocol developed by the C-pilot Kit team called AGUI. I covered it on my channel around when it first came out. Super powerful stuff. Now, the big question is, what does this actually do for us? Well, simply put, AGUI standardizes how front-end applications

**[0:01:42]** connect to AI agents. It's like MCP, but instead of connecting agents to tools, we are connecting agents to our applications in a standard way. It's fully open source. So, they have this GitHub repo, which I'll link to in the description. They have a nice diagram here that shows how it works at a high

**[0:02:00]** level as well. So we have AGUI kind of as a middleman here that provides a standard of communication between our front-end applications and our AI agents. And so as long as both have support for AGUI, which all of these AI agent frameworks do, then we have this seamless communication that makes it so

**[0:02:20]** we can build full applications in hundreds of lines of code instead of thousands and thousands. And that's what we'll see as we build together and go through some of these demos. And so we just have to pick our front-end library and our AI agent framework. And then AGUI takes care of a lot of things. And

**[0:02:36]** so for our front end, we're going to be using Copilot Kit. This is a React library that makes it very easy for us to build userfacing agentic applications. It integrates natively with AGUI, of course. And then out of all the options we have for our AI agent framework, you know, if you've been

**[0:02:54]** following my channel that paid AI is my favorite. And they recently added a direct firstparty integration between Copilot Kit and Pineanti through AGUI. They even have an AGUI doc section in Pideant AAI. So, I'm super excited for this. This is actually the catalyst for me to make this video and I've been

**[0:03:12]** talking to the Copilot Kit team about this and actually asking for this integration. So, I'm super excited that it's finally here because now we can build these kinds of user interactive applications with Pyantic AI agents under the hood driving the whole thing. And these are the demos that they have

**[0:03:28]** for us that I was talking about earlier. I'll link to this in the description. It's a great resource to just explore the power of AGUI. So, they have all of these different demos that each represent something that would very much not be trivial to build without AGUI. But with AGUI, it's really easy. You can

**[0:03:46]** even see the code for both the front end like with copilot kit here and the back end like I have paid ai selected here but you can even just select any AI agent framework you want and it'll immediately drop that in in the back end and then we have to change nothing in

**[0:04:01]** the front end that's what agui gives us that standard communication so we can move from langraph to eggno or eggno to panty and our front end app doesn't have to change at all so let's actually see this in action like I want you to see how this really does unlock a entic

**[0:04:16]** experiences for us. Like in this example right here, it is a recipe builder and there's a state sync between our front end and our backend thanks to AGUI. So like for example, I can add an ingredient here and I can say I'm adding in beef, one pound of beef. And then I

**[0:04:32]** can ask my agent, what are my ingredients? And it's going to immediately recognize the changes that I made in the front end here because we have that two-way sync. There we go. We got our ingredients. And then I can do the other way around. And I can say I

**[0:04:46]** want to make a recipe with a lot of beef. All right. So now instead of syncing the front end to the the backend agent, it's now the agent that's going to be updating our front end here. So it's creating the recipe and boom, it renders out everything in a very

**[0:05:01]** beautiful way in the front end. So we have our typical chat application on the right hand side, but then it's deeply integrated into the rest of the components of our front end. That's what I mean by aentic experiences. Really, really nice. We have our instructions here. We can actually improve it with AI

**[0:05:17]** as well. We have our list of ingredients and I can continue to collaborate with the agent here making changes back and forth to make my perfect recipe. And obviously it's just a very simple example here. But yeah, definitely play around with these different things like human in the loop collaborating with our

**[0:05:33]** agent toolbased generative UI. So we can actually build tools in our front end that we give into our AI agent dynamically. There's so many powerful things here. And like I said, we can view the code. So we can see exactly how the front end was built with Copilot Kit

**[0:05:48]** and how the back end was built with the Pantic AI agent. All right, so now that you know how AGUI works and what it really gives us, let's get into actually building with it. So the easiest way to get started with building these Aente experiences with AGUI is to follow this

**[0:06:03]** quick start, which I'll link to in the description. And so this is the copilot kit documentation and they have an entire section for working with paidantic AI specifically and they do that for all of their integrations. It's really really cool. And so to get started we just have to have mpm

**[0:06:19]** installed on our machine and we can copy this command here. So I'll actually go into my terminal and let's walk through this really quickly. So, it's going to set up a new project for us using Copilot Kit as the front end. And then we're using AGUI here. And we can select

**[0:06:33]** our agent framework. And so, I'll just say test here because I have something else set up already that I'll demo for you. And there we go. We can select our framework. Like I can say I want to use Pinantic AI. There we go. And so, it's going to open up your browser for

**[0:06:45]** authentication because there is a cloud version of Copilot Kit. We don't actually have to pay for anything though. Um, and so we can just get through this and authenticate and then I'll come back once I have this done. Okay, there we go. So, I'm signed in. It creates a Copilot kit cloud API key as

**[0:07:01]** well if you want to host with them. You don't have to though. And so, for demonstration purposes, we're not going to be doing anything with that right now, but yeah, they even give us some documentation here. And so, we can open this new folder that was created for us.

**[0:07:14]** And so, I have it open right now. And then there's a readme here that walks you through the quick start. So, how you can get things set up in both the front end and the back end. And it's literally just a couple of commands. Like, it's so easy to get this up and running. And

**[0:07:27]** that's going to give us a quick start that's going to look kind of like the demos that we saw here. But now we have something that is running entirely locally. And there's a couple of different things we can try to really see the power of AGUI. And we can start

**[0:07:40]** to build on top of this application as well. But I'll just show you really quickly. Like for example, I can say set the theme to green. And so this is a tool that we actually build in the front end and send into our agent. So our backend agent, thanks to AGUI, doesn't

**[0:07:56]** even have to know that there's a tool to change the theme. And we just pass that in from the front end. I can also say write a proverb about the difficulties of SQL. All right. So we'll send this in. It'll make a proverb for us. And then boom, we immediately have that

**[0:08:12]** state sync like that other demo I was showing you where now our front end has this proverb here. And it's displayed and rendered out in a nice rain. I can say write another one. And so we can do another state sync here. And then I can delete one of these as well. Like I'll

**[0:08:25]** just delete this first one. And I'll say I deleted one which is left. Right? So we can know that the front end is also syncing back to the back end as well. And then the last thing that they have for the demo here. I'm just trying to like show you the different kinds of

**[0:08:39]** things that we can do with this front end. It's really, really neat. We can also render out components in our chat UI. So, we're not limited to just having a bland conversation here and then passing things into the rest of our app. We can also render out cool things here.

**[0:08:52]** So, I can say, uh, what is the weather in Orlando, Florida? And it's going to render out a really nice looking card here. So we can take tool calls from the back end and standardize the format like actually make it look like a nice component in our React frontend. So

**[0:09:08]** super cool. That's what we have for our quick demo here. But now let's actually use this as a starting point to build our own applications on top. Now to build on top of this application, we're not going to dive straight into implementation. There's one really cool thing first because the co-pilot kit

**[0:09:26]** team, they have built a vibe coding MCP server. Now, you know that I'm not the biggest fan of vibe coding. So, maybe this isn't the best name for what I'm about to use it for, but this is an MCP server that's kind of like archon for knowledge retrieval. It gives our AI

**[0:09:42]** coding assistant the ability to search through the co-pilot kit and AGUI documentation and best practices. So it becomes our expert guide on our implementation. Super cool. So if you're building any kind of agentic experiences with this tech stack, definitely use this MCP server. That's what I'm going to be using right now. And they have

**[0:10:02]** instructions here based on your AI coding assistant like cursor or client or windsurf exactly how to hook it up. Now they don't have instructions here for claude code specifically. Uh but I've got that for you right now. So you can copy this URL right here and then go

**[0:10:17]** into your editor. I have my terminal open here and I'll just paste the command right here. So it's claude MCP ad and then SSE is their transport and then you just can call this server whatever you want and then the SSE URL is the one that we copied from the

**[0:10:32]** documentation. So I'll add that in here and then I can also do a claude MCP list to test the connection and so this is a remote MCP server completely free to use. Now Claude Code is able to search the C-pilot kit documentation. Super cool. Okay, so now armed with this MCP

**[0:10:50]** server, we can now build any kind of agentic experience that we want on top of this starter template. It provides a really good foundation for us. And so yeah, I'll send in a request here. I'll show you what it looks like to build on top. And then I'll even show you how far

**[0:11:05]** I went taking a rag AI agent that I built with Padantic AI on my channel previously and I'll show you how I built a full application around it with a GUI. So, we'll get there in a second, but right now I just want to send in a simple request here. I'll and first I'll

**[0:11:19]** actually tell it to use the uh copilot kit MCP server to understand how to build this feature. And maybe I don't have to call that out explicitly, but I just want to to make sure that it leverages the MCP. So, what I want to do here, if I go within the source and

**[0:11:37]** page.tsx, one of the things we have here is the co-pilot kit action. This is our front-end tool that we're passing into our agent to give it the ability to change the theme. And so I want to add another tool here to do something else. Let's say maybe clear all the proverbs

**[0:11:56]** that we have on the front end. I think that's a good example here. So I'll say I want to make another uh front-end tool with co-pilot kit to clear the proverbs that we currently have. And so we since we have that state sync as well, the agent will immediately recognize that

**[0:12:15]** everything is cleared in the front end. And so I'm going to go ahead and send this in right now. And it should after maybe looking at some of the files we have in um our starter template here or actually yeah right away it searches the copilot kit docs. Take a look at that.

**[0:12:28]** Use copilot kit action custom actions front end. And we can do control O to expand and actually see the chunks or the snippets as they call them that were retrieved from this rag implementation. It's really, really cool. So, we're pulling in the documentation from C-pilot kit. That's a part of our

**[0:12:45]** context engineering here, giving our coding assistant all the information it needs to actually build out the implementation here. Now, this is a very simple example. And so, it could probably just look at what we already have for a front-end tool and then implement that as well. But I hope that

**[0:13:01]** you can see that like if we didn't have any front-end tools at all, it would have no idea how to use use copilot kit action. So, it would need to search through the documentation like we are doing here. And so, yeah, let me actually scroll down. Um, let me exit

**[0:13:14]** out of this. There we go. All right. Yeah, there we go. It is adding in a clear all proverb tool. And so, when this is invoked from our agent, it's going to yeah, just clear the proverbs in the state that we have and that'll immediately be synced to the backend as

**[0:13:30]** well. Looking really, really nice. So, cool. Yeah, I'll pause and come back once this is fully fully implemented. There we go. I just paused for like 20 seconds and then we are done. So we have that new action and then we just have the button that it added for us to be

**[0:13:43]** able to clear things right here. So there we go. We got our updated UI. So now I can say add a bunch of proverbs. All right. So we'll have to populate it first obviously. So the agent has generated some proverbs. There we go. We have Oh wow. It is adding a lot. All

**[0:13:57]** right. So we added a lot of proverbs here. And now I can clear all of them. And so I'm going to send this in. Click this button here. Or I could just ask it to clear the proverbs. So, well, I'm actually going to click this button here, clear all proverbs. Uh, there we

**[0:14:10]** go. And now we have that state sync. And so, I can say, what proverbs do I have? And it's going to say that there are none. There we go. It is currently empty. And I can also show you. So, I'm going to say add some more. I'll also

**[0:14:23]** show you that like I can have the agent clear them as well. So, it doesn't just have to be this button. So, I can say clear the proverbs. And so just based on a simple text request to our agent, we can do the same thing that that button

**[0:14:34]** did. And so I hope that this just helps you see how our agent is starting to interact with the website. We can build these agentic experiences where AI agents can actually help us navigate through a website as well. Like this is a really simple example where it performs an action of a button click,

**[0:14:51]** but this could be a full onboarding experience where the agent is actually like walking me through clicking on different buttons in my app depending on what I'm talking to it about. Like, oh, I have this question and then it's like, okay, well, let me click on this button

**[0:15:03]** and then highlight this section of a website. Like, there's just so many things that we can do with this. And so, that that's like the higher level principles that I wanted to be speaking to in this video. Like it's cool to like see AGUI and Pantic AI specifically, but

**[0:15:16]** like the most important thing that I'm trying to get across here is the general principles of like we need a way to sync the state between the front end and the back end. The agent needs to know like where we're currently at in our front end. And that is what AGUI makes really

**[0:15:31]** easy for us along with the fact of course that our backend is so incredibly simple thanks to AGUI. Generally, you'd have to build an entire backend with API endpoints and middleware and everything. But our backend right now is literally just a single file. We have our agent.py. And so this is our Pantic AI

**[0:15:50]** agent where we have our agent defined. We're giving it some tools. It's going to look very similar for uh other frameworks as well. We have our primary system prompt. And then the only thing we have to do to turn this padantic AI agent into a fully working API endpoint

**[0:16:06]** compatible with AGUI and our C-pilot kit front end is to call this two AGUI function. So so easy. And so now our agent is running on port 8000 and it is good to go. And we have everything handled here with the state syncing and conversation history. We can even

**[0:16:22]** dynamically adjust the system prompt based on the front end. There's so much integration that we have here for literally 100 lines of code. like this is just so so easy. And so there are a lot of things that are made possible thanks to AGUI. Not because we couldn't

**[0:16:35]** build it without the protocol, but because it just makes it so easy to do so. And it's the same kind of thing with like the model context protocol. I mean, we can connect agents to any tools, but MCP just makes it very easy and accessible. That's what we have here.

**[0:16:50]** And like I said I would cover, I even went as far as to take an existing Pantic AI agent that I built on my channel previously and create a full application around it with AGUI and Copilot Kit. And that's what you're looking at right here. And so I'll link

**[0:17:04]** to the video right here where I built this rag agent. I built it with cloud code and a team of sub agents. And in that video we were just using the command line, a simple CLI tool to talk to our agent. So it was a perfect opportunity to take an existing agent

**[0:17:18]** and barely having to change the code at all thanks to the podantic AI and AGUI integration to build out this full app. And so now I can ask it a question. It's a rag agent. So we have this knowledge base with all this information about AI startup. So I can ask it about OpenAI's

**[0:17:33]** funding for example. And we'll get the answer on the right hand side like a normal chatbot. It's got streaming and conversation history and everything. But then also it takes all of the chunks that we returned from the knowledge base and it populates the front end with them. So we have this super interactive

**[0:17:48]** rag agent where we can actually like view the chunks that it retrieved. We can see the match percentage. We can click into view the contents of the chunks and all the metadata like the document that it came from. I mean this is definitely taking a typical rag agent

**[0:18:02]** that you would have in just a chat interface. taking it to the next level where we can actually see under the hood what information it's using to give us the answer that we have in the chat box. So really really cool and man was it easy to build this out. I'll just show

**[0:18:16]** you the code really quickly here. I had to define some classes here. That's for the state sync so that the chunks that we have in the front end is synced with what the agent knows it's displaying. And then I defined my agent very very much the same way like I always do with

**[0:18:31]** padantic AI giving it tools as well to search my knowledge base both with semantic search and hybrid search like a keyword search. And so I'll scroll down here. We have the system prompt as well. Um this is also dynamic. So all of the chunks that we have as a part of that

**[0:18:46]** state sync through agui we're passing those in as a part of the system prompt. And then all I have to do just like our starter template is call the rag agent.2 to agui and now we have the full backend infrastructure spun up with the agent running on a port 8000. Absolutely

**[0:19:02]** beautiful. And we could swap this out for a langraph agent and not even have to change the front end at all. That is the beauty of AGUI. And to build all of this, all I did is I followed the quick start here in the copilot kit documentation for Pantic AI. They have

**[0:19:18]** instructions specifically for how you can take an existing Pantic AI agent and turn it into something that's compatible with AGUI. So I I use this as a reference point. And then I went into Cloud Code. I took that starter template that I already showed you building on top of, put in the code for my existing

**[0:19:35]** agent, hooked in the vibe coding MCP server and just had it go ham. So yeah, using the MCP for documentation and then the existing template to build on top of, I just told it exactly what I wanted. I want you to take the copilot kit application, make it work with this

**[0:19:50]** rag agent so I can actually see the chunks and all the metadata and it knocked it out of the park. It was so easy to build this out. So there you have it. That is everything you need to know to get started building agentic experiences with AGUI. Now here's the

**[0:20:04]** thing. Pyantic AI, AGUI, Copilot Kit, these are just tools to get the job done. The higher level principles are what I really want you to focus on. things that I covered here like human in the loop and front-end tools and state syncing. That's what you really need to

**[0:20:19]** make these agentic experiences. AGUI is just the protocol to standardize things and make it that much easier to build out this kind of application. Like I literally built this out in like a half hour after I brought in my existing agent. It was so easy to do this with

**[0:20:34]** the help of an AI coding assistant. So there you go. If you appreciated this video and you're looking forward to more things AI agents and AI coding, I would really appreciate a like and a subscribe.
