---
type: raw-transcript
title: "The Future of RAG is Agentic - Learn this Strategy NOW"
youtube_id: _R-ff4ZMLC8
url: https://www.youtube.com/watch?v=_R-ff4ZMLC8
slug: the-future-of-rag-is-agentic-learn-this-strategy-now
published: 2025-01-15
duration: "0:45:50"
fetched_at: 2026-07-21
immutable: true
---

## Transcript

**[0:00:00]** retrieval augmented generation has been the go-to way for feeding external knowledge into llms since the dawn of generative AI it is the classic method for turning an llm into an expert at something that you care about like your favorite agent framework or your Ecommerce store but if you've actually

**[0:00:18]** tried to implement rag before you definitely know its common pitfalls the things that make you want to pull your hair out like the wrong text being returned from the search and the llm completely ignoring the extra content that you give it the kind of things that make it so that even though rag seems

**[0:00:34]** logically sound to you in theory it just completely falls apart in practice and you are certainly not alone if you feel this way that's why there's so much research in the industry right now for how to do rag better and there are a lot of strategies out there like reranking

**[0:00:50]** query expansion rank normalization things that I'll cover in other videos on my channel but out of all of the strategies that I've researched and implemented myself a gentic rag is the most obvious it works the best and it's exactly what I'm going to show you how to do in this video I'll show you how to

**[0:01:08]** take standard Rag and then turn it into an agentic approach that actually delivers so you don't feel like throwing your computer out the window because nothing is working for your agent in the last video I showed you how to use crawl for AI an open- Source llm friendly web

**[0:01:23]** crawler to scrape entire websites super fast for Rag and we use the pantic AI docs as an example now we're going to take this much much further because we are going to ingest all of the documentation into a database for rag using super base then we'll use pantic

**[0:01:41]** AI to create this agentic rag agent leveraging our knowledge base and then finally we'll use streamlet to create a UI to interact with our agent very seamlessly through this I'll walk through what agentic rag is and why it solves the common pain points that we often see with rag all at the same time

**[0:01:58]** building a live example for us to see this in action so buckle up because I am shoving a lot of value into this video for you I'll even talk about things like quadrant versus superbase for rag how you can expand the heck out of this setup and also how you can try this

**[0:02:13]** agent for yourself right now with no setup so with that let's Dive Right In now the big question that I have to answer to really set the stage for the rest of this video where I do a deep dive into an agentic rag solution is what is a gentic rag and there are a lot

**[0:02:30]** of websites and articles and diagrams out through on the internet explaining it and the best one that I have found is this article on the we8 website which by the way we8 is a vector database platform and I'm not going to read through this entire article here but

**[0:02:44]** really it's these first two diagrams that I really really appreciate to help us understand what a gentic rag is and why it is useful because this first diagram which I'll zoom in on here is what is basic rag it explains this very clearly essentially you have a knowledge

**[0:03:01]** base made up of a bunch of documents you split them into chunks so that we have bite-size information to efficiently give to the llm and then we turn all of these chunks into vectors their mathematical representation using an embedding model and then we store that all in a vector database so essentially

**[0:03:18]** every chunk is turned into a large string of numbers in a vector that represents all of that information and then when a query comes in from the user when you're interacting with the agent that query is then turned into a vector representation just like the chunks were using the same embedding model and then

**[0:03:36]** using some mathematics under the hood some Vector math the query is essentially matched to the most relevant documents that are then given as context to the llm so essentially The Prompt is expanded to include whatever relevant context was retrieved from the vector database knowledge base and so you have

**[0:03:54]** something like here's the user question and then here's all of the relevant context for you to answer it essentially what the prompt then looks like for the llm which then gives the final response using all that information to augment its response that's why it's retrieval augmented generation and you can kind of

**[0:04:12]** see the downside to this it's what's what we call a onshot here where the vector database is retrieved from we give that extra context but then the agent can't actually reason about what it was given it can't decide oh this wasn't enough context so I need to look

**[0:04:28]** again or search in a new way there's no opportunity for the agent to actually improve upon whatever it got for that additional context and so that is what a gentic rag does let me zoom in a little bit on this diagram here this is a gentic rag the second diagram in this we

**[0:04:44]** article here that I absolutely love basically instead of just having rag be a oneshot here's some context from the vector database we actually create rag as tools for the agent to interact with which unlocks things like even being able to search through different Vector databases so an agent based on the user

**[0:05:03]** question can reason about where it will actually go to find the knowledge and you can have other tools that can search the knowledge in other ways and so you're giving the agent the ability to intelligently explore the data and not just work with what it's given in the

**[0:05:18]** first shot and that is the power of a gentic rag and I don't like these tool examples in particular because these don't really relate to the knowledge base but you can very much imagine other tools where maybe for the pantic AI documentation you would give it the ability to see the URLs for the pantic

