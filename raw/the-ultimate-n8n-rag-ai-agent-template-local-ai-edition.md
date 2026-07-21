---
type: raw-transcript
title: "The ULTIMATE n8n RAG AI Agent Template - Local AI Edition"
youtube_id: T2QWhXpnT5I
url: https://www.youtube.com/watch?v=T2QWhXpnT5I
slug: the-ultimate-n8n-rag-ai-agent-template-local-ai-edition
published: 2025-03-05
duration: "0:32:41"
fetched_at: 2026-07-21
immutable: true
---

## Transcript

**[0:00:00]** retrieval augmented generation is the most widely adopted method to give agents access to your knowledge base essentially making them domain experts on your documents for Q&A the big problem is though that Rag by itself is oftentimes not powerful enough and so that's why on my channel over the last

**[0:00:18]** month I've been teaching a lot on a gentic rag which is one of the most powerful ways to level up rag making it more powerful and more flexible to work with the different types of documents that you have recently I showcased my n8n agentic rag AI agent template which

**[0:00:33]** you can download for free right now and is a great starting point for you to build your own agentic rag system with no code however on this video an overwhelming number of you asked for me to make a local AI version of this agent I mean it literally felt like over half

**[0:00:48]** the comments on this video were you guys asking for this like hey Cole this is cool and all but can you just skip to the part where you make everything local and I was secretly hoping for this because I truly believe that local AI where you control all of your data and

**[0:01:01]** your llms is the direction we need to head for generative AI as a whole so right now I'm introducing you to the local version of this n8n agentic rag template I'll walk through the workflow use cases it covers and show you how to set up everything that so that you have

**[0:01:16]** your own 100% offline secure and Powerful rag agent and there are some quirks with working with local llms and NN that I'll cover later in this video to save you a huge headache so definitely stick around for that so in the last video on my channel Channel when I covered the cloud version of this

**[0:01:32]** template I obviously talked a lot about what a gentic rag is and why it is so powerful but since then I've come up with an even better way to explain it to make it clearer and more concise for you and that's using this article from we V8 so great resource that I'll have Linked

**[0:01:47]** In the description of this video diving into what naive rag is or traditional Rag and then taking a look at how it's evolved into a gentic rag and so they have a couple of these diagrams that I want to go over right here which will arm us with information to then go into

**[0:02:01]** the na workflow and understand everything there the first diagram here is an example of naive or traditional Rag and we'll see how this levels up later to a gentic rag so how this works is you take all of your documents you split them into chunks so you have

**[0:02:15]** bite-size information to feed into an llm and then you use an embedding model to turn all that information into vectors to store into a vector database like superbase quadrant or pine cone and then you take the user's question when these queries come in and you use the same embedding model to turn the

**[0:02:31]** question into a vector as well so you can use some Vector mathematics behind the scenes to match the question with the document chunks that have the most relevant information and then all of that is combined together into a single prompt for the llm so you're giving it something like a system prompt with

**[0:02:46]** instructions the user question and then the relevant chunks that were received and then hopefully the response that you get back from the llm has the answer because the chunks had the right information to answer the question now the problem with all of this is it is considered a one shot you look up

**[0:03:02]** information in the vector database and you do it only one time and there's only ever the opportunity to do it once the large language model at the bottom here never has the chance to think to itself oh I actually want to reward the user's question or maybe there's a different

**[0:03:15]** Vector database I want to search or maybe I want to look at the data in a different way it has no way to reason about how it explores the knowledge base and so that is when we want to graduate to a gentic rag Now we move on to this

**[0:03:28]** diagram where we have an implementation of a gentic Rag and the tools we see here don't correspond exactly to what I have in my n8n workflow but that's just because there are different ways to implement a gentic rag and so both this and my n workflow are good examples and

**[0:03:41]** this still illustrates what I'm trying to show very clearly and so instead of there being a retrieval before we reach the llm with agentic Greg the agent comes first and then it has tools available for it to perform Rag and then also this is a very key thing explore

