---
type: raw-transcript
title: "Build an ARMY of AI Agents on Autopilot with Archon, Here's How"
youtube_id: -Fpp4CBo14g
url: https://www.youtube.com/watch?v=-Fpp4CBo14g
slug: build-an-army-of-ai-agents-on-autopilot-with-archon-heres-how
published: 2025-04-02
duration: "0:19:46"
fetched_at: 2026-07-21
immutable: true
---

## Transcript

**[0:00:00]** archon is the first of its kind it's an open- source AI agent that builds other AI agents and I used it to create something pretty insane that I'm going to show you right now i'm calling Archon the world's first agent here cuz I really haven't seen anything like it

**[0:00:15]** before it builds AI agents with pure code so you're not tied to a specific platform and it uses advanced agentic techniques under the hood when it's building these agents on the fly so you get much better results compared to the generalist AI coding assistants i have been working constantly on Archon the

**[0:00:33]** last couple of months and not only is it shaping up to be an incredible AI agent builder for you to use and learn from but I have already made a bunch of impressive agents with it and there's one in particular that I cannot wait to showcase to you right now because I used

**[0:00:47]** Archon to build an AI agent army it's a bunch of specialized sub agents that are each leveraging an MCP server so that my primary agent can be connected to a bunch of different services super easily it's the beginning of the ultimate personal assistant and the best part is

**[0:01:04]** I didn't even have to code it myself so it really shows the power of Archon and even this agent is worthy of its own video so allow me to show you this AI agent army which you can use right now and then as a bonus I'll show you how I

**[0:01:17]** was able to build it with Archon really exciting stuff so let's dive right into it so here is the GitHub repo for Archon which I'll link to in the description of this video archon is the mastermind behind everything that I'm about to show you and I use it to build all of my AI

**[0:01:32]** agents now because it is the AI agent that builds other agents or an agenteer as I like to call it and there are two reasons why I'm building this as a completely free and open- source tool for you the first one is that I'm doing what they call build in public where I

**[0:01:48]** build archon in iterations sharing my journey with you as I build this powerful tool so it's not like archon is this productionready thing right now it's experimental i'm still working on it but you get to come alongside the journey with me and even contribute if you want and then the other reason is

**[0:02:03]** it's an educational framework i'm using Archon as a way to teach you more advanced agentic concepts using my favorite Python AI frameworks like Pyantic AI and Langraph so that's Archon as a whole and there's instructions for installing and running this yourself in this readme if you want to use it for

**[0:02:21]** yourself but right now what I want to do is share with you the AI agent army that I built with MCP servers that I built with Archon we'll play around with it and then later I'll dive more into Archon and the future changes that I have for it and as I already alluded to

**[0:02:36]** I've already built a lot of impressive AI agents with Archon so I've got this folder with all of the best agents that I've been working on right now we're going to focus on the MCP agent army and by the way if you're curious about how I built any of these other agents if any

**[0:02:50]** of these names peique your interest check out dynamis.ai it's an exclusive community that I'm starting the wait list, is, open, for, it, now, and, I'm, going to be having a lot of live sessions these workshops where I'll go into how I built all of these agents so you can use them

**[0:03:04]** for yourself but anyway right now we're going to, be, focusing, on, the, MCP, agent army so I've got this open let's bring this into an IDE i'll show you the code really quick and then we'll see how powerful it is so all of the code that you're looking at right here I did not

**[0:03:18]** write myself i used archon to make everything and I did have to iterate a few times as you usually have to do with AI coding assistance but it's just awesome that after just a few tries this is all working and I didn't have to code it at all and so I have this GitHub repo

**[0:03:34]** available for you to download just like Archon if you want to run this yourself hook in your own MCP servers i'll show you how to do that later as well i even have the original prompt that I used to kick off the build with Archon then a read me with instructions on how to set

**[0:03:49]** up everything yourself and I cover why we're doing it this way anyway because the first big question is why set up specialized agents why not just give all of these MCP tools to a single agent and the reason for that is specialized agents are powerful because LLMs get

**[0:04:06]** overwhelmed very quickly if you give them too many tools because every single tool is just increasing the length of the prompt to the LLM and so if you split up the burden of the different tools between different specialized agents that means all your prompts are smaller the LLMs are going to get

**[0:04:23]** overwhelmed less and you just have to have one primary agent that can dish out the requests depending on which MCP server needs to be used and so if you ask it to search the web the primary agent will be like "Oh yeah I need to use the Brave MCP server." So it'll just

