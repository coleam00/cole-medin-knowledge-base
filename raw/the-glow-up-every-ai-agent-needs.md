---
type: raw-transcript
title: "The GLOW-UP Every AI Agent Needs"
youtube_id: 7XZbI_ez8_U
url: https://www.youtube.com/watch?v=7XZbI_ez8_U
slug: the-glow-up-every-ai-agent-needs
published: 2025-01-08
duration: "0:31:12"
fetched_at: 2026-07-21
immutable: true
---

## Transcript

**[0:00:00]** I get asked a lot How I build my fullscale AI agents so I recently started an exciting miniseries showing my entire process and in the series we are building a GitHub agent that can consume entire GitHub repositories for code Q&A and in the last video in the series we took the n8n prototype for

**[0:00:19]** this agent and turned it into a polished agent built with pantic AI but we were still limited to interacting with our agent in the terminal and let's be real that is far from ideal if we want to share our agent with the world and just make it useful in the long run so in

**[0:00:36]** this fourth video of the series we are taking our agent and giving it the ultimate glow up by making it into an API endpoint and then hooking it into a beautiful front end complete with conversation and chat history and we're going to do it in the matter of minutes

**[0:00:52]** how are we pulling it off this fast well in the live agent Studio which is my platform I made for us as a community to build and showcase open- Source AI agents I've created a brand new tool within it as a celebration for the hackathon event called Agent Zero

**[0:01:07]** imagine being able to build and run your AI agents locally and then instantly being able to hook it into a front end for free no complicated setup and no thirdparty hosting required that is what Agent Zero offers you now let me be clear there are a lot of ways to build a

**[0:01:24]** front end for our AI agent and that's what I'm going to be covering in the next video in this series where we'll use bolt. d iy which is our community-driven open- source AI coding assistant to build a fully custom frontend for our GitHub agent and also the API that we build here for the live

**[0:01:41]** agent studio is going to work for that custom front end as well but I specifically wanted to start by having us make our agent compatible with the live agent Studio because I made the live agent studio for exactly this purpose as a guide for us to build our

**[0:01:57]** AI agent into the real world following a lot best practices so it just makes sense it's a super concise and still powerful intro into building our AI agent into something that can actually be productionize as an API endpoint with a front end and Agent Zero is your ticket into using the live Asian Studio

**[0:02:16]** instantly for free and Agent Zero is unlike anything else out there it's free 100% local you can even host superp base to make that local as well and you avoid a lot of the hassle of working with other Frameworks like open web UI that are surprisingly complicated to get your

**[0:02:32]** custom agents working in a front end so if this sounds good to you let's Dive Right In because this is where we really take our GitHub agent and start to turn it into something that we can use in production let's get started all right just like with every other video in the

**[0:02:46]** series I want to start off by going over where we are currently at in this AI agent road map which we are following for the series then we'll dive into the live Asian studio and the super exciting hackathon that we've got going on and then we'll get into turning our GitHub

**[0:03:00]** agent into an API endpoint and hooking it into the studio with Agent Zero if you came here specifically to learn how to build a python agent for the live agent Studio you can skip to this Tim stamp right here otherwise let's dive into this road map and where we are

**[0:03:16]** currently at so the First Step Building any agent you always got to do some planning up front and this is what I covered in the first video in the series and then in the second video which is actually a super exciting live stream that I did a couple weeks ago we Pro

**[0:03:30]** prototyped our agent with n8n we also did a little bit of step three then which is setting up our database and we did that with superbase right here so wonderful platform we're also going to be working with it today doing some more database setup for the live asan studio

**[0:03:45]** and making our agent compatible with that also just following a lot of best practices that we'd want to use in general regardless of if we're making it for the live agent studio and then in the last video in the series the third one we moved our agent to python using

**[0:04:00]** pantic AI so we took our n8n prototype converted it into pantic AI so it's basically all the same functionality but we added some enhancements and just got it ready to make it more production ready and now we're on to step number five in this process creating our front

**[0:04:15]** end and I've got the automator logo here because this represents the live agent Studio which is what we're going to focus on right now and then in the next video in this series we'll be using bolt. DIY to build a custom front end for our agent and I'll also talk about

**[0:04:29]** some other honorable mentions like building a front with streamlet as well but yeah right now we're going to be building for the live agent studio so this is the live agent Studio the platform that I have been pouring my heart and soul into over the last 3 to

