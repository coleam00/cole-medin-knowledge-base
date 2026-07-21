---
type: raw-transcript
title: "Docker Just Made Using MCP Servers 100x Easier (One Click Installs!)"
youtube_id: TxlVdB2gmGE
url: https://www.youtube.com/watch?v=TxlVdB2gmGE
slug: docker-just-made-using-mcp-servers-100x-easier-one-click-installs
published: 2025-10-08
duration: "0:23:07"
fetched_at: 2026-07-21
immutable: true
---

## Transcript

**[0:00:00]** Right now, I'm going to show you the easiest possible way to supercharge your AI agents, and it's all thanks to MCP servers. You might have heard of them before, but there is a new way to set them up and connect them to your agents super quickly. The workflow that you're

**[0:00:16]** looking at right here, and I'll actually show you this later in the video, took me only 10 minutes to set up. I connected my Claw desktop to YouTube, Obsidian, Slack, and GitHub really, really easily. And so I have this whole workflow here where it pulls a YouTube transcript. It summarizes that and puts

**[0:00:32]** it in my Obsidian vault and then I have it read my Slack conversation to get some extra context and then create a GitHub issue and then I even have it mention Claude code in the issue to kick off a cloud code agent to autonomously work on my codebase based on the

**[0:00:47]** research that I did here. So end to end, we started with research all the way to a complete implementation in our codebase and it took me 10 minutes to set this up with all of these MCP servers. Now you might be asking yourself, Cole, isn't that going to take

**[0:01:01]** a while to get everything set up? I mean, if you worked with MCP before, you probably worked with this kind of registry, like the main one that we have in GitHub where you find the MCP servers that you want in this list, but then you have to click into it and you have to

**[0:01:14]** figure out the JSON configuration to connect it and then you have to go and do that for the next one and the next one. It actually is a bit of a hassle to get all of these MCP servers, all this functionality built into our AI agents. But now there is a new tool that makes

**[0:01:30]** it 100 times easier to find and connect MCP servers and that is the Docker MCP catalog. This is what I want to show you today and all the things that we can do with it. It is a beautifully curated list of all of these MCP servers and with a single click of a button I can

**[0:01:48]** connect them and then use them in my own agents. I can connect very easily again with a click of a button to cloud code or cloud desktop. This is now my command center to manage my MCP servers. Right now, I'll show you how easy it is to get

**[0:02:02]** this up and running and then we'll play around with some of these different servers and build out some workflows. So, in order to get access to this lovely catalog of MCP servers, the only thing you have to do is install Docker Desktop. And if you followed along with

**[0:02:16]** any of my content in the past, you probably already have it. I use Docker already for pretty much every application that I build. And so I already have the platform up and running 24/7 with all of my different containers. And so now I get to manage my MCP servers in the exact same place.

**[0:02:33]** It is a beautiful thing. So cool. Let's actually explore all the MCP servers that we have here. And I'll show you how easy it is with a single click of a button to connect these servers into any of your external clients as well. Once you have your server selected like cloud

**[0:02:47]** code, cloud desktop, Gemini CLI, it'll actually update the configuration for these tools for you. So you don't even have to do anything with JSON yourself like you have before if you've used MCP. And so yeah, going back to the catalog, I have this sorted by popularity right now. We've got fetch at the top with

**[0:03:05]** over 500,000 downloads already, giving our agents the ability to take a URL and extract the content from it. We've got Slack. I'm going to be using this one today. Playright for front-end testing. Context 7 for rag. We can hook our agents into our database in one click. We can pull YouTube transcripts. I'll

**[0:03:23]** also be using that one today. It feels like whatever functionality I need for my agent, I can get it from this catalog. We got notion. We've got Brave, Firecrawl for scraping. We've got Discord, Stripe, Chroma DB. It's like everything is here. It's so cool. So, let's actually install one of these. I'm

**[0:03:39]** going to go to YouTube transcripts. click into this and then all I have to do, one click, add MCP server. Boom, we have it now connected. The only other thing you might need to do depending on your MCP is set up configuration. But it's also really convenient that we can

**[0:03:55]** do all of this for things like API keys right within the catalog as well. And then we can also see all of the tools that this MCP now gives to our agent once we have it connected. Also keep in mind that when you are working with the MCP toolkit, which is in beta, you might

