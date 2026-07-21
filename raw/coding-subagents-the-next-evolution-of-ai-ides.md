---
type: raw-transcript
title: "Coding Subagents - The Next Evolution of AI IDEs"
youtube_id: Ri3iyi3qFlI
url: https://www.youtube.com/watch?v=Ri3iyi3qFlI
slug: coding-subagents-the-next-evolution-of-ai-ides
published: 2025-02-19
duration: "0:26:59"
fetched_at: 2026-07-21
immutable: true
---

## Transcript

**[0:00:00]** these days everyone is using an AI IDE like wind surf or cursor even non-coders to do some incredible things I feel like the king of productivity when I use these tools especially with some of the recent additions like documentation retrieval and Claude mCP support the problem is even though there are a lot

**[0:00:19]** of strengths with these tools there are just as many flaws I mean they hallucinate awful code all of the time even when you give them extensive documentation and instructions ladies and Gent gentlemen it is long overdue that we get a big upgrade for these AI coding assistants to tackle all of these

**[0:00:36]** hallucination problems and I think I've started to uncover what the next Evolution will be for this and I'm not just talking about incremental improvements I talking about a complete Paradigm Shift what I'm about to show you is very very experimental but I truly believe it's going to be the next

**[0:00:54]** wave of innovation for AI coding and it all revolves around specialized sub agents and clouds mCP and I'm going to demonstrate it for you in this video using archon as an example which is the AI agent that I started recently that builds other AI agents using pantic Ai

**[0:01:11]** and Lang graph my two favorite Frameworks now buckle up and just hear me out on this cuz I'm going to get you on the same page as fast as I possibly can the problem right now is AI coding assistants are too General they're the Jack of all trades but also the master

**[0:01:25]** of none when it comes to coding with different Frameworks tools and libraries it doesn't doesn't matter if you give them the documentation for something like a framework that is not enough they're still too General and so that begs the question what's the solution how do we get more specialized here is

**[0:01:41]** the golden ticket that I've started to dream about that I want to share with you in this video imagine having specialized agents that are created specifically to code with a certain tool or framework and these agents can be called upon by the general AI coders like wind surf or cursor when necessary

**[0:01:59]** it's the best of both because sometimes you need that General coder and then other times you need something that knows how to work with the specific framework that you are trying to code with and this is possible right now because you can Define these specialized agents as sub agents that work as mCP

**[0:02:15]** tools that you can bake into all the popular AI coding assistants because claud's mCP is becoming so widely adopted now sound complicated it's actually not and I'll show you exactly how to do it in this video we'll take archon my AI agent build that I mentioned earlier and turn it into one

**[0:02:32]** of these mCP sub agents and then bake it right into wind Surf and you could do this with cursor or any other AI coder so allow me to demonstrate this for you I can guarantee that even though this is very experimental in Alpha it is going to light up your imagination with the

**[0:02:47]** Limitless possibilities that we have here so we're going to dive right into a demo of using archon within wind surf to build us an AI agent and then for the rest of this video I'll show you exactly how I set it up cuz archon originally just started running in a streamlet

**[0:03:03]** interface and I actually show you exactly how I built archon in this video you can check out right here using L graph and pantic Ai and now we're focusing on the next evolution of archon turning it into a sub agent with mCP right here so let's go ahead and give it

**[0:03:18]** our first prompt and so right here I'm saying build me an AI agent using archon that is able to search the web using Brave so just starting with a very basic prompt because archon is still in its infancy here but if you click on the hammer icon here we'll actually check

**[0:03:32]** this out before we send in the prompt I have my mCP servers here which archon is the only one that I have configured at this point we've got two tools we have one to create the thread ID because archon needs some sort of conversation ID to manage the conversation just like

**[0:03:46]** wind surf does and then we have our primary tool to actually invoke the creation of the agent or to work on it if iteratively with that human in the loop feedback loop that I showed in my first video for archon so those are our two tools let's go ahead and send in

