---
type: raw-transcript
title: "No Code RAG Agents? You HAVE to Check out n8n + LangChain"
youtube_id: Xifzdn7zW3A
url: https://www.youtube.com/watch?v=Xifzdn7zW3A
slug: no-code-rag-agents-you-have-to-check-out-n8n-langchain
published: 2024-08-25
duration: "0:17:47"
fetched_at: 2026-07-21
immutable: true
---

## Transcript

**[0:00:00]** building Advanced AI agents with rag is definitely not something that's limited to complex and custom coded applications today I'm going to show you how to use my favorite workflow automation tool n8n along with my favorite library for AI development Lang chain to build a full-blown rag AI agent using my Google

**[0:00:20]** Drive as my knowledge base so the agent can answer questions using the documents that I upload and when I say no code I mean that today we are literally going to write zero lines of code to build our AI agent and don't get me wrong I love to code my own agents but I would be

**[0:00:36]** dumb to code them myself every single time when a lot of the times I can make them very simply without code using n8n n8n is a workflow automation tool similar to make.com or zapier but it is way better because you can self-host it so you don't have to pay hundreds and

**[0:00:52]** hundreds of dollars a month like I did at one point for zapier and you can scale it infinitely so definitely more on that in a future video but on top on top of that which already makes n8n amazing it integrates directly with Lang chain so it is so so easy to build AI

**[0:01:07]** agents that are really powerful with tool calling and rag just like what I'm about to show you now so without further Ado let's get right into the meat of it and see how easy it is to build a rag agent with no code all right so I have

**[0:01:21]** already fully built out these NN workflows for my rag AI agent because I just want to walk through it with you very very smoothly to give you a lot of value very quickly you can also steal these workflows from me if you want I've got a link to a GitHub repository in the

**[0:01:34]** description of this video so you can download these workflows as Json files and then you go into your own n8n instance in the top right here you click on the three dots and then import from file and in seconds you can bring in this entire workflow into your own n8n

**[0:01:48]** instance so you can take this further and build something amazing with Rag and so with that we can actually dive into what this workflow looks like so just like with make.com and zapier every workflow in N an is made up of two four parts you have your triggers which is

**[0:02:02]** what starts these workflows and then you have your actions the nodes within the workflow that actually do things like interacting with AI or your Google drive or your vector database whatever it might be so the trigger for this and and workflow is a chat input so when chat

**[0:02:17]** message received if you click into this the options are quite simple you just give authentication optionally then also the initial message that's going to be there in the chat widget for the user when they first click on it to interact with the agent in a chat bot and then

**[0:02:31]** when you add this as a trigger to an NA end workflow you're immediately given this option in the bottom middle here to open up a chat window and this is one of my favorite Parts about n it makes it so easy to quickly test your AI agents because you have a chat window directly

**[0:02:45]** in the UI to test things out as you're iterating on the prompt or the tools or the vector database whatever it might be so this just makes it so easy to test things and iterate on things and so we'll even be looking at this later when I give a demonstration of this AI agent

**[0:03:00]** with Rag and so we have our trigger here that I just covered and when there's a chat message that comes through it flows immediately into our rag AI agent which is a tools agent that uses Lang chain under the hood and so the way that I know that this uses Lang chain aside

**[0:03:15]** from just the documentation telling me if I click on the plus icon here to add a new node to the workflow and I search for Lang chain sure enough AI agent which that's the node that I chose here is the second option and this just does everything for me I don't have to code

**[0:03:30]** anything to have my tools my memory and my chat model if I want to get more custom with it I can use the Lang chain code node to actually code things if I want something more robust that maybe no code can't do for me because no code can't do everything but it can do most

**[0:03:46]** things and so with this use case I can just use the AI agent from laying chain here and it's got everything for me it's got the chat model so I'm using open AI in this case and I can use any model that I want it's really easy to set up

