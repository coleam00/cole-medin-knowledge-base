---
type: raw-transcript
title: "Claude MCP has Changed AI Forever - Here's What You NEED to Know"
youtube_id: v_6EXt6T83I
url: https://www.youtube.com/watch?v=v_6EXt6T83I
slug: claude-mcp-has-changed-ai-forever-heres-what-you-need-to-know
published: 2025-03-19
duration: "0:24:27"
fetched_at: 2026-07-21
immutable: true
---

## Transcript

**[0:00:00]** out of all the things happening in the AI space right now Cloud's model context protocol definitely seems to have the biggest Spotlight and for good reason it's an incredible protocol developed by anthropic to standardize the way that we give tools to our llms for them to do things with our services and everyone is

**[0:00:19]** covering this right now and they're doing a good job with their content but usually the videos I see are either diving into the weeds building something cool with mCP or explaining it at a high level without any examples what I know you need and what I'm going to cover

**[0:00:33]** right now is a comprehensive overview of mCP everything you have to know at a high level like what it is why it's important and how you can start using it today to boost your productivity and build better AI agents and the thing about mCP unlike other things in the AI

**[0:00:49]** space is it is not going anywhere anytime soon we've had a lot of Sparks recently as I like to call them Manis open AI operator deep seek R1 these things that have generated so much hype initially but then that spark dies down in just a couple of weeks contrast this

**[0:01:06]** with mCP it's like a kindling log instead of a dwindling spark and it's just going to keep getting hotter and hotter and it's not even new it's been around since November of last year it's just that people are realizing more and more over time how useful and Powerful

**[0:01:20]** it really is and that is the sign that it is much more than just hype it's why I've been investing so much time into learning it more recently and I'd recommend you to do do the same simply put if you use mCP to enhance your llms and AI agents you have an unfair

**[0:01:36]** advantage over those who don't and that is not going away anytime soon so allow me to catch you up on everything you need to know and towards the end of this video I'll even show you how to integrate mCP with n8n and your python agents with some templates for you to

**[0:01:50]** download right now a lot of value packed into this shorter video so let's go ahead and dive right into it so here is the official documentation for mCP I'll link to this in the description and we're going to be using this as a reference a lot as we go through all of

**[0:02:04]** the important Core Concepts in their introduction page the home page of the docs they have a nice quick and simple definition of what mCP is you can think of it like the USBC ports for AI applications so just like we use USB to in a standard way connect our devices

**[0:02:22]** very easily to all of our peripherals we use mCP as a standardized way to very easily connect our tools to our llm another way to think about it an analogy that I've heard a lot recently is mCP is like API endpoints for our AI agents so just like companies create apis to

**[0:02:40]** expose their backend services to other applications mCP is the way to expose tools for AI agents very nice and simple and I like the mCP docs here they're pretty comprehensive but definitely missing a lot and some of their diagrams I feel like could explain things a lot better but I don't mind that because

**[0:02:59]** that allows me and other Educators to swoop in and really help things click for you so that's what we're going to do right now not just talking about what mCP is but why it's so useful as well and I've got a couple of neat diagrams to help make that clear so the first

**[0:03:13]** beautiful diagram that I made just for you that I want to show is what AI agents look like before we had mCP because in the end telling you what mCP is and why it's so useful is best done by starting with what we had to deal with before it was available to us and

**[0:03:30]** so right here we have an AI agent this could be built with pantic AI crew AI NN it doesn't matter because in the end with AI agents you create all of these functions that are tools given to the AI agent so you create a function to make a

**[0:03:45]** file to make a commit and git to list our tables in our database and with documentation we tell the AI agent when and how to use each tool so that through conversation it can do all these things on our behalf and it's pretty powerful this is what makes AI agent truly an AI

**[0:04:02]** agent instead of just a regular chatbot or a workflow it can reason about based on the things we say oh I need to go and update this file and then make this push to get and then update this record in superbase for example but we start to hit a wall if we want to reuse these

**[0:04:17]** tools for another AI agent that we're making because what if I started with building an agent with pantic AI but then I want to build another agent with something like n8n or maybe I want to use these tools within claw desktop or wind surf or some other AI IDE it's not

