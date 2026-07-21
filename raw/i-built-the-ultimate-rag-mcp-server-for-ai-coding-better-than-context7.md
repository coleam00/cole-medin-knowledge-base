---
type: raw-transcript
title: "I Built the Ultimate RAG MCP Server for AI Coding (Better than Context7)"
youtube_id: ZoyPqXvnnZ8
url: https://www.youtube.com/watch?v=ZoyPqXvnnZ8
slug: i-built-the-ultimate-rag-mcp-server-for-ai-coding-better-than-context7
published: 2025-05-04
duration: "0:28:24"
fetched_at: 2026-07-21
immutable: true
---

## Transcript

**[0:00:00]** With AI coding assistants these days you can pretty much build anything you want. But their biggest limitation right now is they don't always work the best with your favorite tools or frameworks like MCP or Superbase or Pyantic AI. What we really need is a way to give rag

**[0:00:15]** capabilities to our AI coding assistants for the documentation of our favorite tools and frameworks. And so that is why recently on my channel I introduced you to Context 7. This is a free-touse, at least right now, MCP server that instantly provides a rag knowledge base to your AI coding assistants and agents

**[0:00:34]** for the documentation for thousands of different frameworks and tools like Superbase and MCP. A lot of them, pretty much everything that you could care to use is available through contact 7. And so they have both an MCP server that you can attach into your AI coding assistance and then also this user

**[0:00:51]** interface where we can type something like authentication and we can simulate what we'd get back when our AI coding assistant searches the superbase documentation for authentication. So all the tokens that we see here and all these examples and code this is given to our AI coding assistant. So it has

**[0:01:07]** up-to-date documentation to leverage superbase. This reduces hallucinations when coding a lot. It is a very impressive tool. However, there are some pretty big problems with Context 7 that I want to talk to you guys about. And then on top of that, I'm going to introduce you to my new mission to build

**[0:01:24]** something like Context 7, but that is completely open- source and you can run it yourself to build your own private knowledge base for your AI coding assistants and AI agents. So, more on this in a little bit and how I want to integrate with Archon, but right now I

**[0:01:38]** want to talk quickly about the limitations of context 7. The first big problem is that as impressive as it is that there are documentations available here for over 8,000 different libraries you might really only care about 10 out of these 8,000. And so there's going to be a big chance here that your AI coding

**[0:01:56]** assistants will leverage the wrong documentation. It'll just hallucinate in that way because there's really only a very very small subset that you care about. So, it's cool that we have this big collective knowledge base, but you're probably going to want to have something more private and limited to

**[0:02:10]** the tech stack that you are working on. And then the other problem with this is that if you have private GitHub repositories that you want as a part of your knowledge base or something like that, you can't do that because you're forced into this open collective knowledge base. And then another problem

**[0:02:23]** with the whole context 7 MCP server is that even though the MCP server itself is open source like this is the GitHub repository for it. All of the core logic like really the whole context 7 product itself is not open source. And I'll even show you this really quick. It's okay if

**[0:02:40]** you don't understand the code. I'm just going to breeze over this really fast. But if you take a look at the MCP server, like you really dive into the code, you'll see that there's almost nothing here. Like this is it. It's literally 68 lines of code for all of

**[0:02:52]** the logic of their server because they're just hitting this private endpoint that handles searching for libraries. So everything revolving around the scraping and the rag under the hood is all within this private API endpoint that they're probably going to toggle the switch on at some point and just force you to pay for it. Like

**[0:03:07]** they're going to start to monetize this at some point. So it really isn't open source. And so it's not open source. You're going to have to pay for it eventually. And you can't have your own private knowledge bases and we want all of that. And so with this crawl for AI

**[0:03:21]** or rag MCP server that I'm introducing you to now, we have all of those things. You can scrape any website that you want, bring it into your own private knowledge base, and then instantly leverage it in any AI coding assistant or AI agent. That is what I'm super

