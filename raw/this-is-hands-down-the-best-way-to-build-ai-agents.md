---
type: raw-transcript
title: "This is Hands Down the BEST Way to Build AI Agents"
youtube_id: U6LbW2IFUQw
url: https://www.youtube.com/watch?v=U6LbW2IFUQw
slug: this-is-hands-down-the-best-way-to-build-ai-agents
published: 2025-02-12
duration: "0:51:25"
fetched_at: 2026-07-21
immutable: true
---

## Transcript

**[0:00:00]** when it comes to building AI agents the internet is filled with guides but the problem is most of them just get you started with the bare bones and nothing more and don't get me wrong these kind of guides are really useful and valuable especially if you are just getting

**[0:00:13]** started with a topic I mean I make them myself all the time but I just know that you are looking for more you want to know how to build the best of the best when it comes to AI agents and you don't want it to be overly complex either if

**[0:00:25]** that is you then you are in luck cuz I have something very special for you today over the past few days I've been pouring my heart and soul into building an AI agent that I honestly think is the most powerful one that I've shared on my channel yet we're going to be doing a

**[0:00:39]** deep dive into using pantic AI my favorite agent framework with Lang graph an incredible agentic workflow tool to unlock an infinite number of possibilities building AI agent systems that can really do anything I mean in this video we are literally going to be building an agent that can make other AI

**[0:00:57]** agents it's pretty insane also in my last video on agentic workflows I teased an implementation that I wanted to do with pantic AI and Lang graph and a ton of you said it was a really good idea so here it is in my mind using pantic AI with Lang graph together is an absolute

**[0:01:14]** GameChanger and over the course of this video and future ones I'm going to be breaking it down for you to make it super clear both why we're doing it this way and also how we can use these Frameworks together I'll also be covering a fair warning with using these

**[0:01:28]** kind of setups why this matters you even if you're not a coder how we can do everything locally with these agentic flows and I want to share with you some big plans that I got coming up in the near future I have not had this much fun building AI agents in a long time now

**[0:01:44]** super exciting stuff so let's go ahead and dive right into it okay so before we get way ahead of ourselves and start building an AI agent let's get grounded into what pedantic Ai and L graph do for us and why they work so well together so starting here with pantic AI it is a

**[0:01:59]** python agent from framework that makes it super easy to build AI agents while still giving us all of the customizability and control that we need to manage everything with our agents like the testing the function calling and the chat history and really with pantic AI you're able to build any AI

**[0:02:16]** agent that you could possibly want and So within their documentation here they have a really good example that I reference a lot with their weather agent right here so I'll have the documentation Linked In the description you can check out this agent yourself CU it really breaks down in a clear way

**[0:02:30]** the three different parts that go into building any agent with pantic AI and honestly these three parts could be applied to any framework as well and so you start off with your dependencies and so these are the things that your agent needs like API keys or database connections to do things on your behalf

**[0:02:47]** and then the part number two is the definition of the agent itself including things like the system prompt and the large language model that you are using for your agent and then the last part of every agent you build with pantic AI and this is what takes up most of your code

**[0:03:02]** is the functions for the actual tools that allow your agent to do things on your behalf like query a database use your Gmail or in this case get the weather for a specific location so that is pantic AI our AI agent Builder now moving on to Lang graph Lang graph is

**[0:03:19]** not a framework to build AI agents that would overlap way too much with pantic AI there be no reason to use both instead it is an orchestrator it is a way to take AI agents that you've built with something like pantic Ai and combine them together in a workflow so

**[0:03:35]** that they can actually work together and reason together about the same problem that they are tackling or the same conversation with a user so if you scroll down a little bit in their homepage here they explain it very well it's an expressive and customizable agent workflow Builder and the very

**[0:03:50]** important thing with Lang graph here is they have lowlevel abstractions and essentially all that means is they don't try to do way too much for you there are Frameworks out there like crew AI that are really cool because they have high level abstractions they do a ton for you

**[0:04:05]** so that in the end you write a lot less code but the problem with that is you will hit a wall using those kind of Frameworks where you don't have the controller customizability to really get into the intricate developments of the AI agents that you are building and this

**[0:04:19]** kind of ties into what I was talking about pantic AI as well cuz both Lang graph and pantic AI they have these low-level abstractions you still have all of the control that you need and that's what is so important about using both of these tools and also using them

**[0:04:33]** together because you have all your agents built with pantic AI and then you connect them together with Lang graph and that's what we're going to be doing in this video and I even have a quick example to show you here right from the Lang chain blog so they have this

**[0:04:46]** research agent that can generate charts that is using Lang graph under the hood to basically connect all of these nodes together so I have a more zoomed in view that we can take a look at right here you can think about it as these agents like the researcher the chart generator

**[0:05:00]** the router these can all be large language models that are each agents built with pantic AI and then Lang graph is the orchestrator it's what connects all these things together so it defines all the rules for all these arrows that you see that are determining the flow of

**[0:05:14]** this agentic workflow so the user comes in with their requests like generate a chart of the average temperature in Alaska over the past decade there is a lot that has to go into this for both research and generating the chart so the first message goes to the researcher

**[0:05:28]** this is where it does things like get temperature data for Alaska and then the router decides if it has to do more research or if it can go on to generate the chart and then give the final answer to the user and you can see here that this whole flow is very

