---
type: raw-transcript
title: "Introducing Archon - an AI Agent that BUILDS AI Agents"
youtube_id: GjR5UsVGE60
url: https://www.youtube.com/watch?v=GjR5UsVGE60
slug: introducing-archon-an-ai-agent-that-builds-ai-agents
published: 2025-03-02
duration: "0:21:56"
fetched_at: 2026-07-21
immutable: true
---

## Transcript

**[0:00:00]** today it is my pleasure to officially introduce to you archon an open- Source AI agent that literally builds other AI agents and I've covered it a bit on my channel already but I haven't given it a proper introduction or shared with you the crazy Big Ideas that I have for it

**[0:00:16]** I'm going to be using it both as a teaching tool and also to eventually build it into an absolute monster of an AI agent that spins up other agents on demand and I'm doing it all in public for you to follow along learn from and contribute to if you want to be a part

**[0:00:32]** of something big and if we do this right Aron could easily be one of the most important AI agents out there just hear me out on this coding is hands down the biggest and strongest use case for AI right now and I'm not just trying to get you on a hype train using AI to code

**[0:00:48]** really does seem to be top of mind for everyone including every company building llms just look at the huge coding Focus for Claude 3.7 Sonet deep seek R1 quen 2.5 coder and I am all over this right now because there is a gold mine of opportunities for us to build AI

**[0:01:06]** apps that use llms to help us write code cuz here's the thing there are a lot of generalist AI coders out there like winds surf cursor and Klein but not a lot of specialized AI agents that can get the job done really well for a specific framework or tackling specific

**[0:01:24]** problems we have some specialized tools like bolt and lovable for creating incredible front ends but what about an AI coding assistant that creates other AI agents runs them and iterates on them and we need this because it's becoming increasingly clear that AI agents will dominate the landscape of software going

**[0:01:42]** forward and if you can create specialized agents on demand that tackle all of your problems well then you my friend own the world and that is why I'm building archon you can think of it like bolt but for agents instead of front ends and a lot more so let me show you a

**[0:01:57]** demo of it right now and then stick around because I'll share my crazy vision for the project as well so archon can be run in two ways first as a standalone app with a dedicated interface that I'll show later but also and this is what gets me really excited

**[0:02:11]** you can use archon as an engine to build AI agents within AI idees like I'm showing wind surf right here you can do the same with something like cursor and Klein as well and So within my wind surf this is using the model context protocol from Claude I literally have archon as a

**[0:02:28]** tool for wind surf to use you can kind of think of it as a sub agent when wind surf realizes it needs that specialized agent intelligence it'll invoke archon to generate the code and then that code will be returned to windsurf and then implement it straight away in my

**[0:02:42]** development environment it is super neat and so going over to this interface that I'll cover more later for archon I have this service up and running for archon which is the core of my mCP server and then I even have an mCP tab here that shows you for each of these coding

**[0:02:56]** assistants the exact configuration to put in for mCP and how to do all that as well so I make it super easy to get up and running with wind surf cursor and Klein for archon all right so now let's give archon a spin in Wind surf I'm just

**[0:03:10]** going to create a very basic agent right now in more dedicated videos later on I'll build out more complex use cases and it just will make more sense as I build out archon so right here simple AI agent that uses the brave API to search the web and we can see right away that

**[0:03:25]** wind surf is getting into using the archon tools and now it is actually invoking our agent with this tool call right here and we'll see in a little bit that we can watch the logs and in the archon UI as well when it's making the request to our mCP server and the thing

**[0:03:40]** that I want to really emphasize here is that you can use a generalist AI coder like wind surf like I can go and reference the pantic AI documentation or the Lang graph documentation like this to have wind serf build these agents with the same Frameworks that archon uses but because these AI ID are so

**[0:03:58]** generalist it never works as well as I want want it to and that's why we need something specialized like archon that knows how to work with these Frameworks through instructions that we give it through better rag retrieval from the documentation so many opportunities that we have to implement these

**[0:04:13]** specializations and so right here we got the result back from archon it told wind surf the files to create and so now it's going ahead and creating these all in my development environment following the exact structure that I tell archon to produce where we have this agent right

**[0:04:27]** here that is producing literally perfect pantic AI code I mean I'm just kind of glossing over this right here but this looks perfect and then it generates an em. example file so it thinks about things like our environment variables and the requirements that we have as well and even generates a readme that

**[0:04:41]** helps us get started with this agent which is just absolutely beautiful and we can even go back here and ask it to iterate on the agent and then archon will be invoked again to update the code for the agent and all the updates that it gives back to wind surf wind surf or

**[0:04:54]** your AI IDE will edit the necessary files so you don't have to rewrite anything from scratch and this entire time within the UI for archon we can see the logs like these are the logs from when we used archon just now and then any future iterations will show up here