**[0:03:57]** my credentials as well I just need an API key and then also if I wanted a different chat model I can click on this connector here I could use claw if I want to select anthropic I could use grock for llama 3.1 I could use ol llama um open

**[0:04:12]** AI like I already have selected pretty much everything that I actually care about is here already and so even if there's something else like if I wanted to use fireworks for example maybe I could set up custom code here but for most cases I'm happy with everything here so it is just amazing no code

**[0:04:28]** needed for all these Integrations and then also for the chat memory there's a lot of options for that so I'm just using chat memory which is basically going to be stored locally on my n instance um but there are other options as well so if I click on the memory

**[0:04:40]** connector here we could use something like postgress chat memory so having a SQL table that manages all the conversations or using reddis for example a lot of options here as well and then for the tool calling the best part of the AI agent where we actually have the rag integration there are a lot

**[0:04:59]** of options for Tool as well so if I click on this connector there are a lot of custom tools that are already provided for you like a calculator or a vector store which is how I actually retrieve the documents to answer questions with rag um and then my

**[0:05:13]** favorite part is you can literally call any n8n workflow as a tool and so you set up a workflow to do something like interacting with Google Drive and a multi-step workflow which I'll show a little bit and then you just tell the AI agent how to use this workflow like what

**[0:05:28]** parameters to give and then also you tell it when to use that workflow just like you would with any tool that you might Define in custom code and so you can literally have all the power of any na workflow you want even if there's a ton of steps there just packaged as a

**[0:05:42]** neat little tool that you can just shove onto your rag AI agent and so yeah just really cool stuff um and so there's two tools that I have here for this agent the first one is that built-in Vector store tool where I retrieve the documents based on a user query um to

**[0:05:58]** answer a question or something like like that and so I add this on as a tool that's connected here and then it asks me to supply a vector store and so I'm just using an in-memory Vector store so similar to my chat memory it's going to just be stored locally on my n8n

**[0:06:13]** instance so there'll be like files that are there on the server that I am hosting my n8n there are other options as well though so you could use um for example a sua base Vector store or a pine cone Vector store uh if you want my recommendation I would actually highly

**[0:06:27]** recommend to go with super base here and the reason that is if I go back to the chat memory here this is just a nice little gold nugget for you here uh you can use a super based postgress table for your chat memory and then you can also set up a superbase vector store so

**[0:06:43]** you can have everything managed for your Rag and your chat memories all within one place in super base so that's my recommendation if you want to take something like this to production but just for a quick demonstration purpose here I'm running everything locally for my memory and my Vector store uh and

**[0:06:59]** then for your embedding models there's a lot of options for that as well I'm just using open AI for my embeddings as well so same credentials and then I'm just using the text embedding three large model uh from open AI for my embedding so that's what actually takes the

**[0:07:12]** different chunks of documents that I put into my Vector database and turns them into vectors for retrieval later um and then on top of that I have a model that's associated with this tool to retrieve information so I'm just using the same uh GPT 40 mini here as

**[0:07:29]** well um because you're going to get the documents from the vector database and you need a large language model to process that and pick out the right information and so I'm using GPT for that again as well so that is everything for the rag retrieval the actual retrieval part of rag now to put

**[0:07:46]** documents in the vector database knowledge base I have another tool here and this is a NN workflow as a tool like I was mentioning earlier and so the way that my chatot works here and you could take this in a milon different ways is it's going to start out with nothing in

**[0:08:03]** the vector database but I have infinite access to my Google Drive so I can talk to my AI chat bot and say I have this file in Google Drive I want you to add it to your knowledge base for future reference and so what it's going to do

**[0:08:16]** for this tool here is I have a little description that says use this to search for a file in Google Drive so the user might say I want my meeting notes from last week to be added to the knowledge base so it'll search for those meeting notes in Google Drive download it and

**[0:08:31]** add it to the vector database knowledge base for future querying so that's the description to tell my AI agent when to use this tool and then I have parameters so in a Json example here I tell the AI agent what parameters to give this workflow so that it can execute properly

