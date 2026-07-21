---
type: raw-transcript
title: "OpenAI's Swarm - a GAME CHANGER for AI Agents"
youtube_id: q7_5eCmu0MY
url: https://www.youtube.com/watch?v=q7_5eCmu0MY
slug: openais-swarm-a-game-changer-for-ai-agents
published: 2024-10-16
duration: "0:20:49"
fetched_at: 2026-07-21
immutable: true
---

## Transcript

**[0:00:00]** open aai recently revealed their latest and greatest AI tool swarm swarm is an open- Source AI agent orchestration tool that allows you to write super clean and simple python code to build AI agents and seamlessly connect them together to do some really mind-blowing stuff I absolutely love this framework because

**[0:00:19]** we are heading towards a future where AI agents run everything and there is definitely a need for tools like this to help connect these AI agents together and later in this video I'll show you an awesome example as to why that is now this framework is experimental and its

**[0:00:36]** main purpose is educational but it certainly does a good job teaching bulletproof architecture for AI agent orchestration setting up an AI agent with something like Lang chain or n8n is honestly pretty straightforward and there's a lot of content on my channel to help you with that everything from

**[0:00:52]** hooking in the llm the prompting the tools for function calling all that good stuff is pretty easy to set up but what really starts to get tricky is when you have a whole swarm of agents that you have to connect together in very specific ways for your use case and that

**[0:01:07]** is where swarm comes in both as a tool for us to use and learn from so today I'll show you how swarm works and we'll build a really awesome and practical swarm together to manage a SQL database I'm talking AI agents that can extract insights from your data with SQL queries

**[0:01:23]** create and manage your tables and clean your data all that good stuff and I'm really excited to show you this example swarm specifically because when you have a massive SQL database for your business with a lot of different tables and data you oftentimes need a bunch of different

**[0:01:39]** agents that specialize in different areas of your database and that is exactly what I'm going to show you how to build with this new framework so without further Ado let's dive in so here we are in the GitHub repository for swarm by open aai and as you can see

**[0:01:53]** this library is completely open source they have all the code available to you so you could even Fork swarm if you wanted to change it and do things like run your own fine tune llms in your swarms there's so much you can do because you have all the code available

**[0:02:06]** to you and along with that they have really extensive documentation and the readme here for the root of this repo so you can see how to install it they have really good examples and they also overview everything that they are teaching here as a part of this more

**[0:02:20]** experimental and educational framework um so yeah a lot of overview here extensive documentation examples for what you can do and set up with swarm it is just amazing and on top of that if I scroll back up to the top here you can see that the initial commit was 5 days

**[0:02:36]** ago so swarm is brand spanking new open AI is just pushing out awesome new tools for us to use and I really appreciate that it is all open source as well and there are so many powerful things you can build with swarm so what I'm going to show you now with an AI agent swarm

**[0:02:51]** to manage a SQL database is just one example but it's a really cool one so I'm excited to dive into this with you and show you what swarm can do with a specific example and before we do that really quick I just want to talk a little bit about what swarm actually

**[0:03:04]** teaches us because the goal here again it's not to be a production piece of software a library that you could actually use in production to run Enterprise grade applications it's more to teach you something and specifically what it teaches you is it showcases the handoff and routine patterns that are

**[0:03:22]** explored in this cookbook right here that I would highly suggest that you go through because these are the kind of Concepts that relate to building a really robust and reliable AI agent architecture and so yeah this Library if you actually look into the source code you're going to learn a ton so even if

**[0:03:42]** you don't use swarm to build something that is production ready you can learn from it and it is so good as a tool for that so let's go ahead and actually dive into my use case specifically creating a swarm to manage a SQL database so now I get to show you this really neat diagram

**[0:03:58]** that I made here to show you what I'm going to be building with swarm but first of all let me address the question what is the point of this what's the point of building what I'm about to show you or using swarm at all now think about it this way let me break it down

**[0:04:11]** for you very simply if you have an AI agent that is just running by itself you're going to be very limited into what you can actually get this agent to do for you because the more functions that you give it or the more instructions that you give it to do

**[0:04:26]** different things the more you are going to overwhelm the llm just because the llm can handle a certain amount of context doesn't mean that you should try to feed it that much because you're going to run into the needle the H stack problem where the specific part of the

