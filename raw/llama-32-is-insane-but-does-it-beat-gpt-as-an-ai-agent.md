---
type: raw-transcript
title: "Llama 3.2 is INSANE - But Does it Beat GPT as an AI Agent?"
youtube_id: E3jO8YLc_CI
url: https://www.youtube.com/watch?v=E3jO8YLc_CI
slug: llama-32-is-insane-but-does-it-beat-gpt-as-an-ai-agent
published: 2024-09-29
duration: "0:16:31"
fetched_at: 2026-07-21
immutable: true
---

## Transcript

**[0:00:00]** just a couple days ago meta released their latest Suite of large language models llama 3.2 and it is super exciting because they released a 1 billion 3 billion 11 billion and 90 billion parameter versions you can run llama 3.2 on a very wide range of Hardware with a big variety of

**[0:00:19]** generative AI use cases and the benchmarks for llama 3.2 are looking really really impressive the 90 billion parameter version is even getting up to the performance of GPT 40 Min and beating it in some ways which is super impressive for a model that you can just download and run yourself the progress

**[0:00:37]** for local llms is really promising and specifically if you have a requirement to use local llms for your use case this is extra fantastic news now local llms have generally not been good as AI agents because they don't do well with function calling otherwise known as tool calling and this is what enables llms to

**[0:00:56]** actually do things for you besides just generating text things like sending emails chatting in slack interacting with a knowledge base that sort of thing and that is really really valuable I can't wait for the day when local llms are actually fantastic as AI agents and can do function calling well so when

**[0:01:14]** llama 3.2 was released I was really really excited to test it out and see if we've gotten any closer to that point whatever local llm is able to First do function calling reliably is going to be an absolute GameChanger and so you and I get to figure out right now if llama 3.2

**[0:01:30]** is that model So today we're going to test out llama 3.2 as an AI agent and compare it to the performance of GPT 40 mini since generally the Llama 3.2 90b version is considered comparable I'll start by very briefly walking you through the custom-coded AI agent that I've created with Lang chain and Lang

**[0:01:49]** graph and then we'll Dive Right into testing out our agents all right so I want to kick us off here by showing you the code that I've developed for this AI agent to test a bunch of different llms and so I've done this with Lang chain and Lang graph and it's a little bit of

**[0:02:03]** a more complex implementation but it's very very robust and I'll go into it in just a little bit of detail here just to spark some curiosity for you but I'll also have a link in the description of this video to a GitHub repo where I have all this codes you can download it

**[0:02:16]** yourself and play around with a bunch of llms just like I'm going to do right here with llama 3.29 B and GPT 40 mini so in the main function here in my python script I'm just defining the streamlet UI so we can interact with our large language model in the browser I go

**[0:02:32]** into a lot more detail with topics like streamlet and other things in this implementation like Lane chain and Lane graph and other videos on my channel so feel free to check those out if you want something much more in depth but I'm going to be pretty brief here so we can

**[0:02:44]** go into testing the llms and then when we get a chat message from the user we're going to call Prompt AI to get our response and this is what actually interacts with our langing graph runnable to stream the response from the llm and so I'll go over to the runnable

**[0:02:58]** here so we can see how everything everything is set up with L graph it's pretty simple overall and so firstly we have this model mapping and this is what makes it so easy to swap in and out a bunch of different models with this AI agent and So based on our llm model

**[0:03:14]** environment variable which I'll show in a little bit we'll instantiate the right chat class from Lang chain based on if it's an open AI model an anthropic model or a model from grock and I'm even going to add support for hugging face in the near future and so going over to the

**[0:03:29]** envir variables here I have an example environment variable file in the repo so you can see how to set up all of your API keys that you need to play with the different models and then also here's where you define your llm model and so my whole script will determine which

**[0:03:43]** service to set up dynamically based on the value that you have here so you don't have to change any code to go from grock to anthropic or anthropic to open AI it is so so easy and that's part of the the whole setup here and so with that I'll just show how the graph is set

**[0:03:59]** up really really quickly so we just set up our chat instance we bind in all the tools that we have that I'll show in a little bit and then the graph is really really simple for the state we're just managing the messages in the conversation and then for the nodes we

**[0:04:12]** just have two we have one to call the llm and get the response and another to invoke any of the tools that the llm wants to invoke and then this router here is going to determine do we need to make any tool calls did the llm ask to

**[0:04:26]** do so if it did then we'll route to the tool node after we get a response from the llm otherwise we'll just route to the end of the graph and return the response to the user and this handles Loops as well so if the llm wants to invoke a tool and then it does and then

**[0:04:40]** it goes back to the llm and now it doesn't want to it would then exit the graph and so it can handle invoking a bunch of different Tools in a loop until the AI agent has done everything that the user asked it to do and then finally for our git runnable function this is

**[0:04:54]** where we create the graph defining all of the edges and nodes pile it together with memory and return it so that we can use it in our other python script where we have the streamlet UI set up all right so that is everything with the llm now I want to dive into the tools