**[0:03:57]** the knowledge base in other ways and so in this example it can search through multiple Vector databases and it can decide when it wants to look in each one so we have a lot more reasoning baked into this whole retrieval process and it has other tools like web search to look

**[0:04:12]** up information in different ways and like we'll see in my n8n workflow we can also look at the knowledge base in different ways so we aren't just always doing a retrieval based on Vector mathematics an endless amount of possibilities available to us for the different ways you look at a knowledge

**[0:04:25]** base using the agent to reason about that instead of there just being some kind of precursor workflow to to take information from a vector database and dump it into the agent and so that is what agentic rag is as a whole now we can dive into our workflow armed with

**[0:04:39]** this information and take a look at our specific implementation so here is the full local agentic reg n8n template and you'll notice that this is very similar to the cloud version that I built recently on my channel I'm doing that very intentionally because don't fix what ain't broken right like if I gave

**[0:04:57]** you a good template as I promised then when we go to the local version we want to keep it as similar as possible and just switch to the local AI services like olama and a self-hosted super base and so that's what we're doing right here and what makes this agentic regag

**[0:05:11]** let me zoom in on the agent tools here we are giving the agent the ability to explore the knowledge base in different ways with all of these tools that we have to interact with postgress which this can be vanilla postgress or self-hosted super base as well for a

**[0:05:24]** local implementation and so let's just go through some examples right now and see what this looks like watch it leverage these different tools to answer questions that naive rag usually wouldn't be able to buy itself so for our testing here the local llm that I'm using is quen 2.51 14b so a relatively

**[0:05:42]** small model and I have a version with an 8,000 token context limit that'll show you how to set up later because olama by default limits you to only 2,000 tokens which is not enough for systems like this and so that's one of the big headaches that'll help you solve later

**[0:05:57]** on but right now let's just go ahead and test this out so I want to ask it a few questions to force it to use these different tools to explore the knowledge base in different ways based on the question that we're asking so I have Claude uh generate all this fake data

**[0:06:12]** for a maritime tech company and so for the first test I just want to do a basic rag retrieval so scrolling down here I just want to ask it who the CEO of this company is and so I'm expecting it to use this tool on the right for a simple

**[0:06:25]** rag lookup because there's nothing more complex it's a very basic question let's just test it simple at first I'll just ask who is the CEO of the company and we can see with the N end workflow as it decides to use these tools we have the green box around it so in this case it

**[0:06:41]** didn't decide to use these other tools that we have for it like listing documents getting file contents querying our rows but it did do the rag lookup and it got us the right answer Dr Alisa vanderhoven that is the correct answer now for the second test I want to ask it

**[0:06:57]** a question where rag might work because I don't have very many documents in this test environment but it'd be the kind of question that rag could often get wrong so going back here I have a brand new chat end I'm going to ask it uh who was in the Feb 12th meeting and the reason

**[0:07:13]** I'm asking this is because when you have a ton of different meeting notes for different days in a knowledge base a lot of times rag does not do well because it pulls the information from the wrong meeting notes especially if the chunk for the attendees is far away from the

**[0:07:28]** information that actually says the date of the meeting and so I'll ask it this and we'll see then instead of Performing reg hopefully we'll watch it use one of these other tools and yes sure enough it did so it used the tool to list all the documents available in the knowledge

**[0:07:42]** base and then based on those titles it picked a couple to read from to take in that entire document to use to answer our question and so hopefully what it picked to read from is yeah it picked to read the meeting minutes document that is if I go back here this one right here

**[0:07:57]** so our February 12th meeting and hopefully it should give us this list of attendees let's go back and see if we got the right answer and yes sure enough we did that is the right answer all right looking good and yep going back here that list corresponds exactly now

**[0:08:13]** for my favorite kind of test we're going to be testing with tabular data because rag usually does absolutely terribly with tables like this especially if we have more than just a test environment here where we have thousands of Records in our tables because one rag just pulls relevant chunks and those chunks might