**[0:04:41]** instructions or that specific function that you needed to invoke is going to miss or mess up because there's just so much given to it at once and so the solution to that is to actually have multiple agents that are working together tackling different parts of the problem or handling different parts of

**[0:04:58]** the system like in what I have built right here here so essentially what I've built here is a bunch of AI agents that work together to answer a very wide range of questions that a user could have about data in an RSS feed database if you don't know an RSS feed is just

**[0:05:13]** say way for a new source like the Nvidia blog for example to push out a bunch of news as it is being released each day and so this is a really good way actually something I'll probably make a video on later in my channel to keep up with all of the AI news that's happening

**[0:05:27]** every day because you can have a database that collects news articles from all these different sources and you can imagine that this database will get really big so we have a bunch of different sources a bunch of different articles maybe this is a platform so we'll have users and user sessions as

**[0:05:42]** well and so there's a lot of data here so if we have just one agent that's supposed to be able to write queries to extract all this different kind of information and respond to the user in specific ways based on the data it can get very overwhelming and so when a user

**[0:05:57]** question comes in uh maybe like how many likees does this category of posts have on average or maybe something like how many RSS feeds have had an article published in the last day we have these different types of questions but they first all go to this router agent and

**[0:06:12]** this agent has context around which one of these sub agents would be best to handle the specific user request so each one of these agents specializes in handling different parts of data within our RSS feed database so the correct agent is an invoke to answer the user question and this is also where we can

**[0:06:32]** tell these different agents how to respond differently and I'll show that in my example as well so we can have each of these agents that are specialized in different areas and have Specific Instructions and how to write these queries and respond to the user so it gives us a lot of robustness and

**[0:06:48]** flexibility and so what I'm going to walk you through with swarm is how we can set up exactly this diagram and it's literally going to be less than 100 lines of python code it is so so easy to do now the other thing I will say before I dive into the code here is that

**[0:07:03]** sometimes you don't want to build this kind of thing yourself there are platforms out there that have this kind of functionality for you where you can use natural language to talk to and manage your SQL databases and so that actually brings me to the sponsor for this video because there is a time and

**[0:07:19]** place for you to just use something that's already out there and not build it for yourself and that is where chat to DB comes in chat to DB is an incredibly powerful and easy to use platform platform for you to leverage AI to manage your databases it is open

**[0:07:34]** source but they also have a cloud offering for you to get up and running in just to minutes and you can connect practically any SQL database to their platform or create a new one and leverage their llm to improve your SQL queries write SQL with natural language to gain insights from your data create

**[0:07:51]** and manage your tables and that is just covering the basics I'm in the chat to DBU now and you can see here that I have the exact same tables in mock data loaded that I'm using for the custom example in my video and it is so so easy

**[0:08:03]** to prompt the llm with natural language here to generate SQL queries that give me practical business insights it works so so well I will have a link below in the description to chat to DB I would definitely recommend checking it out I picked them out for a collab for a

**[0:08:19]** reason their platform just works so well for managing your SQL databases all right let's Dive Right into this I am so excited to show you how I use swarm to create really easily a bunch of agents to manage a SQL database now the first thing I'll say is that I have a link in

**[0:08:35]** the description of this video to All of the code that I'm going to show and create right now and so you can download that and you can immediately run this entire thing without even having a SQL database because I'm using SQL light here and I also have some SQL scripts to

**[0:08:50]** create all the tables and some mock data as well so you can run what I'm about to show you here with this load SQL data script to load up a full SQL light database with tables and mock data to play around with the Swarm agents right away the only thing that you have to set

**[0:09:06]** up externally is you need to go to the openai website and get your API key I'll have instructions for that in the description as well so once you have your API key you'll just have to create an environment variable for it on your system called open aore aior key with

**[0:09:22]** that out of the way there's also requirements. text file if you want to install all the python packages you need for swarm here including Swarm at s and then you'll be good to go so the first thing that we're going to do is actually set up a database so that we can have

**[0:09:37]** something for our agents to query so that we can give natural language ask a question and it'll query the database fetch the results and then answer our question based on that data so first of all I actually use cloud believe it or not to generate the SQL scripts to give

**[0:09:53]** me all the tables that I need for an rssv database and then some mock data as well so really quickly like for example example we have a table for the sources that RSS feeds themselves the categories the different news articles that will be linked to their feeds and then the