**[0:04:43]** four months to make into the perfect place for us as a community to build and showcase open- Source AI agents so you can go to studio. automator doai right now sign up in the top right and you'll instantly have access to all of these agents that you can try right now and

**[0:04:59]** view the source code over in GitHub to learn how to implement yourself and this is Community Driven you can learn how to build an agent for the live agent studio right now and submit it and I'll host it for you it is that easy to Showcase your agent to the world and in this video

**[0:05:13]** we're building an agent specifically for the live agent studio now it's important for me to say that in this video I'm not just showing you how to build an agent for the live agent Studio you're not going to be stuck to this platform it's actually more the opposite you can think

**[0:05:28]** of it as I built the live agent Studio to show you how to best build an agent that you can use anywhere because you turn it into an API endpoint and then you can hook it into really any front end so don't take it as me just pushing

**[0:05:41]** you shoehorning you into this platform this is just an awesome starting point kind of like I was saying in the intro here and so yeah you can build an agent for the studio right now you just have to follow this developer guide which is a bit long but it's only because it is

**[0:05:55]** so comprehensive I have so much here as far as resources to get you started building an agent with some awesome samples that you can use as a template as well and then you build it here and then you can submit it on this page right here uh just following this form

**[0:06:09]** and then I'll host it for you that is it and that's also all you have to do to compete in our hackathon competition so we got $6,000 in prize pool sponsored by voice flow and NN and also open router students you're going to get some free credits for open router when you

**[0:06:24]** register super exciting event that's going on from the 8th of this month to the 22nd we'll have a community voting period as well so you can contribute to who actually wins this competition and yeah the premise is so simple you just build an agent that's compatible with the live agent studio and you can use

**[0:06:41]** Python like what I'm going to show in this video n8n voice flow flow wise anything that you can put in a Docker container as an API endpoint there's just so many options available to you so it's just an awesome event for you to Showcase your AI Mastery to the world

**[0:06:55]** and win some cash prizes we got some awesome awesome prizes here um you can check out all these pages on studio. automator doai but yeah $6,000 prize pool with a lot of different prizes so you don't even have to be first place to get something pretty sweet out of this

**[0:07:09]** event but yeah really really exciting event um got a timeline as well so you can see everything that goes into this event and when things are happening so yeah register for the hackathon I'll have a link in the description of this video and a pinned comment as well and

**[0:07:23]** with that we can get into Agent Zero because this is what we're going to be building our agent and testing with in this video and so we're going to build our agent into an API endpoint and then if I click on the settings model right here this is what you're presented with

**[0:07:38]** when you first go to Agent Zero these are the only four things that you have to give the live agent Studio give to Agent Zero to make it so that you can instantly start talking to your agent with this front end with your agent hosted locally so you just have to give

**[0:07:53]** your super base information including your public key so you're not even giving your super secret super base key it's just your public key and then you give your agent endpoint and the bearer token as well which is optional for authorization for your agent and I have a guide as well if you click on this

**[0:08:07]** question mark that shows you exactly how to set everything up for Agent Zero and that's going to be following the developer guide which we will do as we build our agent so with that being said we're going to dive first into getting our superbase set up and then we will

**[0:08:21]** turn our GitHub agent into an API for Agent Zero all right so this is the code for the GitHub agent that we built in the last video in the series with pedantic AI so we've got deep seek V3 for our large language model that we were using through open router last time

**[0:08:37]** and it's was just so easy to set up our dependencies our system prompt our agent all the tools everything is working very very well with pantic AI and then the last video we built this little CLI script right here so that we can interact with our agent in the terminal

**[0:08:54]** but this is the main problem right now this is just so ugly so it works well like I can test my agent and everything but it just isn't very pretty and so that's what we're going to be doing now building this into an API endpoint and using it with the live agent studio so

**[0:09:09]** it's very very meta but this exact agent that we're brought to build into an API endpoint you can try it right now so if you go to studio. automator doai and sign in you can view the pantic AI GitHub assistant and try it out even without having to download all the code

**[0:09:25]** or replicate what I'm showing you how to build right now you can just go right to the studio and try it out which is super super neat so that's again what I'm going to be doing with a lot of my guides going forward is all the agents I

