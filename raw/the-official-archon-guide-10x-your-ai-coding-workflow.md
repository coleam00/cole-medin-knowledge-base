---
type: raw-transcript
title: "The OFFICIAL Archon Guide - 10x Your AI Coding Workflow"
youtube_id: DMXyDpnzNpY
url: https://www.youtube.com/watch?v=DMXyDpnzNpY
slug: the-official-archon-guide-10x-your-ai-coding-workflow
published: 2025-10-11
duration: "0:23:19"
fetched_at: 2026-07-21
immutable: true
---

## Transcript

**[0:00:00]** Welcome to Archon, your command center for AI coding. It is your tool to manage all of your knowledge and tasks for your AI coding assistant. The big goal of Archon is to be the one tool that enables AI and human collaboration at a very deep level. It's something that is

**[0:00:18]** very much missing in the AI coding space right now. So, Archon is the tool to fill in that gap for you. for you as the user. It is a beautiful user interface to manage all of your projects and tasks and all of the knowledge that you're curating for your code bases, the

**[0:00:34]** libraries that you are using. And then for the AI coding assistant, it is an MCP server to manage all of the same things. So super easy to connect this to literally any AI coding assistant. And then you instantly give it access through the MCP to search all of the

**[0:00:50]** documentation that you've curated and manage the same projects and tasks in this canban board. And so for this video right now, I've got three things for you. First of all, I want to cover why we actually care about using Archon in the first place. Then a quick start. I

**[0:01:05]** just want to help you in a couple of minutes get Archon fully set up and connected to your AI coding assistant. And then the last thing that I want to go through with you is a practical guide on how to use Archon in your AI coding workflows so that you can significantly

**[0:01:20]** improve the code quality output of your coding assistants and how easy it is for you to manage your AI coding assistance. So putting yourself in the driver's seat while also still enabling your AI coding assistance to go very far. Now first of all why do we care about using Archon in

**[0:01:37]** the first place? I mean, that's the big question you have whenever you're looking at a new tool, especially when it's one related to AI and there's millions of tools out there. Well, the big problem that we have with AI coding assistants right now is they take care of too many things under the hood.

**[0:01:53]** Here's what I mean by that. In our tools that we have like Kirao or Cloud Code or Codeex, all these coding assistants, they have the ability to search the web. That's their way to retrieve external documentation. right now searching the web for lang chain or pideantic AI all

**[0:02:08]** these libraries that we're using and they also have the ability to create their own internal task lists so they can organize their own work and knock things out task by task and that's all fine and these capabilities are quite powerful but the problem is there's not really a way for us to collaborate with

**[0:02:26]** the AI coding assistant on these things we can't really pick the knowledge that it searches through because it's just going to search the entire internet we can't really interact with this task list. It's more of an internal tool. You see the problem here? It takes care of a

**[0:02:40]** lot of things for us, which kind of kicks us out of the driver's seat in some ways that we'd really want to be a part of the process, actually defining the tasks and choosing the different sources that our AI coding assistant is going to look for to understand the

**[0:02:54]** libraries that we're building with. And that is exactly what Archon helps us with. So, I have a little demo going on the lefth hand side here. This is more just mock calls to show you how archon works at a high level. We'll really get into the AI coding workflow in a little

**[0:03:06]** bit here. And so, first of all, it's searching my documentation, everything that I've already curated for it in the Archon user interface. So, I get to point it to where to search. And so, it pulls certain pages from the documentation. It's performing rag under the hood for both keyword and semantic

**[0:03:23]** searching. Very, very powerful rag strategies that we have for this. And then I also have it set up to manage the tasks here. here. So, we'll see in a little bit that it's going to start moving around these tasks and it's going to be realtime updates for us. So, when

**[0:03:36]** it uses the Archon MCP to move these tasks around, we don't even have to refresh our UI and we can watch it work in real time. And we can even create our own tasks here without even having to interrupt Cloud Code. We can collaborate with it because the next time it looks

**[0:03:51]** at the tasks that it has to do, it'll find those new tasks that we have created for it. So, take a look at this in just a second here. We'll see it move the first task to doing. Boom. There we go. Live updates. And it's just going to

**[0:04:02]** keep going through moving all these tasks around. It's kind of simulating what we do in a real AI development workflow. So there we go. It moved it to review. And then it's going to keep going on and on and on. Very, very cool. And there are so many other things that

