---
type: raw-transcript
title: "If You’re Serious About Building AI Agents, This is Your Secret Weapon"
youtube_id: DpPVEw4dd0w
url: https://www.youtube.com/watch?v=DpPVEw4dd0w
slug: if-youre-serious-about-building-ai-agents-this-is-your-secret-weapon
published: 2025-04-23
duration: "0:27:50"
fetched_at: 2026-07-21
immutable: true
---

## Transcript

**[0:00:00]** Let's face it, a lot of AI agent development these days is just guesswork. It's clear that most people aren't serious about building AI agents that are actually useful in the real world. So my question to you very simply is, do you want to stand out and build productionready AI agents? Because if

**[0:00:17]** you do, then I have your secret weapon. It's a completely free and open- source tool that I've also added to my local AI stack and it's called Langfuse. Langfuse is an LLM engineering platform for agent observability, which is hands down the most underrated concept for AI agents right now. But Cole, what do you mean by

**[0:00:36]** observability? I mean being able to monitor every action your agent takes how much each request costs, the response times, and all of the conversations that your users are having with your agent. And this also gives you the visibility that you need to iterate and improve upon your agent over time

**[0:00:53]** which is so crucial. Sure, a lot of these things aren't super important when you're running your agent locally. It's pretty easy to track response times find opportunities to improve your agent, see what's going wrong when you're the only one interacting with it. But without a platform like Langfuse

**[0:01:08]** you're flying completely blind when your agent is out there running in the wild. When it fails, you'll have no idea why. You won't know how much you're spending and most importantly, you won't know how to iterate on your agent to improve specific responses or address any bottlenecks. It is way too dangerous to

**[0:01:24]** not invest time into learning this platform. So if you're serious about building AI agents, allow me to introduce you to Langfuse and get you up and running with it in just minutes. So the first thing that I just have to tell you is that I am opening up a can of

**[0:01:36]** worms with this platform. Langfuse is so featurerich and I already have so many more ideas for videos to build on top of what I'm going to show you right here. So right now I'm going to give you an overview of the platform specifically focused on monitoring agent executions.

**[0:01:51]** But yeah, there's so many other things that I could cover as well. So as you go through this video and you pick things out, just let me know in the comments what you want me to dive into more then next time I cover Langfuse. So yeah just a bit on the platform now. First

**[0:02:03]** they have an awesome demo that I'll show you in a little bit. So you can see very quickly how powerful Langfuse really is and they have a lot of companies that are already using them like Twilio and Con Academy. like they have a pretty impressive wrap sheet here and they have

**[0:02:18]** a lot of different features that I don't have the time to dive into in this video. The main thing I'm going to be focusing on is tracing. So, we can monitor agent executions and see all the decisions that our agents are making under the hood when they're running in

**[0:02:30]** production. And then the other thing that's really cool to me is just the number of different frameworks that Langfuse integrates with. So, it's very easy to set up this agent monitoring no matter which framework you built your agent with. like pinantic AI, my current favorite, lang chain, langraph, crew AI

**[0:02:46]** they've got semantic kernel, pretty much everything that I would care about except n. More on that later. I think they might be adding that at some point here. And then the most important thing with Langfuse overall is that they are 100% open-source. And so you can pay to

**[0:03:00]** have them manage it for you if you want something really simple, but you can host Langfuse entirely yourself if you want to pay absolutely nothing and have utmost data privacy. Now, they are a platform that focuses on enterprise security, but there still are going to be many cases where you want to monitor

**[0:03:16]** your agents, but you don't want all of the interactions your users are having with your agent going to another third party. And so, you can guarantee that everything stays in your own infrastructure when you host Langfuse yourself. And the absolute easiest way to self-host Langfuse is to use my local

**[0:03:32]** AI package. I've been working on this a lot on my channel as a way to curate a bunch of open- source software for you for your database, your large language model, your user interface, and now Langfuse as well for agent observability. And there's a good amount that goes into self-hosting Langfuse

**[0:03:49]** because it relies on a lot of other services for data storage like Reddus Postgress, ClickHost, and then some kind of blob storage. So, it's not super trivial. So, I've spent a lot of time getting it incorporated into the package for you. and check out this video that I'll link to above if you want full

**[0:04:04]** instructions on how to get this package up and running for yourself. That video is entirely up todate except for these environment variables that you have to set for Langfuse, but I've got instructions on how to do that in thev.example. So, just keep that in mind. But then the rest of the process