**[0:05:43]** non-deterministic it's not always the case that the researcher is going to get exactly what it needs in the first try and then it'll go to the chart generator and that'll generate the chart perfectly in the first try and then it's sent to the user that's not going to happen most

**[0:05:56]** of the time a lot of time there has to be some iteration where Maybe you research a couple times or you regenerate the chart a couple of times and the llm has that intelligence to determine if that is necessary and all that kind of non-deterministic flow in a

**[0:06:10]** workflow combining these different agents together is not easy to do without something like L graph and then creating these individual agents that have the tools to do things like research or generate charts that is not easy without pantic AI or some other similar framework and so this is how you

**[0:06:28]** can kind of start to see the power of combining these tools together to have agents that are built very easily with a flow that is managed very easily cuz all of these connections are set up as different nodes and edges in Lang graph that's what we're going to dive into and

**[0:06:41]** I'm going to make it super super clear for you last thing before we dive into what we're going to be building today with pantic AI and L graph I want to give you a fair warning for building these kind of graph agent workflows so we're over here back in the pantic AI

**[0:06:55]** documentation they actually have something similar to Lang graph they have a dedicated page for this and they have a warning for these kind of flows and essentially it's just don't over engineer there is a risk using these kind of agentic workflows built as graphs that you are over engineering and

**[0:07:11]** it's overkill for what you are actually trying to build and that's kind of what they're saying here with don't use a nail gun unless you actually need a nail gun so they're powerful tools but they're not the right tool for every job what we're going to be building today I

**[0:07:25]** do firmly believe is a powerful tool and in general when you want to build super robust agentic workflows with a lot of Agents working together in non-deterministic ways it is a really good tool but I don't want to sit here and try to tell you that this is the end

**[0:07:39]** all be all when a lot of times it can be Overkill I want to really emphasize that and by the way if you're curious why I'm not using graphs instead of L graph it's simply because L graph is way more evolved and has a lot more features some

**[0:07:52]** of which we're going to be using today so maybe at some point graphs will evolve into something I can switch to I mean in the end I'm just teaching principles here I'm not getting tied to one framework but right now we are using Lane graph so that's everything for a

**[0:08:04]** fair warning here um but don't get too scared I mean graphs and agentic workflows with graphs are still super powerful for a ton of use cases so let's dive into that now all right welcome to archon this is an AI agent that builds other AI agents all powered by you

**[0:08:20]** guessed it pantic Ai and L graph and I'm building this completely free and open source for you for two big reasons the first one is that this agent literally builds other AI agents that use Lang graph and pantic Ai and so you can use this as a resource even if you are not a

**[0:08:37]** coder to work with these Frameworks and build everything that I'm teaching here and so I'm actually going to be building this out over time into something that is super powerful and that gets into the second reason that I'm building this in the end pantic Ai and Lane graph are

**[0:08:51]** both pretty easy to work with but the kinds of things that you can build combining them together in very powerful ways are also going to be a bit more complicated so it's not easy for me in just a single YouTube video to create some masterful agentic workflow and

**[0:09:05]** share it with you using these two Frameworks so instead archon is something that I'm going to be developing in iterations as a way to teach you pantic Ai and Lang graph starting with something more simple and getting more complicated overtime in future videos so you can follow along

**[0:09:21]** starting simple and getting to the point where you are a master at these two Frameworks and using them together and So currently we're on version two that's what I'm going to going to show you how to build today with Lang graph and pantic AI version one that I have right

**[0:09:35]** here is just a pantic AI agent so no l graph and it can only build other pantic AI agents and then we'll get into version two in this video that actually leverages an agentic workflow built with both Frameworks that can build just pantic AI agents so we're still getting

**[0:09:51]** pretty simple here but starting to get into agentic workflows and then we'll get into one that can build both pantic Ai and L graph agents and then a ton of other ideas that I have here in my vision for future iterations like self feedback loops tool library integration

**[0:10:05]** supporting other Frameworks like Lane chain llama index and crew AI autonomous framework learning oh there's so many ideas that I have eventually I want to turn this into something that can actually be in an IDE like wind surf or cursor I think that'd be so cool because in the end using those tools right now

**[0:10:21]** to build with pantic AI they completely hallucinate because llms by themselves when they're not in an agent like archon that has access to the pantic AI documentation they do not know how to code with these Frameworks and so that is the value of archon that I want to

**[0:10:36]** turn into something in the end that'd be super easy uh to use and very robust and then even integrate with other things as well in the future like Docker for deployments Langs Smith mCP other Frameworks other Vector databases besides superbase a ton of ideas I'm just so excited for this both for what

**[0:10:53]** it can do for us helping us build agents but also how it can allow me to teach you in a very clear and concise interative way how to work with these two Frameworks and do some incredible things all right let's get into the code for archon and build some awesome things

**[0:11:08]** with pantic AI and L graph so all of the code that we're going to be going over here and that I'll create with you I'll have in that Aron GitHub repository that I just showed you and of course I wouldn't miss it I'll have a link to it

**[0:11:20]** in the description as well and as promised we're going to go iteratively through building archon so you can understand foundationally how pantic Ai and L graph work how they work work together and also so that you can understand why you'd want to use these more complex agentic workflow approaches

**[0:11:36]** with graphs versus when you might actually want to stay simple as well and so version one we're going to start with this here so I'm not getting right into the meat of pantic AI and Lane graph cuz I really want you to understand this because version one is going to first of