**[0:03:34]** excited to bring to you today. So to show you at a high level how this MCP server works, I'm going to give you a quick demonstration in Windsurf. And so first, let me show you what I want to build. Let's say I want to build an AI agent with Pyantic AI as my AI agent

**[0:03:48]** framework. But then I also want it to have long-term memory using another open- source tool called Mem Zero. So I want to get the documentation for both of these different frameworks, bring that into my AI coding assistant. And so I'll show you right now I have nothing in my Superbase knowledge base. So this

**[0:04:05]** is the table that this crawl for AI rag MCP server that I'm demoing here is going to populate as it scrapes content from the documentation for both Pyantic AAI and Memzero. And so what I'm going to do is start by taking this llm-text.fold. This is all the documentation for Pyantic AI that's

**[0:04:24]** structured for LLM. So I'm going to copy this URL. Go back to my AI coding assistant. You can see that I have my project set up already with the planning.md, the task.md. I've got my winds surf rules telling it how to use my MCP server. And so what I'm going to

**[0:04:37]** do before I even start the build though is I'm going to ask it to crawl and then I'm just going to give it this link. And so it knows how to leverage that tool within my crawl for MCP server. And I'll even show you that as it starts the

**[0:04:49]** crawl. I've got the container running right now in Docker. We can see all of the requests coming in as it's scraping and then embedding all of the content into my knowledge base. And so I'm going to let that run here. Looks like it already completed. It was super super

**[0:05:02]** fast. We have 288,000 characters, 67 chunks that it's stored in Superbase. And so I'll go back over to my database here and I'll refresh. And then boom there we go. So we have all the documentation for Pantic AI that is now available for rag and our MCP server can

**[0:05:19]** perform rag as well as do the crawling itself. And so now I also just want to crawl me zero. So this time instead of an LLM's- full.ext, I have a sitemap. So it needs to read this sitemap and then visit each of these URLs dynamically. And so this MCP server can also handle

**[0:05:36]** different types of URLs that you give it like the llm's.ext or sitemaps or even if it just needs to recursively scrape from a base URL that you give it like if we just gave it the URL here for the pedantic AI docs directly. It can handle all of those different types of web

**[0:05:51]** pages. And so now I'll just say also crawl and then I'll give it the link to the sitemap for me zero. This is going to take a little bit longer because it has to fetch each of these different URLs, but we'll see it do that here within the document or within the logs

**[0:06:05]** for my container. It's fetching each of the different pages for me zero. It's going to collect all of the markdown files for each of these pages and then it's going to insert them in batches into my superbase database. So, it's also doing a lot of things in batches

**[0:06:19]** where this is super super fast. And so it's not going to be done in like 2 seconds, but there is a lot of information that it's crawling here and then putting into my knowledge base for rags. So I'll pause and come back once this is complete. And there we go. Just

**[0:06:32]** about 20 seconds later, we now crawled everything for the mem zero documentation and inserted into Superbase. I can go back into my table here. We'll still see all the chunks that we have for Pantic AI. Then if I go towards some of the last rows, we now have everything for me zero as well. And

**[0:06:47]** in the metadata, we have important things like the source that each chunk is coming from. So we can still separate the rag search by specific tools and frameworks if you want as well. That's something you can do in context 7 that I definitely did not want to lose with my

**[0:07:00]** custom open source MCP server that I have for you guys with crawl for AI. And the other thing that I want to hit on really quickly before we dive into now leveraging this knowledge to build something in windsurf is that there are a lot of platforms like cursor and

**[0:07:14]** windsurf that provide native documentation search. And in cursor you can even add custom docs. But the performance for this compared to something like contact 7 is not that impressive. Like there's a reason that contact 7 is blowing up right now. And that's what I want to build out with my

**[0:07:30]** own MCP server for you too. I want it to be a lot more powerful than the custom stuff that we have with something like cursor. And it's just going to be a private knowledge base that we can build up even using local LLMs and bringing this tool into our AI agents, not just

