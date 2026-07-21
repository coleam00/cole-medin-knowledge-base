---
type: raw-transcript
title: "Knowledge Graphs in n8n are FINALLY Here!"
youtube_id: NQ3vJ8iZPaQ
url: https://www.youtube.com/watch?v=NQ3vJ8iZPaQ
slug: knowledge-graphs-in-n8n-are-finally-here
published: 2025-09-23
duration: "0:18:55"
fetched_at: 2026-07-21
immutable: true
---

## Transcript

**[0:00:00]** The time has come, the moment that you have been waiting for. We finally have knowledge graphs in our NAN rag template. So many of you have been asking me to add this, especially after I cover knowledge graphs with graffiti and Python previously on my channel. So, here it is. In this video, I'll show you

**[0:00:18]** how it all works and how you can get it set up for yourself. We're going to get a little bit hacky today. It's going to be fun and it'll still be super practical. Now, first of all, what do knowledge graphs actually give us? Well, to answer that question, I want to go

**[0:00:30]** back to the fundamentals of rag for a second and then show you how we can layer on top knowledge graphs to take our agents to the next level. And so traditional rag, what we've been working with in this template so far is using a vector database like I've been using

**[0:00:47]** Postgress with PG vector. This could be a dedicated vector database like Quadrant or Pine Cone. You'll be familiar with these things if you've been following along with my template. And this works great. I mean, there's a reason that I've been just using a vector database throughout the entire

**[0:01:03]** template as I've been building it on my channel, which by the way, I have this playlist I'll link below if you want to really start with the basics and then get to the point where we have the more complex and powerful template that you're looking at right now. So, we have

**[0:01:14]** our rag pipeline. This is the foundational piece where we take our data from our source like Google Drive and we chunk it up into the bite-sized pieces for our agent to search and digest. And that's what we store in our vector database. And the main problem that we have with vector databases here,

**[0:01:33]** as great as they are, is they don't do a good job storing relationships between the different entities that we have in our data. So when we just dump all of our chunks in a database like this, it's hard for the agent to find one chunk and then see how it relates to other things

**[0:01:50]** that are also stored in our knowledge base. That is what a knowledge graph gives us. And that's what you're looking at right here. So I built up this knowledge graph in the rag pipeline now using an MCP server that I'll introduce you to in a little bit here. This is the

**[0:02:04]** key. It's just a single node that I've added to the pipeline. Super simple. And so we're building up our knowledge graph at the exact same time that we're building up our vector database. So we're storing the information in both places just represented in different ways. Because think about people,

**[0:02:21]** companies, products, all of these entities we have in our data. They're very related to each other. And so we want to be able to store those relationships and give our agent the ability to actually navigate between these different nodes as they're called based on the relationships. And so we

**[0:02:36]** can look at a company and then we can from there go and search and find the executive leadership team as an example. This is just demo data. But as our data really starts to evolve and we have thousands of entities and thousands of relationships, agents definitely get lost in the sauce trying to search

**[0:02:54]** through these things in a vector database. That's why we want a knowledge graph. And so like I said, same data that is being stored just represented in different ways. And this definitely goes with the theme of a gentic rag that I've been covering when in this template. We're giving the agent the ability to

**[0:03:11]** search through our knowledge base in different ways. So if we're asking about a single company, well, we should probably just go to the vector database like we have been. But if we're asking about how two companies work together, now that would be a good example to go and search the knowledge graph. All

**[0:03:26]** right, let me actually show you this in action now. And so I'll be explicit here just for demo purposes to use the vector database asking it to give me an overview of a company that I have mock data for in my Google Drive. And so, yep, there we go. It uses the tool to

**[0:03:39]** search the vector database. These are the chunks it returned to give me the answer. And there is our overview. All right, looking good. So, yeah, in a brand new conversation, let's try something else. Let's say, tell me about Dr. Tanaka and Dr. Chen. And I'll say use the knowledge graph. Again, just

**[0:03:56]** being explicit here because this is a more relational question asking about two entities at the same time. And take a look at that. It is using the graffiti MCP server which I'll show you how to set up next to query our knowledge graph. So the agent drops itself in here

**[0:04:10]** finds the right nodes even looking through relationships. It's really cool the things that happen under the hood to get us our answer. And I was being explicit here but generally in your system prompt for your agent this is where you specify when is it optimal to search the knowledge graph versus the