**[0:04:37]** call the Brave sub agent that will then figure out which tool to use in the Brave MCP server so I hope that makes sense i'll cover in a little bit exactly how everything is set up here but first I want to show you how powerful this is really quick so I have a version of this

**[0:04:52]** which I turned into an API endpoint you can see right here in the studio integration version folder so I've got this running in the terminal as an API endpoint and I have that hooked into my agent zero application which I've covered on my channel previously it's a way for you to connect any local agent

**[0:05:07]** into a front end so we have full chat and conversation history and so right off the bat I can ask it a simple question that will use one of our sub aents so I can say what GitHub repos do I have and then usually it asks for my

**[0:05:20]** GitHub username so I'll say my username is colam0000 so I'll send in this request go back over to my terminal and you can see that it decides to call the GitHub agent with the query list all repositories for the username colam0000 and so it'll take a little bit to make

**[0:05:36]** that request and come back with all my repos so I'll come back once that is done and boom there we go all of my GitHub repos listed we've got Archon the AI agents masterclass automator agents local AI package i don't want to keep scrolling because it lists my private

**[0:05:50]** repos as well but yeah this is working great the primary agent new to route the request to the GitHub sub agent that uses all the tools from the GitHub MCP server and so now I'm going to go ahead and start a new conversation let's ask it something a lot more complex that

**[0:06:05]** will force it to use multiple specialized agents within one request because I want it to search the web for top AI agent frameworks and then what I wanted to do is go into the frameworks table that I have in my AI research base and add each of these with a source

**[0:06:21]** where it found that information from the search, as, well, so, I'm, going to, go, ahead and send in this request and the first thing that it'll do is it'll send a request to Brave there we go top AI agent frameworks for 2025 and so I'll let that run and then after we'll want

**[0:06:35]** it to call into the Air Table sub agent and yep there we go we got a result we got Langchain OpenAI Swarm i don't know if I agree with all of these in this list but yeah it searched the web for me it did what it was supposed to do and I

**[0:06:47]** could be more specific if I wanted to do a deeper search as well obviously and so now it's calling the Air Table agent to list all the entries that are available in the framework table so first it wants to decide what's here already which it's going to, get, nothing, back, and, then, it'll

**[0:07:02]** end up calling for each of those 10 records to add them in for these frameworks and so I'll pause and come back once it has completed that request in full and there we go it added all the records to Air Table we can see the calls to the sub agent in the terminal

**[0:07:15]** and going into Air Table itself we've got these 10 records it's missing Pantic AI so not the perfect list but I mean it's all opinion anyway it did a good job researching that for me and so now I can ask it to continue i can have it use

**[0:07:28]** yet another specialized agent to continue the conversation because I can say "Okay great now get the exact URL for the Air Table base for AI research and send a link to that in the research channel, in, Slack.", All right, so, now continuing the conversation it has to pick up where it left off get that link

**[0:07:51]** using the Air Table sub agent unless it fetched it already in a tool and then send me that message in Slack right here so let's see if it can do that so I'm going to, give, it, a, little, bit, of, time it's thinking about it see let's actually see the terminal here um yep

**[0:08:04]** all right, calling, Air, Table, and, calling the, Slack, agent, all right, so, let's, go into Slack and there we go yep we got our table and I can open this link and boom we're in we got our list up in a new tab here so this is working perfect

**[0:08:15]** it's using all these different sub aents in tandem to do some really neat things kind of like a personal assistant would do for us the sponsor of today's video is Vectorize and I'm excited to bring them to you today because they're solving a huge painoint for AI solutions

**[0:08:28]** cuz here's the thing most AI agents rely on rag to bring external knowledge into the fold so they have access to your documents but the hardest part about implementing rag is just processing your data getting your documents in something like Google Drive formatted in the way where you can store it in your vector

**[0:08:46]** database something like Superbase or Pine Cone this data processing is called a rag pipeline and you've seen these before in N8 workflows custom code it's always complicated especially when you have to work with a bunch of different file types but look at how simple this is in Vectoriz in just four steps we

**[0:09:03]** create a full rag pipeline that's going to be constantly waiting for files that are updated or created within all these different sources that you can select here and then we have a step to extract the text a step to embed it to prep it for the vector database and then finally

**[0:09:16]** the step to insert it and this supports a bunch of different vector databases as well like Pine Cone Weevate Superbase they're all available to you it's so easy to configure this in just minutes plus they have this rag sandbox where you can chat with an AI agent using this