**[0:05:35]** AI docs and actually pick to search in a specific page based on the title of the documentation page and that's actually something that we are going to be implementing and there's one other diagram that I really like as well which is this one and I think this this is

**[0:05:48]** very similar but it explains it very nicely as well because essentially you have your large language model layer here's your AI agent here are the tools that it has access to and the retrieval functions that actually go to things like the vector database s just one of the options you have all these other

**[0:06:02]** tool functions and action functions that can work with the knowledge base in other ways really allowing the AI agent to reason about how it is searching for the answer for the user and that's what makes it so much more powerful and hopefully this example that we're going to go through what we'll be building in

**[0:06:17]** this video will mil make this whole idea of a gentic rag super crystal clear for you all right so there are a few moving parts for building our agentic rag solution so I've created this simple and beautiful diagram here with the help with Claude to walk you through what

**[0:06:32]** we're going to be doing in this video together cuz I'm breaking it down step by step to make this entire process very digestible but then still by the end of this video we're going to have an awesome solution here and so the first thing that I'm going to be doing with

**[0:06:45]** the rag website crawler is essentially taking what we did in the last video with crawl for AI scraping the content of a bunch of websites and now actually putting it into a database so that we have our rag knowledge base and I'll do this before we're even doing anything with

**[0:07:02]** the database set up cuz I want to get into the code right away dive into the meat of it and so then once we have this script set up then we'll go over to super base do the very simple setup there I'll walk you through everything and then we'll run our script and then

**[0:07:14]** boom after these first two steps we have our knowledge base ready to go for an AI agent and then so naturally the next step is using pantic AI to create the foundation of our AI agent and we're actually going to start with just basic rag because I want to give you clear

**[0:07:30]** examples of when basic rag is enough versus when we need our agentic rag approach and so we'll we'll take these negative examples of when rag doesn't work and test it again once we move on to actually implementing a gentic rag so there's a couple new tools that we'll

**[0:07:46]** introduce here to make it a very robust solution and then after that I'll talk briefly about the streamlet UI and show you how I built that so that we have our interface and the entire time as we're doing our testing I'll be using the stream interface and then just reference

**[0:08:00]** ing it at the end showing the code off a little bit for that so that is our entire process breaking it down step by step let's dive right into it first things first if you want to try the exact agent that we're building in this video for yourself right now with no

**[0:08:14]** setup you can do that all you have to do is head on over to the automator live agent studio sign in you'll get some free tokens and I have the exact agent recovering in this video hosted right here so it's a really cool way to actually go and throw some of your

**[0:08:28]** questions at it explore pantic AI documentation and test out what we are building right here and it's really awesome because there's even some example questions for you to get started here everything like I have not changed the code at all like everything is the same so yeah in this case here I'm

**[0:08:42]** asking it for an example agent specifically calling out the weather agent that I know is in the pantic AI documentation and boom look at that we've got the full code example right from the documentation so yeah this agent is awesome it saves so much time having to scrunch the documentation

**[0:08:57]** because the agent is doing it for you with rag super neat all right let's get into coding our agentic rag solution so everything that we're going to create together here I will have in a GitHub repository that I'll have linked to in the description that is all the code

**[0:09:13]** that we are looking at right here so first of all to ingest our documentation into a knowledge base we've got this script right here everything that we currently see is just what we already did in the last video with crawl for AI and so we'll be expanding this to

**[0:09:26]** actually work with a database then we've got the SQL show how to run all this later to set up our database this is our pantic AI agent that we'll Build Together from scratch and then finally the streamlet interface I'll go over the code for this a little bit later as well

**[0:09:40]** and then we've got a nice read me in the repository to walk you through everything and how to set this up yourself as well and so going back to that diagram that I showed earlier I just showed you the code for every single step that we've got here so I'm

**[0:09:53]** going to break it up step by step and I'm going to make this as simple as I possibly can so in the last video on crawl for AI we covered this repo went through their documentation and some of their examples on Multi URL crawling to get it so that we could give all of the

**[0:10:09]** documentation Pages for pantic AI and actually get the contents of every single one of them super super quickly by doing parallel scraping on all these pages and so going back to the code that I've got right here that is what this script is doing so far so again this is

**[0:10:26]** mostly just what I coded up in the last video on my channel where we crawl in parallel all of these URLs that we fetch by getting all of the pantic AI documentation URLs from the sit map so this page right here lays out the entire directory of the pantic AI documentation

**[0:10:45]** so we just process that XML to get all of our URLs and then we crawl them all that's it and so now in this function we have a new step right here so after we crawl the page and get the markdown in the result here now we actually want to add it to our

**[0:11:03]** knowledge base so I'm zooming a little bit here focusing in on this function right here so this is not implemented yet in the script that is what we're going to add so after we get the content we now want to process it as in create the chunks get it ready to insert into

