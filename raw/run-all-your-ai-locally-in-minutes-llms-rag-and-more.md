---
type: raw-transcript
title: "Run ALL Your AI Locally in Minutes (LLMs, RAG, and more)"
youtube_id: V_0dNE-H2gw
url: https://www.youtube.com/watch?v=V_0dNE-H2gw
slug: run-all-your-ai-locally-in-minutes-llms-rag-and-more
published: 2024-09-15
duration: "0:20:21"
fetched_at: 2026-07-21
immutable: true
---

## Transcript

**[0:00:00]** have you ever wished for a single package that you could easily install that has everything you need for local AI well I have good news for you today because I have exactly what you are looking for I have actually never been so excited to make a video on something

**[0:00:14]** before today I'm going to show you an incredible package for local AI developed by the n8n team and this thing has it all it's got old llama for the llms quadrant for the vector database postgress for the SQL database and then n8n to tie it Al together with workflow

**[0:00:31]** automations this thing is absolutely incredible and I'm going to show you how to set it up in just minutes then I'll even show you how to extend it to make it better and use it to create a full rag AI agent in n8n so stick around because I have a lot of value for you

**[0:00:47]** today running your own AI infrastructure is the way of the future especially because of how accessible is becoming and because open-source models like llama are getting to the point where they're so powerful that they're actually able to compete with close Source models like GPT and clad so now

**[0:01:05]** is the time to jump on this and what I'm about to show you is an excellent start to doing so and at the end of this video I'll even talk about how I'm going to extend this package in the near future just for you to make it even better all

**[0:01:18]** right so here we are in the GitHub repository for the self-hosted AI starter kit by n8n now this repo is really really basic and I love it there are basically just two files that we have to care about here we have our environment variable file where we'll set credentials for things like

**[0:01:34]** postgress and then we have Docker compose the caml file here where we'll basically be bringing in everything together like postgress quadrant and olama to have a single package for our local AI now the first thing that I want to mention here is that this read me has instructions for how to install

**[0:01:50]** everything yourself but honestly it's quite lacking and there's a couple of holes that I want to fill in here with ways to extend it to really make it what I think that you need and so I'll go through that a little bit and we'll actually get this installed on our

**[0:02:02]** computer now there are a couple of dependencies before you start basically you just need git and Docker so I'd recommend installing GitHub desktop and then Docker desktop as well because this also has Docker compose with it which is what we need to bring everything together for one package so with that we

**[0:02:18]** can go ahead and get started downloading this on our computer so the first thing you want to do to download this code is copy the get clone command here with the URL of the repository you'll go into a terminal then and then paste in this command for me I've already cloned this

**[0:02:32]** that's why I get this error message but you're going to get this code downloaded on your computer and then you can change your directory into this new repository that you've pulled and so with this we can now go and edit the files in any editor of our choice I like using VSS

**[0:02:46]** code and so if you have VSS code as well you can just type in code Dot and this is going to pull up everything in Visual Studio code now the official instructions in the readme that we just saw would tell you at this point to run everything with the docker compos post

**[0:03:00]** command now that is not actually the right Next Step I'm not really sure why they say that cuz we have to actually go and edit a couple of things in the code to make it customized for us and that starts with the EnV file so you're going to want to go into your EnV file I've

**[0:03:14]** just made a env. example file in this case because I already have my credentials set up so you'll go into your EnV and then set up your postgress username and password the database name and then also a couple of n8n Secrets these can be whatever you want just make

**[0:03:29]** sure that they are very very here and basically just a long alpha numeric string and then with that we can go into our Docker compose file and here's where I want to make a couple of extensions to really fill in the gaps so the couple of things that were missing in the original

**[0:03:42]** Docker compose file first of all for some reason the postgress container doesn't have the port exposed by default so you can't actually go and use postgress as your database in an NN workflow I think n uses postgress internally which is why it's set up like that initially but we want to actually

**[0:03:59]** be a to use postgress for our chat memory for our agents and so I'm going to show you how to do that basically all you have to do is go down to the postgress service here and then just add these two lines of code right here ports and then just a single item where we

**[0:04:14]** have 5432 map to the port 5432 inside the container and that way we can go Local Host 5432 and access postgress so that is super super important otherwise we won't actually be able to access it within an NA end workflow we're going to be doing that later when we build the

**[0:04:30]** rag AI agent now the other thing that we want to do is we want to use olama for our embeddings for our Vector database as well now the base command when we initialize olama is just this part right here so we sleep for 3 seconds and then we pull llama 3.1 with oama so that's