**[0:04:01]** this request so the first thing it'll do is call this tool to create our thread ID which is now going to pass into archon for all future calls and so it's going to be using this API endpoint that I created for archon um since that first video as well and so it's making that

**[0:04:16]** first request already you can see that wind surf is waiting for the API request to finish and this will take a little bit cuz archon has that full workflow where it goes through the Reasoner model create that initial scope for the agent and then it goes to the coder agent like

**[0:04:30]** we see right here that performs rag to get the pantic AI documentation combines it all together to create that initial version of our AI agent and then the control is going to get passed back to winds surf in a little bit here once it finished creating the agent so by the

**[0:04:45]** way this is using 03 mini for the Reasoner model right now and then GPT 40 for the actual coder and then look at that we finished our API response right here um for our archon API and now all the code is passed to Wi to then actually create these files for us so

**[0:05:02]** look at how seamless that is it the control just operates so well going between the different agents that we have here and there we go it used the code from archon to build us agent. py and then just like we have archon build out the requirements. text file and then

**[0:05:17]** the tools file and the em. example file it's spitting out all of these because wind surf is really relying on archon here to directed as the specialized sub agent for building pantic AI agents and I'm not going to actually show running this right now but I will show at the

**[0:05:32]** end of this video a full example of building out an agent perfecting it and actually running it and testing it but yeah look at this like was looking at this right here overall the code looks good like we got our agent right here the requirements look good the agent

**[0:05:46]** tool for executing the brave search looks good we got our EMV example file with the brave API key this is looking absolutely perfect just so cool and and I hope you can see that like even though this is a very basic example at this point with both the infancy of archon

**[0:06:01]** and how basic this agent is I hope you can see that you could make so many different kinds of specialized sub agents that you have something like wind surf or cursor call into when necessary and the way that you can tell these AI coders when to use these is just in the

**[0:06:18]** description for these tools like I can tell it like when you want to build a pantic Ai and L graph agent then use archon here are your tools for it and so you have all these descriptions to guide it without having to actually even edit the cursor config or edit the rules for

**[0:06:32]** wind surf you just have it all defined right here in your mCP servers so with any new innovation always comes a lot of questions and I'm sure that you have a couple on this as well so let me know in the comments if there's something I don't cover in this video but I'm going

**[0:06:46]** to try to address a couple of the big ones that I'm sure will come up right now I mean the first big question is why not just use the documentation feature built right into AI coders like wind surf or cursor I can literally go into the bottom right here say at pantic Ai

**[0:07:01]** and then boom I have the pantic AI documentation available which wind surf is going to use to fulfill my next request and I can do at L graph and then boom I've got the L graph docs as well so why not just use this to code my pedantic Ai and L graph agents instead

**[0:07:16]** of using archon and there's two primary reasons for this first of all with the whole agentic flow that we have for archon having the Reasoner model and the system prompts that we have built in we get this very consistent output for the different files that we split our agent

**[0:07:32]** into and just the structure for things in the scripts themselves and we don't get that with wi Sur for cursor you can try to kind of edit the rules and stuff but really it's more than just the system prompt it's the whole flow of archon that produces this very

**[0:07:45]** consistent code I like that a lot and I don't get that with windsurf it produces code that looks very different every single time and that produces some more errors as well and that's kind of the second big thing as well is that the code is always going to be better with

**[0:07:57]** Aron and it might be kind of comparable at this point because archon is in its infancy but as we build it out and add self feedback loops the ability to break things up into different sections as it's building and really split the problem into small steps it's going to

**[0:08:12]** be so much more robust than just having a general coder spew out all the code at once and then improve on it from there it's just going to be more of a one shot and then just make it more robust you're just going to have such a better

**[0:08:24]** starting point using something like archon and the way that it can leverage the documentation better as well so that's why we care about using archon and then the second big question is why are we generating This Thread ID here I mean it's kind of weird like mCP servers