**[0:04:26]** vector database. You can really play around with this and tweak it to your specific use case. I mean, that's the big thing with this template, right, is that it's all you take this and evolve it to what works best for your use case and your data for rag. So, there we go.

**[0:04:40]** That's a quick demo. Now, let's get into actually setting this up. And getting knowledge graphs added into our template here is super straightforward. There's literally only two nodes that we are adding on top of the previous version of the template. We have one to insert into our knowledge graph using the graffiti

**[0:04:58]** MCP server and then one to give a tool to our agent to search the knowledge graph again with the graffiti MCP server. And so most of the setup is actually for the graffiti MCP. So that's what I'm going to walk you through. Then we'll cover these two nodes and exactly

**[0:05:14]** how they work. Now this does assume that you are using a self-hosted N8N. That is a requirement for following along here. the lang chain code node that I covered in my last video on this template require self-hosted N8N and this MCP server needs to be run internally alongside your N8N instance. So

**[0:05:33]** obviously the cloud version would not work. I'm going to be showing you how to go into your machine where you're hosting N8N bring graffiti and Neo4j alongside it. So we have this MCP server ready to be connected to. And so I will be assuming that you already have

**[0:05:49]** something like a digital ocean droplet with N8N up and running. So if you don't have that yet, just follow this guide that I'll link to in the description to get your own N8N instance self-hosted on Digital Ocean. Digital Ocean's not sponsoring this video. It's actually just what I use to host my N8N. So

**[0:06:06]** definitely follow along with that. Once you have N8N up and running, that's when we can dive into the instructions for Graffiti. And so with a single docker compose we're going to have the graffiti mcp server and neo-4j which is our underlying database hosted and then we'll hook into it with nn. Now let me

**[0:06:25]** be super clear. Neo4j is the database like postgress where we store our knowledge graph and graffiti is the library. It's the tooling that gives us the ability to extract from raw text the entities and relationships to then store in Neo4j and it gives us the MCP server that makes it possible to use graffiti

**[0:06:45]** with nan. Otherwise, this would be 100 times harder. And graffiti is the same tool that I use with knowledger graphs in Python that I covered on my channel earlier. And so I've got my digital ocean droplet up here. And this is the same droplet where I have my N8N

**[0:07:00]** instance up and running. And so I'm going to follow these instructions, which I'll also have linked in the description to get graffiti in Neo4j up and running. It's really not that bad once we get to it here. So I'll go ahead and copy this first command here to

**[0:07:13]** clone the repository. So we're calling in graffiti just like you do with N8N. And then I'll change my directory to graffiti/mcp_server. And the first thing that we have to do is set up our environment variables. So I'll go into.example. I'll print it out here so that you can see. The main thing

**[0:07:30]** that we have to set is our OpenAI API key because we're using a large language model to extract those entities and relationships. That's one of the things that Graffiti does for us using OpenAI. And you can configure this to use other providers as well. That's outside of the

**[0:07:46]** scope of this video, but definitely let me know if you want me to evolve this template to work with CloudN, different LLM providers. There's so many things I can do to continue to build this out for you. So yeah, we just have to set our API key and you can also change your

**[0:07:59]** model name. And so what you want to do is do a copy of.ample and you want to change this to env. So then we can do a nano.env. And this is where we can go and set our API key. So you change this value right here. You can also change your Neo4j

**[0:08:16]** password if you want for the underlying database. And then to exit out of this, you do control or command X and then Y and then enter. Once you've made a change, that's how you actually do it. So here I'll actually make a change and show you. So it's controll X, then Y,

**[0:08:30]** then enter. That is how you save your changes. So off camera, I'll set my OpenAI API key and then I'll be back. Oh, and one last note for this, you're probably going to want to change your URL from localhost to Neo4j. Since we're working in containers here, we need to

**[0:08:46]** reference the service name of our Neo4j container. So just a tiny detail there that's really important. That actually tripped me up as I was getting this set up for you. So, make sure you adjust that. All right. Once you have your environment variables set up, you can run the pseudo docker compose up-d

**[0:09:01]** command. This is going to get our servers up and running. It might take you a little bit longer. I already run this in the background just so it's quicker. And then to check the logs to make sure things are actually good, we can docker logs and then the name of our