**[0:04:11]** need to go to your Docker settings in the top here, and go to beta features and enable it. Now, this was enabled for me by default, but I just want to call that out in case you're missing that there, cuz then it's not going to work when we go on to the rest of the things

**[0:04:23]** here, actually getting these MCP servers connected to our agents. So now with our first server selected from the catalog, we can now hook this in to any of our clients in the click of a button. But there's one other thing I actually want to show you first that's really cool.

**[0:04:38]** Because when you go to this client page for the first time, none of these will be connected except for this one right here, Ask Gordon. It's actually set up to be connected to our MCP toolkit by default because Gordon is the AI agent that is built directly into Docker

**[0:04:53]** Desktop, also in beta, just like the MCP toolkit. And so without even having to connect to any external client yet, we can actually test our MCP servers directly within Docker Desktop thanks to Gordon. And so for the tool that I have right now, you just have to go to your

**[0:05:10]** toolbox MCP toolkit right here. And then just make sure that you have the toolkit enabled for Gordon. And so I have my three tools right now for that YouTube transcript MCP server. So I'll close out of this. And we need it to transcribe a video. So I'm just going to go to one of

**[0:05:25]** the latest videos on my channel where I cover Dockling, which is a tool to help with data extraction and chunking for rag. And so I'm just going to copy this URL at the top. Very simple. Go back to Gordon here. I'm going to say transcribe this video and give me a very concise

**[0:05:41]** summary. I just want something really fast here just to show you how Gordon is a place for us to quickly test our MCP servers. And so Gordon is going to make that tool call. There we go. Calling get transcript. And it's a pretty quick agent overall. So we should get the

**[0:05:55]** summary in just a second here. There we go. Nice. The video introduces Dockling. Didn't quite spell it right. I'll give it a pass on that one. Free open source Python tool designed. Simplify the extraction preparation of complex data. Cool. This is perfect. So, as we're adding these servers in our catalog, we

**[0:06:11]** can use Gordon to quickly test them. But the real deal here is being able to use these MCP servers in our existing clients. You maybe are using Claude code or cursor for your coding or you're just working with cloud desktop to brainstorm with an LLM. Let's give the

**[0:06:28]** functionality to those guys. And so, all we have to do is go to the clients tab and then single click of a button. Just as easy as selecting the servers in our catalog. So, we'll start with Claw Desktop here. All I have to do is click connect. And boom, there we go. Now, the

**[0:06:44]** next time we open up Claw Desktop, all of the servers that we have here are going to be immediately available in Cloud Desktop. Now, for most MCP clients, once we add more servers into them, we have to restart them. So, I'll do that for Cloud Desktop here. I'll

**[0:06:58]** just go and rightclick, quit, and then go and restart the application. Super super fast. Wait for it to load. And then the way that we can verify our connection here is by going to search and tools and then you're looking for the MCP server called mcp_doccker very creatively named. And we can click

**[0:07:14]** into this to see all the tools that it exposes. And so this single server is basically aggregating all the tools from all the MCPs that we have selected in the catalog. So once we start adding more here, we're going to just see it still as a single server in our client

**[0:07:29]** just with all the tools from all of our different servers. And the other thing I want to say here, I think you'll find this interesting. This is a quick 30- secondond explanation how this works. All of these tools that we add, they run as Docker containers. So whenever our

**[0:07:43]** client like Claw Desktop requests to use a tool like to get a transcript, that actually quickly spins up a container to perform that tool action and then once the tool is done running, it immediately spins the container down. So no matter how many MCP servers we have connected

**[0:08:01]** here, it's not like those containers are constantly running taking memory on our machine. It's only when we're using a tool that the container is actually running. So extremely efficient and secure. Very, very cool. And so now with claw desktop here, I'm just going to go ahead and test it with the exact same

**[0:08:17]** thing. So I'll copy this URL, go back in and say transcribe this video, and give me a super concise summary. All right. So, we'll just make sure that it can work as well as Gordon, which quick spoiler, cloud desktop does work quite a bit better than Gordon. It is a lot more

**[0:08:32]** powerful of an LLM running things under the hood. So, there we go. It's calling MCP Docker to get the transcript for the URL. And let's see if we can get a nice summary here. Awesome. Perfect. Yep. Here's our video, what it covers, key features. Looking really good. Honestly,