**[0:07:43]** our AI coding assistants. So, it's going to be a lot more flexible, a lot more private, and more powerful. That's the goal that I have with all of this. All right, so back in Windsurf now, because we have our knowledge base set up, it's time to dive right into coding our

**[0:07:56]** agent. And so I have my wind surf rules here telling it how to use the crawl forai MCP server. I also have my planning and task documents to give it that higher level direction and the vision that I have for the agent that I want to build. And if you're curious why

**[0:08:10]** I have things set up this way with these three markdown files, definitely check out this video that I'll link to above where I dive into my full process for using AI coding assistance. But that's what I'm following to a te right here. So with all that set up, I can now give

**[0:08:23]** it my first prompt. And I'm going to tell it to use the planning.mmd file to get most of the instructions, what I really want it to build here. And so I'm also telling it in this first prompt to use the crawlforai mcp server to get the documentation for pinantic AI and mem.

**[0:08:38]** And there we go. Right away, it performs that search with that initial query. Pantic AI agent creation and setup. And then the output, these are all the chunks that we have back. and it's truncating some of this text which is why this isn't that long but really there's a lot of context that it pulled

**[0:08:52]** here from our superbase knowledge base and then it did the exact same thing with me zero so I guess it searched pantic a couple of times so let's go down okay now we get to me zero so now it's searching mem zero after it searched pantic AI a couple of times

**[0:09:05]** just getting all that initial context and then after it has all that initial context it'll read through my task file understand what it needs to implement maybe even go back and search with rag more however I instructed and you can change all this in your prompting and your global rules. But yeah, there we

**[0:09:20]** go. We can see it leveraging the knowledge base in real time that we just set up like 5 minutes ago. And that's so cool to me that it's one MCP server to manage all the crawling and the rag lookups, which is super neat. And so what I'm going to do here is now pause

**[0:09:32]** and come back once it has built out the full structure for my agent. And there we go. We have our full agent built for us now with Padantic AI and Mem Zero. And it took a good few minutes to do this. Like there's a lot of work that it

**[0:09:45]** did for me. And then it ended the whole thing with updating the tasks for me. And so let me actually go to that quick here just to see everything that I built. I haven't even looked at this yet. Wow, look at that. Every single X that you see here, it intentionally put

**[0:09:57]** that there saying that it completed that task. And wow, there is so much that it did for me. And it recognized that it probably shouldn't just like try to do literally everything, but it did like at least half if not even more than half of all the tasks that I had laid out for it

**[0:10:11]** here. And I don't want to like demo this full agent and iterate on it and everything right now. I just want to more show you that it was able to leverage the knowledge that we just put in Superbase to build this. But yeah take a look at this. I can just tell

**[0:10:23]** right away from the imports from Pantic AI and the way that it defined the agent and the way that it set up the tools and even the system prompt. Like yes, it definitely understood the Pantic AI documentation well to be able to do this. And then going to our memory

**[0:10:39]** implementation, the way that it used mem zero referencing uh actually it set it up in a way where you can leverage both the cloud version of me zero and the self-hosted version and then manage that through environment variables. So I saw that come through as I was building it

**[0:10:52]** out when I was looking at it off camera but that's like super cool. I've never actually set that up myself in me zero. Definitely did not tell it to do that which maybe you wouldn't want that. It's kind of a little overkill, but it's still really cool that it understood the

**[0:11:05]** documentation at such a detailed level that is able to have this switch for me to use different versions of Mem Zero depending if I'm hosting it myself or not. Very, very neat. So, again, not going to run this entire agent right now and perfect it, but I just wanted to

**[0:11:20]** show you how well it's able to leverage the new knowledge base that we created for ourselves and we have running completely privately. Like, I'll even show you. I don't know if you caught this when I was in Superbase. I'm running on local host like I have superbase completely self-hosted and