**[0:11:51]** all be a very good demonstration of how to create an agent with just pantic AI but then more importantly we're going to look at its shortcomings and that will help us understand understand why we'd want to graduate into the more complex other iterations of archon that'll be continuing to build over time that will

**[0:12:07]** leverage Lang graph as well so in the folder right here for version one of archon I have this readme which shows you exactly how to get started with specifically this version of archon and it talks to what exactly is implemented in this version as well and I'm going to

**[0:12:22]** do that for every single version I have in the iterations folder right here going forward and all the code at this point in time as well so that no matter where you jump in in this journey of archon even if it's version six you can still go through all of the versions

**[0:12:35]** iteratively to build on that Foundation start very simple and then get more complex as you work up to what version we're actually on so that way you don't have to jump in the deep and I mean that's the point of me building this iteratively in the first place here and

**[0:12:49]** so that's why we're going to be starting with version one right here and this is actually based on the crawl for AI rag agent that I've already built on my channel so I'm going to go through that pretty quickly here with version one since I've already built it on my

**[0:13:01]** channel so definitely check out that video you certainly don't have to I'll talk about it a little bit right here um but it is pretty basic overall it's a good idea for how to build a pantic AI agent and so setting up the knowledge base here all I do just like I did in

**[0:13:16]** the other video on my channel is I fetch the pantic AI documentation Pages using the sitemap build that up as a list that I then pass into crawl 4 AI to get the contents for all of them in markdown and then I chunk them all up and I put them

**[0:13:29]** into super base so that I have it in my knowledge base for rag using PG Vector so I've really changed nothing for this script at all and the readme talks about running this and getting the database set up and everything too and then for the pantic AI agent again there are

**[0:13:44]** three parts for any pantic AI agent you have the dependencies which in this case we just need superbase for Rag and then the open AI client to create our embeddings for rag then you have your actual agent creation like I have right here and then the rest of this code is

**[0:13:59]** the third part which is just all the tools that we want to give to our agent um so that it can do things on our behalf which in this case is looking up things in the database and Performing rag as well the other big thing that I have right here is this massive system

**[0:14:13]** prompt so this was the big thing that I did to refactor because originally my crawl for AI rag agent was just an agent that could answer questions on the pantic AI docs but I want to actually leverage the docs now to build other pantic AI agents and that's what I'm

**[0:14:28]** telling it that it is in the system prompt now and so I give it a a nice goal here of creating pantic AI agents using the documentations that it can fetch with the tools that I give it I Define a general structure for the different files to create for each agent

**[0:14:42]** that it makes and then a lot of miscellaneous instructions just to make sure that it's not hallucinating in certain ways and that it's following using the tools that I give it um so it's actually grounding its truth in the documentation instead of just making up random stuff for pantic AI and so it can

**[0:14:57]** perform rag with this function right here uh to match with certain chunks in the vector database and then we also have a tool to list all the documentation Pages available to it so if it doesn't just want to perform rag but actually read an entire documentation page it can use this tool

**[0:15:12]** to figure out which pages are available to it and then use our third and final tool right here to get the contents of specific Pages like maybe it wants to read up on an example in the pantic AI docs or the page that talks about defining tools whatever it might be it

**[0:15:25]** can use this function to actually do that so this agent will intell ently use these three tools together to get all the documentation that it thinks it needs to then give us all of this code right here that we have defined in this structure to produce that pantic AI

**[0:15:41]** agent for us now to actually run this agent again going back to the readme I have a streamlet interface that I set up I'm not going to go over this in detail right now just a very basic streamlet interface to work with I pantic AI agent which by the way you can use this as a

**[0:15:56]** reference point if you want to use streamlit for pantic AI so another nice little resource for you there but yeah we just will run this Command right here to spin up our interface I actually already have it up and running here um because I'm going to show you an example

**[0:16:09]** run of when I was using archon V1 just to show again the shortcomings of this so that we can talk about why we want to graduate to version two and then I'll show you how to build that with pantic AI and Lane graph together so for the example for this agent I'm just asking

**[0:16:25]** it to build me an agent that can answer questions about code in a GitHub repo that I give a URL to so essentially just the GitHub agent that I've been building as a part of my series on YouTube showing you how to build AI agents and the results that we get from this are

**[0:16:40]** okay I mean it's still actually probably better than if we were to ask wind surf or GPT or deep seek or something to build an AI agent with pantic AI cuz those guys they have no context over pantic AI they don't understand the documentation at all at least this agent

**[0:16:56]** does and you can definitely tell by the way that it set things up and used function decorators and things like that that it does understand pantic AI though I will say that the results they're not going to run right out the gate it didn't Define the agent correctly the

**[0:17:09]** tools don't look optimal to me I guess the dependencies are okay but then one big thing is it didn't say I need any environment variables even though I very much do need my open AI API key if I were to use actually it doesn't even tell me the model so that's certainly

**[0:17:25]** broken and then also we' probably need a g API key as well unless we're only going to be cloning public repos so definitely not an ideal implementation overall it kind of works and if you have specific use cases for your AI agents that might be simple and something like

**[0:17:42]** just pantic AI would suffice you don't need the added complexity of building with Lang graph as well but you can see for this use case specifically without optimizing a lot more with the system prompt or better tools anything like that I definitely need more and that's where a graph approach an a gentic