**[0:04:21]** is still going to be exactly the same for getting the package up for yourself. And you could always just follow their documentation for self-hosting if you want to do it outside of my local AI package. So, I'll have links in the description both to the local AI package

**[0:04:33]** and this guide for self-hosting. So, now let's dive into the Langfuse documentation and their live demo that they have for us. So, we can try out their platform without having to set up anything for oursel. It's really cool. I mean, whenever you have a platform that gives a live demo in their

**[0:04:48]** documentation, you know that they are legit. And so, I'll have a link to this documentation in the description as well. And if you go to the interactive demo tab, take a look at this. You just have to create a demo account. It's no credit card required or anything. So

**[0:05:02]** you just have to create an account really quick. And then you can chat with the agent. And so, this is a rag AI agent that has access to the Langfuse documentation to answer any questions that we have. So, I can say something like, "How do I use Langfuse with

**[0:05:16]** Pyantic AI?" And it'll take a little bit to get a response because it's going to fetch the relevant documentation. I mean, actually, that took only a couple of seconds, which is super cool. So they talk about the open telemetry backend, which we'll get into that in a little bit. They talk about how we can

**[0:05:30]** integrate with Pantic Logfire. Like this is really legit. They even have some code examples here within Padantic AI and a screenshot as well. Like, oh my goodness, that is really cool. Anyway that's not even the point here. The point is that now that we have chatted with the agent, we can go into this link

**[0:05:47]** right here. That'll bring us into the platform where we can then take a look at the logs that we have for the agent trace. So, here we go. We have this record from me. We have all these other ones from other people as well because this is a live public demo. Just makes

**[0:06:00]** sense that we'll see other stuff here. But yeah, this is my trace. And so, let me zoom in on this for you here. I can click into this and then we can see everything that it tracked throughout this request. Just look at the amount of information that we have here. Even just

**[0:06:15]** at a high level, we have our total cost given the LLM that it used under the hood, how long the request took, the number of input and output tokens. We even can see our user ID and session ID. So we can group all these traces by given users and sessions. More on that

**[0:06:29]** later. It's another very powerful feature. We can see the input and output at a high level. But then more importantly, we can drill down into the specific decisions that the agent decided to make like it decided to use their retrieval tool. So this is the input into the tool basically just

**[0:06:44]** taking my request and passing it in. And then this output is everything that it got from the rag lookup. You can see that if I expand 4,359 more characters there's a lot of relevant documentation that it fetched to aid in its answer. And then we can go into the final

**[0:06:58]** generation and take a look at what this looked like under the hood as well. So we have our system prompt that we gave. We can drill down into more details u kind of in the middle between my question and the final response. But yeah, we have my user message and then

**[0:07:11]** the assistant response. I can show everything else that happened throughout this whole process. you get this kind of visibility that you definitely need for agents in production. If you want to really see the decisions that are happening under the hood for this agent so that you can iterate on it, see where

**[0:07:26]** anything is going wrong, you can take a look at your costs. You have it all here. So, if that didn't convince you that Langfuse is a beast and something you definitely want for your AI agents I don't know what to tell you. And so with that, let's now dive into the docs

**[0:07:39]** and see how we can build Langfuse into our own agents. I have a quick example to get us started and then I'll also show you how we can incorporate Langfuse into our Pyantic AI agents with a downloadable template for you that I'll show you in a bit and have a link to in

**[0:07:54]** the description of this video. And the way that I learned how to do all this is just following the documentation here. It's very comprehensive. And in this integrations tab, they show you for all these different frameworks how you can build in Langfuse. And so I just went to

**[0:08:08]** Pantic AI, followed this to a T. And then also you can ask the AI. So this is a button in the bottom right that my face is currently covering. But yeah you can open up this chat interface with the same rag agent that we used in the demo and ask it anything you want.

**[0:08:22]** Anything in the documentation here it has knowledge of to help you get things set up with Langfuse. So the first example that I have for you is just following what they have in the quick start. Take a look at how easy this is to take your current agent that uses the

**[0:08:36]** OpenAI client and then just have it use Langfuse instead. So they have this dropin replacement where you can import OpenAI from the Langfuse package and then use it in the exact same way that you're already using the OpenAI client and then it instantly has all of that tracing that we saw in the demo. You

**[0:08:52]** just have to add this observe decorator to the top of any function where you're calling into the OpenAI client. So that's pretty much what I have in the downloadable template that I have for you that I have linked in the description. This is the first example just following pretty much everything