**[0:04:33]** really possible to reuse all of these tools that I created just as individual functions so I end up rewriting a lot of that functionality and it gets even worse if you're sharing things between different people like how would you take this as a neat little package and just

**[0:04:48]** give it to someone for them to use with their AI agent no matter what framework they are using and so you get to this point where you're developing a lot of redundant code for yourself or individual people are recreating these tools to do a very similar thing over

**[0:05:03]** and over and over again and that is why we need standardization we need a neat way to package all the tools for Individual Services in a way that we can share with other people and reuse ourselves between our applications and our different agent Frameworks and that is exactly what mCP gives us all of

**[0:05:21]** those nice little packages created in a standardize way so that we don't have this question here of how do we take these tools and reuse them for more use cases so we aren't creating the same code over and over again so now on to the second diagram this shows what our

**[0:05:36]** agent looks like when it's upgraded to use mCP so now instead of having to Define all of those individual tools and functions we have these services that our mCP servers expose that communicate all these tools to our AI agent and allow them to use it in a way where it

**[0:05:54]** doesn't matter if we're creating our agent with n8n or we're using cursor or we're building with pantic AI we can consume these Serv servers in exactly the same way because these mCP servers are a middleman to standardize the way that these tools are given to the agent and under the hood things look exactly

**[0:06:10]** the same like with our superbase service this mCP we have the same tools here but through the mCP protocol these superbase tools that are available they are communicated to the AI agent so through this route the agent knows what superbase tools are available and then the way that our AI agent uses the tools

**[0:06:30]** under the hood is still exactly the same so there's nothing new and revolutionary here with the model context protocol it's not changing the way that tools are used it's just making it easy to reuse these tools and package them together neatly and so for example if this first

**[0:06:45]** agent was built with pantic AI we can include these mCP servers in cursor for example we have a second host and it's still going to be using these servers in the same way so there'll be a separate instance of the server but it's going to be using the exact same code under the

**[0:07:01]** hood so there's no redundancy we don't have to recreate these servers or these tools and under the hood it all looks the same just using the same tools that are available in that same service and I'm saying same a lot because that's the important part of the standardization

**[0:07:16]** now I'm throwing my full face on the screen again because there's something very important that I mentioned earlier that I want to reemphasize and that is the fact that under the hood with mCP AI agents are still using Tools in exactly the same way way because in the end the

**[0:07:31]** tools that these servers expose are just given as a part of the prompt to the llm so the agent can decide that it wants to use a tool and then it'll produce a specific output to make that tool call happen a big misconception that a lot of people have been communicating is that

**[0:07:47]** mCP is somehow revolutionary in the way that it provides these capabilities for llms that we never had before and that my friend is simply not true because we've always had access to these tools TOS to do things with our llms but mCP just makes it standard like we've been

**[0:08:05]** saying to make it more accessible and easier to create these packages of tools to share with other people so still insanely powerful just not a brand new technology that unlocks this next level of capability so with that word of warning out of the way let's dive more into these mCP servers and where we can

**[0:08:22]** use them so back here in the mCP docs if you go to example clients you can see this list and I'm not sure if it's compreh ensive but it shows you so many different apps that support the model context protocol so you've got your AI idees like Klein rine wind surf cursor

**[0:08:38]** you've got your apps like claw desktop and n8n you can use this in Frameworks like pantic AI crew aai Lang chain seems like everything is supporting mCP these days because it's becoming such a big deal and the whole tool standardization that's the main thing that supported with all of these different clients

**[0:08:55]** there are some other parts to mCP like resources prompts sampling and Roots which are pretty cool like resources I'll just show you this really quick resources you can expose data to your llms that that's updated in real time things like files and database records you can share prompt templates with llms

**[0:09:13]** through mCP you can do sampling which lets you uh request completions from llms as a tool it's so cool and like the thing with all of these different features you can see that they're not really supported by most of these clients and so they're they're very much more experimental and still being