**[0:18:01]** workflow to actually make sure that it's reading through the pantic AI documentation correctly and using it correctly is super super important and so I really do want to preface what I'm about to show you by saying like maybe there are other ways to optimize besides moving to a graph approach um like maybe

**[0:18:19]** like I said better system prompts or different tools to analyze the documentation differently um maybe even bringing in the ptic AI GitHub repository right now it's just the documentation pages but like overall that might take just as much work as it is to move to this graph approach and

**[0:18:34]** I'm getting some really good results with version two of archon so with this kind of as the context as to why we'd really need that let's go on to building version two with pantic AI and Lang graph together so this is the graph for the agentic workflow that we're about to

**[0:18:49]** make for archon using pantic Ai and L graph together and that's one of the beauties of using Lang grath is you can visualize your workflows without having to put in any extra work I did not create this myself all I did and you can do this too you can go to version two of

**[0:19:04]** archon in the GitHub repo or it's at the root of the repo at the time of recording set everything up with the readme get your python environment set up and then run the command Lang graph Dev and that'll spin up this studio UI open in your browser automatically and

**[0:19:17]** then boom you'll have this there where you can visualize all the nodes in the workflow that I'm about to show you how to create from scratch and so you can already see that there's a lot more going on essentially version one was just the code coder agent right here so

**[0:19:30]** a request would come through to build an agent and this guy would perform regag look at specific documentation Pages whatever to actually produce the final agent for you but now with version two with lra we have a few different pantic AI agents involved first of all we are

**[0:19:46]** using a reasoning llm at the start of the workflow something like deep seek R1 or open aai 03 mini and this guy is going to take the requirements from the user like the agent that they want to build and create a full scope document outlining everything that needs to be

**[0:20:01]** created and it's going to pick out certain pantic AI documentation pages that it thinks the primary coder agent should use rag to look up to actually have the right context to build the agent and that alone improves the results a lot and then we have this Loop here where the agent is going to code up

**[0:20:18]** another pantic AI agent and then get feedback from the user and then iterate on that and we could go through this forever until the user finally decides yep it created a good agent let's move on this is using a really important Concept in Lang graph and other agentic

**[0:20:32]** workflow tools called human in the loop and that's something I really want to demonstrate here because llms hallucinate all the time and so practically any AI agent you would ever want to make you want some sort of human improval involved to approve certain actions before you go on to the next

**[0:20:49]** stage in a workflow to give feedback whatever it might be and so I'm going to show you how to do that right here and then once the user says that the AI agent is good then we have this final agent that kind of wraps up the conversation by summarizing everything

**[0:21:02]** into the final AI agent for you and instructions to run it as well and overall this is a pretty basic implementation in Lang graph but that's where I want to start with version two of archon and a lot of the things that I chose for the general structure of this

**[0:21:17]** graph is more just to teach you all the concepts that I really want to focus on like human in the loop and then through future iterations of Aron that's when we're really going to hone in on the things that actually make it work the best and really start to build this out

**[0:21:30]** into a full workflow that'll avoid a ton of different hallucinations with creating agents and and things like that right now starting simple but we still get a lot better results so let me show you this really quick so exact same question that I asked version one of Arcon and this time we definitely get

**[0:21:48]** some better results so first of all we even get like a little bit of a breakdown initially I mean just the fact that we give this scope document from the Reasoner into the coder means that it just has so much more information to pull from to give us a more robust

**[0:22:02]** response so we get a file breakdown here then we get the code implementation the tools are looking a lot better it defines the agent and actually specifies in llm now I mean maybe not the choice we'd want necessarily with GPT 40 but it defines it correctly and then we have

**[0:22:17]** the tools populated the prompts file populated the environment variables actually make sense this time and it's not all perfect right now but it still looks so much better and even gives us some additional instructions as well just like you can tell that there is a lot more involved in giving me this

**[0:22:34]** response compared to archon V1 and it's all thanks to this agentic flow that has a Reasoner a feedback loop and then it's got an agent at the end that can help summarize everything with instructions as well so with that in mind we can really start to see the power of using

**[0:22:50]** pantic Ai and laying graph together now let's actually go and implement this graph from scratch here we go let's get into building archon V2 together we're going to do it completely from scratch because as I promised earlier I want this to be a true Deep dive into building with L graph and integrating it

**[0:23:07]** with pantic AI as well so just like with V1 we have this read me here that shows you how to get everything set up including running things locally as well so just to make things quick right now I'm going to be using open AI but I've actually tested this agent with deep

**[0:23:21]** seek R1 distill 7B for my Reasoner model and quen 2.5 instruct 14b for my coding model and and it actually kicked butt I got some really good results using those local llms the only thing I will say is you still need open AI for the embeddings model that's a dependency

**[0:23:38]** that I'm going to get rid of in future versions of archon so that you can do things entirely locally but you can have your agents be local and I got some really good results with that so follow along with this Remy to get everything set up just like you would with V1

**[0:23:50]** couple of other things to get set up as well but the thing that we're going to be building from scratch here is our graph that will actually tie all these agents together including the pantic AI coder agent that we still have as the core agent within this workflow here and

**[0:24:05]** as we're building out this graph I'm going to be showing this UI pointing out the different nodes that we're building just to use this as a visual reference to make this entire walkthrough as clear as I possibly can because even though this is a more simple L graph

**[0:24:20]** implementation there are still a lot of moving Parts here and different agents that we have to build and work with and so I'm going to be using this a lot to make that pretty nice and clear and so yeah let's go ahead and start building our graph for archon v2 now if you bet a

