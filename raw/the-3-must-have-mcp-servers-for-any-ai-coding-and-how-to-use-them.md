---
type: raw-transcript
title: "The 3 MUST Have MCP Servers for Any AI Coding (and How to Use Them)"
youtube_id: MBaTuJfICP4
url: https://www.youtube.com/watch?v=MBaTuJfICP4
slug: the-3-must-have-mcp-servers-for-any-ai-coding-and-how-to-use-them
published: 2025-05-14
duration: "0:19:57"
fetched_at: 2026-07-21
immutable: true
---

## Transcript

**[0:00:00]** A couple of months ago, I revealed to you my full process for using AI coding assistance to build anything fast. But since then, there have been a few new MCP servers that have come out. And so right now, my workflow for coding anything with AI revolves around three

**[0:00:14]** core MCP servers. So, I want to cover those with you right now. But then on top of that, I also want to do a live build with you showing you how we can use these MCP servers together effectively to build anything. You can transform any AI coding workflow with

**[0:00:29]** these servers. no matter what you want to build. So, let's go ahead and dive into that right now. So, here is the document outlining my full process for using AI coding assistance to build anything. I'll link to this in the description of this video. I shared this originally in the other video that I

**[0:00:44]** mentioned. Everything in there is the same except I've updated section 4 where I dive into using MCP servers. And so these are the three core servers that I'll cover in this video. There are some other ones that are worth looking into as well. These are the ones that I use

**[0:00:58]** no matter what I am building. And the important thing to note here is that for each of these servers, there are going to be multiple options. So, I'll talk about a couple of these alternatives but obviously I want to focus on just one for each of these three categories.

**[0:01:11]** So, the first kind of MCP server that you want no matter what is one to bring external knowledge into your AI coding assistant for things like library and tool documentation. So, you have Superbase, MCP, Pyantic AI, all these things that you're building with a lot. these AI coding assistants don't know

**[0:01:28]** them very well. And even though we have built-in documentation support for some AI idees like Windsurf and Cursor, it doesn't always work the best. And so, we want an MCP server that can essentially be the rag knowledge base for our AI coder. And the one that I would highly

**[0:01:43]** recommend using is one that I actually built myself. It's completely free and open source. I built it for you specifically for bringing it into your AI coding assistance. You can crawl any website, any documentation and then use it then as a rag MCP server for your AI coding assistant and all of the

**[0:01:59]** knowledge that you build as a part of the server is stored in your own private superbase. So it's your own knowledge base that you set up and manage for yourself. Another good option that I've covered on my channel previously is contact 7. Now this isn't going to be

**[0:02:12]** building your own private knowledge base like this server is but this is another good option. It's more out of the box. They have thousands of libraries that are already ingested in their knowledge base that you can leverage immediately again as an MCP server. So that is the core one that you want. I'm going to be

**[0:02:28]** using this one that I built in this video here with crawl for AAI. I'll show you how we can use it to crawl like Superbase and Pantic AI. Bring that into our knowledge base. And then the next kind of server is you want one to help you manage your database so that when

**[0:02:42]** the AI coding assistant starts a project for you, not only can it write the code but it can also create everything in the database like new functions, new tables and superbase is the primary one that I use. And so I have this link as well in the description of the video to the

**[0:02:57]** Superbase MCP server. This can create tables for you, list your projects that you have in your Superbase organization. It can write queries like pretty much any SQL query you could want. It can do that as a tool. So it's just a super powerful way to manage your database

**[0:03:13]** with natural language. So as a part of your process for building your application, it can build all the tables as well. Another one that I mentioned before on my channel is Neon. That's a serverless Postgress platform that has a similar MCP server. And so depending on the database that you're using

**[0:03:28]** hopefully there will be an MCP server that'll help you manage that with natural language. And I definitely think we're going in a direction where pretty much every single database you could use is going to have an MCP server. So we might not be there yet. We probably will

**[0:03:41]** in the near future. And then the last server that I use no matter what is one to search the web. And typically I use the Brave MCP server. So I'll have a link available for this as well. The Brave API is pretty affordable and it is very very powerful. It's the kind of web

**[0:03:56]** search that's better than just something that you would have with ChatGBT or Claude by itself. It has a very AI ccentric web search summarizing things for AI. The way that it pulls information is just perfect for LLMs. Usually I'll use this kind of in tandem with my RAG MCP server. So I'll look in

**[0:04:15]** my knowledge base, but then also search the web for supplemental resources. Like sometimes there'll be documentation that wasn't included in the knowledge base or maybe there's like community forum posts that provide examples similar to what I want to build. And then the Brave MCP server will help me find that. And if

**[0:04:31]** you want to bring these three MCP servers into your own AI coding workflows, which I would highly recommend doing, then the links that I have in the description to each of these also have very detailed instructions. Like for the crawl for AI rag MCP server that I built in the readme, I made sure