**[0:09:30]** developed that's why the big Focus right now is just on the tool standardization definitely something worth watching as these things are more developed out by anthropic and the open source Community but right now yeah just focusing on tools to start so that's clients and I'll show you how to build a custom one

**[0:09:46]** with python later but let's go on to the fun part the servers that are already available for us to do things with our file system and Google Drive for example and they show also how to get this all set up in claw desktop we'll do that in a sec but first I want to show you this

**[0:10:00]** official mCP GitHub repo that has a list of a bunch of servers that you can use right now so they have the official ones developed by anthropic the official integration so these companies built mCP servers themselves for you to use their services and then you have community-driven ones as well and it is

**[0:10:20]** amazing the number of services that are available to us already as mCP servers is astounding to me and you can always build one yourself if there's something that isn't available here yet and you've got things like Brave search for example so a lot of llms already have web search

**[0:10:37]** like chat gbt for example but Claude and your local llms they don't and so you can use this as a server for that you can have a server to manage your redis database or your postgress database with superbase even and then with these official Integrations there's so many

**[0:10:51]** incredible companies already working hard to integrated with mCP like browser base for example they have a headless browser as a service for things like web crawling and scraping they have this sub platform called stageand there's an mCP server for it you can literally with natural language have your AI agent

**[0:11:09]** crawl websites pull specific information it's just incredible and then you've got quadrant for example for rag you don't even have to implement custom rag tools you can just use this quadrant mCP and then for each of these mCP servers they're either going to be built with JavaScript or Python and so depending on

**[0:11:26]** how they're built you're going to be running them with a different service so the Brave search mCP server for example you can run with either Docker or MPX and so you can just go ahead and install something like Docker desktop or you can install node.js to have access to that

**[0:11:40]** MPX command and then other mCP servers are built with python like the chroma Vector database mCP server and so you run this uh with uvx which if you have python installed you can just pip install uvx to run that command and all of these instructions they also tell us

**[0:11:57]** how to set it up in cloud desktop and you can take these instructions and use that to set it up in anything else like n8n or wind surf or cursor and so it's always going to be very standard just tweaking in a little bit and so with claw desktop for example the way that

**[0:12:12]** you can set up these servers if you go to the top left click on file and then settings you can go to the developer tab and then edit your configuration right here so it's going to open up this folder on your computer and then I can open up my config in something like vs

**[0:12:27]** code and then here is my Json my configuration for all of my mCP servers that I set up just following the guides in the GitHub repo and so I've got access to my file system brave for web search sequential thinking which is super cool I've got memory which is kind

**[0:12:42]** of like a basic implementation of something like mzero or Zep then I've got stage hand this is the one that I showed earlier which is really cool you're able to with natural language have the agent crawl websites for you and then I've got archon which is my mCP

**[0:12:55]** server for the AI agent Builder that I've been working on on my channel so all of my mCP servers so with that back over to CLA desktop I can see all of the tools available by clicking on this Hammer icon it's going to look very similar for wind Surf and cursor as well

**[0:13:09]** so this gives me all my tools and a description of each of these and so now I can ask it a question that is going to require it to use these tools in conjunction together to do things for me so in this case first it's going to have

**[0:13:21]** to use the brave search to query for the pantic AI docs and then once it finishes that query and gets the link to pantic AI it's going to have to use stageand there we go because it needs to visit that page and so we're using the stageand navigate tool so it's going to

**[0:13:37]** process that for me and then come back and use the next tool so there we go yep it found the models page and now it wants to take a screenshot super cool and browser base is really neat with Stage handier I can actually go into their UI go to sessions take a look at

**[0:13:50]** this running session and sure enough it is here on the pantic AI models page and I can go back to Claude and I can ask it questions about this as well it's just super neat and these are just examples of some of the tools that I could be

**[0:14:04]** using I've got a lot of them set up but just look at how easy it is to use these tools together to do some awesome things all right we have covered a lot already so let's just go ahead and take a breather so at this point we definitely

**[0:14:17]** understand mCP at a pretty high level what it is why it's so important how we can leverage it and we use clae desktop as an example but you could look up the documentation for something like cursor for example they're sure to have it the setup is going to be very similar to

