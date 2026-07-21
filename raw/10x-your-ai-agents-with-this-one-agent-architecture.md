---
type: raw-transcript
title: "10x Your AI Agents with this ONE Agent Architecture"
youtube_id: AgN3RHSZGwI
url: https://www.youtube.com/watch?v=AgN3RHSZGwI
slug: 10x-your-ai-agents-with-this-one-agent-architecture
published: 2025-03-23
duration: "0:41:36"
fetched_at: 2026-07-21
immutable: true
---

## Transcript

**[0:00:00]** complex problems always yield better results when tackled by a team of people with different specializations and with AI agents it works exactly the same way individual expertise combined creates exponentially better Solutions because just like with humans AI agents work better the more narrow their role and goals are it is all about Focus I know

**[0:00:23]** you have seen it before where you're building your AI agent and it works really well at first but then as you continue to add more instructions and tools it starts to hallucinate even with the things that it was doing well with at first and it's so frustrating cuz

**[0:00:36]** llms they just get overwhelmed so quickly and fragmenting your AI agent into different sub agents to handle different components is one of the best ways to solve for this and take your AI agents to that next level and that is exactly what I'm going to show you how

**[0:00:52]** to do right now because here's the thing creating an army of specialized agents takes a lot of consideration how do you split up the problem what tools do your agents need how do you combine the work done by all the agents at the end and most importantly one llm by itself

**[0:01:07]** already takes a while to get a response and so if you have to have many specialized agents running together how do you make it so that your system doesn't take ages to run but it's all right take a deep breath cuz I'm going to cover this all with you in this video

**[0:01:20]** so that by the end these kind of agentic systems are as clear as day to you both the how and equally important the why we'll build a parallel agent architecture using my two favorite Frameworks pantic Ai and Lang graph so we have a group of specialized agents that are running simultaneously all

**[0:01:38]** working to accomplish the same goal this is hands down one of the most important agent architectures and throughout this video I have a lot of tips and trick sprinkled in for both pantic Ai and Lane graph a lot that I'm sharing with you here so let's go ahead and dive right

**[0:01:52]** into it so let's start with the basics what is the parallel agent architecture at its core and I think that this article from anthrop IC on building effective agents explains it the best at a high level and it was published a while ago but I still refer to this

**[0:02:07]** constantly because it's just a great resource covering all the different agent architectures that you and I should be paying attention to and they even mentioned Lang graph in this article which is super neat and they do give a warning about Frameworks it's a level of abstraction that can sometimes

**[0:02:21]** be dangerous so you have to understand how these Frameworks work under the hood but that's why I'm showing you how to do things with Lang graph and pantic AI in this video and then scrolling down they have these diagrams for all these different architectures the one that we're going to be focusing on is this

**[0:02:36]** one right here parallelization and so we have the input com in from a user and then that's fed into these different green boxes each of these represent an AI agent with its own instructions and tools to tackle a certain part of the problem and then you have an aggregator

**[0:02:51]** at the end in this case this is not a large language model that's what the purple box signifies that just takes the output from each of the agents in parallel and prod produces some sort of nicely formatted output combining all the results for the end user like you or

**[0:03:05]** I and then in my case I even want to take this a little bit further and so we have a similar flow here but instead of there just being a non llm that Aggregates the results we use yet another AI agent as a synthesizer to take the output from each of our

**[0:03:21]** parallel agents and figure out a way to summarize it format it whatever for that final output for the user I'm just calling it a parallel agent architecture in our case instead of a work quo for orchestrator workers just because this is just a better name parallel agents and so the architexture that we have for

**[0:03:39]** our agent today is this so what you're looking at here is a visual representation of the L graph workflow for the agent that we are building we're making a travel planner assistant agent today it's a very good example of an AI agent that could operate just as a

**[0:03:55]** single agent but there's a lot that goes into planning a trip and so we have these specialized sub agents to handle different components like the flight hotel and recommending activities and so at the start of this conversation we gather information from the user where are they flying to where are they flying

**[0:04:11]** from how many days is their trip going to be for and so we have this initial Loop making sure we get all the information and then once we have all of that then we move on to the parallel part of our workflow having these different agents plan everything for the