**[0:08:38]** are supposed to be stateless right like you call the tool and then the tool gives you a response then forgets everything but in this case archon is a sub agent tool that actually maintains the conversation history just like winds surf does here's the Lang graph graph that we have for archon and all of this

**[0:08:57]** like this is stateful we have the Reasoner that creates the scope and that goes to the coder agent and then we have this human in the loop where we can actually ask it to iterate on the agent so it has to maintain the conversation using some sort of identifier to know

**[0:09:10]** that this wind surf conversation maps to this run of archon that is iterating on an agent and so we have this thread ID that it creates and the llm has to remember to pass that in to the tool so it has to keep track of this thread ID

**[0:09:25]** which is a little bit uncomfortable that we rely on the llm for that but this has actually worked 100 % of the time for me surprisingly and so then in any future iteration where we maybe tell it to use archon again to improve the agent in some way it'll then use the same thread

**[0:09:39]** ID so that it's invoking that execution of archon going on to kind of that next step in the human in the loop feedback loop that we have here that's how I use the thread ID again kind of forced a little bit into mCP but it works pretty well and so yeah I'm kind of at the

**[0:09:54]** Forefront of innovation like I haven't seen anything like this and so definitely trying to just figure everything out as I go right here but getting some really cool results and so with that let's dive into mCP a little bit talk about archon and I'll show you how I brought everything together the

**[0:10:08]** sponsor of today's video is fish audio an extremely impressive voice cloning and voiceover solution that is transforming the way that developers marketers and content creators create audio with AI and fish audio is not just another speech to text tool it is a state-ofthe-art realtime speech to speech model that delivers top tier

**[0:10:29]** realism let me show you a demo really quick now from the fish audio homepage you just go to my voice Library custom voice and then build a new voice and this is where you can clone yourself in just minutes you add in your cover image name and description then at the bottom

**[0:10:42]** here is where you add in your sample clips for it to mimic you recommended around 30 seconds and you can even record yourself right here in the UI so they make it very easy for you so go ahead and click on create in my case I'm just going to use the custom voice that

**[0:10:55]** I already have built here I'll paste in my kind of silly sample prompt I have here saying archon is the best best AI agent Builder also a pro tip you can change the spelling of things a little bit just to help it enunciate better and all of this is accessible through their

**[0:11:07]** API as well if you want to use it programmatically so you can change the speed and volume as well and then click on Create and then just a few seconds it'll generate our audio clip and play it for us archon is the best AI agent Builder that ever was and ever will be

**[0:11:21]** don't believe me well why wouldn't you fish audio is designed to do it all YouTube voiceovers voice agents adding multiple languages to your projects you name it and at the same time it is super affordable 50% cheaper and two times faster than 11 Labs which has been the

**[0:11:38]** go-to voice platform for a while now even though it's always felt very overpriced to me so it definitely seems like fish audio could be taking the crown as the go-to AI voice platform to say I'm impressed while testing out fish audio is saying the least if you are

**[0:11:54]** ready to level up your AI voice game and make your project sound truly professional head on over to f fish. audio sign up for their generous free trial and experience the magic of their AI voice cloning for yourself I mean you can literally try it out in under 2

**[0:12:08]** minutes so definitely give it a go see how well it works for you and I'll have a link in the description to fish audio as well so the most important thing for me to start with as I show you how I built archon into an mCP sub agent is to

**[0:12:20]** give you some context around what mCP is what archon is and how I can combine them together to build this very specialized agent so first of all mCP it is a protocol developed by Claude pretty recently here just a few months ago to standardize the use of tools with large

**[0:12:36]** language models so they have this full article that you can read if you are curious but essentially it's a way where you can create these servers that you spin up that have access to API endpoints for a certain service like GitHub Google Drive Discord whatever it might be and so essentially This Server

**[0:12:54]** is exposed to a large language model to give those tools dynamically to an l M so when you spin up an mCP server for GitHub and then give it to your llm in Wind surf or claw desktop or whatever the llm can now do things on your behalf