**[0:09:14]** server here. So, I'm just going to copy this and paste it in. And then I this should be uh pseudo as well. So, there we go. All right. So, it's going to spit out a ton of information. You can ignore a lot of these warnings that you'll typically see with graffiti. The main

**[0:09:27]** thing that you're looking for at the bottom here is that it says that ubicorn is running on http 0000 port 8000. And you can also configure this port if you want as well by going into the docker compose. It's a little bit of an advanced thing, but I actually did this

**[0:09:41]** because where I've been running this before uh I was already using port 8000. So I just changed this to map uh port 8030 to 8000 as well. So yeah, you can go ahead and change that. Otherwise, we are looking good. You now have everything up and running. And you can

**[0:09:55]** do a final check by doing uh docker ps- a. It'll show you all of your containers that are running. You want to make sure that none of these say error or exited or restarting, anything like that. So, we've got our N8N and then caddy as well. And then we got Neo4j and our

**[0:10:10]** graffiti MCP. All right, things are looking really good. Now, the last thing that you need to do that is a kind of awkward hacky thing is we have to make sure we actually open up the port so that N8N can connect to our graffiti MCP. And this is the most technical and

**[0:10:26]** hacky part of our setup here, but I'll have step-by-step instructions in the description so you can copy and paste some things that we're about to do here. I'll make it as easy as possible. So, first things first, we need to change our directory into where we set up N8N

**[0:10:39]** because what we need to do is make a super small tweak to the Docker Compose. I already made the change here and I'll have this in the description for you to copy. But, we have to add an extra host so we can use host.doccker.in. This is how we're going to within our

**[0:10:54]** N8N workflow builder connect N8N to our graffiti MCP. And I'll show you what that looks like in a little bit as well. So, you just have to add these two lines right here. And then again it's control or command X Y and enter to exit once you've made that edit in nano. So there

**[0:11:10]** you go. And then you do pseudo docker compose up-d. It's the exact same command that you use to start n for the first time and what we used previously. So you go ahead and use that. Then we are good to go. Now there's just one other thing that we have to do with our

**[0:11:22]** firewall here. What we need to do right now is access the end container and figure out what the gateway IP address is. I know that sounds really technical but don't worry. All we have to do is pseudo dockerexec-it and then the name of our container that we get from the ps command. And so I'm

**[0:11:40]** just going to copy this one right here. This is the name of our container. Paste it in. And then it is /bin /sh. And so this is going to get us within the docker container for nadn. So any commands that we execute now are within this container. We want to do ip route

**[0:11:57]** and then gp default. And you can copy and paste this from the description as well. So we get this IP address right here. So you want to copy this. This is absolutely crucial because now we're going to exit out of the NN container and we're going to do pseudo UFW allow

**[0:12:14]** from and then we have this IP that we just copied. So I actually didn't do that yet. So I'll copy and then I will paste and then to any port and then 8000 or whatever the port that you have set up for your graffiti MCP. So like I

**[0:12:29]** changed mine to 8030. Whatever you need to do here, change it. And so the reason that we're doing something so specific here is we don't actually want to open up this port to the entire public. If we wanted to do that, we could just do pseudo UFW allow and then 8030. So

**[0:12:44]** you're getting a little bit of a network lesson here. I'll make it super brief, I promise. But this would open up the whole port to the entire internet. So instead, we're only allowing this IP. This is the gateway from the N container to access this port. So, we're keeping

**[0:12:57]** security super tight here. And then we can do pseudo UFW reload. So, really specific thing. Just have to bear with me on that. But yeah, we have our firewall set up. So, now N8N can access the graffiti MCP and everything is still secure in our digital ocean droplet. So,

**[0:13:13]** now back in N8N, we are going to install the community MCP node. And the reason that we need this is pretty simple. The MCP functionality built into N8N natively only supports using MCP servers as tools, but within our template, we're using the Graffiti MCP server, not as an

**[0:13:34]** agent tool. You can't actually set this up with the native N8N integration with MCP. So, we're going to use this server right here. So, you can copy the name N8N- nodes-mc. Go to your settings in the bottom left in N8N community nodes. And then when you add a new node, you just paste in

**[0:13:52]** the name that I copied from the mpm page. And then you check this and install. And then you are good to go. And so I've got mine installed obviously already. So if I add the plus icon here and I search for MCP, take a look at this. I can do MCP client. This is the