**[0:04:25]** trip in parallel and then the results for all of these agents they're recommended commendations are fed into this final synthesizer agent that just summarizes all of it in a neat package to present to you for its final recommendation for everything and we even have a streamlet user interface

**[0:04:42]** built out for this travel planner assistant you can give your preferences for things like your Airlines and the amenities that you want in your hotel a budget level and then you can save these preferences and then I can ask it to plan a trip for me so for example I can

**[0:04:57]** say I want to plan a trip frying from Minneapolis to Paris uh in June and then my Max budget for a hotel is $200 per night and look at this I don't know if you caught that there but each of these lines were printed out at exactly the

**[0:05:10]** same time and that is the beginning of the execution of each of those sub agents in this parallel workflow and it happens so fast like it's already printing out the final results from the synthesizer streaming it out to my interface here but it was doing all of that in parallel it got the flight

**[0:05:27]** recommendations Hotel recommendations and activity recommendations at exactly the same time using different agents that were given different tools and instructions for that specific task and then giving me the final output at the end it is super neat so with our travel planner assistant we're not going to be

**[0:05:43]** using real flight hotel or weather data it's all mocked just because we want a simple example and focusing on the architecture itself versus the tooling but as usual I go above and beyond providing a lot of value so if you want to see the parallel agent architecture in in a full-fledged use case check out

**[0:06:02]** archon this is an AI agent that builds other AI agents completely free and open source this project that I'm pouring myself into right now and I recently implemented the parallel agent architecture and so I'll have a link to this GitHub repo in the description but take a look at this you can ask archon

**[0:06:20]** to autonomously refine the AI agent that it produces the code for and then it'll kick off this parallel workflow with these agents to refine The Prompt tools and agent and archon is an mCP server so you can literally hook it into your AI IDE like I'm doing with wind surf here

**[0:06:35]** and so first I ask it to build an agent using archon that searches the web with brave it produces this pantic AI agent for me so I've got all the code for it here but then I can ask it to refine the agent and so after that initial creation

**[0:06:49]** you can see that I just ask it to refine it and then this kicks off that parallel workflow to make all those revisions and then wind surf comes back and adds in all these code changes so we have parallel agents we've got wind surf working with an mCP sub agent there's so

**[0:07:04]** much cool stuff going on here so dive in this if you wanted to go into something insane but to start simple and really make sure we understand this architecture let's get into the code for the travel planner assistant here is the GitHub repository for the travel planning assistant all the code that

**[0:07:20]** we're going to create together right now I'll have a link in the description to this repo if you go there on the homepage you have this read me where I cover the architecture and also how you can can get up and running yourself if you want to follow along or take what

**[0:07:34]** I've built here and tweak it for your own use cases so I cover setting up your environment um your variables running the streamlet interface that I showed earlier all that good stuff and so the plan right now is I'm going to walk you through building the pantic AI agents

**[0:07:49]** that make up all the individual components for our workflow so all of the agents that you see in the agents folder those correspond to the different nodes that we have in our ra we have the infog Gathering agent the specialized agents who are planning the trip and then that final synthesizer all those

**[0:08:06]** are individual Python scripts that you can see right here and so I'll walk you through creating one of the agents from scratch we'll create the flight agent from scratch and then I'll briefly show you each of the other agents that are going to be created in a very similar

**[0:08:20]** way with pantic AI and then with that we can dive into building our Lang graph graph combining all these agents together to create the full process and so with that let's get into building our first agent so to make this as simple as possible for you you can think of

**[0:08:37]** building pantic AI agents as building three distinct parts so let me show you the documentation with a really nice example to demonstrate this so this is the weather agent just very simple implementation that I cover a lot it just shows these different components very well when you're building an agent

**[0:08:54]** the first component is defining the dependencies these are things like the API keys and database connections that your agent tools need for the agent to do things on your behalf then the second component is the definition of the agent itself and so this is where you specify things like the large language model you

**[0:09:12]** want to use the system prompt the exact dependencies and a lot of other different parameters that pantic AI offers for things like defining automatic retries for your agent as well and then the last component which usually takes most of your code for an agent is defining the tools itself and

**[0:09:31]** so you have all the functionality wrapped up in a function that the agent can call upon when it wants to do something specific and in this dock string this larger comment that you have at the top of the function this is where you specify to the agent when and how to