**[0:04:16]** we have in store for Archon as well. Being able to actually kick off our AI coding assistants as background tasks in Archon for our planning or validating like reviewing our poll requests. There's so many different things that we have in store for Archon. This is just the beginning that we have for the

**[0:04:33]** knowledge and task management, but still very very powerful. And so with that, now that you got a good understanding of how Archon works at a high level, allow me to help you get it set up now connected to your AI coding assistant in just a few minutes. So getting started

**[0:04:46]** with Archon is fairly straightforward and most of the setup you're actually walked through in the user interface once you have the application up and running. I'll show you that in a little bit. And there are only a couple of prerequisites that we have in this readme which of course I'll have this

**[0:05:00]** linked in the description. You'll want Docker or Docker Desktop preferably because Archon runs as a few different containers. You'll want Superbase because it's the database that powers all of Archon. There is a free tier for the cloud superbase. You don't even have to pay anything. That's what I'm using

**[0:05:16]** for this demonstration. And then also local Superbase works. If you want to host it yourself, you can do that as well. And then you'll obviously need an API key for an LLM provider, OpenAI. And then we also support Gemini and Olama. So if you want to run things 100%

**[0:05:32]** locally to have your own private knowledge base, you can do that with Olama. And so that's another really awesome benefit to Archon. And then to get started, all we have to do is start by cloning the Archon repository. And we're using the stable branch because that's where we have the official

**[0:05:48]** releases. And so you can use the main branch if you want something a bit more experimental, but I'd recommend starting with the staple branch. Then we just change our directory into archon. And now you can open up this folder in your favorite code editor. Like you can do

**[0:06:01]** Visual Studio Code or Windsurf or Cursor, whatever you want to do. Go ahead and open this up. And then we can set up our environment variables. The only two values we have to set right now is our Superbase URL and service RO key. everything else like our openi API key

**[0:06:18]** for example we actually set in the archon user interface in the settings page we'll see in a little bit and so going to my superbase dashboard the way that you get these two values for cloud superbase is you go into your project once you have it created go to the

**[0:06:32]** project settings on the lefth hand side and then when you go to data API this is where you can get your project URL so go ahead and copy that and insert that for the superbase URL and then to get your service role key you go to API keys And

**[0:06:45]** then you want to reveal and copy the service role secret. And we want to be in the legacy API keys tab. So go ahead and fill out both of those things right here. If you are running local superbase, then usually your Superbase URL is going to be this right here. So

**[0:07:00]** host.doccker.in pointing outside of the archon container then with the port for your Superbase Kong container. And then this service ro key. You set that yourself in the environment variables when you are self-hosting a superbase. That is all you have to do. Now our environment variables are set up. Make sure you

**[0:07:18]** actually do that in av file. So you'll copy. Rename it to env set up those values. And now we can start the archon containers. And actually one last thing before we spin up archon, we need to set up our database. And so going back to the instructions in the readme, we just

**[0:07:34]** finished our environment configuration. Now we need to run our database setup. And so I call up the specific file right here that has all of the SQL you need to run. So you just need to go to migrations complete setup.sql. Copy the content here. And then we'll go into our

**[0:07:49]** SQL editor in Superbase. And so going back over to Superbase, it's this tab right here in the top left for the SQL editor. Create a new snippet. Paste it in and run it. This is going to create all of our archon tables. And you don't have to know every single table that we

**[0:08:04]** need to create here, but I'd recommend just going to the table editor and making sure that you see a lot of Archon tables here after you run that SQL. So, awesome. And this is all going to be empty now, but we're going to populate this in a little bit when I show you

**[0:08:15]** practically how to actually use archon. So, going back to the guide here after we have our database set up, now we can move on to actually spinning up the containers. And it's just a single command. You got make sure you have Docker installed. Once you do, it's just

**[0:08:30]** a single command to spin up everything. And so I'll go to my terminal here back in our archon folder. Paste this in docker compose up build-d. This is going to build all of our archon containers at the same time. We got one for our user interface, one for the MCP server, and

**[0:08:46]** one for all of the API endpoints. And it's going to take a little bit to build. So be patient. Come back in 10 to 15 minutes, and then we'll be good to move on. All right, our containers are built. This is what your logs should look like if everything is working well.