**[0:11:17]** our knowledge base and also Define all the metadata and things like that that we will get into so let's go ahead and do that now so I'm creating a new function here called process and store document that's what's called in our function and its job is to orchestrate

**[0:11:32]** everything that we need to get the information ready for the knowledge base so first of all we want to chunk our text and the reason for that is when we store our information in the database for llm knowledge we don't want to store a massive page just in one record for

**[0:11:48]** the llm to retrieve because if we have a documentation page that's like 50,000 words and we give that all to an llm at the same time that is going to overwhelm The Prompt and just make the llm super confused so we want to split up longer pages into smaller chunks so that the

**[0:12:04]** llm can retrieve the specific knowledge it needs from a piece of documentation without pulling in the entire thing so we chunk the text and we'll Define this function later and then in parallel we want to process all of these chunks so at the exact same time we're going to do

**[0:12:21]** what it takes to actually turn all these chunks into embeddings that we can put into our Vector database in this case using superbase and we'll do set up for that in a little bit and then the last thing that we need to do is store the chunks so we split them up we process

**[0:12:36]** them and then we store them super simple three-step process and so now all we have to do is Define all of these different functions for chunking processing and storing and so let's go ahead and do that right now so the first function that we want to Define is the

**[0:12:51]** one to chunk our text and the chunking can get a little complicated cuz there is a lot that goes into taking a single page and breaking up into smaller bites for the large language model while still respecting things like code blocks and paragraphs because think about it if we

**[0:13:07]** have to split a document at any given point we don't want to split it in the middle of a paragraph or the middle of a sentence or a code example we want it to preserve that so that one chunk has all of the information that it needs so you

**[0:13:20]** don't have to look at the start of a next chunk to finish the sentence or the paragraph or something like that and so because this is a little bit more complicated I actually used AI quite heavily to help me create this function and you can use that as a rule of thumb

**[0:13:33]** like anything that's a little bit more complex that I code here I definitely used AI to help me with and you can do the exact same thing so I'm not going to explain this function in a ton of detail but just know that I'm taking a single document turning it into bite-sized

**[0:13:48]** chunks and respecting code blocks and paragraphs when I do it and so the first thing I'm going to do is just Loop through all the text in the current chunk basically just defining the boundaries for it and so if we're at the end of the text we're just going to take

**[0:14:03]** what's left cuz we're at the end we're not going to split another time otherwise we're going to try to find a code block so because crawl for AI is returning markdown to us I know that this is the syntax represent the start and end of a code Block in markdown and

**[0:14:17]** so I try to find it and actually adjust the end to include the entire code block if I find one there and so that's how I respect code blocks and then I do the same thing for paragraphs and sentences as well and so that way at the very end

**[0:14:31]** of a chunk we are not split in the middle of a paragraph or a sentence or something like that and then we just extract the chunk and clean it up and so now at this point we have a final chunk that we can add on to our list of chunks

**[0:14:43]** and so when you combine all of these chunks together in this list that creates that full document so that's how we have basically just an array like if I go up to the top here this function returns a list of all the chunks that together make up the entire document

**[0:14:56]** that we just split up and then we'll just return all the chunks at the end so a little bit more complex but the idea is very simple uh you can very much see like we get the text and we're given back a list of chunks so that we can

**[0:15:09]** insert them one at a time in the knowledge base so that the llm doesn't get super confused pulling in the entire document at once when really it was just looking for a small portion of the knowledge in that page so that is our function to chunk our text and so at

**[0:15:24]** that point we've gotten past this right here in our main function do process and store every page so now the next thing we have to do is process each chunk and you'll see in a little bit what that actually entails here so first we're going to start by defining our data

**[0:15:39]** class that actually defines what information we get in a chunk when it is fully processed so we have the URL for the pantic AI documentation page we have the chunk number like maybe if we split the document into 10 different chunks this is chunk number two out of 10 and

**[0:15:55]** then we're going to give a title and a summary for every single chunk and this is is going to get into a gentic rag a little bit but if we have this extra context about what this chunk represents that's going to help the agent reason about when to use this specific piece of

**[0:16:09]** knowledge so more on that later then we have the actual content of the chunk some metadata we'll get into that as well and then finally we have our embedding this is what actually allows for reg where we have kind of the vector database part of what we're storing here

**[0:16:23]** where we can do that retrieval with Vector mathematics here so that's our process chunk and that's what we're going to use in this function right here to process our chunks so the job of this function is to take the Chunk in the Raw string format and turn it into this

**[0:16:39]** class right here with all that information I just went over so the first thing that we want to do is actually use a large language model to extract a title in summary from this chunk so we'll Define this function in a bit I just want to lay out this entire

**[0:16:52]** process first same thing with this next function we want to get the embedding so this is the actual Vector representation of the chunk content which is what we're going to use for rag um and then finally we will create the metadata for our chunk and so this includes things like