**[0:09:45]** use each of these tools so you give it the purpose and the arguments so I can reason about when it would invoke this tool specifically and what arguments that you would pass in for something like the location in this example and you just Define all the individual tools

**[0:10:00]** in the same way so that's a good overview of how we build an agent with pantic AI we're going to follow a very similar structure here building our flight agent so first we'll start by importing all of the libraries that we need and defining some of our configuration like getting the exact

**[0:10:15]** large language model that we want which in this utils.py I just have this simple function to get that based on our environment variables that we set next up I want to Define my dependencies for the flight agent in this case we're keeping it very simple again this is

**[0:10:30]** just more of a demonstration focusing on the architecture versus making really robust agents and so in this case our dependencies we just have the preferred Airlines for the user so they're going to set that in the streamlet UI like we saw in the demo earlier and then that's

**[0:10:44]** given as a piece of information to our flight agent then we can Define our system prompt just giving the instructions to the flight agent for its role and goals and how to use the tools that we give it as well and then that brings us to our second component for

**[0:11:00]** building agents which is the definition for the agent itself so we give it just like we saw in the documentation the model system prompt dependencies and giving it some automatic retries and then with that out of the way we can get on to the very last part I mean it's

**[0:11:14]** it's pretty simple overall because now we're just defining the tools for the agent and so we use this python decorator above the function definition itself to tell pantic AI that this is a tool for our flight agent that we just defined above and then the parameters here the large language model decides

**[0:11:33]** what we're going to use for the origin destination and date for searching flights and then this run context this is how pantic AI injects the dependencies like the preferred flights into this function and so at the very beginning just like we saw in the docs we're going to have a comment here this

**[0:11:53]** doc string that tells the agent when and how to use this function and then we can get straight into the implement ation cuz really tools for agents are just functions that you wrap up and send as a part of the prompt to the llm and so in this case we're using mock data so we

**[0:12:08]** have this dictionary that simulates something you might get back if you used a real flight API and so we return a few flight options and then if there are any preferred airlines that the user specified we're going to change the order of the flights based on their preferences and then just add a note

**[0:12:26]** that this flight was preferred or maybe multiple flights were prefer referred and so the result of all of this is then just going to be returned for this function and so whatever is returned here this Json string is going back to the llm so the agent the flight agent

**[0:12:41]** invokes this tool to search for flights and then that list of sorted flights based on preferences is given back so I can then reason about that and give the final answer to the user for what flight it recommends and even though we're building this agent to be a part of a

**[0:12:56]** larger architecture we can use this flight agent in olation and have a conversation with just it and so in this extras folder I created this flight C.P script and so this is a way for us to in the terminal have a conversation with the flight agent and there's a bit more

**[0:13:13]** of a complex implementation that I have here for streaming the output from the pantic AI agent I won't go in the weeds for this but I spent a good amount of time figuring this out so take this and use it for yourself it'll definitely save you a headache if you want to

**[0:13:26]** stream the output from your pantic AI agents so that not only do you get the response from the agent but you get the tokens out in real time as it is producing the response and so back over in the terminal I can run this command to run the flight CLI and then I can say

**[0:13:42]** something basic like Hello this won't cause it to search for flights but then I can say something like I want to go from Minneapolis to Tokyo on June 1st and based on what I sent here it's going to pick out the origin destination and date use that tool to search for flights

**[0:14:00]** and then stream out its recommendations to me obviously it's going to give me the same recommendations no matter what I say because it's not really searching for flights but yeah this is working beautifully and then for the rest of our agents they're built in the same way the

**[0:14:15]** sponsor of today's video is lutra a userfriendly solution for creating automated workflows with natural language ever wish your AI assistant could actually do things and not just chat I mean sure most platforms have web search and canvas at this point but that is not enough lutra is a full-fledged AI

**[0:14:34]** agent that connects seamlessly with your favorite services like slack and Gmail and then it can do things within those Services based on your conversation so it's very similar to a custom agent that you or I would make but the really cool part is that it creates code to take

**[0:14:48]** these actions on your behalf and then you can save that code as an automated workflow to reuse later or set up as a scheduled task called A playbook they're also launching this brand new plugin platform which is going to allow lutra to connect to literally any API you just