**[0:08:58]** You can also verify that the three containers are up and running in Docker Desktop. Then with that, we can go straight to the Archon user interface local host port 3737 by default. Those ports are configurable as well. So you want to bounce right to the settings page here because you want to set up the

**[0:09:15]** credentials for the LLM providers that you want to use. And so all these are blank by default. I'll just start by using OpenAI right now. So I'll save all my changes. And then I can select the provider I want to use for both my large language model and my embedding model.

**[0:09:29]** Archon uses both under the hood for crawling for all the documentation that we store in our knowledge base. And so we have quite a few different chat providers that are available. I'm just using OpenAI. You can select your model and then click on save settings. Don't forget to do that. And then after we

**[0:09:44]** save the settings for the LLM, then we can go to our embedding provider. There's less options here because some providers like open router don't actually have embedding models, but we can set each one separately. I can use OpenAI for chat and then I could use Olama for embeddings for example. So

**[0:09:59]** select your provider here again, set the model and then save your settings and then boom, we are good to go. That's everything that we have to set up in the settings here. And then going to the MCP tab, we have instructions for how to connect Archon to pretty much any AI

**[0:10:13]** coding assistant. I mean, we don't have explicit instructions for every coding assistant here, but we have a lot covered. And any MCP compatible AI coding assistant can connect to Archon. So, you can kind of just copy the instructions we have for one of the other coding assistants. So, for cloud

**[0:10:29]** code, for example, I'll go here. I'll copy the single line. That's literally all I have to do. Then, I'll go back to my editor here. All I have to do is paste this command in my terminal. And boom, I am now connected to Archon. It is that easy. I just get this error

**[0:10:41]** because I already am connected. But then I can do claude mcp list and this is going to actually verify my connection to archon. Looking really really good. So you just have to follow whatever process we have here based on your AI coding assistant and then you're good to

**[0:10:55]** go. The last thing that I'd recommend doing is go back to the settings and copy the recommended global rules that we have for your coding assistant. So you got one for cloud code and then one that applies to any other AI coding assistant. So copy this and then for

**[0:11:09]** cloud code for example, you just go to your cloud.md. I've already got this pasted in here. And then for another AI coding assistant like Codeex, it'd be something like your agents.mmd. So just follow the instructions to set up global rules for your coding assistant and paste this in. And this is all you need.

**[0:11:24]** Your coding assistant now understands how to use archon for the knowledge and task management. And then upgrading archon is also very easy. When there are new changes you want to bring in for new releases that we have, you just have to pull the latest changes with git. run

**[0:11:39]** the exact same docker compose command that you ran to start things for the first time. And then the last thing is there's a section in the settings page that will alert you of any migrations that you need to run. So you can click on a button right here, copy the SQL to

**[0:11:52]** run those migrations and then you go into the SQL editor just like we did earlier running that to get your database up to speed as well. That is it. Very easy to upgrade. So with that, you have Archon fully set up. Now quick word from our sponsor, which is very

**[0:12:06]** thematic for Archon, by the way. Then we'll get on to how you can practically use Archon in an AI coding workflow. I'll show you how I approach a brand new project, how I incorporate Archon into it. The sponsor of today's video is none other than Superbase themselves, which I

**[0:12:20]** am pumped for because for the longest time, they've been a core part of my tech stack and the database that powers all of Archon. Very thematic. They recently had their first ever conference, Superbase Select. That's the video you're looking at right here. It's the full recap, which I'll link to in

**[0:12:35]** the description. and their CEO Paul Coppstone. He kicked things off by introducing a lot of incredible new additions to the platform. Starting with a remote MCP server. I've been waiting for this one so our agents can manage our Superbase projects without us having to install anything. And then a lot of

**[0:12:52]** new things for scalability enterprise level in particular incorporating S3 buckets, Oreo which is a platform they just acquired and a new open source initiative for database orchestration called multi-gress which is probably the biggest thing for making superbase that much more scalable. I really do think that Superbase is the future of

**[0:13:11]** Postgress. When they say scale the millions they really mean it. And the biggest takeaway that I got out of this event is that they understand the limitations of Postgress as the underlying database and they're addressing that by building things on top of the Postgress engine while still making it just as easy for us as the end

