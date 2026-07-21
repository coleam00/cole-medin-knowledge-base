---
type: raw-transcript
title: "We've Been Building AI Agents WRONG Until Now"
youtube_id: pC17ge_2n0Q
url: https://www.youtube.com/watch?v=pC17ge_2n0Q
slug: weve-been-building-ai-agents-wrong-until-now
published: 2024-12-08
duration: "0:19:53"
fetched_at: 2026-07-21
immutable: true
---

## Transcript

**[0:00:00]** the whole idea of AI agents large language models that are able to do things for you autonomously is so brand spanking new that Frameworks like Lang chain crew aai and swarm and especially no code agent Builders aren't actually good enough for mature and production ready AI agents without you having to

**[0:00:19]** put in a lot of additional work but with pantic AI things are starting to change in a lot of really incredible ways pantic AI is an open-source python agent framework that makes it a a lot less painful to develop truly production grade agents it implements a ton of

**[0:00:36]** really important features that are often overlooked in other Frameworks for agents we got things like context management air handling and retry logic testing and evaluation capabilities logging and monitoring large language model output validation just the name a few and this list goes on pantic AI is incredible and it is so easy to use but

**[0:00:56]** in a lot of ways building an agent with it is not actually my focus in this video what's really important for you and what I'm going to be focusing on is the how how is pantic AI actually making it possible for you to more easily build production grade agents because in the

**[0:01:12]** end any framework going forward needs to implement all these features that I'm going to cover in this video and you have to know how to leverage them so that's what I'm going to show you right now I'll show you what I mean first by heading on over to the pantic AI

**[0:01:24]** documentation and blowing your mind there then we'll build an agent from scratch with this framework so I can can show you how easy and Powerful it is let's Dive Right In All right so I promised that I'd blow your mind with the pantic AI documentation and so I'm

**[0:01:38]** going to live up to that right now with a quick overview of all of these features that I've already talked about and then we'll go and build in Asian but first of all pantic itself has been around for a long time it's essentially a validation library in Python and what

**[0:01:52]** I mean by validation is this let's say you're building a fast API endpoint for example fast API is actually built on typ of pantic well you have all these endpoints that expect specific information specific payloads to come into the endpoint and pantic is that validation layer that makes sure what

**[0:02:10]** you expect to come into your endpoint is actually what you receive and similarly for large language models like with open Ai and anthropic you can see right here that they have pantic as their validation layer you expect often times specific input from the large language model or specific output if you're

**[0:02:27]** working with structured output so certain keys and J on something like that and pantic is that validation layer to really ensure that you're getting that structured output that you are expecting and so yeah like I said open Ai and anthropic use it Lang chain llama index crew AI all these other things

**[0:02:44]** that I referenced at the start of the video as well they all use pantic as the validation later now this team is who are going ahead and making pantic Ai and so that's why I really trust in in Mak something beautiful here because they have validation at the core of what they

**[0:02:57]** believe in and that's one of the big things that a lot of the these other Frameworks don't focus on they don't focus on validation for the output of llms or testing llms or working with your tools and making sure you're invoking the right tools all these things they all have to do with

**[0:03:11]** validation so that's why I'm really excited for pantic AI so let's cover some of these features really quickly here in the documentation first of all it's model agnostic they have all these different providers that you can use and you can even added some yourself so later in this video I'll show you how to

**[0:03:27]** use a pantic agent with AMA so it can be 100% local it's type safe they've got structured responses and stream responses that's what really leverages the classic pantic under the hood they have a type safe dependency injection system this is how you can manage context for your agent important things

**[0:03:45]** like database connections and API Keys which a lot of Frameworks don't have and this is super useful also for testing and evaluation as well because you can have mock dependencies for your agents and they also have log fire integration for debugging and monitoring and there's a video down here I want to show really

**[0:04:01]** quickly that gives you a sense of what this actually looks like it's just so robust the way that you can set up a pantic AI agent and then have this entire UI to show you what's going on with all your llm calls and Tool calls it is just amazing and then they got

**[0:04:14]** some other examples in the documentation here like showing how you can use different providers like boom I just say I want to use Gemini 1.5 Flash and it automatically knows to go to Google for the provider and if I switch this to GPT 40 boom we'll be using open AI under the

**[0:04:28]** hood so it integrates with all these different providers and then we have the tools and dependency injection so like right here my agent needs a customer ID and a database connection these are the kind of things that my tools might need that I don't want to actually give to