**[0:24:31]** 100 bucks that at the start of all of my Python scripts I import my packages as my first step you're going to get $100 every single tutorial that I have here so yeah first thing importing all the packages that we need for things like Lang graph and pantic AI as well then

**[0:24:47]** we'll load in some of our configuration like our environment variables which you can set all that up before you run this so be sure to create your own version ofv based on the example here fill in Things based on if you want to use llama for local llms go through open AI

**[0:25:01]** whatever it might be and then hook in your super base as well and then we're also going to not use log fire for our loging monitoring that you can use with pantic AI it's built in I'm going to turn this off for now but we'll configure this later for archon as well

**[0:25:16]** then we're going to pull in our environment variables and so we have our base URL this is how we can configure if we want to go through open AI or olama or open router and then we have our llm API key that we're going to need need for anything except for olama obviously

**[0:25:31]** with AMA we don't need that because it's running entirely locally on our machine and then we also want to determine if we are running olama based on if Local Host is in our base URL and the reason that I'm doing this is because olama within pantic AI doesn't support streaming like

**[0:25:47]** the other providers do I'm not really sure why I think it's a bug in pantic AI that I really hope they fix because right now when you use AMA you have to wait for the entire output from the LM before you can display it to the screen instead of having it type out the

**[0:26:02]** characters as it is producing them and so we'll just see a little bit of a difference there in how we call our pantic AI agents if we're using olama or not the next thing that we want to do is Define our Reasoner agent and so this is our first pantic AI agent that is going

**[0:26:18]** to be responsible for basically managing this first node here that we have in our workflow to actually create the scope for the AI agent that we are building and so it's going to be an open AI model but we're going to override the base URL which is how we can use a local llm or

**[0:26:33]** not and same with the API key and then the model we're fetching this from our environment variable and we're just going to be defaulting to 03 mini if nothing is specified but you can set up a custom AMA model that you've created like I built this one that also has a

**[0:26:47]** larger context link so it doesn't mess things up a bunch and that's this is where you set up your Reasoner model and then we create our actual pantic AI agent with the system prompt as well just keeping it super super simple and then we want to create our router agent

**[0:27:03]** and so this guy is just going to use the same llm as whatever we use for our coder agent like GPT 4 mini uh quen 2.5 instruct whatever it might be and the reason that we need this agent here is because we have to determine within this Loop when we want to break out and

**[0:27:18]** actually end the conversation so the router is going to take the latest user request and determine are they saying the agent is good and we can continue to finish the conversation or do I have to go through another loop here and go back to the coder agent so that's what this

**[0:27:33]** guy is going to be responsible for we'll build that node later as well and then we have our final agent when the conversation is ended this agent its only job is just to kind of summarize a conversation give the code for the agent and then instructions for running it as

**[0:27:47]** well so the user can take the end of that conversation and just copy those commands to execute the agent on their computer so that's everything for our agents and now we just needed to find dependencies for all of these pantic AI agents so we have our open AI client

**[0:28:03]** which we need for the embeddings for Rag and then our superbase client as well to actually perform rag in our superbase database and then the first thing that we need in Lang graph whenever we Define any graph here we can't just go right into defining all these nodes and

**[0:28:20]** connecting them together we have to manage the state for our graph and so let me actually show this here all the different items that we have right here here that we can see in the Lang graph UI these are all pieces of information that we want to keep track of throughout

**[0:28:35]** the entire execution of the graph like the messages for example it doesn't matter which node we are in we need this more Global state that keeps track of things that the entire conversation cares about like the scope that the Reasoner creates that we might want to use in any of these uh nodes or the

**[0:28:54]** message history that we're going to use in pretty much every single one of these except this guy right here and so all that is defined in global state for our graph and so for a specific execution of our graph like creating a single AI agent these things are going to be set up individually for

**[0:29:11]** each execution of our graph and so you have something like maybe a conversation ID or a thread ID you pass that into Lang graph and it's going to manage the state independently for each one of those conversation IDs essentially so you can have multiple executions of the graph all on at the same time and

**[0:29:29]** they're all going to manage separate State and that's how you can have these different conversations happening all at once um so that's our state now we can Define our first node and this is going to be the defined scope with Reasoner so this first guy right here we are now

**[0:29:45]** creating the actual node that's going to use the Reasoner agent that we already set up and this one is going to be pretty simple first of all we're going to use this function that we have from the pantic AI coder I'll just show this right here let me scroll down this one right here

**[0:30:01]** this function to fetch all of the pantic AI documentation pages that are available in superbase and then we're going to Define our prompt which is going to ex include all these documentation Pages as well so we're telling the Reasoner model that we want to create a scope a document that

**[0:30:20]** outlines everything that we have to create for our AI agent and we're also telling it to pick out a few documentation pages that it thinks are relevant for creating this agent this is a little rudimentary there's probably much better ways to use a Reasoner to set the stage for this graph um but

**[0:30:37]** still a really solid example here and so now to actually leverage this Reasoner it's very simple with pantic AI just Reasoner do run we get the scope from the result we'll even write it out to a file here so we can see the results um after it executes I'll show this right

**[0:30:52]** here we'll get something that kind of looks like this I'll just kind of open that preview for the read me here so this is a scope um that g gbt 40 mini actually produced um so when I showed you that example earlier with version two of archon I actually used 40 mini