**[0:04:48]** why we have llama 3.1 Available To Us by default but what I've added here is another line to pull one of the olama embedding models and we need this if we want to be able to use AMA for our Rag and so I've added this line as well

**[0:05:03]** that is very very key so that is literally everything that you have to change in the code to get this to work and I'll even have a link in the description of this video to my version of this you can pull that directly if you want to have all the customizations

**[0:05:15]** that we just went over here and with that we can go ahead and actually start it with Docker compose and so the installation instructions in the readme are actually kind of useful here because there's a slightly different Docker compose command that you want to run based on your architecture so if you

**[0:05:29]** have a Nvidia G you can follow these instructions which are a bit more complicated but if you want to you can and then you can run with a GPU Nvidia profile and then if you are a Mac User you follow this Command right here and then for everyone

**[0:05:42]** else like what I'm going to use in this case even though I have a Nvidia GPU I'll just keep it simple with Docker compose d-profile CPU up and so we'll copy this command go into our terminal here and paste it in and in my case I have already created all these

**[0:05:57]** containers and so it's going to run really really fast for me but in your case it's going to have to pull each of the images for olama postgress n8n and quadrant and then start them all up and it'll take a little bit because I also have to do things like pulling llama 3.1

**[0:06:11]** for the old llama container and so in my case it's going to blast through this pretty quick because it's already done a lot of this I did that on purpose so it can be a quicker walkthrough for you here um but you can see all the different containers the different

**[0:06:22]** colors here that are running everything to set me up for each of the different services and so like right here for example it pulled llama 3.1 and then right here it pulled the embedding model that I chose from AMA as well um and so at this point it's basically done so I'm

**[0:06:37]** going to pause here and come back when everything is ready all right so everything is good to go and now I'm going to actually take you in a Docker so we can see all of this running live so you're going to want to open up your Docker desktop and then you'll see one

**[0:06:49]** record here for the self-hosted AI starter kit you can click on this button on the left hand side to expand it and then we can see every container that is currently running or ran for the setup so they're going to four containers each running for one of our different local

**[0:07:02]** AI services and we can actually click into each one of them which is super cool because we can see the output of each container and even go to the exec tab to run Linux commands within each of these containers and so you can actually do things in real time as well without

**[0:07:17]** having to restart the containers you can go into the postgress container and run commands to query your tables and stuff you can go into actually I'll show you this really quick you can go into the olama container and you can pull in real time like if I want to go to exec here I

**[0:07:32]** can do AMA pull llama 3.1 if I can spell it right 70b so I can pull models in real time and have those updated and available to me in n8n without having to actually restart anything which is super super cool all right so now is the really really fun

**[0:07:48]** part because we get to use all the local infrastructure that we spun up just now to create a fully local rag AI agent within n8n and so to access your new self-hosted n8n you can just go to Local Host Port 5678 and the way that you know that this is the URL is either through

**[0:08:06]** the docker logs for your n container or in the readme that we went over um that was in the GitHub repository we cloned and with that we can dive into this workflow that I created to use postgress for the chat memory quadrant for Rag and olama for the llm and the embedding

**[0:08:22]** model and so this is a full rag AI agent that I've already built out I don't want to build it from scratch just because I want this to be a quicker smooth walk through for you but I'll still go step by step through everything that I set up

**[0:08:33]** here and so that you can understand it for yourself and also just steal this from me CU I'm going to have this in the description link as well so you can pull this workflow and bring it into your own n8n instance and so with that we can go

**[0:08:44]** ahead and get started so there are two parts to this workflow first of all we have the agent itself with the chat interaction here so this chat widget is how we can interact with our agent and then we also have the workflow that is going to bring files from Google Drive

**[0:08:59]** into our knowledge base with quadrant and so I'll show the agent first and then I'll dive very quickly into how I have this pipeline set up to pull files in from a Google drive folder into my knowledge base so we have the trigger that I just mentioned there where we

**[0:09:13]** have our chat input and that is fed directly into this AI agent where we hook up all the different local stuff and so first of all we have our olama chat model and so I'm referencing llama 3.1 colon latest which is the 8 billion parameter model but if you want to do an

**[0:09:28]** AMA PLL Within the container like I showed you how to do you can use literally any olama llm right here it is just so so simple to set up and then for the credentials here it is very easy you just have to put in this base URL right

**[0:09:42]** here it is so important that for the URL you use HTTP and instead of Local Host you reference host. doer. internal otherwise it will not work and then the port for Alama is if you don't change it 11434 and you can get this port either in the Docker compost file or in the

