---
type: raw-transcript
title: "Ollama + OpenAI's Swarm - EASILY Run AI Agents Locally"
youtube_id: 8jpVeUTNExI
url: https://www.youtube.com/watch?v=8jpVeUTNExI
slug: ollama-openais-swarm-easily-run-ai-agents-locally
published: 2024-10-30
duration: "0:20:05"
fetched_at: 2026-07-21
immutable: true
---

## Transcript

**[0:00:00]** open aai recently released an incredible new experimental tool called swarm which makes it so easy to create a bunch of AI agents that work together to do some really incredible things the problem is you have to use open aai models like GPT 40 by default but what if you want to

**[0:00:18]** use olama to create swarms of Agents all running locally on your machine well that is exactly what I'm going to show you how to do today I took my SQL AI agents that I built in my last video on swarm and I made some really simple changes to make all the agents run

**[0:00:34]** locally with olama which by the way AMA supports function calling in the exact same format as the open AI models I am super excited to show this to you today because function calling in agents they take up a lot of tokens and so using swarm with GPT is definitely not cheap

**[0:00:53]** but with olama it is completely free and in my initial testing I've gotten some really good results even with the smaller model I'll start by walking you through the very simple changes that I made to make swarm work with olama then I'll go step by step through how to

**[0:01:09]** install and run this yourself from scratch so you can get up and running creating AI agent swarms with local llms so let's go ahead and dive right into it so if you haven't seen my other video on Swarm yet I would highly recommend checking that out because I dive deep

**[0:01:24]** into what it looks like to actually create a bunch of AI agents to make a swarm with this tool and so right here and what I'm going to show you now is going to be a more higher level how to integrate with olama to run your agents locally but if you're curious how to

**[0:01:38]** actually use this platform I've got a video on that it is so so easy and they've got great documentation in the repository as well for how to set up these agents and Link them all together they also have this example folder right here so you can see a ton of different

**[0:01:52]** examples for different use cases and how you can build those all with swarm so with that being said I'm going to dive into the ol side of things now so there's this article that was published on July 25th of this year so pretty recently AMA added tool support and the

**[0:02:10]** very important thing that I want to call out here you'll see why I'm referencing this in just a second if I scroll down to the bottom of this article on tool calling you'll see here that they have open AI compatibility and what that means is that I can act like I'm sending

**[0:02:25]** a request to GPT for example but I override the URL that the API goes to to use olama instead of open Ai and it's essentially just with this code right here so you even import the open aai library and you set up the chat completion just like you would when

**[0:02:43]** you're calling GPT and your code but you change the base URL to point2 Local Host Port 11434 where olama is hosted by default on your machine and if you have this set up on a different port or have olama hosted externally on another machine you can change this URL to be whatever it

**[0:03:00]** needs to be to connect to your olama instance it is that simple and so I'm going to tie this together with swarm to show you what exactly we have to change because take a look at this file right here so I'm back in the Swarm repository looking at the source code now and here

**[0:03:17]** you can see where that open AI instance is set up so in the default setup for swarm it instantiates a client with no parameters which means it just looks for your openai API key environment variable for authentication and there's no base URL override so it's just going out to

**[0:03:36]** the open aai API now to change this all we have to do is Implement what they show right here in the AMA documentation it's that simple we just have to change the base URL and then the API key that's it and that is what I'm going to show

**[0:03:50]** you how to do in a little bit here so that we can basically instantiate a swarm we don't even have to change the Swarm code I'm not making a fork or anything we just have to when we instantiate our swarm pass in our client that's going to be an olama client and

**[0:04:06]** that is what I'm going to show you how to do all right so here I am in the SQL AI agent swarm code that I showed in the last video that I made on Swarm and there's just a few simple changes that I'm going to show you now to make it all

**[0:04:18]** work with olama going off of what I just covered and so first of all I want to say that all of this code I'm going to have available in GitHub I'll have a link in the description of the video and so later in this video when I show you

**[0:04:29]** how to get everything up and running you can download it all from GitHub and follow my instructions and have this for yourself really really easily the first thing that I made as a change to this is I added an environment variable file similar to a lot of other tutorials on