**[0:31:06]** for my Reasoner just to not be kind of unfair to version one because 03 mini is so powerful that 40 mini is a much fairer comparison to use for Reasoner LM When comparing to V1 but anyway so that that's the scope document right here and then we're just going to return

**[0:31:25]** the scope of scope so in Lang graph when you want to update the state the global state that we're tracking for this execution of the graph at the end of Any Given node you just have to return an object where you have the key that maps to the specific value that you want to

**[0:31:41]** update and then the value that you actually want to update it to so when we first execute our graph we're at the starting point right here the scope value is just going to be undefined or maybe whatever we start the graph with but once we Define the scope with

**[0:31:58]** Reasoner we actually have this state updated so then scope is going to permanently have this value that the Reasoner defined unless we change it in some other node in the graph and so that's how we update the state and that's going to stick with us forever so we can now use this scope as a value

**[0:32:15]** that we put into another prompt in another node for example that's actually what we're going to do in a little bit here so that is our very first node next up we want to create the node for our coder agent and again as promised just going through this as our visual

**[0:32:29]** constantly here we're creating our coder agent now so this is the main guy in this workflow it's going to be doing most of the work pretty much especially if the user has a lot of feedback they want to give to the coder agent and this is going to be using our primary pantic

**[0:32:43]** AI Cod or agent that we're using in V1 but this time we're giving it a lot of extra context as well that the Reasoner gave in the scope and so we're creating our dependencies here which is going to be the superbase client and the open a client just like with with V1 of arcom

**[0:33:00]** but now we have this third dependency here because we want to inject the scope that the Reasoner created dynamically into the system prompt for our pantic AI coder agent and so I added this third dependency here so pantic AI coder dopy it's exactly the same as what we have

**[0:33:18]** for the same file in V1 except I have this third dependency here and the way that you can dynamically inject things into the system prompt is in pantic AI you can reference at and then the name of the agent like at pantic AI coder do system prompt and

**[0:33:38]** just like the tools like we have the retrieve relevant documentation tool we have this context that pantic AI automatically passes in as a parameter to the function and it does that for these dynamic system prompt functions as well and so we can reference the Reasoner output from the context and add

**[0:33:58]** add that into the system prompt so whatever we return from this function is added onto the primary system prompt that we have right here and so that is how we are able to dynamically add whatever scope the Reasoner puts out into the system prompt for our coder agent and the reason we want to add it

**[0:34:16]** into the system prompt is the system prompt is where you define the behavior and the general rules for your agent and definitely the scope of what we are creating is more of a overarching thing that we want to have have in the system prompt instead of somewhere in the

**[0:34:30]** conversation history so I hope that makes sense you can look at the pantic AI documentation for dynamic system prompts if you want to dive into it anymore but that is why we are adding this as a third dependency for our pantic AI agent and then we're going to

**[0:34:44]** get all of the conversation history that we currently have in the state right here I mean when we first execute it's going to be an empty list but as we're getting feedback from the user this message state is going to be built up over time and I'll show how we do that

**[0:34:58]** in a little bit as well so we have to fetch this and then we're um using this model messages type adapter from pantic AI to turn this into the format that we can actually pass into a pantic AI agent so that's really important to keep in mind that the format that we store the

**[0:35:17]** state in for the messages this is a different format than what we actually need to give to a pantic AI agent so we have to do a little bit of conversion when we get the results from the agent and also when we refetch the message history to pass back into the agent and

**[0:35:34]** I'll show more what that looks like in a little bit as well so we get our message history and then if we are running with olama we can't actually stream the output to our interface and so we have to use this concept of a writer which we can pass into any function that we want

**[0:35:50]** in Lane graph this is given automatically into any function that we want and we're just going to call our agents so pantic AIC coder run we give it the latest message from the user as the current prompt pass in our dependencies and then we pass in the message history that we created right

**[0:36:08]** here as well so that's how we call our agent by the way the way that we get the latest user message from the state this is actually passed into the graph through whatever user interface we are using so again to explain this clearly I'll go back to my graph right here when

**[0:36:24]** we execute our graph for the first time latest user message is what we pass in so I'd say like hello and then that goes through the graph here the scope is defined maybe a better example I can say build me a weather agent so this is going to be our first

**[0:36:41]** message from the user so that scope is defined and then we go into coder agent where the scope this is going to be defined as whatever the Reasoner specified and then the latest user message is going to be whatever we specified when we started the graph um and so the way that we do that in Lang

**[0:36:57]** graph I'll just show that really quickly here when we execute a lang graph graph in streamlet we just pass in this object right here where we say that the latest user message is whatever they inputed into the streamlet UI and so we leverage this within our node right here the

**[0:37:15]** state within the state we're getting the latest user message and again this is one of the things that we have defined right here in our Global State for the graph that's how we get the message from the user so we rely on the interface right here here our UI to pass in this

**[0:37:31]** value to the start of our graph so I hope that makes sense and then we just write out the results this is kind of mocking a stream right here because we want streamlet to be able to expect things to be streamed out in case we aren't using AMA um but we also don't

**[0:37:46]** want to we we can't use pantic AI streaming with AMA for some reason so that's just kind of a little thing I hope that they fix here but anyway if we are not using olama then we can actually use the run stream command to stream out the output get the chunks one at a time

**[0:38:02]** to put out to the front end in real time so again we're using the latest user message State the dependencies and the message history and then as we are receiving the chunks asynchronously we are going to write them out to the front end and that is it and now we have our