**[0:15:04]** give it the documentation and then it'll be able to write code to connect to that service just like the native Integrations it is super neat and so what does lutra actually look like well I'll show you a quick demo of it right now so to show you the power of lutra

**[0:15:18]** I'm obviously going to give it a request that something like Claude or GPT would not be able to do so I'm going to ask it to get a list of poll requests from archon my AI agent Builder from GitHub and then add them to a Google sheet and

**[0:15:31]** it's going to start right off the bat by reasoning to itself and you can watch this reasoning which is really cool and then it'll ask me a couple of follow-up questions so I'll go ahead and answer those and then what it's going to do is ask me to connect the necessary accounts

**[0:15:45]** for it to have that authorization for both Google Drive and GitHub and in this case I already connected GitHub so I'm showing you that I don't have to reconnect it but it is going to ask me to connect my Google Drive so first it'll create that code for this custom

**[0:15:59]** integration and then it'll ask me to connect my Google API all right so I'm all connected and now it just continues right away so I don't even have to go somewhere else to configure my credentials I just do it right here in the chat when it's required for the

**[0:16:11]** first time and now it's doing everything that I asked it to do and boom look at that it even opens up the Google sheet within the lutra UI on the right hand side it looks absolutely perfect pulled all my active PRS tells me my sheet ID asks me what I want to do next we can

**[0:16:27]** see all the actions that it did within GitHub and Google sheet this is just incredible to me pretty slick right luch is like having an AI agent that can reason think and build Integrations for you so you're not just chatting with it it's doing stuff for you and building

**[0:16:42]** automations at the exact same time and it's totally free to get started so you can head on over to lutra doai I'll have a link in the description definitely worth checking them out so that is the flight agent now we can dive really quickly into the other specialized

**[0:16:55]** agents I'm going to go fast because this setup is very similar take a look at this this is our hotel agent so we've got our dependencies again and this time it is going to be the amenities that we're looking for and our budget level then we have a system prompt structured

**[0:17:10]** in a very similar way we Define our agent and then we have a tool to look up hotels so that it can make a recommendation so we have again this mock dictionary this is what a real hotel API would give something like this and then we filter and sort based on the

**[0:17:25]** max price preferred amenities and the budget level and then return the final list of TS so the agent can reason about that to make its recommendation and then for the activity agent we don't even have dependencies in this case so it is even simpler we just have our agent definition with the

**[0:17:40]** system prompt and then because the weather oftentimes dictates what activities you can do on a trip we give it a tool to look up the weather so based on the date and a city we have this mock data so for a few cities it can look at the temperature and then use

**[0:17:55]** that to reason about if it's going to recommend more indoor activities or more outdoor activities whatever it might dictate based on the weather so those are all of our specialized agents we've covered everything for these three right here now we just have two left we have our final synthesizer agent and then our

**[0:18:12]** info Gathering agent and so starting with the simpler one we have our final planner and take a look at this there's not even a tool for this agent because it's main job its only job is to take the recommended hotels flights and activities and combine it together in a

**[0:18:30]** nice summary this is also a good opportunity to have an agent that could validate the different outputs from the other agents you can use a synthesizer as a validator as well and add different tools to do that but in our case to keep it very simple it is just an agent with

**[0:18:45]** a system prompt nice and easy and then the last agent that we have is our info Gathering agent and what makes this agent Special is that we are using structured outputs to guarantee that every single response from this agent has these key pieces of information and the reason I'm doing this besides it

**[0:19:03]** just being a good opportunity for me to show you pantic AI structured outputs is because we want to guarantee that we have the necessary information for our specialized sub agents to invoke the tools that they need to invoke to search for flights hotels and weather data and so we get the destination origin Max

**[0:19:22]** hotel price the dates that they're leaving and returning everything that our sub agents need and then we have the resp response this is what we give back to the user as they're conversating with this infog Gathering agent and then finally we have this all important Boolean value that determines if the

**[0:19:39]** user has given all of the necessary values and this is what we key off of to determine in our graph if we can continue to the rest of this flow invoking our parallel agents and so at the beginning the user might say something like I want to take a trip to

**[0:19:56]** Germany and then the G infog Gathering agent will be okay cool but I don't have enough information to call upon the rest of these agents here I need to know where you flying from what dates are your trip going to be and so the user will give all that information and then