**[0:14:07]** one from my community node. And the way that you know that is that it has a publisher here and it's via npm. And specifically to test the connection with the MCP server, I like to use the list available tools function. And so I'll bring in this node. I won't actually

**[0:14:24]** attach it to anything yet. I'm just going to set up my connection to my MCP server, make sure everything's good, and I can view the tools that are available in the graffiti MCP server. And so I'll make a brand new connection here just so I can show you. So for graffiti, it is

**[0:14:38]** server sent events as the protocol. And then for the IP here, we did all that work to set up host. docker.in internal because we need to tell the nn container to look outside of itself to our host machine where we have the graffiti mcp running and then my port is 8030 and you

**[0:14:55]** can keep it as slash ssee. So go ahead and click save and then we can exit out of this and then we can execute this step that's just in isolation right here to make sure that things are working and there we go. Cool. So we have an add

**[0:15:08]** memory tool. This is what we have in our rag pipeline for actually adding into our knowledge graph. And then we have the search memory nodes tool. This is the primary one that I have as the tool for my agent here in this template. And then there are some other ones as well

**[0:15:22]** that aren't really something I'm going to be covering here, but it's actually really nice. Like there are other tools that we have here like get entity edge that's more about like once you have a certain node selected, you can then search through relationships to find other nodes around it. So, there's more

**[0:15:39]** advanced things that I really do want to cover later as well, but for this video, I'm going to keep things simple and just use the two tools that we have at the top. I want to add memories and I want to be able to search through memories. And so, I'm going to delete this guy

**[0:15:51]** right here cuz I'm just using that to test the connection. The main thing that I added into the rag pipeline here is a single call to the graffiti MCP. And so, my operation here is execute tool instead of listing the tools that we just looked at. And for the tool name

**[0:16:07]** specifically, I actually got that by the list operation. It is add memory. And these are the two properties that we have to specify. We need to specify the name of the document that we're adding in as an episode to graffiti. And then also the episode body. This is the text

**[0:16:23]** from the document that it is going to use an LLM through OpenAI in this case to extract the entities and relationships. And so this single edition is all we have to do. super super clean to make it so that we're now adding into our knowledge graph along with our vector database in our rag

**[0:16:40]** pipeline. And then it's just as easy for the agent. So along with all the other rag tools that we have, we're now just adding a new MCP client tool where the operation is again to execute a tool, but this time the search memory nodes. The only thing that we need to specify

**[0:16:55]** for the parameters here is the query. What's the query for searching our knowledge graph? And we're letting the LLM decide that. So the AI agent when it invokes this tool, it determines what the query is because obviously we don't want to have to specify to the agent exactly what the query needs to be. So

**[0:17:12]** it gets to make that up. We're giving the agent that control. And that is it. That is everything you have to do. Like I promised, the setup was mostly just getting the MCP server up and running on our digital ocean droplet. Yeah. And then just for a little demo here, I will

**[0:17:25]** do a test event with a file I have updated in Google Drive. And then I'll go ahead and send this in through the full pipeline here. Take a look at that. We have inserted it into our knowledge graph. The full content of the file and the title being sent in to be processed

**[0:17:40]** into our knowledge graph. So an LLM is going to run to extract the entities and relationships. And there's a queuing process here because knowledge graphs are slower and more expensive compared to a more traditional rag agent with just a vector database. That's the last point that I want to drive home for you

**[0:17:57]** here. your use case might not be the best for knowledge graphs if you don't need that extra power for querying or if you don't have really relational data. Knowledge graphs might just slow you down. Using an LLM to extract all of these nodes can be a slow process. So if

**[0:18:14]** you're working with a ton of data, you should probably just stick to a vector database. And I'll probably make more content on the future doing these kinds of comparisons for your use case, helping you figure out do you want knowledge graphs and vector databases or just a vector database or just a

**[0:18:30]** knowledge graph. There's so much more that I could dive into here. Like I'm really just scratching the surface of what is possible with knowledge graphs for you and helping you incorporate them for the first time in your N8N workflows. And so I hope that you found this super super useful getting you

**[0:18:44]** started with knowledge graphs in N8N. If you did and you're looking forward to more content on AI agents and rag and knowledge graphs, I would really appreciate a like and a subscribe.