**[0:17:08]** the source and so really metadata is just additional information that you attach to the record so you can do specific filtering so for example I say that the source is pantic AI docs and the reason I do that is this actually makes it so I can use one database table

**[0:17:23]** for my knowledge base for many agents because if I have a pantic AI agent and then I have like a CW for AI agent and then a lang chain agent I can have them all use the same knowledge base but whenever I query the knowledge base for that specific agent I would just say

**[0:17:39]** give me the results from your search but only looking at the records where the source is pantic AI docs and so I can segregate my knowledge in a single table for multiple agents using metadata and I can also query based on time for example if I only want to search based on the

**[0:17:57]** records in the last day that were ingested in the last day I can do that with this craw that metadata so that's the importance of metadata it's super key to have good metadata because that gives you a ton of options it unlocks so much as far as additional filtering that

**[0:18:12]** you can do and that's a whole Advanced Concept in it of itself but I just wanted to include that here just to show that you can take filtering very far with Rag and then finally we're just going to return our process chunk so we have the URL at this point that was

**[0:18:25]** given into the function we have our chunk number that was also given in and then we have the title and summary that we extracted with a large language model the content the metadata and then the embedding that we created and so now we can Define the function to actually get

**[0:18:40]** the title and summary and so there's a nice little system prompt that I added here to instruct the large language model which I'm going to be using uh gbt 40 mini but we instructed on how to extract the title in summary and we're looking for a specific Json object so

**[0:18:53]** that way what we get back can be referenced in this way where we want the title that is extracted and then the summary that is extracted and so it's very simple we're just going to make a call with our open aai client that we're giving here where we are using GPT 40

**[0:19:08]** mini or whatever you define in your llm model environment variable so you can tweak this as well and then we give it the system prompt and then also the chunk just the first 1,000 characters that's all it needs to then create a title and a summary and we return a Json

**[0:19:22]** object as our response format and that is what we return so we just load it as Json whatever we get back from the LL M and that is going to again include our title and our summary very very simple and then if we encounter any errors we'll just return that we'll tell that

**[0:19:38]** to our terminal there so we know that there was some issue trying to actually process uh this specific chunk and then next we want to define a function to get the embedding and so this again is what we're going to be using for the actual basic rag when we want to do that search

**[0:19:53]** with ma Vector mathematics and so we're going to be using again the open AI client just using their text embedding 3 small model giving the text from the chunk and then just returning the embedding super simple function open AI makes it so easy to get our embeddings very very easily so that is that and

**[0:20:09]** then we'll just handle any errors as well just like we did before and if we do get an error we're just going to return a zero Vector here just that the process can continue but we at least have some value for the embedding there so that is it for processing a chunk now

**[0:20:23]** we can get on to our very last step here which is actually inserting chunks so we reference this function in our main procedure here to process and store our documents that is inserting a chunk this is where we actually put it into super base now everything that we are

**[0:20:38]** inserting here is not just for basic rag you'll start to see once we get into a gentic rag how some of the things that I'm inserting like the URL and the title and the summary can be used to understand the knowledge in more ways than just basic rag with the embedding

**[0:20:53]** so we have the embedding for basic rag but also this other information so that we can explore the knowledge in different ways and so we'll get into that a little bit first let's finish off this function here to actually insert this data into superbase so first we're going to create an object here which has

**[0:21:08]** all the data that we want to insert just based on the chunk here and then we're going to insert into the site Pages table so we'll create this in a little bit here this is the SQL to actually create this in super base but we're inserting this chunk into the table very

**[0:21:22]** very simple and it will just handle any errors and so that is everything we have now completed this script and there's a lot that went into this actually creating the AI agent itself is going to be much simpler but now we can get on to setting up our database tables and then

**[0:21:36]** running the script to create our knowledge base the sponsor of today's video is an open source platform called GPU stack and I'm super excited to bring this to you today because it is free to get started and solves a huge problem in the AI space which is scaling local Ai

**[0:21:52]** and trust me when you really start to build an application around local AI whether you have your machines hosted in the cloud or you built them yourself you're going to really need to think about how you manage your different gpus and all of the AI inference going on on

**[0:22:07]** your machines and that is what GPU stat can help you with because it is an open-source GPU cluster manager and it is phenomenal it supports any hardware that you could be running on you can dream of any large language model that's going to be accessible and it supports

**[0:22:23]** single node multi-gpu setups as well as multi- Noe setups now the obvious question is is why use a GPU cluster manager and the easy answer is if you have tried to use more than just one GPU for your local AI stack you know how important and difficult it is to monitor

**[0:22:41]** your GPU usage and also efficiently dish out the inference to your different resources and that is what GPU stack makes very easy it is so easy to monitor your gpus in the platform set up your clusters add gpus into them and just manage your entire local AI stack they