**[0:04:42]** my channel and since AMA doesn't need an API key there's no key you have to set here but you can Define the environment variable that determines the model that you are going to use as kind of like your default model for your agents so I love using quen 2.5 coder it's also a 7

**[0:04:59]** billion parameter model it's smaller it's really Nimble it works really really well for this agent here which is generating SQL statements and so it's kind of coding and so I love using that model um for this agent right here and so I pull that model and then down in

**[0:05:14]** the code here again I go into all this code in a lot more detail in my other video I Define the model for each one of my agents and so these ones right here are all using that default model defined in my environment variable but you can also set up your agents to use other

**[0:05:28]** models so my router agent I just want a really really lightweight agent cuz it's not going to make any tool calls besides transferring to other agents so I'm using a 3 billion parameter model so another really cool thing about running this all with oama is you can have all

**[0:05:42]** your agents running on a ton of different models like you can have quen for some or you could use mistol for some of your other agents and you can do that with open AI as well but your options are pretty limited to oh I want to use 40 mini for this agent and then

**[0:05:55]** 40 for this agent but with olama you have dozens and dozens even hundreds of options for models for all your agents which is really really cool and then for the script right here run.py where I actually create my swarm instance this is where I establish the openai instance

**[0:06:14]** where I'm referencing a new base URL and API key just like we saw in that olama blog article when they released tool calling support so I set up my instance like this usually the default in swarm is just like this where there's no parameters supplied so I add in

**[0:06:31]** everything for AMA and then where I instantiate my swarm instance right here this is where I pass in the client and so if you don't give anything at all that's the default setup it just uses open Ai and their API but now I'm using olama that is the only change I have to

**[0:06:48]** do so it's just wherever you use your swarm and set it up with this call you pass in a new client point it to AMA and that is it you are now good to go that is literally the only change we have to do and all this code that you see right

**[0:07:00]** here for running a demo loop I just took this from the open AI swarm repository so they have all this code for you so I just copied into my own version right here and then this is the only change I had to make along with this new client

**[0:07:13]** right here and that is it so now we can go ahead and test this out and actually use our local models for our agents okay so that you know what is actually going on with this testing that I'm about to show with AMA let's quickly go over what

**[0:07:25]** this agent swarm is actually doing so let's say we have an RS SS feed database and RSS feed is just a way to get a bunch of Articles from a new source like the Nidia blog for example we want to store all these articles in a database and maybe we're creating a whole

**[0:07:41]** platform around giving news to users where we have a user table and we have these feeds and all the articles that are linked to these feeds we have this all stored in a database Right Here and Now what we want to do is create a bunch of agents that help us query the

**[0:07:56]** database to get information that we need for Analytics or seeing how many users we have engaging with different articles all that kind of good stuff now the problem is if you have one agent that is operating on this database and has to make all these different types of SQL

**[0:08:11]** queries to get this information it can be overwhelming to the llm so the solution here to make the agent perform better is to split it up into multiple agents so we have this router agent that takes in the initial request from the user and it determines which specialized

**[0:08:28]** agent is going to best be able to create a SQL query a select statement to answer the question for the user and so this router will say oh yeah the user is asking something related to RSS feeds so I'll transfer the request to the RSS feed agent which is going to create that

**[0:08:47]** query in real time to query the RSS feed database get the response back and then answer the user's question or if it's an analytics related question like engagement with these news articles then it will go to the analytics agent which will make an analytics type query maybe joining on a bunch of different tables

**[0:09:06]** and then transferring the request back to the router and answering the question to the user so you can see here that also each of these agents is going to be able to be instructed in a different way and so like one thing I did in my previous video with the RSS feed agent

**[0:09:22]** is I made it um always talk about how excited it is about all the RSS feeds which is just like a silly little example to show that you you can set the behavior for all these different agents so not only are you splitting up these agents into more specialized parts of

**[0:09:37]** this database but you're also able to instruct them on how to answer questions differently because maybe you'd want to answer an analytics question in a much different way than you'd want to answer a question about users on the platform so that is this agent in a nutshell and

**[0:09:51]** that is what we're going to test right now with local models all right in the terminal now all we have to do to spin this up is run the run.py python script and this is going to kick off that swarm instance that's using the AMA base URL and then run in that Loop there where