**[0:09:31]** knowledge base like I did right here got the current version of Archon perfectly you can connect this with an API to N8N or your custom Python agents there's so much control that you have with this bringing it into your own projects and the other thing I want to show you

**[0:09:45]** really quick is you can upload your documents and it'll recommend the configurations for your rag pipeline based on automated testing it does so it really just takes your rag pipelines to the next level so I'll have a link in the description to Vectorize i definitely recommend checking them out

**[0:10:01]** if you want to take all of the unknowns out of ingesting your data for rag so I hope that that quickly showed you how powerful this MCP AI agent army is and now I want to show you how I built it with Archon how everything's set up and

**[0:10:16]** also how you can extend this to add any MCP server that you want because this really can be a template for your personal assistant you can use MCP to connect to any of your different services and having this specialized agent setup means that you can add 10 12

**[0:10:30]** 15 20 MCP servers and you're not going to overwhelm your system and so the way that this is all set up is using the new MCP integration that my favorite AI agent framework Pyantic AI released recently so they have details on this in their documentation which I'll link to

**[0:10:48]** in the description of this video this is what I fed into Archon because Archon ingests all the documentation for Pyanki AI so I use this to understand how to build what I'm about to show you because with this new integration it is this easy to set up an MCP server connection

**[0:11:04]** that you can use in your Pantic AI agents and so the config will look very similar to your config with something like Cloud Desktop or Windsurf or Cursor as well so we set up all the servers like Brave and Air Table we have the file system access access to GitHub to

**[0:11:21]** Slack like we saw earlier and then also firecrawl to scrape individual pages and then we just create an agent for each of these so we have our air table agent where we just give it the model we want to use i'm actually using GPT4 mini in this case and so with that demo that you

**[0:11:35]** just saw it wasn't even that powerful of an LLM it was still able to do things really well and then we have our system prompt and then this new parameter that Pantic AI released where we can pass in a list of MCP servers that we want to connect for the tools for the agent and

**[0:11:49]** so in this case for each of these sub agents we're just giving it a single tool so that it's specialized for using that MCP server and then for our primary agent again we just give it the model and then the system prompt and then we have a tool defined for each of the sub

**[0:12:06]** aents that it can call into and so it uses this dock string to understand when and how to use each of the sub aents and so if we have a request that goes in for it to search the web it'll be like oh yeah okay I should use the Brave MCP

**[0:12:22]** server through that sub aent and so it'll pass on the request to be handled by the Brave agent specifically and so having all the sub aents handle the individual tools in the MCP server releases that burden from the primary agent so now it only has to worry about

**[0:12:38]** which agent to call on not which specific tool so instead of having to pick from 30 different tools it only has to pick from six different agents you can see how that releases the burden decreases the size of the prompts overall and this is all using pretty basic pideantic AI code and so take this

**[0:12:57]** for yourself and set this up for whatever MCP servers you want because you can just go to the configuration guide for any MCP server in GitHub or wherever you find that server and you can just copy that to set up that config here so you define the server you define

**[0:13:12]** a sub agent and then you just have to define a tool for the primary agent to use that sub aent that is all it takes for you to hook in any sub agent that you want and of course Archon can help you with that as well you could give

**[0:13:24]** this as a starting point to Archon like just copy this code paste it into Archon and say "Hey I want you to now add the Quadrant MCP server for example for Rag." And I even have the prompt available in this GitHub repo this shows you the exact prompt I use to kick off

**[0:13:41]** the AI agent process with Archon so you can take this prompt you can copy it and you can set up Archon just following the instructions in the readme and then you can dump it right away in the chat or you can set this up as an MCP server to

**[0:13:53]** use in an AI IDE like Windsurf or Cursor and have it create the code for you that way too and so I already have this conversation up it's just an old one that I want to show you because it did a good job even after the first request it

**[0:14:06]** didn't quite oneshot this whole setup as I said earlier but it still had a really amazing starting point and so yeah this is the same prompt that I had in that text file and then this is what it produced after the first try where it sets up all of these MCP servers it

**[0:14:21]** doesn't have the command quite right for each of these MCP servers that's one of the things that I had to correct but it had a really good starting point hooking in all these individual agents with the different environment variables for all the MCP servers it got that part right

**[0:14:34]** and then it created the primary agent that has a dependency for each of its sub agents so yeah working really really well and so yeah it defines the tools for each of the sub agents to call into pretty much what we saw in the Python script that I showed you earlier but we