**[0:22:59]** have a open web UI like interface which is very very clean with a huge focus on doing all that monitoring and managing of your clusters and also you can set up your Stacks as open aai compatible endpoints so you can really hook in your clusters into any system you could dream

**[0:23:15]** of so I will have a link in the description to GPU stack I would highly recommend checking it out because as soon as you use local AI for an agent or an AI application for anything but just yourself you are going to need something GPU stack to monitor all your resources

**[0:23:32]** as you are scaling your application so we have just finished this step right here now it is onto the super base setup and then we can run the script to create our knowledge base and luckily what we just went over is actually the longest and most complicated part of this entire

**[0:23:46]** process once we actually have our knowledge base set up creating the agent interact with it is actually pretty simple and so let's head on over to superbase right here I'll assume that you already have a project created in superbase the rest of it I'll walk you through everything so this is the

**[0:24:00]** homepage for a superbase project once you have it set up all you're going to want to do to get things started is go on over to the SQL editor tab right here so you'll click on this and then you'll have this Blank Slate right here where you can paste in all of the code in the

**[0:24:16]** SQL script that I have in the repository so going back to our code here that is this so you're just going to want to copy this and I have this set up specifically for superbase including Ro level security policies as well and so then with this you'll just paste it in

**[0:24:31]** right here and then go ahead and click on run and so this is my first time setting up for the super base project so I am doing it completely from scratch with you right here and then once you have this run you can just go to the table editor here and then boom there we

**[0:24:46]** go we've got our site Pages table with nothing in it right now so now it is time to actually set up our environment variables including our superbase URL and service key so we'll insert that all in and then run our script to get everything in this table here and so

**[0:25:02]** first of all to actually get our superbase credentials you want to go down to the project settings in the bottom left here and then click on API what you're going to want to do is copy your superbase URL and then also your service Ro secret these are the two

**[0:25:17]** environment variables that we need to give our script so that it can actually insert the knowledge into the table the site Pages table that we just created so copy those two things and then head on over back to the code and open up your env. example file so you're going to

**[0:25:33]** want to take this rename it Tov like I did here I'm not going to show this file CU that actually has my credentials but you're going to want to take the superbase URL and service key that you just copied from the superbase UI and then paste those here you're also going

**[0:25:46]** to want to get your openai API key which I have instructions here on how to get it just right here in the. example and then Define the large language model that you want to use so in my case I'm using gbt 40 mini this is exactly the ID

**[0:25:59]** that you would just set it to right here to reference it and that's it we now have all the credentials set up and so we can go ahead and run the script that we just created and create our knowledge base over in the terminal now let's go ahead and run this so I have everything

**[0:26:13]** installed including my python libraries already I've got instructions in the Remy for how to do that with the requirements. text file so I'm in the current directory with that script that we just created and now all I have to do is run the command Python and then the

**[0:26:25]** name of the script crawl pantic a do and this is actually going to be quite chatty as it processes all of the chunks and sets them all in the knowledge base but it's kind of cool to see this all roll through and it's running in parallel in batches of I think 10 pages

**[0:26:41]** right now so and also batches of 10 chunks at a time but it's cool to see it make all the calls to open AI to get the titles and the embeddings and the summaries and the calls to superbase to insert into the knowledge base it's pretty neat so I'm going to pause and

**[0:26:54]** come back once this is done in just like 10 to 20 seconds all right there we go we are at the the end of our script and we have everything in our knowledge base now also if you run into any rate limit issues with open a or anything like that

**[0:27:06]** you can also just change the batch size and also add in some delays with the time python Library so play around with that if you have to I didn't run into any of that myself but I know some people did uh from my last video when I did this with crawl 4 AI so let me go

**[0:27:20]** out of this for now and then let's go over into our super base cuz we're going to check out all of the knowledge that we just added in so I'll go back over to the table editor here go to site Pages it says it's empty right now there we go

**[0:27:32]** now refresh we got 245 records so out of the 42 Pages for the pantic AI documentation that we scraped from this right here we turned it into 245 chunks and we've got the URL the chunk number the title and summary that was created for with gbt 40 mini for

**[0:27:51]** every single chunk the content metadata and then the embedding as well that's the massive Vector representation that we'll actually use for basic Rag and so with that we can now move on to our next step here U not this diagram this one which is creating the AI agent for basic

**[0:28:08]** Rags let's go over and do that now so this is super meta but we are building a pantic AI agent to be the pantic AI expert and so if you want help building agents like what I'm about to build right here you can literally refer to this agent to help you code your agents

**[0:28:24]** and also refer back to the pantic AI documentation and so yeah let's Dive Right into creating this agent here and so first of all we're going to start with just a basic rag example then we'll extend this exact same agent to do a lot of really cool stuff with a gentic rag