**[0:08:45]** probably even a better summary. So, cool. That is the YouTube transcript MCP, but let's add in a few more, really spice things up, and actually get a full workflow created with these MCP servers. So, I'm just going to connect a few different ones that I want to have in my

**[0:09:00]** claw desktop. So, I'm going to start with Slack here. I'll go ahead and add this server. Single click. Boom. There we go. And then we just have to configure a couple of things, which I already did off camera for the team ID and the channel IDs. You just get these

**[0:09:11]** from the Slack URLs. And then you just have to create a Slack app and hook in the bot token here. I'm not going to cover that right now. Uh you can read the documentation in Slack if you want. So I got Slack connected. What else do we want here? How about uh GitHub? So I

**[0:09:25]** did actually try the official GitHub and that one wasn't working for me for some reason. So I'm just going to use the archived one here because this has actually been working phenomenally for me. So now all I have to do is add in my personal access token that I can get in

**[0:09:37]** my GitHub settings. And now it can access all my repositories and do things like create issues on my behalf. Very, very neat. And then the last one that I want to add in here, I've been absolutely loving Obsidian recently. Probably going to be creating a lot more content on it in the near future. So,

**[0:09:53]** I'm going to go ahead and add this one. Obsidian is where I do a lot of my note takingaking and knowledge management. Like what you're looking at right here is actually the script that I have written out for this video right now. I know it's really meta u but yeah, when

**[0:10:07]** you go into the settings for Obsidian, you can install community plugins. And one of these plugins that you can install is called the local rest API. So you have to install this and then it's going to give you an API key, which is what you need to hook into the Obsidian

**[0:10:24]** API key right here in the MCP configuration. So that's how you hook in Obsidian. Now going back to my servers, I have four in total now. So I have 26 tools for GitHub, which is kind of a lot, but we'll roll with it here. Then we've got Obsidian, Slack, and YouTube

**[0:10:39]** Transcripts. And so we can start to actually define these workflows for the large language model to combine functionality from these different servers. It's really cool. Now, I'm not going to be testing this with Gordon. Gordon is a pretty cool guy, but I can tell from my testing that I've been

**[0:10:59]** doing that it's not powered by the most powerful LLM. It seems like it's something like Gemini 2.5 Flash or GPT5 Nano. it gets quite overwhelmed with all of these tools when it has more than a couple. And plus, I think Gordon is more fine-tuned to help you with Docker

**[0:11:18]** related things anyway. And so with all these tools connected, I'm just going to jump straight to restarting Cloud Desktop and testing things in Cloud Desktop. And I could connect other clients as well, like if I wanted to connect it to Cloud Code or Gemini CLI, but I'll keep on the the train here of

**[0:11:33]** Claude Desktop because I love using Cloud Desktop just to generally brainstorm ideas with an LLM. So yeah, let's go do search and tools. Scroll down MCP Docker. I'll click into this and sure enough, this time we have a much larger list of tools because we have everything from Slack, Obsidian,

**[0:11:50]** YouTube Transcripts, and GitHub. Awesome. So, I can say, for example, what Slack channels do I have? And it should just say I have access to a research channel because that's the only one that I've given the Slackbot access to. So, yep, listing Slack channels. In a second here, it should say research.

**[0:12:08]** There we go. Okay, perfect. Yep. So, the Slack MCP is working for GitHub. I can say what GitHub repos do I have? And in a second here, I'll actually combine some of these tool usages together to make something pretty interesting. But yeah, first let's just make sure that

**[0:12:23]** these servers are actually working. There we go. I have 50 GitHub repos. Take a look at that. That's actually crazy to me. Yeah, things are working great. Okay, so that was fun just testing out the different MCP servers, seeing these tools in action. But now, let's take it to the next level. This is

**[0:12:38]** where the fun really begins because I wanted to create more of a workflow for my agent to go through leveraging the different MCP servers in tandem to accomplish a single larger task for me. Let's push the limits of Sonnet 4.5 here. And so what I'm going to do is

**[0:12:54]** send in this request that is going to require it to work with all four MCP servers that it has through the Docker catalog. So I'm having it pull the transcript for that same Dockling video. I want to create a summary and put it in my Obsidian Vault. And I'm specifically

**[0:13:08]** having it put it in this reference notes folder right here. And I'll actually delete the previous dockling summary that I have just so that it's starting from scratch. There we go. put it in the reference notes folder. Then after I want it to read my Dockling research that I have in that single Slack channel