**[0:11:34]** then as I'll get into in a little bit when I talk about the vision that I have for this server. I also want to make it so you can use Olama for the embedding model like you can make it so that this knowledge base that you build up is

**[0:11:44]** entirely private and then you could use you you know local LLM something like R code to make the entire process of coding and leveraging your knowledge base 100% local. So, there's just so many different ways that we could take this MCP server and make it very powerful, private, and flexible. That's

**[0:12:01]** what gets me so pumped up about this. As a quick intermission to our rag MCP server, I want to introduce you to an awesome platform called Lindy. You can think of it like if AI and Zapier had a baby. Plus, they just released a new revolutionary feature called agent

**[0:12:16]** swarms. Take a look at this. So, within Lindy, we have a workflow builder. It's very similar to NAND, but actually has more integrations. We have our trigger and our different actions. Like in this case, I give the workflow a list of leads and it's going to search perplexity for each of them and then

**[0:12:31]** craft a personalized outreach email. And where agents forms comes in that makes this really powerful is we have this loop where what it's going to do is for every single lead that I send it, it's going to create and spin up a dedicated agent running in parallel handling each

**[0:12:45]** of these leads. So, even if we were to send in hundreds of leads to this agent it would still be able to finish in just seconds because everything is running in parallel. Take a look at this. It already spun up a task to handle each of the leads that I gave it. And in just

**[0:12:58]** seconds here, we'll see that it'll finish the Plexity search. And then boom, we start to see these tasks getting finished, creating those personalized emails. Like, I even threw my own name in here so we can see what we would do for a reach out to me. And I

**[0:13:10]** can even send this email to really finish the workflow here for each of the leads that we process. Look at how fast that was because we have a dedicated agent for each of our tasks. Lindy also recently partnered with Pipere to give you more than 5,000 integrations and

**[0:13:25]** they partnered with Appify so you can have more than 4,000 different web scrapers to choose from. So the automation possibilities with Lindy really are limitless. So definitely check them out. I got a link to them in the description below. You even get 400 credits to get started for free with

**[0:13:40]** Lindy, which is definitely enough to see what it's like to have an entire AI agent factory working for you. So, I hope that this crawl for AAI rag MCP server just looks so cool to you. I know that I have had a blast using it already, and just building it out for

**[0:13:54]** you. And you can use this today. Like you can go to the GitHub repository which I'll have a link to in the description of this video. Start using this MCP server for yourself just like I did in the demo that I showed you. And I'm going to keep building this out as

**[0:14:06]** well. I've got a lot of plans for it. So, I want to cover that now and then I'll show you how to get everything up and running at the end of this video too. So, I have a few points that I want to hit on that I have just here in the

**[0:14:17]** vision of the readme. The first big thing with this MCP server, it's kind of a proof of concept for the direction that I want to take Archon. So, Archon is my open- source AI agent builder that you can also hook into AI coding assistance with MCP. And so you give a

**[0:14:36]** direction like I want to build an AI agent that can search the web with brave something like that. And then it has this agentic workflow that runs under the hood to build out the agent using pideantic AI and langraph. But what I want to do with archon is instead of it

**[0:14:50]** being just like an agent builder, I want to turn it into more of a general knowledge engine to power agents and AI coding assistants. I think that's going to help a lot more people, give us a lot more flexibility and also not step on the toes as much as AI coding

**[0:15:05]** assistants. People have their processes for using things like wind surf and cursor already. So they don't really need archon to also be the coder. It can just be more of the knowledge engine. So that's what I'm thinking about kind of changing up with archon. And then this is the proof of concept for that. So

**[0:15:20]** turning archon into a obviously much more robust version of this MCP server. But this is that proof of concept. So that's what I want to build out as a whole. And then also some specific ways that I want to improve this MCP server making it possible for you to use