**[0:28:39]** so the first thing we're going to import all the python libraries that we need and then do some of that initial setup like loading our environment variables including the specific model that we want to use uh from open AI configuring log fire this is the login monitoring for pedantic AI which I'm just going to

**[0:28:55]** disable for now I'll set this up maybe in another video on my channel and showcase that and then we want to define the dependencies for our pantic AI agent so the way that you typically set up your agents with pantic AI is in three parts you have your dependencies which

**[0:29:10]** is things like the superbase client and the open AI client that your agent needs access to to use in the tools so that's number one then you set up the actual agent itself that's number two and then number three you define the tools for your agents so we're going to walk

**[0:29:24]** through all three of those so this is Step number one with the dependencies and then we're going to create our system prompt here and this is a pretty rough draft of a system prompt I haven't said too much in this here starting really really basic just describing what

**[0:29:39]** kind of tools it has what the role is of this agent even kind of pointing to some things that we'll have for agentic rag in a little bit here but you can just ignore that for now but anyway that's our system prompt and then we'll create our actual agents so step number two we

**[0:29:54]** Define the agent using the agent class from pantic AI we specify our model that we defined above with open AI we give it our system prompt we tell it the kind of dependencies that the agent will have access to and then also there's retry Logic for your llm calls baked into

**[0:30:09]** pantic AI as well which is super neat so we've already done step one and two with dependencies and the agent and now we can Define our first tool for the agent and that is going to be the tool for basic Rag and so before we even Define that I'm just going to throw in this

**[0:30:24]** function right here to get the embedding for the user's question so get the embedding for the user question and then use that to check the knowledge base with rag so this is basically just the same function that we created in this other script right here um so I'm not

**[0:30:39]** going to go over that again now we can Define our tool to retrieve relevant documentation this is basic reg in its finest so what we're going to start out with is a dock string here because in pantic AI this doc string that you have at the start of a function is how you

**[0:30:56]** tell the agent when and how to to use this tool that gives it all the context it needs like the arguments and the purpose of the function and the way that we turn this function into a tool for the agent is with this what's called a decorator right here so we put this at

**[0:31:11]** the start of our function where with the at symbol and then the name of our agent. tool that immediately turns it into a tool that's accessible for our pantic AI agent and we can continue on with the code for it here so first of all we're going to get the embedding for

**[0:31:26]** the user's query and we're also passing in that open aai client so that our agent has access to open AI to do this and then we are going to run this procedure here this is what actually does rag within our site Pages table so if I go back over to superbase here and

**[0:31:46]** I go to the script that we ran I'll just scroll down right here we have this function that we created called a match site Pages this is all the logic that happens in the database where we can give it a query the embedding for a query and it'll find the records in the

**[0:32:03]** site Pages table based on those embeddings that are the most similar so what we get back from running this is going to be the top and we default to 10 so the top 10 by default records that match the user's question the most and so back over to VSS code here actually

**[0:32:20]** I'm specifying the match count as five right here so I'm getting the top five most relevant document chunks and I'm also doing that metadata filter so I'm only going to be pulling Knowledge from this table here where the source is pantic AI docs and that way if I have

**[0:32:35]** other agents that are also storing knowledge in here I'm not going to overlap and accidentally pull Knowledge from those agents as well obviously right now the only records in this table are going to have the source of pantic AI docs but this is just a nice little value ad for you to show you how you

**[0:32:50]** could do something like this with metadata so pretty neat so now if there are no results that are returned to us we're going to tell that to the agent so that it can report report back to the user otherwise we're going to format all of the chunks so we're going to take the

**[0:33:03]** top five results put them all together into a nice string and then return that to the large language model so we're giving it a nice format so it can understand that oh this is chunk number one and this is chunk number two and so on and then we'll handle any errors as

**[0:33:17]** well so there's any issues when it's retrieving the documents we'll print that to our terminal and also report that back to the agent so again it can go back to the user and say oh sorry I had an issue trying to retrieve from the knowledge base obviously you don't want

**[0:33:30]** that to happen but yeah so that is our first tool that is very basic Rag and so now we can actually run this agent we don't have anything that is agentic rag at this point but we'll get to that but first I want to show you when basic rag

**[0:33:43]** works and when it does not all right so here we are in the streamlit UI chatting with the pantic AI expert that we just built I'll cover streamlit more at the end of this video but let's Dive Right into testing out this agent cuz I want to give you a good example of when basic

**[0:33:57]** rag is enough and then I'll show you an example where this falls apart and then we'll get into a gentic rag to actually fix that problem and so first I'll start with a very basic question what are the supported models and so this will do that retrieval it will perform rag to

**[0:34:13]** get me the answer here based on everything that we put in the knowledge base and there we go pantic AI supports and then it lists a bunch out and then it even says for specific model names here are a list of some of them so yeah this is a solid answer I very much