**[0:05:08]** because that's where we can really see what this AI agent can actually do and that will Define how I'm actually going to test llama 3.2 and gbt 40 mini so first of all at the top like I showed briefly we take all these tools that we import from other files and we bind them

**[0:05:24]** into our model and so the different files are right here within the tools directory that you'll see in the repository in GitHub I split the files based on the service and so a sauna for task management Google Drive for file management and then the vector database tools that we have for Rag and that's

**[0:05:41]** just using a local chroma instance because I don't need anything fancy to test llms with Rag and so I'm not going to go into all these tools obviously um but for Asana we have SIMPLE functions here to create tasks to create projects to get tasks in a certain project all

**[0:05:57]** that good stuff and then for Google Drive we can search for files we can create files download files all that just pretty much everything that you want to do for crud in Google Drive searching through folders as well um and then for the vector database tools everything that you need for reg so

**[0:06:16]** we're able to um search for documents query documents and this is what does the similarity search that's the main rag that actual retrieval and then we can add documents to our knowledge base giving a file path and then also clear the knowled base so if we want to empty

**[0:06:31]** it of everything so that we can retest or move on to the next model we can do that with this and so that is everything for the tools and so now what I'm going to do is I'm going to set this up to work with GPT 40 mini to start and then

**[0:06:43]** I've got a couple of prompts that I want to run on it to see how well it does using all these different tools and then I'll do the exact same thing with llama 3.2 90b all right so here I am in a streamlet UI for my large language model

**[0:06:56]** and right now I set the llm model environment variable to GP T4 mini so that is what we are playing with right here so what I'm going to do to test it is just start out with some more simpler tool call requests and then get up to things that are a bit more complicated

**[0:07:09]** and see how much it can handle and gbt 40 mini is pretty impressive overall so I think you'll be surprised the kind of things that it's actually able to do so I'm going to start with a very basic request like what projects do I have in Assa we're going to ask the exact same

**[0:07:25]** things Al llama 3.2 90b when we test it and sure enough it listed all the projects that I have right here coding personal business YouTube and fitness very good all right so next up what I'm going to do is ask it to make a task for me so a bit more complicated because it

**[0:07:39]** has to Define some parameters now if I go into my terminal here for debugging when it wants to invoke the get Asana projects tool it doesn't need any arguments so it's a very basic tool call so now I'll ask it to create a task in my coding project to endworld hunger

**[0:07:56]** with code oh my goodness I can't spell with code by Monday big task but it doesn't care it's going to add it for me and so we'll give it a little bit to make that tool call and there we go it added it in Monday September 30th for

**[0:08:08]** the due date and it gives me a link as well and then if I go into my coding project sure enough this wasn't here before end world hunger with code due by Monday looking really really good all right so let's just keep getting more complicated here this thing is doing

**[0:08:20]** really great uh next up I wanted to actually do something with my Google Drive and so I have a bunch of meeting notes files that I want to search for and download right now so I'll start with get my and then I'll say 823 meeting notes from Google Drive so it

**[0:08:35]** has to download it well first has to search for it and then download it and then give me the path to it locally as well so let's see if it can do everything and yes it is looking really good it's even even gave me the link here which I don't think this will

**[0:08:48]** actually work I'm not going to test that right now because it's just a local file but anyway that's looking good and yeah you can see all the tool calls I doing here it did a search First and it even formatted the search correctly there's some very specific ways that Google

**[0:09:02]** Drive has to uh format the searches in the API and then it downloaded the file once it got the ID from the search so very very good it's using the context from previous tool calls to make the next one so this is looking really nice and so next up um what I want to do is

**[0:09:17]** actually add this into my knowledge base so I'll say add this doc into your knowledge base and that way I can ask questions using Rag and it's going to have the information from this meeting notes in there to answer my question question so boom there we go then I can

**[0:09:31]** say what are the action items from the 823 meeting and yeah we'll go look at the terminal really quick it's really cool to see all the tool calls as they're happening um so yeah add to the knowledge base then it queries with the question gets the response and then

**[0:09:46]** gives it back out to me and this is perfect word for word if I go into my data folder here you can see that this was actually empty before I ran it so it downloaded 823 meeting notes and what we see here matches exactly what we have here so it is working really really well

**[0:10:01]** and so to make this even more complicated for gbt 40 mini I can make a request that would actually require it to download something from Google Drive add to the knowledge base then answer my question all in one and so I can do that by saying what are the action items from

**[0:10:17]** the 8:25 meeting and so in this case it doesn't have it downloaded it doesn't have it in the knowledge base so it has to intelligently know to do all of those and so it says right here it only has access to the 823 meeting bummer but what I can say is uh get it from the

**[0:10:33]** drive and do what you need to do to answer my question so hopefully this will prompt it to download it add it to the knowledge base then do the search with Rag and give me the response a lot going on here but gbt 40 mini is pretty good it can typically do this so yep it