**[0:15:36]** different embedding models like Gemini or if you want to run everything locally like I've been talking about using Olama for the embedding models. I also want to implement a lot more advanced rag strategy. So right now it's more of a traditional rag lookup whenever it searches the private knowledge base that

**[0:15:52]** we have built out. But we could implement things like contextual retrieval which was released recently by Anthropic or late chunking or a gentic rag like I've covered on my channel. Just giving more ways to have a more robust lookup for all the knowledge that we're going to be scraping and crawling

**[0:16:08]** and providing to our AI coding assistants through this server. And then kind of going along with more advanced rag strategies, we have um better chunking strategies. Right now the strategy that I have in the server after we crawl we have to chunk everything for superbase. I have a decent strategy

**[0:16:25]** where I try to keep all of the paragraphs and sentences together as much as I can but there are a lot better ways to chunk that I want to build out as well. And then the last thing that I have that I want to improve for the server is just better performance. I

**[0:16:38]** mean right now like you saw in the demo it crawls pretty fast even when we have dozens and dozens of pages that we're giving it through something like a sitemap. But we could make it even faster so that there's just even more of a seamless interaction where we're in

**[0:16:51]** our AI coding assistant. We tell it to crawl a couple of things and then we want to code based on that new knowledge. If we can just make that as fast as possible, it'll basically make it feel like we have instant rag no matter the tool or framework that we're

**[0:17:03]** working with. Because if the crawling is fast enough, we don't really think about the fact that under the hood, it actually is crawling hundreds of thousands of tokens and adding that all into our knowledge base. I think that's going to be so cool as well. So that's the general vision that I have. Now I

**[0:17:18]** want to just talk to you kind of how the server works right now and how you can get it up and running yourself. So there is a good amount of logic under the hood to crawl the different types of web pages that we can give our AI coding

**[0:17:28]** assistant. But what we actually surface to our AI IDE is pretty simple. We just have these four tools. We have one to crawl just a single page. So we just give one URL. It'll crawl only that page and then store that in superbase. And then we also have the tool called smart

**[0:17:43]** crawl URL. So you give this a URL. This could be something like a sitemap or llm's.ext or maybe it's a regular web page that it needs to crawl recursively. It'll figure that out, crawl all of those pages that it needs to and then insert those in batches into superbase.

**[0:17:58]** So just to show you really quickly, an example of a regular web page would be like this. Like we could give it a.pidantic.dev and then it would have to crawl this page, then find all the other links in the navigation and recursively scrape all those, insert those into our

**[0:18:12]** knowledge base. Or we have something like the LLM.ext that we saw earlier. This is the one for Lang graph. So we can just scrape this single page that has the entire documentation ready for LLMs. And then yeah, last we saw the sitemap earlier as well. This is the

**[0:18:26]** same sitemap for mezero. A lot of websites have something like this where it just neatly lays out all the different web pages that you would have to visit if you want to get everything available in this documentation or whatever the web page is. And so that's the second tool. Then we have one to get

**[0:18:42]** the available sources. And so like I showed you earlier in superbase part of the metadata is the source for each of those chunks. And so if we want to only search in mem or only search in pideantic AI, we just need to know what that source is. And then we can do that

**[0:18:57]** metadata filter when we perform the rag search. And so this is our way for the AI coding assistant to figure out which sources are currently available in the knowledge base. Like if we were to run this right now, it would tell us that we have mem zero and pideantic AI. And then

**[0:19:13]** for our allimportant rag tool, we get the query from the user like what we're searching in in the knowledge base. The agent will figure out what that query is. And then it can also search within just a single documentation if we want to provide a metadata filter. So it can

**[0:19:27]** do no filter or filter like I said right here. Optional source filtering. This is what does that look to get all that knowledge into our AI coding assistant or AI agent. And I'll show you here in Windinsurf. If I expand my crawl for AI MCP server, we can see each of these