**[0:09:05]** that we saw in that quick start just with a little bit of extra to load in the environment variables that you can set yourself. So you just provide your OpenAI API key and later I'll show you how we can use other LLMs as well. And then you just need these three values

**[0:09:18]** for Langfuse. And the way that you get these once you have Langfuse up and running either hosted locally like I have right now or just in their managed version in the cloud you create a project like I created Dynamis here and then you go to settings in the bottom

**[0:09:31]** left API keys and then you create a new API key and this will give you your secret key public key and host. So those are the three values that you need to put in for your environment variables and that is just what they showed you in the quick start as well covering that

**[0:09:45]** right here. So, back over to the code I'm going to pull up my IDE again. In this example, we're just asking it to write a story for us. And so, I have the observe decorator. I have OpenAI imported from Langfuse. And I have instructions in this repo as well for

**[0:09:59]** how to get everything up and running with your environment and things like that as well. But once you have that set up, you can now go into a terminal and just run the command python simple langfuse.py. And I'm within that iterations folder right here. And so this will make a normal request to

**[0:10:13]** OpenAI. And everything seems the same under the hood, but as we'll see in a second, we have so much data to go along with this request in Langfuse. And so here's our story. I'm not going to read the whole thing right now. I think that would probably be pretty boring. LLMs in

**[0:10:28]** general don't make the best stories, but that's not the point. The point is to show you the trace that we have. So now back over in my Langfuse client, I'm going to go to home, and we can see that we have four traces where I just had three before I made this one. So, I'll

**[0:10:41]** go to traces and then boom, we can open up this brand new trace that happened just 30 seconds ago. So, we see if I go to the OpenAI generation, we have the system prompt, you are a great storyteller, the user message, which is once upon a time in a galaxy far, far

**[0:10:56]** away. And then I'm asking it to continue the story. And there we go. We have the response from the assistant where it picks it up for me and it generates this full story. And just like we saw in the demo, we can see the latency, the cost of this request. I'm using GBT 4.1 mini

**[0:11:10]** for my model by the way. So this was way less than even a penny for this. The number of tokens, all of that metadata and the full response and all the decisions that were made by the agent here. We can see this. Now this is a very basic execution. We don't have any

**[0:11:23]** tool calls here. There's not much to really dive into, but that's why I want to show you how to incorporate Langfuse with Pyantic AI. I want to build out a full agent with you. So we can actually watch the agent make tool calls, see what the responses are from that, see

**[0:11:36]** what parameters it decided to pass into the tools. We really want that kind of visibility with agents in production. So let me show you how to do that. Right now, Pyantic AI is my favorite AI agent framework. They just do everything so well, including logging and monitoring because Pantic AI uses a library called

**[0:11:52]** Logfire under the hood. It supports this open telemetry backend which is basically a standard for communicating this kind of log data that we want to use in Langfuse. So Langfuse can directly integrate with log fire under the hood using open telemetry. And this is super technical so I don't want to

**[0:12:08]** get into this right now but basically we can leverage a part of the padantic AI library to build into langu. And so I'll cover how we can do this with padantic AAI and you can always follow along with this documentation that we have here for any other framework that you might be using.

**[0:12:23]** And so we just need to install podantic AI and logfire. And then we can incorporate the environment variables with a little bit of extra code like this. So I'll show you that in my example in a little bit. And then we just have to set up a little bit of

**[0:12:36]** extra boiler plate to configure logfire. And then this is how we set up our agent within Pyantic AI. Everything is pretty much what you should be used to if you've used pinantic AI before. You just have to make sure that you include this instrument parameter so that we have

**[0:12:50]** logfire enabled and the agent is going to be sending communication through open telemetry as it is invoking tools and generating responses. So for my first podantic AI example with Langfuse, I have built an agent that uses the Brave MCP server. So it's an agent with web search. just a super simple example

**[0:13:08]** because I want to focus mostly on langfuse here, not how I built an agent with podantic AI. So I have this configure langfuse function that incorporates everything that we saw as that boilerplate in the documentation to incorporate our environment variables for langfuse and to configure logfire as well because logfire is our connection

**[0:13:26]** between pyantic AI, our agent and langfuse. And so I just call that function to set up everything. And then I have the Brave MCP server defined like this and I add it into my agent through the MCP servers array. So I have other videos on my channel where I talk about