**[0:34:26]** pulled this from the knowledge base if you were to ask Claude or gp2 some agent that doesn't have access to this documentation it would completely bomb this question so that's awesome it's working pretty well now let's get to an example where just basic rag will not work if I go back to the pantic AI

**[0:34:45]** documentation let me actually go to that right here and I go to the examples they have this weather agent which is a really really awesome example I'd actually recommend checking this out if you want a good example maybe besides my videos of course on how to build a

**[0:34:58]** pantic AI agent I would reference this right here but if I go back over to the interface here and I ask it give me the weather agent example let me spell that right example from the documentation it's going to bomb this I've obviously tested this out a lot

**[0:35:16]** before I recorded this exact segment for you um I know that it doesn't get this right so it's giving the response here and it looks good so far but you can see that this is pretty bad like it kind of started correct but it's not defining the dependencies I mean this is just

**[0:35:32]** like a tiny script compared to what we actually have here in the weather agent it didn't really give me the example you can see that it obviously pulled some relevant information to get me a half decent answer but this still is not acceptable this doesn't actually give me

**[0:35:47]** everything that I need to go ahead and then just run this entire agent so that is why we need to move on to creating a gentic rag what we're going to be doing here is actually giving more tools to the agent so that not only can It perform rag with the embedding column

**[0:36:04]** that we have right here but it can actually pull a list of the URLs from the pantic AI documentation reason about what pages it might want to look at to get the right information and then actually go and visit those URLs and we can even have it for example use the

**[0:36:19]** title in summary to help it figure out which pages to visit as well and pull the content from so this is where we start to get into having the agent actually be able to reason about where it needs to look for knowledge instead of just performing basic Rags let's get

**[0:36:33]** into adding those tools so back over in our code let's add these tools for a gentic rag now before we even do that I just want to say that you could probably tweak the chunking strategy or the retrieval strategy to make it so that it could successfully answer that weather

**[0:36:48]** agent question with just basic rag I don't know for sure but there's so many ways to optimize Rag and other ways besides agentic rag but it still just gave a very clear example of how basic rag can fall apart especially when you have to look at bigger pieces of

**[0:37:03]** information to give a longer answer because typically with rag you're just looking at a tiny segment of the entire knowledge base but with a gentic rag we can actually instruct it on how to visit entire pages and pull all of that or parts of the page that it needs to

**[0:37:17]** answer a question and so the first tool that we're going to implement here we're just adding another tool is the one to list documentation pages so this is going to go to the database here here again we have a doc string to tell the agent when and how to use this tool but

**[0:37:31]** it's essentially just going to go to the site pages and pull all of the URLs and we're doing the metadata filter again just to make sure that we have just the pantic AI docs and nothing else we're pulling this list of URLs returning an empty list of URLs if nothing was

**[0:37:46]** returned otherwise we're giving these back to the llm so it now knows which URLs it can reason about potentially visiting to answer the user's question and then we'll also return an empty list if there's any errors as well well and I promis at the start of the video I would

**[0:38:00]** talk a little bit about quadrant versus super base as well so here's a really quick rundown of when to use either I like using superbase a lot because it simplifies things this is a very good example I have reg for this function right here and then also structur data

**[0:38:18]** that I have to store in a SQL database used in this function all in the same platform because I am using superbase quadron is just a vector database I can only store embeddings and so if I wanted to use quadrant in my solution I could only use it for basic Rag and then when

**[0:38:35]** I get into a gentic rag where I'm actually looking at structure data in a table I would still have to use super base so I'd actually be using both but with superbase I can have the rag and the structured data all in one place that's why I generally recommend

**[0:38:49]** superbase I will say though that quadrant is a lot faster so if I wanted to optimize for Speed here I actually would have all my knowledge embeddings stored in quadrant have this function reference quadrant instead of using superbase with this uh match site Pages function right here and then I would

**[0:39:08]** still also use superbase and have the table for all of the metadata and things like that like the title and the summary and the URL everything that I'm referencing in this function so that's a quick little rundown there now let's get into the second function right here so

**[0:39:22]** now that we have the ability for our llm to get all of the URLs we obviously need to give the ability to get the contents of a specific page that it wants as well so again another doc string here telling when and how to use this function all

**[0:39:35]** we're going to do is query the site pages and grab the title content and chunk number from a specific URL and then we're going to return that to the llm or maybe just say no content found for the URL if it doesn't find anything and then handle any errors as well um

**[0:39:51]** yeah last thing here we'll also do some formatting here just to make the information nice and easy to understand for the llm also combining all the chunks together uh for that single page so this way the llm can now read from an entire page and this is going to improve

**[0:40:06]** the performance of some of the more complex questions because now we are implementing a gentic rag instead of just a basic query using embeddings we're actually giving the agent the ability to look at the URLs and think oh if they're asking for the weather agent example and there's literally a page