**[0:20:11]** we can continue to the rest of the process but if they don't give what's required we continue in this Loop until they do that's the important job of this infog Gathering agent is to gatekeep the rest of the process to make sure that the agents don't hallucinate Because by

**[0:20:26]** the time it gets to them they will have all of the necessary information and so the rest of the agent is defined in a very similar way where we just have a system prompt and then the definition for the agent itself and then the way that we can enforce that it produces a

**[0:20:39]** Json output that matches this structure is we just add this single line to our pantic AI agent the result type is and then we pass in our class that we defined right here for travel details and that is it we have now defined all of our agents in this graph and so now

**[0:20:56]** we can take each of them and piece them together in in our Lang graph implementation and just like with pantic AI you can think of Lang graph implementations as being three distinct parts and I just love breaking down complex things like this if you can compartmentalize the different parts of

**[0:21:12]** what goes into a process it just makes it a lot easier to understand and so for Lang graph our first part is the state for the graph these are the key pieces of information that you want to keep track of throughout the execution that your agents will use you'll give back to

**[0:21:27]** the user things like the conversation history and the results from the different agent executions then the second part is defining all of the nodes for the graph and So within each node you have all the logic to do something like invoke an AI agent or in Lane graph

**[0:21:41]** each node doesn't even have to call upon an llm you can just have deterministic code if you want and sometimes that's even better than using large language models that can be all over the place sometimes so that's the second thing and then the very last component the third

**[0:21:54]** component to Lang graph is setting up the graph itself so you take the State you take your nodes you define all of them within a graph instance and then you connect them all together with edges and that's it that's all that goes into building a graph but what I'm going to

**[0:22:10]** do with you right here to walk you through it step by step is I am going to delete everything take a look at this all right boom it is gone we have a blank slate so I'm going to walk you through this step by step to really make

**[0:22:21]** sure you understand how we are connecting all these agents together and managing the state for everything in L graph so the first thing we're going to do is support all of our libraries that we need and the different agents that we're going to be running through our nodes then we can knock out right away

**[0:22:36]** the first part of our graph which is the state and so this is everything that we have to keep track of throughout the execution of our workflow and so we have the latest user message we are building up conversation history specifically for the infog Gathering agent the rest of

**[0:22:50]** the agents don't really need conversation history then we have the travel details that's that structured output from our info Gathering agent we'll store that because we need to use it for the rest of our agents and then we have user preferences the result from each of the parallel agents and then

**[0:23:05]** finally what is aggregated together into that final plan from our synthesizer agent is stored here so that's the state now we can get on to building the graph itself so I'll show you setting up the structure for the graph and then we'll get into building each individual node

**[0:23:21]** and so the first thing is you want to create an instance of the graph and then you pass in the travel state so now we know what the state is going to look like for this graph and then we can Define all of our nodes and again there'll be a separate python function

**[0:23:35]** for each of these nodes right now I'm just adding them into the graph one at a time all the nodes that you see here like Gathering info getting the next user message getting flight recommendations these names correspond exactly with the nodes that we see in this graph because the lane graph Studio

**[0:23:51]** that we're looking at right here it looks at this python script it builds the graph and then it displays exactly how we set it up with our nodes and then also the edges which we're defining here so we start with the infog Gathering agent and then we have this conditional

**[0:24:07]** Edge and so this is that decision right here do we get the next user message to continue the conversation to gather the info or do we pass on to our specialized parallel agents to finish the workflow recommend the travel details so we make that decision based on this function

**[0:24:26]** that we'll Define later as well and then we add an edge from getting next user message to Gathering info because once we get more details from the user we want to pass back to the info Gathering agent to determine if it has everything it needs now and then finally we add

**[0:24:41]** edges from all the specialized agents going all three into the same create final plan node because that's how we can take the outputs from all three and bring them together into the synthesizer all at the same time and then finally our synthesizer agent just goes to the end of of the graph now we can move on

**[0:25:00]** to building out the nodes for our graph and so starting with our first one the Gathering info agent and so we take two pieces of information for this function we have our state so it can access things like the message history and user input and then we also give it a writer

**[0:25:16]** I'm not going to go into the Weeds on this but this is a custom object that you can pass in in Lan graph which allows us to stream the output from our pantic AI agents so we watch The Tokens come out in real time and so first we'll