**[0:14:49]** just had to refine it through a couple of iterations and so that's what I did throughout this conversation i mean it got kind of long but yeah it didn't take that long overall and this kind of thing is not super easy to set up in a generalist AI IDE like if you were to

**[0:15:03]** try this exact same thing in Windsurf or Cursor you would not get nearly as good of results because just the way that Archon is able to work with the documentation for Padantic AI and refine itself there's a whole agentic flow under the hood that I'll show you in a

**[0:15:18]** second here that makes it possible to produce something like this that isn't going to be perfect right away but it felt pretty close this time and so I've just had a blast building things with Archon especially this AI agent army this is just something that I feel like

**[0:15:32]** is a really good template to take going forward whenever you want to connect MCP servers to your custom AI agents so back over to Archon to finish things off cuz I want to show you how I built Archon in a way where it could build that MCP AI

**[0:15:47]** agent army and I want to share some upcoming features for Archon that are super exciting too so the first thing is I implemented version six for Archon recently which is a tool library and MCP integration and so now we have all of these pre-built tools examples and MCP

**[0:16:05]** servers that are all within this agent resources folder and I have this new agent in the whole process for Archon that based on the user's request it'll actually pick different examples to give to the primary coder so it'll say like oh yeah I need to develop an MCP agent

**[0:16:20]** well let me look at this example and I'll figure out based on this along with the podantic AI documentation how to make that happen and then we also have the MCPS folder which gives the config for a lot of different servers like the ones we were using for our AI agent army

**[0:16:35]** and I definitely want to add a lot more later as well but yeah in each of these JSON files we have the config for that MCP server so Archon will take this and figure out how to format it for what we need for Pyantic AI for that integration

**[0:16:49]** and then we also have pre-built tools as well so that if we don't want to use MCP servers if you want something faster or if we just want custom tools that aren't in MCP servers then we can implement the tools right like this as functions just kind of the classic way to build tools

**[0:17:04]** for our agents and so those are all the resources now and I want to keep adding more and more it's kind of just a version one list of resources and MCP servers but if I scroll all the way down to the graph for Archon we have this new

**[0:17:17]** agent added this is the advisor so this is what intelligently picks the examples pre-built tools and MCP servers and it feeds that into the primary coder agent and that all depends on exactly what the user is asking for and so we have quite a few agents now in this whole process

**[0:17:33]** for Archon like it's it's starting to get pretty robust and I'm able to build things with it that I never could have or, at least, would, have, taken, many, more prompts with something like Windsor Cursor so I'm having a blast with Archon and I've got a lot of other plans for it

**[0:17:48]** as well that are coming up soon here so you can check out this GitHub repo if you want to go through future iterations of Archon things that I got coming up one big thing is including the Langraph documentation as well as Pyantic AI there's already a pull request out for

**[0:18:00]** this that I just needed to review um they did an awesome job so I'm just working on finishing up reviewing that but then Archon will be able to build with both Pantic AI and Langraph so really start to build sophisticated AI agents i can't wait for that and then

**[0:18:14]** one other one I want to call out really quick i don't want to cover all of these right now but another one that'll be super cool is version 9 which this will mean that Archon can literally not just build the agent but actually spin up an isolated environment like create a

**[0:18:27]** database and stuff and run the agent and figure out okay is it working are there any errors is it giving good results and then take all of that and then autonomously refine the agent so just taking that uh self feedback loop to the next level actually running the agent so

**[0:18:42]** so many awesome things that I've got in store for Archon i hope that this can just be an awesome tool for you to build your agents learn more advanced agentic systems cuz it is an educational framework as well like I said earlier so yeah I hope that you just have a blast

**[0:18:56]** with this like I have been having and of course let me know in the comments if you have any questions at all i'm always open to answering anything you're curious about so I hope that this video clearly showed you the power and potential of Archon with an AI agent

**[0:19:09]** that you can use right now and tweak to your own needs i mean you can basically connect any MCP server that you want to this AI agent army also I have a lot more coming up for Archon with more content and more features so stay tuned for that and check out the GitHub page

**[0:19:25]** as well which I'll link to in the description if you want to see my vision and the upcoming features I want to implement and I'd also very much appreciate a star on the GitHub repo as well it means a lot to me so if you appreciated this content and you're

**[0:19:37]** looking forward to more things Archon and AI agents I would really appreciate a like and a subscribe and with that I'll see you in the next