**[0:14:31]** Claude desktop but now I want to dive into building with mCP we can create our own servers to package our own tools and we can also create our own clients so we can build AI agents with Frameworks like pantic AI that can leverage mCP servers for the agent tools and this entire

**[0:14:50]** video has definitely been a crash course I'm just giving you what you need at a high level and so I'm going to go pretty quick through these building pieces with mCP but but just let me know in the comments what you want me to do a dedicated video to to dive into in more

**[0:15:05]** detail cuz I'm definitely going to be creating more mCP content very soon and I would love to do a deep dive into building an mCP server or integrating mCP with n8n or pantic AI so just let me know but right now I'm going to go over things pretty quickly give you some

**[0:15:20]** templates to get started so you can dive into this yourself so first up building your own mCP server very important and I'm almost certainly going to be making a dedicated video on this in the future there are a few different pages in the docs that I want to call out really

**[0:15:34]** quick so first if you go to for Server developers they give you a good example how to build a simple weather mCP server with a couple of tools for dealing with weather data and then depending on the SDK you want to use like if you want to build a python mCP server I'd highly

**[0:15:49]** recommend checking this out it'll bring you right to GitHub where you can go through examples for the specific language you're interested in and there's a lot more information here so not going to dive into this now because the really important thing that I want to show is building mcps with llms cuz

**[0:16:04]** let's face it as much as Vibe coding is something I don't really trust we're all using AI coding assistance to at least get us started with our projects and so Claude in the mCP docs shows you how to do that so you can visit this llm d. text and this is going to give you the

**[0:16:20]** entire mCP documentation and markdown so you can copy and paste into your favorite AI IDE so I can copy this go into something like wind surf for for example and then just paste that whole sucker in there and I can ask it to use that to then build me an mCP server and

**[0:16:36]** so for example I could have it build a brave server if I wanted to and also within win Sur if you can just reference the mCP documentation directly you can do this in other AI IDs I believe as well at cursor so very powerful you have both options but I can say yeah use

**[0:16:52]** these docs to build an mCP server that searches the web with brave boom and I can just send this in I'll let it do its thing it's going to search through all the documentation create a bunch of code for me and I'll come back once it's built and look at this it built us a

**[0:17:08]** full mCP server and I'm not looking through all the code in insane detail I'm not going to run it right now either just because I wanted to show this really briefly but this looks really solid it looks like a very well-coded mCP server I'll accept all these changes

**[0:17:22]** it's got the tool for the brave web search even uses a couple of different API endpoints for brave which is super neat and it gives me example claw desktop configuration a readme it did everything for me I mean part of this is just wind surf being great but yeah like

**[0:17:37]** it used all the documentation for mCP to build this for me and I know that brave is just kind of a a demo example you would probably want to build something that isn't already available on the GitHub repo but yeah I think I'll do a dedicated video on this later where I'll

**[0:17:51]** build an mCP server from scratch doing something that isn't available already because in the end there are a lot of different services that don't have mCP servers and you want to make really custom servers sometimes that maybe are combining different tools together or working with local llms that you have

**[0:18:07]** set up I mean there's Endless Possibilities next up we've got n8n you can integrate mCP servers directly in your n8n AI agents and it's all using this community node that was developed recently I'll have a link to this GitHub repo in the description which has instructions for installing everything

**[0:18:23]** and also an example of how to integrate with the brave mCP server which is what I used actually is one of mine so back in n8n you can go to the settings in the bottom left this will work if you are self-hosting n8n or running it locally and then just go to the community nodes

**[0:18:38]** tab then you can click on install and then just type in nn- no- mCP and install it is that easy I do have my own custom version that I might make a PR into this main repo at some point it's not a very mature node there's some glitches that I was working on fixing

**[0:18:54]** behind the scenes might make a video on that later as well but yeah back to the agent here now Within one of these mCP nodes which you can have as a base node or as a tool for your agents you can go in and then you create credentials for

**[0:19:06]** each of the mCP servers that you want to set up and so very similar to CLA desktop and other apps you have your main command like npx you've got your arguments and then your environment variables you set up all that click save and then you have all these tools