**[0:09:35]** show you how to build I'll have them available on the studio for you to try instantly and that's one of the benefits of having this being an open- Source platform for all of us to contribute to including myself for the content for you so with that we're going to go into the

**[0:09:51]** developer guide here because we're going to follow this to help us build our AI agent right now so starting off we have a lot of stuff that has to do with the inputs and outputs for our agent and we're going to get into this in a little bit here but the first thing that I want

**[0:10:06]** to focus on is getting our super base set up because it's really important that we set up our database for conversation history for our agent and to show you how to do this completely from scratch I have this old superbase account up right now I'm going to create

**[0:10:25]** a brand new project and create the messages table in there and then use that for the agent in this video so it really is going to be creating something completely from scratch with you right now so I'll say this is going to be uh YouTube test that's my project name I'll

**[0:10:40]** just use the smallest compute size and then my database password uh it doesn't really matter I'll just use a strong password and copy it um and then I'll paste it somewhere else on another monitor uh just because it doesn't really matter I'm going to get rid of this instance after this video cuz I'm

**[0:10:56]** going to show you my API keys and stuff as we're moving forward with this so I'm going to go ahead and create new project and it'll take a little bit to spin up this super base project and so what I'm going to do is pause and come back once

**[0:11:08]** it is done with the setup so our super base project is now set up and we can go ahead and create the messages table that's the only thing we have to do in super base to manage the chat histories for our agent and so going back over to

**[0:11:20]** the developer guide in the live agent Studio it gives us all of the SQL that we have to run so we don't even have to think about how we want to set up our messages table or manage ation history that's one of the benefits of building an agent for the studio is it guides you

**[0:11:34]** through that entire process and so we'll copy the SQL right here go back over to superbase and go to the SQL editor Tab and then we have all of the SQL that we need to run pasted right here the only other thing I want to add is if you take

**[0:11:48]** a look at this note right here it says if you're using superbase you'll also want to enable real-time communication with the messages table which is how we get that instant feedback in the front end for the studio and with Agent Zero and so I'll also paste that in at the

**[0:12:01]** bottom right here and so go ahead and run this there we go success no rows returned cuz we're just creating a table and if I go back to the tables here we now have this messages table that's completely empty also row level security is disabled which we want to keep for

**[0:12:16]** now U cuz that's how we can make sure without authentication we can access this table in Agent Zero but yeah we're good to go we have our table now and we can also go down into the project settings in the bottom left here and go to the API tab this is where we're going

**[0:12:30]** to get our project URL and our Anonymous API key our public key and then our service roll this is our secret key right here so these are the credentials that we need for the rest of this video that's how you find it within superbase so with our superbase setup we can now

**[0:12:47]** dive into the code for creating an API endpoint around our GitHub agent and so we've got a completely blank slate right here we're going to be building this from scratch following the live agent Studio developer guide and everything that we're going to build right now I'm going to have a link to it in the

**[0:13:02]** description of this video to the GitHub repo where you can see all of this that we're building right now and then before we actually dive into the developer guide let's open up the env. example file because we want to set up all the environment variables that we need for

**[0:13:17]** our agent so in the last video we covered our open router API key which you're going to need to access large language models you could set up something else through open AI or anthropic if you want we're just using open router right now and then you can Define the large language model that you

**[0:13:31]** want to use for example this is what you'd set it to if you want to use deep seek V3 like we did in the last video also you'll need your GitHub token so the agent can interact with repos and now we have these new three environment variables so now that we're managing

**[0:13:45]** conversation history in superbase we need our superbase URL our project URL and then also that service key that's the hidden secret key below the anonymous one in the project settings that I just showed you so you get both of these from that same place that I just showed you in superbase in the

**[0:14:03]** project settings and then this API Bearer token this is how we're going to protect our API endpoint that goes into our AI agent obviously we don't just want to have our agent out in the cloud as an API endpoint that anybody can hit because that's going to use our large

**[0:14:19]** language model credit so we want to protect it with a bearer token and I'll show you how to use this later but right now you can literally just set this to whatever you want because this is your own pass that you're creating basically as a password for the gateway to your

**[0:14:34]** agent so that's everything in the environment variables that you need to set now I'm going to go back to the developer guide here because we're going to walk through our sample that we have so if you click on this button right here sample python agent in the developer guide it's going to take you