**[0:19:44]** tools that I just showed in the readme. And then we have the descriptions for each of these tools that I have in the MCP server code that tells the AI coding assistant when and how to use each of these tools so it can leverage my MCP server properly. So that is everything

**[0:19:59]** for the tools. How this server works under the hood. And luckily getting started and running this yourself is even easier. So there are only a couple of prerequisites that you need to run this MCP server for yourself. You'll just need either Docker or Python depending on how you want to run the

**[0:20:13]** server. More on that in a little bit. Obviously you'll need Superbase for your database. And this can be hosted locally or in the cloud. And then right now you'll need your OpenAI API key. More support coming later for other providers like Gemini and Olama for local embeddings. So that's it. I've got links

**[0:20:29]** to all these as well to get you up and running. You probably have most of these yourself already. They're very very standard for anything that you're going to be building with AI. And then as far as installation goes, I won't show this step by step on my own computer going

**[0:20:41]** through it with you, but these commands are very very basic. And so first you'll just need to clone the repository whether you're running with Docker or not. And then it's different depending on which way you are running it. So, I'd highly recommend running with Docker it's just less commands overall and more

**[0:20:56]** scalable for your server. But you can also run directly with UV and Python if you don't want to use Docker. But with Docker, when you run this command to build the container, it takes care of everything in a build script to install all of your Python packages, configure

**[0:21:10]** crawl for AI for all of the crawling that it needs to do for you. Takes care of a lot. And so if you do it directly through Python, you have to install UV make sure that's on your system, you have to activate the environment install all the packages, and run this

**[0:21:23]** crawl for AAI setup command that's going to install playright, which is what does the crawling for you. And then some other configuration depending on your operating system. So just a couple of more steps. Docker is definitely easier though. And then once you have all that installed, then we just have to do some

**[0:21:39]** database setup. But I have a SQL script as a part of this repository to make this very very easy for you. So you can just go up in the GitHub and go into this crawl pages.sql. You just copy this content and then you go into your superbase into the SQL editor tab and

**[0:21:55]** then create a new snippet. Paste in all the SQL that we copied from the repo and then go ahead and run that. I'm not going to run it here because I already did, but this is going to create that crawled pages table that we've been working with in our demos. and then also

**[0:22:08]** this match crawled pages function which is used to perform the actual rag lookup in your crawled pages table. So the database setup is very easy there. So let me go back down in the rei where we left off. Once we have the database set up the very last thing you have to do is

**[0:22:24]** configure your environment variables. And so one of the more technical parts to this implementation is I made it possible for you to run the MCP server in either of the transport layers that are possible with MCP, either SSE or standard IO. Don't worry too much about that if you don't know what that means.

**[0:22:43]** Just leave these at the default values generally. Most of the time we'll be running with SSE, which means we'll have a server ready to receive requests from any MCP client. We'll just run it on port 8051. And then you just have to give your OpenAI API key and then your

**[0:22:57]** credentials for Superbase as well. So you'll create this all in AENV file and you can use the env.example file as your guide to get all this set up. Very nice and simple. And then we can move on to the command to execute our MCP server and get it up and running so we can use

**[0:23:12]** it in our AI coding assistance. And so this is the command for Docker and then this is the one for Python. And I'll show you within my Docker desktop after I run that command. I have my crawl for AAI server up and running on port 8051 and I can click into this and view the

**[0:23:27]** logs as well. So as all the crawl requests and the rag lookup requests come in I can see these logs to watch for anything that's going wrong. Obviously in my demos here everything was working perfectly but it's still nice to look at this and see all the requests that are coming in through for

**[0:23:41]** OpenAI and Superbase. And so once you have that up and running now we can hook this into our AI coding assistance. And so for SSSE, which is the default configuration for this server, this is what it's going to look like, the JSON configuration to add into your cursor or windsurf or root

**[0:23:59]** code or client, whatever that is. Um just note for windsurf that you have to use server URL instead of URL just for this JSON key. So I'll show you. Let me open up my Windsurf again and go over here. So to get to the configuration for your M MCP servers, you just have to