**[0:04:41]** the llm to pass as an argument to the function so a lot of times with other Frameworks you have to call your tools manually and add in these extra parameters but you don't with pantic because your agent session has these things tied to it and also to tie a tool

**[0:04:57]** to your agent you just have to say this agent right here that I defined very simply above has this system prompt and it has this tool and then you just attach the function to wherever you put this decorator like right below you to find the function and boom now it's able

**[0:05:12]** to invoke this tool you don't have to do it manually and every single tool call is going to have that extra context that you passed in here like your API keys and whatever just so so easy to set it up and there's so many other things as well like if we go into the results here

**[0:05:26]** it's really easy to get the information from your result to get the cost any other sort of metadata they have chat history and messages you can get the entire chat history after any call to a large language model they have a ton of stuff for testing and evaluation that is

**[0:05:40]** so useful um like being able to have a test model so so you don't actually have to call a large language model to run your unit or integration test because you never really want to pay real money when you're running your tests and so it's just so so important and then they

**[0:05:55]** have a ton of examples here some of them actually get quite complicated but a really basic one right here here is they have a weather agent so if you're looking to really quickly understand how to build an agent with pantic AI I would suggest going to their weather agent

**[0:06:07]** right here uh because it shows you how to set up your context here like the weather API key and your client and then you define your agent you define your tool to get the latitude and longitude like this and then by the way the dock string is what tells the llm when and

**[0:06:22]** how to use your tool um then you define another tool for getting the weather that's a bit of a longer one right here and then you have your main function and this is where you create your dependencies which is that context for the agent and then you call it and

**[0:06:33]** that's it and you can set up conversation history all that good stuff that I'll show you later as well so easy to use this framework but you get all these other things that other Frameworks don't normally have and so with that let's dive into actually creating an agent with pantic AI so for this demo of

**[0:06:48]** pantic AI we'll be building a web search agent it's one of the hottest kind of Agents right now it's just so important to connect your agent to the real world with web search and we'll be doing this with the brave search API it's one of the best apis for browsing the web and

**[0:07:03]** it's free to use to get started as well and so I have the documentation up right here I'll be referencing this a couple of times as we build the agent again it's not the main focus of this video the main focus is just showing the Power Pad antic Ai and the kind of things that

**[0:07:16]** you want in a framework to build production grade agents but it's also a cool little tangent here to show you how to use this API so that's one of the prerequisites along with python having an open AI API key if you want to use GPT like I'll be using in this video and

**[0:07:30]** then also downloading ama if you want to run local llms with pantic AI like I will also be doing in this video and all of this code that I'm about to cover here I'll have a link in the description to my GitHub repository where you'll have all the code that I'm going to be

**[0:07:43]** creating with you here as well as instructions on how to run everything yourself so this read me that we're looking at right here will be available for you to make it as easy as possible to follow along with me run this yourself and extend it yourself and so

**[0:07:56]** with that let's dive into creating the code so the only thing I have in my python script right now is the skeleton for a main function we really are going to be building this pantic agent from scratch together right now the only thing I've really set up at this point

**[0:08:09]** is myv file so you'll see this env. example file in the GitHub repository you just want to set your API keys and the model that you want to use and then rename it Tov just like outline in the instructions right here and so by the way the model I'm using right now is

**[0:08:24]** quen 2.5 coder 32b so we will be using AMA for the demonstration in a bit once I have this agent fully built out with you here and so the first thing that we're going to do is import all the packages that we need right here for our agent and then we can load our

**[0:08:38]** environment variables and Define the large language model that we want to use and to get things ready for olama if we choose olama we're going to create a custom asynchronous open AI instance where we override the base URL right here to point to Local Host Port 11434 where olama is currently running

**[0:08:55]** on my computer and then what we do is Define the model that the actual instance that we want to run based on the value of the large language model environment variable so if it starts with GPT that means we're just going to use a base open AI model not with the

**[0:09:11]** overridden base URL but if we aren't using GPT then I'm going to use this custom client that I set up because I'm assuming we're using olama at this point and so if I have llm model defined to something else like I do currently like quen then we'll be using

**[0:09:25]** olama next up I'm going to configure log fire for that amazing logging and monitoring that's included with pantic AI so this is actually optional if you don't have this set it won't configure log F fire but it'll still work and I'm actually not going to configure this right now because I want to keep this