**[0:13:41]** Pantic AI with MCP. So I'll link one here if you are curious. I don't want to dive into all the specifics of this right now because we are focusing on Langfuse. But that's it. We now have an agent with web search and it's hooked into Langfuse that easily. We just have

**[0:13:54]** to configure everything with this function and then have instrument equals true like we saw in the docs. That is all it takes. It is so easy. And then the rest of this code is just a main function that I have so that we can interact with our podantic AI agent in

**[0:14:08]** the terminal. And so speaking of that let's do that now. So I'm still within this iterations folder here. And now instead of running the simple langu script, I'm going to run simple paidantic AI. So, it'll start up the Brave MCP server, get my agent all connected, and now I can ask it a

**[0:14:23]** question that would cause it to invoke the Brave web search tool. So, I can say something like, "What are the latest offerings for the Gro 3 LM?" If I can spell right. Okay, there we go. So, yep it's preparing the model run. It's calling the Brave web search tool. Now

**[0:14:41]** it's generating the final response. And yeah, that was super super fast. GPT 4.1 Mini is a very fast LLM, by the way. It's pretty impressive. So we have our response and now just like we saw with the simple Langfuse script, we can go back into our Langfuse client and we can

**[0:14:55]** see this execution. There we go. And the input and output is blank, but we'll cover that in the next and final example that I have for you. We can click into this agent and now we have a lot more information given to us here. The other execution was really just the response

**[0:15:10]** and that was it. And now we can take a look at the decisions the agent is making under the hood because it decided to call the Brave web search tool. So we can click into the tool to see any metadata. We can also go to the generation above it and we can see what

**[0:15:23]** the agent decided for the parameters to the tool call. So we have my question here and then the first message from the assistant is its request to use the Brave web search tool and we can look into the exact query that it used to search the web. This is the kind of

**[0:15:37]** thing that we can't just see in our terminal unless we set that up. But this is just such robust logging that we have. Everything that we'd care about seeing, we can see here. And we can go down to the final request and take a look at what it gave for its response.

**[0:15:49]** So now this is the response after it invoked the tool. So we can see the flow here where it's our question and then we have its request to call the Brave tool and then we have the response after it gets everything back. So the Brave web search response is also here. So if we

**[0:16:04]** wanted to expand all these characters we could see everything that the Brave API returned to our agent, which should then use that to give us the final response. So yeah, this is only one tool call, but there's still so much information for us to look into here. And if there's ever a tool that

**[0:16:19]** misbehaves or it seems like the agent always gives bad parameters to a tool we can use this logging to troubleshoot that and really start to figure out how we can iterate on our agent and make it better. Even when we are not the ones interacting with the agent when we have

**[0:16:32]** it running in production, we can go back and look at these logs over time. And we can separate these logs by users and sessions as well. So we really have that granular control to look into exactly what we need to for our troubleshooting. And so with that, I'm going to show you

**[0:16:46]** my full example. Now, that's the complete template that I have for you. So, let's dive into that. So, here is the final template that I have for you connecting Pantic AI to Langfuse. And I put a good amount of work into making this a really nice starting point for

**[0:16:59]** you, even doing things like making it so we can track traces for certain sessions and users. So, you have that kind of granular control within Langfuse. And so this agent uses MCP just like the simple one that I already showed you. But I have many MCP servers set up that are

**[0:17:15]** each connected into a specialized agent that is given the responsibility of handling all the tool calls for that MCP server. And then I connect them all together with this primary agent that is given a tool with Pantic AI to call into each of these specialized sub aents. And

**[0:17:32]** so I don't want to get into the weeds of how I implemented all of this. I actually built this on my channel previously using Archon, my open- source AI agent builder. That is beside the point, though. I just have this primary agent that can use all these different

**[0:17:44]** tools through specialized agents. And I'm doing this on purpose, building something a little bit more involved because I want to show you what it looks like to have an agent actually invoke many different tools and what that ends up looking like in Langfuse. And then I took my configure langfuse function, I

**[0:18:00]** put it in its own file. Most of this is the same for handling the environment variables and configuring logfire. The one thing that I am doing though is I'm returning this trace. So I'm just importing this from the open telemetry library. And the reason that I want this

**[0:18:14]** is because this trace is how we can set custom metadata on the agent execution. Everything that we track in Langfuse. So let me show you that. If I go back to the main function here where I run this multimcp server agent, we have this line right here where we create what's called