**[0:25:28]** will get the user input from the state and then we'll build up the message history over time because we want our info Gathering agent to be conversational because different parts of the trip are going to be given by the user throughout a couple of messages potentially and the reason we're using a

**[0:25:43]** model messages type adapter here this is a special object that we have from pantic AI is because when we get our messages from a pantic AI agent we need to convert it into a format that we can store in a database and to make it very compatible with databases like postgress

**[0:26:00]** we choose Json B binary Json that's the format that we store our conversation history in the database and in the state here but then when we retrieve that conversation history to use a again in a pantic agent we have to convert it back into the format for pantic AI so that

**[0:26:18]** it's an object in Python not just Json being that's what we're doing here so one of the more complicated parts of pantic AI I hope that makes sense though and so now with the conversation history we can invoke our agent using run Stream So that we get the tokens outputed in

**[0:26:34]** real time and we just have to pass in the user input and then the conversation history and also if you want to run synchronously like you don't want to stream the output you just want to get it all at once I have this comment right here which you could use instead it

**[0:26:47]** simplifies things a lot but I think a lot of you appreciate having streamed output it just makes the agent feel snappier and more responsive so I wanted to show you how to do that and so the way that we do that it's kind of unique here because remember this infog

**[0:27:02]** Gathering agent it streams out a structured response we have that Json object I can even go back to the agent and show you that definition again we have this Json object that we're outputting and so it's not as simple as just streaming out a string because it's a dictionary that has these different

**[0:27:19]** values and so there's a very specific way to do this in pantic AI that I I don't want to dive into a ton but if you go to their documentation they do show you how to do this so I just poked around for a couple of hours with this

**[0:27:32]** documentation figuring out how to best do it using this example right here streaming structured responses and so you can see that when you run an agent in stream mode and it outputs a structured response the output that you get over time as it streams out the tokens is going to look something like

**[0:27:50]** this where it slowly builds up the values in the dictionary and even within a single key it can build up that string over time and that's what we're going to do with our response and so over time we're building up the travel details. response because this piece of

**[0:28:06]** information is what we want to give to the user as the output and then the rest of the items we're just keeping track of these behind the scenes because that'll get past into our other agents later this is the most complicated part of the entire graph so I hope that makes sense

**[0:28:20]** to you and then we're just validating the Json at each iteration and we are using this debounce bu so that we're not every single split second validating the Json structure we're just doing it every you know .01 seconds here validating that the Json is good Json and then

**[0:28:38]** finally at the very end if we have a valid travel details. response then we're going to write that out to the user and we're going to save this to our graph state so we get the results from invoking our agent and we append that conversation history so we're adding on

**[0:28:55]** to the conversation history and then also setting the travel details to that structured output that we just got and so now travel details is going to be an object that contains all of these pieces of information that we can reference later from our other specialized agents and then luckily the rest of our nodes

**[0:29:13]** are definitely simpler so starting with our flight recommendations node and so same arguments that we're passing in we're going to get the travel details and preferred Airlines from our state so this is set by the user in the front end and then this is what was just set by

**[0:29:29]** our info Gathering agent and then we also write out to the screen that we are getting flight recommendations so remember we saw in the demo earlier that it wrote out to the screen getting flight recommendations getting Hotel recommendations getting activity recommendations all at the exact same time so I'm just putting this in here so

**[0:29:47]** that we can see that this is truly simultaneous execution CU sometimes people will say it's parallel when really it's just running one after the other sequentially just combining the output put at the end but this is truly parallel and that's really important because otherwise this workflow would take a long time if it wasn't

**[0:30:05]** simultaneous and so then we're going to set up our dependencies for the flight just with the preferred airlines that we get from the state and we can create our prompt and invoke our flight agent so we're injecting the key pieces of information from the travel details into this prompt here so that our flight

**[0:30:22]** agent has the information that it needs to invoke that tool and then we just call it and we do it synchron ly this time so I'm not doing any fancy streaming stuff here because there's nothing that we want to write to the screen yet we want to wait until we have

**[0:30:37]** everything synthesized together and then stream that out to the user and then in the meantime we'll just say that we're loading that we're getting the flight recommendations so pretty simple and then the only thing that we want to update in the state for the graph is the flight results so we just take the