**[0:19:20]** available like you can list the tools for the mCP server list prompts you can execute a tool and so I've got one here to list the tools for brave and then another to execute any given Brave tool within the mCP server and so feel free to download this template available in

**[0:19:34]** the description if you want to see how I prompted the agent to work with these different mCP servers just got a couple uh examples here so brave and then convex but it's yeah it's pretty neat so I can open this chat and now I can say search the web for Elon musk's net worth

**[0:19:51]** the kind of thing that an llm would definitely not be able to do by itself and so you'll see that first it's calling the tool to see what Brave tools are available because it knows that that's for web search and then it executes one to search the web and there

**[0:20:02]** we go we got his net worth yep $323 billion which is down more than a 100 billion from December by the way very interesting the very last implementation I want to show you is how you can create custom mCP clients in Python to use them in AI agents built with Frameworks like

**[0:20:19]** pantic AI which we're using right here and so you can dive into the python SDK documentation more and feel free to download this template as well but yeah I just import a couple of things from mCP and then I use those down here to define the server that I want to connect

**[0:20:35]** to and then I create a client session that I then use within my agent because what I do with the client is I gather a list of tools with this helper function that I have here so it calls into mCP grabs the tools for the server packages them all together as penic AI tool

**[0:20:52]** definitions so it includes the description and the arguments for the tools and everything and then I just feed that in as the tools TOS to my pedantic AI agent just like I would do if I defined all of the tools in code just in like tools. piy or something

**[0:21:06]** else here it is that easy to set up a client and then use that within pantic AI you could do something very similar with any other framework like crew AI or the open AI SDK as well if you wanted and so now in my terminal I can just run

**[0:21:20]** the python script just like usual and then chat with this agent you can see that it loads the file system server tells me what my directory is and I can say something like hide and it won't use the tool just normal conversation but then I can say what files are available

**[0:21:35]** and it'll call upon that tool using the mCP server directly to tell me the files that I have in this folder and yep that is the right answer so yeah I definitely want to do a dedicated video on building these clients into custom AI agents so let me know in the comments if you be

**[0:21:53]** interested in that specifically cuz I think I might really lean into this so that is everything that I wanted to cover for MC P except for a very important final note that I want to leave with you and that's on the future of the model context protocol cuz here's

**[0:22:07]** the thing who knows in the near future if another standardization is developed that's better and makes mCP obsolete I don't think it's going to happen but even if it does it's still really important for us to dive into this protocol because anthropic is doing a great job with this so no matter what

**[0:22:24]** kind of standardization ends up being King in the next half decade or decade it's going to look very similar to this and just getting acquainted with these standardizations for adding tools into llms is very important for us because this is just a higher level understanding that we want to unlock as

**[0:22:42]** developers and people just building things with AI and anthropic also has an incredible road map outlined here I think they really have a good Vision behind mCP and really making this the king of standardization for agents like remote mCP support I mean if you notice we were running all of our servers

**[0:22:59]** locally right now but being able to have them up and running in the cloud having our clients just connect to them in the cloud even things like authentication authorization and starting to monetize mCP servers I'm sure that's going to be a thing as well it's super important and

**[0:23:13]** like agent support like this gets me fired up adding in the ability for complex agentic workflows with mcps and having sub agents that are directly supported as mCP servers hierarchical agent system like oh man so many incredible things that we can build into this standard ation just to make all

**[0:23:30]** these powerful concepts with AI that are already doable with agentic workflows and advanced tools and stuff but it this just makes it so much more accessible to less technical people for us to share tools and ideas with each other this just gets me so fired up and that's why

**[0:23:47]** I want to dive in so much to everything related to mCP so I hope this video gave you everything that you need to understand mCP at a high level and how you can use it right now and please let me know in the comments what you want me

**[0:24:00]** to dive into in more detail for my next mCP related video there are just so many more things that I could go into a lot more depth on like creating your own mCP server integrating with n8n creating these clients into your pantic AI agents a lot more I could do so if you

**[0:24:16]** appreciated this content you're looking forward to more things AI agents and mCP I would really appreciate a like and a subscribe and with that I will see you in the next video