**[0:09:42]** tutorial concise and simple just know that it's really easy to set it up with this code right here and then after this this is where we get to Define our dependencies for our agent and so the client right here this is our dependency for the client that will be browsing the

**[0:09:57]** web and then we have our brave API I key and so this way every time we call a tool with our agent it's able to access these two things which we need we don't want to tell the llm oh here's the brave API key to give to the tool because we

**[0:10:10]** don't want to have to pass our credential into the large language model call so we' know what to give as that parameter so we have that as a dependency so it can still be used by the tool but doesn't ever have to be given to the llm so I hope that makes

**[0:10:22]** sense U but then moving on here this is where we get to actually Define our agent and then we bind the tools to it subsequently so we have the model that we want to use which is going to be either pointing to olama or open aai we can Define our system prompt here which

**[0:10:36]** is a pretty basic system prompt the one thing I do give it is the current time so that it can include that in more you know recent web searches and then I give it the dependencies telling it to expect a client and brave API key and then also

**[0:10:49]** model retry this is something that's so important that other Frameworks don't include I can tell it like if there is an overload error like we see with anthropic all the time it can retry another time for actually fails and so super super useful and then we can Define our tool to actually search the

**[0:11:06]** web and so we just have this decorator here where I reference the name of my agent and then I say do tool and then I Define this function here where it accepts first of all the context which is what we have right here and then also a parameter that the llm will Define

**[0:11:20]** which is the query what does it actually want to search the web for and then we have our doc string that tells the llm when and how to use this function what arguments to give and what to expect from it and then we can go on to Define

**[0:11:32]** it so first of all if the brave API key is not defined in the context for whatever reason like maybe we're just testing this function out then we can return a test sample message right here otherwise we'll move on and start setting up the API call to Brave and so

**[0:11:47]** we Define the headers that are required and again you can go and reference the brave API documentation to figure all this out or even just ask GPT or CLA it can help you with these things which is super neat um so we Define the headers and then we start basically a section of

**[0:12:02]** log fire here so that we can have this Dynamic logging and we can have these different sections to see oh yeah this is the section I click when I want to see what happened in the tool called a brave and So within this log fire span here we are going to use the client that

**[0:12:17]** we have as a part of our context this HTTP client to call the brave API with all the parameters and headers with our API key that we need and then we just get the response and then finish off this section of our log fire logging and so now with that we can massage the

**[0:12:33]** results that we get into what we want to output for the llm and so this is basically just taking this fancy Json that we get back from the brave API turning it into what we want to tell the llm and then returning that so whatever we return here as a string is what the

**[0:12:47]** large language model gets back to then reason about and give the final answer to us and so that is the end of this tool right here and so now in the main function here we get to actually Define the use of our agent and so I start a

**[0:13:00]** new agent here I Define the dependencies for it with my client and my API key which I just get from the environment variable obviously and then all I have to do is say my agent. run and then I give it my prompt and the dependencies and boom that's it you can also attach

**[0:13:17]** chat memory here if you want which I'll show in a little bit for another demo um and that's it we get the result and then we print it out and we can also use this debug library that pantic uses in their documentation so you can see everything that happened all the tool calls and

**[0:13:31]** stuff that got to the response that we'll eventually see with this last print statement right here and that is it we just got basically like a 100 lines of code right here we have this full web search agent it's pretty basic with how it uses the brave search API um

**[0:13:45]** but just know that like there are a lot of other endpoints they have as well where you can like summarize results for example from a bunch of web searches you can do image search as well so you could take this example that I have right here and create a bunch of other Brave tools

**[0:13:58]** to do image search in all the different ways that you need because right now this search is mostly helpful just to get specific articles for example so the question for my demo here is going to be give me some articles talking about the new release of react 19 which came out

**[0:14:12]** just this week by the way and so give me some articles but it's not actually going to go into the Articles and give me research from those but you can do that by extending what I've built here uh with the brave API so with this let's go ahead and try it out running this

**[0:14:27]** thing is super easy I've currently in the Dory for pantic AI where we have the python script and all I have to do now is run the command Python and then web search agent. py and this is using quen running locally on my computer so it's going to take a little bit here but it'd

**[0:14:41]** be even faster with GPT but still you can see it's pretty fast here you can see that it's telling me when it's running the search web tool it's getting the result and now reasoning about it and boom here is our response here are some articles discussing the new release