**[0:10:08]** we're able to infinitely ask questions to our router agent that will direct to one of those specific agents to make that query answer our question based on the data so let's go ahead and run this and this is all using local models I'm using quen 2.5 3B for the router and

**[0:10:24]** then quen 2.5 coder 7B for our agents writing the SQL queries and so we can start off really simple with a query like how many users are on the platform and because this is running locally on my computer and I don't have the beefs machine right now it actually takes a

**[0:10:40]** little bit so let me pause and come back once this is done all right so about 15 seconds later and it routed to the user agent which is great and then it ran this just getting a simple count from the database and then answering my question there are currently five users

**[0:10:55]** on the platform absolutely fantastic so let's go ahead and run another test here all right so what I just did was pretty simple but I wanted to start out with something basic especially because we're using some very small models here let's try to push the limits a little bit more

**[0:11:10]** so again I'm not going to be really really complicated with these queries but I still want to have some sort of query generated with some table joints something that's at least a little bit non-trivial and so now I'm going to say do some analytics for me I want to know

**[0:11:26]** what the most popular RSS feed is so I want it to transfer to my analytics agent now and generate a query that'll actually have to pull data from different tables and combine it together to get a much more intelligent response than just how many users are on the

**[0:11:40]** platform so I'll pause and come back again once that is done all right so about 10 seconds later and we now have our answer so transferred to the analytics agent looking really really good it made a select statement that's a bit more complicated now it has a join

**[0:11:55]** on the feeds View and yeah so it's not as basic as just doing a count star on a single table and it got the right response the most popular RSS feed is ml weekly with six views this is just using a bunch of mock data that I had Cloud

**[0:12:09]** 3.5 Sonic create for me so this is looking absolutely fantastic and these local models are kicking butt like having a 7 billion parameter model that is so tiny compared to GPT but it's still able to do really really well with my SQL agents here and just for your

**[0:12:25]** information I'm running a laptop with a 3060 G CPU and it's able to run these 7 billion and 3 billion parameter models really really quickly if you wanted to try something even bigger like a 32 billion parameter model like code llama for example you'd probably need something larger like a 3080 or 3090

**[0:12:43]** graphics card it all depends on the model you want to use but these smaller models can run like almost any computer like I'm just even using a laptop here and they still work really really well very last thing I want to show you how to run this all yourself from scratch so

**[0:12:56]** you can get up and running with your oama swarm agents and so to get AMA installed all you have to do is go to ama.com and click on this nice big download button this will install for your operating system as well so it works for Mac Linux and windows and all

**[0:13:13]** the instructions that I have here I'll show you how to do everything on the different operating systems when it applies I'm setting this up on Windows but you're going to be able to do this on Linux and Mac as well so go ahead and download AMA and then we'll go on to the

**[0:13:25]** next step all right so now we're going to pull the git repository that I have with all the code the prerequisites here is that you have Python and get installed I don't include that in this walkthrough here because it's super simple you just have to Google both of

**[0:13:39]** those and get those installed on your machine really really easy setup no matter your operating system then what we're going to do is clone my repository here and so it's get clone and then just the URL that we have here for the AI agents Master Class repo where I'm

**[0:13:53]** storing all my code for all my different videos so you're just going to clone that I already have this that's why I get the error here but if you don't you'll clone that and then you just want to change your directory into this local swarm agent folder that has all the code

**[0:14:09]** for the SQL agents that I just showed you running with olama next up what you want to do is create a python or virtual environment this is going to be an isolated place for you to install all the requirements for running this python script specifically and so the way that

**[0:14:23]** you do that is Python dmvnv and then the name of your virtual environment a good default is just a call it venv and so you'll run this command I already have that ran as well so I'm not going to run it but it'll create your virtual environment and then

**[0:14:37]** you can go ahead and activate it to switch your terminal into that specific environment so the python packages will be isolated that will install in a little bit here so using virtual environments is just how you make sure that you can have different projects all using different packages and different

**[0:14:53]** versions for packages so that you don't break one project on your system by updating packages for another keeping an isolated is very very important which is why I'm focusing on it here a super big thing that python beginners miss out on so make sure you do that the next thing