**[0:08:30]** only be a part of the table so only even have all of the records available to do analysis like Computing the average overall rating for example and also llm suck at math so by themselves just looking at the data in a prompt it's not going to be able to calculate the

**[0:08:45]** average very well and so what I did with this template this tool right here actually allows the agent to treat Excel and CSV files as SQL tables so it can write SQL queries to do things like compute the average overall ratings let's just see that in action right here

**[0:09:01]** this is the kind of thing that rag would fail horribly with again especially if my tables were much larger and so I'll ask it what is the average overall score based on the customer feedback not perfect spelling there totally good doesn't really matter and we'll watch it use this tool that it hasn't yet because

**[0:09:18]** it's going to execute a SQL query and once it executes it I'll click into it so we can see it's not the most trivial SQL query so it's very impressive that llms can do this especially smaller ones like quen 2.51 14b I mean that's the best part of this whole thing is it's

**[0:09:33]** not even that big of an llm all right and there we go it executed the query took a little bit there so I had to pause and come back but yeah look at this is the query getting the average overall rating and the answer is 7.89 and that is the correct answer and it

**[0:09:48]** gave it back to us absolutely perfect and one thing I really do want to call out is that your results will be inconsistent depending on the local large language model that you use because as you're using these really really tiny ones of course the results are going to be a lot different than if

**[0:10:03]** you're using the cloud version of this template we're using all of these super powerful llms like Claude 3.7 Sonet or gbt 40 but it still is so cool the kind of power we can have with local Ai and with this whole setup we are 100% secure and offline that's the advantage of

**[0:10:19]** local Ai and so now I'm zoomed out here I want to walk through this entire workflow for you and show you how to set it up and I did build this to be a part of the local AI package that I've been working working on on my channel and so

**[0:10:31]** I have the Json workflow for this template for you to download available here in this repository but I will show you as we're setting up the credentials how you can hook up things outside of the local AI package as well as within it the sponsor of today's video is cesia

**[0:10:46]** and I am genuinely excited to bring them to you today CU they're making some big waves in the voice AI space there is no denying that AI is completely revolutionizing both voice content and products online education customer service spots audiobooks and even video games the need right now for natural

**[0:11:05]** sounding and responsive voice Tech is growing and growing but the big problem with most voice AI Solutions right now is they're too slow too unpredictable or too robotic and caresia is tackling all of those and they're doing it for voice agents voice cloning voice changing and text to speech they are also about to

**[0:11:23]** release Sonic 2.0 their next model that is a complete GameChanger it's based on a revolutionary State space model architecture and it delivers voices that are unbelievably realistic and even the previous version of their model was second place in a bunch of thirdparty evaluations only trailing behind open Ai

**[0:11:42]** and so who knows Sonic 2.0 might take the crown now and what makes sonic 2.0 so incredible is both the speed as low as 40 milliseconds for latency and unprecedented control to change things like emotions accents and speed with remarkable precision and then in the the cartisia playground you can clone your

**[0:12:01]** own voice with as little as 3 seconds of your audio it is just unbelievable and so I'm recording my voice right here I'll give it about 10 seconds and then we're going to have something that is just as good as other platforms like 11 lab it is just amazing so I'm going to

**[0:12:15]** stop it give my voice a name select my language and then clone it and then within a few seconds we'll have a voice that's ready for us to try out which you could also invoke through an API as well so I'm going to paste in a sample prompt

**[0:12:27]** just go ahead and listen to this gentic rag with local AI is an absolute Game Changer like that definitely sounds like me I am very impressed and with the two primary models in their family cesia is tackling all the major problems that we have with voice AI right now cuz they

**[0:12:42]** have Sonic Turbo when you want insanely low latencies and then Sonic 2 when you want a super controllable and very accurate and precise model so whether you are a Creator developer or business owner looking to leverage voice AI I would highly recommend checking out cartesia so I'll have a link in the

**[0:12:59]** description to cia. you can sign up for a free account right now to discover how powerful it is for yourself so the first step for really setting up any AI agent is getting your database ready and I make it really easy to do in this template and your database it's so important