**[0:13:28]** users to leverage Superbase. And with that, they've got their series E for a $100 million raise and a $5 billion valuation, which is extremely impressive. And last thing I'll say, if you really want to dive into multi-gress and see how that makes Superbase so scalable, Sugamarine did a talk right

**[0:13:47]** after Paul Coppstone where he covers more of the core architecture. So if you want to get more technical and see how Superbase can really scale, definitely check that out. And really the whole recap is worth checking out. So link in the description. I am always behind Superbase and I love it as a platform.

**[0:14:03]** So, this is probably the most important part of the video, showing you how to use Archon in an AI development workflow. And the main point that I want to drive across here in the next like five minutes that I've got with you is that it's up to you to define your own

**[0:14:18]** AI coding workflow and how you want to incorporate Archon. There's a lot of flexibility here. I'm going to recommend a couple of commands that I have for reusable workflows. But you get to decide when archon looks in the knowledge base, when it manage tasks, does it create the projects? Do you

**[0:14:33]** create the projects for the coding assistant first? That is all up to you entirely. And so when I am starting a new project or a new feature in an existing project, the first thing I'll do is set up my knowledge. What are the files that I want my coding assistant to

**[0:14:49]** reference or the documentation that I want it to search through? For example, maybe I'm building an AI agent with Pantic AI or I'm working on some backend that's using Superbase for the database and I want my AI coding assistant to be able to search through this documentation to understand how to code

**[0:15:04]** with Pantic AI or with the Superbase SDK. So find those resources and what you want to do is you want to go to the documentation. So for example, I can go to Google here and I can go superbase documentation. There we go. I got the superbase docs and I can actually start

**[0:15:22]** by just crawling this if I want to. So I can go to archon, click on add new knowledge, paste in this URL and start the crawl for any old website. This works. However, there are a couple of formats that are actually more optimal for crawling. So going to superbase to

**[0:15:39]** the documentation here. If I go to llms.ext, text. Take a look at this. Most documentation websites, if you just append llm.ext to it, I can do the exact same thing for Pantic AI. It has this curated list of files that are ready to be ingested as markdown for your AI

**[0:15:59]** coding assistant. So, I'd highly recommend looking to see if your documentation has that, and then if it does, copy this, go into Archon, and then crawl this instead of just the raw web page. I'll actually start the crawl here so we can see this in action. Another format that's really great is

**[0:16:16]** sitemaps. And so mem zero for example, which is a tool for agentic memory. They have a sitemap. And so I can do just/sitemap.xml. This is typically how you check for a sitemap. This is also a very good format. So I can copy this, go into archon, add this knowledge, start

**[0:16:34]** crawling. Boom. There we go. And you can crawl in parallel if you want to. So now we're crawling both the MEZO and Pantic AI documentation at the same time. And once this crawling is complete, our coding assistant through MCP will immediately be able to search through everything that we brought into our own

**[0:16:51]** private knowledge base. All right, I have both of my documentations crawled now and I can also click in to view the different chunks and the code examples that we're able to search through with the Archon MCP. And again, these can be any URLs that you want to crawl. I would

**[0:17:06]** recommend generally sticking to library documentation, especially with the sitemaps and the LLM.ext, but it is quite flexible. There's a lot that you can bring into your Archon knowledge base. So, we've got that set up now and we already have Archon connected through MCP. Now, we can dive right into coding

**[0:17:23]** something. Now, when I am creating code with an AI coding assistant, I always split things up between planning and implementation. I even have a full video that I'll link to right here where I go through my general process. And there's this really nifty Excal diagram that I have going through how I plan things out

**[0:17:41]** and then how I implement it. And I don't do all of this from scratch every single time. I take my general process for planning. I package that up into a markdown document that I have as a reusable workflow. You can take this as a starting point if you want. I'll have

**[0:17:59]** this linked in the description as well. But I encourage you to take my general ideas around planning and executing and actually build your own workflows. And that's the thing with Archon is you get to customize how you leverage it in your workflows. Like for example, I have step

**[0:18:16]** one, read and analyze a requirements. So there's a specific file that I pass in which is just what I want to build. And I have a really simple request for this demonstration purpose. I just want to build a panenti agent that uses mem. So obviously it has to leverage both of the