**[0:40:22]** where it's you know like pantic AI do/ examplee agent oh I should probably go visit that pull all the contents from it and then use that to answer the user question instead of that little bit of knowledge I might retrieve with basic rag that doesn't actually cover the full

**[0:40:36]** example and so with that let's go ahead and run this again and test it out so back in the streamlet UI let's go ahead and ask that Infamous question that it botched the first time I'll say give me the weather agent example code from the documentation all right so it probably

**[0:40:53]** will start with basic rag still because I instructed to do that in the system prompt but then as a part of the reasoning here I'll instruct it to then go on to actually check the URLs pull the right page and then boom look at this we are definitely getting the full

**[0:41:06]** example now and I can even open up my terminal and see that it did start by retrieving relevant documentation basic rag figured out that didn't give it the right answer so it went on to list the document Pages found the right one so it called the tool to get the page content

**[0:41:21]** and now that gives us the full response here even including yeah like literally everything the main function the tools defining the agent this is the full example for us so now we have much better results because the agent can actually reason about the knowledge base and not just do a one shot rag query

**[0:41:38]** last but not least I wanted to cover the streamlit user interface very quickly here because I set this up as a way to use streamlet to really chat with any pantic AI agent so it's pretty neat and I don't want to code this from scratch with you right now um because the big

**[0:41:52]** focus of the video is everything with agentic Rag and this is just the way for us to talk to the agent but I wanted to to show this off very quickly here and this is also in the GitHub repository so you can use this to chat with this agent

**[0:42:04]** or hook it into the live agent Studio like I've showed in other videos on my channel and you can use this to really work with any pantic AI agent with streamlet because essentially I have these functions here that convert the text from this the pantic AI format to

**[0:42:18]** what I can display in streamlet and then I have my main function where I actually invoke my agent here and I pass in the dependencies that I set up on the streamlet side so I give all of the dependencies like the superbase client and the open AI client into my agent

**[0:42:33]** right here get the response and then I actually stream this out so instead of it being just like boom here's all the text at once it streams it out in typewriter style like we like to see with interfaces like you know chat gbt docomo messages in the message history

**[0:42:48]** so the agent when it calls reg and it gets the context for a specific part of the pantic AI documentation that is now a part of the message history so it can even reference that later on as well so it doesn't have to pull that page a second time so it's pretty neat yeah

**[0:43:03]** overall it's a pretty concise function here we got the main function where we set up all the messages in the UI get the user input and then handle that whenever the user inputs something we add it to the conversation history and then we stream the response from the

**[0:43:16]** agent which also adds the AI messages and the tool messages to the message history all in the format that works for pantic AI so again I'm not going to dive super super deep into the script but you have that there for you the main thing that I really wanted to focus on was

**[0:43:31]** this agent right here which by the way if you want to expand on this there's so many ways to even for this specific example to add a lot of new tools to make this even more robust than it already is for example I'm just throwing out something really random here you

**[0:43:47]** could set up a dedicated knowledge basis specifically for pantic AI examples and then you could have a function that is using regag but just for the pantic AI examples so that way when a user asks for an example you're going to get more accurate results actually fetching an

**[0:44:05]** example instead of the agent maybe accidentally looking somewhere else in the pantic AI documentation that doesn't actually have full examples maybe they're just like short little clips of code and that's not what the user wants when they want a full example um and so that kind of goes back to the Wei

**[0:44:18]** article where you can have different knowledge stores that have and have the agent actually intelligently reason about where it wants to go so that's just one example um or you could even have another area of the pantic AI document like maybe you reference the actual code in the GitHub repository and

**[0:44:34]** that could be its own knowledge base and you could have listing and fetching functions for getting specific content in the GitHub repo to actually dive into the code there's so many ways that you could expand a gentic rag here like I'm not promising that what I have set up

**[0:44:48]** here is going to work perfectly um because in the end there's so many different opportunities to make this better and better that is a wrap for building an agentic rag solution that actually soles solves a lot of problems we typically see with Rag by giving your llm the ability to reason about where

**[0:45:03]** and how to get the right information from your knowledge base you get much more consistent and accurate results and of course this is just one way to level up your rag game there are so many different strategies out there and also ways to build on top of a gentic rag and

**[0:45:17]** my solution like I covered earlier in this video the main thing that I just really wanted to drive home here is the importance of giving your agent the ability to intelligently Leverage your knowledge base instead of those one-hot queries that you have to get out of your system and I'll be putting out a lot

**[0:45:34]** more content on Rag and AI agents on my channel going forward as well so stay tuned for that if you appreciated this video and you're looking forward to more things Rag and AI agents I would really appreciate a like and a subscribe and with that I will see you in the next

**[0:45:48]** video