**[0:13:25]** that it has access to. So just giving it some more context to then create a GitHub issue for Archon. I want to actually integrate Dockling with Archon. And then finally last thing we're asking a lot here. Finally, I wanted to add a comment to the issue saying at cloudfix

**[0:13:41]** work on this issue. That is our way to trigger cla code to autonomously work on this issue. So, we're going from the research phase all the way to actually kicking off a workflow for Cloud Code to work on this issue in our repository. I know this is pretty complex, but that is

**[0:13:57]** the point. I'm trying to ask a lot here and see how it performs. And I'm actually super curious. I have not run this yet. This is my first time doing it. And so, we'll see if it's able to accomplish everything. And so, yeah, first it is getting the transcript. I

**[0:14:11]** think what I'm going to do here is let it run. I'll pause and come back once it's done. We'll read through the conversation history together and see if it did what it was supposed to. Okay, this is actually beyond exciting. Everything worked flawlessly. And as I'm speaking, Claude Code is working on this

**[0:14:26]** issue. Take a look at this. This is just so cool. So, it got the transcript. We saw that already before I I paused to come back here. Then, it is creating the research summary in Obsidian. Take a look at this in the reference notes folder. I've got Dockling YouTube

**[0:14:40]** tutorial summary. And it even spelled Dockling right this time. good for Sonnet 4.5. So, we got our nice little summary here of the tool as a whole. Looks really good. Talks about hybrid chunking, which is one of the things that I care about. And then going down now, it goes and it fetches the

**[0:14:55]** conversation history in that Slack channel. So, it lists the channels, finds that research one, it pulls the channel history. So, there's quite a bit of text that I have here, just things that I did to research Dockling. Looking really good. Then it searches my GitHub repositories to find the Archon one.

**[0:15:12]** Once it finds archon, then it creates the issue. And it had a problem creating an issue the first time it used that tool call. But LLMs are quite smart, especially sonnet 4.5. So it's able to correct itself, figure out the problem, call the tool again, and this time it

**[0:15:26]** works, creating that issue for the dockling integration. And then finally, it adds that comment to trigger cla work on this issue. And so yeah, let's actually go to our browser. Now, I want to show you here first. This is the research that I have in the Slack conversation that it pulled by the way.

**[0:15:44]** Then going into archon, we have a new issue. Look at that. Integrate dockling for advanced document processing in the rag pipeline. We got a beautifully formatted issue here. And there we go. Atcloudfix work on this issue. And then cloud code that I already have integrated in the repository responded

**[0:16:02]** to this and is in the middle of processing creating a pull request for my issue. So end to end from cloud desktop. I had to do a ton of research that now finalizes. It culminates into Cloud Code actually working on this for me. Super super cool. All right, Claude

**[0:16:19]** Code has finished its work. It did it all within a feature branch that I created a poll request for as well. So, we can go to that, check it out, and boom, there we go. We have a poll request that was created end to end by automation thanks to MCP servers and the

**[0:16:33]** Docker catalog. Now, I didn't check its work yet here, but that's not the point. It's totally good if you don't understand Archon or exactly what I'm doing at GitHub here. The point that I'm trying to drive home is just how easy it was to create this agentic workflow with

**[0:16:46]** all these MCP servers that we connected in just a couple of clicks. Now, what we were able to do here in Cloud Desktop was pretty incredible. And it's really easy for us to connect to other clients that are in this list as well, especially if you want to take some of

**[0:17:01]** these MCP servers and use them with your coding assistants. Most of the clients here actually are coding assistants that you can connect to. But the big question I have is how can we use these MCP servers in our own custom agents within Python code within NADN. Well, that's

**[0:17:20]** what I'm going to show you right now. To end things off for this video, I want to show you how we can take all this functionality and use it anywhere. So, we're not just limited to this client list. As awesome as this list is, and it does cover the tools that I use

**[0:17:32]** generally, what about my own agents? So, we'll actually start by going back to Claude Desktop because I want to show you that the way that Docker connects to these clients is the same way we can connect to our custom ones. There's just a little bit of extra setup we have to

**[0:17:47]** do. So, let's go to the settings here. Let's see how exactly this connection is set up between the Docker catalog and cloud desktop. If we go to the MCP Docker server here, take a look at this. It is using this thing called the Docker MCP gateway. What the heck is the MCP