**[0:10:01]** logs for the AMA container you'll see this in a lot of places and so with that we've got our llm set up for this agent and then for the memory of course we're going to use postgress and so I'll click into this and we're just going to have

**[0:10:13]** any kind of table name you have here and N will create this automatically in your postgress database and it'll get the session ID from the previous node and then for the credentials here this is going to be based on what you set in yourb file so we have our host which is

**[0:10:28]** host. doer. internal again just like with AMA and then the database name user and password all three of those you defined in your EnV file that we went over earlier and the port for postgress is 5432 and so with that we've got our local chat memory set up it is that

**[0:10:45]** simple and so we can move on to the last part of this agent which is the tool for rag so we have the vector store tool that we attach to our agent and then we hook in our quadrant Vector store for this and so we're just going to retrieve

**[0:10:58]** any documents based on the query that comes into our agent and then for the credentials for Quadrant we just have an API key which this was filled in for me by default so I hope it is for you as well I think it's just the password for the NN instance and then for the

**[0:11:13]** quadrant URL this should look very very familiar HTTP host. doer. internal and then the port for Quadrant is 6333 again you can get this from the docker compose file because we have to expose that Port make it available or you can get it from the quadrant logs as well

**[0:11:30]** and so one other thing that I want to show that is so so cool with hosting quadrant locally is if you go to local hostport 6333 like I have right here you can see in the top left slash dashboard it's going to take you to your very own

**[0:11:46]** self-hosted quadrant dashboard where you can see all your collections your knowledge base basically and you can see all the different vectors that you have in there you can click into visualize and I can actually go and see all my different vectors which this is a document that I already have inserted as

**[0:12:02]** I was testing things um so you can see all the metadata the contents of each chunk it is so so cool so we'll go back to this in a little bit here but just know that like you have so much visibility into your own quadrant instance and you can even go and like

**[0:12:15]** run your own queries to uh get collections or delete vectors or do a search uh it's just really awesome so yeah hosting quadrant is a beautiful thing um and so with that we have our quadrant Vector store and then we're using olama for embeddings using that embedding model that I pulled that I

**[0:12:32]** added to the docker compost file and then we're just going to use llama 3.1 again to parse the responses that we get from rag when we do our lookups so that is everything for our agent and so we'll test this in a little bit but first I want to actually show you the workflow

**[0:12:47]** for ingesting files into our knowledge base and so the way that works is we have two triggers here basically whenever a file is created in a specific folder in Google Drive or if a file is updated in that same folder we want to run this pipeline to download the file

**[0:13:04]** and put it into our quadrant Vector database running locally and so that folder that I have right here is this meeting notes folder in my Google Drive and specifically the document that I'm going to use for testing purposes here is these fake meeting notes that I made I just generated something really really

**[0:13:21]** silly here about a company that is selling robotic pets and AI startup um and so we're going to use this document for our rag I'm not going to do a bunch bunch of different documents um because I want to keep this really simple right now but you can definitely do that and

**[0:13:34]** the quadrant Vector database can handle that but for now I'm just using this single document and so I'll walk through step by step what this flow actually looks like to ingest this into the vector database and so first of all I'm going to fetch a test event which is

**[0:13:48]** going to be the creation of this meeting Note file that I just showed you and then we're going to feed that into this node here which is going to extrapolate a couple of key pieces of information including the file ID and the folder ID and so once we have that I'm going to go

**[0:14:04]** on to this next step right here and this is a very very important step okay let me just stop here for a second there are a lot of rag tutorials with n8n on YouTube that miss this when you have this Step at the end here I'm just going

**[0:14:18]** to skip to the end really quick whether this is super base quadrant pine cone it doesn't matter when you have this inserter it is not an upsert it is just an insert and so what that means means is if you reinsert a document you're actually going to have duplicate vectors

**[0:14:34]** for that document so if I update a document in Google Drive and it reinserts the vectors into my quadrant Vector database I'm going to have the old vectors for the first time I ingested my document and then new vectors for when I updated the file it does not get rid of the old files or

**[0:14:51]** update the vectors in place that is so important to keep in mind and so I'm giving a lot of value to you right here by including this node and it's actually custom code because there's not a way to do it without code in n8n but it is all

**[0:15:05]** good because you can just copy this from me I'm going to have a link to this workflow in the description like I said so you can just download this and bring it into your own n8n take my code here which basically just uses Lang chain to connect to my quadrant Vector store get