**[0:14:54]** of react 19 very pertinent to my question here and then it gives me three articles that I can go go check out right now click on any of these links and there we go did some web research for me and then because we have that debug that I showed earlier running we

**[0:15:07]** have the entire history of what's going on here like with the what the tool returned to me and the tool call that I chose to make absolutely perfect so this thing is working really really nicely now this is the base agent that I want to show you how to make I also have

**[0:15:21]** another version in the GitHub repository where I created a streamlit interface so an actual UI with chat history so you can interact with this agent in a more robust way so I'm not going to show coding that one from scratch but I'll quickly show you the code for it and

**[0:15:35]** then demo that one as well so last up I wanted to show my streamlit version of this agent that we just built together and it's a little bit more in depth so I'm not going to cover building this one from scratch cuz I don't want this video to be 45 minutes long but I want to show

**[0:15:48]** this really quickly because it implements some of the other really cool features of pantic AI the first one being chat history with that other agent we just sent a single question into the agent and it's not like we could repeat chat with it but with what I'm going to

**[0:16:00]** show right here you actually can I also implemented text streaming and so we'll see in typewriter style the output coming out from the llm in real time so we don't have to wait for it to fully finish its response before we can start reading it and so one thing I will say

**[0:16:15]** is olama doesn't seem to support streaming with pantic AI so right now I'm just using GPT 40 for the model but it's still really cool to see this and I'm assuming that there's just some disconnect between how the open AI compatibility of the AMA API works works with pantic that stops this from

**[0:16:31]** happening not totally sure there but anyway we're using GPT 4 for this I have this function set up that uses my agent so I extrapolated some of what we had in the web search agent. py script into my streamlet UI to execute the agent running this stream Command right here

**[0:16:48]** and then I pass in the message history so you can see that as a parameter to this function to call my agent I give the entire message history I take the latest message content as the current prompt and then everything except the latest message as the history and so

**[0:17:02]** that's how I get the response with chat history and I just yield each chunk as they come from streaming the llm output and then within the main function right here I display all the chat history in the UI I take in a prompt from the user chat input and then I manage the state

**[0:17:19]** so I add the user message to the current state of messages and then I add the response to the state when I get that back and then I just use asynchronous operations here to call prompt AI get that response and then display it in the front end so super super basic and then

**[0:17:34]** this second script that I have the streamlit version of the agent is basically the same thing that we already coded just with the parts taken out of it that I have to run within the streamlet UI right here and so with that we can go ahead and run streamlet and

**[0:17:48]** try this out all right let's test this thing out it's basically the same agent what we had already but I don't have to define the question in the code I can do it here in the UI I get streaming I got chat history and it's also using GPT 40

**[0:18:01]** so it should be a little bit faster as well I mean it's really cool that I was using quen I wish I could here too but it'll also be nice to get some a little bit faster here so let's start with the same question here I'll say uh give me

**[0:18:10]** some articles for the new release of react 19 all right and so you can see it's running in the top right getting me my response there we go we have it streaming out this is looking really really nice all right cool cool and then yeah so because it has chat history I

**[0:18:27]** can say what did I just ask and if chat history wasn't working it would have a totally wrong answer here but here we go you asked for some articles about the new release of react 19 perfect so now let's ask uh what is the net worth of Elon Musk let's see if we can get this

**[0:18:41]** answer as well uh so yeah searching the web as of December 2024 surge past 300 billion so I asked this question in my flow wise video as well I just think it's nuts how rich he is it's pretty crazy he's got a little bit of change to spare um but yeah this

**[0:18:56]** is working absolutely beautifully and also the extremely why it just makes it so easy to build something beautiful really fast so I love using streamlet in my videos as well but yeah pantic AI this thing is just the goat I hope that you found this video super informative

**[0:19:09]** it is just so important to stay up to date with the latest and greatest not necessarily so you can just use the hottest framework for the month I mean none of us like switching like that but more so just so you can understand the direction that we are heading as an

**[0:19:22]** industry as we get more advanced with our AI agents and truly understand what goes into making them production grade there are so many features with pantic AI specifically that are crucial and often overlooked and it's your job as a developer to understand what is needed for these Frameworks make sure you

**[0:19:39]** choose the right ones and also know how to leverage all these things to make things Enterprise level if you appreciated this content I would really appreciate a like and a subscribe and with that I will see you in the next video