**[0:30:52]** results from invoking the agent get the data and then that's just a string that we store in Flight results and then for our other parallel agents it's going to look very similar so getting Hotel recommendations again we just get the necessary pieces of State build up the hotel dependencies and then we create

**[0:31:08]** that prompt again passing in the key information from the travel details and then running that agent and then we just set the hotel results to that string the results. data and then finally for the activity recommendations it is exactly the same so I'm just glossing over this really quick there's nothing new to go

**[0:31:26]** over in this node we just have to to get it set up and then we have our synthesizer agent and so this time what we're going to do is take the state that we have for each of our parallel agents because at this point because you set it

**[0:31:41]** up this way in the graph we have all of that defined it's guaranteed to be defined for each of those specialized agents so we get those different pieces of information and then we build up this prompt where we are asking it to summarize all of these recommendations and then we give it the flight hotel and

**[0:32:00]** activity recommendations and we ask it to create a comprehensive travel plan based on these recommendations and then we just run a stream so we call the Run stream again and then we're going to stream a little bit differently it's simpler this time because it's not a structured output it's just a regular

**[0:32:16]** string and so we can call the stream text function instead and it's going to give us a bunch of different chunks basically portions of the response that we can use that custom writer object that we have here to stream the response out to the front end like we saw earlier

**[0:32:31]** in streamlet when I gave you that demo and then finally we can get the response just like we did with our other agents and then set the final plan to that value and that is it we have defined everything for our agent nodes and so now we can just Define a couple of the

**[0:32:46]** other pieces that we need like for example when we make that decision do we have all the information we need to continue or do we have to keep asking the user for more travel details we're doing this with this routing function here so first we get the travel details

**[0:33:02]** cuz remember going back to the graph here this message get next user message it goes back to gather info and then we make the decision which one do we route to and so when we're making that decision we have the travel details defined because that happens after the

**[0:33:18]** Gathering info agent so we get the details and then we just see is all details given that Boolean value that it defines right here is this true true or false and if it's true if they have given all of the necessary details then we can move on but if it's false like we

**[0:33:36]** see right here then we have to move on to that node to get the next user message and then we'll display in that response variable to the user like hey I need the destination or I need the dates you're going on your trip then we get that from the user then it comes back

**[0:33:52]** and we would make this decision a second time after we get a response and so if we are good to continue if all details given is true then we can just return a list of the nodes that we want to move on to and so when we return a list in a

**[0:34:07]** router function like this in L graph that means that we're going to execute all of these nodes in parallel so it is that easy to get simultaneous execution of nodes and laning graph just like this and within our Edge the dictionary or the array I should say right here this

**[0:34:23]** just defines all the different nodes that we could route to and so just like we have a list here we have a subset that we return these are the ones that we want to execute which is basically everything except the get next user message node and then finally for the

**[0:34:37]** node itself to get the next user message we're using this concept in Lan graph called an interrupt this is how you add human in the loop to L graph which is a very powerful way to no matter where you're at in the execution of a l graph workflow you can stop and wait for the

**[0:34:54]** user to input something so in this case we're waiting for them to provide a value and I'll show you later how this is set up in the streamlet UI we're waiting for the user to provide a value which we then set as the user input so we stop the graph here we're not running

**[0:35:09]** it anymore we wait for them to input a message and then we set user input to whatever their message is and because we have the edge that takes get user message back to gather info that's how we then repeat the process of calling our info Gathering agent and so with

**[0:35:27]** that out of the way we now have everything we need for our nodes and so the last thing that I want to add here is memory for our agent so that it can remember the state of the graph when we have that human in the loop interrupt we're just using a simple memory saver

**[0:35:41]** so it's going to save it on the RAM on my machine you can set up a SQL light or a postgress memory saver if you want to use superbase or something to store all this state so you can make it very persistent in production ready as well if you want I'm just keeping it simple

**[0:35:53]** and then finally we'll just call our build travel agent graph so that we have this travel agent graph instance that we can now reference somewhere else to call into this graph and that's what we do in our streamlet UI so for the streamlet interface let me show you really quickly

**[0:36:09]** how we interact with our agent and so first we import the travel agent graph that we just defined right here so we have an instance of the graph that we can then use within our UI anywhere and so in our function specifically to interact with the agent invoke agent