**[0:13:09]** in your GitHub repositories it is so cool how fast you can spin up these servers and then instantly give llms access to do all these things for you there's a server for brave search there's one for Google Drive for your SQL databases there's all these third party servers that are created by the

**[0:13:25]** community kind of like archon is going to be now so you can do things uh with the jet brains or stripe or you got AWS S3 uh if I scroll down a little bit we've got Discord deep seek R1 all of these are servers that we can download

**[0:13:38]** right now they're all open source I can run them on my computer or reference some API endpoint in the cloud and then boom all those tools will now be available for my llm wherever I'm running it and so that's what we're doing with arcom so arcom is an AI meta

**[0:13:52]** agent it is an agent that builds other agents using pantic Ai and L graph so I've been building it out started very recently I only have one video on my channel on it so far but essentially I'm developing an inations to teach pantic Ai and L graph and then also eventually

**[0:14:06]** to build it into a very robust sub agent that we can use in AI coders to build these agents with pantic AI L graph very very nicely and so what I'm doing right now with mCP is turning it into a tool that we can give to llms like we just

**[0:14:23]** saw we did in Wind surf so essentially claw 3.5 Sonet running in Wind surf has archon as a tool and so this is the Lang graph graph that defines the full workflow for coding agents with archon so we have the Reasoner at the start that kind of defines the scope for

**[0:14:40]** building the agent and the high level reasoning and that goes into our faster coder agent which actually produces the code and then we have this feedback loop right here getting input from you as the user so it can iterate on the agent and then it gives the final response and

**[0:14:53]** instructions to run the agent at the end and so we package this entire workflow together to give as a tool to AI coders that is the power of using archon as an mCP sub agent and so now kind of with that as our context here I'll actually dive into how I set up the mCP server

**[0:15:11]** and hooked up everything with archon so this is the python script for our archon mCP server I'm going to go over it at a high level right now might do a future video on my channel where I really dive into building a python mCP server from scratch but also I'll have the links to

**[0:15:26]** the documentation in the description if you're curious to dive into that yourself you can make servers for both Python and JavaScript so at a high level here we're using fast API with the mCP python SDK we have our first tool right here to create that thread ID again

**[0:15:41]** because archon needs that to manage the conversation history and then we have our second tool to actually invoke archon itself and the way that we do that is through an API endpoint that I created for archon so this is new to version three of archon as well we have

**[0:15:57]** this fast API endpoint that I created um that is interacting with archon in a very similar way to how we did with streamlit in the last video on archon on my channel and then the graph for archon that I showed in the last video how to build completely from scratch this

**[0:16:14]** remains entirely the same so there's nothing that I Chang in here we're just wrapping it all up in this API endpoint with fast API that I'm then calling right here in the mCP server so it's a nice and simple implementation where we don't actually have to use archon as an

**[0:16:30]** mCP server now I'm remaining flexible for you where you could still work in streamlit or use this as an API endpoint and some other front end that you make for archon you don't have to use it as an mCP server but I still make it very easy to do so as well and so actually if

**[0:16:45]** I go into the read me here let me just open the preview for this um the updated instructions for archon I show you actually how to run this both without the uh mCP server setup uh so if you want to just do it with streamlet or with mCP so I covered both of these I

**[0:17:02]** got these instructions right here in the REM me to set up everything very very easily so you can play around with this yourself in Wind Sur for cursor or streamlet or wherever um then the other really important thing that I want to hit on for this mCP server the way that

**[0:17:16]** it works in general these dock strings that we Define at the top of our function definitions this is very similar to Tools in pantic Ai and laying chain these actually tell the llm when and how to use these tools so this exact string that I see right here I'll go

**[0:17:34]** back over to wind surf I'll show you this look at that it is right here so the definition of the function this string right here is actually put into the prompt for CLA 3.5 Sonet in Wind surf so that it understands when and how to use these tools and so I can give