**[0:08:46]** and so in this case I'm just giving one parameter here which is a query how are you going to search Google drive to find that file to download and then add to the vector database very very simple couple of other options here like the workflow ID so this tells it what

**[0:09:01]** workflow and na end to actually execute for this tool and then also the field that's going to be outputed from that workflow that you want to use as the response that would then tell the large language model what happened when it invoked that tool very very simple stuff

**[0:09:15]** and so the workflow that I have for this is actually this one right here so it starts out with a web hook and so this gets the query and then it passes it into the Google Drive and so let me click into this and show you it's going

**[0:09:30]** to search for a file or a folder based on the query here and so if you search for um 822 meeting notes for example it would find that word doc file that has those meeting notes in your Google Drive and then on the next action it's going to download that file then after it

**[0:09:48]** downloads it it's going to extract the text from that file and so now at this point in the workflow I have all the text from that file that I've downloaded from Google Drive and I can now put it into my Vector database so it's added as the knowledge base so the AI agent can

**[0:10:03]** use that to answer questions later and so for this I'm just using the same user documents memory key so the way that I retrieve my documents is using this memory key and the way that I insert documents is also using this key otherwise those two things are not going

**[0:10:17]** to sync up um and then it's kind of a similar setup here where I just have to choose my embeddings which I'm going to use gbt 40 or not gbt 40 that's for the llm I'm going to use the text 3 large and beddings from open Ai and then I

**[0:10:31]** have a default data loader so this is going to basically Define how I take my text and put it as vectors in my Vector database and so I'm going to split into chunks basically just using a 1,000 chunk size text splitter so all the same kind of stuff that you would see if you

**[0:10:48]** were to code a rag agent yourself um but you have all the power and customization still within n with absolutely no code and so I'm not really losing out on much here doing it in a workflow with no code which is the best part of it um and so

**[0:11:02]** with all this together I can now test this out a little bit so let me show one quick thing here I'm going to go to a couple of files that I have here for rag I've got two meeting notes Here one from 822 and one from 823 and these this is

**[0:11:18]** just fake data that I made up just to have something here for rag um and so what I'm going to do is I'm going to tell my AI agent to add these to its knowledge base and then I'm going to ask a question that could only be answered

**[0:11:31]** when it has this in its knowledge base so I'm going to go back to my rag agent here I'm going to save it and then I'll go to the chat window in the bottom middle and first I'm going to ask it a question that it shouldn't know at this

**[0:11:41]** point because it doesn't have these meeting notes in its knowledge base I'm going to say what are the action items from the meeting on 8:22 and it's going to take a little bit to get a response try to find it in the vector database and sure enough I don't

**[0:11:56]** have access to that specific um folder or that specific file right here and so I'll say okay cool uh find the 822 meeting notes in the drive and add them to your knowledge base I don't have to get really specific in my quest like this but I'm just doing it right now to

**[0:12:17]** absolutely make sure that it works for a good demo here and there we go and that was like super quick too which is also a really huge plus with na it is as fast so I have successfully added the meeting notes to my knowledge base so now I'm

**[0:12:28]** going to ask the exact same question here and this time it's going to have an answer and it's going to be based on this file that we have here so the action items from the meeting on 8:22 R plan a budget make a bunch of money everything that we have exactly right

**[0:12:41]** here in our Google drive file so I proved that it didn't have this information before I showed in real time how I was able to add it and then get an answer from this document and the reason you might want to do it this way the other way you could do it is you could

**[0:12:54]** just feed in every single file in your Google drive into the vector database automatically like every morning or every hour something like that and then that would be there automatically in the knowledge base um but that when you do it that way sometimes your vector database can get bloated by a ton of

**[0:13:09]** files that you don't necessarily want to have available for Rag and so this way I have control over exactly what I give to my agent to have knowledge of later on when I want to reference something again in a conversation like maybe to remember something like the action items here so