**[0:24:15]** click on the hammer icon and then click on configure. That'll open this JSON file. And I just copied what I showed you from the GitHub repo. Put that in here for my configuration for crawl for AAI. Just changing the server URL key to this like I just pointed out that you

**[0:24:29]** have to do for Windsurf. And then the URL for our server is just going to be local host and then the port that we're running the container on, which is 8051. And then you just have to add the slash SSE at the end. That is how you hook it

**[0:24:42]** into this server. So now we have our client windsurf now connected into our server running through Docker. Nice and easy. And so you just have to go ahead and save that. And then you'll click on refresh after you update your configuration. And the setup for something else like cursor or root code

**[0:24:58]** is going to look very very similar. You can just refer to their documentation for how to get that set up. And so then you are good to go. And you can even have this up and running in other things like N8N for example. So I'll even show you this here. I have N8N hosted locally

**[0:25:13]** on my computer right now. And so I can just hook in the MCP client um node like the tool that I can attach to my agent. And then clicking into this, the SSC endpoint is exactly the same as what we set up in Windsurf except because N8N is

**[0:25:28]** hosted in a container, we have to point outside of our container to the host. And so I know that's a little bit more of a technical thing, but I do call it out in the readme here that for Docker users, you have to use host.doccker.in internal instead of localhost if your

**[0:25:44]** client is running in a different container. That does apply to running in N8N. So that's how you hook into it. It's still the same port, still the same/ SSSE endpoint, but we're just referencing our host machine because that is how we call into our MCP server that's running in a different Docker

**[0:25:59]** container. And so with that, I can now open a chat and I can say something like, "What sources are available to me?" And it'll call into this MCP server as a tool. It'll use that third tool that I talked about in the readme to get the sources that are available. And

**[0:26:13]** boom, there we go. Our sources are the pyantic AI docs and the mem docs. Take a look at that. I can even ask it a basic question here like uh what models are supported in Pantic AI. So I can just see it do a request here using that rag

**[0:26:26]** tool. So let me click into this here and see that. Yep, it called the perform rag query tool with the query model supported by panic AI. These are all the chunks that were retrieved. And then going back to the final answer here supports OpenAI, Deepseek, Anthropic blah blah blah. Pantic AI supports a ton

**[0:26:42]** as we know. Yeah, this is the perfect answer. So, we can use it in agents like this. You could have a paidantic AI agent or a crew AI agent, whatever that's using this server just to give instant rag to your agent. So, you're not limited to AI coding assistance

**[0:26:56]** either. I wanted to showcase that really quickly. So that is everything that I have for this crawl for AI MCP server. So check this out today. Use it for yourself and let me know in the comments if you have any suggestions for me for the direction that I should take this

**[0:27:09]** especially as I turn Archon into the backbone for AI coding assistance using something like this MCP server. It's kind of the proof of concept like I was saying. And the other really exciting thing about this server is sure it's very focused on documentation for tools and frameworks right now. I mean, that's

**[0:27:26]** what we saw with context 7 as well. But really, you could use this as the knowledge backbone for any AI agent, for any website. You could take your e-commerce store or your company's Confluence documentation. I could take my Dynamus community and just make an agent that's an expert on that, just

**[0:27:42]** using this server for the knowledge backbone. That's what gets me so excited. And also, if you can really get behind the vision of this and what I'm working on, definitely check out Dynamus.ai. It's a community of AI early adopters that I started recently. We are having a lot of ideas shared between

**[0:28:01]** each other there already. A lot of the inspiration that I've gotten for this and continuing to build on Archon has come from those people. So, if you want to really get involved with some impressive people doing cool things with AI, definitely check out dynamis.ai. But anyway, I hope that you appreciated this

**[0:28:15]** server and this video. If you did, I would really appreciate a like and a subscribe. And with that, I will see you in the next