**[0:05:07]** in real time as well so it's easy to track everything happening in the mCP server as well it's just such a good combination to use Aron along with an AI IDE because we don't want to build another VSS code Fork we want to focus on creating archon is as this

**[0:05:23]** specialized engine to right now work with pantic AI and L graph but also I want to implement in the future basically every framework that we have like crew AI llama index and autogen all of these so that archon can be this AI agent generator and so super cool stuff

**[0:05:38]** it does take a couple of extra credits because you have to use the llm calls in both archon and your AI IDE but if this can stop a lot of hallucinations and make it actually generate agents faster in the end that is going to save you a lot of credits and that's the most

**[0:05:53]** important thing is we want to be developing agents correctly and we want to do it quickly and so right now I'll show you how to get up and running with archon and then also I want to show the crazy ideas that I have to take archon from its infancy where it is now into

**[0:06:07]** something that truly is an absolute monster to generate AI agents on Dem man not only creating the code here but also iterating autonomously and running these agents itself that is going to be the dream so here is the GitHub repository for arcom which I'll have a link to in

**[0:06:22]** the description of this video and I have covered already on my channel how I built archon from scratch so I'll link to that video right here but essentially archon uses a combination of my two favorite Frameworks pantic Ai and Lang graph for this agentic workflow that can intelligently build agents much better

**[0:06:40]** than General AI coding assistance and I'm building archon in iterations for two reasons first I'm building in public I want you to be able to contribute and follow along as I'm building out archon and then also I'm building an interations because I'm using this as a teaching tool to show you how to build

**[0:06:58]** more complex agents with pantic AI and L graph and so when I have to explain something more complex like this I want to break it down into simple steps and so the iterations of archon are those simple steps so starting with a simple agent then implementing Lang graph for a

**[0:07:12]** more powerful agentic flow for agent creation and then I added in mCP support in version three and then the most recent version is where I added in that huge streamlet interface for you to manage everything for archon and the reason that I'm focusing on pantic AI and L graph specifically is because a

**[0:07:29]** lot of the the other Frameworks out there like Lane chain for example they are what's called an abstraction distraction in my mind they try to implement so much for you that you lose a lot of that customizability and control that you want when you're building your AI agents but I don't feel

**[0:07:44]** like I lose that with pantic AI and L graph I do want to integrate other Frameworks at some point though more on that later but that's why I'm focusing on these Frameworks and so yeah there's just so much that you can read here as far as the vision and future iterations

**[0:07:58]** of archon I'll get into that more in a little bit but as far as actually getting up and running with archon I've made it as easy as I possibly could so if you scroll down a little bit in the read me you'll see the first option to install with Docker it is just three

**[0:08:12]** commands get up and running so stinking easy you can install with just python if you want as well just a couple of more commands Docker is the preferred way but either way you'll have that streamlet interface up and running that'll walk you through setting up everything for archon like the environment variables

**[0:08:29]** your agent service for mCP your documentation for Rag and it'll help you knock them out one by one super quickly so it is very easy to get up and running and I might do a dedicated video later on where I show how to get archon up and running from scratch but I hope that

**[0:08:43]** these instructions make it easy enough to do it for yourself and I know that people have already been doing that so once you have archon up and running with Docker or just pure python the first tab in the interface is this intro tab that'll get you started with everything

**[0:08:56]** that you need to have archon up and running either within the chat interface that we have right here in the UI or as an mCP server like I demonstrated earlier so it walks you through setting up your environment variables your database which is using superbase the documentation crawling which is just

**[0:09:13]** pantic AI right now but I want to use a lot of other docs later on and then setting things up for mCP as well and so each of these tabs I have poured a lot into making absolutely perfect so you can set all of your environment variables right here in the UI for

**[0:09:27]** example so you don't have to do anything with a andv file and this helps you set up everything for your database as well crawling the documentation making sure you have things set up that you have your table setup before you crawl the documentation and create everything for Rag and then we have the documentation

**[0:09:43]** tab which I won't show this right now it's super cool how you can click this button and it'll run that crawl for AI python script behind the scenes to crawl the pantic AI documentation and then update you in real time as it's processing each page of the docs and

**[0:09:58]** then future sources come as well and then we have the agent service that I showed earlier where you can watch the logs for your mCP server and then the setup instructions for your different AI idees like Klein cursor and windsurf both with Docker so if you set things up

**[0:10:15]** with Docker there's one way you have to configure it versus the pure python implementation there's another way and these uh configurations are Dynamic to your operating system and the path that you have to things like the mCP server script and then we have the last section right here this is what I want to spend

**[0:10:31]** some time on I created a dedicated section of this archon interface just to detail all of the future iterations that I want to implement because I don't want to just explain that briefly in the readme I want to put a huge emphasis on the big plans that I have for archon so