**[0:14:51]** to if I go down here right here it's going to take you to the sample python agent folder and if I click on Sample superbase agent .p this is the template that we're going to be using to create our agent compatible with the live agent Studio as an API endpoint and so

**[0:15:09]** basically everything that we're about to create is following all this logic right here because it sets up fast API for the endpoint it defines your request and response schema that follows exactly what we're expecting here by scroll down a little bit exactly what we're expecting here for input for the studio

**[0:15:28]** agents and the output all that's defined here we have a function to fetch the conversation history to feed into the agent we have a function to store messages for both the user messages and the AI responses and then we have our actual endpoint here where we verify against the bearer token

**[0:15:45]** that you define yourself we fetch the conversation history and then we format the messages in the way that works for our specific framework and I'll show you how to do that with pantic AI specifically and then we store the user message and then kind of in the middle

**[0:15:59]** here this is The Big Empty Space for you to fill in with all the logic for your agent so this is where we call our GitHub agent based on the user latest message and then we store the response from the AI in the database and handle some errors and that's about it so we're

**[0:16:13]** going to be using this template so going back to the code here we're going to start from scratch but still mostly using what we have there so if you want to build your agent even if you're not building the GitHub agent here you just want to build something else and you

**[0:16:24]** want to do it with python using pantic AI or crew aai whatever use this as your starting point it takes care of so much for you so the only thing you really have to bother with is converting the messages into a format for your framework and then actually making the

**[0:16:40]** call to your agent so let's go ahead and do that now first things first this is going to be an API endpoint so we're using this python package called UV corn which is going to serve our endpoint on our Local Host using Port 801 this is going to be really important because

**[0:16:56]** later when we hook this into Agent Zero we need to make sure we have the port right so we have the complete URL to our agent running locally then we can import all of the packages that we need here most of which we saw in the sample python agent in the GitHub repository

**[0:17:11]** that I just showed you the only thing that's a little different here is we're importing a lot of the different message types from pantic AI because we have to do some of that custom logic to massage the conversation that we pull from the database into the format that our GitHub

**[0:17:26]** agent built with pantic expects and so after that we can load our environment variables everything that I just showed you how to set and then we'll initialize our fast API app this is what we're going to build the endpoint into and then we're going to use a HTTP Bearer

**[0:17:42]** security again to verify against that Bearer token that you set so that your agent is protected and then we're going to add some course policies here now this is pretty basic I'm not going to get too fancy with allowing just specific URLs and things like that but it's important to have this set because

**[0:18:00]** you need Agent Zero to actually be able to talk to your agent hosted locally if you don't have this code right here if it's gone the core's policy is going to block automator doai my platform from connecting to your agent with Agent Zero so you need to have this and then after

**[0:18:19]** that we'll set up our superbase client to connect to our project just based on the URL and the service key and then we're going to create the schema for our request so just like I showed in the developer guide there's a specific format an input that is given into your

**[0:18:35]** agent you have the query that's the user prompt you have a user ID which you won't always have to use same with the request ID these are just available to you if you want the request ID is a you unique identifier for that specific request to your agent and then the

**[0:18:49]** session ID that represents the ID of your conversation essentially so a lot of times you will want to be using the session ID so that's everything that's going to come into the payload for your agent as an API endpoint and then the only thing that it has to return is a

**[0:19:04]** Json with a single parameter and that is a true or false for the success of the call to your agent and the reason why we're not returning the AI response is because we're storing that directly in the database as a part of this which we'll show in a little bit here and so

**[0:19:18]** your actual response to the API call is very very basic then we have a function to verify the bearer token um it's yeah pretty much just checking to make sure that the uh credentials that are given through the header the call to the API actually matches the expected token

**[0:19:37]** based on that environment variable that you set and so we'll use this as the entry point to our API endpoint to make sure that we are protected then we have this function right here to fetch the conversation history and you can kind of tweak this limit how you want so we're

**[0:19:53]** going to pull right here by default just the last 10 messages generally you don't want to pull the entire conversation in case it's super super long you don't want your llm cost to be out the roof because you have a 1,000 message conversation so we're pulling the latest

**[0:20:07]** 10 and then just executing the super base command to get these messages from the messages table that we have already set up in super base and then we're reversing the order right here because we want to actually get the right chronological order where the latest messages are the last one in the list

**[0:20:25]** then we have this function right here to store messages and so this is going be both for user messages and the AI responses um so we we basically just build up the object here and then within the superbase messages table for that specific session ID remember the session