**[0:15:07]** that we want to do is activate this virtual environment on Windows all you have to do is do dot slash and then the name of your virtual environment that you just created scripts and then activate boom there we go so we've now activated our virtual environment you can see here on the Le hand side that it

**[0:15:22]** says we are in the environment now if you are on Linux or Mac the command for this is a little bit different I'll go ahead and copy this and show just what that looks like really quickly it is source and then the name of your environment SL bin activate obviously

**[0:15:36]** this is not going to work on Windows here but that's what you do for Linux and Mac then what we want to do is take the requirements. text file that I have in the repo which tells you all the packages and their versions that you need and we want to install that with

**[0:15:51]** Pip so pip comes default to your python installation it's their package manager kind of like cargo for rust or npm for JavaScript so do pip install - R requirements. text this is going to go through all the packages there and their specific versions so that you're going to have the exact same setup that I have

**[0:16:11]** when I showed everything in this video so that's how you know that everything is going to work exactly the same and so first it's going to install swarm from the open AI get repository and then all of the other dependencies that I already have installed but in your case if you

**[0:16:26]** don't have them installed yet in this virtual environment it'll take a little bit longer longer and that is it so now the next thing that we have to do is go over to our EnV example file so this is another file in the repo just like we have this requirements. text file you're

**[0:16:40]** going to rename this file Tov and then set the olama model that you want to use so going back to AMA let me show you really quickly how we can actually pull these models now that we have Ama installed so I'm going back to my browser here and I'm going to show you

**[0:16:56]** this page right here so if you go to and I'll have a link to this in the descript deson as well if you go to ama.com search and you go to the tools tab right here it is going to show you all of the models that you can install with olama

**[0:17:11]** that support tool calling you need this for swarm because if you have a model that doesn't support tool calling it's not going to be able to actually act as an agent and invoke the tools that you have set up in your swarm code so you need specifically a model that has the

**[0:17:25]** tool label here that is really really important so for example quen 2.5 is one of my favorites in fact I think it actually performs even better than llama 3.2 and 3.1 so you click into the one that you want and then you select the number of parameters that you want so if

**[0:17:42]** you have a weaker computer um you might want to use like 7 billion or below if you have something really really powerful like double 3090 uh GPU setup you could use like you know 32 or 72 billion parameters so you select the one that you want and then after you select

**[0:17:57]** it you can copy this ID right here so actually let me just copy this right here so I don't want to run it I just want to pull it so let me copy this ID right here and then going back into the terminal what I can do is I can say AMA

**[0:18:11]** pull and then quen 2.53 B so in my case I already have this installed and so that's why this worked like instantaneously but if you don't have it installed already it'll take a while to pull these models because they're actually all multiple gigabytes even the three billion parameter ones and so you

**[0:18:28]** have the model now and you are good to go so what we can do is go back to your code here and then that same ID that you use to pull the model with olama you put that in here for the llm model so that will now be the default olama model that

**[0:18:42]** these agents use within swarm and then also like I showed earlier if you want to pull other models and set them here U manually for the agents that you create you can do that and that is how I was able to use the default model for some of these agents and then for the router

**[0:18:55]** I had hardcoded here to use quen 2.53 you could also if you want to set up multiple environment variables like you could say router llm and then the agent llm you could set this up however you want this is just an example here but that is how you pull the old llama

**[0:19:09]** models and use them within the Swarm here and that is everything make sure you rename this and then you can go through the exact same process I did with my demo where I ran the run.py script and I tested out my agents and everything was working really really

**[0:19:24]** well the future of local llms is looking really bright and I find it incredible that you're able to do this kind of thing with even smaller models running on your computer now you're still going to get better performance with GPT compared to a model like Quin I'm not

**[0:19:39]** going to sugarcoat that but the gap between open source and the massive close Source models is diminishing really really quickly it's super exciting stuff and I hope that you had a blast playing around with AI agents with swarm running locally just like I did if you appreciated this content and you're

**[0:19:56]** looking forward to more local AI content I would really appreciate a like and a subscribe and with that I will see you in the next video