**[0:17:50]** Specific Instructions here like for example telling Claud that before it can run archon it needs to generate a thread ID if it's the start of building building an AI agent and then if it's not the start needs to pass in the same thread ID so archon is managing that

**[0:18:05]** conversation cuz obviously it won't run if there's not a thread ID yet it has to pass that in as one of the parameters to this tool when it runs archon so that is the mCP server as a whole again nothing changed with the graph very simple fast API implementation don't need to dive

**[0:18:22]** into this overall and then I also have this neat little script that I have created I have this in the instructions as well but it'll completely set up your virtual environment for you and it'll even generate the mCP config to put into cursor or wisor so I actually pop up my

**[0:18:38]** terminal here I'll even show you that so this is the API in point that we have running right here but if I stop this and I run the command Python and then setup mCP dopy my virtual environment is already created so it skips that step but then look at

**[0:18:53]** this it gives me my configuration that I'd have to put into cursor instructions for that in the readme and then it also gives me the Json to put in the um the config for mCP in Wind surf or something like Claude desktop as well so you run this script you know exactly what to do

**[0:19:09]** to set up your archon mCP so I make it as simple as I possibly can for you all right so really quick let me show you how to run everything then we'll build an agent from scratch so going back to the read me here which again is just at

**[0:19:21]** the root of the GitHub repository we have our installation instructions and so if you're doing it the old way just interacting through streamlet and not as an mCP server again that is still supported then you can follow these commands right here so you just clone the repo activate your virtual

**[0:19:36]** environment install all your requirements then if you're using through mCP you can run this setup script that I showed earlier which sets up your virtual environment gives you your mCP config and then you want to activate your virtual environment as well and then I have instructions for both wind Surf and cursor how to include

**[0:19:52]** the config that the setup mCP script gives you and it'll be the same or at least very similar to one of these two if you're using something else like claw desktop or some other AI coder that supports mCP and then set up all your environment variables all of this

**[0:20:06]** remains unchanged same thing with running this python script here to actually get the pantic AI documentation and then put it in the super base knowledge base for Rag and then using mCP servers you'll run the API endpoint to expose archon as an API otherwise you can just use streamlit directly because

**[0:20:24]** that interacts right with the graph instead of going through the API like we do with m CP so that is everything for running I'm not going to go through all these commands right now um cuz I hope it's really clear for you so I have this all up running on my machine already so

**[0:20:37]** now we're going to go ahead and actually test it all out because now we have the full archon graph packaged together as a tool for wind Surf and I also want to reemphasize like super important for you to know that like this really is just in the first stages of development I'm

**[0:20:55]** going to add so many more nodes and improve system prompts and add in a tool Library like so many ideas I have to make this really robust but even this is a good starting point so let's go ahead build an agent from scratch iterate on it and test it out so I thought it would

**[0:21:07]** be fitting to take the brave agent we started at the beginning of the video and see that through to completion for our final demo here so I am building it from scratch but using the same prom so I've got the API endpoints spun up for archon right here graphs service. I'll

**[0:21:21]** show the logs for that so you can see things happening in real time as we build the agent so I'll paste in the same prompt here use archon to make an AI agent so first it gets the thread ID now it says It'll ask archon for help I

**[0:21:33]** just love that like it just shows it like this is an agent asking another agent for help a sub agent when it knows it has the expertise it doesn't and so starting with our Reasoner model 03 mini it's creating that scope which also includes the pantic AI documentation

**[0:21:46]** Pages it thinks the coder should look at which it goes ahead and does so pantic AI coder performing rag getting all the contents here to create our AI agent based on the pantic AI documentation and I will be expanding to work with Lang graph later as well but just starting

**[0:22:02]** very simple here with archon so now it's generating that final response wind surf is still waiting for it but in just a little bit here we'll see it Flash and then yep there we go all right so now we got the final response from archon and it's going to take those files and