**[0:18:30]** pieces of documentation I have in archon. So I have it understand the requirements first and then I have this little research phase where it lists the different sources that we have crawled in archon and then it performs rag to look through the different chunks and code examples that we have there. And

**[0:18:46]** then I do codebase analysis if it's a feature in an existing codebase. And then I have a plan and design. I don't need to cover this whole markdown because the point I'm trying to drive home here is I just fit archon into some part of my planning process and you can

**[0:18:59]** customize this to however you want your AI coding assistant to use archon. And then I'm going to do the exact same thing for the implementation phase. I'm going to take my general process, package it up into a command that I can execute as a reusable workflow. And this

**[0:19:15]** one specifically speaks to how to leverage the projects and tasks within archon. So, I tell it to look in my global rules because this is where I'll specify any existing projects in Archon that I'm working on. If it doesn't find one there, then I tell it to make a new

**[0:19:30]** project and then manage all the tasks. So, create new tasks for each of the things that it's doing to knock out my implementation for me. These are the kinds of things again that you can customize to however you want to use Archon. And I'm going to keep saying

**[0:19:43]** that over and over again because that's the main point that I want to drive home here. And so, I'll show you. I actually ran the create plan already on my simple request for the Pantic AI agent. And here we go. It's using rag uh in Archon to search through the chunks and the

**[0:19:58]** code examples. It's doing quite a bit analysis here. This is looking really good. And then finally, after it reads through all of my documentation that it thinks it needs, it builds the plan for me. So, I go into the PRPS folder. This is a very simple version of PRP, by the

**[0:20:14]** way, if you followed my other content in the past. But yeah, take a look at this. We have this full implementation plan with all my research findings from Archon. It's got the different tasks that I wanted to knock out one by one. So now when I go and actually execute

**[0:20:28]** this plan, we're going to have all of these tasks created and managed in Archon. It is a beautiful thing. So I'm going to come back once I have everything executed. I'll show you how that worked as well. All right. I just wanted to come back mid-execution really quick to show you that I executed my

**[0:20:44]** workflow. It's starting a new project and adding a bunch of new tasks. And so we can see that here it created a brand new project in Archon. The nine tasks that I had in the plan that I created, it converted into Archon tasks and it moved the first one into doing to set up

**[0:20:57]** the initial project structure. Very, very nice. So, not only is it easier for us to manage the tasks for our coding assistant in Archon, it also gives us a lot of observability into what's happening. We can even click in to see the description to kind of see a little

**[0:21:10]** bit of extra details of what the coding assistant wants to do for this specific task. And again, we can always edit this to change the instructions live. We can add new tasks if we think it's missing something. We have that flexibility to edit things live and again determine the

**[0:21:26]** workflow in the markdown document. So I'll come back again once we have the final implementation. Okay, our implementation is complete. I just cut it short of the validation here because it's not the point to have a fully complete solution in this video here. But yeah, it's got all the tasks in

**[0:21:41]** review. It was just about to create the tests and then move everything into done. So the Archon integration for the project management is working perfectly. And if we look at the code just really quickly here, I can see and I I checked this off camera already. It's looking

**[0:21:54]** really good. Like it clearly understands how to build padanti agents, how to work with the memories with me zero. This is the kind of thing it would not have been able to figure out without being able to look at the mem zero and podantic documentation because LLMs have the

**[0:22:08]** notorious training cutoff. They don't understand these libraries and that's why we need rag with archon for it to write accurate code and it definitely looks like it did. So yeah, at a high level that's how I use archon with my planning and my executing. Build these workflows yourself. take inspiration

**[0:22:26]** from this if you want because again I will have these linked in the description if you want to use these slash commands and slash commands are just prompts and so no matter your AI coding assistant you can tell it to look at this markdown document and and execute this operation you don't have to

**[0:22:41]** use cloud code like I'm using in this demo it is just my preferred AI coding assistant right now so that is everything that I have for you my friend on using archon a full guide with the setup and how to incorporate in your AI coding workflows I definitely want to be

**[0:22:55]** putting out a lot more content on my channel in the near future as well, diving even deeper into incorporating Archon into building full projects end to end. So definitely stay tuned for that if you're interested. If you appreciated this video and Archon and you're looking forward to more content

**[0:23:11]** on AI coding and using Archon, I would really appreciate a like and a subscribe. And with that, I'll see you in the next