**[0:36:25]** graph we take in the user input as a par parameter and then we first Define our configuration including a thread ID this is how we can have a unique identifier for this specific execution of our Lan graph graph and then if it is the first message from the user as in the current

**[0:36:43]** chat history just has a length of one that means we're invoking the graph for the first time so we build up our initial state where we have the first user message and then we have all the preferences that they set in the UI and then with all of that we just use the

**[0:36:57]** aam function call for our travel agent graph giving the initial State the config that has the thread ID and then stream mode equals custom is how we have that writer object passed into our nodes so that our pantic AI agents can stream the output in real time to our front end

**[0:37:14]** because we just use this async 4 so that as we're getting those chunks we're able to yield those and display them in real time and then if we have more than just a single message in the chat history that means that the convers ation has already began with our info Gathering

**[0:37:30]** agent and we want to continue it and so in our graph that's where we have this interrupt here where we are waiting for that next value from the user and so to send in that value we call the agent in a very similar way as when it's the

**[0:37:45]** first message except instead of passing in our initial State we're using this command directive in Lang graph where we say resume is equal to user input so whatever you set resume to here that is what that value gets defined as for that human in the loop interrupt and so value

**[0:38:02]** is now whatever user message and that's what's set for the user input State and so we're just passing in user input for the resume here and then the rest of it the same we just give the config and then the stream mode of custom yield each message so we're streaming out that

**[0:38:16]** response it's it that's it and I'm not going to dive into the exact setup for the streamly interface and everything like that because that's not the focus of this video but with that we can now just I'll show you the command here you can just run streamlit run and then the

**[0:38:29]** name of the UI I forgot to save which is why I got that error but yeah you just run this command and then that'll spin up the UI in the browser for you so we can go ahead and chat with our agent and so I can say my name is Cole my

**[0:38:40]** preferences are I like Ocean Air for my Airline I really want to have a restaurant and free breakfast because I'm just a foodie I guess um and then a budget level of mid-range I'll sa my preferences and then just like with our initial demo let's just have a fun

**[0:38:56]** conversation with it so I'll say I'm want to go to Spain all right and so obviously this isn't enough information at first and so now the agent the info Gathering agent is going to ask for more details and it's not the nicest response it's just very blunt like boom give me

**[0:39:13]** more you could obviously change that in the system prompt if you want I just kept it very basic but I'll say I'm flying from Minneapolis just keep that same thing going um going June 1st through the 6th um and I don't want to spend more than let's just say $250 per

**[0:39:36]** night for a hotel all right so we give it all the information that it needs and now yep there we go we have everything that we need and look at that it invokes all three of our specialized agents at the exact same time so we're just waiting for all three of them to finish

**[0:39:50]** and then it's going to get fed into our synthesizer agent that streams the output look at this your comprehensive travel plans for Spain and and Bam this is really fast this is using GPT 40 mini under the hood for the llm for all of these agents by the way and yeah this is

**[0:40:06]** just awesome again just using all mock data so it's not like the most amazing thing but yeah here we go we got our restaurant this one doesn't have free Wi-Fi or or free breakfast rather so it didn't accommodate all of our preferences but it did for the flight it

**[0:40:19]** said Ocean Air so it did its best based on the mock data that we gave it yeah this is working so well and you can take this kind of architecture and and all the things that I taught you here with pantic AI and Lang graph and use this

**[0:40:32]** for your own use case and get really complex with it you can turn your synthesizer agent into a validator as well you can give a ton of powerful tools to your different specialized agents to really take advantage of the fact that you can split up the different tasks in that way there's so many ways

**[0:40:48]** that you can take this further a lot of things I want to do with that with my content going forward as well so there you have it you now have what it takes to build specialized AI agents that run in parallel and that just unlocks that next level of

**[0:41:00]** building agentic systems that are far more powerful than what you could do with just a single AI agent so this architecture it's not just efficient it is transformative for the way that allows you to solve complex problems for really any use case also I'm planning on putting out a lot more content in the

**[0:41:16]** near future for different AI agent architectures and continuing to build powerful agents with pantic AI and L graph so if you appreciated this video and you're looking forward to more things AI AG pantic Ai and L graph I would really appreciate a like and a subscribe and with that I will see you

**[0:41:33]** in the next video