**[0:18:03]** gateway? Well, it is the tooling under the hood that allows us to connect the MCP servers in the Docker catalog to all of those clients in that preconfigured list. But the beautiful thing with this MCP gateway is it is actually opensourced. And so we have this documentation page that I'll link to in

**[0:18:23]** the description where they talk about this. The MCP gateway is Docker's open-source enterprise ready solution for orchestrating and managing MCP servers. So the exact same functionality that is used under the hood to connect with our catalog and that preconfigured set of clients like cloud desktop and cloud code, we can use that same

**[0:18:43]** functionality. We can run it ourself and then connect our own agents like what I have right here in N8N. And I'll show you this in a second here. And so going to their open source repo for MCP gateway, they have some instructions for setup. You basically build the gateway

**[0:18:59]** from source and then we can run it with a couple of different commands depending on the MCP protocol specifically that we want to use. Now HTTP streamable is the de facto standard protocol for MCP. So this is the command that I'm going to run myself. So, I followed the

**[0:19:17]** instructions in this readme to get everything up and running locally already. So, now I can run docker mcp gateway and I'm going to run it on port 8089 and I'm going to use the streaming transport layer for MCP. So, I'll run this and it's going to look at my Docker

**[0:19:34]** catalog registry and it's going to figure out the MCP servers that I have connected. So, the exact same ones that we connected within Docker Desktop in the UI with the catalog we have available here. And so it's going to run all of these. And so now we have the

**[0:19:49]** server listening on port 8089. It's ready to receive any requests for any of the tools for any of these servers. It is that easy to get this all up and running. And so now in N8, I'll just show you really quickly. And now we can do this with like any agent that we

**[0:20:05]** want. N is just like the easiest way to take advantage of this right out the gate. So I have a chat trigger that goes to a super basic AI agent. Like this is like extremely barebones right now. I'm just using GPT4.1 mini for my LLM. And then for the MCP client, the connection

**[0:20:22]** here is host.doccker.in because I have to look outside of the n container to my host machine where I'm running the docker mcp gateway. And then the port obviously is 8089 because that's exactly what I selected when I ran the gateway. And then the server transport is HTTP streamable. And then

**[0:20:41]** everything's running locally. So, I don't have any authentication at this point. Super easy to get it set up. So, I'll go back to the canvas here. I can actually open the chat and show you here. Let's do something like, you know, what Slack channels do I have? I'm not

**[0:20:53]** going to do like a whole complex workflow again because we already saw that in action, but we can just quickly see it leverage the MCP client. It used the Slack list channels here. And we have our research channel. Cool. And then I can actually go to the MCP

**[0:21:06]** gateway logs and I can see the logs from the N8N. So, first we have the connection that's made here from N8N and then it's running this specific tool to list the channels that we have, Slack list channels, and it took 1.5 seconds in total. So, absolutely beautiful. And

**[0:21:23]** I also did a video recently on my channel showing you how to build live kit voice agents. And there I did show very briefly using the Docker MCP gateway to connect to the servers I have in the catalog. And so definitely check out the video I'll link to right here if

**[0:21:38]** you want a full guide on building LiveKit voice agents. But right here, I just want to show you another example of using our custom agents to talk to these MCP servers that we've curated. And so in my agent session, I've just added this MCP servers parameter where I'm

**[0:21:52]** connected to the same URL that we used in N8N. So again, connected to the same servers that we were using in Claw Desktop and N8N. So in my console here, I can go ahead and run this voice agent and let's see it in action. >> Hello, how can I assist you today?

**[0:22:07]** >> Yeah, my GitHub username is Cam0000. I want you to search my repos and find the one that has the most stars and tell me what it is. >> The repository with the most stars under your GitHub username, Colium0000 based on the top results is Archon. It is described as the beta release of that

**[0:22:27]** is the right answer. So I'll go ahead and close out of that there. But there you go. We have a live voice agent that is connected to all the servers that we have curated in our Docker catalog. So there you go. That my friend is everything that I have to cover right

**[0:22:39]** now for the Docker MCP catalog. And huge thanks to Docker for actually collaborating with me on this video just to make sure that I was hitting on all of the important features that we have with the MCP catalog. It really is the easiest way to bring external functionality into our AI agents like I

**[0:22:56]** showed you in this video. So, if you appreciated this video and you're looking forward to more things AI and AI agents, I'd really appreciate a like and a subscribe.