**[0:10:50]** I have this dedicated page outlining everything in excruciating detail because I want to show you the vision that I have and really hope get you behind this as well so the first big thing that I want to knock out next with archon going into version five is a

**[0:11:07]** multi-agent coding workflow and what I mean by that I have this graph here that outlines this nicely I want to take the primary coding agent that I just showed you in the agentic workflow and split it up into sub agents that specialize in different parts of the code generation

**[0:11:22]** like one to create the prompt another to define the tools for our agent another to create the dependencies for things like dat based connections and API keys and then one to create the instance of the agent itself and Define things like the large language model to use and I

**[0:11:37]** want to do this for two reasons the first one is there is a huge use case with agentic workflows to have different llms tackling different parts of a problem kind of like what we're seeing right here and then come together to aggregate everything into a final result for the user and again archon is

**[0:11:54]** partially a teaching tool and so this is a great opportunity for me to demonstrate this huge use case in a IC workflows with something practical and then the other reason I want to do this is in general just because you can give a lot of instructions to an llm just

**[0:12:07]** because the system prompt and all the tools can fit in the context window doesn't mean you should do it because llms can get overwhelmed when you give them too much to do and so splitting our coder agent into different sub agents means we have these specialized parts of

**[0:12:23]** the workflow that handle different things so we should get much better results and I've implemented these kind of work Flows In other projects it definitely does improve the results a lot so I'm looking forward to version five a lot and then going into version six I want to develop a tool library and

**[0:12:39]** example integration so essentially giving pre-built tools and example agents to help archon create new agents better because with the tool Library if we have something like this I mean this is a very preliminary look at what the configuration might look like we have all these tools that are predefined for

**[0:12:56]** something like web search or querying a database and so that way when archon builds the agent it can use a tool that looks like this that's already defined in an agent in a very simple way so that instead of archon having to build that tool from scratch it can pull it from

**[0:13:10]** the library and inject it right into the code and so that way we don't have to worry about hallucinating the creation of tools when that's a tool that's already been built a thousand times we might as well just have that ready to be pulled in whenever an agent needs

**[0:13:23]** something like a weather tool or the ability to query a database and it's the similar kind of idea with example agent so instead of having to Define this structure from scratch for an agent it can look at an example agent like the weather agent that we see in the pantic

**[0:13:38]** AI documentation so using this as its grounding Point what does a basic pantic AI agent look like so we can use this and then build on top of it for any more complex use cases that we'd want to make with pantic AI and then going into version seven I want to include the Lang

**[0:13:56]** graph documentation within archon's knowledge base so we have more than just pantic Ai and this is where we get into archon being able to work with more and more Frameworks so as a starting point adding in Lane graph as well but then I want to add in crew Ai and llama index

**[0:14:13]** I'll get into this more in another version but this is a kicking it off essentially making it so that instead of it being hardcoded to use pantic AI for everything we can start to incorporate other Frameworks allow the user to choose which framework archon will build and maybe even have it intelligently

**[0:14:29]** determined and based on the agent that it's building should it use just pantic AI or should it use Lang graph and pantic AI together and then once we have another Frameworks maybe it chooses to use one of those instead just depending on what we are building exactly and so

**[0:14:43]** this is an example of a l graph agent just showing more complex agentic workflows that you can't build with only pantic Ai and so adding in L graph to the capabilities of archon is just going to make it be able to build more and more complex use cases which we need for

**[0:14:59]** the AG agents that we have in the real world solving these important problems for us then going into version 8 we get back to improving the agentic flow for archon itself with self feedback loops right now archon when it produces the Asian code immediately goes to you as

**[0:15:13]** the user to give feedback but what if you want it to autonomously iterate on the agent sometimes it knows better than you what it needs to work on or maybe the hallucinations are kind of silly and it's easy enough for the llm to just correct it itself we want that kind of

**[0:15:26]** power within Arc that's what we're doing with imersion eight and then going down into Version 9 here we have self agent execution this is going to be one of the more challenging parts of archon but I cannot wait for this because right now any AI coding assistant the generalists

**[0:15:43]** like wind Surf and cursor archon if they build the code for an agent it doesn't execute in any way there's no way to automatically hook up a database for reg or to get another service installed like CRX for Local web search like you don't have that functionality and so I want to

**[0:15:58]** build that into archon so once it creates the code for the agent and maybe gets the green light from the user that everything looks good then it would use the local AI package I've covered this on my channel a lot to spin up an isolate an environment with the database

**[0:16:13]** like a vector database a SQL database uh web search capabilities they'll have that all packaged together ready for the AI agent to hook into so we would create the agent as a container bake it into a Docker compos stack with all these other services so it has this environment