**[0:13:14]** because it stores your conversation history and your entire knowledge base and so zooming in on the red box here I have a couple of nodes that you can run to create everything for you and so the first thing that you have to do is obviously set up your post grass

**[0:13:28]** credentials which I've shown how to do this for the local AI package before that's what I'm using right now so my host is DB that's how I reference the superbase database service in my Docker compos stack and then for the rest of the information you just get that from

**[0:13:42]** the environment variables that you set up in the local AI package so we have our database and user which is postgress by default you set your password and then the port for postgress is 5432 and then if you're not using the local AI package you can still do

**[0:13:56]** everything in this template you just have to change the host from DB to whatever your local hosted postgress or superbase host is and so once you have your credential set up you can automatically test it right here it looks good for me and then we can go on

**[0:14:10]** to executing our first table creation statement and that is the one to create our document metadata now I'll go into superbase quick and show you this the document metadata table shows the highlevel information for our documents this is how the llm is able to use that tool I'll go over to this right here use

**[0:14:29]** the tool to list the documents that are available in the knowledge base so it knows which ones to pull the entire content from when it wants to do that instead of reg and then we also have this schema column here that I'll get into more later for our table files we

**[0:14:43]** want to tell the llm The Columns that are available so it knows how to write those SQL queries to work with the column specifically for the file like customer feedback or the sales Pipeline and so that's what the metad data is for and then we have our table for document

**[0:14:57]** rows and so instead of cre creating a separate SQL table for every single tabular file that we have instead we're storing it all in the same table and we're using this row data Json B this is how no matter the structure of the table we're able to store all of the records

**[0:15:15]** right here in this column and so for one file we have these columns like the notes and the status and the cost and then going down to another CSV file that I put in here we have the date vessel ID vessel name so these files all have different structures but we can store

**[0:15:30]** them all in document rows like this and then we query just based on this row data column when the agent creates those SQL queries to analyze certain files like the maintenance records for example and so that's everything for creating your tables the other table that we have is the documents table and this is where

**[0:15:46]** we actually store our embeddings for regag and the cool thing about the postgress PG Vector store node this is our rag node it creates this table for us automatically so we don't even have to have a third node here to build this I will say that the text column that

**[0:16:03]** postgress creates in this table is different than if you're using the superbase vector node it uses a Content column so that's why I have one that's specifically called documents PG here so if you've followed my tutorials before and you've been using the superbase vector store node just know that you

**[0:16:18]** will have to recreate it because it is slightly different with postgress but I wanted to use postgress for this entire workflow because that way you aren't limited to superbase I know that superbase is preferred by most people but also postgress is a lot more lightweight so I wanted to cover both

**[0:16:33]** here now before we can run our agent now that we have our database set up we need to set up our knowledge base and we do that with this rag pipeline in the blue box this is the largest part of the workflow because what we're doing is we're taking our local files hence the

**[0:16:46]** local file trigger and adding them into our superbase or postgress knowledge base and so I already have this workflow executed here just so I can show you the inputs and outputs for all the nodes as we go through them really quick here and so we are watching for files that are

**[0:17:01]** added or changed you could add deleted if you want to as well I'm just keeping it simple and we're watching in this folder on our machine specifically and the reason that I picked this path is because using the local AI package I have this shared folder on my machine

**[0:17:15]** mounted onto the n8n container That's What It Is by default so it's probably the case for you as well so we have all of our test data some of which we saw earlier that is now all in the N8 end container and you do want to include these options as well for polling and

**[0:17:29]** files and folders otherwise this trigger will not work it'll just spin forever waiting for you to add or edit files and I have seen on Mac computer specifically sometimes that issue persists even with these options selected submit a bug to NN if you see that I know that is

**[0:17:43]** something that they are working on but anyway once we have this trigger then we have an event and path so the path of the file and then the event is either going to be change or add as in the file is created for the first time and then

**[0:17:55]** we're going to Loop right here just in case we are uploading more than $1 document at the same time so the rest of this workflow is going to be done for each file that we have uploaded or edited within that second of polling for the local files and so the first thing