**[0:13:24]** that's why I have it set it up this way um but yeah there are a lot of ways that you could do this the best part about n is however you want to do it you can do it very easily in these workflows like it was it just took minutes to create

**[0:13:35]** this workflow to find a file in Google Drive download it and put it in the vector database but you could set up something similar that you'd run on a schedule basis to uh maybe pull files from a specific folder and constantly hydrate your vector database with those files there's a ton of things you could

**[0:13:49]** do U so it's very very powerful stuff the one thing that I wanted to mention is that I have a second workflow involved here and that is simply a workflow to call this web hook so there's kind of a little issue with naan that's unfortunate but I found a really

**[0:14:07]** solid work around here when you have a tool that references a workflow ID you can't reference the workflow ID of the workflow that has the agent so I can't just take what I have right here is my workflow ID and dump that in here because it gives some weird errors

**[0:14:24]** saying that there's like not credentials or something like that so you have to reference a separate workflow so I just have this workflow that then hooks right back into um this web hook within my original workflow um and the reason you need to do that is because in

**[0:14:39]** my in-memory Vector store here my memory key it says here that it's prefixed by the workflow ID to avoid Collision so if I am inserting into a vector database in a different workflow it's going to have a different memory key because it's prefixed by a separate workflow ID so I

**[0:14:54]** have to have my retrieval be the exact same workflow as I have the insertions the data insertions into the vector database otherwise they'll be prefixed by different workflow IDs and so that data won't actually be available for the agent so it's like a really really technical thing that I just had to solve

**[0:15:11]** but I have it solved for you now and so that's why there'll be two workflows in the GitHub repository um but yeah it's just like a tiny little thing that you had to do unfortunately um but however if you were to use um a production Vector database like super base then you

**[0:15:26]** would't have to worry about this because when you set up a a supera base Vector store here as the tool for the regag AI agent you get to define the memory key in a more Dynamic way where it's not going to be prefixed by the workflow ID that's something that's just done for

**[0:15:40]** the inmemory vector store so you wouldn't have this issue and you could actually have this whole tool to add a Google drive file to a vector database as that separate workflow instead of having this weird workaround where you need to invoke this separate workflow that just hooks then right back into

**[0:15:55]** this part of uh this whole workflow setup that I have here so I hope that makes s it's all Built For You at this point so now you can just take these workflows that I have steal them for yourselves and expand upon this to make the vector database production or to add

**[0:16:08]** more tools or to improve upon the rag or the prompts whatever you want to do this is yours to play around with no code at all and you can even embed this in a website so I'll show that really quick as well just to give you a lot here so I

**[0:16:21]** can take um the embed so I go to more info right here uh when I open my chat window and I know that this is code we didn't have have to write any code though and you don't have to know code to be able to embed this you can just

**[0:16:33]** take this right here copy it you and you can go over to your website I'm just going to go to an online HTML editor here you can paste it in here and then when I click run I have this chat widget in the bottom right like you see on a

**[0:16:46]** lot of websites where I can click into this and there we go we've got our chat bot now and I can say something like Hi how are you and then after it gives me an answer super super fast um I can say what are the action items from 820 too

**[0:16:59]** and so that's going to again reference the document with rag giv me the answers because I've already inserted that into the vector database super cool um so yeah that's pretty much everything for this workflow um I'm definitely going to be making more videos on rag with NN in the

**[0:17:14]** future because this is super powerful stuff and one thing that I'm probably going to do is also focus on super base and getting things deployed in production so if you're interested in that let me know I would really appreciate knowing just so I can know that that's something that you want to

**[0:17:28]** see and then uh I'll probably make a video on it so yeah more on rag to come I hope that you found this useful and that you're able to build really cool things with Rag and N using this as your foundation if you found this helpful I would really really appreciate a like

**[0:17:42]** and a subscribe and with that I will see you in the next video