**[0:04:46]** to walk you through everything as far as installing, setting up the project getting your database configured and ready to crawl websites and put in your knowledge base. You can take care of all that just reading through this step by step. And then for Brave, you just have to create your API key and they have

**[0:05:00]** instructions for how you'll set this up in Cloud Desktop or Windsurf or Cursor whatever that might be. And then for Superbase, it's the same kind of deal. And the configuration is generally going to look very, very similar between these different MCP servers. And so going into my own Windsurf here, I have the

**[0:05:16]** configuration set up. And the way that I get to that, by the way, I'll just show you really quickly. So when I'm in the cascade mode on the right hand side, you just have to click on the hammer icon for MCP servers and then click on configure and that'll open up this JSON

**[0:05:30]** file for the MCP configuration. And there's going to be something very similar for cursor or rue code or client no matter what AI IDE you are using. You'll have something like this where you can add each of the servers individually. And all these servers are completely free by the way. So this is

**[0:05:44]** my crawl for AI one. Once you follow the instructions and you have the server running on SSE in a terminal, you can then cook into it just like this. And then for the Brave search, we're just pulling this through MPX. The only thing we need to set up beforehand here is our

**[0:05:59]** Brave API key. And there is a very generous free tier with Brave. And so that's why you can get started for free with Brave. Even though there are paid plans, I'm still not paying anything for when I'm using it right here. And then for Superbase, they also have a very

**[0:06:13]** generous free tier that you can spin up an instance, have that running indefinitely, and so you can use this also without paying anything. The only thing you have to set up here is your access token. And in the read me that I link you to, there's instructions for

**[0:06:26]** getting this set up as well. So very easy to get all these configured. Once you have that all configured, you just have to save here, go back into our configuration, and click on refresh. And then that'll load the MCP servers and you can see all the tools that are

**[0:06:39]** exposed from each of these servers and the descriptions for them as well. So we can take a look at everything that our AI coding assistant is now able to do with these tools. And so we're giving superpowers to our AI coders. Now we can dive into using these all together to

**[0:06:54]** build something from scratch, leveraging all these to do something that we definitely couldn't do very easily without them. The sponsor of today's video is Datab Button, the AI app builder for businesses. I've been trying it out the past few weeks, and I've been seriously impressed just how much of the

**[0:07:10]** development life cycle DataButton takes care of for you. Like they say in their homepage, your hunt for a CTO ends here because it takes care of everything from just starting your project all the way to deploying it. When you first begin a project, you can start by describing

**[0:07:24]** what you want to build, giving specific requirements. You can even give inspiration as well like screenshots from other web pages and then you can hook in your integrations like for authentication, your database, what you want for payments and then storage as well. And then you can get started and

**[0:07:40]** the data button agent will go ahead and start creating a full plan with all the tasks listed out that it's going to knock down one by one. We have our preview so we can see what it's currently built so far and then we can interact with our agent on the right

**[0:07:52]** hand side where we provide any feedback or additional tasks we wanted to do. we can kick off each individual task and it'll ask for certain things like our API keys as it sets up superbase and stripe getting all those integrations ready for us and this takes care of the

**[0:08:06]** front end and the back end so you can deploy agents and APIs behind the scenes as well and then deploy it all together once your project is done this takes care of everything that's why they say that you don't need a CTO anymore data button really is a gamecher for lean

**[0:08:21]** businesses that are looking to leverage AI to compete with companies that are 10 times their size. So, I'll have a link in the description to data button. It's free to get started. You can check it out and see how you can use it to really build any app that you need for your

**[0:08:34]** business. All right, here we go. Now, it is time to build. So, we're going to be leveraging my full process for using AI coding assistance. I already have some of the things set up based on this process. So, I'll show you what that looks like right now. Then, I'll show

**[0:08:48]** you specifically how I'm going to be prompting the AI coding assistant to leverage these different MCP servers. and then we'll see it in action as well. And so the first thing is I have my wind surf rule set up which by the way the way you get to that is you just go to

**[0:09:02]** additional options in the top right and go to manage memories and then you can create global or workspace rules. So I created some workspace rules here telling it how to leverage my planning and task files how to use the crawl for AI MCP server all that highle direction

**[0:09:16]** that I don't necessarily want to prompt it to do every single time but I want it to follow this as its golden rules. And then I also have my planning file which I can preview this for you really quickly just so you can see what this looks like. So I use claw desktop to

**[0:09:28]** help me make this. Just giving me an overview of my project and the different components that I want to build out so that the AI coding assistant can reference this and just know what I really want it to build. So I don't have to be extremely specific within my

**[0:09:41]** prompt when I actually kick off the build of this agent that I'm making here. And so what we are building here as our live demo is a rag AI agent with Pantic AI and Superbase. And so we're going to have this local folder that we can put files into. It'll automatically