**[0:18:10]** that we want to do is set the metadata here so our file ID which I'm just using the path since unlike Google Drive we don't really have a true ID and then for the file type and title just extracting those with a little bit of JavaScript from our path and then the first thing

**[0:18:25]** that I want to do before I even insert anything into the knowledge base is I want a clean slate if we have already added the file to the knowledge base at some point I want to delete everything and that's what I'm doing with these two nodes right here so I'm deleting all the

**[0:18:39]** old document records from the document PG table where we have our embeddings for reg and then I am also deleting for any table files all of the rows here in the document rows table and the reason I want to do this is I want to absolutely guarantee that when I update a file the

**[0:18:58]** knowledge base only only contains the updated information for that file and doesn't have anything from an old version hanging around that would definitely make the llm hallucinate so we're taking care of that and by the way for all of the postgress nodes in the rag pipeline the credentials are going

**[0:19:12]** to be the exact same ones that you set up when you did the database setup and so after that now we can get on to inserting our document metadata so this is our first insertion into the knowledge base where we are adding in this record just starting with the ID

**[0:19:26]** title and created ad and then the schema for the the tables will come later and so at this point we are just setting the title like you can see right there and then we move on to reading the file to disk and so we're bringing this file into our n8n instance so we can then

**[0:19:41]** extract the text from it and that's what we're doing in this fancier part of the workflow right here because based on the file that we are adding to our knowledge base we have to extract the content in different ways you can't read a PDF file the same way that you read a text file

**[0:19:55]** so we have this switch statement right here that based on the file type just looking at the extension from the file path if it's a PDF we go down one route if it's a CSV we go down another route and then if it's a text file we go down

**[0:20:08]** this bottom route like we see in my current execution and this bottom route is also the default and so if you have something like a markdown file it can also be handled as just a regular text file so we handle different file types as well and if you're curious if you go

**[0:20:22]** to open uh and go to a new node here and click on extract from file there are different file types that are orted from n8n so if you want to do something like HTML or Json you could expand this template to include those file types as well because you have all these

**[0:20:36]** different nodes to handle these different file types and so right here in this execution just very basic extract the document text so we take our file the binary data and we get the text from it to actually have that in the 8 end workflow for subsequent nodes and so

**[0:20:53]** we take that text and then we just dump it into our knowledge base we use the PG Vector store node to take all of the text split it into chunks and then put it in our knowledge base in the documents PG table right here and so for this we have to hook in a couple of

**[0:21:08]** things we have our AMA embedding model which I'm just using namic embed text that's the model that comes with the local AI package by default and then for the document loader here just using the default data loader super simple the one thing that I did add on to this though

**[0:21:23]** is I am adding metadata for this record including the file ID and file title and so these pieces information are available to us in the metadata jsonb and this is really important because when we do a rag lookup when this record is returned the metadata is included so

**[0:21:39]** the llm can actually use this information to cite its source like it can tell you that I got this information from the company overview text document so that's why we care about metadata and then finally for the text splitter here to take our document and turn it into

**[0:21:54]** individual chunks we're just using a basic recommended recursive character text splitter with a chunk size of 400 I got this as a recommendation in my last video specifically to use 400 so that is everything for a basic text document then for our CSV and Excel files we do

**[0:22:11]** something a little bit extra here because we have to insert the rows into the document rows table as well so first we extract from the Excel and CSV just like we would do with our text and PDF documents but we do two things in parallel first we insert the table rows

**[0:22:27]** so with a little bit of fan JavaScript here I take all of the data for each row and I insert them right here into the document rows so we have this Json B that has all of the column data for each row and then also what we want to do is

**[0:22:42]** add it into our knowledge base for regular rag cuz sometimes a rag lookup does actually work well with tables especially if you want to look up a specific row so even though we are primarily going to be using the rows to write SQL queries for our tabular data

**[0:22:55]** we still also want to add it in to the knowledge base just like our other more text based files and so we aggregate all of the rows together then we summarize it so that we have the text representation of the entire table and then just like with the text document we