**[0:16:27]** ready to execute right away and this gets into so many more possibilities in the future as well being able to automatically test and execute these agents and really improve that autonomous iteration so it's more than just the llm reasoning about the code that was outputed but it can literally

**[0:16:42]** test the agent and then see any errors and work on it that way so I just can't wait for this and then I alluded to this a lot already but for version 10 I want to implement multi-f framework support So pantic AI L graph Lang chain egno crew Ai and llama index are all the big

**[0:16:58]** ones that I know of and even though pantic Ai and Lan graph are my favorites I know that people have different preferences and there are reasons to use other ones maybe if you want something more simple like crew AI for example so I want archon to support all of that and

**[0:17:11]** then going into version 11 an autonomous framework learning process so essentially whenever archon creates a good Agent or defines good tools and it iterates and tests and confirms that I wanted to add that to its examples and to the tool Library so that it can continuously give itself better examples

**[0:17:29]** and tools to have this self-improvement process I think that would just be so cool maybe even doing things like adjusting its own system prompt as well as it iterates over time and realizes what makes the agents work the best so very far out there I mean these last few

**[0:17:45]** that we have are definitely more advanced things but I would love to get to this point also probably a lot more versions coming later as well we're up to version 13 already but yeah there's so many ways that we could take Aron much much further even and then going on

**[0:17:57]** to version 12 Advanced rag techniques cuz right now the methods that I have for exploring the knowledge base with regag they work pretty well but I haven't implemented that many Advanced Techniques things like hybrid search reranking uh query decomposition or better chunking through things like hierarchical chunking there's a lot of

**[0:18:15]** opportunities that we have here to make it so that archon can understand and use the documentation for all our different Frameworks much better and then the last version that I have at least for now is the mCP agent Marketplace so being able to take these agents that we' built with

**[0:18:30]** archon and publish them to a Marketplace an mCP Marketplace so that other people can bring them in as sub agents to use within their AI Ides or any other mCP clients so just like archon is a tool a sub agent that an mCP client can use the agents itself produces can also be used

**[0:18:50]** as sub agents it gets very meta here again I don't want to dive into everything that would be involved with this but I think this would just be so cool it just a way for everything that Arcon creates to be reusable by other people and shared in something like an

**[0:19:04]** mCP agent Marketplace then for future Integrations I don't know exactly which version these will fit into but I want to integrate with these different services so starting with Langs Smith here this is Lang Chain's tracing and monitoring platform it just gives you a very good inside scoop with what's

**[0:19:19]** happening with your agentic workflows it'll help us better debug archon and the Agents that archon creates so definitely want to integrate with Lang Smith at some point also could could use something like Lang fuse as well so there's a couple different options here but since we're working with Lang graph

**[0:19:34]** as one of the core components to archon I think Lang Smith certainly makes sense and then also an mCP Marketplace and this is different than version 13 so this is for publishing Aron agents to mCP marketplaces but I'm talking about actually having archon in mCP marketplaces so that people can use it

**[0:19:52]** as an mCP server directly through there so they can run everything without having to go through my GitHub repo and get everything set up themselves I think this would be super cool and then also other Frameworks besides pantic AI obviously this is covered in version 10 so this one I know where it' slot in a

**[0:20:08]** couple of these others I'm not sure exactly which version I'd add them in but this one is very clearcut here um and then also other Vector databases besides superbase a lot of really popular options that I have listed out here I think it'd be good because people appreciate different Vector databases

**[0:20:23]** for different things like quadrant is faster than superbase you can also self-host it pine cone runs serverless it's not open source but it's very very fast so there's reasons to use different ones it'd be good to integrate that as well and then last of all the local AI

**[0:20:35]** package which I want to integrate um specifically for version 9 when we have the self- agent execution so I know where this one slots in as well but this will just be so cool to tie everything with archon to the local AI package that I also have been pouring my heart and

**[0:20:50]** soul into so that is literally everything as far as future Integrations and future iterations of archon so many exciting things planned and yeah if you're not pumped about this I don't know what to tell you because I myself am just so stoked for what archon is now and what it's going to turn into as I

**[0:21:09]** build it out and as we build it out together so that is archon and the awesome plans that I have for it in a nutshell and I encourage you to be a part of this journey follow along as I build it out contribute if you're interested and just try it out and

**[0:21:22]** suggest features for me and the last thing that I want to say really quick is that archon is the perfect example of what I try to do on my channel I try to build agents that are complex enough to be powerful practical and not easily replaced but also build them in a way

**[0:21:37]** where I can break down these complex topics into things that are easy to understand for you so I can teach you best how to build AI agents so if you appreciated this content and you're looking forward to more things archon and AI agents I would really appreciate a like and a subscribe and with that I

**[0:21:53]** will see you in the next video