**[0:09:55]** ingest that into our Superbase knowledge base and then we'll have a simple streamlet interface for us to interact with the agent and ask questions about our knowledge base. So it's a very simple example, still something we care about though. I mean rag AI agents are just so important. And so that's why

**[0:10:10]** we're going to build one right now. And then I also have my task file with all of the individual tasks that we want our agent to look here. and knock these off one by one and then come back and update when these tasks are complete. And so again, everything that I've already

**[0:10:25]** covered in my previous video on my full process, I have that all set up so that now we can just dive right into prompting our AI coding assistant to get started with this build for us. And so I'll show you I have the prompt prepared already. So I'll start at the top

**[0:10:39]** explain everything really quickly, then we'll see it in action. So I'm just starting by saying that I want to build a simple rag AI agent with padantic AI and superbase telling it to read the planning and task files at first as well. And I do specify in the global

**[0:10:52]** rules to do this, but I'm just really making sure that it handles this right now. And then I just describe the different components that I want for my AI agent. And I do go into more detail in the planning and task files for this as well. So just giving the more higher

**[0:11:04]** level instructions right here. And then one really powerful thing for using AI coding assistants in general is to give examples whenever you can. And so for the Streamlit user interface specifically to interact with our agent I've seen in the past that AI coding assistants don't always handle this the

**[0:11:20]** best. And so something that I'm doing here is I'm giving it an example of a streaming interface that I've made in the past specifically to work with Pyantic AI agents. And so I'm referencing it like this in windsurf so it can analyze this file and see exactly how it's going to build this interface

**[0:11:35]** for me for this agent. So that's just another gem that I wanted to drop really quickly for you there. Using examples is so so powerful. And then I do yet another example here. So I have the SQL already prepared for a different project where I created a rag AI agent. So it

**[0:11:51]** can use this as a reference as well while it is using the superbase MCP server to create everything for me in Superbase for this agent specifically. And that's why I tell it here. I tell it to use the Superbase MCP server to create the necessary database tables. Make sure I have the extension enabled

**[0:12:07]** for rag and then using this as an example. And then I continue with the other two servers. So using crawl for AI to get the documentation for Pantic AI and Superbase. I already have all of that crawled. And so I just had a separate request where I'm like, hey

**[0:12:20]** here is the page for podent AI crawl all those docs. And here's the same thing for superbase. So I did that already. Now it has that documentation available. So just perform the rag queries and then also use the Brave MCP server like I mentioned earlier just as kind of like a

**[0:12:34]** supplemental resource for our knowledgebased lookups because sometimes when you search the internet you'll find things like forum posts that have examples for something like what you're trying to build. things that can go in tandem with what we've retrieved from our superbase knowledge base. So using these two servers together and then I'm

**[0:12:52]** also very explicit here telling it to make sure that it uses these servers at the very start of the process so it has all the documentation before it tries to write any code. We don't want it to look up the documentation after writing all the code because then it never is really

**[0:13:05]** leveraging it. And so with that we can now send in this request and see it in action. And so the first thing that it'll do because we instruct it to do so in the prompt in the global rules is to check our planning and task documents. And so there we go. It's looking at

**[0:13:19]** planning. Now it's looking at tasks. And then pretty soon here because we told it to do it early on, it should start using our MCP server. So first it's looking at these examples that we gave, which is good. I want it to do that as well. Now here we go. Now we're hitting the

**[0:13:32]** perform rag query endpoint of our MCP tool getting some of that documentation for Pyantic AI and it's searching multiple different times with different queries. this is exactly what I want it to do to make sure it has a very overarching view of everything that it has to know to implement this agent for

**[0:13:49]** me and then also leveraging the brave MCP server getting some examples with integrating superbase and um pyantic AI together and that's a really powerful thing in general is a lot of times the knowledge base will give you here's how to use this specific library but then the brave search can tell you how to use

**[0:14:07]** these libraries together. So, yet another reason that we want to use both of these tools in tandem. And so, boom it's done with all the knowledge lookup. Now, it's going to update the tasks and it's going to start creating the readme. It'll go through the rest of the process

**[0:14:19]** here. And this is going to take a few good minutes here to build everything out. And so, what I'll do here is pause and come back once it has the first version of my agent complete. And boom there we go. It created the full AI agent for us. It created a readme that

**[0:14:34]** describes the entire project structure. Look at how many files it built for us. Making really a full AI agent application here with the rag pipeline the agent and everything. We can take a look at these individual files. We have the podantic AI agent. We've got our dependencies and we have the definition

**[0:14:49]** of the agent itself. This is looking like really really clean code. We have our prompts. We have our tools for rag. We've got everything for actually processing documents that we upload in a local folder. Bringing that into our superbase. We have all the tests as well because I instructed it to write tests