**[0:23:10]** insert it all into postgress or superbase with the chunks and everything like that and then the final thing that we do is we set the schema as well and so this is within the documents metadata table we create the schema just extracting all of the columns from this

**[0:23:25]** file and then we update that record so we go back to document metadata remember earlier on in the workflow we already created this record it just didn't have the schema yet so now this is where we add in the schema so we say for customer feedback here are the columns available

**[0:23:40]** so you know how to write a SQL query to query this row data right here and that is it that is our rag Pipeline and so now you can literally just go and dump a bunch of files in this folder that's being watched and you can go into the

**[0:23:53]** executions Tab and watch it load each of these files individually into the knowledge base and it happens happens very very quick even with not a super powerful machine the namic Ed text model from Alama is super fast this trigger it'll instantly trigger unlike the Google Drive one where you have to pull

**[0:24:09]** every minute so within just like a few seconds you'll have a bunch of files already ready in your knowledge base ready to now chat with the agent and get it set up last but not least we get to set up our AI agent that's everything in the yellow and green boxes here and so

**[0:24:24]** first of all two triggers for this we have a chat trigger that's what gives us the ability to interact with it right in the n8n UI and then we also have a web hook so we can use our agent as an API endpoint and then I have this edit

**[0:24:36]** Fields right here just to standardize the input that comes from both of these triggers and then we get into our tools agent and I have a very basic system prompt here just telling it that it's a personal assistant who has these different tools for a gentic rig to look

**[0:24:50]** at the knowledge base in different ways and I give it some instructions on when to use the different tools as well and then for our chat memory here just very basic postgress chat memory same credentials you already set up and then it'll automatically create this n8n chat histories table just like it

**[0:25:05]** automatically creates the documents PG table for our embeddings and then for our chat model this looks a little weird here like why is there an open AI icon when it's all local AI don't worry this is using olama it's just within my open AI credentials I set the API key to

**[0:25:23]** whatever the heck I want it's olama it doesn't matter and then I change the base URL to point to my Lama container with the local AI package and then if you are using AMA host on your machine you would just change this to Local Host now the reason I have to do this the

**[0:25:38]** reason I can't just use the chat olama model node it's a weird glitch in NN where if you use this guy which I wish I could instead of the open AI one if you use this one you'll get an error whenever it invokes the rag tool and I've seen this on the community forums

**[0:25:55]** already it's something like expected string but received object or some kind of erid like that you'll get that when you use this guy so we can't use this for now and it's kind of unfortunate I'll expand on this more later so we just have to use the open AI one and

**[0:26:10]** then we can change the base URL and then it still will be able to dynamically load the models that we have pulled in olama so it still works pretty well and then for our tools here first we have reg just with our postgress PG Vector so just a very basic description for the

**[0:26:25]** agent to know when to use this tool you could probably expand this prompt just just like you could with really any of the prompts in this template it's just to get you started um but yeah then we have our table name documents PG limiting to four and then we're

**[0:26:36]** including the metadata as well things like the title and the file ID that I showed earlier so that the llm can cite its sources when it uses this rag tool and then for the embeddings just using AMA just like we saw in the rag pipeline same exact model and the credentials for

**[0:26:51]** this again you just reference the olama service if you are in the local AI package or you change this to Local Host if you you are using oama on your own machine and not within a container with the local AI package and then we have our last three tools here we have one to

**[0:27:07]** list our documents again going to the documents metadata table and so that just is a simple list over this table not much more than that and then the tool to get the contents of a specific file as well so we have this kind of fancy query here basically just going to

**[0:27:24]** the documents PG table that na creates for us taking all of the chunks for a single document and combining it together to get the full text for that document and then we have it parameterized here so the llm decides the file ID and then everything else is predefined in the SQL query here and

**[0:27:42]** then it's actually kind of different than the last tool here because for the querying the tabular data we allow the llm to completely generate the SQL query and this is where we might get a little bit more inconsistent results cuz we're requiring it to generate a whole query