**[0:10:10]** categories for the items and then things for users and their preferences and user sessions so all that good stuff as well and then we have mock data that I've created again using Claud for each one of these tables really really nice and simple and then this python script right

**[0:10:25]** here this isn't what I'm going to be focusing on so I'm just going to uh cover this very quickly it's going to take in both of these scripts right here and it's going to execute each of the commands one at a time so that by the time the script is run we will have a

**[0:10:39]** full sqlite database with all the tables created and all of the mock data ready for our agents to query all right I have got a completely blank python script here because we're going to walk through step by step how to create this AI agent setup with swarm to manage our SQL

**[0:10:55]** database and I'm going to go pretty quick but you're still going to get a good understanding how everything works together with this setup here so the first thing that I want to do is import all of the packages that we need and believe it or not this is literally it

**[0:11:08]** we just need swarm and SQL light 3 for everything that we are doing here and so then the first actual code that I'll write here is going to be to create that connection to our sqlite database that we created in the last step when we ran our load SQL data script and then what

**[0:11:23]** we have to do after that is we want to load in our SQL script for creating all of our tables and the the reason we want to do that is because we're going to give all of these statements to our AI agents so they understand our tables and

**[0:11:38]** their schemas and can create scripts for us to extract data to answer questions that we give with natural language so this is the ticket for the agents to really understand our structure is all of these things right here we're going to give in as a part of the instruction

**[0:11:53]** prompt to those agents next up I'm going to create the first tool here this is going to be the tool for for an agent to invoke to make a select statement in our database and so the agent just needs to pass in that full select statement it wants to make and then we are going to

**[0:12:09]** run it for the agent and this doc string that we have right here this is actually given into the agent prompt so it understands when and how to use this function and this function is very very simple all we're going to do is query the database with the SQL statement that

**[0:12:26]** the agent generated itself if there are no records tell the agent that is the case so it can report it back to the user otherwise we're going to in a very nice format create a string representing all the data that we just fetched so we can give it back to the agent to report

**[0:12:41]** on to the user so we're going to get the column names calculate some width here because we're going to make a nice and formatted string so we could also print this out to the terminal for our debugging and then we're going to get the results together add the header at

**[0:12:54]** the top and then add the rows one at a time and then that is what we return to the agent so at this point we've made the select query in the database formatted it very nicely as a string to then give back to the agent so that it

**[0:13:07]** can reason about it and answer our question next up what we want to do is we want to create functions here that are going to create the instructions for our agents now these are going to be very very basic but you could extend these to maybe fetch instructions from a

**[0:13:24]** database or maybe you have something a bit more dynamic in this case we're just going to have hard-coded strings here for the the instructions for our agents now there are a lot of ways to extend this you could add more functions here to run insert statements or run

**[0:13:38]** statements to create tables that's how you can extend this to really fully manage a SQL database but I'm keeping things really simple here I'm going to keep this as a setup just to make select statements on the database and I'm going to have very simple prompts here but

**[0:13:51]** hopefully you can see how you could extend this very easily to have more Dynamic prompts have more tools all that will be made very clear when we go through this script as a whole and so for our router here we're just telling it that you're an orchestrator of different AI agents for SQL experts

**[0:14:06]** and your job is to determine based on a user query which agent you send the request to again going back to the diagram that I went over earlier and then we also want to Define our instructions for our agents that will actually make SQL queries so this is

**[0:14:21]** where we tell the agent that you are a SQL expert who takes in a request from the user for information and you generate a SQL statement that will be able to get the information that you need to answer the user's question that they put in in natural language and this

**[0:14:34]** is also where we feed in the table schemas so now it has all the information that it needs to know to make the select statements to actually get that data from the database now we're going to use this prompt for every single one of the agents even though

**[0:14:47]** they're all operating on different parts of the database but we could easily again extend this so that you would have a very different prompt for each agent to tell it how to operate on different parts of the database next up we're we're going to do is create our very first agent it is so

**[0:15:03]** easy to do this with swarm you just use this agent object right here you given a name and then you pass in the instructions so in this case we're just calling this function here to get the instructions for our router and then we'll just do the same thing for the

**[0:15:16]** other agents as well we have our RSS feed agent which is going to specialize in fetching data around RSS feeds and then we give it the instructions so it understands the schemas and then we also tell it help the user with data related RSS feeds and then I include something