**[0:10:48]** downloaded the file it looks like it's downloading a bunch of files which is really really weird I'm not sure why it did that but it added to the knowledge base and then it queried with what are the ACs from the 825 meeting and got the respon and there we go this is looking

**[0:11:01]** really really good so if I go over here I now have for some reason it decided to download the 825 meeting notes four times I'm not sure why it did that that's kind of weird but anyway it downloaded added to the knowledge base and we got the right answer so this is

**[0:11:15]** looking really really good I would say this is kind of the first time that GPT 40 mini messed up I've never seen like clae 3.5 Sonet or GPT 40 do that kind of weird thing where it downloads the file four times but overall it is really really good as an agent and so now I'm

**[0:11:30]** going to go over to testing llama 3.2 90b with the same questions and seeing how well it does okay so I stopped my streamline instance and I changed my llm model environment variable to llama 3.2 90b and now I'm back up and running using that model for testing I tried

**[0:11:45]** using the other llama 3.2 models like 1B 3B and 11b for function calling but they straight up don't work they won't invoke tools so that is why I'm only using the 90b model here and it's the one that's comparable to GPT 40 mini anyway and so I'm going to start start by going with

**[0:12:00]** the exact same queries that I used for GPT 40 mini so I'll say what projects do I have in a sauna and just like before it's going to list out coding Fitness yep there we go business personal and YouTube that is exactly right and so now I'll follow up with just like before

**[0:12:17]** create a task in coding to create an AI pet startup by Tuesday all right let's see if it can pull this one off for me here all right there we go the task create an AI pet startup has been created Dubai Tuesday and sure enough that looks absolutely perfect so so far

**[0:12:35]** it is keeping up with GPT 4 mini and that is really really exciting because this is the Moment of Truth where we see do we have an LM model that can actually be a good AI agent and so next up I'm going to have interact with Google Drive

**[0:12:46]** and I'll say just like before download my 823 meeting notes from Google Drive let's see if it can actually pull this one off and so I'm going to have the terminal open and we can also watch as the tool calls come in just like before all right so the query came through and

**[0:13:03]** it looks like it is completely incorrect it has name contains and then it doesn't have any actual search term here so it is not looking as good as GPT 40 min and that is a bummer now this is a bit more of a complicated tool because it has to

**[0:13:17]** format the search query in a very specific way but even 4 mini was able to handle this this is kind of disappointing we'll give it a shot and see if it can correct itself here so I'm going to pause and come back after it goes through the loop a few more times

**[0:13:30]** and we'll see if it can hold itself together okay so after a while it failed to make the query and it even told me it needs a bit more information can you tell me more about the file name I should not have to do it when I ask for

**[0:13:43]** the 823 meeting notes and the file is basically just called 823 meeting notes in Google Drive it is definitely failing here so this unfortunately is not looking very good at all and so it seems to be failing with Google drive but I at least want to test it out with rag here

**[0:13:58]** because that's another really important thing and if you just have a use case with rag you can probably still use llama 3.2 but let's figure this out right now so first I'll ask it to clear my knowledge base so that way I just make sure that it doesn't have any

**[0:14:11]** information that it just had previously from when I ran it with GPT 40 mini so there we go I cleared my knowledge base so now what I'm going to do is I can't have it actually download the file from Google Drive determine the file path from it and then add that to the

**[0:14:24]** knowledge base so I'm just going to give it the file path directly so I'm going to go into here and I'm going to copy the path to this file go back in and paste it and say add this to your knowledge base and so this will invoke the function that using the file path

**[0:14:40]** will add it to the vector database and there we go boom the files been added to the knowledge base and so now I can ask it what are the action items from the 823 meeting and so now it should give us the same answer that I did before now that I

**[0:14:55]** have the knowledge in for rag all right there we go look looking good we've got the right answer for the action items from the meeting notes that have been added to the knowledge base so it seems like llama 3.2 overall is looking really good as an AI agent it's not as good as

**[0:15:11]** GPT 40 mini though which is pretty disappointing but llama 3.1 aside from the 405b version of course was unusable for function calling even the 70b version and so this is looking really nice and is definitely a step forward for local llms as AI agents so I'm pretty excited also I just wanted to say

**[0:15:30]** that I did a lot more testing off camera comparing llama 3.2 to GPT 40 mini for AI agents and it really does seem that llama 3.2 is great for function calling better than llama 3.1 but it doesn't quite reach the level of GPT 40 mini so kind of disappointing but at the same

**[0:15:48]** time it still is a huge step forward for these local llms and also there's a lot that you can do to make the dock strings better for the tools make the LM understand it better do some fine-tuning you can really really make it work if you want this demonstration here is just

**[0:16:04]** to show that at a base level gbt 4o mini still does surpass llama 3.2 90b as an AI agent so I hope that you found this video super super informative I'm going to keep doing these as new models come out until we do get to the point where

**[0:16:19]** there's just going to be some open-source model that just crushes it for AI agents if you appreciate this content I would really appreciate a like and a subscribe and with that I will see you in the next video y