**[0:27:57]** and sometimes smaller llms in particular can hallucinate bad queries but in the description for the tool here I give it some examples and I found that this helps a lot so the description of the tool this is given as a part of the prompt to the llm so we tell it how to

**[0:28:12]** use this tool when to use it and some examples of good queries taking advantage of this row data column so basically allowing it to understand how we have things structured in this document rows table so it can write good queries to reference all of this Json B properly and so that is everything for

**[0:28:29]** our tools the very last thing that I want to cover is that huge headache that I promis to save you cuz here's the thing olama models by default they only have a context length of 2,000 tokens and so what that means is as your prompts get longer as you include more

**[0:28:46]** information from your rag lookups you start to lose things like the system prompt and the tools instructions because all that stuff at the start of your prompt gets overridden by the things that are in the most recent part of the context window because that length is only 2,000 tokens and trust me

**[0:29:01]** you will go over 2,000 tokens for most use cases with AI agents and so looking at the chat AMA model node we do have the option here to change the context length right here in NN so yeah here's the default 248 we can change this to 8,000 or whatever but as we saw earlier

**[0:29:20]** we don't have the luxury to use the AMA chat model because of that glitch with Rag and so we have to use open Ai and just change the base you but it doesn't have an option here to change the context length like we have in ama maximum number of tokens that

**[0:29:35]** defines the max for the output that doesn't change the context links that doesn't work I did actually test that and so the solution here if you look at the models that I have for AMA I have the ones that I installed directly from olama and then I have these versions

**[0:29:50]** that I created that have 8,000 context as that parameter set for the model and so I'll show you how to do that right here so in the local AI package AG you can have your olama container up otherwise if you're running AMA locally you can just do this in the command line

**[0:30:05]** but what you want to do is create this thing called a model file and so I'm going to run this Command right here you're going to want to change the model ID or the context link just based on whatever you want to do for your use case and I'll show you the contents of

**[0:30:17]** this because essentially what we're doing is we're inheriting from the base model and then just changing the context link with this parameter right here and then the last command there's just two commands here and actually I have this as a comment in the docker compost file for the local AI package you can see

**[0:30:33]** copy those commands right there the last command is to create a version of the model you can name this whatever you want just based on the file model file in the current directory and so I'm not going to run this right here because I already have well I guess I did run it

**[0:30:47]** anyway it just recreated the model for me so now we have a version you can see that happened instantaneously because it doesn't have to redownload the model it'll use what you already have downloaded and then just make a new version that has that extra context length and so you can do an olama list

**[0:31:02]** and you'll see it just with all of your other models and so now we have a version of AMA that has an extra context link and that's what makes it not hallucinate completely when you actually start to get some of these tool invocations more data coming in from

**[0:31:16]** your knowledge base the context length is important it'll definitely go to Five 6 7,000 tokens as you're looking out your documents so that is everything for the local version of the n8n agentic rag template and just for fun let's give it another spin here so I'll just ask it

**[0:31:30]** another random question like what are areas for improvement something very general that we might actually wanted to look at multiple documents to get a good answer for us let's see what it does I'm actually super curious I've never asked it this question in particular um but yeah as this thing spins I just want to

**[0:31:44]** say that if you have any questions at all with this template as you're going over it as you're extending it to fit to your use case just let me know in the comments I always love to chat with you share ideas with you and just see what you're building as well and yeah look at

**[0:31:57]** this based on the information available Geographic expansion product enhancements yeah looks pretty cool this agent is just fantastic and a lot of things I want to do in the future as well to continue to expand it it is just crazy to me the kind of power we have

**[0:32:10]** these days for local Ai and no code and I hope that this n8n agentic rag agent can be a good example of that for you so please just take this template and run with it to build out your specific use cases and I would love to hear what you

**[0:32:23]** make as well also a lot more content coming out soon for local Ai and a local AI package so stay tuned for that if you appreciated this content and you're looking forward to more things local AI I would really appreciate a like and a subscribe and with that I will see you

**[0:32:38]** in the next video