**[0:38:19]** result from our pantic AI coder so at this point we have version one of our AI agent that it's created in this node right here so at this point we've executed these two now it is time to get feedback from the user whether or not we want to

**[0:38:35]** continue on to finish the conversation or iterate more on the agent and so first of all we want to take the messages that we got back all of the new messages that we got from this conversation which will include any tool calls as well this is super important

**[0:38:51]** this will include all the results from Rag and everything that we can add into the conversation history so that the agent retains that cont context that's super important we're adding these on to the messages so now the messages state is going to include all the old messages the user prompt and all the new messages

**[0:39:09]** and Tool calls and stuff as well so that's how we're building up the conversation history over time so now the next thing that we want to do is add in this human in the loop interrupt because now it's time to return to our streamlet interface or whatever interface that we are using for

**[0:39:27]** our us Y and get the next message from the user conversation and another way that you can do this is you could just end the graph and then have a complete reentry when the user's next message comes in I just wanted to set it up this way to show you human in the loop

**[0:39:41]** because essentially what we're going to do is we use this concept in L graph called an interrupt that's essentially their way to do human in the loop so we have this interrupt and this object right here is how you can pass certain values into the front end like maybe the

**[0:39:56]** agent is requesting a certain kind of feedback so you would add that into the object here to display in the front end in this case I don't actually have anything extra that I want to display so I just have an empty bracket here and so it's going to essentially on the front

**[0:40:09]** end just look like it's time for the user to enter in their message so they type in whatever they want and then I'm setting the latest user message to whatever that value is that comes through when I call the graph again after that human in the loop interrupt

**[0:40:23]** and so in my streamlet code right here you can see that if I'm starting the conversation I invoke the graph this way but then if it is a continued conversation I use this command narrative right here and I'm resuming with the value of user input and so I'm

**[0:40:41]** not going to get too technical in explaining exactly how this works but essentially using this Command right here is how you resume the graph at the current execution and whatever you pass in right here for resume equal is what is given as the value and then we're returning this object right here

**[0:40:58]** because now we are updating the user messages state with whatever they typed in when we have that interrupt so I hope that makes sense that is this node right here so now we're going to resume execution back to the coder agent and I'll show you at the end of this code

**[0:41:13]** how we actually set up all of these different nodes and their connections as well U but let's actually finish defining all of these nodes here um because the next one that we need to Define is our router and this is the agent that is going to to determine did

**[0:41:29]** the user say that the agent is good and we can finish the conversation or do we have to go back to the coder agent and so this is my prompt for that based on the latest message from the user that we just set right here I'm going to see if

**[0:41:43]** we want to end the conversation or continue and I could use structured output there definitely is a better way I could do this but this works pretty well haven't had an issue with this we're just going to run the router agent with this prompt and then the next

**[0:41:53]** action is either going to be finish conversation or it's going to be coder agent so if it's finished conversation then we're going to move on to the last node in the graph otherwise we're going to loop back so that's what this does right here all you have to do with Lang

**[0:42:10]** graph for your router nodes is just return the name of the node that you want to go to when you have a choice between going to one or the other and we'll see that in a little bit when we actually Define the connections between our nodes at the end of this file here

**[0:42:26]** all right so now very last node that we got here this is the one to finish a conversation and so just like the other coder agent node we create the conversation history that we want to pass into pantic Ai and then if it's AMA we just call the end conversation agent

**[0:42:42]** again just kind of mocking the stream here we're just running synchronously in this case everything else is kind of uh set up the same here um and then otherwise we're going to call our run stream on our end conversation agent and so again with the system prompt we're

**[0:42:58]** telling the end conversation agent to just kind of summarize the conversation give the final code for the agent and then the instructions to run it as well so we're just going to stream this out to the front end all the chunks for that last message there uh finally update the

**[0:43:11]** messages in our state so that the conversation history is updated again just like we did with our coder agent a very similar setup here and we're using Json for the message State here so again we're turning this into a format that we actually want to store so it's actually

**[0:43:28]** binary Json it's kind of weird that pantic AI does it this way but when you fetch the Json from the new messages from calling a pantic AI agent it turns it into binary Json that's what we're putting into this messages state right here and then when we convert it back

**[0:43:43]** into the what we want to pass into pantic AI using the model messages adapter we're turning it into um whatever format like the objects that pantic AI uses to represent the different messages from that binary Json on so that is it so now we can create this Builder right here based on the

**[0:44:02]** state that we have defined for our graph and we can add in all of our nodes so we have our scope definer with the Reasoner llm our coder agent the one that has the interrupt to get the messages from um us and then finally our finished conversation agent and now we get to set

**[0:44:19]** our edges and so what we just defined here is all these individual nodes but now we have to Define how they all connect together and so first up the start of our graph is going to immediately connect to the Reasoner node then we're going to connect the Reasoner

**[0:44:34]** to the coder agent there's no routing at this point it's just straight shot that goes right to the Reasoner then right to the coding agent and then the coding agent goes right to that node that gets the next message from the user and then this is where we get into a conditional

**[0:44:49]** Edge because now we're finally at the point where we have a decision to be made this blue node right here can either follow this this blue arrow or this blue arrow and we have to figure out what that is and the way that we do that is we use the route user message