**[0:18:32]** a span from the trace. And then so that is going to now track everything for the current agent execution. And look at this. We can set custom attributes like we can set the user ID, the session ID. At the bottom here, we can define the input and output value. So that fixes

**[0:18:48]** what we saw earlier where in Langfuse the input and output was just completely blank. And the way that I knew how to set all this up, by the way, is just in the Pantic AI docs within Langfuse. If you go down to um step five, passing additional attributes, they cover how

**[0:19:03]** you can set all this up just like you saw in my code just now. So, we set the user ID and the session ID. We set the input and output at the bottom. I pretty much just follow this to a T. So, it's not like I'm some wizard that figured

**[0:19:15]** out how to do all this crazy stuff with open telemetry. I'm just following the docs. And you can do the exact same and use the ask AI feature within the Langfuse docs as well if you want. And please take this template for yourself. The only thing that you really have to

**[0:19:28]** swap out is when you run the agent you'll have to call into your Podantic AI agent instead of the one that I have set up right here. But you can configure the trace in the same way, set all the span attributes, and then at the top here, I'll show you I have the configure

**[0:19:42]** langu function. So you can just reuse all of this and set up all your environment variables in exactly the same way like I have for everything with Langfuse. Use this as a resource to easily connect Langfuse into any Pyantic AI agent that you want. And so with that, I've got all my environment

**[0:19:58]** variables configured. I can go back over into my terminal and execute this agent. So I went out of the iterations directory because the other ones were within this folder, but now I'm within the primary folder that I'll have in the description below. And then I'll just run the padantic AI laying fuse agent

**[0:20:13]** that's hooked into all of these different MCP servers. So it takes a little bit because it has to start all the servers and then connect the agent to each of them. But we'll get a message in a second saying that everything is good to go. There we go. All right. And

**[0:20:25]** now we can ask it some kind of question where we want it to use many of these different tools and see what that looks like in Langfuse. And so the question that I'm going to ask it very simply is to get a list of large language models that I have in some table in Air Table.

**[0:20:39]** I want to research the price for each of them with the Brave MCP server and then finally use the Slack MCP to send a message with those results. And so it's just kind of a random example. I just want to have it use many of these different tools. And yeah, we can

**[0:20:53]** already see it doing so. So first it's calling the tool to list the bases in Air Table. Then it's listing the tables listing the records. We're getting a lot of tool calls already. This is exactly what I was looking for. Then after it does everything in Air Table, it should

**[0:21:06]** move on to Brave. There we So, we're making a ton of web searches based on all the different LLMs. It'll then synthesize all of those results and then hopefully just make a single call at the end to call into Slack and send that message for me. So, let's see if we can

**[0:21:19]** have that happen. Yeah, there we go. All right. So, it didn't really get that good of results for some of these LLMs but that's beside the point. I don't really care about how well this is operating right now. I didn't really set this up as the best example for it to

**[0:21:31]** really work well. I just wanted to invoke a bunch of different tools. So we can then go into Langfuse and see what this looks like. So, I'm going to go back into my Langfuse, pull up my client here, and boom, we have the input and output this time, which we can see

**[0:21:45]** at a high level, as long as all the other metadata like the latency and the number of tokens, and it looks like it tried to use the wrong Slack channel that doesn't have permission for, but again, that's beside the point. I'm not trying to create the perfect example

**[0:21:56]** here. What I want to show you is a trace like this. Look at how many different tool calls we have. This is definitely one when you want to have monitoring for your agent. when you just have so much going on under the hood. And so we can click into any one of these tool calls

**[0:22:09]** and we can see what the agent decided to do. Like in this case, it uses a Brave web search and this is the query that it used to look up pricing for the Llama LLMs. And then we can also look at the response what it got back. So this is

**[0:22:21]** exactly what the Brave API returned to our agent. And just as another example I can go down to some of the Slack requests here. Like this one is where it decided to list the Slack channels. And then this is the response that we got from listing the channels. All of this

**[0:22:35]** logging is just so important, especially when there's failures as well. And so I can even show you as a really quick example. Let me go back to the code. And on purpose, I'll add an error to one of these tools. And so when we call our Brave agent, let me just go down to this

**[0:22:49]** tool here. Instead of running the agent I'll just say that the result is equal to uh let's just say 0 / 0. Okay. So I'll force an error here. And then within my agent, I will just force close it and restart it. And then when I ask it to use the Brave MCP server, it's