**[0:15:30]** kind of random and silly here but this is where you specify how you want the behavior for this agent specifically to be different so I say be super enthusiastic about how many great RSS feeds there are in every one of your responses and we'll see this come out

**[0:15:44]** when we play around with these agents and this is how we'll know like oh yeah this response is definitely coming from the RSS feed agent and then we also have another parameter here for functions where we give it the Run SQL select statement function and so this is how

**[0:15:59]** it's going to have access to that to be able to call this to actually interact with our database and then the setup for the user agent and the analytics agent is going to look very very similar again with just slightly different instructions at the end here that we

**[0:16:14]** appended onto that primary set of instructions we get from this function call right here and all of these have the ability to run a SQL select statement so again these aren't super customized to what they're actually specialized in because this is just a simple example but you can see how you

**[0:16:28]** could give different functions of these agents have very different instructions instead of keeping everything mostly standard very very robust a lot of possibilities here next up what we want to do is Define our transfer functions so again going back to the diagram we have our router agent that will transfer

**[0:16:46]** the requests to different agents that specialize in certain areas of the database and then also those agents need to be able to route back to the router so that the query could then go onto a different agent and so we have our first function right here that is going to be

**[0:17:01]** for our agents to route back to the router and then we have a set of functions right here that is going to be how our router will route to the different experts and so you'll see how this all plays in together because first of all we're going to add onto our SQL

**[0:17:17]** router a list of functions which is each of those transfers so now it's going to be able to go to each of the AI experts and then for our AI SQL experts each of these agents we're going to append a function to transfer back to the router and that is literally it we have now

**[0:17:35]** fully built out our agent workflow exactly like I have in the diagram and there is nothing missing here the only other thing we need to do is create this run.py script and this is it it's just five lines of code because we can use this run demo Loop provided by the Swarm

**[0:17:51]** Library which is essentially going to create a chat in our terminal where we can interact with our agents and that is exactly what we're going to do right now to test it out okay let's test this out now so I'm in my terminal and to run this swarm agent all I have to do is run

**[0:18:05]** the command Python run. and it will immediately ask us for our first prompt where we say how many users do we have on the platform and this should route to the user agent right now and yep sure enough it did so transferred to the user agent and then it ran the Run SQL select

**[0:18:22]** statement function with this select count Star as user count from users and then we got back the answer we currently have five users on the platform this is looking perfect and so now I'll go ahead and route back to the router agent you could also handle this automatically

**[0:18:38]** behind the scenes and update the code for that I'm just doing this manually for now but yes I am back to the router agent and so now I can ask another question that would maybe route to the RSS feed agent so I'll say how many RSS feeds do we have in total and so now it

**[0:18:53]** should route to the RSS feed agent we should get quite a different answer and yes we do all right so we transferred the RSS speed agent it's running the exact same function with this new SQL select statement and we got a very different answer because again remember we included in the instructions to talk

**[0:19:10]** about how awesome the RSS feeds are and so it says we have a total of five fantastic RSS feeds available party emoji isn't it amazing how many great feeds we have to explore all right looking good uh nice I like it so now I can say route back and so we'll go back

**[0:19:25]** to the router agent and then um let's ask an analytics related question question so I'm just going to paste this one in here I've got what are the most popular categories among users I'll say looking to do some analytics I really want to make sure that it actually goes

**[0:19:38]** to the analytics agent sometimes it doesn't with this setup um but again you could always just work on the prompting to make sure it does with these kind of questions I'm just keeping it simple right now and so now it'll route to the analytics agent and there we go so a

**[0:19:52]** more complicated query now but it worked perfectly and so yeah we got machine learning it's preferred by three users and so this is the most popular category and then it lists all the other ones as well in a nice format so this is absolutely beautiful it is so cool how

**[0:20:06]** you can set up agents to work on different parts of your database and answer any questions that you have even creating like some pretty complex queries to get the information that you want from natural language prompts this is just awesome so let me know in the comments what you think of open AI swarm

**[0:20:21]** is it better than Frameworks like Lang chain plus Lang graph or tools like n8n I think it is incredible but also you do lose out on some customization compared to those things because it is a bit more black box so let me know what you think and also let me know if you want me to

**[0:20:36]** keep diving into these SQL database agent setups with other Frameworks or tools as well if you appreciated this content I would really appreciate a like and a subscribe and with that I will see you in the next video