**[0:22:16]** Implement them into my IDE here so starting with the requirement. text okay looks pretty good pantic Ai and httpx definitely only dependencies that we do need here and then we have our agent okay that looks pretty pretty good it says the model is none which I don't like that so it looks like it's pretty

**[0:22:33]** good overall I mean the brave Search tool looks good okay like that and then we have our envi example file for the brave API key looks good looks like we'll have to implement an llm here but everything else looks good so I'm going to accept these changes but now I'm

**[0:22:48]** going to use human in the loop because I want to let me actually move myself here so you can see me typing right here I'm going to ask it to fix the first big issue that I see here because model is none so I'm going to say ask archon to

**[0:23:02]** fix the model for the brave search agent right now the model is none and I want to use GPT we'll just say GPT 40 so now it's going to use that human in the loop here and so it's going to invoke archon using the exact same thread ID so now

**[0:23:21]** going back over to the logs here it jumps right to the uh yeah right right to the pantic AI coder so it didn't invoke the Reasoner this time because we are already within the graph execution within that loop with just the coder agent so we got the response back from

**[0:23:36]** Aron and now it edited the model so open AI GPT 4 and it should probably be GPT 40 so I'll just go ahead and edit this right here you still want a little bit of human intervention especially because archon is such a new implementation at this point but still really cool we

**[0:23:53]** could see there that it actually use archon to then update the agent and obviously this is something that that wind surf probably could have done itself but I just wanted to give it really simple example here for human in the loop with Aron and so yeah this is

**[0:24:05]** looking pretty good what I'm going to do right here is test this off camera fix up any little glitches that I have here and then we'll go ahead and run this with a streamlit interface so I'm back after fixing just a couple of things it did not take much to get this to a

**[0:24:17]** working State and I'll even show in a streamlet interface that I made really quick for this agent everything working perfectly so the main thing that I had to fix obviously besides getting everything with the environment variable set up cuz I had to create a EnV and then it wasn't using that in my agent is

**[0:24:33]** it didn't really have the right URLs and parameters for interacting with the brave API so in the end it didn't actually mess up with things related to pantic AI or Lan graph it was a hallucination with the brave API which I didn't give the documentation for so can't really blame archon it would have

**[0:24:50]** been the exact same thing with wind surf that's why a tool library is going to be so useful so I could have like a pre-made Brave tool that it would just pull and use right there for the pantic AI agent so that's all I had to fix up

**[0:25:02]** everything else I kept exactly the same and so then I created the streamlet interface that I just ran right here with command streamlet run and then streamlet ui. piy obviously added that as dependency for the project as well and then boom we now have this chat interface right here for our agent that

**[0:25:18]** was almost completely generated by archon with wind surf just calling it for the help to make this agent so I can ask it a question like what is the net worth of Elon Musk the kind of thing an llm wouldn't know by itself because of its training cut off so it's going to be

**[0:25:34]** leveraging the web search tool here which it did you can see right here in the logs that it made the request to the brave API for his net worth and there we go $400 billion which is absolutely insane but the right answer so there we go our archon agent is working perfectly

**[0:25:51]** and we're just going to keep building out archon as an mCP server doing some crazy things with it it's going to just keep getting better and better now that archon can be integrated into AI idees as an mCP server I have so many ideas to turn this into a massively powerful sub

**[0:26:08]** agent to create other agents with my favorite Frameworks I just love that I can run wild with the agentic flow for archon and not have to worry about the logistics of having to actually create and edit files because the AI coders just take care of that for me now so

**[0:26:23]** check the GitHub readme that I have Linked In the description for all the future plans that I have for archon or at least some of them I mean I've got so many ideas in my head I've got things like self feedback loops or breaking down the agent creation down into

**[0:26:36]** smaller steps a tool Library so many insane ideas and if you have more suggestions yourself or if you want to contribute definitely feel free because archon is a community-driven project so if you appreciate this video and you're looking forward to more things AI agents and archon I would really appreciate a

**[0:26:53]** like and a subscribe and with that I will see you in the next video