**[0:23:06]** going to fail, give me an error. And then I want to be able to see that in Langfuse because that's one of the most important things for monitoring in general is just being able to watch for errors. So I can say, search the web for Elon Musk's net worth. All right. And

**[0:23:19]** then we should get an error like really really fast here. There we go. Error occurred. Division by zero. And so now I can go back into Langfuse. I should have another trace now. There we go. So, we have no input and output here because the execution failed entirely, but it

**[0:23:33]** tells us that we have these errors. You can see that on the right hand side here. So, you can set up monitoring to watch for these specifically or you can just go through your logs and look for this error and we can see exactly what went wrong. So, I can go here and see

**[0:23:44]** yep, status message division by zero. So, yeah, you can even for your full executions that are successful, it's still valuable to go and see the decisions the agent is making because maybe there's no explicit error, but the agent still made a mistake. So, that's valuable. But then also looking for

**[0:23:58]** straight up errors in all your tool calls and stuff is extremely valuable as well. And then the very last thing that I want to show you with this is we have the session and user ID set like we saw in the code. And this is really important because now we can go into the

**[0:24:12]** sessions tab in Langfuse and we can take a look at all of the individual conversations that users are having with our agent and we can even filter by user ID. You can go to the users tab and then see all the conversations that one individual user has as well. And then

**[0:24:27]** back in sessions, we can click on a given session ID and see all of our messages and responses from the agent for that given conversation as well even looking at the total cost for this conversation. So there's so much functionality that we have in here to drill down into specific conversations.

**[0:24:44]** And so you can also handle things like if a specific user comes to you and says that I'm having this issue with your agent, you can then ask for their email that you'll have tied to some user ID in something like Superbase and then you can search for that in Langfuse and then

**[0:24:57]** find their conversation. Go into the trace and then look at what exactly went wrong with the latency or if there's an error in the tool or whatever that might be. You have that control to do everything. And so definitely in a future video on my channel, I want to

**[0:25:11]** cover building out a full front end with Superbase authentication, how we can coordinate those user IDs with Langfuse and our agent to set all that up. I think that'll make for a really awesome video. And I know a lot of you following my channel absolutely love N8N just like

**[0:25:26]** I do. So I wanted to talk about integrating it with Langfuse really quickly. Unfortunately, right now there is not a native integration for Langfuse in N8N. You can't just go and search for the Langfuse node and then bake that into your workflow in any way. But a lot

**[0:25:40]** of people are looking for this because it really would be powerful to be able to monitor our agents with N8N just like we can do with our Pantic AI agents or our OpenAI agent SDK agents. And so here's an example in the community forum in N8N of someone asking for this

**[0:25:54]** integration. Got quite a bit of visibility. And also something that I really love is that Mark, one of the maintainers of Langfuse, one of the founders, he even posted here and said they'd be happy to contribute to this effort, which is so cool to see them active here looking to integrate with

**[0:26:10]** more and more platforms. And then there was an issue created for this in GitHub as well in the Langfuse GitHub. So both people using N8N want to incorporate Langfuse and people that are using Langfuse actively want to incorporate into their N8N workflows as well. There's a lot of demand for this and

**[0:26:26]** there was a post recently in the community forums in N8N. Jim Lee, he creates a lot of awesome resources for NNN in general. He showed how we can incorporate languin NN, but it's a custom setup. It's not a native integration. And so you have to use these custom tool nodes. It gets a

**[0:26:42]** little bit more complex. And the biggest downside to all this is that you have to hardcode your Langfuse authentication keys in the code node in N8N. So it's really not an ideal solution. We want something native for Naden. So hopefully this will come at some point and when it

**[0:26:57]** does, I'll definitely cover that in a video. But for now, the main thing that I have for you is that template to integrate Langfuse very easily with Pantic AI. So just take that, run with it to add that crucial observability to your agents. So I hope that this video

**[0:27:11]** has given you what you need to get started with agent observability. And I hope that I've convinced you how important it is as well. I would highly recommend against deploying any AI agent into production without having a platform like Langfuse backing you up. And Langfuse is just the best in my

**[0:27:27]** mind. It has the best features from what I've seen. And it is completely open source unlike a lot of its competitors like Langmith. And so I'm going to keep focusing on this as my observability platform and probably a lot more content coming out for it as well. So if you

**[0:27:40]** appreciate this content, you're looking forward to more things AI agents and local AI, I'd really appreciate a like and a subscribe. And with that, I will see you in the next