**[0:15:05]** in our workspace rules. We have our user interface that we can clearly see that like this is inspired by the example that I gave earlier. I mean maybe you don't know that as much as me because I've used that example in the past, but yeah, this is looking really really

**[0:15:19]** good. And then one little glitch here is it made a brand new task file. So it wasn't perfect. And I think there are a couple of bugs that I'll have to fix up here, but still it did a really really good job getting me started. I've got my

**[0:15:30]** example environment variables. So, it tells me everything that I have to set up with instructions to run everything in the read me. Like, this feels like a full software engineer built this out. Like, I'm really really impressed. And so, now what I'm going to do is accept all these changes. I'm going to get

**[0:15:44]** everything set up off camera. There's probably a couple of iterations that I'll have to make to make this like really working. And so, I'll explain all of that after I do it, too. But, yeah let me take care of that now. Then, I'll show you a full demo with this AI agent

**[0:15:57]** that was created for us so fast. All right. So, there were a few things that I had to do to make this in tip-top shape for us. The first thing is even though I told it in the first prompt to use the Superbase MCP server to create my tables for me, it didn't actually do

**[0:16:11]** that. And AI coding assistants are kind of unpredictable. Sometimes you have to reask them to do certain things for you. So, I did that here. We can see that now it used the apply migration tool to create everything with this query that we can see right here. And then going

**[0:16:24]** into my superbase, I'll actually go to the table right now. I now have this rag pages table where we have ID, URL, chunk number, the embeddings. That's what we actually use for rag. So, we're good with the table now. And then there were some issues around how it embedded the

**[0:16:38]** documents that I would upload to the interface. So, I had to fix that as well. Nothing that was related to Superbase or Pyantic AI. So, it leveraged the documentation effectively. Like it actually had zero errors for anything related to padantic AI like in our agent here. And then for Superbase

**[0:16:55]** like when it actually creates the embeddings and ingests those into our database. So this whole setup script that creates this client with all of our functions to do all of our inserts and lookups like all of this was perfect code which is super cool. So I just had

**[0:17:07]** to fix some things with mostly the chunker and then just the way that it ingested. So I don't want to get into the details of all that right now. It's not very important. But now I have the interface up and running. Take a look at this. So I have this streamlight

**[0:17:18]** interface. Let me zoom in on this for you just a little bit here so you can see it really well. Now I can browse my files and I can upload text or PDF files. Those are the two types that I'm supporting right now. And so I just have

**[0:17:30]** this fake company overview generated by Claude that I'm going to use as my mini knowledge base for this simple example. So I'll go ahead and upload this and it'll tell me that it's processing this file. It's creating all those embeddings and inserting it into Superbase for me. And boom, there we go. All documents are

**[0:17:45]** processed. We got five chunks for this file. We now have one document in our knowledge base. Now going back to my table. There we go. All right, we have our five chunks here. Take a look at that. This is so cool. And then now I can talk to my agent or first I can even

**[0:17:58]** show you like if I refresh my page it'll now say like, "Yep, you have one document in your knowledge base." And so now I can just send a basic message to the agent just like, "Hello." All right there we go. We even have the text streaming. So it typed it out in like

**[0:18:10]** typewriter style. Super cool. Now I can ask it a question where it has to leverage my knowledge base. And I know this is super basic right now, but I just wanted to show this at a high level. uh more focusing on my process for using these MCP servers. But yeah

**[0:18:23]** just to show you really quick, I'll say uh give me an overview of the company. All right, so we'll watch it perform rags. So it's going to take a little bit longer now because it's going to search my knowledge base. And boom, there we go. An overview of the company.

**[0:18:37]** Neuroverse Studios, founded in 2022. Let's go check that really quick. So yeah, Neuroverse Studios. Yep, founded in 2022. All right. So, it's leveraging our knowledge base and it's such a simple example, but it's just so cool that I only had to iterate like 20 minutes off camera. So, basically in

**[0:18:54]** like less than an hour, I created this full application using these three core MCP servers to guide the entire process for knowledge, web search, and also setting up my database for me. I had to do nothing in Superbase, and this was all created for me, including the function under the hood that's used for

**[0:19:12]** rag. So, very, very cool stuff. So, I'll have a link in the description to this full example if you want to play around with it yourself. The main focus though was how we could start this project using our three core MCP servers to get our feet on the ground running. I'd also

**[0:19:27]** highly recommend checking out my previous video on my full AI coding assistant process. And also, if you're interested in taking your AI skills to the next level, definitely check out Dynamis.ai. It's my early AI adopter community that I started recently for people like you to level up your AI game

**[0:19:43]** to transform your career or business. And so with that, if you appreciated this content and you're looking forward to more things AI coding and AI agents I would really appreciate a like and a subscribe. And with that, I will see you in the next