**[0:45:04]** function so that's this one right here this one that we defined that Returns the name of the next node to go to so if we return coder agent we're going to go to this node right here otherwise if we return finish conversation we're going to go to finish conversation very nice

**[0:45:21]** and easy to understand how these conditional edges work in Lan graph these are the kind of things that Lan graph really helps you with like wouldn't be easy to Define all of these pantic AI agents and start connecting them together without having a tool like Lang graph to orchestrate it all

**[0:45:37]** together have these simple routing functions have all this Global State defined that you can update super easily I mean I hope you can really see how using a tool like glang graph is so powerful and then using pantic AI to create all these individual agents that are super easy to run I hope that you

**[0:45:52]** can just see the power of using these together and then we just have our final edge here which finished conversation just goes to end and then we add in our memory so that we can actually have chat persistence for L graph and then we compile our graph and that's it it is

**[0:46:06]** that easy and also this is using inmemory uh for storing all of the state for each execution of the graph I would highly recommend using a sqlite or postgress memory saver um which you can look at the L graph documentation for that definitely going to be adding that

**[0:46:23]** in for future iterations of archon but just keep things simple right now everything is just running in memory so when I execute my python script and I've just got it running in the terminal here it's going to just be storing all the things in my Ram for um you know the

**[0:46:36]** chat histories and the scope and everything that I have defined in the state right here so that is everything for our graph took a little bit to go through that that was yeah like a solid 20 minutes of walking through everything with L graph but I really did want this

**[0:46:50]** to be a super comprehensive overview of everything that goes into this and if you have any questions at all for anything that I might have explain the best and maybe the visual didn't really help you understand how something might have worked just let me know in the comments I love to help you understand

**[0:47:05]** anything that I didn't do a deep enough dive into here but I'm going to continue to on my channel just keep doing deeper and deeper Dives in a l graph and pantic AI because it is really incredible the kind of things that you can build with this and then I'm not going to go over

**[0:47:19]** the streamlet interface a ton right here but like you can see it's only like 115 lines of code like overall setting up an entire chat interface to work with a lang graph implementation is super easy and the way that you call it right here I went over this a little bit already

**[0:47:34]** but you just run this a stream command on the agentic flow so what I created at the very bottom right here is what I'm importing in my streamlet UI this right here and that's all I'm using right here so let me go back down to it so I'm

**[0:47:47]** calling a stream again passing in the latest user message either when I'm continuing from a human in the loop or at the very start of the conversation and then the way that I get this custom writer that's the kind of the last thing that I want to cover right here when you

**[0:48:01]** see that I have the uh writer that's passed in to coder agent and also passed in to finish conversation this is automatically injected when I tell stream or tell Lang graph that I want my stream mode to be custom so there's a lot of little things that took me a bit

**[0:48:20]** to figure out for you so I hope this gives you a lot of value not having to go through the pain that I had to just to work through a couple of the the little glitches to make sure that Lang graph and pantic AI could actually work really well together so I hope that you

**[0:48:32]** find that super helpful um so that that's that and now let's just go go through another Quick Test here and just have fun with this now that we have a build if you have made it this far congratulations this was not a super simple implementation but I hope that

**[0:48:44]** you can see how powerful this really is and I hope I made it very clear for you as well and that those graph visualization helped too but now we get to actually play around with this and have fun I know that we tried it out already earlier when I was comparing it

**[0:48:56]** to V one but let's just have some fun with this so I'm going to use the full power now with 03 mini for my Reasoner and gbt 40 for the main Cod agent just going to build the example that I have right here just a simple web search

**[0:49:09]** agent let's see how it does and so yeah we got the terminal right here we can watch things come in in real time first we have 03 mini that's going to create that scope document for context for our coding agent and 03 mini is not the fastest because it's a Reasoner model

**[0:49:24]** but I mean actually that was pretty quick so we're already going over to our pantic AI coder agent that is performing rag looking at the documentation pages and now also getting those pages for extra context right here from the pantic AI docs and look at this this is so cool

**[0:49:39]** so all right we got our dependencies right here which is our HTTP client and our brave API key we're using open AI gbt 40 for our model it's got a system prompt it's defining the dependencies correctly this is looking really really good then we've got our tool that's got

**[0:49:55]** The Decorator this is looking good we got our brave API from the pantic AI context this is looking incredible Perfect Tool implementation main function looks good and then it tells us that we don't need anything in the tools and prompts because it has it defined all right here and then for our. example

**[0:50:13]** file it looks like it missed the open AI API key I think we would probably need that but at least it has the brave API key so not perfect I mean you can definitely see why we're going to need future iterations of archon um but this is looking so good compared to archon V1

**[0:50:30]** trying to build this kind of agent with GPT or cursor or any kind of AI coding assistant this absolutely knocks it out of the park just so cool to see the kind of things that it can build so absolutely phenomenal all right that is a wrap for our Deep dive into pantic Ai

**[0:50:45]** langra and archon and trust me I have some big plans with archon I really want to turn this into a revolutionary open- Source agent that can completely change the way that we build agents and and make these coding Frameworks accessible to non-coders as well so definitely stick around and tune in future content

**[0:51:03]** as well if you are interested in archon or just interested in using pantic Ai and L graph because I'm going to keep using archon as a way to teach all this stuff in a very clear and concise way so if you appreciated this content and you're looking forward to more things

**[0:51:17]** with pantic AI and Lang graph I would really appreciate a like and a subscribe and with that I will see you in the next video