**[0:20:41]** ID is basically the ID of the conversation we're going to store this messages object and that's going to contain the type of message like if it's an AI or human and then also the content of it as well and then there's going to be some default values set like the

**[0:20:56]** timestamp for the message as well now we can Define our API endpoint so this right here this helps Define the URL for our agent so it's going to be local hosts like HTTP backb localhost port and then our port number right here like port 80001 and then this is our URL so it's

**[0:21:17]** going to be SL API pantic D GitHub D agent and we're expecting this payload to come in so we're saying we are expecting these parameters to be available to us which will use throughout our agent and then we are authenticating based on this verify token function that we created right

**[0:21:35]** here so before anything happens in the API endpoint we go through this layer of protection and so first we want to fetch the conversation history based on the session ID that's passed into our endpoint and then we need to create the messages in an array that's in the

**[0:21:52]** specific format that we need for pantic AI and the way that we do that it's mostly this line of code that's doing all the work so I'm not going to get into the detail of why it looks like this exactly if you want to go to the pantic AI

**[0:22:05]** documentation you can take a look at how the conversations are formatted with model requests and model responses and then we have the user prompt right here these are all of our human messages and then we have our AI responses which are just called text part not sure why they

**[0:22:21]** named it like this exactly but yeah basically we're just setting up an array of all of the human messages and the AI responses now it's important to note that this doesn't cover any tool calls or tool responses that part is missing from this cuz I want to keep it very

**[0:22:36]** very simple but later on in this series I will actually expand this to store everything related to Tool calls in the message history as well so the AI can have that context for the conversation going forward but yeah just keeping it very simple right now with just the user

**[0:22:50]** and AI messages and now we can store the user message in the database that just came in through the API call uh just using the function that we defined above and then we'll initialize an HTTP client because this is what we're going to give to our agent so that it can make

**[0:23:08]** requests to the GitHub API so this is going to be one of the dependencies for our agent and so we set up our dependencies right now and again this is very similar to what we did in the CLI so if I actually go to this right here just as an example when we initialized

**[0:23:22]** our agent in the CLI we set up our dependencies in just the same way our agent needs an H P client to interact with the GitHub API and it needs the GitHub API token and so we're setting up both of these in the dependencies here and exactly the same way and then we're

**[0:23:38]** going to interact with it also in a very similar way so in the CLI we have this line of code right here and then in our endpoint it's basically the same so we get the query that came in from the API request so this is going to be exactly

**[0:23:54]** what we stored as the user message right here and then we have the message history that we pulled and then the dependencies that we set up right here so this is going to invoke the agent the agent will call any tools that it needs to analyze the GitHub repo or specific

**[0:24:06]** files in any way and then it'll return the response to us right here and so we're just going to store that in the database as the AI message as the response to the user's request super super basic and so now we're going to just return the agent response and again

**[0:24:22]** because we're storing the AI message here we don't actually have to return the ai's response as a response to the API call we just say if success is true which it is in this case and then obviously when success is false that's when we encounter any error that we have

**[0:24:38]** to handle that's what we do right here so if there's any exception when processing the agent request we store an error message in the database so the AI can actually let us know that there was an error and we don't just see nothing happen in the front end and then we

**[0:24:52]** return the same agent response but this time success is false and that is everything that is all it takes and most of this is just following that template that I showed you earlier um that was in the developer guide for building an agent for the live agent studio and

**[0:25:07]** Agent Zero so super easy so now we have this agent and the only thing we have to do now is run it in the terminal so we have it running locally we have this endpoint hosted locally and then we'll go over to Agent Zero and play around with it there so now over in the

**[0:25:22]** terminal we're going to actually start our fast API endpoint for our GitHub agent and the way that we do this first of all change your directory to the same one that has all the code that we just wrote and now it's just like running any python script so it's Python and then

**[0:25:35]** GitHub agent endpoint dopy and this will instantly start up our endpoint running on Local Host this is synonymous with Local Host by the way with all the zeros and then our Port is 801 just like we specified right here and that is it so now we can go over to Agent Zero and

**[0:25:51]** hook this up and so going back over to my browser here you just have to go to studio. automator doai log in in the top right and now we can head on over to Agent Zero completely for free and hook up our agent so once you click right