**[0:15:19]** all of the vector IDs where the metadata file ID is equal to the ID of the file I'm currently ingesting and then it just deletes those vectors so basically we clear everything that's currently in the vector database for this file so that we can reinsert it and make sure that we

**[0:15:36]** have zero duplicates that is so so important because you don't want different versions of your file existing at the same time in your knowledge base that will confuse the heck out of your llm and so this is a very very important step and so I'll run this as well and

**[0:15:51]** that's going to delete everything so I can even go back to quadrant here go to my Collections and you can see now that this number was nine when I first showed this quadrant dashboard and now it is zero but it's going to go back up to 9 when I finish this workflow so next up

**[0:16:06]** we're going to download this Google drive file nice and simple uh then we're going to extract the text from it and so this it doesn't matter if it's a PDF a CSP a Google doc it'll take the file and get the raw text from it and then we're

**[0:16:21]** going to insert it into our quadrant Vector store and so now I'm going to run test step here and we're going to go back to the UI after it's done doing these insertions you can see here nine items because it chunked up my document so we go back here and I'll refresh it

**[0:16:36]** right now it's zero I'll refresh and there we go boom we're back up to nine chunks and the reason there's so many chunks for such a small document is because if we go to my chunk size here in my recursive character text splitter I have a chunk size of 100 so every

**[0:16:51]** single time I put in a document it's going to get split up into 100 character chunks so I want to keep it small just because I'm running llama 3 .1 locally I don't have the most powerful computer and so I want my prompts to be small so I'm keeping my context lower by having

**[0:17:06]** smaller chunk sizes and not returning a lot of documents when I perform Rag and so the other thing that I wanted to show really quickly here is my document data loader and so or my default data loader I'm adding two pieces of metadata here the file ID and the folder ID the more

**[0:17:22]** important one right here is the file ID because that is how I know that a vector is tied to a specific document so I use that in that other step right here to delete the old document vectors before I insert the new one so that's how I make

**[0:17:36]** that connection there so that's kind of the most in-depth part of this walkthrough is how that all works and having this custom code here but just know that this is so so important so just take this from me I hope that it makes sense to an extent I spent a lot

**[0:17:48]** of time making this work for you um so yeah with that that is everything we've got our agent fully set up everything ingested in uh we have the document currently in the knowledge base CU I ran through that step by step and so now we can go ahead and test this thing so I'm

**[0:18:04]** going to go to the chat widget here actually I'm going to save it first and then go to the chat widget and then I'll ask it a question that it can only answer if it actually has the document in the knowledge base and can retrieve it so I'll say what is the ad campaign

**[0:18:17]** focusing on and because this is llama 3.1 running locally it's going to actually take a little bit to get a response because I don't have the BPS computer so I'm going to pause and come back when it has an answer for me all right so we got an answer from llama 3.1

**[0:18:31]** and this is looking pretty good it's a little bit awkward at the start of the response here uh but this is just the raw output without any instructions from me to the model on how to format a response and so you can very very easily fix this by just adding to the system

**[0:18:45]** prompt for the llm and telling it how to respond with the information it's given from rag but overall it does have the right answer and it's talking about robotic pets which obviously it is only going to get that if it's using regag on the meaning notes document that I have

**[0:18:58]** uploaded through my Google Drive so this is working absolutely beautifully now I would probably want to do a lot more testing with this whole setup U but just to keep things simple right now I'm going to leave it at this as a simple example um but yeah I would encourage

**[0:19:12]** you to just take this forward keep working on this agent and um yeah it's fully fully local it is just a beautiful thing so I hope that this whole local AI setup is just as cool for you as it is for me because I have been having a

**[0:19:25]** blast with this and I will continue to as I keep expanding on it so just just as I promised in the start of the video I want to talk a little bit about how I'm planning on expanding this in the future to make it even better cuz here's

**[0:19:36]** the thing this whole stack that I showed here is a really good starting point but there's some things I want to add on to it as well to make it even more robust things like redis for caching or a self-hosted super base instead of the vanilla postgress CU then it can handle

**[0:19:49]** things like authentication as well maybe even turning this into a whole local AI Tech stack that would even include things like the front end as well or maybe baking in best practices for red and llms or na end workflows for that to make this more of like a template as

**[0:20:03]** well to actually make it really really easy to get started with local AI so I hope that you're excited about that if you are or if you found this video just helpful in general getting you set up with your local AI Tech stack I would really appreciate a like and a subscribe

**[0:20:16]** and with that I will see you in the next video