**[0:26:04]** here I've already got the Page open with my configuration so when you haven't set your configuration yet you'll immediately be presented with this page where you can enter in all of your information that you need for Agent Zero so the first thing we need is our superbase project URL so going back to

**[0:26:20]** superbase here I will just copy my URL so let me bring that in right here and now we need our Anonymous key otherwise known as our public key so I'll copy that and bring that in as well and then we need our agent endpoint URL and so this is going to be uh HTTP colon back

**[0:26:38]** SLB SL Local Host cuz we're running it locally and then our Port is 801 and then the URL again we just get that from uh if I scroll up to the top right here to our endpoint so it's SL API pantic GitHub agent so I'll copy this go back

**[0:26:55]** over and paste that in boom that is the end point for our agent and then the bearer token this you just have to set to whatever you set for your Bearer token right here so I have this one hidden it's set in myv file it also has my open rouer API key so I don't want to

**[0:27:13]** show this right now so I'm going to pause and come back once I have the bearer token copied and pasted into Agent Zero all right so I've got my Bearer token pasted and as long as this is exactly the same as what you have in your EnV file that will work and then

**[0:27:27]** the other thing that you want to make sure is that your superbase project URL is exactly the same as the one that you have set in uh your EnV file right here and then you need your service key in the agent and then the public key in the

**[0:27:41]** front end so these don't have to be the same but you have to make sure that this is the service key and then this is the public key from the same superbase project CU that's how we can make sure that the front end is talking to the same messages table that your agent in

**[0:27:54]** the back end running locally is also talking to so I'll go ahead and and save all of this and it'll refresh the page and get your credentials set which you can click on this little gear icon in the bottom left to uh change your settings or view them whatever and now

**[0:28:08]** we are in a new conversation and yeah you can also view the setup instructions I showed this earlier in the video as well but this is everything you need a lot of it goes along with the uh developer guide that we saw here as well but yeah you can view the this guide as

**[0:28:19]** well if you want there's some troubleshooting steps as well but that's pretty much it so now what we can do is talk to our agent and it's going to actually run locally so I'll even show the terminal when we make a request we'll see the the requests come through

**[0:28:32]** on my agent running locally right here in my terminal um and so I'm going to copy a GitHub URL I'm actually just going to copy this one so the same GitHub repository where we saw this python uh template I'm going to use this so I'm going to paste this in and say

**[0:28:48]** describe this project all right boom there we go and then I'm going to go over to my terminal here and look at that we are making requests from our studio Studio from Agent Zero to our local agent that we have running using fast API and we got a response it's a

**[0:29:06]** repository by me and it is hosting all the open source agents for the automator live agent Studio python based very very small 112 Stars hopefully a lot more to come created on December 2nd so perfect and last updated today cuz I'm always making updates to this thing I promise

**[0:29:24]** so yeah perfect this is working beautifully we have our agent turned into an API point that we can use instantly with Agent Zero to have this wonderful front end we also have conversation history and chat history um so it's not showing any of this right here because I changed my database but

**[0:29:39]** if I start a new conversation here and say hello and I get a response from my agent which we'll see in a second I can now like toggle between these conversations I can refresh my page and I'll still have these conversations so everything's very permanent and yeah this just takes care of so much for us

**[0:29:54]** with all the conversation and chat management I mean it's not trivial so super super helpful so I hope that you found this useful and then in the next video in the series we're going to take this so much further building a fully custom frontend using the same API

**[0:30:07]** endpoint for our agent and just like that we have turned our humble terminal bound GitHub agent into a full-fledged API endpoint with a polished front end all using the live agent studio and Agent Zero completely for free and this has been a massive step towards building our AI agent into something that is

**[0:30:25]** production ready and at this point you could literally take what we made just now and submit it to the live asent studio to share it with the world and compete in the hackathon that's all that it takes and we're not stopping here either in the next video in this series

**[0:30:39]** we're going to take the API endpoint that we built around our agent and hook it this time into a fully custom front end that we're going to build with bolt. DIY which is our community-driven project which we are building to be the best open- source AI coding assistant

**[0:30:53]** and this is going to be your ticket into building something truly custom if the live asent studio is maybe just a starting point for you so if you appreciated this video and this Series has already taught you a lot about building AI agents I would really appreciate a like and a subscribe and

**[0:31:08]** with that I will see you in the next video
